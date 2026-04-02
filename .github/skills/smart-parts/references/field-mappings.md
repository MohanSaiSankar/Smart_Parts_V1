# Field Mappings Reference

All current AI-extracted field names and their corresponding Hexagon SmartParts Excel column headers.

---

## Plate (`plate`)

| AI Field | Excel Column | Type |
|---|---|---|
| `name` | `PartNumber` | str |
| `width1` | `IJUAhsWidth1::Width1` | int |
| `length1` | `IJUAhsLength1::Length1` | int |
| `thickness1` | `IJUAhsThickness1::Thickness1` | int |
| `width2` | `IJUAhsWidth2::Width2` | int |
| `length2` | `IJUAhsLength2::Length2` | int |
| `thickness2` | `IJUAhsThickness2::Thickness2` | int |
| `width3` | `IJUAhsWidth3::Width3` | int |
| `length3` | `IJUAhsLength3::Length3` | int |
| `thickness3` | `IJUAhsThickness3::Thickness3` | int |

---

## U-Bolt / J-Bolt (`ubolt`)

| AI Field | Excel Column | Type |
|---|---|---|
| `name` | `PartNumber` | str |
| `uBoltWidth` | `IJUAhsUBolt::UBoltWidth` | int |
| `uBoltCenterToEnd` | `IJUAhsUBolt::UBoltCenterToEnd` | int |
| `uBoltRodDia` | `IJUAhsUBolt::UBoltRodDia` | int |
| `uBoltFlatSpot` | `IJUAhsUBolt::UBoltFlatSpot` | int |
| `uBoltDia2` | `IJUAhsUBolt::UBoltDia2` | float |
| `uBoltDia2Start` | `IJUAhsUBolt::UBoltDia2Start` | float |
| `uBoltTopGap` | `IJUAhsUBolt::UBoltTopGap` | float |

---

## Pipe Clamp (`clamp`)

| AI Field | Excel Column | Type |
|---|---|---|
| `name` | `PartNumber` | str |
| `size` | `IJUAhsSize::Size` | str |
| `diameter1` | `IJOAhsDiameter1::Diameter1` | int |
| `diameter2` | `IJOAhsDiameter2::Diameter2` | int |
| `thickness1` | `IJUAhsThickness1::Thickness1` | int |
| `thickness2` | `IJUAhsThickness2::Thickness2` | int |
| `height1` | `IJUAhsHeight1::Height1` | int |
| `height2` | `IJUAhsHeight2::Height2` | int |
| `height3` | `IJUAhsHeight3::Height3` | int |
| `width1` | `IJUAhsWidth1::Width1` | int |
| `width2` | `IJUAhsWidth2::Width2` | int |
| `rodTakeOut` | `IJUAhsRodTakeOut::RodTakeOut` | int |
| `gap1` | `IJUAhsGap1::Gap1` | float |
| `gap2` | `IJUAhsGap2::Gap2` | float |
| `angle1` | `IJUAhsAngle1::Angle1` | float |
| `pin1Length` | `IJUAhsPin1Length::Pin1Length` | float |
| `pin1Diameter` | `IJUAhsPin1Diameter::Pin1Diameter` | float |
| `offset1` | `IJUAhsOffset1::Offset1` | float |
| `numberOfBolts` | `IJUAhsNumberOfBolts::NumberOfBolts` | int |
| `multiQty` | `IJUAhsMultiQty::MultiQty` | int |
| `multiLocatedBy` | `IJUAhsMultiLocatedBy::MultiLocatedBy` | str |
| `multiLocation` | `IJUAhsMultiLocation::MultiLocation` | float |

---

## Straight Pipe Lug (`lug`)

Template sheet: `Stright_Pipe_Lug` (note: intentional typo matches template tab name)

### Basic Attributes

| AI Field | Excel Column | Type |
|---|---|---|
| `name` | `PartNumber` | str |
| `rodDiameter` | `IJUAhsRodDiameter::RodDiameter` | float |
| `pipeOD` | `IJOAhsPipeOD::PipeOD` | float |
| `rodTakeOut` | `IJUAhsRodTakeOut::RodTakeOut` | float |
| `isPerpendicular` | `IJUAhsIsPerpendicular::IsPerpendicular` | int (0=parallel, 1=perpendicular) |

### Side Attributes

| AI Field | Excel Column | Type |
|---|---|---|
| `topShape` | `IJUAhsLug::TopShape` | int (1=Curved, 2=Squared, 3=Rounded, 4=Chamfered) |
| `angle1` | `IJUAhsAngle1::Angle1` | float |
| `width1` | `IJUAhsWidth1::Width1` | float |
| `width2` | `IJUAhsWidth2::Width2` | float |
| `angle2` | `IJUAhsAngle2::Angle2` | float |
| `angle3` | `IJUAhsAngle3::Angle3` | float |
| `thickness1` | `IJUAhsThickness1::Thickness1` | float |
| `gap1` | `IJUAhsGap1::Gap1` | float |
| `stiffenerOffset` | `IJUAhsLug::StiffenerOffset` | float |
| `stiffenerHeight` | `IJUAhsLug::StiffenerHeight` | float |
| `stiffenerLength` | `IJUAhsLug::StiffenerLength` | float |
| `offset1` | `IJUAhsOffset1::Offset1` | float |
| `chamfLength` | `IJUAhsLug::ChamfLength` | float |
| `pin1Diameter` | `IJUAhsPin1::Pin1Diameter` | float |
| `pin1Length` | `IJUAhsPin1::Pin1Length` | float |
| `height2` | `IJUAhsHeight2::Height2` | float |

---

## Elbow Lug (`elbow_lug`)

Template sheet: `Elbow_Lug`

### Basic Attributes

| AI Field | Excel Column | Type |
|---|---|---|
| `name` | `PartNumber` | str |
| `rodDiameter` | `IJUAhsRodDiameter::RodDiameter` | float |
| `pipeOD` | `IJOAhsPipeOD::PipeOD` | float |
| `elbowRadius` | `IJOAhsElbow::ElbowRadius` | float |
| `faceToCenter` | `IJOAhsElbow::FaceToCenter` | float |

### Lug Shape Attributes

| AI Field | Excel Column | Type |
|---|---|---|
| `topShape` | `IJUAhsLug::TopShape` | int (1=Curved, 2=Squared, 3=Rounded, 4=Chamfered) |
| `angle1` | `IJUAhsAngle1::Angle1` | float |
| `rodTakeOut` | `IJUAhsRodTakeOut::RodTakeOut` | float |
| `width1` | `IJUAhsWidth1::Width1` | float |
| `width2` | `IJUAhsWidth2::Width2` | float |
| `angle2` | `IJUAhsAngle2::Angle2` | float |
| `angle3` | `IJUAhsAngle3::Angle3` | float |
| `angle4` | `IJUAhsAngle4::Angle4` | float |
| `thickness1` | `IJUAhsThickness1::Thickness1` | float |
| `gap1` | `IJUAhsGap1::Gap1` | float |
| `stiffenerOffset` | `IJUAhsLug::StiffenerOffset` | float |
| `stiffenerHeight` | `IJUAhsLug::StiffenerHeight` | float |
| `stiffenerLength` | `IJUAhsLug::StiffenerLength` | float |
| `offset1` | `IJUAhsOffset1::Offset1` | float |
| `chamfLength` | `IJUAhsLug::ChamfLength` | float |
| `radiusActual` | `IJUAhsLug::RadiusActual` | float |
| `pin1Diameter` | `IJUAhsPin1::Pin1Diameter` | float |
| `pin1Length` | `IJUAhsPin1::Pin1Length` | float |

---

## Hexagon Naming Convention

```
IJUAhs<Category>::<PropertyName>   = User Attribute, Hangers/Supports
IJOAhs<Category>::<PropertyName>   = Object Attribute, Hangers/Supports
```

- `IJUAhs` → attributes the user configures (dimensions, shape options)
- `IJOAhs` → attributes derived from the object context (pipe OD, elbow geometry)
