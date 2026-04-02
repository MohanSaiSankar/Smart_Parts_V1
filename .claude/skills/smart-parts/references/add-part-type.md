# Adding a New Part Type — Step-by-Step Guide

Follow these steps in order whenever a new part type needs to be added to Smart Parts V1.

---

## Step 1 — Extract Reference Images from the PDF

Place the PDF in `Knowledge_Pdf/`. Then extract all images:

```python
import fitz, os
doc = fitz.open("Knowledge_Pdf/YourPart_Knowledge.pdf")
img_dir = "Knowledge_Pdf/images"
prefix = "yourpart"   # short lowercase prefix used for all image filenames

for pg_idx, page in enumerate(doc):
    for img_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        if pix.width < 30 or pix.height < 30:
            continue
        fname = f"{prefix}_p{pg_idx+1}_img{img_idx+1}.png"
        pix.save(os.path.join(img_dir, fname))
        print(f"Saved: {fname} ({pix.width}x{pix.height})")
```

View each image and note which one illustrates which parameter.

---

## Step 2 — Read the PDF Text to Get All Fields

```python
import fitz
doc = fitz.open("Knowledge_Pdf/YourPart_Knowledge.pdf")
for i, page in enumerate(doc):
    print(f"=== PAGE {i+1} ===")
    print(page.get_text())
```

Look for `IJUAhs::` and `IJOAhs::` property names. These are the exact Excel column headers.

---

## Step 3 — Add to `detect_part_type()` in `extractor.py`

**3a.** Add a bullet point describing the new part to the detection prompt:
```python
"- your_type : brief distinguishing description\n"
```

**3b.** Update the reply instruction:
```python
"plate   OR   ubolt   OR   clamp   OR   lug   OR   elbow_lug   OR   your_type"
```

**3c.** Add `"your_type"` to the valid-list loop. If your type name contains another type as a substring (like `elbow_lug` contains `lug`), place the longer name FIRST:
```python
for valid in ("plate", "ubolt", "clamp", "elbow_lug", "lug", "your_type"):
```

---

## Step 4 — Add extraction block to `extract_data()` in `extractor.py`

Insert a new `elif` block. Follow this template:

```python
elif part_type.lower() == "your_type":
    knowledge_imgs = [
        "yourpart_p4_img1.png",   # FieldName: description of what arrow/dimension shows
        "yourpart_p5_img2.png",   # AnotherField: description
        # ... add all relevant reference images
    ]
    ref_blocks = _knowledge_blocks(knowledge_imgs)

    content = [
        {
            "type": "text",
            "text": (
                "You are a Hexagon SmartParts specialist.\n\n"
                "REFERENCE IMAGES below show the geometric meaning of each parameter:\n"
                "- Field1: description\n"
                "- Field2: description\n"
                # ... all fields with precise geometric meaning
            )
        },
        *ref_blocks,
        {"type": "text", "text": "INPUT TABLE/DRAWING to extract from:"},
        input_block,
        {
            "type": "text",
            "text": (
                "Using the reference images as your guide, extract Your Part specifications from the input table.\n\n"
                "IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any.\n\n"
                "For each row return ALL of the following fields:\n"
                "- name, field1, field2, field3, ...\n"
                "Use null for any field not present in the table.\n\n"
                "Return ONLY a valid JSON array — no extra text, no comments, no truncation.\n"
                'Example: [{"name":"DN50","field1":16,"field2":60.3,...}]'
            )
        }
    ]

    response = client.chat.completions.create(
        model=AZURE_DEPLOYMENT,
        messages=[{"role": "user", "content": content}],
        max_tokens=4096,
        temperature=0,
    )
```

> **Rules:**
> - Always set `max_tokens=4096` and `temperature=0`
> - Always include the `IMPORTANT: Extract EVERY SINGLE row` instruction
> - End with `"no extra text, no comments, no truncation"`

---

## Step 5 — Add mapping block to `mapper.py`

Insert a new `elif` block that converts AI field names to Hexagon column names:

```python
elif part_type.lower() == "your_type":
    for item in vector_json:
        mapped_row = {"PartNumber": item.get("name")}

        field1 = item.get("field1")
        if field1 is not None:
            mapped_row["IJUAhsYourCategory::Field1"] = float(field1)

        field2 = item.get("field2")
        if field2 is not None:
            mapped_row["IJUAhsYourCategory::Field2"] = int(field2)

        # ... map every field
        mapped_data.append(mapped_row)
```

> **Type rules:**
> - Dimensions → `float()`
> - Counts/integers/boolean flags → `int()`
> - Text/codes → `str()`
> - Only add to `mapped_row` when value is not `None`

---

## Step 6 — Add to `excel_engine.py`

```python
_SHEET_FOR_PART = {
    # ... existing entries ...
    "your_type": "YourSheetTabName",   # must exactly match the tab name in Input_Parts.xlsx
}
```

---

## Step 7 — Verify Excel Template Sheet

Run this to confirm row alignment and that all mapped fields exist as column headers:

```python
from openpyxl import load_workbook

wb = load_workbook("templates/Input_Parts.xlsx")
ws = wb["YourSheetTabName"]

start_row = next(r for r in range(1, ws.max_row+1) if ws.cell(r,1).value == "Start")
header_row = start_row - 2
print(f"Start={start_row}, headers at row {header_row}")

headers = {ws.cell(header_row, c).value: c for c in range(1, ws.max_column+1) if ws.cell(header_row, c).value}

your_fields = [
    "IJUAhsYourCategory::Field1",
    "IJUAhsYourCategory::Field2",
]
for f in your_fields:
    col = headers.get(f)
    print(f"{'OK' if col else 'MISSING'}  {f}: col {col}")
```

If `Start` is not at row 9 (i.e., header row wouldn't be `start_row - 2`), adjust the template rows:
- Headers must be at `start_row - 2`
- One empty row between headers and Start

---

## Step 8 — Final Import Check

```bash
python -c "import extractor; import mapper; import excel_engine; print('All OK')"
```

---

## Checklist

- [ ] PDF images extracted to `Knowledge_Pdf/images/<prefix>_p*_img*.png`
- [ ] `detect_part_type()` prompt updated with new category
- [ ] New type added to valid-list in correct order (longer names before substrings)
- [ ] `extract_data()` elif block added with `max_tokens=4096, temperature=0`
- [ ] `mapper.py` elif block added with all fields mapped to IJUAhs/IJOAhs names
- [ ] `_SHEET_FOR_PART` entry added in `excel_engine.py`
- [ ] Template sheet exists with correct row alignment (Start at `header_row + 2`)
- [ ] All mapped fields verified present in template headers
- [ ] Import check passes
