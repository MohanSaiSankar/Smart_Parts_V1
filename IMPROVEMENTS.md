# Dimension Mapping & Extraction Improvements

## Overview
Improved dimension mapping and extraction for three specific component types based on **Hexagon Smart3D Hangers and Supports SmartParts Configuration (Version 14)** documentation.

---

## Component Types Improved

### 1. PLATE
**Reference**: SmartParts > Block Clamp > Plate Properties

**Improved Extraction**:
- **Top Plate** (Plate 1):
  - `width1` → `IJUAhsWidth1::Width1` - Top plate width dimension
  - `length1` → `IJUAhsLength1::Length1` - Top plate length dimension  
  - `thickness1` → `IJUAhsThickness1::Thickness1` - Top plate thickness

- **Bottom Plate** (Plate 2):
  - `width2` → `IJUAhsWidth2::Width2` - Bottom plate width (optional)
  - `length2` → `IJUAhsLength2::Length2` - Bottom plate length (optional)
  - `thickness2` → `IJUAhsThickness2::Thickness2` - Bottom plate thickness (optional)

- **Vertical/Base Plate** (Plate 3):
  - `width3` → `IJUAhsWidth3::Width3` - Vertical plate width (optional)
  - `length3` → `IJUAhsLength3::Length3` - Vertical plate length (optional)
  - `thickness3` → `IJUAhsThickness3::Thickness3` - Vertical plate thickness (optional)

**Key Improvements**:
- Now extracts **up to 3 plate configurations** instead of generic 3 dimensions
- Support for multi-plate assemblies (top, bottom, vertical configurations)
- Null handling for missing plate configurations
- More accurate column header matching in source tables

---

### 2. U-BOLT
**Reference**: SmartParts > Beam Clamp > Clip with U-Bolt / J-Bolt

**Improved Extraction**:
- **Core Dimensions**:
  - `uBoltWidth` → `IJUAhsJUBolt::UBoltWidth` - Center-to-center distance between legs
  - `uBoltLength` → `IJUAhsJUBolt::UBoltLength` - Distance from bottom to top end of legs
  - `uBoltRodDia` → `IJUAhsJUBolt::UBoltRodDia` - Diameter of round stock (automatically extracts numeric value)

- **Optional Advanced Properties**:
  - `uBoltFlatSpot` → `IJUAhsJUBolt::UBoltFlatSpot` - Flat spot dimension on curved section (if present)
  - `isJBolt` → `IJUAhsJUBolt::IsJBolt` - J-Bolt vs U-Bolt indicator ("Yes"/"No")

**Key Improvements**:
- Correctly identifies **UBolt center-to-center measurement** (critical for assembly fit)
- Automatic numeric extraction from mixed alphanumeric rod specifications (e.g., "M8" → 8)
- Support for J-Bolt variant detection
- Flat spot dimension handling for modified bend profiles
- Proper dimension validation (UBoltWidth > UBoltRodDia)

---

### 3. PIPE CLAMP (Block Clamp)
**Reference**: SmartParts > Block Clamp > Basic Block Clamp Properties

**Improved Extraction**:
- **Pipe Support Dimensions**:
  - `diameter1` → `IJOAhsDiameter1::Diameter1` - First pipe diameter
  - `diameter2` → `IJOAhsDiameter2::Diameter2` - Second pipe diameter (for dual-pipe clamps)

- **Height Dimensions**:
  - `height1` → `IJUAhsHeight1::Height1` - Distance from pipe centerline to top
  - `height2` → `IJUAhsHeight2::Height2` - Distance from pipe centerline to bottom
  - `height3` → `IJUAhsHeight3::Height3` - Additional height dimension

- **Plate/Width Dimensions**:
  - `thickness1` → `IJUAhsThickness1::Thickness1` - Top plate thickness
  - `thickness2` → `IJUAhsThickness2::Thickness2` - Bottom plate thickness (if distinct)
  - `width1` → `IJUAhsWidth1::Width1` - Top plate width
  - `width2` → `IJUAhsWidth2::Width2` - Bottom plate or offset width

- **Rod Connection Point**:
  - `rodTakeOut` → `IJUAhsRodTakeOut::RodTakeOut` - Distance from pipe centerline to rod port

- **Optional Gap Dimensions**:
  - `gap1` → `IJUAhsGap1::Gap1` - Primary gap dimension
  - `gap2` → `IJUAhsGap2::Gap2` - Secondary gap dimension

- **Size Classification**:
  - `size` → `IJUAhsSize::Size` - String attribute for clamp size selection (BOMs)

**Key Improvements**:
- Distinguishes **single vs dual-pipe configurations**
- Proper **height measurement context** (from centerline not edge)
- RodTakeOut dimension support (critical for connection design)
- Flexible gap dimension handling
- Size attribute for BOM generation and reporting

---

## Technical Changes

### extractor.py
**Changes**:
- Enhanced AI prompts with **detailed Hexagon spec references**
- Added specific field names and measurement contexts
- Improved JSON schema documentation in prompts
- Better handling of optional dimensions
- Automatic numeric extraction for mixed-format specifications

**Example Prompt Improvement**:
```
Before: "Extract U-Bolt specifications from table..."
After: "Extract U-Bolt specifications following Hexagon SmartParts standard 
(Beam Clamp - Clip with U-Bolt/J-Bolt section). For each U-Bolt row..."
```

### mapper.py
**Changes**:
- Expanded field coverage from 3-8 fields per component
- Proper null-handling for optional dimensions
- Correct Hexagon IJUAhs/IJOAhs interface naming conventions
- Type conversion with validation
- Component-specific field organization

**Example Field Growth**:
```
Before (Plate): 3 fields (Width, Length, Thickness)
After (Plate):  9+ fields (Width1-3, Length1-3, Thickness1-3)

Before (Clamp): 8 fields (basic)
After (Clamp):  13+ fields (diameter1-2, height1-3, width1-2, thickness1-2, gaps, rodTakeOut, size)
```

### excel_engine.py
**Changes**:
- Added logging for traceability
- Enhanced error messages with sheet names
- Null-value aware field iteration  
- Better documentation with specifications
- Improved debugging information

---

## Validation Recommendations

When extracting from source documents:

### Plates
- ✓ Verify plate assembly type (single, dual, triple)
- ✓ Confirm dimension order (Width is typically X-axis, Length is Y-axis)
- ✓ Check thickness measurements are consistent (perpendicular to surface)

### U-Bolts
- ✓ Validate UBoltWidth > UBoltRodDia * 2 (legs must fit)
- ✓ Confirm rod diameter extraction format (extract numeric from M8, M10, etc.)
- ✓ Verify length is total vertical span

### Pipe Clamps
- ✓ Identify single vs dual-pipe configuration
- ✓ Confirm height references to centerline (not edges)
- ✓ Verify RodTakeOut measurement context
- ✓ Check gap dimensions match assembly intent

---

## Usage Example

```python
from extractor import extract_data
from mapper import map_to_excel_fields
from excel_engine import fill_sheet

# Extract data
image_json = extract_data("clamp_table.png", "clamp")

# Map to Excel fields
mapped = map_to_excel_fields(image_json, "clamp")

# Fill template
fill_sheet("template.xlsx", "output.xlsx", mapped, "clamp")
```

---

## References
- Hexagon Smart3D Hangers and Supports SmartParts Configuration v14
- SmartParts Common Attributes
- Beam Clamp Properties (U-Bolt specification)
- Block Clamp Properties (Plate & Pipe Clamp specifications)
- Field naming convention: `IJ<Category><Component>::<PropertyName>`

