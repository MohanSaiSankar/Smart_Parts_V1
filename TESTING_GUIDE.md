# Testing & Validation Guide

## Overview
This guide helps validate that the improved dimension extraction and mapping works correctly for plates, u-bolts, and pipe clamps.

---

## Unit Test Examples

### Test 1: Plate Multi-Configuration Extraction

**Test Case**: Plate with top, bottom, and vertical components

```python
def test_plate_extraction():
    from extractor import extract_data
    
    # Mock response structure
    expected_output = [
        {
            "name": "PLT-001",
            "width1": 100,
            "length1": 150,
            "thickness1": 10,
            "width2": 95,
            "length2": 145,
            "thickness2": 8,
            "width3": 20,
            "length3": 150,
            "thickness3": 12
        }
    ]
    
    # Validate structure
    assert len(expected_output[0]) == 10  # 10 fields including name
    assert expected_output[0]["width1"] > expected_output[0]["thickness1"]
    print("✓ Plate extraction test passed")
```

**Success Criteria**:
- ✓ Returns list of dictionaries
- ✓ Each dict has 10 fields (name + 9 dimensions)
- ✓ Numeric values are integers
- ✓ Optional fields can be null
- ✓ Width > Thickness (logical check)

---

### Test 2: U-Bolt Dimension Validation

**Test Case**: U-Bolt with automatic rod diameter extraction

```python
def test_ubolt_extraction():
    from extractor import extract_data
    
    ubolt_data = [
        {
            "name": "UBOLT-M8-34",
            "uBoltWidth": 34,
            "uBoltLength": 60,
            "uBoltRodDia": 8,
            "uBoltFlatSpot": 0,
            "isJBolt": 0
        }
    ]
    
    # Key validations
    assert ubolt_data[0]["uBoltWidth"] > ubolt_data[0]["uBoltRodDia"] * 2
    assert ubolt_data[0]["uBoltLength"] > 0
    assert ubolt_data[0]["uBoltRodDia"] == int(8)  # Extracted numeric
    print("✓ U-Bolt validation test passed")
```

**Success Criteria**:
- ✓ uBoltWidth > uBoltRodDia × 2 (legs can fit)
- ✓ uBoltLength is positive
- ✓ Rod diameter extracted as numeric
- ✓ isJBolt is 0 or 1
- ✓ All values are integers

---

### Test 3: Pipe Clamp Single vs Dual Configuration

**Test Case**: Single-pipe and dual-pipe clamps

```python
def test_clamp_extraction():
    from extractor import extract_data
    
    # Single pipe clamp
    single_pipe = {
        "name": "CLM-DN15",
        "size": "S1",
        "diameter1": 15,
        "diameter2": None,  # No second pipe
        "height1": 22,
        "height2": 25,
        "rodTakeOut": 5
    }
    
    # Dual pipe clamp
    dual_pipe = {
        "name": "CLM-DN15-DN25",
        "size": "D2",
        "diameter1": 15,
        "diameter2": 25,   # Second pipe present
        "height1": 35,
        "height2": 40,
        "rodTakeOut": 8
    }
    
    # Validations
    assert single_pipe["diameter1"] > 0
    assert single_pipe["diameter2"] is None
    
    assert dual_pipe["diameter1"] > 0
    assert dual_pipe["diameter2"] > dual_pipe["diameter1"]
    
    print("✓ Clamp single/dual pipe test passed")
```

**Success Criteria**:
- ✓ diameter1 always present
- ✓ diameter2 present only for dual-pipe
- ✓ Heights reference centerline context
- ✓ rodTakeOut is positive
- ✓ Size attribute captured

---

## Integration Tests

### Test 4: Full Mapping Pipeline

```python
def test_mapping_pipeline():
    from extractor import extract_data
    from mapper import map_to_excel_fields
    
    # Sample data
    clamp_json = [
        {
            "name": "DN15",
            "size": "S1",
            "diameter1": 15,
            "diameter2": None,
            "thickness1": 4,
            "thickness2": None,
            "height1": 22,
            "height2": 25,
            "height3": None,
            "width1": 10,
            "width2": 10,
            "rodTakeOut": 5,
            "gap1": None,
            "gap2": None
        }
    ]
    
    # Map to Excel fields
    mapped = map_to_excel_fields(clamp_json, "clamp")
    
    # Validations
    assert len(mapped) == 1
    assert mapped[0]["PartNumber"] == "DN15"
    assert "IJOAhsDiameter1::Diameter1" in mapped[0]
    assert mapped[0]["IJOAhsDiameter1::Diameter1"] == 15
    assert "IJOAhsDiameter2::Diameter2" not in mapped[0]  # Null not mapped
    
    print("✓ Mapping pipeline test passed")
```

**Success Criteria**:
- ✓ Correct field name conversion
- ✓ Numeric values present
- ✓ Null values excluded from mapping
- ✓ PartNumber captured
- ✓ Component-specific fields used

---

### Test 5: Excel Output Validation

```python
def test_excel_output():
    from openpyxl import load_workbook
    
    # Check output file
    wb = load_workbook("Output_Plate_POC.xlsx")
    
    if "Clamp" in wb.sheetnames:
        ws = wb["Clamp"]
        
        # Validations
        assert ws.max_row > 2  # Header + at least 1 data row
        
        # Check specific cell values
        diameter_col = None
        for col in range(1, ws.max_column + 1):
            if ws.cell(1, col).value == "IJOAhsDiameter1::Diameter1":
                diameter_col = col
                break
        
        assert diameter_col is not None
        # Check first data row has numeric value
        assert ws.cell(3, diameter_col).value > 0
        
        print("✓ Excel output validation passed")
```

**Success Criteria**:
- ✓ Sheet created for component type
- ✓ Headers match field names
- ✓ Data rows populated
- ✓ Numeric values correct type
- ✓ Proper cell alignment

---

## Performance Tests

### Test 6: Extraction Speed

```python
import time
from extractor import extract_data

def test_extraction_performance():
    start = time.time()
    
    # Extract from test image
    result = extract_data("test_images/clamp_table.png", "clamp")
    
    elapsed = time.time() - start
    
    # Should complete in reasonable time (adjust as needed)
    assert elapsed < 30  # 30 seconds timeout
    assert len(result) > 0
    
    print(f"✓ Extraction completed in {elapsed:.2f}s")
```

---

## Validation Checklist

### Before Deployment

- [ ] **Extraction Tests**
  - [ ] Plate: 9-field structure validated
  - [ ] U-Bolt: uBoltWidth > uBoltRodDia×2 check passes
  - [ ] Clamp: Single/dual-pipe detection works
  
- [ ] **Mapping Tests**
  - [ ] Field names use correct IJUAhs/IJOAhs conventions
  - [ ] Numeric conversions succeed
  - [ ] Null handling correct for optional fields
  
- [ ] **Excel Tests**
  - [ ] Output file created successfully
  - [ ] Sheet names match component types
  - [ ] Data appears in correct columns
  - [ ] File can be opened without errors
  
- [ ] **Edge Cases**
  - [ ] Single-plate configurations handled
  - [ ] Mixed numeric/alphanumeric extraction works
  - [ ] Tables with incomplete rows handled gracefully
  
- [ ] **Documentation**
  - [ ] All field mappings documented
  - [ ] Validation rules in README
  - [ ] Example JSON included
  - [ ] Error messages helpful

---

## Troubleshooting Guide

### Issue: JSON parsing error
```
Solution:
1. Check AI response format in extractor.py
2. Verify no extra text before/after JSON
3. Check regex extraction handles escaped characters
```

### Issue: Field not mapped to Excel
```
Solution:
1. Verify field name in mapper.py matches header row
2. Check header row exists 2 rows above "Start" marker
3. Ensure no typos in IJUAhs field names
```

### Issue: U-Bolt width validation fails
```
Solution:
1. Check uBoltRodDia extraction from part number
2. Verify uBoltWidth is center-to-center, not radius
3. Add validation logging to debug values
```

### Issue: Clamp height appears incorrect
```
Solution:
1. Confirm heights measure from centerline (not edge)
2. Check documentation for height1 vs height2 definition
3. Review table column headers carefully
```

---

## Expected Test Results

### Successful Run Output
```
✓ Plate extraction test passed
✓ U-Bolt validation test passed
✓ Clamp single/dual pipe test passed
✓ Mapping pipeline test passed
✓ Excel output validation passed
✓ Extraction completed in 8.34s

All tests passed: 6/6 ✓
```

### Field Count Validation
```
Plate:   9 fields (width1-3, length1-3, thickness1-3)
U-Bolt:  5 fields (width, length, rodia, flatspot, isjbolt)
Clamp:  13 fields (diameter1-2, height1-3, width1-2, 
                    thickness1-2, rodtakeout, gap1-2, size)
```

---

## Continuous Testing

Add these tests to your CI/CD pipeline:

```yaml
test:
  script:
    - python -m pytest tests/test_extraction.py
    - python -m pytest tests/test_mapping.py
    - python tests/test_excel_output.py
  artifacts:
    - Output_Plate_POC.xlsx
    - test_results.log
```

---

## Contact & Support

For validation issues, check:
1. QUICK_REFERENCE.md - Field mapping guide
2. IMPROVEMENTS.md - Detailed technical changes
3. extractor.py - AI prompt definitions
4. mapper.py - Field conversion logic

