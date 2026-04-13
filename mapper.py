def _to_int(v):
    """Convert v to int via float, returning None on failure."""
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _to_float(v):
    """Convert v to float, returning None on failure."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def map_to_excel_fields(vector_json, part_type):

    if not isinstance(vector_json, list):
        raise ValueError("Expected list from AI output")

    mapped_data = []

    if part_type.lower() == "plate":
        for plate in vector_json:
            mapped_row = {"PartNumber": plate.get("name")}

            for suffix in ("1", "2", "3"):
                w = _to_int(plate.get(f"width{suffix}"))
                if w is not None:
                    mapped_row[f"IJUAhsWidth{suffix}::Width{suffix}"] = w

                l = _to_int(plate.get(f"length{suffix}"))
                if l is not None:
                    mapped_row[f"IJUAhsLength{suffix}::Length{suffix}"] = l

                t = _to_int(plate.get(f"thickness{suffix}"))
                if t is not None:
                    mapped_row[f"IJUAhsThickness{suffix}::Thickness{suffix}"] = t

            mapped_data.append(mapped_row)

    elif part_type.lower() == "ubolt":
        for ubolt in vector_json:
            mapped_row = {"PartNumber": ubolt.get("name")}

            uBoltWidth = _to_int(ubolt.get("uBoltWidth"))
            if uBoltWidth is not None:
                mapped_row["IJUAhsUBolt::UBoltWidth"] = uBoltWidth

            # Support both 'uBoltCenterToEnd' (current) and legacy 'uBoltLength' key names
            raw_length = ubolt.get("uBoltCenterToEnd") or ubolt.get("uBoltLength")
            uBoltLength = _to_int(raw_length)
            if uBoltLength is not None:
                mapped_row["IJUAhsUBolt::UBoltCenterToEnd"] = uBoltLength

            uBoltRodDia = _to_int(ubolt.get("uBoltRodDia"))
            if uBoltRodDia is not None:
                mapped_row["IJUAhsUBolt::UBoltRodDia"] = uBoltRodDia

            uBoltFlatSpot = _to_int(ubolt.get("uBoltFlatSpot"))
            if uBoltFlatSpot is not None:
                mapped_row["IJUAhsUBolt::UBoltFlatSpot"] = uBoltFlatSpot

            uBoltDia2 = _to_float(ubolt.get("uBoltDia2"))
            if uBoltDia2 is not None:
                mapped_row["IJUAhsUBolt::UBoltDia2"] = uBoltDia2

            uBoltDia2Start = _to_float(ubolt.get("uBoltDia2Start"))
            if uBoltDia2Start is not None:
                mapped_row["IJUAhsUBolt::UBoltDia2Start"] = uBoltDia2Start

            uBoltTopGap = _to_float(ubolt.get("uBoltTopGap"))
            if uBoltTopGap is not None:
                mapped_row["IJUAhsUBolt::UBoltTopGap"] = uBoltTopGap

            isJBolt = _to_int(ubolt.get("isJBolt"))
            if isJBolt is not None:
                mapped_row["IJUAhsUBolt::IsJBolt"] = isJBolt

            mapped_data.append(mapped_row)

    elif part_type.lower() == "clamp":
        for clamp in vector_json:
            mapped_row = {"PartNumber": clamp.get("name")}

            size = clamp.get("size")
            if size is not None:
                mapped_row["IJUAhsSize::Size"] = str(size)

            diameter1 = _to_int(clamp.get("diameter1"))
            if diameter1 is not None:
                mapped_row["IJUAhsDiameter1::Diameter1"] = diameter1

            diameter2 = _to_int(clamp.get("diameter2"))
            if diameter2 is not None:
                mapped_row["IJUAhsDiameter2::Diameter2"] = diameter2

            thickness1 = _to_int(clamp.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            thickness2 = _to_int(clamp.get("thickness2"))
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = thickness2

            height1 = _to_int(clamp.get("height1"))
            if height1 is not None:
                mapped_row["IJUAhsHeight1::Height1"] = height1

            height2 = _to_int(clamp.get("height2"))
            if height2 is not None:
                mapped_row["IJUAhsHeight2::Height2"] = height2

            height3 = _to_int(clamp.get("height3"))
            if height3 is not None:
                mapped_row["IJUAhsHeight3::Height3"] = height3

            width1 = _to_int(clamp.get("width1"))
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = width1

            width2 = _to_int(clamp.get("width2"))
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = width2

            rodTakeOut = _to_int(clamp.get("rodTakeOut"))
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = rodTakeOut

            gap1 = _to_float(clamp.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            gap2 = _to_float(clamp.get("gap2"))
            if gap2 is not None:
                mapped_row["IJUAhsGap2::Gap2"] = gap2

            angle1 = _to_float(clamp.get("angle1"))
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = angle1

            pin1Length = _to_float(clamp.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1Length::Pin1Length"] = pin1Length

            pin1Diameter = _to_float(clamp.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1Diameter::Pin1Diameter"] = pin1Diameter

            offset1 = _to_float(clamp.get("offset1"))
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = offset1

            numberOfBolts = _to_int(clamp.get("numberOfBolts"))
            if numberOfBolts is not None:
                mapped_row["IJUAhsNumberOfBolts::NumberOfBolts"] = numberOfBolts

            multiQty = _to_int(clamp.get("multiQty"))
            if multiQty is not None:
                mapped_row["IJUAhsMultiQty::MultiQty"] = multiQty

            multiLocatedBy = clamp.get("multiLocatedBy")
            if multiLocatedBy is not None:
                mapped_row["IJUAhsMultiLocatedBy::MultiLocatedBy"] = str(multiLocatedBy)

            multiLocation = _to_float(clamp.get("multiLocation"))
            if multiLocation is not None:
                mapped_row["IJUAhsMultiLocation::MultiLocation"] = multiLocation

            mapped_data.append(mapped_row)

    elif part_type.lower() == "elbow_lug":
        for elbow in vector_json:
            mapped_row = {"PartNumber": elbow.get("name")}

            rodDiameter = _to_float(elbow.get("rodDiameter"))
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = rodDiameter

            pipeOD = _to_float(elbow.get("pipeOD"))
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = pipeOD

            elbowRadius = _to_float(elbow.get("elbowRadius"))
            if elbowRadius is not None:
                mapped_row["IJOAhsElbow::ElbowRadius"] = elbowRadius

            faceToCenter = _to_float(elbow.get("faceToCenter"))
            if faceToCenter is not None:
                mapped_row["IJOAhsElbow::FaceToCenter"] = faceToCenter

            topShape = _to_int(elbow.get("topShape"))
            if topShape is not None:
                mapped_row["IJUAhsLug::TopShape"] = topShape

            angle1 = _to_float(elbow.get("angle1"))
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = angle1

            rodTakeOut = _to_float(elbow.get("rodTakeOut"))
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = rodTakeOut

            width1 = _to_float(elbow.get("width1"))
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = width1

            width2 = _to_float(elbow.get("width2"))
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = width2

            angle2 = _to_float(elbow.get("angle2"))
            if angle2 is not None:
                mapped_row["IJUAhsAngle2::Angle2"] = angle2

            angle3 = _to_float(elbow.get("angle3"))
            if angle3 is not None:
                mapped_row["IJUAhsAngle3::Angle3"] = angle3

            angle4 = _to_float(elbow.get("angle4"))
            if angle4 is not None:
                mapped_row["IJUAhsAngle4::Angle4"] = angle4

            thickness1 = _to_float(elbow.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            gap1 = _to_float(elbow.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            stiffenerOffset = _to_float(elbow.get("stiffenerOffset"))
            if stiffenerOffset is not None:
                mapped_row["IJUAhsLug::StiffenerOffset"] = stiffenerOffset

            stiffenerHeight = _to_float(elbow.get("stiffenerHeight"))
            if stiffenerHeight is not None:
                mapped_row["IJUAhsLug::StiffenerHeight"] = stiffenerHeight

            stiffenerLength = _to_float(elbow.get("stiffenerLength"))
            if stiffenerLength is not None:
                mapped_row["IJUAhsLug::StiffenerLength"] = stiffenerLength

            offset1 = _to_float(elbow.get("offset1"))
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = offset1

            chamfLength = _to_float(elbow.get("chamfLength"))
            if chamfLength is not None:
                mapped_row["IJUAhsLug::ChamfLength"] = chamfLength

            radiusActual = _to_float(elbow.get("radiusActual"))
            if radiusActual is not None:
                mapped_row["IJUAhsLug::RadiusActual"] = radiusActual

            pin1Diameter = _to_float(elbow.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = pin1Diameter

            pin1Length = _to_float(elbow.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = pin1Length

            mapped_data.append(mapped_row)

    elif part_type.lower() == "lug":
        for lug in vector_json:
            mapped_row = {"PartNumber": lug.get("name")}

            rodDiameter = _to_float(lug.get("rodDiameter"))
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = rodDiameter

            pipeOD = _to_float(lug.get("pipeOD"))
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = pipeOD

            rodTakeOut = _to_float(lug.get("rodTakeOut"))
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = rodTakeOut

            isPerpendicular = _to_int(lug.get("isPerpendicular"))
            if isPerpendicular is not None:
                mapped_row["IJUAhsIsPerpendicular::IsPerpendicular"] = isPerpendicular

            topShape = _to_int(lug.get("topShape"))
            if topShape is not None:
                mapped_row["IJUAhsLug::TopShape"] = topShape

            angle1 = _to_float(lug.get("angle1"))
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = angle1

            width1 = _to_float(lug.get("width1"))
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = width1

            width2 = _to_float(lug.get("width2"))
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = width2

            angle2 = _to_float(lug.get("angle2"))
            if angle2 is not None:
                mapped_row["IJUAhsAngle2::Angle2"] = angle2

            angle3 = _to_float(lug.get("angle3"))
            if angle3 is not None:
                mapped_row["IJUAhsAngle3::Angle3"] = angle3

            thickness1 = _to_float(lug.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            gap1 = _to_float(lug.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            stiffenerOffset = _to_float(lug.get("stiffenerOffset"))
            if stiffenerOffset is not None:
                mapped_row["IJUAhsLug::StiffenerOffset"] = stiffenerOffset

            stiffenerHeight = _to_float(lug.get("stiffenerHeight"))
            if stiffenerHeight is not None:
                mapped_row["IJUAhsLug::StiffenerHeight"] = stiffenerHeight

            stiffenerLength = _to_float(lug.get("stiffenerLength"))
            if stiffenerLength is not None:
                mapped_row["IJUAhsLug::StiffenerLength"] = stiffenerLength

            offset1 = _to_float(lug.get("offset1"))
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = offset1

            chamfLength = _to_float(lug.get("chamfLength"))
            if chamfLength is not None:
                mapped_row["IJUAhsLug::ChamfLength"] = chamfLength

            pin1Diameter = _to_float(lug.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = pin1Diameter

            pin1Length = _to_float(lug.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = pin1Length

            height2 = _to_float(lug.get("height2"))
            if height2 is not None:
                mapped_row["IJUAhsHeight2::Height2"] = height2

            mapped_data.append(mapped_row)

    elif part_type.lower() == "bolt":
        for bolt in vector_json:
            mapped_row = {"PartNumber": bolt.get("name")}

            shape1Type = bolt.get("shape1Type")
            if shape1Type is not None:
                mapped_row["IJUAhsBHShape::Shape1Type"] = str(shape1Type)

            shape1Width1 = _to_float(bolt.get("shape1Width1"))
            if shape1Width1 is not None:
                mapped_row["IJUAhsBHShape::Shape1Width1"] = shape1Width1

            shape1Width2 = _to_float(bolt.get("shape1Width2"))
            if shape1Width2 is not None:
                mapped_row["IJUAhsBHShape::Shape1Width2"] = shape1Width2

            thickness1 = _to_float(bolt.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            rodDiameter1 = _to_float(bolt.get("rodDiameter1"))
            if rodDiameter1 is not None:
                mapped_row["IJUAhsRodDiameter1::RodDiameter1"] = rodDiameter1

            length = _to_float(bolt.get("length"))
            if length is not None:
                mapped_row["IJUAhsLength::Length"] = length

            overLength1 = _to_float(bolt.get("overLength1"))
            if overLength1 is not None:
                mapped_row["IJUAhsOverLength1::OverLength1"] = overLength1

            shape2Type = bolt.get("shape2Type")
            if shape2Type is not None:
                mapped_row["IJUAhsNutShape::Shape2Type"] = str(shape2Type)

            shape2Width1 = _to_float(bolt.get("shape2Width1"))
            if shape2Width1 is not None:
                mapped_row["IJUAhsNutShape::Shape2Width1"] = shape2Width1

            shape2Width2 = _to_float(bolt.get("shape2Width2"))
            if shape2Width2 is not None:
                mapped_row["IJUAhsNutShape::Shape2Width2"] = shape2Width2

            thickness2 = _to_float(bolt.get("thickness2"))
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = thickness2

            shape3Type = bolt.get("shape3Type")
            if shape3Type is not None:
                mapped_row["IJUAhsWPlateShape::Shape3Type"] = str(shape3Type)

            shape3Width1 = _to_float(bolt.get("shape3Width1"))
            if shape3Width1 is not None:
                mapped_row["IJUAhsWPlateShape::Shape3Width1"] = shape3Width1

            shape3Width2 = _to_float(bolt.get("shape3Width2"))
            if shape3Width2 is not None:
                mapped_row["IJUAhsWPlateShape::Shape3Width2"] = shape3Width2

            thickness3 = _to_float(bolt.get("thickness3"))
            if thickness3 is not None:
                mapped_row["IJUAhsThickness3::Thickness3"] = thickness3

            twPlateCount = _to_int(bolt.get("twPlateCount"))
            if twPlateCount is not None:
                mapped_row["IJUAhsTWPlateCount::TWPlateCount"] = twPlateCount

            bwPlateCount = _to_int(bolt.get("bwPlateCount"))
            if bwPlateCount is not None:
                mapped_row["IJUAhsBWPlateCount::BWPlateCount"] = bwPlateCount

            gap1 = _to_float(bolt.get("gap1"))
            if gap1 is not None:
                mapped_row["IJOAhsGap1::Gap1"] = gap1

            mapped_data.append(mapped_row)

    elif part_type.lower() == "nut":
        for nut in vector_json:
            mapped_row = {"PartNumber": nut.get("name")}

            rodDiameter = _to_float(nut.get("rodDiameter"))
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = rodDiameter

            shape1Type = nut.get("shape1Type")
            if shape1Type is not None:
                mapped_row["IJUAhsShape1::Shape1Type"] = str(shape1Type)

            shape1Width1 = _to_float(nut.get("shape1Width1"))
            if shape1Width1 is not None:
                mapped_row["IJUAhsShape1::Shape1Width1"] = shape1Width1

            shape1Width2 = _to_float(nut.get("shape1Width2"))
            if shape1Width2 is not None:
                mapped_row["IJUAhsShape1::Shape1Width2"] = shape1Width2

            shape1Length = _to_float(nut.get("shape1Length"))
            if shape1Length is not None:
                mapped_row["IJUAhsShape1::Shape1Length"] = shape1Length

            mapped_data.append(mapped_row)

    elif part_type.lower() == "pin":
        for pin in vector_json:
            mapped_row = {"PartNumber": pin.get("name")}

            pin1Diameter = _to_float(pin.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = pin1Diameter

            pin1Length = _to_float(pin.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = pin1Length

            cotterDia = _to_float(pin.get("cotterDia"))
            if cotterDia is not None:
                mapped_row["IJUAhsCotter1::CotterDia"] = cotterDia

            cotterLength = _to_float(pin.get("cotterLength"))
            if cotterLength is not None:
                mapped_row["IJUAhsCotter1::CotterLength"] = cotterLength

            cotterOffset = _to_float(pin.get("cotterOffset"))
            if cotterOffset is not None:
                mapped_row["IJUAhsCotter1::CotterOffset"] = cotterOffset

            mapped_data.append(mapped_row)

    elif part_type.lower() == "clevis":
        for clevis in vector_json:
            mapped_row = {"PartNumber": clevis.get("name")}

            rodDiameter = _to_float(clevis.get("rodDiameter"))
            if rodDiameter is not None:
                mapped_row["IJUAhsRodDiameter::RodDiameter"] = rodDiameter

            rodTakeOut = _to_float(clevis.get("rodTakeOut"))
            if rodTakeOut is not None:
                mapped_row["IJUAhsRodTakeOut::RodTakeOut"] = rodTakeOut

            opening1 = _to_float(clevis.get("opening1"))
            if opening1 is not None:
                mapped_row["IJUAhsOpening1::Opening1"] = opening1

            shape1Type = clevis.get("shape1Type")
            if shape1Type is not None:
                mapped_row["IJUAhsShape1::Shape1Type"] = str(shape1Type)

            shape1Width1 = _to_float(clevis.get("shape1Width1"))
            if shape1Width1 is not None:
                mapped_row["IJUAhsShape1::Shape1Width1"] = shape1Width1

            shape1Width2 = _to_float(clevis.get("shape1Width2"))
            if shape1Width2 is not None:
                mapped_row["IJUAhsShape1::Shape1Width2"] = shape1Width2

            shape1Length = _to_float(clevis.get("shape1Length"))
            if shape1Length is not None:
                mapped_row["IJUAhsShape1::Shape1Length"] = shape1Length

            diameter2 = _to_float(clevis.get("diameter2"))
            if diameter2 is not None:
                mapped_row["IJUAhsDiameter2::Diameter2"] = diameter2

            thickness2 = _to_float(clevis.get("thickness2"))
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = thickness2

            gap2 = _to_float(clevis.get("gap2"))
            if gap2 is not None:
                mapped_row["IJUAhsGap2::Gap2"] = gap2

            width3 = _to_float(clevis.get("width3"))
            if width3 is not None:
                mapped_row["IJUAhsWidth3::Width3"] = width3

            gap3 = _to_float(clevis.get("gap3"))
            if gap3 is not None:
                mapped_row["IJUAhsGap3::Gap3"] = gap3

            overLength1 = _to_float(clevis.get("overLength1"))
            if overLength1 is not None:
                mapped_row["IJUAhsOverLength1::OverLength1"] = overLength1

            overLength2 = _to_float(clevis.get("overLength2"))
            if overLength2 is not None:
                mapped_row["IJUAhsOverLength2::OverLength2"] = overLength2

            pin1Diameter = _to_float(clevis.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = pin1Diameter

            pin1Length = _to_float(clevis.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = pin1Length

            mapped_data.append(mapped_row)

    elif part_type.lower() == "rod":
        for rod in vector_json:
            mapped_row = {"PartNumber": rod.get("name")}

            rodDiameter1 = _to_float(rod.get("rodDiameter1"))
            if rodDiameter1 is not None:
                mapped_row["IJUAhsRodDiameter1::RodDiameter1"] = rodDiameter1

            length = _to_float(rod.get("length"))
            if length is not None:
                mapped_row["IJUAhsLength::Length"] = length

            wtPerLen = _to_float(rod.get("wtPerLen"))
            if wtPerLen is not None:
                mapped_row["IJUAhsWtPerLen::WtPerLen"] = wtPerLen

            weight = _to_float(rod.get("weight"))
            if weight is not None:
                mapped_row["IJUAhsWeight::Weight"] = weight

            rodEnd1Type = rod.get("rodEnd1Type")
            if rodEnd1Type is not None:
                mapped_row["IJUAhsRodEnd1::RodEnd1Type"] = str(rodEnd1Type)

            rodEnd2Type = rod.get("rodEnd2Type")
            if rodEnd2Type is not None:
                mapped_row["IJUAhsRodEnd2::RodEnd2Type"] = str(rodEnd2Type)

            rodCenterType = rod.get("rodCenterType")
            if rodCenterType is not None:
                mapped_row["IJUAhsRodCenterType::RodCenterType"] = str(rodCenterType)

            offset1 = _to_float(rod.get("offset1"))
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = offset1

            thickness1 = _to_float(rod.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            length1 = _to_float(rod.get("length1"))
            if length1 is not None:
                mapped_row["IJUAhsLength1::Length1"] = length1

            diameter1 = _to_float(rod.get("diameter1"))
            if diameter1 is not None:
                mapped_row["IJUAhsDiameter1::Diameter1"] = diameter1

            overLength1 = _to_float(rod.get("overLength1"))
            if overLength1 is not None:
                mapped_row["IJUAhsOverLength1::OverLength1"] = overLength1

            overLength2 = _to_float(rod.get("overLength2"))
            if overLength2 is not None:
                mapped_row["IJUAhsOverLength2::OverLength2"] = overLength2

            minLen = _to_float(rod.get("minLen"))
            if minLen is not None:
                mapped_row["IJUAhsMinLen::MinLen"] = minLen

            maxLen = _to_float(rod.get("maxLen"))
            if maxLen is not None:
                mapped_row["IJUAhsMaxLen::MaxLen"] = maxLen

            mapped_data.append(mapped_row)

    elif part_type.lower() == "shoe":
        for shoe in vector_json:
            mapped_row = {"PartNumber": shoe.get("name")}

            shoeShape = shoe.get("shoeShape")
            if shoeShape is not None:
                mapped_row["IJUAhsShoeShape::ShoeShape"] = str(shoeShape)

            shoeHeight = _to_float(shoe.get("shoeHeight"))
            if shoeHeight is not None:
                mapped_row["IJOAhsShoeHeight::ShoeHeight"] = shoeHeight

            shoeWidth = _to_float(shoe.get("shoeWidth"))
            if shoeWidth is not None:
                mapped_row["IJUAhsShoeWidth::ShoeWidth"] = shoeWidth

            shoeLength = _to_float(shoe.get("shoeLength"))
            if shoeLength is not None:
                mapped_row["IJUAhsShoeLength::ShoeLength"] = shoeLength

            shoeGap = _to_float(shoe.get("shoeGap"))
            if shoeGap is not None:
                mapped_row["IJOAhsShoeGap::ShoeGap"] = shoeGap

            diameter1 = _to_float(shoe.get("diameter1"))
            if diameter1 is not None:
                mapped_row["IJOAhsDiamter1::Diamter1"] = diameter1

            slopeAngle = _to_float(shoe.get("slopeAngle"))
            if slopeAngle is not None:
                mapped_row["IJOAhsSlopeAngle::SlopeAngle"] = slopeAngle

            shoeQty = _to_int(shoe.get("shoeQty"))
            if shoeQty is not None:
                mapped_row["IJUAhsShoeQty::ShoeQty"] = shoeQty

            insulationTh = _to_float(shoe.get("insulationTh"))
            if insulationTh is not None:
                mapped_row["IJOAhsInsulationTh::InsulationTh"] = insulationTh

            insulationLength = _to_float(shoe.get("insulationLength"))
            if insulationLength is not None:
                mapped_row["IJOAhsInsulationL::InsulationLength"] = insulationLength

            legSpace = _to_float(shoe.get("legSpace"))
            if legSpace is not None:
                mapped_row["IJUAhsShoeLegSpace::LegSpace"] = legSpace

            legLowSpace = _to_float(shoe.get("legLowSpace"))
            if legLowSpace is not None:
                mapped_row["IJUAhsShoeLegLowSpace::LegLowSpace"] = legLowSpace

            endPlateNum = _to_int(shoe.get("endPlateNum"))
            if endPlateNum is not None:
                mapped_row["IJUAhsShoeEndPlate::EndPlateNum"] = endPlateNum

            endPlateHeight = _to_float(shoe.get("endPlateHeight"))
            if endPlateHeight is not None:
                mapped_row["IJOAhsShoeEndPlate::EndPlateHeight"] = endPlateHeight

            endPlateOffset = _to_float(shoe.get("endPlateOffset"))
            if endPlateOffset is not None:
                mapped_row["IJUAhsEndPlateOffset::EndPlateOffset"] = endPlateOffset

            plateShape = shoe.get("plateShape")
            if plateShape is not None:
                mapped_row["IJUAhsShoeEndPlate::PlateShape"] = str(plateShape)

            repadShape = shoe.get("repadShape")
            if repadShape is not None:
                mapped_row["IJUAhsRepadShape::RepadShape"] = str(repadShape)

            mapped_data.append(mapped_row)

    elif part_type.lower() == "strap":
        for strap in vector_json:
            mapped_row = {"PartNumber": strap.get("name")}

            strapWidthInside = _to_float(strap.get("strapWidthInside"))
            if strapWidthInside is not None:
                mapped_row["IJUAhsStrap::StrapWidthInside"] = strapWidthInside

            strapHeightInside = _to_float(strap.get("strapHeightInside"))
            if strapHeightInside is not None:
                mapped_row["IJUAhsStrap::StrapHeightInside"] = strapHeightInside

            strapThickness = _to_float(strap.get("strapThickness"))
            if strapThickness is not None:
                mapped_row["IJUAhsStrap::StrapThickness"] = strapThickness

            strapStockWidth = _to_float(strap.get("strapStockWidth"))
            if strapStockWidth is not None:
                mapped_row["IJUAhsStrap::StrapStockWidth"] = strapStockWidth

            strapFlatSpot = _to_float(strap.get("strapFlatSpot"))
            if strapFlatSpot is not None:
                mapped_row["IJUAhsStrap::StrapFlatSpot"] = strapFlatSpot

            strapTopGap = _to_float(strap.get("strapTopGap"))
            if strapTopGap is not None:
                mapped_row["IJOAhsStrapGap::StrapTopGap"] = strapTopGap

            strapWidthWings = _to_float(strap.get("strapWidthWings"))
            if strapWidthWings is not None:
                mapped_row["IJUAhsStrap::StrapWidthWings"] = strapWidthWings

            strapOneSided = _to_int(strap.get("strapOneSided"))
            if strapOneSided is not None:
                mapped_row["IJUAhsStrap::StrapOneSided"] = strapOneSided

            strapSplitGap = _to_float(strap.get("strapSplitGap"))
            if strapSplitGap is not None:
                mapped_row["IJUAhsStrap::StrapSplitGap"] = strapSplitGap

            strapSplitExtension = _to_float(strap.get("strapSplitExtension"))
            if strapSplitExtension is not None:
                mapped_row["IJUAhsStrap::StrapSplitExtension"] = strapSplitExtension

            pin1Diameter = _to_float(strap.get("pin1Diameter"))
            if pin1Diameter is not None:
                mapped_row["IJUAhsPin1::Pin1Diameter"] = pin1Diameter

            pin1Length = _to_float(strap.get("pin1Length"))
            if pin1Length is not None:
                mapped_row["IJUAhsPin1::Pin1Length"] = pin1Length

            multi1Qty = _to_int(strap.get("multi1Qty"))
            if multi1Qty is not None:
                mapped_row["IJUAhsMulti1::Multi1Qty"] = multi1Qty

            multi1LocateBy = strap.get("multi1LocateBy")
            if multi1LocateBy is not None:
                mapped_row["IJUAhsMulti1::Multi1LocateBy"] = str(multi1LocateBy)

            multi1Location = _to_float(strap.get("multi1Location"))
            if multi1Location is not None:
                mapped_row["IJUAhsMulti1::Multi1Location"] = multi1Location

            gap1 = _to_float(strap.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            height1 = _to_float(strap.get("height1"))
            if height1 is not None:
                mapped_row["IJUAhsHeight1::Height1"] = height1

            width1 = _to_float(strap.get("width1"))
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = width1

            length1 = _to_float(strap.get("length1"))
            if length1 is not None:
                mapped_row["IJUAhsLength1::Length1"] = length1

            pipeOD = _to_float(strap.get("pipeOD"))
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = pipeOD

            mapped_data.append(mapped_row)

    elif part_type.lower() == "shield":
        for shield in vector_json:
            mapped_row = {"PartNumber": shield.get("name")}

            pipeOD = _to_float(shield.get("pipeOD"))
            if pipeOD is not None:
                mapped_row["IJOAhsPipeOD::PipeOD"] = pipeOD

            size = shield.get("size")
            if size is not None:
                mapped_row["IJUAhsSize::Size"] = str(size)

            thickness1 = _to_float(shield.get("thickness1"))
            if thickness1 is not None:
                mapped_row["IJUAhsThickness1::Thickness1"] = thickness1

            length1 = _to_float(shield.get("length1"))
            if length1 is not None:
                mapped_row["IJUAhsLength1::Length1"] = length1

            angle1 = _to_float(shield.get("angle1"))
            if angle1 is not None:
                mapped_row["IJUAhsAngle1::Angle1"] = angle1

            angle2 = _to_float(shield.get("angle2"))
            if angle2 is not None:
                mapped_row["IJUAhsAngle2::Angle2"] = angle2

            width1 = _to_float(shield.get("width1"))
            if width1 is not None:
                mapped_row["IJUAhsWidth1::Width1"] = width1

            width2 = _to_float(shield.get("width2"))
            if width2 is not None:
                mapped_row["IJUAhsWidth2::Width2"] = width2

            thickness2 = _to_float(shield.get("thickness2"))
            if thickness2 is not None:
                mapped_row["IJUAhsThickness2::Thickness2"] = thickness2

            length2 = _to_float(shield.get("length2"))
            if length2 is not None:
                mapped_row["IJUAhsLength2::Length2"] = length2

            angle3 = _to_float(shield.get("angle3"))
            if angle3 is not None:
                mapped_row["IJUAhsAngle3::Angle3"] = angle3

            angle4 = _to_float(shield.get("angle4"))
            if angle4 is not None:
                mapped_row["IJUAhsAngle4::Angle4"] = angle4

            width3 = _to_float(shield.get("width3"))
            if width3 is not None:
                mapped_row["IJUAhsWidth3::Width3"] = width3

            width4 = _to_float(shield.get("width4"))
            if width4 is not None:
                mapped_row["IJUAhsWidth4::Width4"] = width4

            thickness3 = _to_float(shield.get("thickness3"))
            if thickness3 is not None:
                mapped_row["IJUAhsThickness3::Thickness3"] = thickness3

            angle5 = _to_float(shield.get("angle5"))
            if angle5 is not None:
                mapped_row["IJUAhsAngle5::Angle5"] = angle5

            height1 = _to_float(shield.get("height1"))
            if height1 is not None:
                mapped_row["IJUAhsHeight1::Height1"] = height1

            length3 = _to_float(shield.get("length3"))
            if length3 is not None:
                mapped_row["IJUAhsLength3::Length3"] = length3

            multi1Qty = _to_int(shield.get("multi1Qty"))
            if multi1Qty is not None:
                mapped_row["IJUAhsMulti1::Multi1Qty"] = multi1Qty

            multi1LocateBy = shield.get("multi1LocateBy")
            if multi1LocateBy is not None:
                mapped_row["IJUAhsMulti1::Multi1LocateBy"] = str(multi1LocateBy)

            multi1Location = _to_float(shield.get("multi1Location"))
            if multi1Location is not None:
                mapped_row["IJUAhsMulti1::Multi1Location"] = multi1Location

            diameter1 = _to_float(shield.get("diameter1"))
            if diameter1 is not None:
                mapped_row["IJUAhsDiameter1::Diameter1"] = diameter1

            offset1 = _to_float(shield.get("offset1"))
            if offset1 is not None:
                mapped_row["IJUAhsOffset1::Offset1"] = offset1

            mapped_data.append(mapped_row)

    elif part_type.lower() == "guide":
        for guide in vector_json:
            mapped_row = {"PartNumber": guide.get("name")}

            for suffix in ("1", "2", "3", "4", "5", "6"):
                w = _to_float(guide.get(f"width{suffix}"))
                if w is not None:
                    mapped_row[f"IJUAhsWidth{suffix}::Width{suffix}"] = w

                l = _to_float(guide.get(f"length{suffix}"))
                if l is not None:
                    mapped_row[f"IJUAhslength{suffix}::Length{suffix}"] = l

                t = _to_float(guide.get(f"thickness{suffix}"))
                if t is not None:
                    mapped_row[f"IJUAhsThickness{suffix}::Thickness{suffix}"] = t

            for suffix in ("1", "2", "3", "4"):
                o = _to_float(guide.get(f"offset{suffix}"))
                if o is not None:
                    mapped_row[f"IJUAhsOffset{suffix}::Offset{suffix}"] = o

            for suffix in ("1", "2", "3", "4"):
                a = _to_float(guide.get(f"angle{suffix}"))
                if a is not None:
                    mapped_row[f"IJUAhsAngle{suffix}::Angle{suffix}"] = a

            gap1 = _to_float(guide.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            guideHeight = _to_float(guide.get("guideHeight"))
            if guideHeight is not None:
                mapped_row["IJUAhsGuideHeight::GuideHeight"] = guideHeight

            connection1 = guide.get("connection1")
            if connection1 is not None:
                mapped_row["IJUAhsConnection1::Connection1"] = str(connection1)

            connection2 = guide.get("connection2")
            if connection2 is not None:
                mapped_row["IJUAhsConnection2::Connection2"] = str(connection2)

            multi1Qty = _to_int(guide.get("multi1Qty"))
            if multi1Qty is not None:
                mapped_row["IJUAhsMulti1::Multi1Qty"] = multi1Qty

            multi1LocateBy = guide.get("multi1LocateBy")
            if multi1LocateBy is not None:
                mapped_row["IJUAhsMulti1::Multi1LocateBy"] = str(multi1LocateBy)

            multi1Location = _to_float(guide.get("multi1Location"))
            if multi1Location is not None:
                mapped_row["IJUAhsMulti1::Multi1Location"] = multi1Location

            mapped_data.append(mapped_row)

    elif part_type.lower() == "strut":
        for strut in vector_json:
            mapped_row = {"PartNumber": strut.get("name")}

            length = _to_float(strut.get("length"))
            if length is not None:
                mapped_row["IJUAhsLength::Length"] = length

            stretchShape = strut.get("stretchShape")
            if stretchShape is not None:
                mapped_row["IJUAhsStretchShape::StretchShape"] = str(stretchShape)

            rodEnd1Type = strut.get("rodEnd1Type")
            if rodEnd1Type is not None:
                mapped_row["IJUAhsRodEnd1::RodEnd1Type"] = str(rodEnd1Type)

            length1 = _to_float(strut.get("length1"))
            if length1 is not None:
                mapped_row["IJUAhsLength1::Length1"] = length1

            diameter1 = _to_float(strut.get("diameter1"))
            if diameter1 is not None:
                mapped_row["IJUAhsDiameter1::Diameter1"] = diameter1

            gap1 = _to_float(strut.get("gap1"))
            if gap1 is not None:
                mapped_row["IJUAhsGap1::Gap1"] = gap1

            angle1 = _to_float(strut.get("angle1"))
            if angle1 is not None:
                mapped_row["IJOAhsAngle1::Angle1"] = angle1

            shape1Type = strut.get("shape1Type")
            if shape1Type is not None:
                mapped_row["IJUAhsShape1::Shape1Type"] = str(shape1Type)

            shape1Width1 = _to_float(strut.get("shape1Width1"))
            if shape1Width1 is not None:
                mapped_row["IJUAhsShape1::Shape1Width1"] = shape1Width1

            shape1Width2 = _to_float(strut.get("shape1Width2"))
            if shape1Width2 is not None:
                mapped_row["IJUAhsShape1::Shape1Width2"] = shape1Width2

            shape1Length = _to_float(strut.get("shape1Length"))
            if shape1Length is not None:
                mapped_row["IJUAhsShape1::Shape1Length"] = shape1Length

            minLen = _to_float(strut.get("minLen"))
            if minLen is not None:
                mapped_row["IJUAhsMinLen::MinLen"] = minLen

            maxLen = _to_float(strut.get("maxLen"))
            if maxLen is not None:
                mapped_row["IJUAhsMaxLen::MaxLen"] = maxLen

            wtPerLen = _to_float(strut.get("wtPerLen"))
            if wtPerLen is not None:
                mapped_row["IJUAhsWtPerLen::WtPerLen"] = wtPerLen

            weight = _to_float(strut.get("weight"))
            if weight is not None:
                mapped_row["IJUAhsWeight::Weight"] = weight

            stroke = _to_float(strut.get("stroke"))
            if stroke is not None:
                mapped_row["IJUAhsStroke::Stroke"] = stroke

            mapped_data.append(mapped_row)

    else:
        raise ValueError(f"Unknown part type: {part_type!r}")

    return mapped_data
