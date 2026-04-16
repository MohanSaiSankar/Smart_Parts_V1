def map_to_excel_fields(vector_json,part_type):

    if not isinstance(vector_json, list):
        raise ValueError("Expected list from AI output")

    mapped_data = []
    if part_type.lower() == "plate":
        for plate in vector_json:
            Name = plate.get("name")
            mapped_row = {"PartNumber": Name}
            
            # Top plate dimensions (Plate Properties - Thickness1, Length1, Width1)
            width1 = plate.get("width1")
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = int(width1)
                
            length1 = plate.get("length1")
            if length1 is not None:
                mapped_row["IJUAhsLength1::Length1"] = int(length1)
                
            thickness1 = plate.get("thickness1")
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = int(thickness1)
            
            # Bottom plate dimensions (if applicable)
            width2 = plate.get("width2")
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = int(width2)
                
            length2 = plate.get("length2")
            if length2 is not None:
                mapped_row["IJUAhsLength2::Length2"] = int(length2)
                
            thickness2 = plate.get("thickness2")
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = int(thickness2)
            
            # Vertical/base plate dimensions (if applicable)
            width3 = plate.get("width3")
            if width3 is not None:
                mapped_row["IJUAhsWidth3::Width3"] = int(width3)
                
            length3 = plate.get("length3")
            if length3 is not None:
                mapped_row["IJUAhsLength3::Length3"] = int(length3)
                
            thickness3 = plate.get("thickness3")
            if thickness3 is not None:
                mapped_row["IJUAhsThickness3::Thickness3"] = int(thickness3)
            
            mapped_data.append(mapped_row)
            
    elif part_type.lower() == "ubolt":
        for ubolt in vector_json:
            Name = ubolt.get("name")
            mapped_row = {"PartNumber": Name}
            
            # U-Bolt dimensions based on Hexagon SmartParts spec
            uBoltWidth = ubolt.get("uBoltWidth")
            if uBoltWidth is not None:
                mapped_row["IJUAhsUBolt::UBoltWidth"] = int(uBoltWidth)
                
            uBoltLength = ubolt.get("uBoltCenterToEnd") or ubolt.get("uBoltLength")
            if uBoltLength is not None:
                mapped_row["IJUAhsUBolt::UBoltCenterToEnd"] = int(uBoltLength)
                
            uBoltRodDia = ubolt.get("uBoltRodDia")
            if uBoltRodDia is not None:
                mapped_row["IJUAhsUBolt::UBoltRodDia"] = int(uBoltRodDia)
                
            # Optional: Flat spot dimension
            uBoltFlatSpot = ubolt.get("uBoltFlatSpot")
            if uBoltFlatSpot is not None and uBoltFlatSpot != 0:
                mapped_row["IJUAhsUBolt::UBoltFlatSpot"] = int(uBoltFlatSpot)

            # Inner curved diameter and start position
            uBoltDia2 = ubolt.get("uBoltDia2")
            if uBoltDia2 is not None:
                mapped_row["IJUAhsUBolt::UBoltDia2"] = float(uBoltDia2)

            uBoltDia2Start = ubolt.get("uBoltDia2Start")
            if uBoltDia2Start is not None:
                mapped_row["IJUAhsUBolt::UBoltDia2Start"] = float(uBoltDia2Start)

            # Top gap clearance
            uBoltTopGap = ubolt.get("uBoltTopGap")
            if uBoltTopGap is not None:
                mapped_row["IJUAhsUBolt::UBoltTopGap"] = float(uBoltTopGap)

            # Support both legacy 'uBoltLength' and new 'uBoltCenterToEnd' key names
            # (handled above via ubolt.get("uBoltCenterToEnd") or ubolt.get("uBoltLength"))

            mapped_data.append(mapped_row)
            
    elif part_type.lower() == "clamp":
        for clamp in vector_json:
            Name = clamp.get("name")
            mapped_row = {"PartNumber": Name}
            
            # Size attribute for clamp selection
            size = clamp.get("size")
            if size is not None:
                mapped_row["IJUAhsSize::Size"] = str(size)
            
            # Pipe diameter dimensions
            diameter1 = clamp.get("diameter1")
            if diameter1 is not None:
                mapped_row["IJUAhsDiameter1::Diameter1"] = int(diameter1)
                
            diameter2 = clamp.get("diameter2")
            if diameter2 is not None:
                mapped_row["IJUAhsDiameter2::Diameter2"] = int(diameter2)
            
            # Plate thickness dimensions
            thickness1 = clamp.get("thickness1")
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = int(thickness1)
                
            thickness2 = clamp.get("thickness2")
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = int(thickness2)
            
            # Height dimensions
            height1 = clamp.get("height1")
            if height1 is not None:
                mapped_row["IJUAhsHeight1::Height1"] = int(height1)
                
            height2 = clamp.get("height2")
            if height2 is not None:
                mapped_row["IJUAhsHeight2::Height2"] = int(height2)
                
            height3 = clamp.get("height3")
            if height3 is not None:
                mapped_row["IJUAhsHeight3::Height3"] = int(height3)
            
            # Width/plate dimensions
            width1 = clamp.get("width1")
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = int(width1)
                
            width2 = clamp.get("width2")
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = int(width2)
            
            # Rod connection point
            rodTakeOut = clamp.get("rodTakeOut")
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = int(rodTakeOut)

            # Gap dimensions if applicable
            gap1 = clamp.get("gap1")
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = float(gap1)

            gap2 = clamp.get("gap2")
            if gap2 is not None:
                mapped_row["IJUAhsGap2::Gap2"] = float(gap2)

            # Sweep angle
            angle1 = clamp.get("angle1")
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = float(angle1)

            # Pin / stud dimensions
            pin1Length = clamp.get("pin1Length")
            if pin1Length is not None:
                mapped_row["IJUAhsPin1Length::Pin1Length"] = float(pin1Length)

            pin1Diameter = clamp.get("pin1Diameter")
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1Diameter::Pin1Diameter"] = float(pin1Diameter)

            # Bolt offset for multi-bolt configurations
            offset1 = clamp.get("offset1")
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = float(offset1)

            # Number of bolts
            numberOfBolts = clamp.get("numberOfBolts")
            if numberOfBolts is not None:
                mapped_row["IJUAhsNumberOfBolts::NumberOfBolts"] = int(numberOfBolts)

            # Multi-location parameters
            multiQty = clamp.get("multiQty")
            if multiQty is not None:
                mapped_row["IJUAhsMultiQty::MultiQty"] = int(multiQty)

            multiLocatedBy = clamp.get("multiLocatedBy")
            if multiLocatedBy is not None:
                mapped_row["IJUAhsMultiLocatedBy::MultiLocatedBy"] = str(multiLocatedBy)

            multiLocation = clamp.get("multiLocation")
            if multiLocation is not None:
                mapped_row["IJUAhsMultiLocation::MultiLocation"] = float(multiLocation)

            mapped_data.append(mapped_row)

    elif part_type.lower() == "elbow_lug":
        for elbow in vector_json:
            Name = elbow.get("name")
            mapped_row = {"PartNumber": Name}

            # Basic attributes
            rodDiameter = elbow.get("rodDiameter")
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = float(rodDiameter)

            pipeOD = elbow.get("pipeOD")
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = float(pipeOD)

            elbowRadius = elbow.get("elbowRadius")
            if elbowRadius is not None:
                mapped_row["IJOAhsElbow::ElbowRadius"] = float(elbowRadius)

            faceToCenter = elbow.get("faceToCenter")
            if faceToCenter is not None:
                mapped_row["IJOAhsElbow::FaceToCenter"] = float(faceToCenter)

            # Lug shape attributes
            topShape = elbow.get("topShape")
            if topShape is not None:
                mapped_row["IJUAhsLug::TopShape"] = int(topShape)

            angle1 = elbow.get("angle1")
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = float(angle1)

            rodTakeOut = elbow.get("rodTakeOut")
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = float(rodTakeOut)

            width1 = elbow.get("width1")
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = float(width1)

            width2 = elbow.get("width2")
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = float(width2)

            angle2 = elbow.get("angle2")
            if angle2 is not None:
                mapped_row["IJUAhsAngle2::Angle2"] = float(angle2)

            angle3 = elbow.get("angle3")
            if angle3 is not None:
                mapped_row["IJUAhsAngle3::Angle3"] = float(angle3)

            angle4 = elbow.get("angle4")
            if angle4 is not None:
                mapped_row["IJUAhsAngle4::Angle4"] = float(angle4)

            thickness1 = elbow.get("thickness1")
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = float(thickness1)

            gap1 = elbow.get("gap1")
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = float(gap1)

            stiffenerOffset = elbow.get("stiffenerOffset")
            if stiffenerOffset is not None:
                mapped_row["IJUAhsLug::StiffenerOffset"] = float(stiffenerOffset)

            stiffenerHeight = elbow.get("stiffenerHeight")
            if stiffenerHeight is not None:
                mapped_row["IJUAhsLug::StiffenerHeight"] = float(stiffenerHeight)

            stiffenerLength = elbow.get("stiffenerLength")
            if stiffenerLength is not None:
                mapped_row["IJUAhsLug::StiffenerLength"] = float(stiffenerLength)

            offset1 = elbow.get("offset1")
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = float(offset1)

            chamfLength = elbow.get("chamfLength")
            if chamfLength is not None:
                mapped_row["IJUAhsLug::ChamfLength"] = float(chamfLength)

            radiusActual = elbow.get("radiusActual")
            if radiusActual is not None:
                mapped_row["IJUAhsLug::RadiusActual"] = float(radiusActual)

            pin1Diameter = elbow.get("pin1Diameter")
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = float(pin1Diameter)

            pin1Length = elbow.get("pin1Length")
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = float(pin1Length)

            mapped_data.append(mapped_row)

    elif part_type.lower() == "lug":
        for lug in vector_json:
            Name = lug.get("name")
            mapped_row = {"PartNumber": Name}

            # Basic attributes
            rodDiameter = lug.get("rodDiameter")
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = float(rodDiameter)

            pipeOD = lug.get("pipeOD")
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = float(pipeOD)

            rodTakeOut = lug.get("rodTakeOut")
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = float(rodTakeOut)

            isPerpendicular = lug.get("isPerpendicular")
            if isPerpendicular is not None:
                mapped_row["IJUAhsIsPerpendicular::IsPerpendicular"] = int(isPerpendicular)

            # Side attributes
            topShape = lug.get("topShape")
            if topShape is not None:
                mapped_row["IJUAhsLug::TopShape"] = int(topShape)

            angle1 = lug.get("angle1")
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = float(angle1)

            width1 = lug.get("width1")
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = float(width1)

            width2 = lug.get("width2")
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = float(width2)

            angle2 = lug.get("angle2")
            if angle2 is not None:
                mapped_row["IJUAhsAngle2::Angle2"] = float(angle2)

            angle3 = lug.get("angle3")
            if angle3 is not None:
                mapped_row["IJUAhsAngle3::Angle3"] = float(angle3)

            thickness1 = lug.get("thickness1")
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = float(thickness1)

            gap1 = lug.get("gap1")
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = float(gap1)

            stiffenerOffset = lug.get("stiffenerOffset")
            if stiffenerOffset is not None:
                mapped_row["IJUAhsLug::StiffenerOffset"] = float(stiffenerOffset)

            stiffenerHeight = lug.get("stiffenerHeight")
            if stiffenerHeight is not None:
                mapped_row["IJUAhsLug::StiffenerHeight"] = float(stiffenerHeight)

            stiffenerLength = lug.get("stiffenerLength")
            if stiffenerLength is not None:
                mapped_row["IJUAhsLug::StiffenerLength"] = float(stiffenerLength)

            offset1 = lug.get("offset1")
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = float(offset1)

            chamfLength = lug.get("chamfLength")
            if chamfLength is not None:
                mapped_row["IJUAhsLug::ChamfLength"] = float(chamfLength)

            pin1Diameter = lug.get("pin1Diameter")
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = float(pin1Diameter)

            pin1Length = lug.get("pin1Length")
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = float(pin1Length)

            height2 = lug.get("height2")
            if height2 is not None:
                mapped_row["IJUAhsHeight2::Height2"] = float(height2)

            mapped_data.append(mapped_row)

    return mapped_data