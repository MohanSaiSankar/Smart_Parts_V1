import base64
import json
import os
import re
import time
from openai import AzureOpenAI, RateLimitError, APITimeoutError, APIConnectionError, InternalServerError
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
    """Retry fn() up to `retries` times on transient Azure errors; raise immediately on others."""
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return fn()
        except (RateLimitError, APITimeoutError, APIConnectionError, InternalServerError) as exc:
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

def detect_part_type(image_path, *, _input_b64=None, _input_mime=None):
    """
    Classify the input engineering drawing / table image as one of the supported SmartPart types.

    Decision is made purely from the input image — no reference images used.
    Pass _input_b64 / _input_mime to reuse an already-encoded image and avoid a second disk read.
    """
    if _input_b64 is None:
        with open(image_path, "rb") as f:
            _input_b64 = base64.b64encode(f.read()).decode()
    if _input_mime is None:
        _input_mime = _mime_for(image_path)

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
                            "which SmartPart category it belongs to:\n\n"
                            "- plate     : flat rectangular steel plates with Width, Length, Thickness dimensions\n"
                            "- ubolt     : U-shaped or J-shaped threaded rod hardware (U-bolt / J-bolt)\n"
                            "- clamp     : circular pipe clamp hardware with bolt holes and sweep geometry\n"
                            "- lug       : straight pipe welding lug mounted on a straight pipe (parallel/perpendicular)\n"
                            "- elbow_lug : elbow lug mounted on a pipe elbow fitting with ElbowRadius and FaceToCenter\n"
                            "- bolt      : bolt hardware showing head shape, rod, nut, and washer dimensions\n"
                            "- nut       : standalone nut hardware (hex, square, or round) with rod diameter\n"
                            "- pin       : cylindrical pin with optional cotter pin specifications\n"
                            "- clevis    : clevis connector/fork fitting with opening and end-nut geometry\n"
                            "- rod       : straight hanger rod with end-type and length specifications\n"
                            "- shoe      : pipe shoe support welded to pipe bottom with height and shape\n"
                            "- strap     : pipe strap/band wrapping around pipe with inside dimensions\n"
                            "- shield    : curved pipe shield or protection saddle wrapping around pipe\n"
                            "- guide     : pipe guide bracket constraining lateral pipe movement\n"
                            "- strut     : structural strut member (rigid or spring) with end connector shapes\n\n"
                            "Reply with EXACTLY one word from the list above — no punctuation, no explanation."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{_input_mime};base64,{_input_b64}"}
                    }
                ]
            }],
            max_tokens=15,
        )

    response = _call_with_retry(_call)
    raw = response.choices[0].message.content.strip().lower()
    # Check in priority order — elbow_lug before lug to avoid substring match
    for valid in ("plate", "ubolt", "clamp", "elbow_lug", "lug",
                  "bolt", "nut", "pin", "clevis", "rod",
                  "shoe", "strap", "shield", "guide", "strut"):
        if valid in raw:
            print(f"Detected part type: {valid}")
            return valid
    raise ValueError(f"Could not detect part type from image. Model replied: {raw!r}")


def extract_data(image_path, part_type=None):
    # Encode input image once — reused for detection and extraction to avoid a second disk read
    with open(image_path, "rb") as f:
        input_b64 = base64.b64encode(f.read()).decode()
    input_mime = _mime_for(image_path)

    if not part_type:
        part_type = detect_part_type(image_path, _input_b64=input_b64, _input_mime=input_mime)

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

    elif part_type.lower() == "bolt":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract bolt specifications from the engineering drawing or data table.\n\n"
                    "Bolt anatomy:\n"
                    "- Head (Shape1): bolt head shape (Hex/Square/Round), Shape1Width1/Shape1Width2 = outer dims, Thickness1 = head thickness\n"
                    "- Rod: RodDiameter1 = shank diameter, Length = total bolt length including head, OverLength1 = threaded protrusion past RodEnd1\n"
                    "- Nut (Shape2): nut shape, Shape2Width1/Shape2Width2 = outer dims, Thickness2 = nut thickness\n"
                    "- Washer plate (Shape3): washer shape, Shape3Width1/Shape3Width2 = outer dims, Thickness3 = washer thickness\n"
                    "- TWPlateCount: number of top washer plates, BWPlateCount: number of bottom washer plates\n"
                    "- Gap1: gap specification\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, shape1Type, shape1Width1, shape1Width2, thickness1, rodDiameter1, length, overLength1,\n"
                    "  shape2Type, shape2Width1, shape2Width2, thickness2,\n"
                    "  shape3Type, shape3Width1, shape3Width2, thickness3,\n"
                    "  twPlateCount, bwPlateCount, gap1\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"M16x80","shape1Type":"Hex","shape1Width1":24,"shape1Width2":null,"thickness1":10,'
                    '"rodDiameter1":16,"length":80,"overLength1":35,"shape2Type":"Hex","shape2Width1":24,"shape2Width2":null,'
                    '"thickness2":13,"shape3Type":"Round","shape3Width1":30,"shape3Width2":null,"thickness3":3,'
                    '"twPlateCount":1,"bwPlateCount":1,"gap1":null}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "nut":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract nut specifications from the engineering drawing or data table.\n\n"
                    "Nut fields:\n"
                    "- RodDiameter: thread/rod diameter the nut fits\n"
                    "- Shape1Type: nut shape (Hex, Square, Round)\n"
                    "- Shape1Width1: outer dimension of nut (across flats for hex)\n"
                    "- Shape1Width2: second outer dimension (for non-circular shapes)\n"
                    "- Shape1Length: thickness/height of nut\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return: name, rodDiameter, shape1Type, shape1Width1, shape1Width2, shape1Length\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"M16 Hex Nut","rodDiameter":16,"shape1Type":"Hex","shape1Width1":24,"shape1Width2":null,"shape1Length":13}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "pin":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract pin specifications from the engineering drawing or data table.\n\n"
                    "Pin fields:\n"
                    "- Pin1Diameter: pin body diameter\n"
                    "- Pin1Length: total pin length\n"
                    "- CotterDia: cotter/split pin diameter (null if no cotter pin)\n"
                    "- CotterLength: cotter pin length (null if no cotter pin)\n"
                    "- CotterOffset: distance from pin end to cotter pin hole center (null if no cotter pin)\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return: name, pin1Diameter, pin1Length, cotterDia, cotterLength, cotterOffset\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"P25x100","pin1Diameter":25,"pin1Length":100,"cotterDia":4,"cotterLength":30,"cotterOffset":90}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "clevis":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract clevis specifications from the engineering drawing or data table.\n\n"
                    "Clevis fields:\n"
                    "- RodDiameter: diameter of the rod attaching to the clevis\n"
                    "- RodTakeOut: distance from pin port to rod end port\n"
                    "- Opening1: distance from pin centerline to inside face of end fork\n"
                    "- Shape1Type: end fork/eye shape type (Round, Square, Hex)\n"
                    "- Shape1Width1/Shape1Width2: outer dimensions of end fork\n"
                    "- Shape1Length: thickness of end fork shape\n"
                    "- Diameter2: outer diameter of round ends\n"
                    "- Thickness2: end thickness\n"
                    "- Gap2/Gap3: gap specifications\n"
                    "- Width3: body width\n"
                    "- OverLength1/OverLength2: overlength protrusions at each end\n"
                    "- Pin1Diameter/Pin1Length: clevis pin dimensions\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, rodDiameter, rodTakeOut, opening1, shape1Type, shape1Width1, shape1Width2, shape1Length,\n"
                    "  diameter2, thickness2, gap2, width3, gap3, overLength1, overLength2, pin1Diameter, pin1Length\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"CV-M16","rodDiameter":16,"rodTakeOut":50,"opening1":20,"shape1Type":"Round",'
                    '"shape1Width1":30,"shape1Width2":null,"shape1Length":15,"diameter2":null,"thickness2":10,'
                    '"gap2":null,"width3":25,"gap3":null,"overLength1":15,"overLength2":15,"pin1Diameter":16,"pin1Length":45}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "rod":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract hanger rod specifications from the engineering drawing or data table.\n\n"
                    "Rod fields:\n"
                    "- RodDiameter1: rod stock diameter\n"
                    "- Length: total rod length (null for variable-length rods)\n"
                    "- WtPerLen: weight per unit length\n"
                    "- Weight: total rod weight\n"
                    "- RodEnd1Type/RodEnd2Type: end condition codes (e.g. Threaded, Eye, Hook)\n"
                    "- RodCenterType: center feature type code\n"
                    "- Offset1: offset dimension\n"
                    "- Thickness1: rod feature thickness\n"
                    "- Length1: length of rod end feature\n"
                    "- Diameter1: feature diameter at rod end\n"
                    "- OverLength1/OverLength2: threaded protrusion at each end\n"
                    "- MinLen/MaxLen: minimum and maximum rod lengths\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, rodDiameter1, length, wtPerLen, weight, rodEnd1Type, rodEnd2Type, rodCenterType,\n"
                    "  offset1, thickness1, length1, diameter1, overLength1, overLength2, minLen, maxLen\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"ROD-M16","rodDiameter1":16,"length":500,"wtPerLen":null,"weight":null,'
                    '"rodEnd1Type":"Threaded","rodEnd2Type":"Threaded","rodCenterType":null,'
                    '"offset1":null,"thickness1":null,"length1":null,"diameter1":null,"overLength1":30,"overLength2":30,"minLen":200,"maxLen":1000}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "shoe":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract pipe shoe specifications from the engineering drawing or data table.\n\n"
                    "Shoe fields:\n"
                    "- ShoeShape: overall shoe shape code\n"
                    "- ShoeHeight: height from pipe bottom to shoe base (primary dimension)\n"
                    "- ShoeWidth: total shoe width (override; if null, calculated from pipe OD)\n"
                    "- ShoeLength: total shoe length along pipe axis (override; if null, calculated)\n"
                    "- ShoeGap: gap in the shoe (e.g. between shoe and pipe)\n"
                    "- Diameter1: pipe outer diameter the shoe wraps\n"
                    "- SlopeAngle: slope angle of the shoe base\n"
                    "- ShoeQty: number of shoes per support\n"
                    "- InsulationTh/InsulationLength: insulation thickness and length under shoe\n"
                    "- LegSpace/LegLowSpace: spacing between shoe legs (top and bottom)\n"
                    "- EndPlateNum/EndPlateHeight/EndPlateOffset/PlateShape: end plate geometry\n"
                    "- RepadShape: reinforcement pad shape\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, shoeShape, shoeHeight, shoeWidth, shoeLength, shoeGap, diameter1, slopeAngle,\n"
                    "  shoeQty, insulationTh, insulationLength, legSpace, legLowSpace,\n"
                    "  endPlateNum, endPlateHeight, endPlateOffset, plateShape, repadShape\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"SH-DN100","shoeShape":null,"shoeHeight":75,"shoeWidth":null,"shoeLength":200,'
                    '"shoeGap":null,"diameter1":114.3,"slopeAngle":null,"shoeQty":1,'
                    '"insulationTh":null,"insulationLength":null,"legSpace":null,"legLowSpace":null,'
                    '"endPlateNum":null,"endPlateHeight":null,"endPlateOffset":null,"plateShape":null,"repadShape":null}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "strap":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract pipe strap specifications from the engineering drawing or data table.\n\n"
                    "Strap fields:\n"
                    "- StrapWidthInside: inside width of the strap opening (= pipe OD + clearance)\n"
                    "- StrapHeightInside: inside height of the strap opening\n"
                    "- StrapThickness: strap material thickness\n"
                    "- StrapStockWidth: width of the flat strap stock material\n"
                    "- StrapFlatSpot: flat section at top of strap bend\n"
                    "- StrapTopGap: gap clearance at strap top\n"
                    "- StrapWidthWings: width of the bolt wings/ears extending past the strap body\n"
                    "- StrapOneSided: 1 if strap only goes halfway around pipe, 0 for full wrap\n"
                    "- StrapSplitGap/StrapSplitExtension: split strap gap and extension\n"
                    "- Pin1Diameter/Pin1Length: optional pin dimensions\n"
                    "- Multi1Qty/Multi1LocateBy/Multi1Location: multiple strap placement\n"
                    "- Gap1/Height1/Width1/Length1: additional geometry\n"
                    "- PipeOD: pipe outer diameter\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, strapWidthInside, strapHeightInside, strapThickness, strapStockWidth,\n"
                    "  strapFlatSpot, strapTopGap, strapWidthWings, strapOneSided,\n"
                    "  strapSplitGap, strapSplitExtension, pin1Diameter, pin1Length,\n"
                    "  multi1Qty, multi1LocateBy, multi1Location, gap1, height1, width1, length1, pipeOD\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"ST-DN50","strapWidthInside":60.3,"strapHeightInside":null,"strapThickness":5,'
                    '"strapStockWidth":30,"strapFlatSpot":null,"strapTopGap":null,"strapWidthWings":40,"strapOneSided":0,'
                    '"strapSplitGap":null,"strapSplitExtension":null,"pin1Diameter":null,"pin1Length":null,'
                    '"multi1Qty":null,"multi1LocateBy":null,"multi1Location":null,"gap1":null,"height1":null,"width1":null,"length1":null,"pipeOD":60.3}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "shield":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract pipe shield/saddle specifications from the engineering drawing or data table.\n\n"
                    "Shield fields:\n"
                    "- PipeOD: pipe outer diameter the shield wraps around\n"
                    "- Size: nominal size designation\n"
                    "- Thickness1: primary shield plate thickness\n"
                    "- Length1: primary shield length along pipe axis\n"
                    "- Angle1/Angle2: wrap angles of the primary shield section\n"
                    "- Width1/Width2: widths of shield sections\n"
                    "- Thickness2/Length2/Angle3/Angle4: secondary shield section geometry\n"
                    "- Width3/Width4/Thickness3/Angle5: tertiary shield section geometry\n"
                    "- Height1: shield height\n"
                    "- Length3: third length dimension\n"
                    "- Multi1Qty/Multi1LocateBy/Multi1Location: multiple shield placement\n"
                    "- Diameter1: feature diameter\n"
                    "- Offset1: offset dimension\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, pipeOD, size, thickness1, length1, angle1, angle2, width1, width2,\n"
                    "  thickness2, length2, angle3, angle4, width3, width4, thickness3, angle5,\n"
                    "  height1, length3, multi1Qty, multi1LocateBy, multi1Location, diameter1, offset1\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"SH-DN100","pipeOD":114.3,"size":"DN100","thickness1":5,"length1":300,'
                    '"angle1":120,"angle2":null,"width1":100,"width2":null,"thickness2":null,"length2":null,'
                    '"angle3":null,"angle4":null,"width3":null,"width4":null,"thickness3":null,"angle5":null,'
                    '"height1":null,"length3":null,"multi1Qty":null,"multi1LocateBy":null,"multi1Location":null,"diameter1":null,"offset1":null}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "guide":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract pipe guide specifications from the engineering drawing or data table.\n\n"
                    "Guide fields (up to 6 width/length/thickness sets for each plate component):\n"
                    "- Width1/Length1/Thickness1: primary guide plate dimensions\n"
                    "- Width2/Length2/Thickness2: secondary guide plate dimensions\n"
                    "- Width3/Length3/Thickness3: tertiary guide plate dimensions\n"
                    "- Width4/Length4/Thickness4: fourth plate dimensions\n"
                    "- Width5/Length5/Thickness5: fifth plate dimensions\n"
                    "- Width6/Length6: sixth plate dimensions\n"
                    "- Offset1/Offset2/Offset3/Offset4: offset dimensions\n"
                    "- Gap1: gap between guide and pipe\n"
                    "- GuideHeight: overall guide height\n"
                    "- Angle1/Angle2/Angle3/Angle4: angles\n"
                    "- Connection1/Connection2: connection type codes\n"
                    "- Multi1Qty/Multi1LocateBy/Multi1Location: multiple guide placement\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, width1, length1, thickness1, width2, length2, thickness2, width3, length3, thickness3,\n"
                    "  width4, length4, thickness4, width5, length5, thickness5, width6, length6,\n"
                    "  offset1, offset2, offset3, offset4, gap1, guideHeight,\n"
                    "  angle1, angle2, angle3, angle4, connection1, connection2,\n"
                    "  multi1Qty, multi1LocateBy, multi1Location\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"GD-DN80","width1":120,"length1":200,"thickness1":10,"width2":80,"length2":150,'
                    '"thickness2":10,"width3":null,"length3":null,"thickness3":null,"width4":null,"length4":null,"thickness4":null,'
                    '"width5":null,"length5":null,"thickness5":null,"width6":null,"length6":null,'
                    '"offset1":null,"offset2":null,"offset3":null,"offset4":null,"gap1":5,"guideHeight":100,'
                    '"angle1":null,"angle2":null,"angle3":null,"angle4":null,"connection1":null,"connection2":null,'
                    '"multi1Qty":null,"multi1LocateBy":null,"multi1Location":null}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
        ]

    elif part_type.lower() == "strut":
        content = [
            {
                "type": "text",
                "text": (
                    "You are a Hexagon SmartParts specialist.\n\n"
                    "Extract strut specifications from the engineering drawing or data table.\n\n"
                    "Strut fields:\n"
                    "- Length: fixed strut length (null for variable-length struts)\n"
                    "- StretchShape: cross-section shape code of the strut body\n"
                    "- RodEnd1Type: connection type at end 1 (e.g. Clevis, Eye, Threaded)\n"
                    "- Length1: length of end connector feature\n"
                    "- Diameter1: diameter of end connector\n"
                    "- Gap1: gap at connector\n"
                    "- Angle1: angle of end connection\n"
                    "- Shape1Type/Shape1Width1/Shape1Width2/Shape1Length: end shape geometry\n"
                    "- MinLen/MaxLen: min and max strut lengths\n"
                    "- WtPerLen/Weight: weight specifications\n"
                    "- Stroke: allowable stroke for spring/variable struts\n\n"
                    "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                    "For each row return:\n"
                    "- name, length, stretchShape, rodEnd1Type, length1, diameter1, gap1, angle1,\n"
                    "  shape1Type, shape1Width1, shape1Width2, shape1Length,\n"
                    "  minLen, maxLen, wtPerLen, weight, stroke\n"
                    "Use null for any field not present in the table.\n\n"
                    "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                    'Example: [{"name":"STR-500","length":500,"stretchShape":null,"rodEnd1Type":"Clevis",'
                    '"length1":null,"diameter1":null,"gap1":null,"angle1":null,'
                    '"shape1Type":null,"shape1Width1":null,"shape1Width2":null,"shape1Length":null,'
                    '"minLen":200,"maxLen":800,"wtPerLen":null,"weight":null,"stroke":null}]'
                )
            },
            {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
            input_block,
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

