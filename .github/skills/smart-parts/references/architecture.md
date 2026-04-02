# Smart Parts V1 — Architecture Reference

## Module Details

### `extractor.py`

**`detect_part_type(image_path)`**
- Single GPT-4o call, `max_tokens=10`
- Prompt lists all 5 valid categories with distinguishing characteristics
- Returns one of: `"plate"`, `"ubolt"`, `"clamp"`, `"lug"`, `"elbow_lug"`
- Raises `ValueError` if model returns an unrecognized word

**`extract_data(image_path, part_type=None)`**
- If `part_type` is None, calls `detect_part_type()` first
- Loads reference images from `Knowledge_Pdf/images/` via `_knowledge_blocks()`
- Builds a multi-part message: `[system text, *ref_image_blocks, "INPUT:", input_image, extraction_prompt]`
- Calls GPT-4o with `max_tokens=4096, temperature=0`
- Returns `(part_json: list[dict], part_type: str)`

**`_knowledge_blocks(filenames)`**
- Skips any filename that doesn't exist on disk (safe — no crash if image missing)
- Injects a text label before each image: `[Reference: <filename_stem>]`

---

### `mapper.py`

**`map_to_excel_fields(vector_json, part_type)`**
- Input: `list[dict]` from extractor, part type string
- Output: `list[dict]` where keys are exact Hexagon column header strings
- Naming convention:
  - `IJUAhs<Category>::<Property>` — User Attributes (Hangers/Supports)
  - `IJOAhs<Category>::<Property>` — Object Attributes (Hangers/Supports)
- Always includes `"PartNumber"` key sourced from `"name"` field
- Skips fields where value is `None` (not written to Excel)
- Type converts: int for integer fields, float for dimensions, str for text

---

### `excel_engine.py`

**`fill_workbook(template_path, output_path, batches)`**
- `batches`: list of `(mapped_data, part_type, label)` tuples
- For each batch: copies the template sheet for that part type, renames it to `label` (max 31 chars, de-duplicated)
- Removes all original template part sheets after creating batch sheets
- Keeps `CustomInterfaces` sheet always
- Template sheets removed: all values in `_SHEET_FOR_PART`

**`_fill_ws(ws, mapped_data)`**
- Finds `Start`/`End` row markers in column 1
- Reads headers from row `start_row - 2`
- Finds template row (marked `!` in column 1, or last row before `End`)
- Clears existing data area, then inserts one row per record
- Copies template row values/styles into each new row, then overlays mapped values
- Column 1 is blanked on data rows (removes the `!` marker)

**`_SHEET_FOR_PART` dict**
```python
{
    "plate":     "Plates",
    "ubolt":     "Ubolt",
    "clamp":     "Clamp",
    "lug":       "Stright_Pipe_Lug",   # note: typo in sheet name is intentional (matches template)
    "elbow_lug": "Elbow_Lug",
}
```

---

### `app.py`

**`POST /api/process`**
- Accepts `multipart/form-data` with field `images` (multiple files allowed)
- Max upload size: 64 MB
- Allowed extensions: `png`, `jpg`, `jpeg`, `gif`, `bmp`
- For each file: saves to `uploads/`, calls extractor → mapper → accumulates into `batches`
- Calls `fill_workbook()` once for all batches → single output Excel file
- Cleans up uploaded image files after processing
- Returns JSON:
  ```json
  {
    "success": true,
    "message": "Processed N image(s) successfully",
    "output_file": "Output_SmartParts.xlsx",
    "images": [{ "filename": "...", "part_type": "...", "rows": N, "data": [...] }],
    "extracted_data": [...]
  }
  ```

**`GET /api/download/<filename>`**
- Serves files from the `uploads/` folder as attachments

---

## Knowledge PDF → Reference Image Extraction

When a new PDF is added to `Knowledge_Pdf/`, extract images using:

```python
import fitz  # PyMuPDF — install with: pip install pymupdf
import os

doc = fitz.open("Knowledge_Pdf/YourPart_Knowledge.pdf")
img_dir = "Knowledge_Pdf/images"
prefix = "yourpart"  # e.g. "lug", "elbow", "clamp"

for pg_idx, page in enumerate(doc):
    for img_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        if pix.width < 30 or pix.height < 30:
            continue  # skip tiny icons/logos
        fname = f"{prefix}_p{pg_idx+1}_img{img_idx+1}.png"
        pix.save(os.path.join(img_dir, fname))
        print(f"Saved: {fname} ({pix.width}x{pix.height})")
```

Then view each image to assign it to the correct parameter before referencing in `extractor.py`.

---

## Template Excel Row Alignment Check

Run this to verify a sheet's alignment before deployment:

```python
from openpyxl import load_workbook

wb = load_workbook("templates/Input_Parts.xlsx")
ws = wb["YourSheetName"]

start_row = next(r for r in range(1, ws.max_row+1) if ws.cell(r,1).value == "Start")
header_row = start_row - 2

print(f"Start={start_row}, header_row={header_row}")
headers = {ws.cell(header_row, c).value: c for c in range(1, ws.max_column+1) if ws.cell(header_row, c).value}

# Check specific fields
for field in ["IJUAhsYourField::YourField"]:
    print(field, ":", headers.get(field, "NOT FOUND"))
```
