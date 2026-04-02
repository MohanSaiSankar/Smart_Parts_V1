# Quick Reference: Dimension Extraction Improvements

## Summary Table

| Aspect | Before | After |
|--------|--------|-------|
| **Plate Fields** | 3 (basic) | 9+ (multi-plate) |
| **U-Bolt Fields** | 3 basic | 5+ with validation |
| **Clamp Fields** | 8 generic | 13+ detailed |
| **AI Prompts** | Generic | Hexagon spec-aligned |
| **Field Naming** | Simplified | IJUAhs/IJOAhs standards |
| **Null Handling** | Basic | Component-aware |
| **Debugging** | Minimal | Comprehensive logging |

---

## Component-by-Component Guide

### PLATE - From 3 to 9+ Fields

#### Before:
```json
{
  "name": "M10",
  "width": 75,
  "length": 100,
  "thickness": 9
}
```

#### After:
```json
{
  "name": "M10",
  "width1": 75,      // Top plate
  "length1": 100,
  "thickness1": 9,
  "width2": 70,      // Bottom plate (optional)
  "length2": 95,
  "thickness2": 8,
  "width3": null,    // Vertical plate (optional)
  "length3": null,
  "thickness3": null
}
```

**Field Mapping**:
```
width1          → IJUAhsWidth1::Width1
length1         → IJUAhsLength1::Length1
thickness1      → IJUAhsThickness1::Thickness1
width2          → IJUAhsWidth2::Width2
length2         → IJUAhsLength2::Length2
thickness2      → IJUAhsThickness2::Thickness2
width3          → IJUAhsWidth3::Width3
length3         → IJUAhsLength3::Length3
thickness3      → IJUAhsThickness3::Thickness3
```

---

### U-BOLT - From 3 to 5+ Fields

#### Before:
```json
{
  "name": "DN15",
  "width": 34,
  "UBolt Center To End": 60,
  "Rod Dia": 8
}
```

#### After:
```json
{
  "name": "DN15",
  "uBoltWidth": 34,              // Center-to-center leg distance
  "uBoltLength": 60,             // Bottom to top vertical
  "uBoltRodDia": 8,              // Round stock diameter
  "uBoltFlatSpot": 0,            // Optional flat modification
  "isJBolt": 0                   // 0=U-Bolt, 1=J-Bolt
}
```

**Field Mapping**:
```
uBoltWidth      → IJUAhsJUBolt::UBoltWidth
uBoltLength     → IJUAhsJUBolt::UBoltLength
uBoltRodDia     → IJUAhsJUBolt::UBoltRodDia
uBoltFlatSpot   → IJUAhsJUBolt::UBoltFlatSpot
isJBolt         → IJUAhsJUBolt::IsJBolt (Yes/No)
```

---

### PIPE CLAMP - From 8 to 13+ Fields

#### Before:
```json
{
  "name": "DN15",
  "diameter": 15,
  "thickness": 4,
  "width": 22,
  "width2": 25,
  "height": 10,
  "height2": 25,
  "gap1": 10
}
```

#### After:
```json
{
  "name": "DN15",
  "size": "S1",                  // Size classification for BOM
  "diameter1": 15,               // Primary pipe diameter
  "diameter2": null,             // Secondary pipe (dual-pipe)
  "thickness1": 4,               // Top plate thickness
  "thickness2": null,            // Bottom plate thickness
  "height1": 22,                 // Centerline to top
  "height2": 25,                 // Centerline to bottom
  "height3": null,               // Additional height
  "width1": 10,                  // Top plate width
  "width2": 10,                  // Bottom/offset width
  "rodTakeOut": 5,               // Centerline to rod port
  "gap1": null,                  // Primary gap
  "gap2": null                   // Secondary gap
}
```

**Field Mapping**:
```
size            → IJUAhsSize::Size
diameter1       → IJOAhsDiameter1::Diameter1
diameter2       → IJOAhsDiameter2::Diameter2
thickness1      → IJUAhsThickness1::Thickness1
thickness2      → IJUAhsThickness2::Thickness2
height1         → IJUAhsHeight1::Height1
height2         → IJUAhsHeight2::Height2
height3         → IJUAhsHeight3::Height3
width1          → IJUAhsWidth1::Width1
width2          → IJUAhsWidth2::Width2
rodTakeOut      → IJUAhsRodTakeOut::RodTakeOut
gap1            → IJUAhsGap1::Gap1
gap2            → IJUAhsGap2::Gap2
```

---

## Key Improvements in AI Extraction

### Plate Extraction
```python
# Enhanced prompt now includes:
- Documentation reference to Hexagon SmartParts
- Explicit field definitions for each plate type
- NULL handling guidance for optional plates
- Example JSON with all plate configurations
```

### U-Bolt Extraction
```python
# Enhanced prompt now includes:
- Specification of center-to-center measurement
- Automatic numeric extraction from mixed formats (M8 → 8)
- J-Bolt vs U-Bolt indicator
- Flat spot dimension handling
```

### Clamp Extraction
```python
# Enhanced prompt now includes:
- Single vs dual-pipe detection
- Height measurement context (from centerline)
- RodTakeOut port distance
- Gap dimension classification
- Size attribute for BOMs
```

---

## Field Naming Convention

All fields follow Hexagon SmartParts naming:
- **IJUAhs** = Interface for User Attributes - Hangers/Supports
- **IJOAhs** = Interface for Object Attributes - Hangers/Supports
- Format: `IJUAhs<Component>::<Property>`

Examples:
- `IJUAhsWidth1::Width1` - First width dimension
- `IJUAhsJUBolt::UBoltWidth` - U-Bolt specific width
- `IJOAhsDiameter1::Diameter1` - Object diameter dimension

---

## Validation Rules

### Plate
- width1, length1, thickness1 are **required**
- width2-3, length2-3, thickness2-3 are **optional**
- All dimensions should be numeric (mm or inches)

### U-Bolt
- uBoltWidth > uBoltRodDia × 2 *(critical: legs must fit)*
- uBoltLength > 0 *(minimum vertical span)*
- uBoltRodDia extracted as numeric or null *(e.g., M8 → 8)*
- isJBolt must be 0 or 1

### Clamp
- diameter1 is **required** (single pipe minimum)
- height1 and height2 should reference centerline (NOT edges)
- rodTakeOut distance must be positive
- All optional fields (2nd diameters, gaps) should be null if not applicable

---

## Debugging Guide

### Enable Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)  # Shows all extractions
```

### Check Mapped Fields
```
Output shows: "Clamp DN15: IJUAhsDiameter1::Diameter1 = 15"
Format: "<Part Type> <PartNumber>: <Field Name> = <Value>"
```

### Validation Points
1. ✓ Check JSON parsing succeeds
2. ✓ Verify field count matches component type
3. ✓ Confirm numeric conversions
4. ✓ Validate null handling for optional fields
5. ✓ Review Excel sheet population success

---

## Usage

```bash
# Standard workflow
python main.py
# Enter image path: test_images/clamp_table.png
# Enter part type: clamp

# Output
# Extracting data from image...
# Mapping fields...
# Filling Excel template...
# POC completed successfully.
```

Check `Output_Plate_POC.xlsx` for results with properly mapped dimensions.

