import base64
import json
import os
import re
import time
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
KNOWLEDGE_IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Knowledge_Pdf", "images")

_MIME_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".bmp": "image/bmp",
    ".webp": "image/webp",
}

# Module-level cache: path -> base64 string (knowledge reference images never change)
_IMAGE_CACHE: dict = {}


def _encode_image(path):
    if path not in _IMAGE_CACHE:
        with open(path, "rb") as f:
            _IMAGE_CACHE[path] = base64.b64encode(f.read()).decode()
    return _IMAGE_CACHE[path]


def _mime_for(path):
    """Return the correct MIME type based on the file extension."""
    ext = os.path.splitext(path)[1].lower()
    return _MIME_MAP.get(ext, "image/png")


def _img_block(path, mime=None):
    """Return an image_url content block for a given file path."""
    if mime is None:
        mime = _mime_for(path)
    b64 = _encode_image(path)
    return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}


def _call_with_retry(fn, retries=3, backoff=2):
    """Call fn() up to `retries` times, sleeping `backoff` seconds between attempts."""
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            if attempt < retries:
                print(f"Azure API error (attempt {attempt}/{retries}): {exc} — retrying in {backoff}s")
                time.sleep(backoff)
    raise last_exc


def _knowledge_blocks(filenames):
    """Return list of (label text block, image block) pairs for knowledge images that exist."""
    blocks = []
    for fname in filenames:
        path = os.path.join(KNOWLEDGE_IMG_DIR, fname)
        if os.path.exists(path):
            # Label each reference image with the parameter name derived from filename
            label = fname.replace(".png", "")
            blocks.append({"type": "text", "text": f"[Reference: {label}]"})
            blocks.append(_img_block(path))
    return blocks

def detect_part_type(image_path):
    """
    Classify the input engineering drawing / table image as one of:
      'plate', 'ubolt', or 'clamp'

    Decision is made purely from the input image — no reference images used.
    """
    with open(image_path, "rb") as f:
        input_b64 = base64.b64encode(f.read()).decode()
    input_mime = _mime_for(image_path)

    def _call():
        return client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are a Hexagon SmartParts specialist.\n\n"
                            "Look at the engineering drawing or data table in the image and decide "
                            "which of the four SmartPart categories it belongs to:\n\n"
                            "- plate     : flat rectangular steel plates with Width, Length, Thickness dimensions\n"
                            "- ubolt     : U-shaped or J-shaped threaded rod hardware (U-bolt / J-bolt)\n"
                            "- clamp     : circular pipe clamp hardware with bolt holes and sweep geometry\n"
                            "- lug       : straight pipe welding lug mounted on a straight pipe (parallel/perpendicular)\n"
                            "- elbow_lug : elbow lug mounted on a pipe elbow fitting with ElbowRadius and FaceToCenter\n\n"
                            "Reply with EXACTLY one word — no punctuation, no explanation:\n"
                            "plate   OR   ubolt   OR   clamp   OR   lug   OR   elbow_lug"
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{input_mime};base64,{input_b64}"}
                    }
                ]
            }],
            max_tokens=10,
        )

    response = _call_with_retry(_call)
    raw = response.choices[0].message.content.strip().lower()
    for valid in ("plate", "ubolt", "clamp", "elbow_lug", "lug"):
        if valid in raw:
            print(f"Detected part type: {valid}")
            return valid
    raise ValueError(f"Could not detect part type from image. Model replied: {raw!r}")


def extract_data(image_path, part_type=None):
    # Auto-detect part type from the image when not supplied
    if not part_type:
        part_type = detect_part_type(image_path)

    with open(image_path, "rb") as f:
        input_b64 = base64.b64encode(f.read()).decode()
    input_mime = _mime_for(image_path)
    input_block = {"type": "image_url", "image_url": {"url": f"data:{input_mime};base64,{input_b64}"}}

    if part_type.lower() == "plate":
        knowledge_imgs = [
            "plate_p5_img2.png",   # Width1 definition
            "plate_p5_img3.png",   # Length1 definition
            "plate_p5_img4.png",   # Thickness1 definition
        ]
        ref_blocks = _knowledge_blocks(knowledge_imgs)

        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "REFERENCE IMAGES below show the geometric meaning of each SmartParts parameter for plates:\n"
                    "- Width1: horizontal width of the plate (top view)\n"
                    "- Length1: vertical length of the plate (top view)\n"
                    "- Thickness1: plate thickness (side view)\n"
                    "Additional plates may have Width2/Length2/Thickness2 (second plate) and Width3/Length3/Thickness3 (third plate)."
                )
            },
            *ref_blocks,
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
            {
                "type": "text",
                "text": (
                    "Using the reference images above as your guide for what each parameter means geometrically, "
                    "extract plate specifications from the input table.\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row extract:\n"
                    "- name: Part identifier or size\n"
                    "- width1, length1, thickness1: primary plate dimensions\n"
                    "- width2, length2, thickness2: second plate dimensions (null if absent)\n"
                    "- width3, length3, thickness3: third plate dimensions (null if absent)\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"M10","width1":75,"length1":75,"thickness1":9,"width2":null,"length2":null,"thickness2":null,"width3":null,"length3":null,"thickness3":null}]'
                )
            }
        ]

    elif part_type.lower() == "ubolt":
        knowledge_imgs = [
            "ubolt_p4_img2.png",   # UBoltWidth
            "ubolt_p4_img3.png",   # UBoltCenterToEnd
            "ubolt_p4_img4.png",   # UBoltRodDia
            "ubolt_p4_img5.png",   # UBoltDia2 (inner curved diameter)
            "ubolt_p4_img6.png",   # UBoltDia2Start
            "ubolt_p5_img1.png",   # UBoltFlatSpot
            "ubolt_p5_img2.png",   # UBoltTopGap
        ]
        ref_blocks = _knowledge_blocks(knowledge_imgs)

        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "REFERENCE IMAGES below show the geometric meaning of each SmartParts U-Bolt parameter:\n"
                    "- UBoltWidth: center-to-center distance between the two vertical legs\n"
                    "- UBoltCenterToEnd: distance from bend center/bottom to the threaded rod tip\n"
                    "- UBoltRodDia: diameter of the rod stock (e.g. M8 → 8)\n"
                    "- UBoltDia2: inner diameter of the U-bolt curved section (pipe-facing bore)\n"
                    "- UBoltDia2Start: position along the leg where the curved section begins\n"
                    "- UBoltFlatSpot: flat section added at the top of the bend\n"
                    "- UBoltTopGap: gap clearance at the top of the U-bolt"
                )
            },
            *ref_blocks,
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
            {
                "type": "text",
                "text": (
                    "Using the reference images as your guide, extract U-Bolt specifications from the input table.\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, uBoltWidth, uBoltCenterToEnd, uBoltRodDia, uBoltDia2, uBoltDia2Start, uBoltFlatSpot, uBoltTopGap, isJBolt\n"
                    "- isJBolt: 1 if J-Bolt configuration, 0 otherwise.\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"DN15","uBoltWidth":34,"uBoltCenterToEnd":60,"uBoltRodDia":8,"uBoltDia2":21,"uBoltDia2Start":null,"uBoltFlatSpot":0,"uBoltTopGap":null,"isJBolt":0}]'
                )
            }
        ]

    elif part_type.lower() == "clamp":
        knowledge_imgs = [
            "clamp_p4_img4.png",   # Diameter1
            "clamp_p4_img5.png",   # Thickness1
            "clamp_p5_img1.png",   # Width1
            "clamp_p5_img2.png",   # Width2
            "clamp_p5_img3.png",   # Height1
            "clamp_p5_img4.png",   # Height2
            "clamp_p5_img5.png",   # Gap1
            "clamp_p6_img1.png",   # Gap2
            "clamp_p6_img3.png",   # Angle1
            "clamp_p6_img4.png",   # Pin1Length / Pin1Diameter
            "clamp_p8_img1.png",   # Offset1 (NumberOfBolts offset)
        ]
        ref_blocks = _knowledge_blocks(knowledge_imgs)

        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "REFERENCE IMAGES below show the geometric meaning of each SmartParts pipe clamp parameter:\n"
                    "- Diameter1: pipe outer diameter the clamp supports\n"
                    "- Thickness1: clamp body/plate thickness\n"
                    "- Width1: total wing width of the clamp (left wing + right wing, measured outer to outer)\n"
                    "- Width2: inner lug/bolt-area width\n"
                    "- Height1: distance from pipe centerline to top of clamp\n"
                    "- Height2: distance from pipe centerline to bottom of clamp\n"
                    "- Gap1: clearance gap at the top of the clamp split\n"
                    "- Gap2: clearance gap at the bottom of the clamp split\n"
                    "- Angle1: sweep angle of the clamp arc\n"
                    "- Pin1Length: stud/bolt pin protrusion length\n"
                    "- Pin1Diameter: stud/bolt pin diameter\n"
                    "- Offset1: bolt offset when NumberOfBolts > 1"
                )
            },
            *ref_blocks,
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
            {
                "type": "text",
                "text": (
                    "Using the reference images as your guide, extract pipe clamp specifications from the input table.\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, size, diameter1, diameter2, thickness1, thickness2,\n"
                    "  height1, height2, height3, width1, width2, rodTakeOut,\n"
                    "  gap1, gap2, angle1, pin1Length, pin1Diameter, offset1,\n"
                    "  numberOfBolts, multiQty, multiLocatedBy, multiLocation\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"DN15","size":null,"diameter1":21.3,"diameter2":null,"thickness1":4,"thickness2":null,'
                    '"height1":null,"height2":null,"height3":null,"width1":65,"width2":25,"rodTakeOut":null,'
                    '"gap1":15,"gap2":null,"angle1":null,"pin1Length":null,"pin1Diameter":null,"offset1":null,'
                    '"numberOfBolts":null,"multiQty":null,"multiLocatedBy":null,"multiLocation":null}]'
                )
            }
        ]

    elif part_type.lower() == "elbow_lug":
        knowledge_imgs = [
            "elbow_p4_img2.png",   # Local coordinate / lug shape overview
            "elbow_p4_img3.png",   # ElbowRadius: radius of elbow (red arc)
            "elbow_p4_img4.png",   # FaceToCenter: blue vertical arrow, long elbow
            "elbow_p5_img1.png",   # FaceToCenter: blue vertical arrow, short elbow
            "elbow_p5_img2.png",   # TopShape: 1=Curved, 2=Squared, 3=Rounded, 4=Chamfered
            "elbow_p5_img3.png",   # RodTakeOut: blue vertical arrow from pipe CL to top port
            "elbow_p5_img4.png",   # Angle1: arc sweep on curved top
            "elbow_p6_img1.png",   # Width1 (top) and Width2 (bottom) horizontal spans
            "elbow_p6_img2.png",   # Width2 labeled arrow at base
            "elbow_p6_img3.png",   # Angle2: left taper angle
            "elbow_p7_img1.png",   # Angle3: right taper angle
            "elbow_p7_img7.png",   # Gap1: gap between double lug components
            "elbow_p8_img5.png",   # Pin1Diameter / Pin1Length: pin through lug hole
        ]
        ref_blocks = _knowledge_blocks(knowledge_imgs)

        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "REFERENCE IMAGES below show the geometric meaning of each SmartParts Elbow Lug parameter:\n\n"
                    "BASIC ATTRIBUTES:\n"
                    "- RodDiameter: diameter of the rod; used by the part selection rule (does not affect graphics)\n"
                    "- PipeOD: outer diameter of the pipe the elbow lug is placed on\n"
                    "- ElbowRadius: radius of the elbow where the lug is mounted (red arc in reference)\n"
                    "- FaceToCenter: distance from elbow face to elbow center; equals ElbowRadius for short tangent elbows\n\n"
                    "LUG SHAPE ATTRIBUTES:\n"
                    "- TopShape: shape of lug top — 1=Curved, 2=Squared, 3=Rounded, 4=Chamfered\n"
                    "- Angle1: sweep angle of the curved top arc (positive, >90° and <270°; only when TopShape=1; default 180°)\n"
                    "- RodTakeOut: distance from horizontal pipe centerline to the top lug port\n"
                    "- Width1: top width of the lug (if zero, Width2 is used; if both zero, PipeOD is used)\n"
                    "- Width2: bottom width of the lug (if zero and Angle3=0, Width1 is used instead)\n"
                    "- Angle2: left side taper angle (positive, <30°; 0 = vertical)\n"
                    "- Angle3: right side taper angle (positive, <30°; overrides Width2 for tapered bottom point)\n"
                    "- Angle4: bottom taper angle (positive, <45°; default 45°; controls lug extension along pipe)\n"
                    "- Thickness1: thickness of the lug body\n"
                    "- Gap1: gap between components of a double lug (null = single lug)\n"
                    "- StiffenerOffset: stiffener offset from pin port center (double lug only)\n"
                    "- StiffenerHeight: height of the stiffener between double lug components\n"
                    "- StiffenerLength: length of the stiffener between double lug components\n"
                    "- Offset1: distance from top port to top of lug (used as eye radius when TopShape=1)\n"
                    "- ChamfLength: length of chamfered edges (only when TopShape=4)\n"
                    "- RadiusActual: required radius of the bottom arc of the elbow lug\n"
                    "- Pin1Diameter: diameter of the pin through the lug hole (0 = no pin drawn)\n"
                    "- Pin1Length: length of the pin (must be > Gap1 + 2*Thickness1)"
                )
            },
            *ref_blocks,
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
            {
                "type": "text",
                "text": (
                    "Using the reference images as your guide, extract Elbow Lug specifications from the input table.\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return ALL of the following fields:\n"
                    "- name, rodDiameter, pipeOD, elbowRadius, faceToCenter,\n"
                    "  topShape, angle1, rodTakeOut, width1, width2,\n"
                    "  angle2, angle3, angle4, thickness1, gap1,\n"
                    "  stiffenerOffset, stiffenerHeight, stiffenerLength,\n"
                    "  offset1, chamfLength, radiusActual, pin1Diameter, pin1Length\n\n"
                    "- topShape: integer 1=Curved, 2=Squared, 3=Rounded, 4=Chamfered\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"DN50","rodDiameter":16,"pipeOD":60.3,"elbowRadius":76.2,"faceToCenter":76.2,'
                    '"topShape":2,"angle1":null,"rodTakeOut":85,"width1":65,"width2":50,'
                    '"angle2":0,"angle3":0,"angle4":45,"thickness1":10,"gap1":null,'
                    '"stiffenerOffset":null,"stiffenerHeight":null,"stiffenerLength":null,'
                    '"offset1":null,"chamfLength":null,"radiusActual":null,"pin1Diameter":null,"pin1Length":null}]'
                )
            }
        ]

    elif part_type.lower() == "lug":
        knowledge_imgs = [
            "lug_p4_img2.png",   # Local coordinate system / port layout (Pin port, Route port)
            "lug_p5_img1.png",   # PipeOD: horizontal arrow = pipe outer diameter
            "lug_p5_img2.png",   # RodTakeOut: vertical arrow from pipe CL to top port
            "lug_p5_img3.png",   # IsPerpendicular: parallel (left) vs perpendicular (right) lug
            "lug_p6_img2.png",   # TopShape=1 Curved
            "lug_p6_img3.png",   # TopShape=2 Squared
            "lug_p6_img4.png",   # TopShape=3 Rounded
            "lug_p6_img5.png",   # TopShape=4 Chamfered
            "lug_p7_img1.png",   # Angle1: arc sweep angle at curved top
            "lug_p7_img2.png",   # Width1: top width of lug (horizontal arrow at top)
            "lug_p7_img3.png",   # Width2: bottom width of lug (horizontal arrow at bottom)
            "lug_p7_img4.png",   # Angle2: left side taper angle
            "lug_p8_img1.png",   # Angle3: right side taper angle
            "lug_p8_img6.png",   # StiffenerLength / double lug stiffener area
            "lug_p9_img1.png",   # Offset1: distance from top of lug to top port
        ]
        ref_blocks = _knowledge_blocks(knowledge_imgs)

        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "REFERENCE IMAGES below show the geometric meaning of each SmartParts Straight Pipe Lug parameter:\n\n"
                    "BASIC ATTRIBUTES:\n"
                    "- RodDiameter: diameter of the rod used by the pipe lug and the part selection rule\n"
                    "- PipeOD: outer diameter of the pipe the lug is welded to (horizontal arrow across pipe)\n"
                    "- RodTakeOut: distance from horizontal pipe centerline to the top lug port (vertical arrow)\n"
                    "- IsPerpendicular: 0 = lugs are parallel to pipe axis, 1 = lugs are perpendicular to pipe axis\n\n"
                    "SIDE ATTRIBUTES:\n"
                    "- TopShape: shape of lug top — 1=Curved, 2=Squared, 3=Rounded, 4=Chamfered\n"
                    "- Angle1: sweep angle of the curved top arc (positive, >90° and <270°; used only when TopShape=1)\n"
                    "- Width1: top width of the pipe lug (horizontal span at top)\n"
                    "- Width2: bottom width of the pipe lug (horizontal span at base)\n"
                    "- Angle2: angle of the left tapered side (positive, <30°; 0 = vertical)\n"
                    "- Angle3: angle of the right tapered side (positive, <30°; overrides Width2 for tapered bottom)\n"
                    "- Thickness1: thickness of the lug body\n"
                    "- Gap1: gap between components of a double lug (null = single lug)\n"
                    "- StiffenerOffset: distance the stiffener is offset from pin port center (double lug only)\n"
                    "- StiffenerHeight: height of the stiffener between double lug components\n"
                    "- StiffenerLength: length of the stiffener between double lug components\n"
                    "- Offset1: distance from top of lug to top port (used as eye radius when TopShape=1)\n"
                    "- ChamfLength: length of chamfered edges (used only when TopShape=4)\n"
                    "- Pin1Diameter: diameter of the pin/stud through the lug hole\n"
                    "- Pin1Length: length of the pin/stud through the lug hole\n"
                    "- Height2: height dimension of the lug base/plate"
                )
            },
            *ref_blocks,
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
            {
                "type": "text",
                "text": (
                    "Using the reference images as your guide, extract Straight Pipe Lug specifications from the input table.\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return ALL of the following fields:\n"
                    "- name, rodDiameter, pipeOD, rodTakeOut, isPerpendicular,\n"
                    "  topShape, angle1, width1, width2, angle2, angle3,\n"
                    "  thickness1, gap1, stiffenerOffset, stiffenerHeight, stiffenerLength,\n"
                    "  offset1, chamfLength, pin1Diameter, pin1Length, height2\n\n"
                    "- isPerpendicular: integer 0 (parallel) or 1 (perpendicular)\n"
                    "- topShape: integer 1=Curved, 2=Squared, 3=Rounded, 4=Chamfered\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"DN50","rodDiameter":16,"pipeOD":60.3,"rodTakeOut":85,"isPerpendicular":0,'
                    '"topShape":1,"angle1":180,"width1":65,"width2":50,"angle2":0,"angle3":0,'
                    '"thickness1":10,"gap1":null,"stiffenerOffset":null,"stiffenerHeight":null,"stiffenerLength":null,'
                    '"offset1":null,"chamfLength":null,"pin1Diameter":null,"pin1Length":null,"height2":null}]'
                )
            }
        ]

    else:
        raise ValueError(f"Unsupported part type for extraction: {part_type!r}")

    response = _call_with_retry(
        lambda: client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=[{"role": "user", "content": content}],
            max_tokens=4096,
            temperature=0,
        )
    )

    # Print raw response for debugging
    raw_output = response.choices[0].message.content
    print("RAW OUTPUT:")
    print(raw_output)

    # Convert to JSON
    try:
        part_json = json.loads(raw_output)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        # Try to extract JSON from response if it contains extra text
        json_match = re.search(r'\[.*\]|\{.*\}', raw_output, re.DOTALL)
        if json_match:
            try:
                part_json = json.loads(json_match.group())
            except json.JSONDecodeError:
                print("Could not parse JSON from response")
                print(f"Extracted text: {json_match.group()}")
                raise
        else:
            raise

    return part_json, part_type

