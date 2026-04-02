---
name: smart-parts
description: 'Smart Parts V1 application skill. Use when: adding a new part type, modifying extraction fields, updating Excel field mappings, fixing AI prompts, debugging extraction failures, understanding the pipeline, adding knowledge PDF reference images, or changing the Flask API. Covers extractor.py, mapper.py, excel_engine.py, app.py, and the Excel template. Part types supported: plate, ubolt, clamp, lug (straight pipe lug), elbow_lug.'
argument-hint: 'Describe the change needed (e.g. "add new part type", "fix extraction", "update field mapping")'
---

# Smart Parts V1 — Application Skill

## What This Application Does

Smart Parts V1 is an AI-powered engineering parts data extraction system. Users upload images of engineering component drawings or data tables. The system:

1. Detects the part type automatically using Azure GPT-4o
2. Extracts all dimensional fields by sending the image + reference geometry images to GPT-4o
3. Maps extracted fields to Hexagon SmartParts/IJUAhs Excel column naming conventions
4. Fills the corresponding sheet in `templates/Input_Parts.xlsx` and returns a populated Excel workbook for download

---

## Supported Part Types

| Part Type Key | Excel Sheet | Description |
|---|---|---|
| `plate` | `Plates` | Flat rectangular steel plates |
| `ubolt` | `Ubolt` | U-bolt / J-bolt threaded rod hardware |
| `clamp` | `Clamp` | Circular pipe clamp hardware |
| `lug` | `Stright_Pipe_Lug` | Straight pipe welding lug (parallel/perpendicular) |
| `elbow_lug` | `Elbow_Lug` | Elbow lug mounted on a pipe elbow fitting |

---

## File Map

| File | Role |
|---|---|
| `extractor.py` | Azure GPT-4o calls — detect type, extract fields |
| `mapper.py` | Convert AI field names → Hexagon IJUAhs/IJOAhs column names |
| `excel_engine.py` | Clone template sheet, fill with mapped data |
| `app.py` | Flask API — uploads, orchestrates pipeline, returns JSON + download |
| `templates/Input_Parts.xlsx` | Excel template with one sheet per part type |
| `Knowledge_Pdf/images/` | Reference geometry PNG images injected into AI prompts |
| `Knowledge_Pdf/*.pdf` | Source knowledge PDFs (one per part type) |

---

## End-to-End Pipeline

```
User uploads image(s)
        ↓
app.py  →  extract_data(filepath)          [extractor.py]
               ↓
           detect_part_type()              → GPT-4o → "plate" | "ubolt" | "clamp" | "lug" | "elbow_lug"
               ↓
           Load reference images           from Knowledge_Pdf/images/<prefix>_p*.png
               ↓
           GPT-4o prompt + image           → raw JSON string
               ↓
           Parse JSON (regex fallback)     → list of dicts
        ↓
       map_to_excel_fields(json, type)     [mapper.py]
               ↓
           Convert field names             → IJUAhs*/IJOAhs* column headers
        ↓
       fill_workbook(template, batches)    [excel_engine.py]
               ↓
           Load template .xlsx
           For each image: copy sheet → fill with mapped row(s)
           Remove template-only sheets
           Save to uploads/
        ↓
app.py  returns JSON + /api/download/<file>
```

---

## Key Design Rules

### Excel Template Layout
Every part sheet in `templates/Input_Parts.xlsx` follows this layout:

```
Row (start_row - 2) : Column headers  (IJUAhs... names)
Row (start_row)     : "Start"
Row (start_row + 1) : "!"  ← template row cloned for each data record
Row (start_row + 2) : "End"
```

`excel_engine._fill_ws()` reads headers at `start_row - 2`, clones the `!` row for each record, and writes values by matching `mapped_row` keys to header names.

> **Critical**: When adding a new sheet to the template, ensure `Start` is at row `N` and column headers are at row `N-2`. There must be exactly one empty row between headers and `Start`.

### AI Extraction Rules
- `max_tokens=4096` and `temperature=0` are set on every extraction call to ensure full table extraction
- Every prompt includes: `"IMPORTANT: Extract EVERY SINGLE row from the table without skipping or truncating any."`
- Reference images from `Knowledge_Pdf/images/` are injected as `image_url` blocks before the input image
- JSON parse uses `re.search(r'\[.*\]|\{.*\}', raw, re.DOTALL)` as fallback if model includes extra text

### Detection Priority Order
`detect_part_type()` checks in this order: `"plate"`, `"ubolt"`, `"clamp"`, `"elbow_lug"`, `"lug"`  
`elbow_lug` must come before `lug` to avoid the substring `"lug"` matching inside `"elbow_lug"`.

---

## How to Add a New Part Type

See [./references/add-part-type.md](./references/add-part-type.md) for the full step-by-step procedure.

**Summary of touch-points:**
1. `extractor.py` → `detect_part_type()` prompt + valid list
2. `extractor.py` → `extract_data()` new `elif` block with reference images + prompt
3. `mapper.py` → new `elif` block mapping AI keys → IJUAhs column names
4. `excel_engine.py` → add entry to `_SHEET_FOR_PART`
5. `templates/Input_Parts.xlsx` → verify sheet exists and row alignment is correct
6. `Knowledge_Pdf/images/` → extract reference images from PDF

---

## Field Mapping Reference

See [./references/field-mappings.md](./references/field-mappings.md) for all current field names per part type.

---

## Environment Setup

```bash
# .env file required at project root
AZURE_OPENAI_API_KEY=<your-key>
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

---

## Common Debugging

| Symptom | Cause | Fix |
|---|---|---|
| Partial rows extracted | `max_tokens` too low or model truncated | Check `max_tokens=4096` is on all extraction calls |
| `JSONDecodeError` | Model returned extra text around JSON | Regex fallback handles this; check RAW OUTPUT in console |
| `Template sheet 'X' not found` | `_SHEET_FOR_PART` key missing or sheet name typo | Match `_SHEET_FOR_PART` value exactly to sheet tab name |
| Fields not written to Excel | Header name mismatch between mapper and template | Run column verification script in add-part-type guide |
| Wrong part type detected | Ambiguous image or prompt ordering | Check `detect_part_type()` valid list ordering (elbow_lug before lug) |
| `Start/End markers not found` | Template row alignment wrong | Ensure Start row - 2 = header row |
