---
## Document Metadata

{
  "Product Name": "Intergraph Smart 3D/3Dx",
  "Product Version": "14",
  "Article Source": "Fluid Topics",
  "Article Name": "Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration",
  "Article Date": ""
}
---

# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
ft:locale: en-US
Product: Intergraph Smart 3D
Subproduct: Hangers and Supports
Search by Category: Reference Data
Smart 3D Version: 14

###### [Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325393?contentId=F6H0P7~xSIt9d2TCIuHSWA)
IJUAhsShieldShape::ShieldShape

Specifies the name of the shield. The shield name is required for the shield to be
drawn. For more information on shield shape details, see [Shield Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/zE0Dq8eKkCQI5_YsU~vgQA).

IJUAhsMulti7::Multi7Qty

Specifies the quantity of shields. Shields are not shown when Multi7Qty is set to zero.

IJUAhsMulti7::Multi7LocateBy

Specifies the location of the Shields. Individual shields can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of shields. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti7::Multi7Location

Specifies the distance for exact location of the shields depending on Multi7LocateBy and Multi7Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsShieldOffset1::ShieldOffset1

Offsets the shield(s) along with the sloped pipes.

IJUAhsShieldLength::ShieldLength (Override Property)

Specifies the length of the shoe shield which overrides the Shield Shape Length1,
Length 2 and Length 3 properties.


Image:[Image-Analysis: The image illustrates a diagram representing a mechanical component, likely a type of guide or mount for a moving part. It depicts a rectangular section (highlighted in red) that seems to be a moving guide or part, indicated by the dashed lines and arrows which suggest movement along a track or support structure. At the bottom, there are two vertical elements that could serve as supports or mounting points. The red squares likely indicate points of interest or attachment. Overall, the diagram portrays how one component interacts with another in a mechanical assembly, highlighting their spatial relationships and functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FZfqvrW4jbmx1aRUlGrWyg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FZfqvrW4jbmx1aRUlGrWyg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShieldLengthSel::ShieldLengthSel

Specifies the codelist value for the length of the Shield.

The following values are supported:

1 = Auto - based on the length of the Shoe  
2 = Input - based on the input from the occurrence.

IJUAhsShieldLenOvrHng::ShldLenOvrHng

Specifies the overhang for the Shoe length. If the codelist value of IJUAhsShieldLengthSel::ShieldLengthSel is 1, then the length is based on the length of the Shoe. You can specify overhang
and the IJUAhsShieldLenOvrHng::ShldLenOvrHng attribute controls the overhang.


Image:[Alt-Text: Illustration of Shield Length Overhang - Shoe Attributes 
Image-Analysis: The image depicts a horizontal bar that contains several horizontal lines resembling a grid or a table format. There are indicators on both sides suggesting that the content is meant to slide or scroll horizontally, which implies functionality such as viewing more items or options beyond what is currently visible within the box. This design layout is commonly used in user interfaces for displaying a collection of data or items, like a menu or a list of options that can expand. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9XRKToSgTBSyySaLMuHmoA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Shield Length Overhang - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9XRKToSgTBSyySaLMuHmoA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Stiffner Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325405?contentId=v_S7LSCmRh2pO2TKRyY57A)
IJUAhsShoeStiffener::StiffenerShape

Specifies the name of the stiffener. The stiffener name is required for the stiffener
to be drawn.


Image:[Alt-Text: shoe(Stiffner properties) 
Image-Analysis: The image consists of a series of five illustrations that depict a structural component known as a "stiffener." A stiffener is an additional structural member that is added to strengthen or reinforce various elements in construction or manufacturing. In the images, the stiffeners are represented in various configurations. The first two images show stiffeners placed vertically, while the third image depicts a horizontal stiffener positioned between vertical elements. The fourth image illustrates a different design of a stiffener, likely providing more support with a varied pattern. The last illustration seems to focus on the stiffener's placement in relation to the framework. All the illustrations are labeled with the letter "A" in blue, indicating perhaps that these are different views or types of the same component identified as 'A - Stiffener.' Overall, the series portrays how stiffeners can be utilized in different orientations and designs to enhance structural integrity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vOKieUtRJgjF56s4ss3PtQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe(Stiffner properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vOKieUtRJgjF56s4ss3PtQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

For more information on plate (stiffener) shape details, see [Plate Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/mJQkALuDD6MiGWwj0PYgwg).

IJUAhsMulti8::Multi8Qty

Specifies the quantity of stiffeners. Stiffeners are not shown when Multi8Qty is set to zero.

IJUAhsMulti8::Multi8LocateBy

Specifies the location of the stiffeners. Individual stiffeners can be located in
two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of stiffeners. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti8::Multi8Location

Specifies the distance for exact location of the stiffeners depending on Multi8LocateBy and Multi8Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsStiff::StiffVerticalOffset

Defines the vertical offset of the stiffener with respect to bottom of the shoe.


Image:[Alt-Text: shoe(stiffner properties offset) 
Image-Analysis: The image illustrates a technical drawing related to "Vertical Offset." It depicts a horizontal bar supported by vertical lines, which may represent a structure or a mechanical component. The red dashed lines and vertical arrows indicate the concept of vertical offset, showing a difference in height or positioning between various elements. The label "Vertical Offset" is positioned prominently at the bottom right, indicating that this drawing explains how vertical displacements are addressed in the design or engineering context. The vertical offsets are likely relevant to how components interact in three-dimensional space or how they are adjusted during assembly or operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IPV_5BPMfh3KUR5FGMOtXw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe(stiffner properties offset)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IPV_5BPMfh3KUR5FGMOtXw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStiff::StiffLength

Specifies the maximum height of the Stiffener Plate.


Image:[Alt-Text: Illustration of Stiffener Length - Shoe Attributes 
Image-Analysis: The image depicts a technical illustration of a circular object, likely representing a mechanical part such as a bearing or a coupling assembly. The circular shape suggests it is designed to fit within another component, while the additional structures on either side might represent supports or mounting features. The vertical arrows indicate movement or adjustment capabilities, which could imply that this object is adjustable or movable within its assembly. The two rectangular bases at the bottom may indicate how this component is attached or supported in a larger mechanism. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/a_mK537mv7ffMppzygtkUg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Stiffener Length - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/a_mK537mv7ffMppzygtkUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStiff::StiffCRad

Specifies the radius of the Stiffener Plate curve.


Image:[Alt-Text: Illustration of Stiffener Radius - Shoe Attributes 
Image-Analysis: The image illustrates a basic representation of a dial gauge, which features a circular dial with a needle pointing to a scale. The circular dial is mounted on a base that supports the gauge. The gauge typically measures the pressure, temperature, or other physical properties in a range of applications. The two side supports suggest that it can be mounted securely for accurate readings. The vertical line from the center likely represents the zero point of measurement, while the arrow points to the measurement being taken on the scale. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ELkW7zQoSsmS4jrQlAa6Jg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Stiffener Radius - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ELkW7zQoSsmS4jrQlAa6Jg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStiff::StiffCEndX

Specifies the x-location of the center of the Stiffener Plate curve.


Image:[Alt-Text: Illustration of Stiffener x & y Location - Shoe Attributes 
Image-Analysis: The image depicts a cross-sectional view of a circular storage tank or pressure vessel. It illustrates key components and their relationships. The tank is supported at the bottom by two vertical supports, indicating it might be placed on a platform or base. There are two points labeled "X" and "Y" in red. Point "X" represents the height or level of the liquid inside the tank, while point "Y" is likely related to another dimension, possibly indicating the height of the tank or a measurement related to the liquid level. This setup is commonly used in engineering and storage applications, where monitoring levels and structural support are crucial for safe operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ujweGP3yHRx2xvHkorC5Iw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Stiffener x & y Location - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ujweGP3yHRx2xvHkorC5Iw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStiff::StiffCEndY

Specifies the y-location of the center of the Stiffener Plate curve.


Image:[Alt-Text: Illustration of Stiffener x & y Location - Shoe Attributes 
Image-Analysis: The image depicts a cross-sectional view of a circular storage tank or pressure vessel. It illustrates key components and their relationships. The tank is supported at the bottom by two vertical supports, indicating it might be placed on a platform or base. There are two points labeled "X" and "Y" in red. Point "X" represents the height or level of the liquid inside the tank, while point "Y" is likely related to another dimension, possibly indicating the height of the tank or a measurement related to the liquid level. This setup is commonly used in engineering and storage applications, where monitoring levels and structural support are crucial for safe operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ujweGP3yHRx2xvHkorC5Iw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Stiffener x & y Location - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ujweGP3yHRx2xvHkorC5Iw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Slide Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325409?contentId=d3BYm1jymvN4BMsw~gLuKQ)
IJUAhPlateShape::SlidePlateShape

Specifies the name of the slide plate. The slide plate name is required for the slide
plate to be drawn. For more information on slide plate shape details, see [Slide Plate Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/hvwVsyLWDQ4PnVhjHOkkBA).

IJUAhsMulti9::Multi9Qty

Specifies the quantity of slide plates. Slide plates are not shown when Multi9Qty
is set to zero.

IJUAhsMulti9::Multi9LocateBy

Specifies the location of the slide plates. Individual slide plates can be located
in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of slide plates. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti9::Multi9Location

Specifies the distance for exact location of the slide plates depending on Multi9LocateBy and Multi9Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shield2 Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325413?contentId=~i9xKYtn16S3xC43VrJ0yA)
IJUAhsShield2Shape::Shield2Shape

It is the string specifying the name of the second shield to use. The shield name
is required for the shield to be drawn. For more information on shield shape details,
see [Shield Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/zE0Dq8eKkCQI5_YsU~vgQA).

IJUAhsMulti10::Multi10Qty

Specifies the quantity of shields. Shields are not shown when Multi10Qty is set to
zero.

IJUAhsMulti10::Multi10LocateBy

Specifies the location of the shields. Individual shields can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of shields. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti10::Multi10Location

Specifies the distance for exact location of the shields depending on Multi10LocateBy and Multi10Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsShield2Offset1::Shield2Offset1

Offsets the shield(s) along with the sloped pipes.

IJUAhsShield2Length::Shield2Length

Specifies the length of the shoe Shield2 which overrides the Shield2 Shape Length1,
Length 2, and Length 3 properties.


Image:[Image-Analysis: The image depicts a mechanical or structural element likely related to a system that involves movement or force transfer. The top section is highlighted with red and features arrows pointing outward, suggesting that it is a component that expands or applies pressure. The bottom portion is wider and has two horizontal arrows indicating movement or adjustment capacity. The central red dot could represent a pivot point, alignment mark, or a control mechanism. Overall, the design suggests a functional element used in engineering or machinery for active motion or support. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C2idfV0w1TSgj5j8pQT8ww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C2idfV0w1TSgj5j8pQT8ww-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Additional Plate properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325419?contentId=L~KArBsNGFopxx1vE9zmxw)
IJUAhsAddPlate::AdditionalPlateShape

Specifies the shapes for additional plates. If this value is not set, additional plates
are not drawn.


Image:[Alt-Text: shoe(Additional plate properties1) 
Image-Analysis: The image depicts a mechanical component, likely a part of machinery or equipment, outlined in a circular shape with some internal structures visible. There are red crossed lines, which typically suggest something is prohibited or that certain areas should not be overlapped. A central circular area shows some bolts or attachment points, possibly for securing additional components. The text "Additional Plates" indicates that this component may have optional or extra plates that can be attached to it, hinting at versatility in its configuration or usage. The pink arrow points towards where these additional plates might be considered for installation or assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CHxjpZ~t~eJtzzxTD_ewHg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe(Additional plate properties1)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CHxjpZ~t~eJtzzxTD_ewHg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAddPlate::PlateNumber

Specifies the number of additional plates

IJUAhsAddPlate::CenterDiameter

Specifies the diameter from which the additional plates are drawn.

![shoe(Additional plate properties2)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7bGPht693pCk26b7IIMnww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ee54aeadd55890be)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7bGPht693pCk26b7IIMnww-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAddPlate::PlateRotAngle

Specifies angle by which the plates are rotated about the x-axis of the pipe.

![shoe(Additional plate properties3)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QQeiC0rxJ0sMWMvp_C94BQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=95313ab0c764f705)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QQeiC0rxJ0sMWMvp_C94BQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAddPlate::PlateAngle

Defines the angle between the plates.

IJUAhsAddPlate::AddPlateOffset1

Specifies the offset of the plates along the x-axis of the pipe.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp2 Properties (Shoe) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325428?contentId=eXqjjtoImVyzfb~PBgyIiQ)
IJUAhsClamp2Shape::Clamp2Shape

Specifies the name of the clamp. The clamp name is required for the clamp to be drawn.

![shoe(clamp2 properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6aj6oxWQEaf1UsxO2WrGTg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2bb61c4b9c662f4d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6aj6oxWQEaf1UsxO2WrGTg-_PVFQNoCl4XmjAxWO0f7XQ/content)

For more information on clamp shape details, see [Clamp Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/~XTaC6Du53R6Y0iz~BpDRg).

IJUAhsMulti11::Multi11Qty

Specifies the quantity of clamps. Clamps are not shown when Multi11Qty is set to zero.

IJUAhsMulti11::Multi11LocateBy

Specifies the location of the clamps. Individual clamps can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of clamps. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti11::Multi11Location

Specifies the distance for exact location of the clamps depending on Multi11LocateBy and Multi11Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325381?contentId=CLQfCK5ZGfVuJs9q_SazTg)
IJUAhsStrapShape::StrapShape

Specifies the name of the strap. The strap name is required for the strap to be drawn.
For more information on strap shape details, see [Strap Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/sE4HnPstEhqoCtKNV7gvkg).

IJUAhsMulti4::Multi4Qty

Specifies the quantity of straps. Straps are not shown when Multi4Qty is set to zero.

IJUAhsMulti4::Multi4LocateBy

Specifies the location of the straps. Individual straps can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of straps. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti4::Multi4Location

Specifies the distance for exact location of the straps depending on Multi4LocateBy and Multi4Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rib properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325434?contentId=YV_7DVoA1qDKTbPlcPs33g)
IJUAhsRibShape::RibShape

It is the string specifying the name of the rib plate. The rib plate name is required
for the rib plate to be drawn.

For more information on plate (Rib) shape details, see [Plate Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/mJQkALuDD6MiGWwj0PYgwg).

IJUAhsRibHeight::RibHeight

Specifies the height of the rib plates which overrides the height on the ribshape
sheet.

IJUAhsRibQty::RibQty

Specifies the number of rib rib plates and the location of the rib plates.

IJUAhsRibGap::RibGap

Specifies the gap between the centers of two Rib plates.


Image:[Alt-Text: Rib Gap 
Image-Analysis: The image depicts a schematic representation of a "Rib Gap" used in engineering or design contexts. It features a circular shape represented by a dashed line at the top, which could signify a component that is being supported or connected by vertical lines below it. These vertical lines are likely indicative of "ribs" or structural members that provide support to the circular component. The bottom horizontal line represents a base or platform where these ribs are anchored. The term "Rib Gap" is highlighted at the bottom of the image, suggesting it refers to the space between the ribs, which may be important for structural integrity or functionality in the designed system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GCNxYLE348CRWY1EqRDYqg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Rib Gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GCNxYLE348CRWY1EqRDYqg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Maintenance Aspect Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/665485?contentId=YtcDUIN6qySCxGtxlQKTjA)
IJUAhsMaintenanceTh::MaintenanceThickness

Specifies the maintenance thickness.


Image:[Alt-Text: Illustration of Maintenance Thickness - Shoe Attributes 
Image-Analysis: The image shows a simple diagram of a circular frame, likely representing a globe or spherical object mount. It has two horizontal bars on the left and right sides, which appear to hold the circular frame in place. The frame may symbolize a rotating globe or a mechanism for displaying a spherical item, as suggested by the arrows on the right side indicating movement or rotation. The vertical base at the bottom supports the entire structure, signifying that the circular frame is meant to stand upright. This drawing emphasizes the basic mechanical setup used to aid in the display or interaction with a round object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/A73w_~Uof4ARGrtjWx3K1Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Maintenance Thickness - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/A73w_~Uof4ARGrtjWx3K1Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCreateMaintAspect::CreateMaintenanceAspect

Specifies a boolean value for the maintenance aspect of the Shoe.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Insulation Aspect Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/665486?contentId=XpENLcFtE28O4ItaT4TIog)
IJOAhsCreateInsAspect::CreateInsulationAspect

Specifies a boolean value for the inspection aspect of the Shoe.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/326656?contentId=CuGaRYUq2wvHwJB_DL8kWw)
The following properties are used to specify the different port types and their sizes
for the Shoe.

![port_details (Shoe)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ruqoWRk00q83j173ZjJASA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=202e1691895883a6)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ruqoWRk00q83j173ZjJASA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image consists of two main sections labeled "1" and "2," which depict mechanisms involving forces and moments acting upon objects in different orientations. In section "1," there is a visual representation of a circular object with force vectors labeled X, Y, and Z indicating the directions in which these forces act. This arrangement implies a rotational or dynamic scenario, possibly related to torque or angular motion. In section "2," a vertical structure (appears to be a beam or column) is shown, with a horizontal base under it. It also has force vectors labeled X, Y, and Z, which suggests analysis related to static equilibrium or structural mechanics. The bottom part may represent a scenario under load, analyzing how forces interact with the object and its supports. The use of arrows indicates the direction of the forces, and the red squares likely designate points of interest or application of those forces. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LhwR4EMwgkRnDRFcXxoMmQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LhwR4EMwgkRnDRFcXxoMmQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Route

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1016 | Pipe outside diameter | Pipe outside diameter | Pipe outside diameter |

Port 2 - Steel

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 | -1 | -9999 | 9999 |

Port 2 - Weld

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 | -1 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shield - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307753?contentId=vnTMpOwOj7IeMbVIVkwaUg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Shield  
Part Name: Shield  
Part Description: Shield SmartPart

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

To place a sample Shield SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that resembles a plus sign with a stylized square around it, often used to indicate an action for adding or creating something:  and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Saddles and Shields > Insulation Protection Shield folder as shown below.

   
Image:[Image-Analysis: The image presents a hierarchical structure, likely depicting a directory or a catalog of parts within a system called "SmartParts". At the top level, there is the "S3D Standard" folder, which contains various categories of components, such as "Beam Attachments", "Clevises", "Miscellaneous", "Pipe Clamps", "Pipe Straps", "Plates", "Rod Fittings", "Rods", and "Struts", along with "U-Bolts". Each category may contain further subcategories or specific items. For instance, within the "Saddles and Shields" category, there is a specific item labeled "Insulation Protection Shield." This indicates a structured organization of parts possibly used in engineering or construction applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rR3rI8fWX3vgALEMUVI95A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rR3rI8fWX3vgALEMUVI95A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image contains two diagrams depicting routes with different orientations and positions. The upper diagram shows a circular route labeled "Route" with directional arrows indicating the Y and Z axes. The lower diagram presents a rectangular route also labeled "Route," with directional arrows indicating the X and Z axes. The relationships between the routes can be interpreted as different navigation paths in a coordinate system, likely used in the context of routing or navigation systems, where Z represents a common vertical axis, while X, Y represent horizontal orientations. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OsZU2lVvoxpar4sryNZHGw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OsZU2lVvoxpar4sryNZHGw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307780?contentId=6OHuxZA9kZrsXOXqXu78tw)
IJOAhsPipeOD::PipeOD

Provides the following:

* The outside diameter of the pipe.
* The pipe insulation dimension, if needed.
* The inside diameter of the shield.


Image:[Image-Analysis: The image depicts a diagram related to the measurement of pipe outer diameter (PipeOD). It consists of two shapes: a circular shape at the top representing a pipe's cross-section, and a rectangular shape at the bottom which likely represents a different type of pipe or cross-section. The red dots marked at the center of each shape may indicate the internal reference points for measurement. The text "PipeOD" above the circular shape indicates that the focus of this illustration is on measuring the outer diameter of a pipe. The overall purpose of the image is to provide a visual representation of how to identify and note measurements relevant to different pipe shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_DqL4fKsmf4uPpN7EzGm3A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_DqL4fKsmf4uPpN7EzGm3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSize::Size

This value is used for part selection rules to choose a correct shield part. It is
not included in the shield graphics.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Lower Plate Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307859?contentId=35ZWTLewR6Pk6UQzIL_NtA)
IJUAhsThickness1::Thickness1

Specifies thickness of the lower curved plate. This value must be greater than zero.


Image:[Image-Analysis: The image illustrates a concept related to "Thickness1" and depicts two different shapes: a circle and a rectangle. The top part shows a shaded circle with a red point denoting a measurement, indicating possibly a radius or a specific thickness measurement. There are arrows pointing outward, suggesting the concept of measuring thickness around the circle. Below the circle, there is a rectangular shape with rounded edges, also shaded, and another red point indicating a measurement. The overall theme seems to revolve around the comparison or detailing of different thickness measurements related to various geometrical shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/07ykr7MezBQ9T061Hy~TVA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/07ykr7MezBQ9T061Hy~TVA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of the lower plate. This value must be greater than or equal
to zero.


Image:[Image-Analysis: The image depicts two shapes: a circle and a rectangle, both shaded in gray. At the top, there is a circle positioned above a dashed line. Below the dashed line, there is a rectangle. Both shapes have a red dot marked within them, indicating a specific point of interest. The rectangle is labeled "Length1" underneath its width, suggesting this is a measurement related to the rectangle. This image could be illustrating a geometric relationship or providing a visual for a technical or engineering problem where the dimensions of a circle and a rectangle are relevant. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uvybtRw63fwumVcxW4c2IQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uvybtRw63fwumVcxW4c2IQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle1::Angle1

Specifies the angle from vertical center line of the pipe to the left edge of the
plate. Angle1 and Angle2, or Width1 and Width2, can define the sweep of the plate. Angle1 and Angle2 take precedence. If there is no top plate then:

Angle1 <= 360 degrees – Angle2

Else if there is a top plate then

Angle1 <= 180 degrees – Angle3


Image:[Image-Analysis: The image depicts a diagram illustrating the concept of angle measurement. At the top, there is a gray circle representing the vertex of an angle, labeled as "Angle1." A line extends from the vertex, showing the direction of the angle formed. Below the circle is a rectangular shape, which may represent a surface or base where the angle is applied. The drawing suggests a relationship between the angle at the circle and the dimensions at the rectangle, possibly indicating how angles can affect or relate to different geometric shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UcNCoiQdzQC0cr~ovcgjOg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UcNCoiQdzQC0cr~ovcgjOg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle2::Angle2

Specifies the angle from vertical center line of the pipe to the right edge of the
plate. Angle1 and Angle2, or Width1 and Width2, can define the sweep of the lower plate. Angle1 and Angle2 take precedence. If there is no top plate then:

Angle2 <= 360 degrees – Angle1

Else if there is a top plate then

Angle2 <= 180 degrees – Angle4


Image:[Image-Analysis: The image illustrates a geometric concept involving a circle and an angle, labeled as "Angle2". The diagram shows a circle with a shaded area, a radius extending from the center to the circumference, and a point marked in red, which likely indicates the vertex of the angle. The angle is formed between the radius and a horizontal line, which suggests the relationship between the radius and the angle at the circle's center. This is a common representation in geometry to explain angles and their relation to circles, showing how angles can be measured in relation to circular arcs. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IvBmpMwFtywD6RcP3XTyEg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IvBmpMwFtywD6RcP3XTyEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the distance from vertical center line of the pipe to the left inside edge
of the plate. Curved plate only drawn on the lower half of the pipe. Angle1 and Angle2 must be 0 or this will be ignored. Width1 must be less than 0.5 \* PipeOD.


Image:[Image-Analysis: The image depicts a circular shape (likely a circular cylinder) with a line indicating its width labeled as "Width1." The circle is filled with a gray color and has a red point at the top center. The line extending horizontally from one side of the circle to the other signifies the measurement of the width across this circular shape. This image is often used in technical drawings or engineering contexts to specify dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rGbxE1vXGCvWRSMpOhxyYw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rGbxE1vXGCvWRSMpOhxyYw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the distance from vertical center line of the pipe to the right inside edge
of the plate. Curved plate only drawn on the lower half of the pipe. Angle1 and Angle2 must be 0 or this will be ignored. Width2 must be less than 0.5 \* PipeOD.


None: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Upper Plate Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307959?contentId=~6gdVaqNCtotxUE7guoThA)
IJUAhsThickness2::Thickness2 (optional)

Specifies the thickness of the upper curved plate. If Thickness2 is less than or equal to zero, then the upper plate is not drawn.


Image:[Image-Analysis: The image depicts a technical illustration that represents the concept of "Thickness" in a design or engineering context. At the top, there is a circular object, likely a disk or a wheel, indicated by a dashed boundary, which symbolizes its thickness. This circular object has a red dot to indicate a point of reference or center. Below it, the term "Thickness2" is written, suggesting a specific measurement or a variation of thickness. Underneath this label, there is a rectangular shape with another red dot at its center, representing another cross-section or a different solid that emphasizes the concept of thickness in varying geometrical forms. Overall, the relationship indicates comparing two different shapes (circle and rectangle) in terms of their thicknesses, illustrating an abstract concept in a portion of a design or technical drawing. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/csIebJE69Ab82WBNEiVc1Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/csIebJE69Ab82WBNEiVc1Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2 (optional)

Specifies the length of the upper plate. If Thickness2 is greater than zero, then Length2 is greater than or equal to zero.


Image:[Image-Analysis: The image illustrates two geometric shapes: a circle and a rectangle. The circle is represented on the top section of the image, and there is a red dot at its center, indicating a reference point. Below the circle, there is a rectangle with a rounded top. The rectangle has a label at its top that reads "Length2," suggesting that this dimension is important, possibly indicating one of the sides of the rectangle. The red dot is also present at the center of the rectangle, indicating a reference point similar to that of the circle. The connection between the two shapes appears to concern their dimensions or a specific measurement related to both shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6qqUAopL0RuGdisjLV735A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6qqUAopL0RuGdisjLV735A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3 (optional)

Specifies the angle from the vertical center line of the pipe to the left edge of
the top plate. Either Angle3 and Angle4, or Width3 and Width4, can define the sweep of the plate.  Angle3 and Angle4 take precedence. If Thickness2 is greater than zero, then either (Angle3 and Angle4) or (Width3 and Width4) is greater than zero.

Angle3 <= 180 degrees – Angle1


Image:[Image-Analysis: The image depicts a geometric representation involving two shapes: a circle and a rectangle. At the top left, there is a circle shaded in gray with a red point inside, which likely represents a pivot or a center point. An angle is indicated by a line drawn from this center to the outer edge of the circle, labeled "Angle3." This suggests that a specific angle measurement is relevant to this circle. Below the circle, a rectangular shape is shown, also shaded in gray, with another red point marked inside it. The positioning and relationship of these shapes might imply a connection between the angle defined in the circular region and the rectangular area below, possibly indicating a rotational or positional relationship that pertains to geometric or physical principles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JNhmLH9fVwCvdqh~ZiWFaQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JNhmLH9fVwCvdqh~ZiWFaQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle4::Angle4 (optional)

Specifies the angle from the vertical center line of the pipe to the right edge of
the top plate. Either Angle3 and Angle4, or Width3 and Width4, can define the sweep of the plate. Angle3 and Angle4 take precedence.

If Thickness2 is greater than zero, then either (Angle3 and Angle4) or (Width3 and Width4) is greater than zero.

Angle4 <= 180 degrees – Angle2


Image:[Image-Analysis: The image illustrates an angle measurement process involving a circular shape and a rectangle positioned underneath. At the top, there is a circular shape with a radius and an angle labeled "Angle4" indicating a specific measurement between a line extending from the center of the circle to its circumference. Below this, a rectangular figure is shown, likely representing a base or component related to the circular measurement. The red dot at the center serves as a reference point for measurements. Overall, this image appears to visualize an angle measurement in a geometric context, showing the relationship between a circle and a rectangle. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GRCfgiO3tqE9oAjx1_dC5Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GRCfgiO3tqE9oAjx1_dC5Q-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image depicts a circular representation divided into four distinct angles, labeled as Angle 1, Angle 2, Angle 3, and Angle 4. The circle is shaded in a gray color and has a red dot in the center, possibly indicating a reference point or origin. The arrows extending from the center towards the edges of the circle suggest a directional relationship, which is often used in geometry or trigonometry to represent angles in a coordinate system. This visualization allows for the understanding of angular measurements and their orientation in a two-dimensional plane. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ooq~2aAEdQluzu0AIm8y3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ooq~2aAEdQluzu0AIm8y3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the distance from the vertical center line of the pipe to the left inside
edge of the top plate. The curved plate is only drawn on the upper half of the pipe.
Angle3 and Angle4 must be zero or this is ignored. Width3 must be less than 0.5 \* PipeOD.


Image:[Image-Analysis: The image consists of two shapes: a circle and a rectangular shape below it. The circle is labeled with "Width3" and has a red dot in the center. The circle's diameter is indicated by arrows pointing outward, suggesting it measures its width at that point. Below the circle is a rectangular shape which also features a red dot in the middle, indicating a focus point or center. The arrangement suggests a relationship where both shapes share a common measurement (Width3), and the positioning of the red dots signifies a reference point for each geometric figure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NHfhjA2cL7O0jYKki1f0cQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NHfhjA2cL7O0jYKki1f0cQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Specifies the distance from the vertical center line of the pipe to the right inside
edge of the top plate. The curved plate is only drawn on the upper half of the pipe.
Angle3 and Angle4 must be zero or this is ignored. Width4 must be less than 0.5 \* PipeOD.


Image:[Image-Analysis: The image depicts two geometric shapes: a circle on the top and a rectangle on the bottom. The circle is labeled with the word "Width4," indicating a measurement or specification related to the width of this circle. The circle is filled with a gray color and has a red dot at its center that could designate the center point. Below the circle, there is a rectangle that appears to have two cut-outs, and it is also shaded in gray with a similar red dot at the center. The dashed line separating the two shapes may suggest a focus on the relationship between their dimensions or how they are utilized in a certain context, possibly in design, engineering, or architecture. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~jyMH2CbEbi0wtdsNHGGDQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~jyMH2CbEbi0wtdsNHGGDQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Weld Plate/Bolt Blocks Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308029?contentId=YVIx6rxRXVlFx9geQVrQiQ)
IJUAhsThickness3::Thickness3 (optional)

Specifies the thickness of the weld plate\bolting block. All plates\blocks have the
same thickness. If Thickness3 is less than or equal to zero, then the weld plates are not drawn.


Image:[Image-Analysis: The image displays two components related to "Thickness3." The upper section illustrates a circular shape with arrows indicating its diameter, emphasizing its thickness marked by a red dot in the center. The lower section shows a rectangular shape, also marked with a red dot indicating a similar measurement of thickness or depth. The presentation suggests that both shapes are meant to be compared in terms of thickness, possibly within a technical or design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qaBrlJ1qIe2kifbvQ8aSvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qaBrlJ1qIe2kifbvQ8aSvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle5::Angle5

Specifies the total angle of the plate. The plate is always centered on the pipe centerline.
The weld plates on both sides of the pipe will have the same dimensions. Angle5 takes precedence over Height1.

* If Thickness3 is greater than zero, then either Angle5 or Height1 is required.
* Angle5 must be greater than 180 – (Angle1 + Angle3)
* Use Height1 instead of Angle5 for a SQUARE or RECTANGLE plate.
* If Angle5 is used, the plate is drawn as a CURVED PLATE.


Image:[Image-Analysis: The image illustrates an object (possibly a spindle or a rotary component) and its angular position. The top part shows a circular view of the object with a marked angle, labeled "Angle5," which indicates the angle measurement from a reference point. The circular shape represents the aspect of rotation or angular displacement. The bottom part depicts the object from the side, showing a simplified view where the object is divided into sections or layers, with a red dot indicating a specific point of interest or measurement, possibly the center of the object. This dual perspective helps in understanding the object's geometrical properties in both angle (top view) and structure (side view). 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u3_HCihKZ8SRPOJruON4sA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u3_HCihKZ8SRPOJruON4sA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height of the left plate. This value is measured from the inside bottom
corner to the inside top corner. The plate is always centered on the pipe centerline.
The plates on both sides of the pipe have the same dimensions. Angle5 takes precedence over Height1.

* If Thickness3 is greater than zero, then either Angle5 or Height1 is required.
* Height1 must be greater than 180 – (Angle1 + Angle3)
* Use Height1 instead of Angle5 for SQUARE or RECTANGLE plates.
* If Angle5 is used, the plate is drawn as a CURVED PLATE.


Image:[Image-Analysis: The image depicts a schematic representation of dimensions related to two objects. At the top, there is a cylindrical shape (represented by the circle) that has a label of "Height1," indicating a measurement associated with its height. Below the cylindrical shape, there is a rectangular shape, possibly representing a box or a container, which typically experiences a different set of dimensional measurements. The red dots within both shapes likely indicate points of interest or specific measurement references. The arrangement of the two shapes suggests a comparison or relationship between their dimensions, with the top part focusing on the cylindrical height and the bottom part on the rectangular dimension layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vEoWlqoR_LYVp5MvJLjVoA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vEoWlqoR_LYVp5MvJLjVoA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3

Specifies the length of the plate\block. If Length3 equals zero and Thickness3 is greater than zero, use the smaller of Length1 and Length2. If there is more than one plate or block on each side, they have the same length.


Image:[Image-Analysis: The image consists of two diagrams depicting a cylindrical object and a rectangular object. The top section shows a cylinder viewed from above, marked with a red dot that likely indicates a focus or measurement point. The bottom section displays a rectangular shape, also with a red dot, and features arrows pointing toward its width labeled "Length3." The use of these diagrams suggests that they may be related to dimensional specifications or measurements applicable for some technical or engineering context, possibly relating to the design or layout of these objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i8g26hgkShbwnxvphQVzFQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i8g26hgkShbwnxvphQVzFQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty

Specifies the number of plates. This is same on both sides.

IJUAhsMulti1::Multi1LocateBy

Specifies how to locate the plates. This is the same on both sides. The plates are
located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of plates. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the location of plates. This is the same on both sides.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Sleeve Shield Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308058?contentId=ETUjSTDhd0UrsXGPt20T1A)
IJUAhsDiameter1::Diameter1 (optional)

Specifies the inside diameter of the plate. If Diameter1 is greater than zero, then the sleeve is a floor sleeve. This value must be greater
than PipeOD, and Angle1 + Angle2 equals 360 degrees, or Angle1 + Angle2 + Angle3 + Angle4 equals 360-degrees.


Image:[Image-Analysis: The image consists of two illustrations showing the concept of "Diameter1." The top part depicts a circular object with an inner shaded area, indicating the presence of a diameter, which is marked by two horizontal arrows pointing outward. The arrows denote the measurement across the circle at its widest point. The bottom part of the image shows a rectangular shape that aligns with a similar center point marked in red, suggesting another geometric relationship. The term "Diameter1" serves as a label for the entire illustration, indicating that it is likely related to measurements or specifications in geometric contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y7moxBECiEgB0nafRX8E3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y7moxBECiEgB0nafRX8E3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1 (optional)

Specifies the offset of the graphics from the route port. The route port remains at
the origin (0,0,0).


Image:[Image-Analysis: The image displays a technical drawing featuring two views of an object. The top view is a circular shape that highlights a central point marked in red, which indicates the center of the circle. Below it, there is a side view of a rectangular object that seems to be oriented horizontally. The side view shows two overlapping rectangles suggesting a cross-section, with a red dot marking their intersection. Additionally, the term "Offset1" is labeled next to vertical arrows, indicating a measurement or distance related to the offset from the central point to the main rectangular shape. This likely illustrates a specific design or manufacturing detail related to these shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EsGeR_ijcYXjO_of2EU00w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EsGeR_ijcYXjO_of2EU00w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308088?contentId=179iRqgHInubmMW_rYONHQ)
These properties are used to specify the different port types and their sizes for
the shield.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lo6CCAYO8Hno6JdWYyFUzw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b5d1f35d366d912b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lo6CCAYO8Hno6JdWYyFUzw-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image consists of two separate diagrams depicting routes in a 3D space. The top diagram represents a circular route, labeled as "Route," with coordinates indicated as Y and Z, suggesting a vertical axis represented by Y, and a horizontal axis indicated by Z. The bottom diagram illustrates a rectangular route, also labeled "Route," with the axes X and Z showing the horizontal and vertical orientations. Both diagrams highlight the spatial relationships of the routes in terms of their geometric shapes and coordinate systems, suggesting different movement or travel patterns. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uhB88Mf9a4iDWaRfT6Gr2Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uhB88Mf9a4iDWaRfT6Gr2Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 – Route (0, 0, 0)

To connect to a pipe, the X axis of the route port is along the length of the plate.
The Z axis is pointing towards the lower plate.

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1016 | Diameter1 | Diameter1 | Diameter1 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Weld Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308094?contentId=WlUDpNbFrb1Sgd2a_Qg3LA)
To make adding welds to support assemblies easier, weld ports are added at common
weld locations.

Single Plate


Image:[Image-Analysis: The image presents two views of a geometrical shape related to a welding process, specifically denoted as "Shield_Weld1". The top view shows a circular outline with the point labeled "Shield_Weld1" marked in red at the bottom of the arc. This perspective indicates the placement or focal point of the welding operation on the circular part. The second view, depicted below the first, shows a rectangular shape with an inset that also has "Shield_Weld1" marked in red, potentially indicating a different segment of the same welding operation. The coordinate axes are represented in both views: "X" is shown to the right in the bottom view, "Y" extends to the right in the top view, and "Z" is directed downward in both views. This structure suggests that the welding operation is evaluated from different angles, emphasizing its three-dimensional relationship. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H61jfVp5SRcVEAQ4AXW1MA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H61jfVp5SRcVEAQ4AXW1MA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Double Plate


Image:[Image-Analysis: The image consists of two diagrams displaying different views of a welded component, labeled with specific welding identifiers (Shield_Weld1 and Shield_Weld2). The top part represents a circular view of one section, while the bottom part illustrates a rectangular view. The labels indicate the locations of welds on the component, with arrows showing the orientation of the Y, Z, and X axes respectively. The diagrams provide important information regarding the welding positions and structural orientation of the component in a three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LCWJ0GuoDH6nf3FA~ua59w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LCWJ0GuoDH6nf3FA~ua59w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Double Plate with Welded Lap Plate

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dOEa3s1MFtt9FScBL9OlRg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=36130c2c30afff5d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dOEa3s1MFtt9FScBL9OlRg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 2 – Weld1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1012 | Use- 1 | Use- 0 | Use- 1 |

Port 3 – Weld2

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1012 | Use- 1 | Use- 0 | Use- 1 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Slide Plate - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316943?contentId=aLTnmAxlJY2UkcFov3RuBg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.SlidePlate  
Part Name: Slide Plate  
Part Description: Slide Plate SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nhQj3zthHJx5QYR9vblUwQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d824a36034c54a25)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nhQj3zthHJx5QYR9vblUwQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

o place a sample Slide Plate SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Slide Plate > Slide Plate as shown in the following example:

   
Image:[Image-Analysis: The image is a hierarchical tree structure that represents the organization of various components under the category "SmartParts" and "S3D Standard." At the top level, we have "SmartParts," which is the main category. Under this category, there is a sub-category called "S3D Standard." Below "S3D Standard," there are various folders representing different types of parts, such as "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Saddles and Shields," and "Slide Plate." The "Slide Plate" folder is highlighted, indicating it may be of particular interest or selection among the various parts listed. Additionally, at the same level, we have two other folders: "Struts" and "U-Bolts," signifying they are also part of the components in this category but are not under "S3D Standard." This structure helps users navigate through the parts and understand their relationships and categories. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u7CwS8tDFBLiJsN_KUx_Og-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u7CwS8tDFBLiJsN_KUx_Og-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts two distinct components, one above the other, representing a system with a focus on coordinates and positions. The upper section shows a red circle that seems to be positioned above a rectangular box, suggesting it may represent a movable point or object. The lower section includes a rectangular box labeled with the coordinates (0,0,0), indicating a fixed point in a three-dimensional space. This suggests a relationship where the red circle could be a reference point or object that is related to the axis labeled by these coordinates, indicating its position in a 3D coordinate system. The overall design seems to illustrate concepts of spatial relationships or positioning in three-dimensional geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vdxAf1UIrQYJjjMb3UUpGw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vdxAf1UIrQYJjjMb3UUpGw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316945?contentId=tvXQ8XWAvEwj29UbZMaHrw)
These properties are used to create the graphical representation of the plates. Each
of the six plates—Plate1, Plate2, Plate3, Plate4, Plate5, and Plate6—possesses the
same properties, as shown in the following illustration:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZmMsrOTKLdkwZFLswDSSqw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=07b8fe121e76e24a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZmMsrOTKLdkwZFLswDSSqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Defines the width of Plate1.


None: 

IJUAhsHeight1::Height1

Defines the depth of Plate1.

IJUAhsThickness1::Thickness1

Defines the thickness of Plate1.


Image:[Image-Analysis: The image depicts a simple graphical representation of two different boxes or elements, typically used in designs or applications. The top box is empty and has no fill or label, while the bottom box has a label that reads "Thickness1". This suggests that the bottom box may represent a specific state or measurement related to thickness, indicating a measurement tool or setting. The empty box could potentially represent a placeholder or a different parameter yet to be defined. The visual relationship indicates that the thickness is categorized or defined separately from the upper element, suggesting they are part of a series of options or attributes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZMjH~_Zy~wjz5z6qf4CCxA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZMjH~_Zy~wjz5z6qf4CCxA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsXPl1::XPl1

Specifies the distance in X direction between slide plate part local (0,0,0) and Plate1
(0,0,0).

IJUAhsYPl1::YPl1

Specifies the distance in Y direction between slide plate part local (0,0,0) and Plate1
(0,0,0).

IJUAhsZPl1::ZPl1

Specifies the distance in Z direction between slide plate part local (0,0,0) and Plate1
(0,0,0).

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MEjHDxfZtoOUx_JYnbugxg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9e2ab482d1632fd7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MEjHDxfZtoOUx_JYnbugxg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The attribute definitions for Plate2, Plate3, Plate4, Plate5, and Plate6 are the
same as those defined for Plate1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Guide Property - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316946?contentId=GGs6wS8oULqAsaiyupA~Zw)
You can use this property to include a guide.

IJUAhsGuideShape::GuideShape

Specifies the name of the guide. If GuideShape is set to zero or left blank, then no guide is drawn in the graphics.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pipe Diameter Property - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316947?contentId=BtxvXYNTAxR_oB~i7zp0Dg)
IJUAhsDiameter1::Diameter1

Specifies the diameter of the pipe.


Image:[Image-Analysis: The image depicts a geometric figure, specifically a circular shape, which is labeled as "Diameter1" next to it. The circle is connected by dashed lines to a rectangular base, suggesting a relation where the diameter measurement originates from the circular shape and possibly extends down to the rectangular base. The dashed lines may indicate measurement references or denote the continuation of linear dimensions. The overall illustration seems to be related to geometry or engineering, possibly indicating the relationship between a circular object and a foundation underneath it. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/78~~y9gUTlMMtBNjucqljQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/78~~y9gUTlMMtBNjucqljQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shoe Height Property - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316948?contentId=ETz27FLlXqmwgcXAMkFzvw)
IJUAhsShoeHeight::ShoeHeight

Specifies the distance between the bottom of the pipe and the top of the slide plate.


Image:[Image-Analysis: The image illustrates a simple diagram depicting a shoe with a circular object on top, possibly representing a figure or component. There are dashed red lines surrounding the circular object, connecting it to a base that represents the shoe. The measurement "Shoe Height" is indicated on the right side of the image, suggesting that the height from the base of the shoe to the top of the circular component is being measured. This may relate to design considerations in footwear, such as the height of heels or other features regarding the shoe's construction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l32aHK3Lh2zECJD760wnsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l32aHK3Lh2zECJD760wnsg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/316949?contentId=Lbp0kZirni1z2NhO3aTEHw)
These properties are used to specify the different Slide Plate port types and their
sizes.


Image:[Image-Analysis: The image displays a structured comparison between two ports labeled "Port 1: Route" and "Port 2: Structure." Each port has a list of attributes organized in a vertical format. For Port 1, the attributes include "Name," "PortType," "Size," "MinSize," "MaxSize," and "UnitType," with each corresponding to "HgrSymbolPort(1)." Similarly, for Port 2, the same attributes are listed correspondingly for "HgrSymbolPort(2)." The distinction between the two sections is highlighted with a color coding; Port 1 is in pink and Port 2 is in green, signifying different categorizations or functionalities for each port within a potential system or framework. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5RTTlGjT9EwFPZcSCEcXZg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5RTTlGjT9EwFPZcSCEcXZg-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9zEjjYRDG1CrL87jRo1D7A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e583e9f94c11d0fd)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9zEjjYRDG1CrL87jRo1D7A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 2 - Route | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Structure

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 3 - Structure | 0 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Spreader Beam - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574506?contentId=8X8ATq0otYjGXlwg4RFASw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.SpreaderBeam  
Part Name: Spreader Beam  
Part Description: Spreader Beam SmartPart

![SpreaderBeam](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LpgzPY8bveesVu~vM1boDw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=112d95421b26b412)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LpgzPY8bveesVu~vM1boDw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Ensure that these workbooks are available in the following location before you place
the parts:

[Product Folder]\CatalogData\BulkLoad\DataFiles\

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

The HS\_S3DParts.xls file provides sample SmartPart data and is available from the following location:

[Product Folder]\CatalogData\BulkLoad\DataFiles

Part Placement

To place a sample Spreader Beam SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a price tag, indicating an addition or increase in price or value: , and then select the design support.
4. In the Select Part dialog box select a part from Parts > SmartParts > S3D Standard > Spreader Beam > Spreader Beam as shown below.

   ![SmartPart_SpreaderBeam-UI](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8_7lOC4IQFPlgIGJuV7dCg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9486edbe3cbf28bb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8_7lOC4IQFPlgIGJuV7dCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as red highlighted
points.

Local Coordinate System

![SmartPart_SpreaderBeam_LocalCoordinateSystem](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cMv_BBYuHry8O2Iqoyfj_g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=76fb2100416ced4b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cMv_BBYuHry8O2Iqoyfj_g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Spreader Beam Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574519?contentId=fK41nhslpkUR1gihTxdC_A)
Specifies the shape and structure of the Spreader Beam. The following properties are
categorized under basic Spreader Beam attributes.

IJUAhsDiameter1::Diameter1

Specifies the pipe diameter.

IJUAhsShoeHeight::ShoeHeight

Specifies the shoe height. This property is used to offset the Spreader Beam down
from the bottom of the pipe.

IJUAhsSBeamTopType::TopPlacementType

Specifies the position where the top attachment is placed and cannot be null. This
property uses the following hsSBeamAttachmentType codelist values:

1 - Center  
2 - Edge  
3 - Both Center and Edge

IJUAhsSBeamBotType::BotPlacementType

Specifies the position where the top attachment is placed and cannot be null. This
property uses the following hsSBeamAttachmentType codelist values:

1 - Center  
2 - Edge  
3 - Both Center and Edge# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Attachment - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574520?contentId=1M~GqMhfX6GSq54y5koXXA)
IJUAhsSBeamTopAtt::TopAtt

Specifies the part that needs to be selected as top attachment. The part is attached
directly to the top of the beam and is considered only when the Top Placement codelist
value is 2 (Edge) or 3 (Center and Edge). This property uses the following hsSBeamAttachment codelist values:

1 = Lug


look for icon that looks like a target or crosshair: 

2 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment 
Image-Analysis: The image depicts a simple geometric diagram resembling three stacked rectangular blocks. There are two vertical rectangles on the left and right, which might represent large container-like structures, outlined in black. At the center, there is a horizontal rectangle representing a bridge or connection, likely indicating a space to transfer or connect between these two larger structures. There are also two small red rectangles positioned: one towards the middle of the vertical bars and another below, which could indicate points of interest or focus areas in the structure. The overall arrangement suggests a connection between the entities represented by the rectangles, possibly illustrating some functional relationship between them. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = U Bolt


icon-description is an arch with two red squares inside it, resembling a simplified structure or gate: 

4 = Plate


Image:[Alt-Text: SmartPart_SpreaderBeam_Plate 
Image-Analysis: The image depicts two rectangular shapes, one being larger and positioned to the left, and the other smaller and positioned to the right. The larger rectangle can represent a document, book, or similar item, while the smaller rectangle could signify a notepad or a related accessory. The arrangement suggests a relationship where the larger item may contain or encompass the smaller item, indicating a potential organizational or hierarchical connection between the two. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_SpreaderBeam_Plate](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBeamTopShape::TopShape

Specifies the shape to use for the top attachment. Top shapes can be Lug, WBA, U-Bolt,
or Plate. If the property value is blank, the shape is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Middle Attachment - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574731?contentId=SUpSMXvC2EkaBB1QUwpepQ)
IJUAhsSBeamMiddleAtt::MiddleAtt

Specifies the part that needs to be selected as the top-middle attachment. The part
is attached directly to the top-middle of the beam and is considered only when the
Top Placement codelist value is 1 (Center) or 3 (Center and Edge). This property uses
the following hsSBeamAttachment codelist values:

1 = Lug


look for icon that looks like a target or crosshair: 

2 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_SpreaderBeam_Welded Beam Attachment 
Image-Analysis: The image depicts a simple schematic or diagram, likely representing a top view of a rectangular structure or object with a central area. The central rectangle is enclosed by two other rectangles on either side, which may suggest a design involving separation or organization of space. The red rectangles inside the central area may indicate specific features, points of interest, or functional components within the overall structure. The presence of an outer square suggests a boundary or limit to the area being focused on, while the side rectangles could represent sections or adjoining parts. This layout suggests functionality or a system that may involve movement or flow from one part to another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/960SP1Nbs8ZRBmY51LYwrg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_SpreaderBeam_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/960SP1Nbs8ZRBmY51LYwrg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = U Bolt


icon-description is an arch with two red squares inside it, resembling a simplified structure or gate: 

4 = Plate


Image:[Alt-Text: SmartPart_SpreaderBeam_Plate 
Image-Analysis: The image displays two rectangular shapes. On the left, there is a larger rectangle that is wider and taller than the one on the right, which is a narrower and shorter rectangle. The two rectangles are separated by a vertical dashed line, suggesting a distinction or difference between them. There is no text present, indicating that the shapes may represent different categories or items, possibly in a visual comparison or selection process. The context may imply they could relate to a choice between two options or types of objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_SpreaderBeam_Plate](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBeamMiddleShape::MiddleShape

Specifies the shape to use for the middle attachment. Middle shapes can be Lug, WBA,
U-Bolt, or Plate. If the property value is blank, the shape is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Attachment - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574732?contentId=3O6QQMPQKDOm4G3L_eplog)
IJUAhsSBeamBottomAtt::BottomAtt

Specifies the part that needs to be selected as the bottom attachment. The part is
attached directly to the bottom of the beam. This property uses the following hsSBeamAttachment codelist values:

1 = Lug


look for icon that looks like a target or crosshair: 

2 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_SpreaderBeam_Welded Beam Attachment 
Image-Analysis: The image depicts a floor plan of a rectangular area with a set of walls. There are two entrances or openings on the left and on the right side, indicated by the wider spaces among the walls. The central part of the diagram shows a rectangular space enclosed by walls, with two horizontal lines suggesting potential divisions for different sections within this space. The red boxes in the center and bottom may represent specific features or areas of interest, such as furniture, appliances, or other elements important to the design. Overall, the layout seems to be organized and indicative of a structured environment, possibly a room or portion of a building. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/960SP1Nbs8ZRBmY51LYwrg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_SpreaderBeam_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/960SP1Nbs8ZRBmY51LYwrg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = U Bolt


icon-description is an arch with two red squares inside it, resembling a simplified structure or gate: 

4 = Plate


Image:[Alt-Text: SmartPart_SpreaderBeam_Plate 
Image-Analysis: The image consists of two rectangular shapes of different sizes aligned vertically. The left shape is a larger rectangle, while the right shape is a smaller, narrower rectangle. This arrangement may represent a comparison between two items, a book or a document being the larger shape and perhaps a smartphone or a notepad being the smaller shape. The visual contrast could imply a discussion about different formats of media or devices used for reading or viewing content. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_SpreaderBeam_Plate](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0lnzyT4P_eNh~gUEElWEeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBeamBotShape::BottomShape

Specifies the shape to use for the bottom attachment. Bottom shapes can be Lug, WBA,
U-Bolt, or Plate. If the property value is blank, the shape is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Connection - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574884?contentId=LdSE6RK0XlUO5Rpn49xuSA)
IJOAhsSBeamTopCon::TopCon

Specifies the part that needs to be connected to the top attachment. This property
uses the following hsSBeamConnection codelist values:

1 = Clevis


Image:[Alt-Text: Clevis 
Image-Analysis: The image depicts a simplified diagram of scissors. The upper part, represented by the rectangle, indicates the handle of the scissors, while the lower parts are the blades, which are slightly separated at the tips but connected at the base. The red dots may indicate points of interest or pivot points where the blades operate. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Clevis](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 = Eye Nut

![SmartPart_3DSymbols_SpreaderBeams_Eye Nut](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=63bbd7b2bbee0de7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = Swivel Hanger

![SmartPart_3DSymbols_SpreaderBeams_Swivel Hanger](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c087fb70d9da63f1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment 
Image-Analysis: The image depicts a simple schematic diagram of a box-like structure. It consists of a rectangular outline divided into three main sections: two vertical sections on the sides and one horizontal section in the middle. Each section appears to represent different components or spaces. In the center of the middle section, there is a small red rectangle, which may indicate a specific focus point or feature of importance within the structure. The design suggests a potential use for organization or storage, possibly for items to be placed within the outlined areas. The overall layout conveys a sense of symmetry and modularity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsSBeamTopConShape::TopConShape

Specifies the shape to use for the top connection. Top connection shapes can be Clevis,
Eye Nut, Swivel Hanger, or WBA. If the property value is blank, the shape is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Middle Connection - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574891?contentId=kTDanfSY6hOm1_VEOFJ3TQ)
IJOAhsSBeamMiddleCon::MiddleCon

Specifies the part that needs to be connected to the middle attachment. This property
uses the following hsSBeamConnection codelist values:

1 = Clevis


Image:[Alt-Text: Clevis 
Image-Analysis: The image depicts a mechanical structure that appears to be a representation of a lifting device, likely a jack or a hydraulic lift. At the top, there is a rectangular block, possibly indicating the lifting platform. Below it, two vertical supports or arms extend downward, indicating the structural components that maintain stability. The connection at the bottom shows a horizontal beam between the two arms, which may serve as the base. The red squares indicate specific points of interest, potentially signifying where controls or important connection points are located. The overall design hints at a relationship between different elements, suggesting how lifting actions can be facilitated through this assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Clevis](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 = Eye Nut

![SmartPart_3DSymbols_SpreaderBeams_Eye Nut](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=63bbd7b2bbee0de7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = Swivel Hanger

![SmartPart_3DSymbols_SpreaderBeams_Swivel Hanger](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c087fb70d9da63f1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment 
Image-Analysis: The image depicts a simple structure that resembles a bag or a box with flaps. It has two vertical sides and a base, with a red section possibly indicating an opening or a fold. The top part appears to have two flaps that could be folded down. The design suggests a packaging or container concept, where the red placements highlight specific features or actions, possibly a user interface component, such as a drag-and-drop feature or a foldable design instruction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsSBeamMidConShape::MidConShape

Specifies the shape to use for the middle connection. Middle connection shapes can
be Clevis, Eye Nut, Swivel Hanger, or WBA. If the property value is blank, the shape
is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Connection - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/574893?contentId=Iuktq_f6yjU6G7dxCGQ3Cg)
IJOAhsSBeamBottomCon::BottomCon

Specifies the part that needs to be connected to the bottom attachment. This property
uses the following hsSBeamConnection codelist values:

1 = Clevis


Image:[Alt-Text: Clevis 
Image-Analysis: The image depicts a mechanical device that resembles a scissor lift or hydraulic lift system. It consists of two vertical columns on either side that support a platform, which is represented at the top. The platform appears to be adjustable, likely moving up and down using the hydraulic mechanism or a scissor mechanism indicated by the connections below. The small red squares may represent control points or key positions of the lift. This type of design is typically used in construction or manufacturing for elevating heavy materials or equipment safely. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Clevis](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wmSA6Yiy_7skGWj2JABUCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 = Eye Nut

![SmartPart_3DSymbols_SpreaderBeams_Eye Nut](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=63bbd7b2bbee0de7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SWuQ9pHdibEk5XDxTQ6~kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 = Swivel Hanger

![SmartPart_3DSymbols_SpreaderBeams_Swivel Hanger](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c087fb70d9da63f1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vT9Y1knYERr~viY9rD_Xww-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 = Welded Beam Attachment


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment 
Image-Analysis: The image depicts a simple diagram of a container with dimensions. It shows a rectangular solid or box-like structure. The red lines indicate specific dimensions or highlighted areas, likely marking the centers of the top and base of the container. The outer rectangles represent the sides of the container, while the inner divisions suggest an internal section or perhaps different compartments within the container. This layout can be commonly used in design, engineering, or packaging to visualize the shape and dimensions of a container, noting the importance of the highlighted areas for focus or measurement purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_Welded Beam Attachment](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kuirLkhOMQpDHr3fbHGtfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsSBeamBotConShape::BotConShape

Specifies the shape to use for the bottom connection. Bottom connection shapes can
be Clevis, Eye Nut, Swivel Hanger, or WBA. If the property value is blank, the shape
is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Offset Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575401?contentId=hXet~K9TCnEBDWIk5_LKnw)
IJUAhsSBTopOffsetDef::TopOffsetDef

Specifies the offset for the top attachment. The default codelist value is set to
1. This property uses the following hsSBeamOffsetDefinition codelist values:

1 = From Center  
2 = From Edge

IJUAhsSBeamTopOff1::TopOff1

Specifies the distance from the center or edge of the beam to the center of the top1
attachment. The codelist value cannot be negative.

![SmartPart_3DSymbols_SpreaderBeams_Top Offset1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PylS5RsdFsZvMtsU5UPi0g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e88636c6885a2a4f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PylS5RsdFsZvMtsU5UPi0g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBeamTopOff2::TopOff2

Specifies the distance from the center or edge of the beam to the center of the top2
attachment. The codelist value cannot be negative.

![SmartPart_3DSymbols_SpreaderBeams_Top Offset2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lAEEIKPuoZbk8RY9fYekNA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2621e6054c856f4c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lAEEIKPuoZbk8RY9fYekNA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBBotOffsetDef::BotOffsetDef

Specifies the offset for the bottom attachment. The default codelist value is set
to 1. This property uses the following hsSBeamOffsetDefinition codelist values:

1 = From Center  
2 = From Edge

IJUAhsSBeamBottomOff1::BottomOff1

Specifies the distance from the center or the edge of the beam to the center of the
bottom1 attachment. The default value for BotOffsetDef is 1.

![SmartPart_3DSymbols_SpreaderBeams_Bottom Offset1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xMuX2siqnzDDWJKWUuU~LA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9d7f85567e8ebb81)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xMuX2siqnzDDWJKWUuU~LA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBeamBottomOff2::BottomOff2

Specifies the distance from the center or the edge of the beam to the center of the
bottom2 attachment. The default value for BotOffsetDef is 1.

![SmartPart_3DSymbols_SpreaderBeams_Bottom Offset2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MdI4PGq7dy84ANmVgg8Rbw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1b22f3ba8afe1584)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MdI4PGq7dy84ANmVgg8Rbw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSBMiddleOffsetDef::MiddleOffsetDef

Specifies the offset for the middle attachment. The default codelist value is set
to 1. This property uses the following hsSBeamOffsetDefinition codelist values:

1 = From Center  
2 = From Edge

IJUAhsSBeamMiddleOff::MiddleOff

Specifies the distance from the top middle attachment to the center or edge of the
beam.

![SmartPart_3DSymbols_SpreaderBeams_Middle Offset](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GMy9oZFPDWVqTieumTt_5A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e921b7200c62c027)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GMy9oZFPDWVqTieumTt_5A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Attachment Orientation Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575407?contentId=i5KNYKahDG34PB8UQaT7Og)
IJUAhsBeamTopAtt1Orient::TopAtt1Orient

Specifies the orientation of the top attachment1 with respect to the beam. The default
codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned

IJUAhsBeamMidAtt1Orient::MidAtt1Orient

Specifies the orientation of the top attachment2 with respect to the beam. The default
codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned

IJUAhsBeamBotAtt1Orient::BotAtt1Orient

Specifies the orientation of the bottom attachment1 with respect to the beam. The
default codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned

IJUAhsBeamTopAtt2Orient::TopAtt2Orient

Specifies the orientation of the bottom attachment2 with respect to the beam. The
default codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned

IJUAhsBeamMidAtt2Orient::MidAtt2Orient

Specifies the orientation of the middle attachment1 with respect to the beam. The
default codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned

IJUAhsBeamBotAtt2Orient::BotAtt2Orient

Specifies the orientation of the middle attachment2 with respect to the beam. The
default codelist value is Aligned. This property uses the following hsOrientation codelist values:

1 = Perpendicular  
2 = Aligned# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Connection Rotation Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575408?contentId=i_8_KvdidmsR2Cnmsp1HCA)
IJUAhsSBeamTopCon1Rot::TopCon1Rot

Specifies the rotation of the top attachment1. The default codelist value is set to
zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This property
uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree

IJUAhsSBeamTopCon2Rot::TopCon2Rot

Specifies the rotation of the top attachment2. The default codelist value is set to
zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This property
uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree

IJUAhsSBeamMidCon1Rot::MidCon1Rot

Specifies the rotation of the middle attachment1. The default codelist value is set
to zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This
property uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree

IJUAhsSBeamMidCon2Rot::MidCon2Rot

Specifies the rotation of the middle attachment2. The default codelist value is set
to zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This
property uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree

IJUAhsSBeamBotCon1Rot::BotCon1Rot

Specifies the rotation of the bottom attachment1. The default codelist value is set
to zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This
property uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree

IJUAhsSBeamBotCon2Rot::BotCon2Rot

Specifies the rotation of the bottom attachment2. The default codelist value is set
to zero degrees and is applicable if the connection type is 3 (Swivel Hanger). This
property uses the following hsRotation codelist values:

1 = 0 degree  
2 = 90 degree  
3 = 180 degree  
4 = 270 degree# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Steel Section Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575416?contentId=VXlo7wpxJ_WYnd1JM401og)
IJUAhsLength::Length

Specifies the length of the beam.

![SmartPart_3DSymbols_SpreaderBeams_SteelSection_Length](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qz2XIGNHovSOX3ypq4SwTg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=075298124f373e29)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qz2XIGNHovSOX3ypq4SwTg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsBBGap::BBGap

Specifies the gap for a back to back channel. The software draws the section only
if the gap is zero. If the gap is more than the zero then, the software draws more
than two sections in a back to back configuration with spacing that is equal to BBGap.

IJUAhsSteelSection::SteelName

Specifies the name of the steel section.

IJUAhsSteelSection::SteelType

Specifies the type of the steel section.

IJUAhsSteelSection::SteelStandard

Specifies the standard of the steel section.

IJUAhssteelAngle::SteelAngle

Specifies the angle of rotation along the x-axis for the steel section.

IJUAhsSteelCPoint::SteelCpoint

Specifies the cardinal point of the steel section.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Stiffener Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575418?contentId=jOO~EMv_G~Xgsv23Bcog~w)
IJUAhsSBStiffenerShape::Stiffener

Specifies the stiffener shape to use. If the property value is blank, the stiffener
shape is not drawn. If the BacktoBack property value is Yes, then the stiffeners are drawn on both sides. Otherwise they are drawn on one side.

![SmartPart_3DSymbols_SpreaderBeams_Stiffener Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/srJJLPJHBL7PgJWyGSJGzw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=eee948d5a1c80c7a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/srJJLPJHBL7PgJWyGSJGzw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty, IJUAhsMulti1::Multi1Location

Specifies the number of stiffeners. If zero, no stiffeners are drawn.

IJUAhsMulti1::Multi1LocateBy

Specifies how to locate the stiffener that is by center or by edge. If zero, no stiffeners
are drawn.

IJUAhsMulti1::Multi1Location

Specifies the location value that determines the spacing. If zero, no stiffeners are
drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [EndPlate Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/672341?contentId=UD51KmEI7cau2MSZqsDClg)
IJUAhsSBEndPlate::EndPlateShape

Specifies the shape to use for the EndPlate attachment.

IJUAhsSBEPVOffset::EndPlateVerticalOffset

Specifies the vertical offset between the bottom of the EndPlate and bottom of the
Spreader Beam.


Image:[Alt-Text: Illustration of Spreader Beam - EndPlate Shape 
Image-Analysis: The image depicts a horizontal rectangular shape shaded in green, resting on a gray background. There are two vertical lines at each end of the rectangle, possibly indicating support or boundaries. Above the rectangle, there is a small L-shaped icon, which may represent a coordinate system or the orientation of the shape. The term "Vertical Offset" is labeled to the right of the rectangle, suggesting that the image is likely discussing adjustments in positioning the rectangle vertically. This could be relevant in contexts like engineering, design, or CAD (Computer-Aided Design), where precise measurements and placements are important. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Puk70EXkQr8M49b4nMsnXg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Spreader Beam - EndPlate Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Puk70EXkQr8M49b4nMsnXg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/575566?contentId=J77QQX8gqNXlU~gCT2F4Jg)
These properties are used to specify the different port types and their sizes for
the spreader beam. A spreader beam can have the following six ports:

* Route - origin of the spreader beam
* Topport1 - top port1
* Topport2 - top port2; if two top attachments are present
* Botport1 - bottom port1
* Botport2 - bottom port2; if two bottom attachments are present
* BotMiddleport - bottom middle port; if the bottom middle attachment is present

![SmartPart_3DSymbols_SpreaderBeams_Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QEqa8FqnQRBE9v1anuN~8w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=098a264fb573295d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QEqa8FqnQRBE9v1anuN~8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the spreader beam has one middle attachment and two bottom attachments then the
spreader beam would have three ports as shown in the following illustration.


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_3-Ports 
Image-Analysis: The image shows a simplified technical drawing of a horizontal lifting beam or spreader beam used in lifting applications. It consists of a horizontal beam supported at both ends by two lifting devices, likely hooks or similar attachments. The red squares near the ends indicate points for connecting slings or lifting devices. The centralized lifting point at the top is meant for attaching a crane or hoisting equipment. The design is intended to distribute weight evenly across the beam during lifting, ensuring safety and stability. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/n4~FiNME381cldqRiOkDpw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_3-Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/n4~FiNME381cldqRiOkDpw-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the spreader beam has two top attachments without any middle attachment and two
bottom attachments then it will have five ports as shown in the following illustration.


Image:[Alt-Text: SmartPart_3DSymbols_SpreaderBeams_5-Ports 
Image-Analysis: The image depicts a schematic representation of a lifting beam or spreader beam used in construction or industrial applications. The beam is illustrated horizontally with attachment points on either end for hooks. There are two lifting points, which are denoted by red squares, where the hooks can be attached to lift heavy objects. The design allows for the weight to be evenly distributed, optimizing the lifting of loads by using multiple points of attachment, which reduces stress on both the lifting equipment and the load. The overall structure represents a crucial tool for safely handling and transporting heavy materials. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GzQMsR4InhNV~zFJY4tpxw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![SmartPart_3DSymbols_SpreaderBeams_5-Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GzQMsR4InhNV~zFJY4tpxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the spreader beam has two top attachment with no middle attachments and no bottom
attachments then the spreader beam would have three ports as shown in the following
illustration.

![SmartPart_3DSymbols_SpreaderBeams_3-Ports-top](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BinnJMNuy3oDuAdtsgVn0w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=96f52ffe90e7227d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BinnJMNuy3oDuAdtsgVn0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port details and orientation

* Route

  ![SmartPart_3DSymbols_SpreaderBeams_Route](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Iz4lN7XGpFylmAa0I3j2gg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c89a15660a63c02e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Iz4lN7XGpFylmAa0I3j2gg-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port1:Route

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |

* Top port1

  ![SmartPart_3DSymbols_SpreaderBeams_Top port1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZNDGfuAMoI~vQQLqZtLNIg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=524b00c595213702)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZNDGfuAMoI~vQQLqZtLNIg-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port2:Topport1

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |

* Top port2

  ![SmartPart_3DSymbols_SpreaderBeams_Top port2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9ZeGCyvXlimKV7xelocavA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b2bd6d9d96337a8b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9ZeGCyvXlimKV7xelocavA-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port3:Topport2

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |

* Bot port1

  ![SmartPart_3DSymbols_SpreaderBeams_Bottom port1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LwUGS9As4mGG2Bb_xyy9wg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3d6ac30f0b32e7a3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LwUGS9As4mGG2Bb_xyy9wg-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port4:Botport1

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |

* Bot port2

  ![SmartPart_3DSymbols_SpreaderBeams_Bottom port2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mamZl6BmMWS55jqias_aSA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1c3cf55bd272a8b0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mamZl6BmMWS55jqias_aSA-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port5:Botport2

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |

* BotMiddleport

  ![SmartPart_3DSymbols_SpreaderBeams_Bottom Middle port](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_OSOhM4P2G9mXj2D_Pq9bg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b3c6c0eaaf99a051)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_OSOhM4P2G9mXj2D_Pq9bg-_PVFQNoCl4XmjAxWO0f7XQ/content)

  Port6:BotMiddleport

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - other | 0 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Straight Pipe Lug - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775921?contentId=q_Jp9l5icglC8ps6JsrSow)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PipeLug  
Part Name: Straight Pipe Welding Lug  
Part Description: Single/Double Lug With Curved top/Square top, Parallel  
 Single/Double Lug With Curved top/Square top, Perpendicular  
 Double Lug With Stiffener/Rounded top/Chamfered top

![Straight Pipe Lug SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rKg8AmAQBe3T__knQb4bLw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ce88e234009a7e10)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rKg8AmAQBe3T__knQb4bLw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Straight Pipe Welding Lug SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Straight Pipe Lug > Straight Pipe Welding Lug as shown below.

   ![S3D Pipe Saddle SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VTasSEvPjJoWzYXHi_baKw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=265578eeade6cd0d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VTasSEvPjJoWzYXHi_baKw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System

![Straight Pipe Lug SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HutBsdriZU8nKYywn4Rh8Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4d91c95f56c5c8c2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HutBsdriZU8nKYywn4Rh8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Straight Pipe Lug Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775965?contentId=d~Og1N83E6C_SlJ86W9MJQ)
IJUAhsRodDiameter::RodDiameter

Specifies the rod diameter that is used by the PipeLug and the part selection rule.

IJOAhsPipeOD::PipeOD

Specifies the outer diameter of the pipe that is used with the PipeLug.


Image:[Alt-Text: Straight Pipe Lug - Pipe OD 
Image-Analysis: The image depicts a technical diagram of a circular object, possibly a ring or a loop, with a vertical feature extending from the top. The large circle at the bottom represents the main body, while the narrower vertical segment at the top likely indicates a mounting or connection point. The dashed lines may suggest measurements or outlines for further details, indicating dimensions for the diameter of the circle and the length of the vertical feature. The arrows at the bottom imply that the structure has a defined width, emphasizing its geometric properties. This type of diagram is commonly used in engineering or technical fields to represent components in assemblies or mechanisms. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GTmKLxh4VAgDNVcWczSHGg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Pipe OD](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GTmKLxh4VAgDNVcWczSHGg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance between the horizontal pipe center line and the top lug port.


Image:[Alt-Text: Straight Pipe Lug - Strap Att - Strap Thickness 
Image-Analysis: The image depicts a technical drawing of a circular component, likely a mechanical part or a fitting. The main body is represented as a large circle, with a smaller square marked in red at its center, indicating a point of interest or a reference point. The drawing includes vertical and horizontal measurements, shown by the arrows on the right side and the top, suggesting dimensions that are crucial for manufacturing or assembly. The straight line extending from the top of the circle indicates a shaft or stem that could be used for connection purposes. This drawing suggests an engineering or design context where precise dimensions and positions are important for proper functionality of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7hsB3udgOTYV6RgubXE9gg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Strap Att - Strap Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7hsB3udgOTYV6RgubXE9gg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsIsPerpendicular::IsPerpendicular

Specifies whether the lugs are parallel or perpendicular to the pipe axis. This attribute
accepts a boolean value.

IsPerpendicular - 0 (False)


Image:[Alt-Text: Straight Pipe Lug - IsPerpendicular - 0 False 
Image-Analysis: The image depicts a technical drawing of a padlock from two perspectives: the front view on the left and the side view on the right. The front view shows the circular body of the padlock with a shackle (the U-shaped part) at the top, which is designed to be lifted open. It includes a small horizontal line indicating a cut or a notch on the shackle. The side view on the right reveals the rectangular shape of the padlock's body where it connects to the shackle. This type of drawing is typically used in engineering or design contexts to illustrate the mechanism and form of the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m9kLYVdAb6QXJOR8hzl30Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - IsPerpendicular - 0 False](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m9kLYVdAb6QXJOR8hzl30Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IsParallel - 1 (True)


Image:[Alt-Text: Straight Pipe Lug - IsPerpendicular - 1 True 
Image-Analysis: The image depicts a simple geometric design, showing two shapes: a circular disc on the left and a rectangular block on the right. The circular shape, which has a hole at the top, represents a top view of a disc or ring, possibly indicating a connector or a fitting component. The rectangular shape on the right is a side view of a block, with an indentation at the top suggesting it may have a cylindrical or circular opening from the top view, possibly hinting at a fitting or attachment that aligns with the circular shape on the left. The dashed line in the rectangular shape indicates dimensions or represents a guide for height or depth. This arrangement could imply that the circular component is meant to connect or fit into the rectangular block, suggesting a mechanical or structural application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aoQ7TI8XOO1H3FGZzrlgGg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - IsPerpendicular - 1 True](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aoQ7TI8XOO1H3FGZzrlgGg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775978?contentId=tv4GeG0moP2v~rIndUoaOQ)
IJUAhsLug::TopShape

Specifies the shape that is used for the top of the lug.

1 - Curved 2 - Squared


Image:[Alt-Text: Straight Pipe Lug - TopShape - 1 Curved 
Image-Analysis: The image depicts a simple geometric shape resembling a bell or a dome. It has a rounded top and a wider base, which is typical of a bell shape. At the midpoint of the shape, there is a small circle, which may represent a hole or a pivot point. A dashed horizontal line runs through the middle of the image, possibly indicating a baseline or a reference line for measurements. This image may be related to concepts in geometry, such as volume calculation, symmetry, or it might be representing a physical object like a bell used in different contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y9WzzijrjDWL7ncZGMX00g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - TopShape - 1 Curved](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y9WzzijrjDWL7ncZGMX00g-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Alt-Text: Straight Pipe Lug - TopShape - 2 Squared 
Image-Analysis: The image depicts a rectangular shape which can represent a box or a border and contains a dashed horizontal line near the top with a small circle in the center. This design could symbolize a type of switch, button, or interface element where the circle represents an interactive part (like a toggle) and the dashed line may indicate some form of connection or relationship. The overall layout suggests a simplified schematic or design element possibly related to buttons or user interface elements in a digital context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IHV0q1CDcSO0wNZMZ5QVfA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - TopShape - 2 Squared](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IHV0q1CDcSO0wNZMZ5QVfA-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Rounded 4 - Chamfered


look for an icon that resembles an envelope with a circular seal in the center:  
look for a simple envelope or package icon with a circular hole in the middle, indicating it could be used for mailing or inserting something: 

IJUAhsAngle1::Angle1

Specifies the angle between the start and the end points of the top curve. If the
TopShape is not curved, then the software ignores this attribute. The Angle1 value must be
positive and greater than 90 degrees and less than 270 degrees, else the software
displays a warning message and resets the Angle1 value to 180 degrees.

![Straight Pipe Lug - Side Attributes - Angle1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o0QgdSuzFm2aLdm_0XObXw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f14f5379d9e31ca3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o0QgdSuzFm2aLdm_0XObXw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies top width of the pipe lug. If Width1 is set to zero, then Width2 is used.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Width1 
Image-Analysis: The image depicts a geometric shape resembling a rounded rectangular prism or a truncated cone. It shows a dashed horizontal line across the middle, indicating a bisecting line, which could represent height or midline. There are also arrows pointing sideways at the top, suggesting that it can be measured or compared in terms of its width or diameter. The small circular point in the center likely indicates a reference point or a center for measurement. This setup might be used in contexts involving dimensions such as engineering, architecture, or design to visualize measurements and proportions of this shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hd3krL~lzynwtX38JbCfoQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Width1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hd3krL~lzynwtX38JbCfoQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the bottom width of the pipe lug. If the Width2 and Angle3 values are zero, then Width1 is used instead.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Width2 
Image-Analysis: The image depicts a geometric shape resembling a truncated cone or a bell. The top of the shape is rounded, and there is a horizontal dashed line across the middle. At the center of the top part, there is a small circle, possibly indicating a point of interest or detailing. Additionally, horizontal arrows at the bottom suggest measurement or dimensions, indicating the width or diameter of the shape at its base. The purpose of the shape could be related to measurements in design, engineering, or architectural contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aa2AqtwTpVH6Kb3byYvy~A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Width2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aa2AqtwTpVH6Kb3byYvy~A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle2::Angle2

Specifies the angle of the left tapered portion. If you do not assign a positive value
to Angle2 that is less than 30 degrees, the software displays an error message. If Angle2 is set to zero, then the left line is drawn as global vertical.

![Straight Pipe Lug - Side Attributes - Angle2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K6nVe1m5~RrMI_a8xD1YlA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=75c6c3662c006818)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K6nVe1m5~RrMI_a8xD1YlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3

Specifies the angle of the right tapered portion. If you do not assign a positive
value to Angle3 that is less than 30 degrees, the software displays an error message. Angle3 overrides Width2 to get the tapered bottom point.

![Straight Pipe Lug - Side Attributes - Angle3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yhfPnxTH3Ki2aFLcaRqx~g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=62dd18a6ae4f7277)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yhfPnxTH3Ki2aFLcaRqx~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the lug.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Thickness1 
Image-Analysis: The image depicts a schematic representation of a switch in an electrical circuit. The arrows on the left and right side indicate the direction of the current flow, while the vertical rectangle in the center represents the switch itself. When the switch is closed, current flows through it (indicated by the arrows), completing the circuit. If the switch is open, the current cannot flow, thereby stopping the operation of the connected devices. This illustrates the fundamental principle of how switches control the flow of electricity in a circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kaZ9Cd1gaiq_Mfxk0DebnA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Thickness1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kaZ9Cd1gaiq_Mfxk0DebnA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies the gap between the lug components of a double lug. If a value is not specified,
then a single lug is drawn.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Gap1 
Image-Analysis: The image depicts two vertical boxes with arrows pointing towards each other on the left and right sides. These arrows suggest a force or interaction, possibly indicating compression or drawing something closer together. The boxes may represent objects involved in this interaction. This kind of diagram could be used to illustrate concepts in physics, such as force application or distance adjustment between two entities. The proximity of the boxes to the arrows implies they are the subject of the interaction being represented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uHJLKUK42OVeTm8LbyJ9kQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Gap1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uHJLKUK42OVeTm8LbyJ9kQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerOffset

Specifies the distance a stiffener is offset between the two components of a double
lug. StiffenerOffset is set from the center of pin port.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Stiffener Offset 
Image-Analysis: {explanation='The image depicts a schematic representation of a logical circuit or a function. On the left side, there are two vertical rectangles that likely represent elements of the circuit, possibly inputs or processing units. The small red square within a dashed rectangle may indicate a specific point or a specific condition affecting the operation of the circuit. On the right side, there are two upward arrows, suggesting a flow or a direction of control, indicating how the outputs or signals may be routed or directed based on the conditions set in the circuit. Overall, this image encapsulates the concept of inputs affecting outputs within a logical system, likely indicating functionality.',} 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qa1y5taa2FRKQaR1gl3mFg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Stiffener Offset](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qa1y5taa2FRKQaR1gl3mFg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerHeight

Specifies the height of the stiffener between the two double lug components.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Angle3 
Image-Analysis: The image depicts a mechanical system involving two vertical elements, indicated by the two rectangular blocks on the left, and two arrows indicating a downward force on the right. The dashed red line in the center suggests a point of connection or possibly a pivot point. This arrangement may represent a force transmission system where the arrows signify the application of force resulting in movement or compression between the two vertical blocks. The relationship between the components indicates how the applied force influences the system, likely illustrating concepts of mechanics or structural engineering. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9KoJaoX5iXwah6srEkj7BA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Angle3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9KoJaoX5iXwah6srEkj7BA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerLength

Specifies the length of the stiffener between the two double lug components.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Stiffener Length 
Image-Analysis: The image depicts a schematic drawing of an item with a rounded top and a rectangular opening in the center. The item has a dashed rectangle indicating a moveable part or a space for something to fit in. Red arrows extend outward from the dashed rectangle, suggesting movement or expansion capability left and right. Additionally, there is a circular hole at the top of the image that may serve as a point for attachment or as a guide. The overall impression is that this item has functionality involving space within the dashed rectangle. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k21f21FcSa5qHBQQrpxLZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Stiffener Length](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k21f21FcSa5qHBQQrpxLZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the distance between the top of the lug and the top port. When TopShape is set to 1 - Curved, Offset1 is used as the eye radius.


Image:[Alt-Text: Straight Pipe Lug - Side Attributes - Angle3 
Image-Analysis: The image depicts a geometric shape that resembles a rounded rectangle or a bell-like figure with a circular hole at its mid-point. The top portion of the shape is curved, while the bottom is straight, suggesting it has a wider base. There is a vertical double-headed arrow indicating measurement related to height. The dashed line across the shape might suggest a baseline from which the height is measured. This could be part of a technical drawing relating to dimensions or a blueprint, possibly for a design or engineering purpose. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4_Nuv~4xPx4oFas9qKXcmw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Straight Pipe Lug - Side Attributes - Angle3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4_Nuv~4xPx4oFas9qKXcmw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::ChamfLength

Specifies the length of the chamfered edges. This attribute is valid only when TopShape is set to 4 - Chamfered.


icon that looks like a tag with arrows indicating movement inward or folding: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt / Pin Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776562?contentId=YIWsnGDvmBLJ5ieqV85KEA)
The bolt and pin attributes define the size and location of the bolt and the pin.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt or the pin. If the value is zero the software does
not draw the pin.

IJUAhsPin1::Pin1Length

Specifies the length of the bolt or the pin. If the value is zero the software does
not draw the pin. The length is always centered on the port location.

IJUAhsHeight2::Height2

Specifies the height of the bolt centerline relative to the bottom of the lug. The
height attribute also determines the location of the bolt graphic and the port. You
can ignore this attribute if the RodTakeOut attribute is specified.

![Straight Pipe Lug - Bolt-Pin Attributes - Height2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Ex05qAiOSY6MxeLlzH7EA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=442cad2e8ffc791c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Ex05qAiOSY6MxeLlzH7EA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776565?contentId=TjlNYl9R0D0DYexfxUOwfw)
The following graphic illustrates the orientation of the ports and their sizes for
the straight pipe lug:

![Straight Pipe Lug SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HutBsdriZU8nKYywn4Rh8Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4d91c95f56c5c8c2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HutBsdriZU8nKYywn4Rh8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port details and their orientation

Port1:Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 2 | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2: Lug Port (0, 0, RodTakeOut)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1008 - Single Lug | Can be set as per your specifications. | Smallest size that can connect but can be set as per your specifications. | Largest size that can connect but can be set as per your specifications. |
| 1008 - Double Lug | Can be set as per your specifications. | Smallest size that can connect but can be set as per your specifications. | Largest size that can connect but can be set as per your specifications. |
| 1005 - Pin | Can be set as per your specifications. | Smallest size that can connect but can be set as per your specifications. | Largest size that can connect but can be set as per your specifications. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776602?contentId=ni0VOOSMVC2NI6uKAcYCCQ)
The BOM description must use the part description.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307712?contentId=TBUFO3EQ8f6bZekv5S65Lw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Strap  
Part Name: Strap  
Part Description: Strap SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XxteQr_XJmee5rvDstrEEA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=970022846cf164c2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XxteQr_XJmee5rvDstrEEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Strap SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Pipe Straps > Round Strap - with Wings for Bolting as shown in the following example:

   
Image:[Image-Analysis: The image displays a hierarchical structure of components under the main category "SmartParts," which is further divided into a section labeled "S3D Standard." Within this section, there are various categories such as "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," and "Pipe Straps." The "Pipe Straps" category further expands to include a specific item titled "Round Strap - with Wings for Bolting." This hierarchical format indicates how different components are organized and categorized under the main topic, making it easier to understand the relationship and structure of the items listed. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wyoHCntiASXx4~SH7q3LIw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wyoHCntiASXx4~SH7q3LIw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a three-dimensional coordinate system used in mathematics and physics. It shows the X, Y, and Z axes, which are essential for defining a point in 3D space. The Y-axis is represented horizontally to the left, while the Z-axis is depicted vertically going upwards, both in red. The origin point, labeled as "0,0,0," marks where the three axes intersect. This image helps in understanding spatial relationships and how to represent objects in three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WKhD3YLGeUFK4hTFT7x5ng-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WKhD3YLGeUFK4hTFT7x5ng-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307715?contentId=eG5sAdWr12q6RmTwBTYSrw)
These properties define the geometry of the strap.

IJUAhsStrap::StrapWidthInside

Specifies the inside distance between the legs of the strap. This value is greater
than PipeOD.


None: 

IJUAhsStrap::StrapHeightInside

Specifies the inside height from the base of the strap to the top.


Image:[Image-Analysis: The image illustrates a diagram with a semi-circular arch indicating a parameter related to strap height inside a structure. At the top, there are arrows pointing up and down which likely signify the measurement of a height. The text "StrapHeightInside" is horizontally aligned at the bottom of the arch, indicating the parameter being measured. There are also red dots indicating specific points of reference in relation to the height measurement. This relationship suggests that the height measurement is significant for understanding the dimensions of the strap or arch structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QAai9Ina2A5M5BWTwTuOYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QAai9Ina2A5M5BWTwTuOYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapThickness

Specifies the thickness of the rectangular stock used to make the strap. This value
cannot be zero.


Image:[Image-Analysis: The image depicts a simple diagram that illustrates the concept of "Strap Thickness." It features a curved line resembling a strap or loop, with two red dots positioned within the arc, indicating the points that are relevant to measuring or determining the thickness of the strap. Below the diagram, the word "StrapThickness" is labeled, clarifying the subject of the illustration. The arrows at the bottom suggest measurement direction, emphasizing the distance between the two points, which represents the thickness of the strap being referenced. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eO2vHMLyI9coIi3kbAhKfA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eO2vHMLyI9coIi3kbAhKfA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapStockWidth

Specifies the width of the rectangular stock used to make the strap. This value cannot
be zero.


Image:[Image-Analysis: The image appears to illustrate the concept of "Strap Stock Width" in a design or engineering context. On the left side, there is a diagram showing a round strap with a highlighted red point, which seems to indicate a specific measurement point on the strap. The outer structure might represent the strap while the inner part, with the red indicators, could denote important measurement areas. On the right side, a rectangular shape is presented, probably indicating the stock width dimensions that are relevant to the design or manufacturing of the strap. The double-headed arrows signify measurement width, indicating that this rectangle's width can measure significant parameters for the strap design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1ljSQstP3vNSBrne_vRPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1ljSQstP3vNSBrne_vRPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapFlatSpot

Adds a flat spot in the curved part of the strap. This value can be less than or equal
to StrapWidthInside. If it is set to zero, then no flat spot is shown on the curved part of the strap.
If it is set to a positive value, a flat spot is added in the curved section of the
strap as shown in Fig. 1. If it is set to StrapWidthInside, then the strap is drawn like three plates with no corner rounding as shown in Fig.2.


Image:[Image-Analysis: The image depicts a design or schematic labeled "StrapFlatSpot". It illustrates an object that appears to be a curved frame or strap with arrows indicating a compressive force acting towards the center from both sides. Beneath this curve, there are two red dots which could represent points of interest or specific features related to the design. Additionally, the image includes a label "Fig. 1" in blue at the bottom, indicating that this is the first figure in a series of illustrations. The overall context suggests it is part of a technical or engineering diagram addressing a component or feature. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L_foMXyP1_Lni_S_eyPYAA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L_foMXyP1_Lni_S_eyPYAA-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image depicts a diagram labeled as "StrapFlatSpot", illustrating a flat spot in a strap design. It shows a rectangular shape with two vertical lines representing the ends of the strap and a horizontal line at the top indicating the flat part. There are red dots below the strap indicating specific points of interest for measurement or reference. Additionally, the label "Fig. 2" in blue suggests that this is a figure within a larger set of illustrations, possibly for a technical manual or documentation. The arrows indicate the width measurement across the top of the strap. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/49YX1H_Hc8ecXhTQpFBJ4g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/49YX1H_Hc8ecXhTQpFBJ4g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStrapGap::StrapTopGap

Specifies the gap between outside of pipe and inside of the strap.


Image:[Image-Analysis: The image illustrates a mechanical or structural concept labeled "StrapTopGap." It features a circular element shown at the center with a strap or arch-like structure above it. The lines denote a gap between the circular element and the strap, indicated by vertical arrows pointing downwards. The arrows suggest measurement or attention to this space, possibly for determining the required distance or clearance for proper function or fit in an engineering context. Red squares appear below the circular element, possibly marking points of interest or connection. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iv7Pcgo_PzfbvN3tsQG2hA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iv7Pcgo_PzfbvN3tsQG2hA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapWidthWings

Specifies the width to the outside of the wings. If this value is set to zero, or
less than StrapWidthInside + 2\* StrapThickness, the strap wings are not shown.


Image:[Image-Analysis: The image depicts a diagram showing a particular strap or component design, identified by the term "StrapWidthWings" placed below the illustration. The upper section is represented by a semi-circular shape, while the lower section indicates some width with arrows pointing outward. There are two red dots marked in the upper section, suggesting points of interest or measurement. This diagram likely serves a technical purpose, possibly for specifying dimensions or features associated with the strap in a product design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gS0ucrHqWAROu_KWoo4SfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gS0ucrHqWAROu_KWoo4SfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapOneSided

Standard Yes or No codelist. If this value is set to Yes, the right side of the strap is not shown below the tangent point. Wings, bolts, and
gussets are not included in the right side if StrapOneSided is set to Yes.


Image:[Image-Analysis: The image presents a simple line drawing that appears to show a schematic layout of a structure or a series of connected elements. At the top, there are two curved lines which suggest an overhead arch or doorway, indicative of a structure's upper part. Below, there is a rounded shape that may represent a chamber or enclosed space, suggesting some central area that could be important for circulation or function. Further down, the image presents a rectangular box which could symbolize a foundation, entrance, or platform. The dashed red lines might represent pathways, connections, or dimensions, emphasizing the structure's design. The layout suggests a hierarchal relationship, where the top outlined elements flow into the central area, leading into a foundation. This could represent a conceptual model of a building or an architectural feature. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w2C6s3zJS_jRyYqZ1w75ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w2C6s3zJS_jRyYqZ1w75ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitGap

Specifies the gap at the top and splits the strap into two parts.


Image:[Image-Analysis: The image illustrates a concept labeled "StrapSplitGap." It shows a graphical representation of a structure resembling a gap formed by two symmetrical sides. The two horizontal arrows point inward towards the gap, indicating a closing or narrowing effect. The image contains two red squares positioned between the curved structures at the bottom, which may represent connection points or elements related to the gap. Overall, the diagram suggests a technical or engineering design that involves spacing or separation between two components, emphasizing the importance of the gap in the context it is presented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jedQ1NTVr878ylDPyAdXJQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jedQ1NTVr878ylDPyAdXJQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitExtension

Specifies the length of the tabs from the top inside of the strap to the end of the
tabs.


Image:[Image-Analysis: The image depicts a technical illustration related to a component referred to as "StrapSplit Extension." At the top of the image, there is a vertical line indicating the measurement or height associated with the StrapSplit Extension. The image features a shape that resembles a divided strap or channel, with two sections that seem to originate from the same base but extend outward. Below the main structure, there are two red dots positioned symmetrically, which could represent attachment points or important reference locations in relation to the StrapSplit Extension. This image is likely used in a technical manual or design document to convey information about the component's dimensions and features. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bm4z4gKt3alTE2LFUR_Ctw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bm4z4gKt3alTE2LFUR_Ctw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Hold-Down Bolts Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307717?contentId=PeBvSb9k33mZDEXUzNtHZg)
These properties are optional. Enter values for these properties to add bolt geometry
to the strap. One row of any number of bolts on either side of strap can be added;
however, both sides must have the same number of bolts, the same offset from the strap
centerline, and the same spacing within the row of bolts. There are no separate nuts.

IJUAhsPin1::Pin1Diameter (Optional)

Specifies the pin diameter of all bolts. If Pin1Diameter is set to 0, then no bolts are shown.


Image:[Image-Analysis: The image illustrates a component with two main parts located on either side of a central area. On the left side, there is a simplified view of an electrical pin connector labeled "Pin1Diameter" at the bottom. Above this pin, there are some red points indicating measurement positions. The right side shows a more detailed outline of the electrical connector's shape, suggesting it is designed to fit into a corresponding receptacle. The overall image focuses on dimensions and the design of the connector, specifically highlighting the diameter of the first pin in a visual manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fWuNl~c4y4~g6IGVwR_nWg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fWuNl~c4y4~g6IGVwR_nWg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length (Optional)

Specifies the pin length for all bolts. All bolts have the same length, starting at
Offset2 above the bottom of the strap. If Pin1Length is set to zero, bolts are still shown.


Image:[Image-Analysis: The image displays a technical diagram featuring a component, likely representing an electrical connector. On the left side, there is a depiction of a pin header with dimensions labeled, specifically highlighting "Pin1Length" at the bottom. The presence of red dots suggests specific reference points or dimensions relevant to the pin length. On the right side, another illustration displays the connector from a different angle, providing a visual comparison for understanding its structure or size. This type of imagery is commonly used in electronics to clarify specifications and design details between different views of a component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YjjHgjQ1oHUYgkWxVHSdQg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YjjHgjQ1oHUYgkWxVHSdQg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAOffset1::Offset1 (Optional)

Specifies the offset of the bolt row from the pipe centerline. This value is always
positive.

IJUAOffset2::Offset2 (Optional)

Specifies the offset of the start of the bolts above the bottom of the strap.


Image:[Image-Analysis: The image illustrates a mechanical part that appears to be a type of connector or clamp with an associated diagram denoting an "Offset2" position. The left side shows a top view of a U-shaped connector with red marks that may indicate specific points of interest, such as bolt holes or alignment markers. The right side depicts a side view of the same connector, illustrating how it fits into a parent structure or another component. The dotted line and arrows suggest the possibility of offset positioning for installation or alignment purposes. Overall, the image indicates a component that likely requires precise placement or installation in a mechanical assembly context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VAlK2QPmK~wgskhtrjrs7g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VAlK2QPmK~wgskhtrjrs7g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty (Optional)

Specifies the quantity of bolts. Bolts are not shown on the strap when Multi1Qty is set to zero. Valid cases are shown in the example below.

IJUAhsMulti1::Multi1LocateBy (Optional)

Specifies the location of the bolts. Individual bolts can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (edge). Valid cases are shown in the example below.

IJUAhsMulti1::Multi1Location (Optional)

Specifies the distance for the exact location of the bolts depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge or a center-to-center spacing. Valid
cases are shown in the example below.

Example: Valid Multi1Qty, Multi1LocateBy, Multi1Location cases:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=22c816e178fece5f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b11acb2f39c30a64)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image illustrates a diagram showing the arrangement of multiple items (represented by circles) within a defined space. The text explains key parameters for positioning these items: "MultiQty greater than 3 (5 shown)" indicates that there are more than three items arranged, specifically showing five items here. "MultiLocatedBy = Center (only valid choice)" clarifies that the items should be centered within the defined boundaries. Finally, "MultiLocation = x" specifies that the positions of these items within the space can be represented by 'x', although the exact meaning of 'x' isn't provided in the diagram. The lines and markings further help visualize the layout and relationships of the items to the surrounding space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Block Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307718?contentId=FDVUlT86hggMs4p0YZOEjg)
The block properties are optional and can be used to specify two stacked rectangular
blocks that are used to represent slide plates, shims, insulation pads, cradles, and
so forth. Enter the values for these properties only when Block geometry is required.

The position of Block 1 is exactly Gap1 below the bottom of the strap. The position of Block 2 is on top of Block 1. Both
blocks have similar input properties: height, width and length. The blocks are not
included if any of these values are set to zero.


Image:[Image-Analysis: The image depicts a technical diagram showing two blocks labeled "Block 1" and "Block 2," positioned above a component labeled "Existing Steel." The diagram seems to be illustrating a structural or mechanical assembly involving these blocks and the existing steel base. Block 1 and Block 2 appear to be connected to the existing steel base, which might suggest they are part of a support structure or mounted components, potentially for engineering or construction purposes. The red dots likely indicate points of interest or specific features within the assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ1qRWylGtsXzEfHRM_KVA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ1qRWylGtsXzEfHRM_KVA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1 (Optional)

Specifies the distance between the bottom of the strap and the top of Block 1. This
distance value can be a negative, zero, or a positive value.


Image:[Image-Analysis: The image illustrates a mechanical setup involving two blocks and existing steel. It features a gap labeled "Gap1" at the top, indicating a space between two elements. Below the gap, "Existing Steel" is shown as a base or foundation. There are two blocks referred to as "Block 1" and "Block 2" placed strategically in relation to the existing steel, potentially indicating some form of assembly or support structure. The diagram suggests a relationship where the blocks might be adjusting or resting on the existing steel while maintaining a gap between the upper structure and the blocks. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xw7qQVmSKifMwTmF6rS_6g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xw7qQVmSKifMwTmF6rS_6g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1 (Optional)

Specifies the height of Block 1.


Image:[Image-Analysis: The image depicts a technical drawing or diagram illustrating a specific height measurement labeled as "Height1." The diagram features a shape that resembles a support or beam structure, which has various marked points. The labeled height measurement indicates the vertical distance from the base (shown at the bottom with arrows indicating downward direction) to a reference point at the top of the structure. The use of red dots likely emphasizes key points of interest in the measurement process. This is commonly used in engineering or architectural contexts to denote important dimensions in a design or analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v~R5gTujGuROOafUf_z0ug-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v~R5gTujGuROOafUf_z0ug-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1 (Optional)

Specifies the width of Block 1.


Image:[Image-Analysis: The image depicts a cross-sectional view of a structural element resembling a beam or arch with a specific shape. At the top of the image, there is a curved upper section, while the lower part is a flat, rectangular section. There are two red dots marked along the centerline of these sections, indicating critical points or reference locations. Below the shape, there is a label "Width1", which suggests that it is a dimension or measurement of the width of the rectangular section. This visual representation is typically used in engineering or architectural contexts to convey the dimensions and shape of a component in design or construction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2bdLgqoWP6X_N84uEdxBEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2bdLgqoWP6X_N84uEdxBEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1 (Optional)

Specifies the length of Block 1 in the direction of the pipe.


Image:[Image-Analysis: The image depicts a technical illustration showing two shapes with measurements. On the left is a rounded shape, possibly a component with an arch-like design, where specific points (marked by red squares) indicate measurement reference points. On the right is a rectangular shape, which appears to be a basic outline of a block or another component. Below this shape, the label "Length1" is shown, indicating a dimension related to the rectangle. The overall format suggests that these shapes could be part of design specifications or engineering drawings, where precise dimensions and features are critical for fabrication or modeling. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fUYOvWd2tQVcxWz4rxyMUw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fUYOvWd2tQVcxWz4rxyMUw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2 (Optional)

Specifies the height of Block 2.

A![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PU9d~Vn9WVJZSxR1vxW8KQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d35bb0ac2d3b2587)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PU9d~Vn9WVJZSxR1vxW8KQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2 (Optional)

Specifies the width of Block 2.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9e3MyS4PAap8lhTyPJOdgg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=638be335c0ec400f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9e3MyS4PAap8lhTyPJOdgg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2 (Optional)

Specifies the length of Block 2.


Image:[Image-Analysis: The image displays two different views of a component, likely a type of mechanical part. On the left side, there is a top view of the component, showing a curved section on top and a rectangular base with marked points (highlighted in red) which may indicate specific features or points of interest, such as mounting locations or dimensions. On the right side, there is a side view of the component which depicts its vertical dimensions and shape more clearly. The text “Length2” indicates a measurement that is crucial for understanding the size or fitting of the part in an assembly. Overall, the image provides a technical reference for engineers or designers to understand the shape and size of the component for construction or replacement purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ah93qBWg6kG2F6Eq3x7PqQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ah93qBWg6kG2F6Eq3x7PqQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rectangular Wrap/Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307719?contentId=u7LkCt3jCoIMJbPShxnNyA)
These properties are optional. Enter the values for these properties to represent
rectangular insulation wrap, solid blocks or any strap-shaped liners. There is no
allowance for wings, one-sided straps or split strap shapes. The Thickness4 property determines if it is drawn as a block or as a strap.

IJUAhsWidth4::Width4 (Optional)

Specifies the outside width of a strap or a block. By default, the shape is drawn
with the top as a half-circle with its diameter equal to Width4. This can be changed to a flat top using Width6 as a flat spot.

* Strap


Image:[Image-Analysis: The image depicts a shape resembling an arch or a rounded-top rectangle with measurements indicated. It includes a horizontal line labeled "Width4" at the bottom, suggesting that it represents the width of the arch, which measures 4 units. The two small red dots inside the arch could signify specific points along the height or width, potentially for reference in construction or design. The entire diagram seems to focus on illustrating the dimensions and characteristics of this arch structure, emphasizing its width and the uniformity of the shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/302JpjhhDE12hn2U4bWgvA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/302JpjhhDE12hn2U4bWgvA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Block


Image:[Image-Analysis: The image depicts a geometric shape that resembles a rounded rectangle or an arch. It is labeled with measurement indicators that suggest dimensions, specifically noting a width of 4 units. The top half of the shape is a curved arc while the bottom half is straight, giving it a semi-circular appearance. There are also two small red dots located inside the shape, which could indicate specific points of interest or dimensions. The image likely serves as a visual representation for measurements in a design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pi6S8_Bqmq3avC_~_z_Qog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pi6S8_Bqmq3avC_~_z_Qog-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight4::Height4 (Optional)

Specifies the outside height of the strap of block.

* Strap


Image:[Image-Analysis: The image depicts a diagram of an arch or a rounded structure. It includes two red points located on the vertical sides of the shape, which likely indicate the height or reference points of the arch. Additionally, there is a dimension line labeled "Height4," suggesting that this height measurement is key to understanding the dimensions of the arch. The diagram's simplicity highlights the structure's design and essential measurements associated with it. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wIovLqpRu_jZ5KmKf8xkQg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wIovLqpRu_jZ5KmKf8xkQg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Block


Image:[Image-Analysis: The image depicts a simple geometric shape resembling a semicircle or dome on top of a rectangle. It includes a label indicating "Height 4," which implies that the total vertical measurement from the base of the shape to the top of the dome is 4 units. There is a small red square positioned at the bottom center, which may be indicative of a reference point for measurement or indicating the center of the base. The image visually represents a 2-dimensional shape and its height dimension, which could be relevant in contexts such as geometry or architectural design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lP_Dc9LX2O_Xx8Vx7g_Dwg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lP_Dc9LX2O_Xx8Vx7g_Dwg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness4::Thickness4 (Optional)

Specifies the thickness of the rectangular stock of wrap. If zero or greater than
half of the width, then Thickness4 is ignored and the shape is drawn as a block rather than as a strap.


Image:[Image-Analysis: The image represents a cross-sectional view of a shape, likely a circular arc, with annotations indicating its thickness. The term "Thickness4" at the bottom suggests a specific measurement or designation related to the thickness depicted. There are small red squares positioned along the arc, which may denote specific points of interest or measurement locations. The arrows indicate a measurement of the thickness, showcasing how the thickness dimension is being represented in relation to the shape above. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3fXf_XDE~SXkoZsZngbhhw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3fXf_XDE~SXkoZsZngbhhw-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  If Thickness4 is set to zero, then the block is drawn.


Image:[Image-Analysis: The image shows a geometric shape resembling a semicircle on top of a rectangular base. Inside the semicircle, there is a red point located at the center, indicating a focal point of the shape. The rectangular base has another red point positioned at the center of its bottom edge. This configuration suggests a possible discussion around geometric properties, symmetry, or could relate to concepts in physics such as focus in optics or mechanics, where the dimensions and the placement of points are significant for further analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iMdIeeMv19spN9pkTZZV~g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iMdIeeMv19spN9pkTZZV~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth5::Width5 (Optional)

Specifies the width of the rectangular stock used to make the wrap or block. If Width5 is set to zero, then the shape is not drawn.


Image:[Image-Analysis: The image displays two main shapes: on the left, a curved or circular shape, which is likely representing a tube or pipe section, and on the right, a rectangular shape which could represent a flat piece or a different part. The left side features a predefined width of 5 units, marked by the "Width5" label, indicating the distance across the circular section. Inside the circular section, there is a solid red square, likely indicating a point of interest or a specific measurement location within the circular area. The rectangular shape on the right does not have any annotations, but it appears to be compared in dimensions or context with the curved shape on the left. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jGwzaz9v4cn5Z_EQAOpq9Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jGwzaz9v4cn5Z_EQAOpq9Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth6::Width6 (Optional)

Adds a flat spot on top of the curved part. If set to zero, then the flat spot is
not shown. For a block, if Width6 is greater than Width4, then the strap is drawn as a rectangular block with no curved top. For a strap,
if Width6 is greater than Width4 - 2 \* Thickness4, then the strap is drawn as a rectangular strap with no curved top.


Image:[Image-Analysis: The image displays two different shapes labeled as "Width6." On the left side, there is a rounded shape, while on the right side, there is a square corner shape. Both shapes have a central red dot at the bottom. The arrows indicate the width, which is consistent across both shapes, specifically 6 units. This suggests a comparison between the two designs, where the user can choose between a rounded and a square corner option, both maintaining the same width measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XjInQr5PTqdQ4MIOvzVP9g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XjInQr5PTqdQ4MIOvzVP9g-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  If Width 6 is set to a positive value, a flat spot is added in the top curved section. This
also reduces the radius and center points for the curves. It can be used to produce
rectangular shapes rather than rounded tops.


Image:[Image-Analysis: Could not explain Image because of Safe AI filtering issues. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lstv8ZCpvAVR1MYvcKkGnA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lstv8ZCpvAVR1MYvcKkGnA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Split Strap Bolts Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307720?contentId=Nx_pNbKvnLYtP~uwIwKizQ)
These properties are optional. Enter values for these properties to have a row of
top bolts to use with split, clamp-type straps. These bolts are at the specified offset
from the top of the pipe and are also centered on the top extensions.

IJUAhsPin2::Pin2Diameter (Optional)

Specifies the pin diameter of the bolt. All bolts are drawn with the same diameter.
If Pin2Diameter is set to zero, then the bolts are not drawn.


Image:[Image-Analysis: The image depicts a technical drawing related to measuring the diameter of a pin. The term "Pin2Diameter" is indicated at the top, suggesting that this is a reference or tool for converting between a pin's size and its diameter. Below the text, there is a schematic diagram of a pin with indications for measuring dimensions. The arrows likely represent measurement lines, pointing towards dimensions that need to be noted. The two red squares might denote specific points of interest or measurement. This image illustrates the relationship between a pin's outline and its diameter, emphasizing how to determine the latter based on the former. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7R1dfiKSzUU6srz_NPNqqQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7R1dfiKSzUU6srz_NPNqqQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin2::Pin2Length (Optional)

Specifies the length of the bolt. All bolts are drawn with the same length, starting
at Offset2 above the bottom of the strap. If Pin1Length is set to zero, then the bolts are not drawn.


Image:[Image-Analysis: The image depicts a diagram labeled "Pin2Length", indicating a measurement related to the lengths of pins. It displays two vertical lines representing the pins with a horizontal arrow between them denoting the distance or length measurement. There are two red squares located beneath the pins, which may represent reference points for measurement or markers that indicate specific lengths. The diagram provides a clear representation of how the lengths between the pins can be visually assessed. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sI9qRSYBgbGAGkt0yZUVlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sI9qRSYBgbGAGkt0yZUVlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset3::Offset3 (Optional)

Specifies the offset of the bolt centerline from the top surface of the pipe.


Image:[Image-Analysis: The image presents a technical diagram labeled "Offset3" which appears to illustrate a geometric or mechanical design, possibly related to a piping or engineering component. It includes a circular shape that might represent a pipe or tube, with two vertical lines indicating measurements or offsets. The arrows point in opposite directions, suggesting the measurement of offsets with a reference to the circular component in the middle. This type of diagram is typically used in engineering to communicate dimensions and relationships between various parts of a structure or system. The overall arrangement indicates structural or functional relationships between the offsets and the circular element. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LRTGQt4D1~KuQY2x9FaN5w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LRTGQt4D1~KuQY2x9FaN5w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti2::Multi2Qty (Optional)

Specifies the quantity of bolts. Bolts are not shown on the strap when Multi1Qty is set to zero. Valid cases are shown in the example below..

IJUAhsMulti2::Multi2LocateBy (Optional)

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti2::Multi2Location (Optional)

Specifies the distance for exact location of the bolts depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge or a center-to-center spacing. Valid
cases are shown in the example below.

Example: Valid Multi2Qty, Multi2LocateBy, Multi2Location cases:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=22c816e178fece5f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b11acb2f39c30a64)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image illustrates a multi-location setup involving five circular indicators arranged in a horizontal line. It emphasizes a configuration where the quantity (MultiQty) is greater than 3, specifically indicating 5 circles (shown). The text below the circles specifies that the "MultiLocatedBy" parameter is set to "Center," indicating that the centers of these circles are to be aligned in the center of the setup. Additionally, the "MultiLocation" is referenced with an "x," suggesting a specific positional reference that is not explicitly defined in the image itself. Overall, the image conveys a structured method to arrange multiple items with specific emphasis on their quantity and central alignment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Circle Wrap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307721?contentId=1zIRlcznhAkileHL87WptQ)
These properties are optional. Enter the values for these properties to draw a cylinder
that is coincident with the pipe.

IJUAhsDiameter3::Diameter3 (Optional)

Specifies the outside diameter of the wrap. If it is set to zero, then the wrap is
not shown.


Image:[Image-Analysis: The image features a technical illustration representing two distinct components: on the left, there is a circular shape, possibly signifying a bearing or a ring, highlighted with a red dot at its center, indicating a point of interest. The circle is enclosed within a semi-circle, suggesting a cross-section view. On the right side of the image, there is a labeled "Diameter3" that points to a vertical dimension feature, indicating a measurement related to the component's diameter. Additionally, there are vertical arrows showing dimensions, which denote height or length, indicating that this part also has a specific height parameter to consider along with the diameter. Together, these elements suggest a mechanical component's measurement diagram, useful for technical specifications in engineering or manufacturing contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dml7cUKUBq4Ku4j9rRzqxw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dml7cUKUBq4Ku4j9rRzqxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3 (Optional)

Specifies the length of the wrap. If it is set to zero, then the wrap is not shown.


Image:[Image-Analysis: Could not explain Image because of Safe AI filtering issues. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HqpBji4XjUimZKt93elZPw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HqpBji4XjUimZKt93elZPw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Gussets Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307722?contentId=9asL4nBTRCvmQdIg6Nw2EA)
These properties are optional. Enter the values for these properties to have triangular
gussets. Multiple gussets are allowed. If any dimension or quantity is set to zero,
gussets are not drawn.

IJUAhsHeight3::Height3 (Optional)

Specifies the height of the gussets. If the strap has wings, the gussets are on top
of the wings. If there are no wings, then the gussets are aligned with the bottom
of the strap.


Image:[Image-Analysis: The image consists of two main components: on the left, there is an arch-like shape that is labeled as "Height3," and it is associated with marked red squares at the base, which likely indicate measurement points. The arch represents a physical structure, while the right side shows a vertical bar graph with varying heights. The bar graph illustrates different height measurements, possibly comparing the height of the arch with those of other objects or structures. This image likely serves to demonstrate a relationship between the geometrical shape of the arch and quantitative measurements shown in the bar graph, providing a visual comparison of heights. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4vk7Yrc2cLBI7sspiTMFCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4vk7Yrc2cLBI7sspiTMFCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3 (Optional)

Specifies the width of the gussets.


Image:[Image-Analysis: The image depicts a technical drawing that appears to illustrate the dimensioning of an arch or a similar structure. The drawing includes the word "Width3," indicating a measurement of width related to the arch. There are two red dots marked on either side of the arch, likely denoting specific points of interest or measurement. To the right of the arch, there's also another box, probably indicating a separate component or section, which might be related to the main structure with varying heights depicted in three vertical rectangles. This suggests a relationship between different parts of the design, emphasizing the measurements and proportions of each section for clarity in construction or fabrication. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zb4k2DScUV1ueES8UHBmIg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zb4k2DScUV1ueES8UHBmIg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3 (Optional)

Specifies the thickness of the gussets.


Image:[Image-Analysis: The image appears to be a technical illustration related to a cross-section view of a curved structure, possibly a pipe or a tunnel. The diagram includes a rectangular section on the right side, possibly indicating where to measure thickness. The term "Thickness" is emphasized, suggesting that the focus of this illustration is on determining the thickness of the material at various points along the curve. There are also red marks indicating specific measurement points or reference points, which are likely important for ensuring proper dimensions are maintained during construction or analysis. The overall layout indicates a relationship between the curved and straight sections, hinting that thickness may vary depending on location. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lxeWfcvGALk~gFDlzMsSdQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lxeWfcvGALk~gFDlzMsSdQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti3::Multi3Qty (Optional)

Specifies the quantity of the gussets. Gussets are not shown on the strap when Multi1Qty is set to zero. Valid cases are shown in the example below..

IJUAhsMulti3::Multi3LocateBy (Optional)

Specifies the location of the gussets. Individual gussets can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of gussets. This value can be 0 (nothing), 1 (center), or 2 (edge). Valid cases are shown in the example below.

IJUAhsMulti3::Multi3Location (Optional)

Specifies the distance for exact location of the gussets depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge or a center-to-center spacing. Valid
cases are shown in the example below.

Example: Valid Multi3Qty, Multi3LocateBy, Mult32Location cases:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=22c816e178fece5f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBCV6B82_8iqtBO_I5OJxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b11acb2f39c30a64)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kot79AmpHgcWgbHh240bQ-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image illustrates a diagram related to a quantity and location system, specifically showing how to position multiple items. It contains five circles aligned in a horizontal row, suggesting that multiple items are being displayed. There are annotations explaining the configuration: "MultiQty greater than 3 (5 shown)" indicates that there are more than three items in this configuration, and the specific scenario shown has five items. "MultiLocatedBy = Center (only valid choice)" states that the items should be centered as their placement strategy. Finally, "MultiLocation = x" denotes the variable or space where the items will be situated. Overall, the image serves as a guideline for a geometric arrangement of products or icons, focusing on their quantity and alignment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/byM6GJHt6w~dRy1ZcrO61A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Min/Max Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307723?contentId=3wmbDa2hvFAe4YUsWE2UXw)
IJUAhsMinPipeToSteel::MinPipeToSteel

Specifies the minimum allowed clearance between outside of pipe and steel.

IJUAhsMaxPipeToSteel::MaxPipeToSteel

Specifies the maximum allowed clearance between outside of pipe and steel.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [User Prompts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307725?contentId=skSQcyTKAkguOZ8JjoqZnw)
You can edit these properties on the part properties dialog box.

IJOAhsPipeOD::PipeOD

Specifies the actual outside diameter of the pipe (or insulation). By default, it
is set to some reasonable value. Typically this value is passed in by the Assembly
Information Rule (AIR). This value is used to position the strap vertically along
with StrapTopGap.

IJOAhsPipeToSteel::PipeToSteel

Specifies the clearance between the outside of the pipe and the steel. By default,
it is set to some reasonable value. Typically this value is passed in by the AIR.

IJOAhsSteelThickness::SteelThickness

Specifies the thickness of the steel to which the U-Bolt is attached. By default,
it is set to some reasonable value. Typically this value is passed in by the AIR.

IJOAhsRoty::RotY

Rotates the strap along the Y-axis of the route port. Use this property to run the
strap across the pipe and perpendicular to the pipe centerline.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Maintenance Aspect - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/722582?contentId=QkmkITyPDqYG5yAShxgBJA)
IJUAhsCreateMaintAspect::CreateMaintenanceAspect

Specifies a boolean value for the maintenance aspect of the Strap.

IJUAhsMaintenanceTh::MaintenanceThickness

Specifies the maintenance thickness.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307726?contentId=_7wFVvme3lX66dS_SjpMew)

Image:[Image-Analysis: The image displays a structured table divided into two main columns labeled "Route" (left) and "Steel" (right). Each column lists various attributes associated with ports of two entities, identified as HgSymbolPort(1) and HgSymbolPort(2). Under the "Route" column, the listed attributes are: Name, PortType, Size, MinSize, and UnitType for HgSymbolPort(1). In the "Steel" column, similar attributes are listed for HgSymbolPort(2), which include Name, PortType, Size, MaxSize, and UnitType. This organization indicates a relationship between two port types, highlighting their respective attributes in a side-by-side comparison for clarity and reference. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ijlk4Pac4DNAjweneC1ACA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ijlk4Pac4DNAjweneC1ACA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Strap


Image:[Image-Analysis: Could not explain Image because of Safe AI filtering issues. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x08EKvCGYtDGBi6iiH_Xng-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x08EKvCGYtDGBi6iiH_Xng-_PVFQNoCl4XmjAxWO0f7XQ/content)


None: 

* BOPtoTOS is Bottom of Pipe to Top of Steel (PipetoSteel).
* If RotY is given a value, the route port is rotated about its Y-axis, effectively tilting
  the strap when it is joined to the pipe reference port.
* To join the strap to the structure, the steel port must be at PipeOD/2 - BOPtoTOS. To add a plate below the strap, use BottomofStrap - Gap1 - Block1Height.

Port1 - Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 - Steel

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Steel | 1011 (Steel) | Not applicable for this type of port. Use 0. | Not applicable for this type of port. Use -9999. | Not applicable for this type of port. Use 9999. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strut\_A - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307708?contentId=DBTl6unSkTcyssaO23ltIQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Strut\_A  
Part Name: Strut A  
Part Description: Strut A SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JYcYuqMmMVwZG~9PRLKHqw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6f6bcf4222d2191b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JYcYuqMmMVwZG~9PRLKHqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Strut\_A SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Struts > Adjustable Rigid Strut - Part A as shown below.

   ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pKNzdMxBhzkEdSsCGtXwJg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=706f456e6552e166)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pKNzdMxBhzkEdSsCGtXwJg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

This symbol is used to represent struts and snubbers. The Strut\_A shapes are divided
into the following.

* Five graphic shapes: Round, Oval, Square, Rectangular, Hexagonal shapes are possible
* One rod end shape: Plain, Eye, One Spade, Two Spades, Bolt, Nut (Female) end shapes
  are possible
* One side shape: Round, Oval, Square, Rectangular, Hexagonal shapes are possible

Most of the struts and snubbers also require a separate Strut\_B end part to allow
rotation of the two ends, especially for eye or lug shaped ends.


Image:[Image-Analysis: The image presents a technical or engineering diagram illustrating a component with multiple identifiable parts. It includes a linear arrangement of labeled sections, namely "End1," "Shape1," "Shape2," "Shape3," "Shape4," and "Shape5." Each of these labels denotes a specific segment of a larger object or assembly. "End1" appears to be a rounded part at the far left, possibly representing a connection point or interface, while "Shape3" is depicted as a central block that could be a main body or housing for other components. The "Side" label suggests there is another section or feature that is oriented perpendicularly to the main axis of the object. Overall, the diagram aims to clarify the structure of this object by defining its various parts and how they are connected. The red dots at "End1" and "Shape5" may indicate points of interest or interfaces for connection or measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9nH5MQ7ME0Yo2aEYjlqZ5A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9nH5MQ7ME0Yo2aEYjlqZ5A-_PVFQNoCl4XmjAxWO0f7XQ/content)


None: 

* The graphics are built up by defining the various shapes while the port locations
  are determined only from the Length property. Enter the Length property correctly in the workbook to determine the port correctly. In some cases,
  for example if the second end is a female threaded hole, the port will not be coincident
  with the end of the shapes.
* Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
  specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: {explanation='The image appears to be a schematic diagram of a mechanical system, likely representing a fluid or hydraulic mechanism. There are two ports labeled "Port1" and "Port2," suggesting input and output connections. Port1 has coordinates labeled as "0,0,0," which could indicate its position in a three-dimensional space, while Port2 is labeled as "0,0,Length," implying it extends in length from the connection point. 

The diagram includes a component labeled as "Z," which could represent a cylinder or actuator, and there is an arrow indicating direction labeled "X" showing the action that might occur in this system, suggesting movement or fluid flow. Overall, it illustrates the configuration of the system, connections, and how various components relate spatially to one another.'} 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rA8cW1OXj9ILxtdsAmXifQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rA8cW1OXj9ILxtdsAmXifQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307730?contentId=hPFDyaoVC~TFkJ_C2eyjyQ)
These properties are used for the port locations and shape stretching. Enter the values
to get a correct port location and to define which shape part needs to be stretchable
or flexible.

IJOAHgrOccLength::Length (if variable length)

Enter the reasonable default length of the strut that specifies the distance between
Port1 and Port2 regardless of end type. The value of this length is determined by the user during
placement. For the location of ports with each end type, refer Port Details section
below. This property should be an occurrence attribute.

-OR-

IJUAhsLength::Length (if fixed length)

Enter the length of the strut which specifies the distance between Port1 and Port2
regardless of end type.


Image:[Image-Analysis: The image depicts a simple schematic representation of a hydraulic or pneumatic system. It features a cylinder (indicated by number 1) connected to a control unit (represented by the rectangular box in the middle). The left end of the cylinder has a circular shape, which likely represents a piston or a connection point, while the right end (labeled as number 2) indicates the direction of force or motion produced by the system. The horizontal line between the components suggests a connection, perhaps showing how fluid or air travels through the system to operate the cylinder. This diagram could be used to understand the basic functioning of a system involving linear motion generated by pressurized fluid or air. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FKRy4QQLCMRbXAQijadGOQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FKRy4QQLCMRbXAQijadGOQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStretchShape::StretchShape

For variable length struts, specify a value from 0 to 5 to determine which of the
five shapes should be stretched. If this value is set to 0, then none of the segments
will be variable in length.

0 - None  
1 - Shape 1  
2 - Shape 2  
3 - Shape 3  
4 - Shape 4  
5 - Shape 5


Image:[Image-Analysis: The image depicts a technical diagram showcasing various shapes and components identified as End1, Shape1, Shape2, Shape3, Shape4, and Shape5, with a labeled section referred to as "Side." The diagram appears to outline a linear arrangement of different geometric forms, likely representing parts of a mechanical or engineering assembly. "End1" seems to denote one terminal point in the configuration, while "Side" suggests a separate component or area related to the overall structure. There is an indication of specific shapes or structural elements (Shape1 to Shape5) that are probably important for understanding the function or composition of the assembly. Additionally, it may imply a sequential relationship, where each shape contributes to the final design or operational capability of the assembly, demonstrating connections between these shapes in a potentially mechanical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9nH5MQ7ME0Yo2aEYjlqZ5A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9nH5MQ7ME0Yo2aEYjlqZ5A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End1 Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307742?contentId=nk~kgVd8JJvOxQbBFQt8iA)
These properties specify the End1 shape properties for the Strut\_A.

IJUAhsRodEnd1::RodEnd1Type

Specifies the graphic shape to be used at End1. The value for this column is a codelist number. Valid codes are listed in the HS\_S3DParts\_Codelist.xls
workbook on the hsRodEndType sheet. Enter the ShortName of codelist for readability in XLS. The nut (female) uses the same graphic shape
as the bolt, but the port orientation will be reversed. The port location (red dot)
is at z=0.

1 – Plain (Default, no additional graphics)


Image:[Image-Analysis: The image shows a rectangular box with red indicators on the left and right sides, and a circle on the right. The rectangle may represent a button or a clickable element, while the circle could symbolize a status indicator or an option. This layout may indicate a user interface element where the user can select or interact with the rectangular button, and the circle might show active status or provide additional functionality related to the button. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Eye


Image:[Image-Analysis: The image consists of three distinct shapes. On the left, there is a circular shape connected to a rectangular shape, with a small red square inside the circle, indicating potentially a mechanism or a relation between the two shapes. The circle could represent a wheel or a gear, while the rectangle might indicate a bar or rod. To the right, there is another shape that appears to connect with the elements on the left. This right shape is also circular but is showcased in a different perspective, possibly representing a slot or a holder. The arrangement suggests an interaction between these objects, possibly indicating a mechanical system or assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpwJXnWbOC4xbnsvsvXcXQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpwJXnWbOC4xbnsvsvXcXQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image depicts a simplified electrical circuit involving a plug and a socket. On the left, there is a plug with a red dot indicating a terminal, which is typically the live wire connection. The plug is designed to fit into a socket, shown on the right side. The socket has a circular opening that corresponds to the shape of the plug's head. This setup illustrates the basic connectivity required for electrical devices to receive power from an outlet. Such configurations are commonly used in household or industrial settings for devices that require electrical energy to operate. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MhWI4GOW0cXZO8zRAc7PEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MhWI4GOW0cXZO8zRAc7PEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image depicts two main components often found in mechanical assemblies. On the left, there is a representation of a bolt, consisting of a long shaft (the body) with a head at one end and possibly a nut on the other side. The red dots indicate points where the bolt could interact with other components, such as being fastened through a hole or paired with a nut. On the right, there is a circular representation which likely represents a washer or a nut, which are commonly used in conjunction with bolts to distribute load or secure the assembly. The washer goes underneath the bolt head or nut to protect the surface and prevent loosening due to vibrations. This relationship highlights how bolts and nuts/washers work together in fastening applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zI2wn~ijXRiDHa~gxNTeHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zI2wn~ijXRiDHa~gxNTeHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image shows two different mechanical components, specifically a cylindrical rod on the left and a circular disc on the right. The rod is depicted with a rectangular block next to it and includes red indicators at both ends, likely representing the ends of the rod. The circular disc on the right appears to have a dot or marker at its center, which may indicate a feature such as a pivot point or a marking for alignment. These components may represent parts of a simple mechanical assembly, where the cylindrical rod could fit into or work with the circular disc in some way. The presence of red dots might indicate important points of interest, such as connections or load-bearing points. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RrS5CX_8vofbFbgKVCLFjA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RrS5CX_8vofbFbgKVCLFjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

JUAhsThickness1::Thickness1

Specifies the thickness of the rod end. This value can be negative for Type 4 - Bolt
and Type 5 - Nut.

1 – Plain (no effect on graphics)


Image:[Image-Analysis: The image shows a rectangular box with red indicators on the left and right sides, and a circle on the right. The rectangle may represent a button or a clickable element, while the circle could symbolize a status indicator or an option. This layout may indicate a user interface element where the user can select or interact with the rectangular button, and the circle might show active status or provide additional functionality related to the button. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Eye


Image:[Image-Analysis: The image illustrates two mechanical components typically found in engineering applications. On the left side, there is a depiction of a circular mechanical part with a red highlighted center, which may represent a bearing or a wheel component, along with a shaft that appears to extend horizontally. On the right side, two parallel lines indicate a positioning mechanism, possibly a pair of clamps or a switching device. The relationships between these components may suggest that the circular part could rotate or move within the positioning mechanism represented on the right side. Overall, this image represents components that may interact in a mechanical system, possibly for motion or fastening purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VDcI~xxAVuI9tHBsmcc4bw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VDcI~xxAVuI9tHBsmcc4bw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image shows two different electrical components. On the left side, there is a representation of a plug with a red dot indicating a terminal connection, which is commonly used to connect electrical devices to a power source. On the right side, there are symbols representing a switch and a resistor. The switch symbol shows the two positions of an on/off switch, indicating that it can either allow or disrupt current flow. The resistor symbol shows a component that resists the flow of current in a circuit, controlling voltage and current. These components are essential in circuit designs for managing and directing electrical energy. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOY75MHuIeQqCggew5utsw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOY75MHuIeQqCggew5utsw-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image depicts a simple electrical circuit. On the left side, there is a switch with a red indicator, and on the right, it shows a light bulb also indicated by a rectangle. The arrows between the switch and the light bulb suggest that the switch is used to control the flow of electricity to the light bulb. When the switch is closed (turned on), electricity flows to the bulb, lighting it up; when open (turned off), the flow stops, and the bulb goes out. The red indicators at each point suggest that these components might be active or highlighted in a certain context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image depicts a simple electrical circuit. On the left side, there is a switch with a red indicator, and on the right, it shows a light bulb also indicated by a rectangle. The arrows between the switch and the light bulb suggest that the switch is used to control the flow of electricity to the light bulb. When the switch is closed (turned on), electricity flows to the bulb, lighting it up; when open (turned off), the flow stops, and the bulb goes out. The red indicators at each point suggest that these components might be active or highlighted in a certain context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length from the base of the spade to the port location, which is also
the start of the curved end. Only zero or positive values are allowed. This property
is valid for spade end type only.


Image:[Image-Analysis: The image depicts a simple mechanical system comprising a block and a slider mechanism that allows motion along a linear path. The block appears to be fixed, while the slider can move left and right along a horizontal axis, indicated by the horizontal arrows. There is also a circular shape with a red dot in the center, which may represent a pivot point or a connection point for the slider. The left part of the image shows a schematic of the moving parts, making it clear that the setup is likely designed for demonstrations of motion or mechanics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tXG7etG~3QePnR_FirPGIA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tXG7etG~3QePnR_FirPGIA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the outside diameter of the rod ends.

1 – Plain (no effect on graphics)


Image:[Image-Analysis: The image shows a rectangular box with red indicators on the left and right sides, and a circle on the right. The rectangle may represent a button or a clickable element, while the circle could symbolize a status indicator or an option. This layout may indicate a user interface element where the user can select or interact with the rectangular button, and the circle might show active status or provide additional functionality related to the button. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eRGzQfyA8HIx9cTk~zmQUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Eye


Image:[Image-Analysis: The image depicts a mechanical system likely representing a linear motion mechanism. It features a cylindrical component (possibly a rotary part) attached to a red block, indicating a point of action or connection. The central circular area may represent a rotational element where the red square suggests a pivotal point or a location for a connection. To the right, there is a vertical arrow indicating movement or a measure of distance, suggesting the function of this assembly is to translate rotary motion into linear motion, or vice versa. The black lines and arrows help to show directionality, indicating the nature of forces or movement involved in this mechanical setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PkirdDBSg2l~APF3iRhqDA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PkirdDBSg2l~APF3iRhqDA-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image depicts a simple mechanical or electronic connector, typically used in various devices and circuits. The left side of the image shows a red dot, which possibly indicates a pin or an input/output reference point. The circular part at the center is likely the main body of the connector, featuring a hole in the center (showing the red square), which suggests a receptacle for another pin or wire to fit into. To the right, two vertical arrows indicate measurements, possibly showing the height or width of the connector itself. Overall, the image visualizes the structure and dimensions of a specific type of connector. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TvNtvDW0wc0swf8wRM8Cww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TvNtvDW0wc0swf8wRM8Cww-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image depicts two different shapes: on the left, there is a horizontal rectangular box with red dots at each end, which may represent the endpoints of a line. On the right, there are two triangular arrowheads pointing upwards and downwards at the top and bottom of a vertical line connecting them. This suggests a relationship indicating measurement or direction, possibly showing height or some form of elevation between the two arrowheads. The use of red dots may indicate significant points, such as supports or connections, in relation to the rectangular shape, further implying that these shapes are part of a larger system or drawing concerning structural or mechanical design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image depicts two different shapes: on the left, there is a horizontal rectangular box with red dots at each end, which may represent the endpoints of a line. On the right, there are two triangular arrowheads pointing upwards and downwards at the top and bottom of a vertical line connecting them. This suggests a relationship indicating measurement or direction, possibly showing height or some form of elevation between the two arrowheads. The use of red dots may indicate significant points, such as supports or connections, in relation to the rectangular shape, further implying that these shapes are part of a larger system or drawing concerning structural or mechanical design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies a double-spade end or a single-spade end. If this value is zero, then a
single-spade is drawn. If this value is a positive number, then a double-spade is
drawn with two identical spades separated by the gap value defined here.


Image:[Image-Analysis: The image depicts an electrical circuit component. On the left side, there is a representation of a battery with markings that indicate the positive and negative terminals. The right side shows a switch, which is typically represented in a way that illustrates its ability to control the flow of electrical current. Arrows near the switch imply the direction of current flow when the switch is closed or opened. The battery provides power to the circuit, and the switch allows users to open or close the circuit, thereby controlling the operation of other components connected in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ltl85UL0Pvj~G3ysAVAYIQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ltl85UL0Pvj~G3ysAVAYIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsAngle1::Angle1

Specifies the rotation angle about the longitudinal axis for the rod end, Shape 1,
and the port.


Image:[Image-Analysis: The image depicts a simplified schematic of an electric motor. On the left side, there is a circular symbol representing the rotor and a small arrow indicating the direction of rotation. The rotor is connected to a stator (the rectangular shape in the middle) which generates a magnetic field. The motor's design allows for conversion of electrical energy into mechanical energy, enabling it to perform work. The dotted line suggests the flow of electrical current, and the arrangement of components shows a basic relationship where the rotor and stator work together to create movement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rv_VM0BT5ybctK5y7Gx_cw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rv_VM0BT5ybctK5y7Gx_cw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307997?contentId=zuTzVPUCAg0uD9fsw_Vh~g)
The shape properties specify the segments shapes properties for Strut\_A. Specify None for the ShapeNtype property, if the shape ‘N’ is not needed. For example, if Shape 4 does not need to
be modeled, you would enter None for the Shape4Type properties. The shapes can be defined by:

For Struts:


Image:[Image-Analysis: The image appears to illustrate a diagram featuring multiple shapes and labels, which may represent a flow or a process. The diagram includes the following components: a circular shape labeled "End1", which likely signifies a starting or terminating point in a process; three rectangular shapes labeled "Shape1", "Shape2", and "Shape3", which presumably denote specific activities or stages within that process; and two additional shapes labeled "Shape4" and "Shape5" that suggests forward movement or continuation. Overall, the diagram seems to depict a process flow, connecting different entities with arrows or lines, each with specific functions as defined by the labels. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/En13t~~S5ynuah_3pfEqrA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/En13t~~S5ynuah_3pfEqrA-_PVFQNoCl4XmjAxWO0f7XQ/content)

You would specify None for Shape6Type because no side shapes is needed for struts.

For Snubbers or the Struts which have additional side shape:


Image:[Image-Analysis: The image depicts a schematic representation of a mechanical or engineering component labeled with various shapes and identifiers. At the far left is "End1" which connects to "Shape1" and "Shape2", suggesting these are parts that fit or connect at this end. The main body of the component is represented by a rectangular "Shape3" in the center. Additionally, there are two more shapes, labeled "Shape4" and "Shape5", connected at the right side of "Shape3". At the top, there is a label "Shape6 (Side)", indicating a side view or aspect of the component. This schematic likely serves to illustrate the structure and connection points of the various parts in a mechanical assembly or design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L4DiM_3UScHdQ_VlEanyQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L4DiM_3UScHdQ_VlEanyQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

The length of the shapes can be set to negative, zero, and positive values. For example:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UD2f34SJOdbcVJuv4Yi3Rw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=38b3914248f0b32d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UD2f34SJOdbcVJuv4Yi3Rw-_PVFQNoCl4XmjAxWO0f7XQ/content)

For the figure above, the strut would be modeled by entering Shape4Length to be a negative value as shown below. Set the Shape5type value to be None because there is no Shape 5 type.


Image:[Image-Analysis: The image depicts a diagram with various shapes represented as labeled outlines. There are four primary shapes: Shape1 is a small circle (likely representing a point), Shape2 is a line extending from Shape1, Shape3 is a longer line extending further, and Shape4 is another line indicated with a negative sign suggesting a direction or characteristic opposite to the others. The shapes appear to be interconnected, with arrows showing the direction associated with Shape2 and Shape3, while Shape4 indicates a negative direction or impact. The red dots within the shapes may indicate specific points of interest or reference points related to these shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WAI6Z3DhkPvjG7yW5n~OEA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WAI6Z3DhkPvjG7yW5n~OEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

There are similar properties for Shape1, Shape2, Shape3, Shape4, Shape5, and Shape6.
Shape1 properties descriptions are shown below. All other shapes needs to follow the
same methods for corresponding shapes properties.

In general, the shape properties are defined as:


Image:[Image-Analysis: The image is a schematic representation of a mechanical system or device, likely illustrating a specific configuration of shapes and their dimensions in a 3D space. It features three axes labeled X, Y, and Z which typically represent three-dimensional coordinates. The arrows indicate the direction of these axes; X is represented with a red arrow pointing to the left, Z is directed horizontally, and Y is oriented vertically. Additionally, there are two measurements labeled "Width1 of shapes" and "Length of shapes," which suggest specific dimensions related to these shapes within the system. The image may be used for an engineering or design purpose, providing a visual aid for understanding the spatial and dimensional relationships between the components of the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2FyZgFQHpK_NZx2X~n~K7w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2FyZgFQHpK_NZx2X~n~K7w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Enter ShapeNWidth1 is in X direction  
Enter ShapeNWidth2 is in Y direction (into the page)  
Enter ShapeNLength is in Z direction (along length of strut/snubber)

Where N is the Shape Number of 1, 2, 3, 4, 5, or 6

IJUAhsShape1::Shape1Type

Specifies the graphic shape. The center hole shown in the figures below is only for
reference and will not be modeled. The value for this column is a codelist number
from the HS\_S3DParts\_Codelist.xls workbook on the hsShapeType sheet.

1 - Round


look for icon that looks like a circular loading or spinning indicator: 

2 - Square


look for an icon that looks like a loading circle or spinner: 

3 - Hex


icon of a hexagon with a circular shape inside it, resembling a chemical structure or molecule representation: 

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the shape.

1 - Round


Image:[Image-Analysis: The image depicts two geometrical shapes: a vertical line representing a double-ended arrow and a circle. The double-ended arrow indicates measurement or distance, with arrows pointing upwards and downwards, suggesting that this may represent a height or vertical dimension. The circle represents a cylindrical shape, indicating that the measurement of height may pertain to the cylinder illustrated. This connection suggests that the image could relate to dimensions of a cylindrical object, either showing the height alongside the circular face of the cylinder. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZRreIyn75y~tHR6xZjZxlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZRreIyn75y~tHR6xZjZxlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image consists of two icons. On the left, there is an icon depicting a vertical arrow with another inverted arrow, suggesting a concept of "up and down" movement or adjustment. This typically represents a function related to resizing or changing height. On the right, there is a square with a circle inside it and small dots around the circle, which usually symbolizes a concept of selecting, editing, or various settings related to a circular object. The relationship between these two icons could indicate an interface where one might adjust the vertical size of a circular element or an object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oI0GRIGGxHUOGXiBdAYqAw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oI0GRIGGxHUOGXiBdAYqAw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image depicts a hexagonal shape that has arrows pointing outwards from its left and right edges. This could represent a mechanical component or a fitting that connects two sections in a symmetric manner, indicating that it can expand or contract or that it serves as a connector between two entities while being adjustable. The inner circle within the hexagon might symbolize a socket or a joining point where another component could be attached. The arrows suggest movement or the ability to change dimensions, emphasizing flexibility or adaptability in design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Sg8NSqXiVE0SmBGuNzHzqQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Sg8NSqXiVE0SmBGuNzHzqQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the outside length of the shape. If this value is set to zero or a negative
value, then Shape1Width1 is used. This value is not used for the hex shape.

1 - Round


Image:[Image-Analysis: The image depicts a cylindrical shape, often representing a right circular cylinder. The top view is shown as an ellipse, while the side view is represented with two vertical lines indicating the height and horizontal lines indicating the diameter. This shape can be related to various practical applications including storage tanks, barrels, and pipes, where understanding the dimensions and volume is vital. The empty circle inside the ellipse could represent the top opening of the cylinder. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIZKYqYtPD69HrSW0Lv4JQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIZKYqYtPD69HrSW0Lv4JQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image features a circular shape positioned above a rectangular shape, with arrows on both sides of the rectangle pointing outward. This configuration visually represents the idea of expansion or growth, where the circular shape could symbolize an object or idea that is seeking to spread or increase within the confines of the rectangular area. The arrows suggest movement to the sides, indicating that whatever is represented by the circle interacts with the boundaries of the rectangle, potentially expanding beyond it. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mekLIORzDLy0bOFAjSe4fg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mekLIORzDLy0bOFAjSe4fg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the length for the shape. If this value is zero, then the shape is not displayed.
Both positive and negative values are valid.


Image:[Image-Analysis: The image depicts a mechanical or engineering diagram, likely related to a type of actuator or coupling system. It shows a cylindrical object on the left, which may represent one end of a machine or a part with a circular cross-section. The straight section extending from it likely represents a shaft or connecting piece. The two circular ends in the diagram, marked with red dots, might indicate connection points or operational endpoints. The dimensions, indicated by the horizontal arrows at the bottom, suggest that the image might include specifications for the measurements of the components involved. The relationships between the components suggest a functional assembly where forces or movements are transmitted from one part to another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hwv3wBMn6drVuN_VQ4d33g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hwv3wBMn6drVuN_VQ4d33g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Feature Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308038?contentId=3XkrkSah9JnU1aKOjfRBng)
These properties specify the side feature shapes properties for the Strut\_A. Define
values only when the side shape is needed.

IJUAhsLoc1:Loc1X

Enter the X coordinate distance for the start position of the center (not the edge)
of the side nut shape.

IJUAhsLoc1:Loc1Y

Enter the Y coordinate distance for the start position of the center (not the edge)
of the side nut shape.

IJUAhsLoc1:Loc1Z

Enter the Z coordinate distance for the start position of the center (not the edge)
of the side nut shape.

The black dot in the figure represents the Loc1 position, which might have XYZ values
of (-5.5", 0", 12") for example.


Image:[Image-Analysis: The image illustrates a simplified schematic of a mechanical or pneumatic device. It shows a cylinder with an attached actuator, likely indicating a system that involves movement or control based on pressure or fluid dynamics. The arrows labeled X and Z suggest directions of movement or flow: X points downwards and Z points left, indicating the possible movement of a piston or a fluid. The small box at the top may represent a control unit or sensor that governs the operation of the device. This diagram is useful for understanding how different parts of the system are interconnected and how they operate together to achieve a specific mechanical function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G6o19v8S_~cBUFr7YuMIHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G6o19v8S_~cBUFr7YuMIHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDirection1::Direction1

Specifies the orientation direction of the side nut shape relative to the LOC1 start
position. In the example figure above, the shape runs in the positive Z direction
from the start position. The values for this property are in the HS\_S3DParts\_Codelist.xls on the hsDirection sheet.

0 is positive X  
1 is negative X  
2 is positive Y  
3 is negative Y  
4 is positive Z  
5 is negative Z# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Other Strut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308040?contentId=DJueNOeuLFhUeb2I3ScsGA)
These properties specify the other strut properties like bill-of-materials (BOM) and
weight. Enter these properties which will be used for only BOM description and for
weight but not for the modeling geometry.

IJUAhsMinLen::MinLen

Specifies the minimum length that is allowed for this strut. If the strut is shorter
than this length, a warning message appears. If you do not want a warning message,
enter zero for the minimum length.

IJUAhsMaxLen::MaxLen

Specifies the maximum length that is allowed for this strut. If the strut is longer
than this length, a warning message appears. If you do not want a warning message,
enter a large value such as 9999m for the maximum length.


None:  These minimum and maximum length values will be different from the manufacturer's
catalogs since this length does not include the separate Strut\_B part length.

IJUAhsRepOverLen1::RepOverLen1

Specifies the additional length that needs to be added or subtracted from the modeled
length of the strut when reporting the length in the bill-of-materials (BOM) description.
This value does not affect the strut graphics in any way. This value should be the
length of the separate Strut\_B part when it is connected.

* If this value is zero, then the actual Port1 to Port2 length is used in the BOM description.
* If this value is a positive number, then this value is added to the Port1 to Port2 length and the resulting sum is used in the BOM description.
* If this value is a negative number, then this value is subtracted from the Port1 to Port2 length and the resulting value is used in the BOM description.
* If the resulting value is less than or equal to zero, then the strut length is not
  included in the BOM description.

IJUAhsWtPerLen::WtPerLen

Specifies the value to use for calculating the total strut weight based on the final
strut length. The total weight is calculated by adding the variable weight and the
fixed weight.

* If StretchSegment is set to zero, then the actual graphical length between Port1 and Port2 is used for the length and the RepOverLen1 property is ignored. The weight for the fixed length is added in the Weight property as a fixed value.
* If StretchSegment is anything other than zero, then the calculated length/thickness of the segment
  (that is variable in length) is used for the weight.

IJUAhsWeight::Weight

Specifies the weight for the fixed portion of the strut that is not dependent on length.

* Total weight is calculated by adding “fixed” weight and the variable weight (the previous
  property). For example, a snubber with a cylinder, reservoir, a variable length of
  tubing, and two end connections has a fixed weight for the cylinder, reservoir and
  end connections, plus a variable weight for the variable length of tubing.
* Often the weight of the entire Strut/Snubber is included in Strut\_A, with the Strut\_B
  weight set to zero. If several different Strut\_B options can be used with a single
  Strut\_A, then it’s best to separate the weights.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Selection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308495?contentId=7_dI03jA6vKdDC4vW59JQA)
These properties specify for the part selection properties and for report properties
for the Strut\_A. Enter these properties to select the correct part from an Assembly
Information Rule (AIR) and used for Reporting purpose.

IJUAhsStroke::Stroke

Enter the stroke of the snubber. This value is used by the AIR for the part selection
of the snubbers.

IJOAhsExtension::Extension

Enter the extension distance for snubbers due to thermal movement from cold to hot.
This value is used to compare the travel of the snubber against the stroke of the
snubber and is required for ordering.

IJOAhsRetraction::Retraction

Enter the retraction distance for snubbers due to thermal movement from cold to hot.
This value is used to compare the travel of the snubber against the stroke of the
snubber and is required for ordering.

IJUAhsAllowance::Allowance

Enter the excess travel allowance, for example 20%. A warning is displayed if (extension
+ retraction) times (one + allowance) is greater than stroke.

IJOAhsSetPosition::SetPosition

Enter the set position that is used for purchasing. This value is used for reporting.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308496?contentId=25qCJRrQA8qMSmo~5~ioFA)
These properties specify the port properties.


Image:[Image-Analysis: The image presents a table layout comparing two ports, labeled as Port1 and Port2. Each port has associated attributes organized into rows. The attributes include: \n- Name: Identifying the name of the port.\n- PortType: Describing the type of port.\n- Size: Indicating the size of the port.\n- MinSize: Specifying the minimum size requirement.\n- MaxSize: Indicating the maximum size restriction.\n- UnitType: Describing the unit of measurement for the port. \nThe left side in an orange background represents the attributes of Port1, while the right side in a light blue background features the attributes of Port2. This structured comparison allows easy assessment of the differences and similarities between the two ports. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GBchwrOoyDvYwhhfkhro1g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GBchwrOoyDvYwhhfkhro1g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Plain End – Type 1

The plain end does not add any additional graphics. This would be used if the end
of, for example, Shape5 is to be threaded as a rod, or if the end is a stub, to be
welded to some other object.


Image:[Image-Analysis: The image depicts a schematic representation of a network configuration or a circuit. It showcases two ports named "X" and "Z" connected to a central component represented as a box. The left side has an arrow pointing from point "Z" towards the box, indicating a flow or connection towards it. Additionally, there’s a downward arrow from port "X" which suggests another connection that diverges from the main path. The box likely represents a device or system that interacts with the inputs from both "X" and "Z" ports. The text "Port1: 0,0,0" in the top-left corner could imply a configuration or status indicator for Port 1. The overall goal of this image is to illustrate how data or signals move between these entities in the network or circuit layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D0WN7Bc08q1kOfvJ_qcCUQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D0WN7Bc08q1kOfvJ_qcCUQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1000 – ExtThdRH | Enter the diameter of the plain end, for connecting to other components. | Enter the minimum amount that the plain end can penetrate a female threaded hole. (Minimum Thread Length) | Enter the maximum amount the plain end can penetrate a female threaded hole. (Maximum Thread Length) |
| 1002 – ExtThdLH |
| 1200 – Other (for non-threaded stub-ends) | N/A for this port type– Use 0 | N/A for this port type – Use -9999 | N/A for this port type – Use 9999 |

Port 1 - Eye End - Type 2


Image:[Image-Analysis: The image depicts a schematic representation of a system with a defined port, referred to as Port1. The port is indicated with the label "Port1: 1:0.0.0," suggesting it has an identifier related to its function or location. The circular part of the image likely represents a connection point, labeled with directional axes 'X' (downward) and 'Z' (to the side), indicating how signals or data flow might be oriented in this system. The arrow between the port and the rectangular block symbolizes data transfer or connection, showing a one-way direction from the circular port to the block. The rectangular block may represent a component or device that processes inputs from the port before passing them further along the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YC~yWW3ek4gVR~mA~oqJxQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YC~yWW3ek4gVR~mA~oqJxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 – Eye | Enter the "thickness" of the eye, which needs to be compared against the opening in the connecting item, to check if the thickness of the eye fits into the opening.  This value will be equal to Thickness1 (that is, the thickness of that rod end). | Enter the smallest size of pin or bolt that will fit inside the eye, usually zero. | Enter the largest pin or bolt that will fit inside the eye, Needs to be taken from the catalog specs. |

Port 1 - Spade End - Type 3


Image:[Image-Analysis: The image illustrates a diagrammatic representation likely related to an electrical or mechanical system involving ports and connections. It features a circular component at the left, probably indicating a rotational part, and two labeled points: X and Z. The arrow pointing from point X into the component suggests a flow or direction of energy or data. The line connecting point Z to another box suggests these elements are part of a greater system where Z leads to a subsequent stage or phase. The presence of "Port1: 0,0,0" likely denotes a specific configuration or initialization parameter related to this setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uzx3cdKHYdoXGy6AII4~bQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uzx3cdKHYdoXGy6AII4~bQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 – Eye | Enter the "thickness" of the eye, which needs to be compared against the opening in the connecting item, to check if the thickness of the eye fits into the opening.  This value will be equal to Thickness1 (that is, the thickness of that rod end). | The smallest pin or bolt that will fit inside the spade end’s hole, usually zero. | The largest pin or bolt that will fit inside the spade end’s hole, from the catalog specs. |

Port 1 - Bolt End- Type 4

This would rarely be used in a strut as the end of the strut would be a bolt-head.
The rod end codelist includes this option, so it is implemented for the strut as well.
It may be useful to represent some types of threaded connections.


Image:[Image-Analysis: The image depicts a simple circuit connection labeled "Port1: 0.0,0.0". It shows an arrangement with two entities, X and Z, connected through a line. The entity X appears to be a source or input, indicated by the downward arrow, while Z is an intermediary or processing element connected to a line leading to another endpoint, which is likely representing an output or another entity. The arrows signify the direction of flow or connection between these entities in the circuit. The red dots at both ends of the line may represent connection points or terminals. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eonlkETPqINMpXHejVC0jg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eonlkETPqINMpXHejVC0jg-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 – Other | N/A for this port type – Use 0 | N/A for this port type – Use -9999 | N/A for this port type – Use 9999 |

Port 1 - Nut (Female) End- Type 5

If the end of the strut is a female hole, threaded or not, use this type. The port
orientation for this type is opposite to all of the other types, so it coincides with
the orientation of the connected male threaded port.


Image:[Image-Analysis: The image appears to be a diagram representing a system involving ports and connections. It shows a point labeled "Z" from which connections extend, one of which is directed towards a block on the right side of the image. This block likely represents a processing unit or component that interacts with the input from "Z". The arrowed line labeled "X" indicates a feedback or directional flow of information or power originating from "Z". There is also a text note at the top indicating a port designation (Port1:0,0,0), suggesting this is a technical schematic related to network or hardware configurations. The relationship among the components implies a data flow from Z into the processing block, with the possibility of returning or altering the input based on the direction indicated by X. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ODDwc5rjnoEK~oP_THK1sg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ODDwc5rjnoEK~oP_THK1sg-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 – IntThdRH  1003 – IntThdLH | Enter the depth of the threaded hole, for comparison with the thread length of the connected male threaded port. | Enter the minimum diameter of the connected male threaded port. | Enter the maximum diameter of the connected male threaded port. |

Port 2 - Other

The other end of Strut\_A has a port of type Other for connecting to Strut\_B.


Image:[Image-Analysis: The image depicts a diagram illustrating a 3D coordinate system and a component with various ports. There is a central block labeled "Z," which indicates that it is aligned along the Z-axis, along with two other axes represented as X and Y, although the Y-axis is not labeled in this specific view. The "Port2" label suggests that this is the second port of the component. Below Port2, the coordinates are stated as "0,0 Length," indicating that it likely references a position or a length measurement associated with that specific coordinate in the system. The use of arrows indicates the direction along the X and Z axes, suggesting how the component might be positioned or oriented in space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/apCDz8PJqm2TiEV_TxuJgA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/apCDz8PJqm2TiEV_TxuJgA-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this port type.  Use 0 | Not applicable for this port type.  Use -9999 | Not applicable for this port type.  Use 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strut\_B - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308515?contentId=qeQcoC5BNheeUC~dgbePNg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Strut\_B  
Part Name: Strut B  
Part Description: Strut B SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4Z0oC9LBcWFiiRzL2I2Dvw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d6eebf81c06db486)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4Z0oC9LBcWFiiRzL2I2Dvw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Strut\_B SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Struts > Adjustable Rigid Strut - Part B as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical structure of components related to a project or system labeled "SmartParts". At the top level, there is a category named "S3D Standard", and beneath it, there are multiple subcategories including "Beam Attachments", "Clevises", "Miscellaneous", "Pipe Clamps", "Pipe Straps", "Plates", "Rod Fittings", "Rods", and "Struts". Within the "Struts" category, two items named "Adjustable Rigid Strut - Part A" and "Adjustable Rigid Strut - Part B" are listed, where "Part B" is highlighted, indicating it may be selected or of particular interest. The "U-Bolts" is another top-level category that stands separately in the list. This structure suggests that it is part of a design or assembly process, systematically organizing components for easy reference and selection. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RFIV_aWmaNOwxefrcfg5Vg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RFIV_aWmaNOwxefrcfg5Vg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

This symbol is used to represent the second end part of struts and snubbers. The Strut\_B
shapes are divided into the following.

* One graphic shape: Round, Oval, Square, Rectangular, Hexagonal shapes are possible
* One rod end shape: Plain, Eye, One Spade, Two Spades, Bolt, Nut (Female) end shapes
  are possible

Because Strut\_B is defined as the second end part, this separate part allows for a
rotating joint between this end and the strut/snubber body (Strut\_A). Strut\_B has
a fixed length. All variable length adjustment of struts and snubbers is handled with
Strut\_A.

The following figure shows how the strut part is divided into shape and end.


Image:[Image-Analysis: The image shows a diagram comprising different shapes and labels related to a design or engineering context. It features a bullet-like shape, which is labeled as "Shape1," along with an end section denoted as "End1." There is a red dot positioned centrally within this shape, possibly indicating a specific point of interest or reference. The presence of shapes and the labeling suggests that the image is part of a technical illustration or schematic that denotes specific parts or features involved in a mechanical or structural design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GiC0f5hqNpzzhWXJblbOeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GiC0f5hqNpzzhWXJblbOeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Local Coordinate System


Image:[Image-Analysis: The image depicts a diagram with two ports, labeled "Port1" and "Port2." Port1 has coordinates (0, 0, 0) and shows a direction labeled "Z" illustrated by a red arrow pointing right. It also shows another direction labeled "X" with a red arrow pointing downwards. Port2 is indicated to have coordinates (0, 0) with an additional specification of "Length" next to it. This diagram likely represents a schematic in a technical or engineering context, illustrating relationships between different ports and their orientations or positions in a three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0hmF9uAVlohPSvk3R3zayA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0hmF9uAVlohPSvk3R3zayA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308523?contentId=8_ZCVBXJBv_phgzmfNiAtg)
These properties define the location of the ports and weight of the Strut\_B.

IJUAhsLength::Length

Specifies part length, which the distance between Port1 and Port2 regardless of the
end type.


Image:[Image-Analysis: The image depicts a schematic representation of a circuit or mechanical system showing two components labeled "1" and "2." Component "1" appears to be a circular shape with a dotted boundary, possibly indicating a loop or a connection point, while component "2" is represented as a rectangular shape. The arrows between the components suggest a flow or transfer of energy/material from one component to the other. The red dot next to the number "1" might indicate a specific point of reference, activation, or a measurement point in the system. The overall layout suggests an interaction or relationship between the two components where the behavior of one may affect the other. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gICMyinKKZycTmxjNkKkrQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gICMyinKKZycTmxjNkKkrQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWeight::Weight

Specifies the weight for this part of the strut if it has not already been included
in the weight of Strut\_A.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308524?contentId=2bVDLhKzXGnvnDy2NuUVSg)
These properties specify the shape of Strut\_B. In general, the shape properties are
defined as:


Image:[Image-Analysis: The image illustrates a 3D coordinate system along with dimensions labeled for a specific shape. It shows an axis (Z) pointing upwards, an axis (X) pointing left, with a reference to width and length dimensions of the shape. The labeled dimensions, "Shape1Width1" and "Shape1Length," indicate that the width and length of the shape are being measured along these axes. The arrows suggest the direction for measurement, and the image likely pertains to design or engineering, specifying how to define the dimensions of a given shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SV7zUY60COHWD50UBFrPQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SV7zUY60COHWD50UBFrPQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Shape1Width1 is in X direction  
Shape1Width2 is in Y direction (into the page)  
Shape1Length is in Z direction (along length of strut/snubber)

IJUAhsShape1::Shape1Type

Specifies the graphic shape. The center hole shown in figure is only for the reference
and will not be modeled. The value for this column is a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsShapeType sheet.

1 - Round


look for icon that looks like a circular loading or spinning indicator: 

2 - Square


look for an icon that looks like a loading circle or spinner: 

3 - Hex


icon of a hexagon with a circular shape inside it, resembling a chemical structure or molecule representation: 

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the shape.

1 - Round


Image:[Image-Analysis: The image depicts a vertical line with arrows at both ends and a circular shape nearby. The vertical line represents a measurement or an object with height or depth, while the circle suggests it is measuring or indicating something related to the circular shape, possibly its diameter or radius. The image illustrates a relationship between the vertical measurement and the circular object, possibly in a geometrical or architectural context, showing how height relates to circular dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZRreIyn75y~tHR6xZjZxlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZRreIyn75y~tHR6xZjZxlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image consists of two distinct symbols. The left symbol depicts arrows pointing upwards and downwards, which commonly represent the concept of "vertical movement" or "height adjustment." This could signify an action such as raising or lowering an object. The right symbol is a square with a circle inside it, along with a dotted line that surrounds the circle. This symbol typically represents "a button" or a "selected option," indicating a choice that can be made or an action that can be activated. Together, these symbols might be used in a user interface to indicate adjustable settings related to height (left) and a selection or activation action (right). 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oI0GRIGGxHUOGXiBdAYqAw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oI0GRIGGxHUOGXiBdAYqAw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image depicts a hexagon with arrows on either side indicating a measurement or comparison of width. The hexagon is outlined and has a dashed circle in the center, which may suggest that it is a representational figure for a hollow shape or a space within the hexagon. The arrows imply that there is a dimension being referenced, likely measuring the distance between the two points indicated by the arrows. This could relate to geometrical calculations, manufacturing specifications, or design guidelines involving hexagonal shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Sg8NSqXiVE0SmBGuNzHzqQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Sg8NSqXiVE0SmBGuNzHzqQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the outside length of the shape. If this value is set to zero or a negative
value, then Shape1Width1 is used. This value is not used for the hex shape.

1 - Round


Image:[Image-Analysis: The image depicts a cylindrical object, shown from the side with open circular ends. The object is represented horizontally with arrows on either side indicating width, suggesting a focus on the cylindrical dimensions. The small circle inside the cylinder likely represents a cross-section view of the cylinder's inside space. This visual could represent concepts in geometry, physics, or engineering, particularly regarding volume, capacity, or structural properties of cylindrical shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIZKYqYtPD69HrSW0Lv4JQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIZKYqYtPD69HrSW0Lv4JQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a simple layout that involves a rectangular box on the top and a horizontal line with arrows pointing to both ends at the bottom. The top rectangle contains a small circle in the center, which suggests it could represent a container or a button with possibly interactive functionality. The horizontal line with arrows indicates movement or adjustment, possibly implying that the box can be resized or moved horizontally. Overall, this could represent an adjustable user interface element or a dynamic component in a graphical application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mekLIORzDLy0bOFAjSe4fg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mekLIORzDLy0bOFAjSe4fg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the length of the shape.


Image:[Image-Analysis: The image depicts a circuit diagram showing the flow of electric current. It illustrates a source indicated by the circular shape on the left, where the current exits from point X, moves toward point Z through the red arrows denoting direction, and continues to a component represented by the vertical lines on the right, which likely symbolizes a resistor or some other circuit element. The arrows imply the direction of current flow, which goes from the source toward the load. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Go3FrClA2iVNZhLZY9kudg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Go3FrClA2iVNZhLZY9kudg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rod End Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308525?contentId=RjO5~U6CnSWsjHs7bNZNRw)
These properties specify the end shape for Strut\_B.

IJUAhsRodEnd1::RodEnd1Type

Specifies the graphic shape to be used at Rod End. The value for this column is a codelist number and valid codes are listed in the
HS\_S3DParts\_Codelist.xls workbook on the hsRodEndType sheet. Enter the codelist short name for readability in XLS file. The nut (female)
uses the same graphic shape as the bolt, but the port orientation is reversed. The
port location (red dot) is at z=Length.

1 – Plain (Default, no additional graphics)


look for icon that looks like a rectangular box with red dots on the sides and a circle on the right: 

2 – Eye


Image:[Image-Analysis: The image depicts two distinct mechanical components. On the left, there is a circular element attached to a rectangular bar, which may represent a crank mechanism where the circle is a wheel or gear that rotates. The red square within the circular element suggests a key or a part that aids in the transmission of motion. To the right, there appears to be a rectangular outline, which may represent a housing or casing for the circular component, likely showing how the components fit together within a mechanical assembly. The relationship between the left and right parts indicates that the circular element interacts with the rectangular housing, possibly as part of a larger machine or device. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpwJXnWbOC4xbnsvsvXcXQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpwJXnWbOC4xbnsvsvXcXQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image depicts a simple schematic of a circuit connection. On the left side, there is a red point indicating a positive terminal, likely representing a power source or battery. The arrow structure suggests a connection point that leads to a round element, which could be a component such as a light bulb or resistor. The right side of the image shows what appears to be a battery or power connector that completes the circuit. The overall layout illustrates how electrical connections are made between these components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MhWI4GOW0cXZO8zRAc7PEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MhWI4GOW0cXZO8zRAc7PEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image shows two mechanical components: a shaft and a bearing. On the left, there is a depiction of a shaft, represented by a long horizontal rectangle with two red dots indicating the attachment points or supports. The right side shows a circular bearing, which typically allows the shaft to rotate smoothly within it. The relationship between these two components is that the shaft is designed to rotate, often supported by bearings, which help reduce friction and wear. The placement of the red dots suggests where the shaft would connect to other parts, possibly indicating the location of bearings or other fixtures that hold the shaft in place. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zI2wn~ijXRiDHa~gxNTeHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zI2wn~ijXRiDHa~gxNTeHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image shows two different mechanical components. On the left, there is a rectangular block with two red dots indicating the ends of a linear shaft, suggesting that it may be a guide or a stop for linear motion. This is often used in mechanical assemblies to limit the movement of another component that slides or moves alongside it. On the right, there is a circular component with a dotted line, which may represent a bearing or a pulley. Bearings are used to reduce friction and allow rotational motion, while pulleys are used for lifting or changing the direction of force. These components could be part of a larger mechanical system, such as a conveyor belt or other machinery that involves movement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RrS5CX_8vofbFbgKVCLFjA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RrS5CX_8vofbFbgKVCLFjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

JUAhsThickness1::Thickness1

Specifies the thickness of the rod end. This value can be negative for Type 4 - Bolt
and Type 5 - Nut.

1 – Plain (no effect on graphics)


look for icon that looks like a rectangular box with red dots on the sides and a circle on the right: 

2 – Eye


Image:[Image-Analysis: The image depicts two different types of electrical components. On the left, there is a representation of a capacitor with a circular shape, indicating one of the terminals (usually marked with a red dot) connected to a flat, rectangular terminal. Capacitors are devices that store electrical energy temporarily. On the right side, there is a visual of two parallel plates with arrows suggesting an electric field direction between them, which further illustrates the concept of a capacitor's function, where these plates hold opposite electrical charges. The arrangement symbolizes the basic principle of a capacitor, where an electric field is created by the separation of charges on these plates. This dual depiction emphasizes both the structure and the fundamental working principle of capacitors in electronic circuits. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VDcI~xxAVuI9tHBsmcc4bw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VDcI~xxAVuI9tHBsmcc4bw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image displays two electrical components related to circuit design. On the left side, there is a symbol for a connector or terminal block, often used to create a junction point for electrical connections. It features a circular feature that likely represents a screw or a wire entry point, colored in red, which indicates a positive terminal or connection. The right side shows a symbol of a switch, which can control the flow of electricity in a circuit. The switch is presented in an open position, suggesting that the circuit is currently incomplete, thus not allowing current to flow. These components are typically part of electrical schematic diagrams used to illustrate circuit designs, with the connector allowing connections to other circuit elements and the switch enabling or disabling the circuit flow. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOY75MHuIeQqCggew5utsw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOY75MHuIeQqCggew5utsw-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image shows a simple circuit diagram featuring two main components: a power source (represented by a rectangle with a line connecting it) and a control device (depicted as a rectangular box). Arrows indicate the flow of electricity within the circuit. The red dots may represent terminals or connection points in the circuit. The arrows signify the direction in which current flows, indicating a source connected to a load. This image illustrates fundamental concepts in electrical engineering, specifically how power is distributed in a circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image shows a simple circuit diagram featuring two main components: a power source (represented by a rectangle with a line connecting it) and a control device (depicted as a rectangular box). Arrows indicate the flow of electricity within the circuit. The red dots may represent terminals or connection points in the circuit. The arrows signify the direction in which current flows, indicating a source connected to a load. This image illustrates fundamental concepts in electrical engineering, specifically how power is distributed in a circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nxQGDSP6AWpsjDhaRauDqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length from the base of the spade to the port location, which is also
the start of the curved end. Only zero or positive values are allowed. This property
is valid for spade end type only.


Image:[Image-Analysis: The image depicts a diagram illustrating the concept of a magnetic switch mechanism. It shows a rectangular box, likely representing the switch, with a small circle indicating a magnetic area on one side. There are arrows pointing towards and away from the box, suggesting movement or activation, and a line connecting the box to a dotted circle, possibly symbolizing connectivity or a circuit relationship. This diagram may represent how a magnetic field can activate or deactivate the switch, illustrating its function in an electronic or mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tXG7etG~3QePnR_FirPGIA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tXG7etG~3QePnR_FirPGIA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the outside diameter of the rod ends.

1 – Plain (no effect on graphics)


look for icon that looks like a rectangular box with red dots on the sides and a circle on the right: 

2 – Eye


Image:[Image-Analysis: The image depicts a schematic of a simple mechanical system. It shows a cylindrical object (possibly a pulley or a wheel) connected to a rectangular shape that may represent a lever or bar. The circle in the center is likely indicating a pivotal point or axle upon which the cylinder rotates. The red square inside the circle suggests a specific point of interest, such as a contact point or load. The vertical arrows on the right indicate a force or measurement of distance, signifying that the system might be meant to illustrate principles of mechanics, such as motion, leverage, or force distribution in a lever system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PkirdDBSg2l~APF3iRhqDA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PkirdDBSg2l~APF3iRhqDA-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 – Spade


Image:[Image-Analysis: The image depicts a mechanized component, likely a solenoid or electromagnet assembly. It features a coil (noted by the circular shape) with a central plunger. The drawing indicates a cross-section view of the component, showcasing the plunger's position (marked in red) within the coil. The vertical arrows represent the possible movement direction of the plunger, which can be pushed in or pulled out when energized. A small red dot is also included, possibly indicating an electrical connection or operational note. The overall diagram serves as a schematic for understanding how the solenoid operates in relation to its electrical components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TvNtvDW0wc0swf8wRM8Cww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TvNtvDW0wc0swf8wRM8Cww-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 – Bolt


Image:[Image-Analysis: The image depicts a mechanical system consisting of two parts connected by a horizontal line, which likely represents a rod or a shaft. On the left, there is a red dot that may indicate a pivot or a point of rotation, while on the right, there is a rectangular box with two triangular shapes pointing downward, suggesting a connection point for another component. The presence of dimensions indicated by lines suggests that this image might be part of a technical drawing or a schematic representation of a mechanical assembly or linkage. The red dots further emphasize specific points of interest in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 – Nut (Female)


Image:[Image-Analysis: The image depicts a mechanical system consisting of two parts connected by a horizontal line, which likely represents a rod or a shaft. On the left, there is a red dot that may indicate a pivot or a point of rotation, while on the right, there is a rectangular box with two triangular shapes pointing downward, suggesting a connection point for another component. The presence of dimensions indicated by lines suggests that this image might be part of a technical drawing or a schematic representation of a mechanical assembly or linkage. The red dots further emphasize specific points of interest in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ttjdsq8IC7aJ7NDfUbh3nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies a double-spade end or a single-spade end. If this value is zero, then a
single-spade is drawn. If this value is a positive number, then a double-spade is
drawn with two identical spades separated by the gap value defined here.


Image:[Image-Analysis: The image depicts an electrical circuit diagram with two key components. On the left, there is a capacitor represented as a cylindrical shape, indicated by the curved line. The red dots likely signify the positive and negative terminals. Capacitors are used to store electrical energy temporarily. On the right side, there are parallel lines symbolizing a battery connection, another critical component in electrical circuits that provides a continuous voltage supply to power various electronic devices. The arrow between the two sides signifies the flow of electricity from the battery to the capacitor, illustrating a simple circuit setup where energy can be transferred and stored. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ltl85UL0Pvj~G3ysAVAYIQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ltl85UL0Pvj~G3ysAVAYIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308526?contentId=3pgpTBNKJQx7TqqMJ7oKXw)
These properties define the ports.


Image:[Image-Analysis: The image displays a tabular format comparing two ports, referred to as Port1 and Port2. Each port has multiple attributes that are arranged in a structured manner. The attributes for each port include: "Name", "PortType", "Size", "MinSize", and "MaxSize". The table consists of two columns, with Port1 represented in light blue and Port2 in light orange. Each row within the columns pertains to the corresponding attributes for each port, allowing for an easy comparison between the two ports under each relevant category. This organization helps in understanding the similarities and differences between the specified ports based on the listed attributes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i9gX4TUrBv3doAxGDCIBfg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i9gX4TUrBv3doAxGDCIBfg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Plain End – Type 1

The plain end does not add any additional graphics. You use this end if, for example,
Shape5 is threaded as a rod, is a stub, or is to be welded to some other object.


Image:[Image-Analysis: The image shows a diagram related to a port system, with specific coordinates indicated as Port1: 0,0,0. It depicts a three-dimensional coordinate system with designated axes. The 'X' axis is represented vertically downward with an arrow pointing downwards, while the 'Z' axis is presented horizontally, moving to the right with an arrow pointing in that direction. The origin point at the intersection of the axes can be inferred as where the coordinates start. The diagram likely represents a spatial representation used in technical fields like engineering or computer graphics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i~jBuE86xhnSau~Gmezm8w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i~jBuE86xhnSau~Gmezm8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1000 – ExtThdRH | Enter the diameter of the plain end, for connecting to other components. | Enter the minimum amount that the plain end can penetrate a female threaded hole. (Minimum Thread Length) | Enter the maximum amount the plain end can penetrate a female threaded hole. (Maximum Thread Length) |
| 1002 – ExtThdLH |
| 1200 – Other (for non-threaded stub-ends) | Not applicable for this port type.  Use 0 | Not applicable for this port type.  Use -9999 | Not applicable for this port type.  Use 9999 |

Port 1 - Eye End - Type 2


Image:[Image-Analysis: The image depicts a diagram that represents a port configuration with a focus on three axes: X, Y, and Z. The central red dot signifies the origin or the center of a spherical coordinate system, while the surrounding circular outline indicates the boundary for some form of measurement or analysis. The axes are labeled accordingly, with the Z-axis extending to the right and the X-axis extending downward. The notation "Port1:0,0,0" suggests that this is a coordinate reference, indicating the position of the point in a three-dimensional space, where Port1 might represent the first port or interface in a certain context. The orientation and positioning of the axes and port are crucial for understanding spatial relations in this scenario. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RygfiT7goTLZSaSCZyN89w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RygfiT7goTLZSaSCZyN89w-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 – Eye | Enter the "thickness" of the eye, which needs to be compared against the opening in the connecting item, to check if the thickness of the eye fits into the opening.  This value will be equal to Thickness1 (that is, the thickness of that rod end). | Enter the smallest size of pin or bolt that will fit inside the eye, usually zero. | Enter the largest pin or bolt that will fit inside the eye, Needs to be taken from the catalog specs. |

Port 1 - Spade End - Type 3


Image:[Image-Analysis: The image represents a diagram commonly used in engineering or physics to illustrate the orientation of axes in a three-dimensional space. It shows a curved shape with three orientation arrows indicating the X, Y, and Z axes. The arrow pointing left is labeled "X", the vertical arrow pointing upwards represents the "Z" axis, and there is reference to "Port1: 0,0,0", suggesting that the coordinates for Port1 are at the origin (0,0,0) of the system. The small red dot at the intersection of the X and Z axes likely signifies a specific point of interest or origin within this spatial representation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/706tEvQCg2HA~BXVL5zicg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/706tEvQCg2HA~BXVL5zicg-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 – Eye | Enter the "thickness" of the eye, which needs to be compared against the opening in the connecting item, to check if the thickness of the eye fits into the opening.  This value will be equal to Thickness1 (that is, the thickness of that rod end). | The smallest pin or bolt that will fit inside the spade end’s hole, usually zero. | The largest pin or bolt that will fit inside the spade end’s hole, from the catalog specs. |

Port 1 - Bolt End- Type 4

This end type is rarely used in a strut as the strut end would be a bolt-head. The
rod end codelist includes this option so it is implemented for the strut as well and
may be useful to represent some types of threaded connections.


Image:[Image-Analysis: The image depicts a schematic representation illustrating a 3D coordinate system associated with a port labeled "Port1: 0,0,0". In this diagram, three axes are represented: X, Y, and Z. The X-axis is oriented vertically downward, while the Z-axis extends horizontally. There is a block or a container structure at the left side indicative of a 3D space, and an arrow pointing along the Z-axis represents a direction or flow. The coordinates (0,0,0) suggest the origin point in this 3D system is at the intersection of these axes. This kind of schematic is often used in fields such as engineering and computer graphics to define the spatial orientation of objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nWN_MxQ4m9pScvQuabExRA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nWN_MxQ4m9pScvQuabExRA-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this port type.  Use 0 | Not applicable for this port type.  Use -9999 | Not applicable for this port type.  Use 9999 |

Port 1 - Nut (Female) End- Type 5

If the end of the strut is a female port, threaded or not, use this type. The port
orientation for this type is opposite to all of the other types, so it coincides with
the orientation of the connected male threaded port.


Image:[Image-Analysis: The image depicts a three-dimensional coordinate system with axes labeled X, Y, and Z. The X and Z axes are shown in a two-dimensional plane, while the Y axis is depicted as being vertical. There is a rectangular shape that seems to represent a port labeled "Port1: 0,0,0," indicating a possible reference with coordinates (0,0,0) relative to this coordinate system. The red dot on the intersection of the X and Z axes likely signifies a specific point of interest within this coordinate framework. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4T4eZ1~~JX_QJ2l07zweeg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4T4eZ1~~JX_QJ2l07zweeg-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001 – IntThdRH  1003 – IntThdLH | Enter the depth of the threaded hole, for comparison with the thread length of the connected male threaded port. | Enter the minimum diameter of the connected male threaded port. | Enter the maximum diameter of the connected male threaded port. |

Port 2 - Other

The other end of Strut\_B has a port type of Other for connecting to Strut\_A. The orientation of the Z-axis of this port is opposite
to the connecting port on Strut\_A. In assemblies, these ports are connected to each
other with a revolute joint, allowing rotation around the Z-axes (twisting).


Image:[Image-Analysis: The image depicts a three-dimensional coordinate system with labels indicating the X, Y, and Z axes. There is a rectangular shape drawn in the Z direction, representing an object or section of an object. The Z axis is shown pointing upwards, while the X axis is pointing to the right and is labeled with "0,0, Length," suggesting it is at an origin point extending in the length direction. The text "Port2:" is indicating that this diagram may be referencing a specific connection or entry point related to the object represented in the diagram. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lu8~l0lAX3l47fUCiXJ9bA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lu8~l0lAX3l47fUCiXJ9bA-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this port type.  Use 0 | Not applicable for this port type.  Use -9999 | Not applicable for this port type.  Use 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Swivel Ring - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307820?contentId=o_KSvdtVQS7mw0wbGl4LYw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.SwivelRing  
Part Name: Swivel Ring  
Part Description: Swivel Ring SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ALmLaoA5M8kLKl1pDAe5QQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3cf914164831baec)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ALmLaoA5M8kLKl1pDAe5QQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in

[Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in

[Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample swivel ring SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon-description: look for an icon that resembles a camera with a plus sign, indicating the option to add or upload a photo.: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Pipe Clamps>Adjustable Swivel Ring as shown below.

   
Image:[Image-Analysis: The image displays a hierarchical structure, likely representing a categorized list of components or parts related to "SmartParts". At the top level, "SmartParts" is the main category. Under this, there are multiple subcategories such as "S3D Standard", "Beam Attachments", "Clevises", "Miscellaneous", and "Pipe Clamps". The "Pipe Clamps" has further subdivisions: it includes entries like "Pipe Clamp - Medium 2-Bolt", "Riser Clamp", "Split Pipe Ring", and importantly highlights "Adjustable Swivel Ring". This hierarchical structure helps in organizing parts for easy identification and access. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q7YoxJna~AKhfZ1cM8fVLg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q7YoxJna~AKhfZ1cM8fVLg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image displays two separate diagrams illustrating different components or configurations, likely related to mechanics or machinery. On the left side, there is a depiction of a rod end connected to a component labeled “Route” with arrows indicating axes marked as X, Y, and Z, which suggest the orientation and movement capabilities of the rod mechanism. The right side shows a different view of the same or a similar object, maintaining the X, Y, Z axis markings, but presented in a vertical orientation. This implies a relationship where both views can represent the same object from different perspectives, aiding in understanding the mechanics or functionality associated with the rod and the route. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h7OiIyKvc2B~PtdhoxQE0g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h7OiIyKvc2B~PtdhoxQE0g-_PVFQNoCl4XmjAxWO0f7XQ/content)

The part origin is at the pipe centerline where the Route port is located.

With this coordinate system, the swivel ring shows up in the most-frequently-used
orientation when using the AddPart command.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Swivel Ring Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307826?contentId=TNATLIOhixhoe6cDo7S9VA)
IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of the rod that attaches to the swivel ring. The rod
does not display as part of the swivel ring and does not affect the graphics. The
rod diameter value is mandatory. If the value is set to zero, a warning displays.


Image:[Image-Analysis: The image depicts a technical illustration related to measuring or displaying the diameter of a rod. The diagram includes a vertical rod structure with measurement indicators on both sides, suggesting that it is showing how to determine or visualize the rod's diameter. The label "RodDiameter" at the top indicates the subject of the diagram - that is, the diameter measurement of the rod. The circular representation at the bottom signifies the end view of the rod, where a red dot at the center might represent the geometric center or a point of measurement. This illustration is likely used in engineering or mechanics to convey information about the size and properties of the rod. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aTbTNkrV69INmNzTYM81pQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aTbTNkrV69INmNzTYM81pQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance from the pipe centerline to the bottom of the rod. This value
specifies the location of the rod end port. This value must be greater than Height1 + (2 X Thickness1).


Image:[Image-Analysis: The image depicts a conceptual diagram related to the process of removing a rod from a container. The container has a cylindrical shape with a rounded bottom and is partially filled with a gray substance. At the top, a mechanism (represented by a small circle and a line) is used to facilitate the removal of the rod, which is likely inserted into the gray substance. The upward and downward arrows suggest that the rod can move vertically within the container. The text "RodTakeOut" indicates that the focus of this image is on the process of extracting the rod effectively. This may pertain to scientific or industrial applications where such a mechanism is necessary for operations involving materials in containers. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cJ2eHdzo7Stxzytm~WiP5w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cJ2eHdzo7Stxzytm~WiP5w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPipeOD::PipeOD

Specifies the outside diameter of the pipe. This value must be greater than zero.
It determines the inside diameter of the clamp unless Diameter1 greater than PipeOD.

The band curve does not necessarily stop at the pipe centerline. This curve wraps
around the pipe until a tangent line can be drawn from the edge of the pipe to the
lower face of the top on that side.


Image:[Image-Analysis: The image depicts a technical illustration of a component, likely pertaining to engineering or plumbing. It shows a pipe with a specific term labeled "PipeOD," referring to the outer diameter of the pipe. The image features a funnel-shaped container that may suggest an application where liquid or gas is to be funneled through the pipe. There’s also a circular solid object within the funnel likely representing a valve or a ball and the red dot on this object could indicate its position or some point of interest. Overall, the image captures elements essential for understanding the functioning or measurements related to piping systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/t7glB6Zc7KmTeWI~CZIIfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/t7glB6Zc7KmTeWI~CZIIfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Band Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307835?contentId=dRy6refYn68L9y6Lyu99Pw)
These properties define the band portion of the swivel ring. Some of these properties
are optional. If they are left blank or set to zero, the part creates the dimension
(or ignores the dimension) based on the rule provided.

IJUAhsWidth1::Width1

Specifies the first width for the swivel ring.

* Standard Type - Enter the distance from the rod centerline to the edge of the lower top flange.


Image:[Image-Analysis: The image depicts a diagram of a narrow container, commonly referred to as a "thistle funnel" which is often used in laboratory settings for transferring liquids. It has a notable highlighted area where the word "Width1" indicates a specific measurement of the funnel’s width. The funnel has a rounded bottom containing a gray shaded sphere which likely represents a liquid or another substance within the funnel. The small arrows pointing inward from the sides suggest the measurement of the narrow part of the funnel, emphasizing its constricted dimensions which could be significant for liquid flow or Chemistry experiments. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1EvtFCFXT8PtA0A_Diz02g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1EvtFCFXT8PtA0A_Diz02g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* J Hanger Type - If Gap1 is greater than 0, then the hanger is a J Hanger. Enter the distance from the rod centerline to the
  edge of the top on the bolt side.


Image:[Image-Analysis: The image depicts a cross-sectional view of a conical or cylindrical container, likely used for scientific or engineering purposes. The container has a circular bottom where a sphere is placed, indicated by the gray shading. The container's width at the top is labeled as "Width1". A line extending from the top side of the container indicates the measurement of this width. There seems to be a measurement point indicated with a red dot, which may signify a particular level or reference line for measurements within the container. This layout suggests a focus on dimensional measurement, likely relevant in contexts like fluid dynamics or material containment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CAdDbPGW8Z8wzjKN1HzW9w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CAdDbPGW8Z8wzjKN1HzW9w-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Adjustable Ring Type - If Width1 < 0.5 X RodDiameter and Width2 < 0.5 X RodDiameter, then the hanger is the adjustable ring type. There is no top flange. Width1 is not used. The bands have the space equal to the RodDiameter between them at the base of the top rod connection. By default, Width1 value is 1.5 X RodDiameter.


Image:[Image-Analysis: The image depicts a simple pulley system, consisting of a fixed overhead support from which a box (usually referred to as a block) is suspended. The block is connected via a rope or cable to a circular weight (illustrating a mass). The arrangement suggests that the weight is being lifted or supported by the box, which likely indicates a scenario related to mechanics, physics, or engineering principles. The red dots may represent points of interest or specific forces acting on the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GLvPoMiSCzae_P3dbCcKIg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GLvPoMiSCzae_P3dbCcKIg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the second width for the swivel ring.

* Standard Type - Enter the distance from the rod centerline to the edge of the upper top flange.


Image:[Image-Analysis: The image depicts a laboratory flask with a narrow neck and a wider body, which is commonly used in various scientific experiments. At the top of the flask, there is a label indicating "Width2," suggesting a measurement or dimension related to the neck of the flask. The flask contains a shaded area, likely representing a liquid inside, and there are also two marked points (one red dot and one potentially indicating the center of the flask). This visual aids in understanding the shape and dimensions of the flask, which may have specific relevance in experiments requiring precise volume measurements or heating of substances. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zVwXteloEOOU3vMbuk~e_A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zVwXteloEOOU3vMbuk~e_A-_PVFQNoCl4XmjAxWO0f7XQ/content)

* J Hanger Type - If Gap1 is greater than 0, then the hanger is a J Hanger. Enter the distance from the rod centerline to the
  edge of the top which is not on the bolt side.


Image:[Image-Analysis: The image depicts a cross-sectional view of a container (possibly a funnel or a vessel) containing a sphere at its base. The container has a specific width labeled as "Width2." There is a red point marked within the container, indicating a focal or measurement point. The container's design allows for holding a spherical object at the bottom, likely relevant to fluid dynamics or material science discussions, emphasizing spatial relationships and dimensions. The presence of the width measurement suggests technical specifications important for the application of the container. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6_3pZ3~UyKKrlKJxVz73lA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6_3pZ3~UyKKrlKJxVz73lA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Adjustable Ring Type - If Width1 < 0.5 X RodDiameter and Width2 < 0.5 X RodDiameter, then the hanger is the adjustable ring type. There is no top flange. Width2 is not used. By default, the Width2 value is is 1.5 X RodDiameter.

IJUAhsWidth3::Width3

Specifies the width of the band or ring. This value must be greater than zero. By
default, Width3 is 2 X RodDiameter.


Image:[Image-Analysis: The image displays two diagrams that illustrate different shapes or profiles. On the left, there is a side view of a shape with a round base and a tapering outline, indicating a conical or funnel-like structure with annotations for measurements. The right diagram shows a rectangular shape with rounded edges, which has a flat surface on top. This diagram includes a dimension labeled "Width3," suggesting a specific width measurement for this rectangular object. The two shapes may represent different designs or components, possibly for engineering or manufacturing purposes, with their respective dimensional specifications noted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lgdMU3v5zoHuyVYtwmW9vA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lgdMU3v5zoHuyVYtwmW9vA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the band or ring. This value must be greater than zero.
By default, Thickness1 is 0.5 X RodDiameter.


Image:[Image-Analysis: The image depicts a scientific apparatus resembling a flask, specifically designed to demonstrate a concept related to thickness. The flask has a rounded bottom and a narrow neck. An arrow labeled “Thickness1” points toward the thickened area at the bottom of the flask, indicating that this is the section where the thickness is being measured or noted. There is a small red dot marking a reference point and a line at the top suggesting the container has some management of airflow or liquid filling, possibly for experimental purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DT74w1fredRlHj4900aQiQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DT74w1fredRlHj4900aQiQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the distance from the pipe centerline to the bottom face of the lower flange.
This value must be greater than 0.5 X PipeOD. By default, Height1 is PipeOD.


Image:[Image-Analysis: The image depicts a basic diagram of a container (likely a graduated cylinder or a similar vessel) with a liquid inside. The container is represented in a cross-sectional view, showing the liquid as a shaded area (gray) occupying the bottom part of the cylinder. There are two indicators, labeled "Height1," which measures the distance from the bottom of the container to a reference point at the top. This height measurement is important in various scientific contexts, such as calculating the volume of liquid or understanding fluid pressure within the container. Additionally, there appears to be a small cap or opening at the top of the container, indicated by the spiral line, possibly suggesting a mechanism for pouring or venting. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zVP~4iqNtitvKLNIP034tg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zVP~4iqNtitvKLNIP034tg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the inside diameter of the band if it differs from the PipeOD. If Diameter1 £ PipeOD, then use PipeOD as the inside diameter of the band or ring. In this case, the curve of the band is
always 180 degrees.


Image:[Image-Analysis: The image illustrates a technical drawing of a mechanical part, likely a pulley or similar component. It shows the part in a side view, with a focus on its shape and dimensions. The overall structure has a tapered design at the top, where a hole is indicated for mounting or attachment. Below, there's a circular section marked as "Diameter1", which refers to the diameter of the circular part seen at the bottom of the drawing. Additionally, there are small red dots that might indicate reference points or measurements. This type of drawing is commonly used in engineering and manufacturing to convey design specifications clearly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_5jOt0Gs9GPtqNnAnksfIA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_5jOt0Gs9GPtqNnAnksfIA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies the distance between the two bolt ears for the J Hanger type. If Gap1 £ 0, then this is not a J Hanger so do not use Gap1.


Image:[Image-Analysis: The image depicts a laboratory setup likely involving a flask and a sphere inside it. The flask appears to be conical, with a narrow opening at the top where some apparatus or a stopper can be seen. Inside the flask, there is a sphere, which is shaded gray, indicating it is likely solid or filled with a material. The image also labels a measurement called "Gap1," which suggests that it is referencing the space between the sphere and either the flask wall or another component within the setup. This suggests that the image might be illustrating a scientific principle, experiment, or an observation concerning the interactions between the sphere and the flask in terms of distance or speed. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j~ThBGr_Zcwdenv9bTOKbw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j~ThBGr_Zcwdenv9bTOKbw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Enter the distance from the inside edge of the band to the outer edge of the upper
bolt ear for the J Hanger type. If Gap1 is zero, then this is not a J Hanger so do not use Width4. If Gap1 < 0, then Width4 > Pin1Diameter + Thickness1. Otherwise, the software sets the default to 3 X (Pin1Diameter + Thickness1).

* J Hanger type - top ear - The ears are drawn perpendicular from the band. The top portion of the band is
  drawn at the same angle so that a continuous band is drawn such that it meets up with
  the pipe at the correct position. The bottom ear is always 1.5 X Width4.


Image:[Image-Analysis: The image depicts a schematic representation of a measuring device or apparatus that appears to be used for gauging dimensions, possibly of spherical objects. The main features include a thin vertical structural part terminating in a round object at the bottom, which is likely the sphere being measured. Above this sphere, there is an adjustable arm or measuring tool with a clearly marked position indicated as "Width4." This likely suggests a specific measurement or setting related to the width of the object. The use of red dots may indicate measurement points or reference markers, which are essential for accurate reading during measurement. Overall, the image portrays a technical setup for measuring a spherical item's width or size using a calibrated measuring device. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tZi~aZxThFIGkNjUXFdSNA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tZi~aZxThFIGkNjUXFdSNA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* J Hanger type - bottom ear - The ears are drawn perpendicular from the band. The band needs to wrap around,
  and possibly extend away from, the pipe in order to make the correct gap. Both the
  ears are parallel.


Image:[Image-Analysis: The image depicts a technical drawing of a conical vessel with a circular object (likely a ball) at the bottom. The vessel has a side view that shows its shape and interior. The highlighted part labeled "Width4" indicates a dimension, likely referring to the width of the opening or section of the vessel. A small red dot is present at the top and bottom, potentially indicating measurement points or reference markers. The drawing seems to serve an engineering or scientific purpose, detailing geometrical relationships and measurements pertaining to the vessel and its contents. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lKrHQ4DdJIRG_hiPfTT6gw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lKrHQ4DdJIRG_hiPfTT6gw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Connection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307913?contentId=3Rnl0fgPCZxLfJidrGxa4g)
Enter the values for these properties for the part to contain a top rod connection.
These properties are optional for the standard and J Hanger types but they are required
for the Ring Hanger type. The rod connection is always cylindrical and is centered
about the rod centerline.

IJUAhsHeight2::Height2

Specifies the height of the top rod connection.

* Standard and J Hanger Type - This property is optional for standard or J Hanger types and is the distance from
  the top surface of the band flange to the top of the rod connection.


Image:[Image-Analysis: The image depicts a geometrical shape that appears to represent a container, possibly a flask or a vessel. The container has a circular base and a tapered neck leading up to a threaded opening at the top. Inside the container, there is a representation of a substance denoted by a shaded area, which suggests that the container is partially filled. The height of the substance or the container is indicated with an arrow labeled "Height2." There is also a red dot inside the container, possibly to signify a specific measurement point or to highlight the level of the substance within the flask. The overall structure and labeling are commonly used in scientific illustrations to convey information about liquids and their measurements. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yGtiJPMvSM6XTHn_O6DszA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yGtiJPMvSM6XTHn_O6DszA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Adjustable Ring Type - Specifies the height from RodTakeOut to the top of the rod connection. By default, this value is 2 X RodDiameter.


Image:[Image-Analysis: The image depicts a simple pulley system. At the top, there is a rectangular block labeled as "Height2," which likely represents a weight or an object being lifted. Below it, a circular object (possibly a ball or pulley) is shown hanging from two slings that connect to the block above. The situation suggests that physical concepts such as weight, gravity, and possibly height or displacement are being illustrated, with "Height2" indicating a specific vertical measurement in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Msdtl7WDGU5TFSWQCWxX2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Msdtl7WDGU5TFSWQCWxX2w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter2::Diameter2

Specifies the diameter of the top rod connection.

* Standard and J Hanger Type - This property is optional for standard or J Hanger type. Enter a value greater
  than RodDiameter


Image:[Image-Analysis: The image depicts a scientific or technical diagram illustrating a container, likely a flask or a similar vessel, with a conical lower section and a cylindrical neck at the top. It is labeled with "Diameter2" which suggests that it refers to a specific measurement at the neck of the container. The diagram also includes labeled points marked '1' and '2', indicating points of interest or reference on the container, which may relate to calculations or dimensions relevant to its design or usage. The overall design emphasizes the importance of understanding the dimensions of the container, especially at different points (the neck and the body) for practical applications such as volume calculations in laboratory settings. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l4OyNGVaf3KC7iGVatuvHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l4OyNGVaf3KC7iGVatuvHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Adjustable Ring Type - Specifies a value greater than RodDiameter. By default, Diameter2 is 1.25 X RodDiameter.


Image:[Image-Analysis: The image illustrates a pulley system showing the dimensions involved, particularly the diameter of the pulley labeled "Diameter2". The conveyor belt or rope is represented passing around a round pulley which is shaded in gray. The diagram includes directional arrows indicating tension or movement, while a red point at the center of the pulley may denote the pivot or center point. This setup is typical in mechanical engineering, where understanding the diameter of pulleys is important for calculating movements, forces, and tensions in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lGVbuWiM2FNRYBLzdv4d4A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lGVbuWiM2FNRYBLzdv4d4A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Wrap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307925?contentId=42KBBWutKs0BtN4qlOC~Uw)
Enter value for this property to include wrap on the band or ring. The wrap is always
centered on the band. The thickness specified is applied to each side of the band.

IJUAhsThickness2::Thickness2 (Optional)

Specifies the thickness of the wrap from the outside of the band to the outside of
the wrap. If the value entered is greater than zero, then the wrap is applied with
the same thickness on all sides of the band. The wrap extends from the pipe center
line up to a distance equal to 0.5 X PipeOD as shown by the grey dimension. If this value is zero, or not defined, then wrap
is not seen.


None:  A warning displays if you try to put wrap on J Hanger type parts.


Image:[Image-Analysis: The image depicts a technical illustration, likely related to material thickness in a cylindrical object. It features a circular shape representing a cross-section of a solid object, with a measurement line indicating thickness marked as "Thickness2". There are also arrows pointing to specific areas, which may denote the measurement points or areas of interest. The top part shows a connection point, suggesting that this illustration could pertain to mechanical or structural engineering, where the thickness of materials is crucial for determining strength and stability. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P4Cp9UPlFEWnI2Bhf3u~WQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P4Cp9UPlFEWnI2Bhf3u~WQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307934?contentId=3N~oZvPJ2QTYKbYhq3172Q)
These bolt properties are for J Hanger Type. The bolt is parallel to where the existing
band runs, if there was not a gap.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt. For J Hanger type, if Pin1Diameter £ 0, then use
RodDiameter.


None: 

IJUAhsPin1::Pin1Length

Specifies the length of the bolt. For J Hanger type, if Pin1Length £ 0, then use Gap1 + 2 X Pin1Diameter.


Image:[Image-Analysis: The image depicts a technical drawing of a component, likely related to pin or bolt measurements. It illustrates a cylindrical part with markings indicating lengths, specifically labeled as "Pin1Length." The drawing includes directional arrows indicating the measurement dimensions. The marking at the top suggests a possible connection or attachment point, while the circular base might represent a fitting or connector within a larger assembly. Overall, the image serves as a reference for understanding a specific measurement in mechanical or engineering applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ivRht4gsvC0FXD8U4OksDg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ivRht4gsvC0FXD8U4OksDg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Hole Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307940?contentId=MaaBBX1QrXTzwPjWRA6bIg)
This is the bolt for J Hanger type only. The J Hanger can be used without a rod so
it has a structure port on the band.

IJUAhsHeight3::Height3

Specifies the distance from the pipe centerline to the structure port. The hole does
not display on the graphics.


Image:[Image-Analysis: The image depicts a simple mechanical system that includes a circular object, likely a gear or pulley, connected to an arm that is supported by a vertical structure. The left side shows a line labeled "Height3", indicating a measurement of height associated with the circular object. There are red points which could represent key reference locations or pivot points. The design suggests a relationship between the height measurement and the positioning or operation of the circular object, possibly in a physical system where height affects its function or movement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GFGFAqHs7qwtWRpyb6Q88A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GFGFAqHs7qwtWRpyb6Q88A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307953?contentId=1tH6f8N~p7j7nXk3izqcpg)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Kw5Gftc209P_jl5RG0hcAg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=aba493bfdb98ad90)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Kw5Gftc209P_jl5RG0hcAg-_PVFQNoCl4XmjAxWO0f7XQ/content)

For the standard type and ring type there are two ports: Route and RodEnd.


Image:[Image-Analysis: The image presents a technical illustration showing two different components, probably related to mechanical or structural engineering. On the left side, there is a diagrammatic representation of a component identified as "Rod End" and labeled with its coordinate axes: X, Y, and Z. The term "Route" is also indicated within the circular section denoted in grey, likely indicating a pathway or passage related to the component. The right side features a simpler cylindrical component that appears to be a casing or housing, also labeled with the same axes (X, Y, Z) along with a circular base indicated in grey. The annotation of axes suggests that both components may interact or be installed in a manner that requires understanding their orientations and positioning in a three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wZjtV3M0Q0FTNBYKxOMNVQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wZjtV3M0Q0FTNBYKxOMNVQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

For the J Hanger type, there are three ports: Route, RodEnd, and Surface.

In the J Hanger configuration, both the Route port and the RodEnd port retain their orientation. The Surface port’s X-axis is aligned along the side of the band. Its XY plane is flush with the
surface of the band.


Image:[Image-Analysis: The image depicts a mechanical or geometrical diagram illustrating the relationship between various components and axes. It features a labeled 'Surface' and 'RodEnd' positioned next to an articulated path named 'Route.' The diagram indicates three axes: X, Y, and Z, with their corresponding orientations. The X and Z axes are shown vertically and horizontally, respectively, while the Y axis appears to be represented within the circular 'Route.' This arrangement suggests that the components are part of a system where spatial orientation is crucial, likely for a mechanical assembly or simulation involving motion or force distribution. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h5P8oOR78bZYKFb8W0MLQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h5P8oOR78bZYKFb8W0MLQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

In order to be able to connect easily to a pipe, the X-axis of the Route port goes through the opening of the ring. The Z-axis points towards the RodEnd port.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1016 - Pipe Clamp | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – RodEnd

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - IntThdRH | Diameter of the rod for connecting to other components | Rod Diameter | Rod Diameter |
| 1011 - IntThdLH |

Optional Port3 – Structure (0, -PipeOD/2 – 2\*Thickness2 – Thickness1, Height4)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - Steel | -1 | 9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Turnbuckle - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307148?contentId=RUj8CIOLEYTY61ZN9EwaIg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Turnbuckle  
Part Name: Turnbuckle  
Part Description: Turnbuckle SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GnTyP93ml3e7R5UigSTeMA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0ab1087cb11cecab)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GnTyP93ml3e7R5UigSTeMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Turnbuckle SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Rod Fittings > Turnbuckle - approx 6 in Opening as shown in the following example:

   ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eXjWAJ9toZ507Pf6q6NYjQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6ca47e2ba4828fc7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eXjWAJ9toZ507Pf6q6NYjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a diagram showing the structural alignment of two rods with their endpoints labeled. It includes an XYZ coordinate system with Z oriented vertically and X oriented horizontally. The two rods are labeled as RodEnd1 and RodEnd2. RodEnd1 is positioned at coordinates (0,0,0), while RodEnd2 is positioned at (0,0,-Opening), indicating a downward offset from the first rod. This suggests a relationship where RodEnd2 extends below RodEnd1 by a certain opening distance, possibly indicating a mechanical or structural relationship between them. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBkVCRi6jQYv3wvdx2YB2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBkVCRi6jQYv3wvdx2YB2w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Turnbuckle Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307152?contentId=Yx3CTLF90kW5SuQMqyG4zQ)
The following properties are used for the part selection rule and the location of
the ports. You must enter the values to get a correct port location and for the selection
of turnbuckle part based on part selection rule.


None:  The default unit of distance for these properties is "mm". Use "in" to specify inches
for the dimensional value.

IJUAhsRodDiameter::RodDiameter

Defines the outside diameter of the rod that attaches to the turnbuckle. This value
is used only for part selection rules for choosing the correct turnbuckle part and
has no impact on creating graphics. For reducing couplers, you must enter the larger
rod diameter.


None:  The rod is not modeled in the turnbuckle's graphics.


Image:[Image-Analysis: The image depicts a schematic diagram of a mechanical component, likely a hydraulic or pneumatic actuator. It consists of a cylinder with two ends, each connected to a separate chamber. The red dots within the chambers could represent pistons or internal components that manage the movement of fluids or gases within the cylinder. Arrows indicate the direction of flow or actuation, illustrating how pressure can lead to upward or downward movement. The component operates by converting energy into mechanical motion, which is essential in various applications such as machinery, automotive systems, or industrial equipment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BDeKjARiQgY6oGhGD77EtQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BDeKjARiQgY6oGhGD77EtQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Defines the distance between the ports. This value represents the amount that the
turnbuckle takes out of the overall rod lengths. If this value is set to zero, such
as for a coupler, then the ports will be located with a small space between them.


Image:[Image-Analysis: The image depicts a schematic representation of a piezoelectric element, which is used in various applications to convert mechanical energy into electrical energy and vice versa. The sketch includes two side-by-side rectangles representing the piezoelectric material, with arrows indicating movement or the flow of energy between the two. The arrows point towards the center where the electrical connections are likely made, showcasing how compression or tension applied to the piezoelectric element will generate an electric charge. The red arrows suggest the direction of force or energy flow, enhancing the understanding of how the piezoelectric device operates in converting energy forms. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TUq5H9fIw547hTzsP0xaRg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TUq5H9fIw547hTzsP0xaRg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOpening1::Opening1

Defines the inside distance between the two nuts. This value can be set to zero.


Image:[Image-Analysis: The image illustrates a mechanical system consisting of two elements on either side, indicated by the rectangular boxes that represent loads or supports. There are two arrows pointing left and right, suggesting that there is tension or compression occurring between the two sides. The red dots represent internal reference points or stress indicators, possibly signifying points where forces are applied. This configuration could be part of a larger structural analysis, analyzing how forces are transmitted through this mechanism. The elements on the far left and right could be considered supports holding the central component, analogous to how bridges are supported. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jbkYQTbsKIeclYYIq1tFZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jbkYQTbsKIeclYYIq1tFZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307155?contentId=qtyHyF2B0GpPywXpVUOeqQ)
These properties specify the end nut shape properties for the turnbuckle.

IJUAhsShape1::Shape1Type

Enter the codelist number of the shape type as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.


None:  In each of the following examples, the end nut shape is depicted with hatched lines.

* 1 - Round


Image:[Image-Analysis: The image depicts a mechanical component, likely a bearing assembly. On the left side, there are two cylindrical parts that represent the outer and inner rings of the bearing. These rings are shown in a way that suggests they can rotate relative to each other, which is a common characteristic of bearings, allowing for smooth motion. The two red dots indicate points of contact or possible lubrication points, which are critical areas for reducing friction. On the right side of the image, a circular view of the bearing is shown, which likely represents the cross-section view of the bearing. This is meant to illustrate the internal structure and the arrangement of the components within the bearing. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tJJSb63G4Kav11_RwLDt0g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tJJSb63G4Kav11_RwLDt0g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: The image shows a mechanical component, likely a coupling or a similar device used to connect two shafts or pipes. On the left, there are four components lined up horizontally. The outer sections appear to have textured or grooved surfaces, possibly to enhance grip or allow for a better connection. The two central sections, marked with red dots, likely indicate where alignment or connection points are, showing the precise spot where two parts would connect or engage. On the right side, there is a top-down view of a similar component, revealing a circular opening in the center, which can be a feature designed for connecting to another shaft or as part of a larger assembly. This setup is commonly found in machinery where rotational motion needs to be transferred between different parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dz5nm5DO2NxlyVqfqkdNMw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dz5nm5DO2NxlyVqfqkdNMw-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image displays two mechanical components. On the left side, there is a depiction of a cylindrical part with red dots indicating specific points of interest. This part appears to be a type of connector or coupling component, which is often used to join two shafts or sections of machinery together. The red dots could signify alignment marks or indicate where other components are connected. On the right side, there is a hexagonal shape that looks like a nut or a bolt head, which is commonly used in fastening applications. It is essential for connecting parts securely. Overall, these shapes highlight components that are typically involved in mechanical assemblies and connections. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yh5~7vIi3wqaoWsfX_R9qw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yh5~7vIi3wqaoWsfX_R9qw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the end nuts. If this value is set to zero, the
end nut shape is not displayed.

* 1 - Round


Image:[Image-Analysis: The image displays a mechanical component, likely a coupling or a connector used in engineering or machinery. On the left side, there are two cylindrical components, separated by a space, indicating that they are connected by something that allows for movement or flexibility (perhaps a flexible coupling). The red dots suggest points of attachment or alignment necessary for proper functioning. The right side shows a top view of a cylindrical shape with the indicated vertical arrows, which may represent motion or the range of movement allowed in the axial direction. This design typically serves to connect two rotating shafts while accommodating misalignment or vibration between them. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ONqqU9Ek2l7IxMbH2pD4EQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ONqqU9Ek2l7IxMbH2pD4EQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: The image depicts a mechanical component, likely a coupling mechanism, which connects two shafts. On the left side, there are two cylindrical parts with red dots indicating connection points. The central area suggests there are two shafts that align through these couplings. On the right side, it is shown how the couplings allow for axial movement, as indicated by the arrows pointing up and down. This mechanism is essential in transmitting torque and rotational motion while allowing some degree of flexibility or movement between the connected shafts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EYhDZBrICjdBq2VtY0zgug-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EYhDZBrICjdBq2VtY0zgug-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image depicts a simplified schematic of a mechanical component, likely a coupling or connector system that involves two connected shafts. The left side shows two shaft segments, possibly indicating an alignment or connection point, while the two red dots likely represent connection points or positions for alignment. The right side includes a representation of a clamp or fastener that surrounds the shaft, with arrows indicating movement or adjustment capabilities. Overall, the diagram illustrates how these components fit together and the mechanism by which they can be adjusted or locked in place. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DKB9nrIVNWqj6OrPsZRSHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DKB9nrIVNWqj6OrPsZRSHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the outside length of the end nut shapes. If this value is set to zero,
then the value specified in Shape1Width1 is used. This value is not used for Hex Shape.

* 1 - Round


Image:[Image-Analysis: The image depicts a circular shape in the center, which has a concentric dashed circle around it. This likely represents the concept of a radial measurement or a model illustrating measurements like diameter or radius. The horizontal arrows on both sides at the bottom indicate a dimension being measured across the diameter of the circle, showing the distance from one side of the circle to the other. The relationship between the concentric circles and the arrow measurements indicates a focus on understanding the size and spatial properties of the circular shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lyO51yvkzfK2gB5w3_QMHg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lyO51yvkzfK2gB5w3_QMHg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: The image depicts a square shape with a circular outline inside it, suggesting some geometric relationship. There are arrows at the bottom indicating measurements or dimensions, likely representing the width or distance across the square. The circular outline could imply a focus on the inner space of the square, possibly indicating a design or engineering context where these shapes and measurements are relevant for understanding size or fit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NXSbsM6ERZrF4bKrccEj3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NXSbsM6ERZrF4bKrccEj3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the thickness of the end nut shape. Both positive and negative values are
acceptable. If this value is set to a negative, then the end nut shapes are located
within Opening1. If this value is set to zero, then the end nut shape is not displayed.

* Shape1Length < 0 (Negative)


Image:[Image-Analysis: The image depicts a mechanical component with a labeled opening referred to as "Opening1." The drawing illustrates a space between two separate sections, indicating a mechanism where materials or forces can pass through. The arrows suggest movement, potentially indicating flow or direction within the context of the mechanism. Two red points within a central section likely indicate key positions or sensors related to this opening. The overall structure suggests a focus on how external elements interact with internal components through this designated space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FHxqcxvckfjoJwNUlDkKAQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FHxqcxvckfjoJwNUlDkKAQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Shape1Length > 0 (Positive)


Image:[Image-Analysis: The image illustrates a basic electrical circuit component called a "capacitor." It shows the structure of a capacitor, which consists of two conductive plates (represented by the two horizontal rectangles) separated by an insulating material (the space in between). The arrows on the left indicate the flow of electrical charge, which can be stored in the capacitor. The red dots inside the capacitor represent the positive and negative charges that build up on the plates when voltage is applied. Capacitors are essential components in electronic circuits, as they store electrical energy temporarily and release it when needed. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61bqHiW_HvXSmHXoRWnDPQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61bqHiW_HvXSmHXoRWnDPQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Blocks Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307156?contentId=oohYX1_VzK7TGclX_EmKcg)
IJUAhsLength2::Length2

Specifies the length of the side blocks. If this value is set to zero, then the side
blocks are not displayed.


Image:[Image-Analysis: The image depicts a simplified mechanical illustration of a component, possibly a coupling or a drive shaft, shown in a top-down and side view. There are two main cylindrical parts situated horizontally and vertically. The cylindrical components are depicted with a hatched texture, indicating they may be solid and robust, suitable for transmitting torque. Red dots suggest points of interest, possibly indicating connection points or assembly features. Arrows on the horizontal space depict directional movement or adjustment, likely indicating how the components can slide or align with other parts. The circular outline on the right presents a cross-sectional view, emphasizing the cylindrical shape of the component. Overall, this image is likely part of an engineering or mechanical design that illustrates how different parts connect and function as a system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4anlqOtAHgOtDdfDqo86lw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4anlqOtAHgOtDdfDqo86lw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the width of the side blocks. If this value is set to zero, then the side
blocks are not displayed.


Image:[Image-Analysis: The image illustrates a basic schematic of an electromagnetic relay. On the left side, the relay is depicted in a simplified form, showcasing its coil and contact points. The highlighted red dots likely represent the points where the current flows or interacts within the relay. The right side shows a circular representation of the relay, highlighting its function as a switch that opens or closes the circuit based on the electromagnetic effect generated by the coil when energy is applied. The arrows indicate the direction of the current flow and the operation of the switch. Overall, the image communicates the fundamental components and operation of an electromagnetic relay in electrical circuits. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jku3yADQE49~FPrUpCaTkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jku3yADQE49~FPrUpCaTkg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the side blocks. If this value is set to zero, then the
side blocks are not displayed.


Image:[Image-Analysis: The image depicts a simplified schematic of a linear solenoid and its operation. On the left, we can see a rectangular shape representing the solenoid body with arrows indicating direction of magnetic and linear force. There are also red dots indicating the positions and motions of certain elements within the solenoid. The right side of the image shows a circular representation of a solenoid that emphasizes its cylindrical shape, typically where the electric coil would be wound. The overall relationship here is between the solenoid's physical structure and the directional forces exerted when it is activated, which is essential in understanding how solenoids convert electrical energy into linear mechanical motion. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJwiegs8GhRPTWPo~cdMig-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJwiegs8GhRPTWPo~cdMig-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOpening2::Opening2

Specifies the opening between the two side blocks. If blocks are not to be displayed,
ignore this value.


Image:[Image-Analysis: The image depicts a schematic diagram of a control or interface system. It features two rectangular elements on either side, possibly representing input and output devices or processes. The central area includes a component with arrows indicating a flow or transfer of information or materials between the two boxes. It suggests that the left side sends input to the central control system, which then processes this input and outputs it to the right side. The highlighted red elements could indicate points of control or critical interactions within this system. This design may be related to automation, manufacturing processes, or data handling systems, showing connections with clear directional indicators for operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m28TPtI8zx2kI7F8_Tn2Kw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m28TPtI8zx2kI7F8_Tn2Kw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Center Tube Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307158?contentId=1LPe7gxeGQdgg7TAHTSrKA)
IJUAhsDiameter1::Diameter1 (Optional)

Specifies the diameter of the round center tube. Usually this property is used for
a turnbuckle without side blocks, but it can be used for either. The tube will be
modeled as the same length as that defined in Opening1 and will be fitted between the two nut end shapes. If this value is set to zero, then
the center tube will not be displayed.


Image:[Image-Analysis: The image depicts a simple diagram illustrating the concept of a mechanical system, possibly a coupling or a connector between two elements. On the left and right sides, there are two rectangular boxes representing separate entities (like machines or components) that are connected by a central cylindrical shape, which could symbolize a shaft or a joint. The arrows indicate the direction of movement or force transmission between the components, suggesting an interaction or relationship where energy or motion is being transferred from one side to the other. Overall, the diagram simplifies how components in a mechanical system work together. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jgChX9UHn7xqCFN85qs_xw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jgChX9UHn7xqCFN85qs_xw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307153?contentId=HTr8j8sbarFns28X_ncDSw)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mkrzs2SI2jAKbYWabbFgWg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=91aad54851e193cc)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mkrzs2SI2jAKbYWabbFgWg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Turnbuckle

Port1 - RodEnd1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001 – IntThdRH    1003 – IntThdLH | Enter the maximum depth that the connecting rod can penetrate the turnbuckle.  Use the distance between the RodEnd1 and the Surface1 ports. | Enter the smallest rod diameter that can connect to this port.  Use same value as RodDiameter attribute. | Enter the largest rod diameter that can connect to this port.  Use same value as RodDiameter attribute. |

Port2 - RodEnd2

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1003 – IntThdLH    1001 – IntThdRH | Enter the maximum depth that the connecting rod can penetrate the turnbuckle.  Use the distance between the RodEnd2 and the Surface2 ports. | Enter the smallest rod diameter that can connect to this port.  Use same value as RodDiameter attribute. | Enter the largest rod diameter that can connect to this port.  Use same value as RodDiameter attribute. |

Port3 - Surface1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this port type.  Use 0. | Not applicable for this port type.  Use -9999. | Not applicable for this port type.  Use 9999. |

Port4 - Surface2

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this port type. Use 0. | Not applicable for this port type. Use -9999. | Not applicable for this port type. Use 9999. |

Sample Configurations

The following port types can be used for both ends:

|  |  |  |
| --- | --- | --- |
| Part Name (Opening) | RodEnd1 | RodEnd2 |
| Turnbuckle Short (~ 3") | 1001 – IntThdRH | 1003 – IntThdLH |
| Standard Turnbuckle (~ 6") | 1001 – IntThdRH | 1003 – IntThdLH |
| Turnbuckle, Medium (~ 9") | 1001 – IntThdRH | 1003 – IntThdLH |
| Turnbuckle, Long (~ 12") | 1001 – IntThdRH | 1003 – IntThdLH |
| Turnbuckle, Extra Long (~ 18") | 1001 – IntThdRH | 1003 – IntThdLH |
| Turnbuckle, Double Extra Long (~ 24") | 1001 – IntThdRH | 1003 – IntThdLH |
| Turnbuckle, Both Ends RH Thread (~ 6") | 1001 – IntThdRH | 1001 – IntThdRH |
| Rod Coupler | 1001 – IntThdRH | 1001 – IntThdRH |
| Reducing Coupler | 1001 – IntThdRH | 1001 – IntThdRH |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307278?contentId=MW0MverqLZULccD_7ESdSg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.UBolt  
Part Name: U-Bolt  
Part Description: U-Bolt SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ioJmpgFBZPEMJVtTDErupA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=37fc081cd594de13)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ioJmpgFBZPEMJVtTDErupA-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample U-Bolt SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity: , and then select the design support.
4. In the Select Part dialog, select a part from Parts > SmartParts > S3D Standard > U-Bolts > U Bolt - Standard as shown below.

   
Image:[Image-Analysis: The image represents a hierarchical tree structure, likely from a software or a database, showing a categorization of parts or components. At the top level, there are the categories "SmartParts" and "S3D Standard," which branches into more specific subcategories. Under "S3D Standard," there are several folders including "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Struts," and "U-Bolts." Each of these folders likely contains related items or specifications for that category. The emphasis on U-Bolt, marked at the bottom, suggests it is a specific item of interest within the broader classification. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7BVhUlomUrDmnBcW92hf2Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7BVhUlomUrDmnBcW92hf2Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image is a three-dimensional coordinate system diagram used in mathematics or engineering, showing the X, Y, and Z axes. The Y-axis is represented with a leftward arrow and a label, while the Z-axis has an upward arrow, both in red color. The origin point is marked as "0,0,0" with a green waveline beneath it. The diagram is likely depicting a quarter-section of a cylindrical shape based on the arches seen, while highlighting the points of reference in a spatial context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ke0QMQ7XzAgnbbXnuTJ3hw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ke0QMQ7XzAgnbbXnuTJ3hw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic U-Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307283?contentId=ScpmLEx~KMvtugjZKwpAZg)
These properties define the geometry of the U-Bolt.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of the dimensional value to use inches (for example 10in).

IJUAhsUBolt::UBoltWidth

Specifies the center-to-center distance between the legs of the U-Bolt. This value
is always greater than UBoltRodDia and determines the spacing of the vertical legs of the U-Bolt as well as the bend
radius for the curved part of the U-Bolt. The nominal bend radius is equal to half
the UBoltWidth dimension.


Image:[Image-Analysis: The image depicts a U-bolt, which is a type of fastener shaped like the letter "U". It is commonly used to secure objects, particularly in applications involving pipes or other round materials. The image includes a labeled measurement indicating the "U Bolt Width", which is the distance between the two vertical legs of the U-bolt. There are also small red dots representing the edges of the U-bolt at the top, providing a visual reference for the width measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJqQSyiRwTC0agczEtLbBA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJqQSyiRwTC0agczEtLbBA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltCenterToEnd

Specifies the distance from the pipe centerline to the end of the U-Bolt legs.


Image:[Image-Analysis: The image illustrates a U-bolt diagram, which is a type of fastener used to hold objects together. It shows a U-shaped bolt with measurements indicating the distance from the center of the bolt to its end. The highlighted points in red may represent specific measurement markers, while the blue arrow points to the measurement line labeled "UBoltCenterToEnd." This label indicates the name of the measurement, emphasizing that it pertains to the distance from the center of the U-bolt to one of its ends. Overall, the image provides a technical representation of how to measure a U-bolt relevant for engineering or construction applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vz4BrTD5RMOrU2LumLLiWw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vz4BrTD5RMOrU2LumLLiWw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltRodDia

Specifies the diameter of the round stock used to make the U-Bolt. If this value is
zero, none of the U-Bolt shape is drawn (unless the UBoltDia2 is non-zero).


Image:[Image-Analysis: The image depicts a U-bolt, which is a type of fastener commonly used to support or secure pipes, rods, or other cylindrical objects. It consists of a curved section and two straight legs extending downward. The graphical representation includes two red dots, likely indicating specific points of measurement or attachment, and a label at the bottom that reads "UBoltRodDia," suggesting a focus on the diameter of the rod that the U-bolt is designed to accommodate. Overall, the image serves to illustrate the structure of a U-bolt and may be used in technical documentation related to its design or application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvEz4rkVYm8kdjgoUYZ_FA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvEz4rkVYm8kdjgoUYZ_FA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2

Specifies a diameter change, for round insulation, coatings, or to delete the curved
part of the U-Bolt. If this value is greater than zero, changes the diameter of the
curved part of the U-Bolt starting at the position UBoltDia2Start as shown in Figure 1. This value can be larger or smaller than UBoltRodDia. If the value is zero, defaults to the same diameter as UBoltRodDia. If the value is less than zero, curved part of U-Bolt is not visible in the graphics
starting at the UBoltDia2Start as shown in Figure 2.


Image:[Image-Analysis: The image depicts a U-bolt, a type of fastener shaped like the letter "U" that is used to secure objects. The U-bolt is shown in a simplified schematic form with labels to highlight specific features. The highlighted section labeled "UBoltDia2" indicates a measurement relevant to the diameter of the U-bolt, which is commonly necessary for understanding the specifications of the bolt in various applications. The image also includes red dots that likely represent points of measurement or reference on the U-bolt. The label "Fig. 1" suggests that this is part of a larger documentation or presentation, indicating it is the first figure referenced. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D10dzZamLGjDyeU7VIOlNA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D10dzZamLGjDyeU7VIOlNA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2Start

Specifies the start position of a diameter change and is used to represent round insulation,
coatings, or to delete the curved part of the U-Bolt. If UBoltDia2 is zero or the same as UBoltRodDia, then this value has no effect because there is no change in the rod diameter.


None: 

IJUAhsUBolt::UBoltFlatSpot

Controls whether a flat-spot is shown on the curved part of the U-Bolt and also reduces
the bend radius and center points for the curved part of the U-Bolt. If this value
is positive, a flat spot is shown in the curved section of the U-Bolt. If this value
is zero, no flat spot is shown. This value is always less than BoltCenters1 minus UBoltRodDia.

If the value for UBoltDia2 is negative, then this flat spot value is ignored because there is no curved part
of the U-Bolt to have a flat spot.


None: 

IJUAhsUBolt::UBoltTopGap

Specifies the gap between outside of pipe and inside of U-Bolt (this gap is based
on UBoltRodDia, not on UBoltDia2). This value affects the vertical position of the bend radius center for the curved
portion of the U-Bolt.


None: 

IJUAhsUBolt::UBoltOneSided

Specifies if the U-Bolt is one-sided. If it is set to Yes, the right side of the U-Bolt is not shown below the tangent point, nor are the nuts
included on the right side.


look for an icon that resembles a U-shape with red dots below it, suggesting a curved design or arch: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307311?contentId=fVyMHxpupVkRWN4mgM3UwA)
You can define properties for four different nuts or washers.


Image:[Image-Analysis: The image depicts a schematic representation of a connection involving existing steel elements and an unspecified component. The drawing shows a central bar labeled "Existing Steel," indicating that it is part of a structural element. On either side of this bar, there are two vertical components with lower connectors (indicated by numbers 1 and 2) that suggest they are affixing to the existing steel. Above the existing steel, there is a semi-circular arch, likely representing a structural or reinforcement element. Points labeled 3 and 4 may indicate connection points or specific features related to the arch or connectors. The overall structure hints at engineering or construction context, focusing on metal connections. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vxJgF9AE2VHpoNJn9~kr6g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vxJgF9AE2VHpoNJn9~kr6g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Position of Nut 1 is immediately below existing steel
* Position of Nut 2 is below Nut 1
* Position of Nut 3 is Gap1 below bottom of pipe
* Position of Nut 4 is above Nut 3

IJUAhsShape1::Shape1Type

Determines the graphic shape used for the nut or washer using the codelist number
defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.


Image:[Image-Analysis: The image displays three different geometric shapes, each labeled with a number and a name. The first shape, labeled "1 - Round," is a circle with a dot in the center. The second shape, labeled "2 - Square," is a square, also with a dot in the middle. The third shape, labeled "3 - Hex," is a hexagon, featuring a dot at its center as well. This image likely serves as a reference or guide for identifying or distinguishing these shapes based on their numerical labeling. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B8Dpm2sO7xpTuSXya5JIkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B8Dpm2sO7xpTuSXya5JIkg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned codelist values are applicable for Shape2Type, Shape3Type, and Shape4Type as well.

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the nut or washer.


Image:[Image-Analysis: The image displays three different geometric shapes, each labeled with a number and a descriptive term. The first shape is a round circle, labeled "1 - Round," indicating its circular form. The second shape is a square, labeled "2 - Square," emphasizing its four equal sides and right angles. The third shape is a hexagon, labeled "3 - Hex," which has six sides and is shown with a dotted circle in the center. This image likely serves to illustrate basic geometric shapes and their characteristics for educational purposes or design considerations. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QvjRer4FtonQvCImmpWa8Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QvjRer4FtonQvCImmpWa8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Width1, Shape3Width1, and Shape4Width1.

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Image-Analysis: The image provides a visual representation of three different shapes alongside their corresponding effects or characteristics. The shapes shown are a round shape (labelled as 1 - Round), a square shape (labelled as 2 - Square), and a hexagonal shape (labelled as 3 - Hex). Each shape is illustrated with its boundaries and has directional arrows indicating dimensions or effects associated with them. The round shape likely represents a specific effect or property in a particular context, the square shape has its own unique effect, while the hexagonal shape is noted to have "No effect." This implies there might be different contexts or applications where these shapes are used, with varying impacts depending on the shape utilized. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gVs~31axm~OXJk~H3S9~_A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gVs~31axm~OXJk~H3S9~_A-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Width2, Shape3Width2, and Shape4Width2.

IJUAhsShape1::Shape1Length

Specifies the thickness of the nut or washer.


Image:[Image-Analysis: The image displays a schematic representation typically used in electrical engineering or circuit design. On the top, there are two arrows pointing towards a vertical line, which suggests a flow or connection being initiated or terminated. Below that, there is a box-like structure with two red rectangles at its base. This structure likely represents a switch or a control element, indicating a mechanism to enable or disable the flow of current, corresponding to the arrows above. Overall, the image illustrates the concept of controlling or switching the flow in a circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/93xtGpp0AAgN0ESJPhWZ9A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/93xtGpp0AAgN0ESJPhWZ9A-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Length, Shape3Length, and Shape4Length.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Block Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307317?contentId=d~9zBOC9EGtFyPiRfCIYeg)
The block properties are optional and can be used to specify two stacked rectangular
blocks that are used to represent slide plates, shims, insulation pads, cradles, and
so forth. Enter the values for these properties only when Block geometry is required.

The position of Block 1 is exactly Gap1 below the bottom of the pipe. The position of Block 2 is on top of Block 1. Both blocks
have similar input properties: height, width and length. The blocks are not included
if any of these values are set to zero.


Image:[Image-Analysis: The image depicts a schematic representation showing two blocks, labeled as Block 1 and Block 2, which are likely components in a mechanical or structural assembly. They are positioned above an existing steel structure indicated at the bottom of the image. The central circular component may represent some kind of fastener, connector, or mounting point that plays a crucial role in the assembly of these blocks. The arrangement suggests a relationship in which the blocks are mounted or secured to the existing steel base, with an emphasis on how they are spatially oriented relative to one another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ1qRWylGtsXzEfHRM_KVA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ1qRWylGtsXzEfHRM_KVA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1 (Optional)

Specifies the distance between the pipe bottom and the top of Block 1. This distance
value can be a negative, zero, or a positive value. If set to zero, no gap exists
between pipe and Block 1. If set to a positive value, there is a gap of the specified
distance between the pipe and the top of Block 1. If set to a negative value, Block
1 is partially embedded into the pipe.


Image:[Image-Analysis: The image depicts a mechanical or structural setup involving a circular component, referred to as "Block 1," positioned above a rectangular horizontal segment labeled "Existing Steel." There are measurements indicated by the term "Gap1," which suggests a space between the circular component and the existing steel section. The components are interconnected in a manner that suggests they might be part of a support or bearing system, where "Block 1" is positioned to rest above the existing steel structure. The red dots likely represent points of interest or attachment, emphasizing the critical areas in construction or engineering design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r6Arzt1HGAeqbupcbaPsCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r6Arzt1HGAeqbupcbaPsCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::HeightX (Optional)

Specifies the height of the block.


Image:[Image-Analysis: The image depicts a technical illustration, likely related to an engineering or architectural context. It shows an object with a circular feature at the top, which is connected to a rectangular base labeled "Existing Steel." The term "Height1" is indicated to the right, suggesting that it is measuring a vertical dimension associated with this arrangement. There is also a red dot marked on the circular feature, possibly indicating a point of interest or measurement reference. The graphic elements suggest a schematic view where the relationship between the circular object and the steel base is being illustrated, highlighting both spatial configuration and height measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J2q13hpb_X9Ehq0A~tY6pQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J2q13hpb_X9Ehq0A~tY6pQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::WidthX (Optional)

Specifies the width of the block.


Image:[Image-Analysis: The image displays a technical diagram, likely related to a mechanical or engineering component. It features a central circular part, possibly representing a connector or fitting, outlined with dimensions labeled as "Width1." Below this circular component is a rectangular base labeled "Existing Steel," indicating that this part is designed to be mounted on or connected to an existing steel structure. The red dots in the diagram may represent specific points of reference or connections related to the assembly or positioning of the components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mRw6zeXyqJ0jZ2KnbQs5vw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mRw6zeXyqJ0jZ2KnbQs5vw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::LengthX (Optional)

Specifies the length of the block (the direction parallel to the pipe).


Image:[Image-Analysis: The image depicts a technical drawing of a steel component, likely for engineering or construction purposes. On the left side, we see a circular shape labeled "Existing Steel," which indicates this is a part that is already in place. Below it are two small horizontal bars that represent the base or anchoring points of the component. The right side includes a side view of the same component, showing a vertical prong extending upwards labeled "Length1." This suggests an emphasis on the dimensions or the specifications related to the height of this prong. Overall, it highlights the connectivity and specifications of this component in relation to existing structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jSZeuKpedyp1HI6kEWo25w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jSZeuKpedyp1HI6kEWo25w-_PVFQNoCl4XmjAxWO0f7XQ/content)

For the Nut properties, make sure that all four properties are similar for Nut 1,
Nut 2, Nut 3, and Nut 4 and are defined in a generalized way as you have done for
the Block properties.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307328?contentId=ptAX9h4pU49VZ1Z5V9xutw)
These properties are optional and are used to represent rectangular insulation, U-Bolt-band
combinations, or strap-shaped liners, with or without wings. Specify the values for
these properties only when strap geometry is required.

IJUAhsStrap::StrapWidthInside (Optional)

Specifies the inside distance between the legs of the strap. This value is greater
than PipeOD.


Image:[Image-Analysis: The image depicts a graphic representation of a strap width measurement. It shows a curved shape that resembles a hook or a strap loop. There are two red dots located at the top and bottom center of the loop. The horizontal lines with arrows indicate the width inside this loop, and there is text labeled "StrapWidthInside" below the illustration. This graphic likely serves as a visual guide to measuring the internal width of a strap or loop. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VH2wBPkkFr4HvKgWmqRXKQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VH2wBPkkFr4HvKgWmqRXKQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapHeightInside (Optional)

Specifies the inside height from the strap base to the top.


Image:[Image-Analysis: The image depicts a curved shape resembling a strap or a handle, with a marked vertical height indicated by arrows. The text "StrapHeightInside" labels this measurement which likely refers to the internal height of the strap or loop. The red squares may signify measurement points or endpoints, suggesting that the measurement is to be taken from these indicators. The overall layout emphasizes the importance of understanding the dimensions related to the inner height of the strap. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/REuYR~rL3ScTyVRIXJ9fQw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/REuYR~rL3ScTyVRIXJ9fQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapThickness (Optional)

Specifies the thickness of the rectangular stock used to make the strap. This value
cannot be zero.


Image:[Image-Analysis: The image illustrates the concept of "Strap Thickness." It features an arch-like shape, which may represent a strap or band, with two red dots indicating specific reference points on the strap. Below the arch, there is a visual representation of width, shown by two arrows pointing towards the center, suggesting measurement. The text "StrapThickness" is positioned beneath the diagram. This layout indicates that the thickness of the strap can be understood or measured in relation to the visual elements provided. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o1OljSd3wM~hhC60vyi4zQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o1OljSd3wM~hhC60vyi4zQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapStockWidth (Optional)

Specifies the width of the rectangular stock used to make the strap. This value cannot
be zero.


Image:[Image-Analysis: The image displays a diagram labeled "StrapStockWidth," which is likely related to the dimensions of a strap or a similar component. On the left side of the image, there is a curved shape representing the strap’s cross-section, possibly indicating how it fits around an object or component. It features two red dots, which could be highlighting specific measurement points or features of the strap design. On the right side, there is a rectangle, which appears to represent the width of the strap stock, providing a comparison between the two shapes. This arrangement suggests that the image is used to convey information about the width of the strap in relation to its cross-sectional profile. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9YKOkeIrlPsmmKtkKPrzCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9YKOkeIrlPsmmKtkKPrzCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapFlatSpot (Optional)

Adds a flat spot in the curved part of the strap. This value can be less than or equal
to StrapWidthInside. If set to zero, no flat spot is shown on the curved part of the strap. If set to
a positive value, the software adds a flat spot in the curved section of the strap
as shown in Figure 1. If set to the same value as StrapWidthInside, the software draws the strap like three plates with no corner rounding as shown
in Figure 2.


Image:[Image-Analysis: The image depicts a schematic representation labeled as "StrapFlatSpot." It shows a U-shaped connector with arrows indicating a compressive force, suggesting that the connector is designed to be flat or undergo flattening at the points indicated by the arrows. Additionally, there are two red dots marked along the central axis of the connector and a reference to "Fig. 1" in blue at the bottom. This likely denotes the first figure in a series of diagrams explaining the design or function of a component in a broader context, such as an engineering or mechanical design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C9Z12PwaWHF0IRlyfzP2Yg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C9Z12PwaWHF0IRlyfzP2Yg-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image illustrates a diagram labeled "StrapFlatSpot" and includes a rectangular shape with two horizontal lines at the top which represent the basic form or outline of what could be a flat strap or support structure. Below the rectangular shape, there are two red dots marking specific points of interest, possibly indicating dimensions or critical locations related to the structure's design. Additionally, the image features "Fig. 2" in blue text, implying that this diagram is part of a series and suggests a connection to previous figures or more extensive documentation on the topic. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eShTmsiI0WFCOswaMcMJ7Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eShTmsiI0WFCOswaMcMJ7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStrapGap::StrapTopGap (Optional)

Specifies the gap between the outside of the pipe and the inside of the strap.


Image:[Image-Analysis: The image illustrates a technical concept labeled "StrapTopGap." It features a circular object, presumably representing a component or part, with an arching strap-like element on top. The space or gap between the upper strap and the circular object is highlighted with a double arrow indicating measurement, suggesting that the "StrapTopGap" refers to the distance or gap between these two elements. Two red squares are positioned below the circular object, likely serving as reference points for alignment or measurement. Overall, the image focuses on the relationship between the strap, the circular object, and the defined gap, which is essential for understanding the requirements or specifications of an engineering design or mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/14CzjxQHe99d9LwwLw1vlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/14CzjxQHe99d9LwwLw1vlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapWidthWings (Optional)

Specifies the width of the outside wings. If this value is set to zero or to a value
that is less than (StrapWidthInside + 2 X StrapThickness), then the strap wings are not shown.


Image:[Image-Analysis: The image depicts a geometric shape resembling a strap or a loop, identified as "StrapWidthWings." At the top, there is a semicircular arch, and two vertical lines (represented by red dots) indicate specific points of measurement within the design. The horizontal arrow at the bottom suggests that the width of the strap or the area between the wings can be measured. This image likely serves as a technical diagram for understanding the dimensions and shape design for a particular purpose, such as in a product design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i__1Hd2oLHMbM~~7GGXFuQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i__1Hd2oLHMbM~~7GGXFuQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapOneSided (Optional)

Specifies if the strap is one sided or not. If set to Yes, then the right side of
the strap is not shown below the tangent point nor are wings, nuts, or gussets included
on the right side.


Image:[Image-Analysis: The image appears to be a simple diagram that shows the outline of a shape resembling a hook or a U-shaped figure. At the top half, there is a rounded part that represents the curve of the hook, and straight vertical lines extend downward, parallel to the central vertical axis. Below the hook, it seems to depict a horizontal line that signifies a flat surface, possibly indicative of the base on which the hook would rest. The red dots are placed at various points along the shape, likely to indicate specific points of interest or measurement within the diagram. Overall, the image serves as a simplistic representation of the hook shape, focusing on its basic geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lgm247Aa6XD9BNeVJxwVsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lgm247Aa6XD9BNeVJxwVsg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitGap (Optional)

Specifies that there is a gap at the top of the strap and splits the strap into two
parts.


Image:[Image-Analysis: The image depicts a schematic representation labeled "StrapSplitGap." It shows a set of parallel lines indicating some type of gap between them, which might suggest a physical separation in a material or a configuration of components. Below the gap are two red squares, which could indicate points of interest or electrical connections. The design appears to be technical, possibly related to electrical engineering or materials science, and the gap likely plays a significant role in the functionality of the system being represented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bZRhRvoDrPDoF6t0dN~O9A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bZRhRvoDrPDoF6t0dN~O9A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitExtension (Optional)

Specifies the length of the tabs from the top inside of the strap to the end of the
tabs.


Image:[Image-Analysis: The image appears to be a technical diagram that illustrates a component called "StrapSplit Extension." The diagram features a structure resembling a bracket or a split strap with a vertical measurement indicated. There are two red dots noted on the lower part of the design, which could signify specific points of interest or connection points. The use of the term "Extension" suggests that this component may serve to extend or modify the function of an existing part in a mechanical or structural application. Overall, this image conveys specific engineering details related to this component's design and function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_1q5hm6jALRdmxHVm7JPaQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_1q5hm6jALRdmxHVm7JPaQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Min/Max Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307347?contentId=s3Q~jEqQAKnMSYlRPs4Hdg)
IJUAhsMinPipeToSteel::MinPipeToSteel

Specifies the minimum allowed clearance between outside of pipe and steel.

IJUAhsMaxPipeToSteel::MaxPipeToSteel

Specifies the maximum allowed clearance between outside of pipe and steel.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [User Prompts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307348?contentId=3gCvhes61RI0rSCkKNfh6Q)
You can edit these properties on the part properties dialog box.

IJOAhsPipeOD::PipeOD

Specifies the actual outside diameter of the pipe (or insulation). This value is passed
in by the Assembly Information Rule (AIR) and by default it is set to some reasonable
value. This value is used to position the U-Bolt vertically along with UBoltTopGap and is used with Gap1 to locate the blocks and the nuts.

IJOAhsPipeToSteel::PipeToSteel

Specifies the clearance between the outside of the pipe and the steel. This value
is passed in by the AIR and by default it is set to some reasonable value.

IJOAhsSteelThickness::SteelThickness

Specifies the thickness of the steel to which the U-Bolt is attached. This value is
passed in by the AIR and by default it is set to some reasonable value.

IJOAhsRoty::RotY

Rotates the U-Bolt along the Y-axis of the route port. Use this property to align
the U-Bolt with sloped pipes or sloped steel.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307351?contentId=yJmCwBF6D7NX2Ek8gKHKEw)
These properties define the different U-Bolt port types and their sizes.


Image:[Image-Analysis: The image shows a table containing two main sections titled "Port 1: Route" and "Port 2: Steel." Each section lists several attributes related to ports, likely within a data structure or a database schema. The attributes include "Hgr/SymbolPort(1):Name," "Hgr/SymbolPort(1):PortType," "Hgr/SymbolPort(1):Size," "Hgr/SymbolPort(1):MinSize," "Hgr/SymbolPort(1):MaxSize," and "Hgr/SymbolPort(1):UnitType" for Port 1, while Port 2 has similar attributes prefixed with a (2) indicating it relates to the second port. This structure implies a comparison or relationship between two ports, each characterized by similar properties. The colors pink and green differentiate the two ports, making it easy to visually parse the data. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EcX0w1kSFoq_SAXE1Rt65w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EcX0w1kSFoq_SAXE1Rt65w-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  These ports are oriented to be aligned with the normal orientation of the reference
ports on the route and the structure when used in a U-Bolt assembly. If RotY is set
to some value, the route port is rotated about its Y-axis, effectively tilting the
U-Bolt when it is joined to the pipe reference port.


Image:[Image-Analysis: The image is a technical diagram illustrating a 3D routing path, likely for piping or cable systems. It features a curved route indicated by an arc, defining a specific path in a three-dimensional space. The diagram shows three axes: X, Y, and Z, which represent dimensions in a Cartesian coordinate system, a common reference in engineering and design. The labels "Route: 0,0,0" and "Steel: 0,0,-PipeOD-Gap1-Block1Height" provide coordinates and specifications related to the materials and parameters involved in the path. This implies that the routing must account for both the physical space (designated by the coordinates) and the material specifications (referenced in the 'Steel' label). This is crucial for engineers who design and analyze such systems to ensure proper fit and functionality in construction or manufacturing projects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9hjEnnJvRUJJUQZ8I13dJA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9hjEnnJvRUJJUQZ8I13dJA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 – Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 – Route | Pipe outside diameter | Pipe outside diameter | Pipe outside diameter |

Port 2 – Steel (0,0,-PipeOD-Gap1-Block1Height)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 – Steel | N/A – Set to 0 | N/A – Set to -9999 | N/A – Set to 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Variable Spring - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317078?contentId=g91qK7~vYXrBTVHUTC~Cfg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgIDs: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeA, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeB,
HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeC, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeD,
HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeE, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeF,
HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeG, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.VariableTypeGA  
Part Name: Variable Spring  
Part Description: Variable Spring SmartPart

Type A Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rIqTAtKK1yHjalUnN3FZZw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=23d42536d4f4f395)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rIqTAtKK1yHjalUnN3FZZw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type B Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OeX1vtAa374oL~JyM09NQw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e9a63965b700c2f6)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OeX1vtAa374oL~JyM09NQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type C Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pysXHjIP81tXosOKSd9_vg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dbc05a23501534de)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pysXHjIP81tXosOKSd9_vg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9iITCETHTYYY0aHgowV_xA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=de407e6e7dd39e66)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9iITCETHTYYY0aHgowV_xA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W0UfAwmfAiru~wwTSsrXww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=56ececac318a47cd)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W0UfAwmfAiru~wwTSsrXww-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YKu4Dha7lelH1dUaxgJT~g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8e5e08ea5630ace4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YKu4Dha7lelH1dUaxgJT~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6q39UXAwUydcfyQtymYahA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3bd11588b5f75082)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6q39UXAwUydcfyQtymYahA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type GA Spring:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/scRRRmdlY298w9LVJuekCg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f69efc1fef593147)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/scRRRmdlY298w9LVJuekCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Variable Spring SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Variable Spring Supports > Variable Spring - TypeA as shown in the following example:

   ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/66KN2yOI804_EJeEA36zsQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e1555c33e117ab6c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/66KN2yOI804_EJeEA36zsQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System

Type A Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pglvdHlZtAd3rboOATQvxw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=06ccd387edd78328)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pglvdHlZtAd3rboOATQvxw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type B and C Springs

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nAgDsOaQkuPt~23A3sfU4A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0a595cc40711a630)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nAgDsOaQkuPt~23A3sfU4A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fqjnjMWXmJ28V5aJZ0Sj_Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=66a571baa688c5a1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fqjnjMWXmJ28V5aJZ0Sj_Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6taVQok7jGVUiGypt6q12A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9bee0df1a1172974)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6taVQok7jGVUiGypt6q12A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2849VmWJhmAS_tCN9ROW2g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f00b407e35ebb265)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2849VmWJhmAS_tCN9ROW2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cghgu9xXbjlh0GtOQTpRAw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7b4c17d12e9ddfca)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cghgu9xXbjlh0GtOQTpRAw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type GA Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x9cNdMjpKOkT6mgzovKexA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ecabc86fb407b8f6)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x9cNdMjpKOkT6mgzovKexA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Generic Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317091?contentId=uJcS1my~V7NDEV0WOsQ1og)
IJUAhsSpringType::SpringType

Specifies the type of spring. Common types of springs are Type A, B, C, D, E, F, and
G.

IJUAhsSize::Size

Specifies the Variable Spring part for the Part Selection rule. This value is optional and is not included in the
Variable Spring graphics.

IJUAhsFigureNumber::FigureNumber

Specifies the manufacturer figure number.

IJUAhsRodDiameter::RodDiameter

Specifies the diameter of the rod that threads into the spring. RodDiameter is not included on a Type F spring.


None: 

IJUAhsWeight::Weight

Specifies the base weight of the trapeze type spring. This value is calculated based
on BaseLength.

IJUAhsBaseLength::BaseLength

Specifies the length of the trapeze spring. This value is calculated based on Weight.

IJUAhsWtPerLen::WtPerLen

Specifies the ratio of Weight and BaseLength due to deferring rod spacing on a trapeze spring.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dimensional Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317144?contentId=PU1NtBGUyfpSd~EKYORrzA)
Each spring type has a specific set of dimension attributes that govern the parts
functionality and controlling port locations. Though many of the dimension attributes
are common to all spring types, they are interpreted differently depending on spring
type. For more information, see [Dimension Details (Variable Spring)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/Cx4Zx71h7_Gae1xpxF7pMw).

IJUAhsHeight1::Height1

Specifies the total height of the spring casing. This value includes all shapes that
are used to make the casing and is common to all spring types.


Image:[Image-Analysis: The image depicts a vertical cylindrical object with a clear indication of its height labeled as "Height1." There are arrows at the top and bottom pointing upwards and downwards, showing potential movement or measurement direction related to the height. This likely represents a measurement concept, where the height of the cylinder is important for understanding its dimensions or physical properties. The cylindrical shape is often associated with various applications in physics or engineering contexts, such as fluid dynamics or structural analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUaoHUI2gbhMJgWcN1VWow-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUaoHUI2gbhMJgWcN1VWow-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the offset of a port with respect to a user-defined location on the spring.
Each spring has a unique offset value.

IJUAhsOffset2::Offset2

Specifies the offset of a port with respect to a user-defined location on the spring.
Each spring has a unique offset value.

IJUAhsLength1::Length1

Specifies the length of the load column. This value does not affect the functionality
of the part, but is used to model how far the column extends into the spring and does
not affect port locations.

IJUAhsGap1::Gap1

Specifies the distance between the two top lugs on a Type C spring.


None: 

IJUAhsRodTakeOut::RodTakeOut

Specifies the minimum working range load for RodTakeOut. This property is used in the calculations that determine the InstalledRodTakeOut of the installed load. Also, this value is used by Type A, B, C, and G springs.

IJUAhsRodAddIn::RodAddIn

Specifies the minimum working range load for RodAddIn. This property is used in the calculations that determine the InstalledRodAddIn of the installed load. Also, this value is used by Type D and E springs.

IJUAhsColumnHeight::ColumnHeight

Specifies the minimum working range load for the column height. This property is used
in the calculations that determine the InstalledHeight of the installed load.

IJUAhsColumnHeightMin::ColumnHeightMin

Specifies the minimum allowable column height at the minimum working range load. This
property is used by Type F springs.

IJUAhsColumnHeightMax::ColumnHeightMax

Specifies the maximum allowable column height at the minimum working range load. This
property is used by Type F springs.

IJUAhsRodLength::RodLength

Specifies the length of the top rod in a Type E spring. The actual rod is not included
with the part, but this length affects the port locations and the location of the
turnbuckle.

IJUAhsCC::CC

Specifies the distance between the centerlines of the road connected to a Type G spring.


Image:[Image-Analysis: The image is a technical illustration showing a setup involving two cylindrical objects (possibly pulleys or supports) connected by a straight bar. The abbreviation "CC" is prominently displayed, indicating "center to center," which is a common measurement in engineering that refers to the distance between the centers of the two cylindrical objects. The dashed lines leading to the cylindrical objects suggest points of connection, possibly for attaching cables or other components. Overall, this image likely represents a component layout or a schematic for mechanical design purposes, emphasizing the distance between two critical points. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6n7Oij~3dlLjTNM9ZYyXGQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6n7Oij~3dlLjTNM9ZYyXGQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCCMin::CCMin

Specifies the minimum allowable CC dimension.

IJUAhsCCMax::CCMax

Specifies the maximum allowable CC dimension.

IJUAhsBBGap::BBGap

Specifies the back-to-back gap between the steel sections of a Type G spring. If this
value is negative, only one section is modeled. If this value is greater than zero,
two sections are modeled back-to-back.


None: 

IJUAhsShoeHeight::ShoeHeight

Specifies the height of the shoe. This value is used by Type F and G springs to control
the location of the route port.

IJOAhsPipeOD::PipeOD

Specifies the outer diameter of the pipe. This property is used by Type F and G springs
to control the location of the route port.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dimension Details (Variable Spring) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317150?contentId=RBqlYYvk4AGqbgjhzjWGiA)
The supported dimensions for each spring type are shown below:


None:  Ports are shown as 
icon-description: look for an icon that resembles a red circle or stop sign: .

Type A Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/whvgsAWOHsfxq8ZINIedfw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ffb347a6dc052716)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/whvgsAWOHsfxq8ZINIedfw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type B and C Springs

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5erLaXUzrzAAvXYerzfJ1g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9180cd4b7db3618d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5erLaXUzrzAAvXYerzfJ1g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7QZyqogNoAqhL3RVy9kXPg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d2c6476ab7a0058c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7QZyqogNoAqhL3RVy9kXPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hLQeEReT5~9Z2i1J6AVp7A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e4a749f390a09d01)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hLQeEReT5~9Z2i1J6AVp7A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bote0ZZ1EKAZzU4Ek5GpuQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8d497ee9e4309a6a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bote0ZZ1EKAZzU4Ek5GpuQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g8p_TKDbUXfo7Pn9f0EEIg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=02e346bc00d8a96b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g8p_TKDbUXfo7Pn9f0EEIg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type GA Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8H5S2kXSkUl953m1Uy9~AQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9863d1b874d57c3e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8H5S2kXSkUl953m1Uy9~AQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Input Engineering Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317160?contentId=QPeCl575rBDklUlEM74Stw)
The input engineering properties control the functionality of the spring part over
varying loading conditions. These properties are used by the software while calculating
output engineering properties.

IJUAhsOperatingLoad::OperatingLoad

Specifies the operating load on the spring at the operating condition. This load is
also commonly referred to as the hot load.

IJUAhsMovement::Movement

Specifies the amount of thermal displacement of the pipe when moving from the Installed (Cold) to Operating (Hot) conditions.

IJUAhsMovementDir::MovementDirection

Specifies the direction of the new movement when switching from the Installed to Operating conditions. This property uses the codelist number defined in the hsSpringMovementDir sheet in the HS\_S3DParts\_Codelist.xls. A value of 0 specifies the direction as Up, while a value of 1 specifies the direction as Down.

IJUAhsSpringRate::SpringRate

Specifies the amount of force required to deflect the spring by a given unit distance.
Common units are 
None: .

IJUAhsMaxVariability::MaxVariability

Specifies the maximum allowable variability, where variability is defined as the percentage
change in the supporting load between the Operating and Installed conditions.

IJUAhsMinWorkingLoad::MinWorkingLoad

Specifies the low end of the spring working load range.

IJUAhsMaxWorkingLoad::MaxWorkingLoad

Specifies the high end of the spring working load range.

IJUAhsMinOvertravelLoad::MinOvertravelLoad

Specifies the load at which the spring is completely extended, and is equal to the
precompression of the spring in the casing.

IJUAhsMaxOvertravelLoad::MaxOvertravelLoad

Specifies the maximum spring load at the high end over travel, and is defined as the
load at which the spring is completely compressed.

IJUAhsMinLimitStopTravel::MinLimitStopTravel

Specifies the location of a limit stop restricting the travel of the spring with respect
to the minimum working range. A negative value is possible if the limit stop is placed
within the range of the over travel. If the value is less than the travel value corresponding
to the minimum over travel, then the limit stop is ignored.

IIJUAhsMaxLimitStopTravel::MaxLimitStopTravel

Specifies the location of a limit stop restricting the travel of the spring. If a
value is not assigned to this property, there is no limit stop applied.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Output Engineering Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317284?contentId=sgYnft8wBSleQTLkMBU1Jg)
The output engineering properties are calculated and populated by the software based
on the information provided by the input properties.

IJUAhsInstalledLoad::InstalledLoad

Specifies the load on the spring at the installed condition. This load is commonly
referred to as the cold load. The following calculation is used to find the installed
load value:


None: 

IJUAhsVariability::Variability

Specifies the percentage difference between Operating and Installed loads.


Image:[Image-Analysis: The image contains a mathematical formula representing variability in a specific context. It indicates that variability is calculated by taking the difference between Movement and SpringRate in the numerator, and dividing it by OperatingLoad in the denominator. This implies a relationship where changes in Movement and SpringRate impact the overall variability, depending on the Operating Load applied. Each of these terms (Movement, SpringRate, OperatingLoad) likely pertains to a particular field, possibly engineering or physics, where these parameters are relevant for analysis or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oBDjju~SQ5h3fdF03Y9K5g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oBDjju~SQ5h3fdF03Y9K5g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsInstalledTravel::InstalledTravel

Specifies the total spring travel at the installed load with respect to the working
range.


Image:[Image-Analysis: The image displays a mathematical equation used to calculate Installed Travel in a spring system. The equation is shown as: Installed Travel = (Installed Load - Min Working Load) / Spring Rate. This formula indicates that the Installed Travel is determined by the difference between the Installed Load and the Minimum Working Load, divided by the Spring Rate. Each component has a specific role: the Installed Load is the total weight or load applied to the spring, the Minimum Working Load is the least amount of load required for the spring to function effectively, and the Spring Rate is a measure of the stiffness of the spring, defined as the amount of force required to compress it by a specific distance. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/baCjzr9QBN5DGZIVje9NBA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/baCjzr9QBN5DGZIVje9NBA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOperatingTravel::OperatingTravel

Specifies the total spring travel at the operating load with respect to the working
range.


None: 

IJUAhsInstalledRodTakeOut::InstalledRodTakeOut

Specifies the calculated rod takeout at the installed load. This value is used by
Type A, B, C, and G springs. Alternatively, this value is the rod takeout that is
used when modeling the spring and determining port positions.


None: 

IJUAhsInstalledRodAddIn::InstalledRodAddIn

Specifies the calculated rod add-in at the installed load, and is used by Type D and
E springs. Alternatively, this value is the rod add-in that is used when modeling
the spring and determining port positions.


None: 

IJUAhsInstalledHeight::InstalledHeight

Specifies the calculated ColumnHeight at the installed load, and is used by Type F springs. Alternatively, this value is
the height that is used when modeling the spring and determining port positions.


None: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317295?contentId=RZ0zaFtQZm_GckQSCLV1ew)
For each shape property, the name of a shape can be specified. The name must correspond
to a shape of the correct type that is defined on a separate Hanger Service Class.
Not all shapes are used by all spring types, and all shapes are optional except for
SpringCase and LoadColumn.

IJUAhsNut1Shape::Nut1Shape

Specifies the name of the first nut shape.

IJUAhasNut2Shape::Nut2Shape

Specifies the name of the second nut shape.

IJUAhsLugShape::LugShape

Specifies the name of the lug shape.

IJUAhsPlate1Shape::Plate1Shape

Specifies the name of the first plate shape.

IJUAhsPlate2Shape::Plate2Shape

Specifies the name of the second plate shape.

IJUAhsCasingShape::CasingShape

Specifies the name of the spring case shape.

IJUAhsPlate3Shape::Plate3Shape

Specifies the name of the plate shape used for the bottom plate of a Type F spring.

IJUAhsColumnShape::ColumnShape

Specifies the name of the load column or rod shape.

IJUAhsColumnEndShape::ColumnEndShape

Specifies the name of the load column or rod shape. This is typically a nut shape.

IJUAhsTurnbuckleShape::TurnbuckleShape

Specifies the name of the turnbuckle shape.

IJUAhsNut3Shape::Nut3Shape

Specifies the name of the third nut shape.

IJUAhsTopAttachment::TopAttachment

Specifies the name of a shape.

Shape Details

Type A

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/53j1xpFQxg_TX2kffJuIzA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4c4e51cbb0f021b2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/53j1xpFQxg_TX2kffJuIzA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type B

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oqohjcuGKJvRi5mcBoAldA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2e1ca3680e8250a6)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oqohjcuGKJvRi5mcBoAldA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type C

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IRcVakLb5DsqPhkcl4iQ7Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f676277eacb6cacf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IRcVakLb5DsqPhkcl4iQ7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BuAojYAyaCo84KJFVPxnDA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=025672d162a45da7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BuAojYAyaCo84KJFVPxnDA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y4x9yE18hnC~tIxN15_Xrg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c9175e2f2bcb0ddc)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y4x9yE18hnC~tIxN15_Xrg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eCbblJZCT9AvGaOo_gsx0w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7b00d288edde32b3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eCbblJZCT9AvGaOo_gsx0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OhwM3PX0wPZnLkNmTf~Rug-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ea7e763d6b12ee83)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OhwM3PX0wPZnLkNmTf~Rug-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type GA

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5s0kNBiyKTaj3aP0ZVA~Rw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=de9a8db003035d60)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5s0kNBiyKTaj3aP0ZVA~Rw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317333?contentId=DRAqsY2jFRGgk7HSeo4tWA)
RodEnd Ports

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 - Internal Thread RH  1003 - Internal Thread LH | Rod Diameter | Rod Diameter | Rod Diameter |

Surface Ports

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 - Other | Use 0 | Use -9999 | Use 9999 |

Hole Ports

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1007 - Eye 1008 - Single Lug 1009 - Double Lug | Hole Diameter | 0 | Hole Diameter |

Structure Ports

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 3 - Structure | Use 0 | Use -9999 | Use 9999 |

Route Ports

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 2 - Route | Pipe OD | Pipe OD | Pipe OD |

BOM Description

This function provides the BOM Description in the following format:

++++++

The Part Description mainly includes any additional information required for ordering
purposes, including spring type, size, figure and travel series, and so on.

Units can be set by rules on the HgrBOMRules sheet in HS\_System.xls. These rules control the units, precision type, and precision.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Weld - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/348634?contentId=5TsUK~rHFDGck179UxzvYQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.WeldPoint, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.WeldRect  
Part Name: Weld  
Part Description: Weld SmartPart


Image:[Image-Analysis: The image appears to be a technical drawing or engineering blueprint that shows a junction or connection point between two lines, with a dimension indicated. The dimension shows a measurement of 6.3 units from one point to another. The layout is likely used in design and manufacturing processes, where precise measurements are crucial. The right side features a circle with a line through it, which may represent a specific type of bolt or hole used in the assembly of the components depicted in the drawing. Blue and green lines are used for clarity, indicating different layers or elements in the design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TlTznEsroAV~Bxdp3DQYUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TlTznEsroAV~Bxdp3DQYUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Weld SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign combined with a tool, suggesting an option for adding or editing: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Miscellaneous > Welds as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical tree structure representing folders and subfolders. At the top level, there are two main categories: "Parts" and "SmartParts". Under "SmartParts," there is a subcategory labeled "S3D Standard," which contains several further subcategories, including "Beam Attachments," "Clevises," "Constant Supports," and "Miscellaneous." The "Miscellaneous" category leads to items such as "Bolts," "Nuts," and "Pins." Within "Pins," there is a highlighted subfolder labeled "Welds," which further contains two items named "Point" and "Rectangle." This demonstrates an organizational structure that likely relates to engineering or manufacturing components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5IFL75URSsKEo49h5HDQLg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5IFL75URSsKEo49h5HDQLg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Weld Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/348636?contentId=Xl3eBvWNm7n8QcatA2UkJg)
IJWeldingSymbol::PrimarySideSymbol

Specifies the drawing symbol to use on the primary side. This property is applicable
only for fillet weld.

IJWeldingSymbol::SecondarySideSymbol

Specifies the drawing symbol to use on the secondary side. This property is applicable
only for fillet weld.

IJWeldingSymbol::PrimarySideGroove

Specifies the type of groove on the primary side. Available codelist values are:

* None
* Square
* V
* Bevel
* U
* J
* Flare-V
* Flare-Bevel

IJWeldingSymbol::SecondarySideGroove

Specifies the type of groove on the secondary side. Available codelist values are:

* None
* Square
* V
* Bevel
* U
* J
* Flare-V
* Flare-Bevel

IJWeldingSymbol::PrimarySideGrooveSize

Specifies the actual depth of penetration of the weld. This property is defined as
rule-based, but no value is computed. You can set a reasonable value for this property
based on factors such as material thickness, bevel depth, and so on.

IJWeldingSymbol::SecondarySideGrooveSize

Specifies the actual depth of penetration of the weld. This property is defined as
rule-based, but no value is computed.You can set a reasonable value for this based
on factors such as material thickness, bevel depth, and so on.

IJWeldingSymbol::PrimarySideActualThroatThickness

Specifies the depth of bevel from the primary side. This property is set from the
bevel parameters. A bevel depth of zero indicates that there is no bevel.

IJWeldingSymbol::SecondarySideActualThroatThickness

Specifies the depth of bevel from the secondary side. This property is set from the
bevel parameters. A bevel depth of zero indicates that there is no bevel.

IJWeldingSymbol::PrimarySideNominalThroatThickness

Specifies the fillet throat thickness, if it is a fillet weld.

IJWeldingSymbol::SecondarySideNominalThroatThickness

Specifies the elementary symbol on the secondary side.

IJWeldingSymbol::FieldWeld

Specifies whether this is a site or field weld. This is a codelisted value. Allowed
values are:

* YES


Image:[Image-Analysis: The image shows a simple diagram consisting of a horizontal line with an arrow indicating a direction. The arrow points downwards from a point where the horizontal line ends. This could represent a transition or flow from one state to another, suggesting movement or a connection towards something below. The angled arrow and the horizontal line can indicate a process, decision point, or relationship between different stages or objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_BX1TLyC_W2hLNVRx8TjYA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_BX1TLyC_W2hLNVRx8TjYA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* NO


look for icon that resembles a downward line with an arrow pointing to the right at the end, indicating a transition or direction change.: 

IJWeldingSymbol::AllAround

Indicates that the weld extends all the way around the joint that the arrow is pointing
at. This is a codelisted value. Allowed values are:

* YES


Image:[Image-Analysis: The image consists of a simple diagram featuring a straight horizontal line leading to a circular shape, which appears to represent a point of interest or a node. There is also a diagonal line extending downwards from the circular shape, leading to an arrowhead that indicates direction or movement toward the bottom of the image. This kind of diagram could be used to illustrate a concept, flow of information, or directional guidance, but it lacks context to specify its exact meaning. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PM8UnsrDOPtFzbjSdZ8sJQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PM8UnsrDOPtFzbjSdZ8sJQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* NO


icon-description: look for icon that resembles a downward arrow with a diagonal tail: 

IJWeldingSymbol::PrimarySideSupplementarySymbol

Specifies whether the shape of the weld surface on the primary side needs to be indicated
precisely.

IJWeldingSymbol::SecondarySideSupplementarySymbol

Specifies whether the shape of the weld surface on the secondary side needs to be
indicated precisely.

IJWeldingSymbol::WeldTailNotes

Specifies the text to be added in the tail notes. If WeldTailNotes is set to "TYP", the weld symbol shows the tail area with the text "TYP" in it. If WeldTailNotes is not populated, the tail area is not displayed.


Image:[Image-Analysis: The image shows a flowchart-like structure. It has an arrow pointing downward leading from the text "TYP" which appears to indicate a category or a point in the flowchart. The arrow suggests a direction or progression to the next step or element in the flowchart. However, the image does not provide additional context or information about what "TYP" refers to or what follows in the flow, making it difficult to determine the relationship or hierarchy of entities involved. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hPbw~c7TEeaZtrzmyEu4kg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hPbw~c7TEeaZtrzmyEu4kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJWeldingSymbol::TailNoteIsReference

Specifies whether a tail note is applied to the reference part. This property is valid
only if a tail note is provided.

IJWeldingSymbol::PrimarySideLength

Specifies the length of the weld on the arrow side. This property is used only for
intermittent welds. This property sets the nominal length of the individual weld segments.

IJWeldingSymbol::SecondarySideLength

Specifies the length of the weld on the other side.

IJWeldingSymbol::PrimarySidePitch

Specifies the center-to-center spacing on the arrow side.

IJWeldingSymbol::SecondarySidePitch

Specifies the center-to-center spacing distance on the other side.

IJWeldingSymbol::PrimarySideDiameter

Specifies the diameter of the spot weld on the arrow side.

IJWeldingSymbol::SecondarySideDiameter

Specifies the diameter of the spot weld on the other side.

IJWeldingSymbol::PrimarySideContour

Specifies the finished contour of the face of the weld. Contour symbols are used with
weld symbols to show how the face of the weld is formed. Set this property to NONE for all weld types.

IJWeldingSymbol::SecondarySideContour

Specifies the finished contour of the face of the weld. Contour symbols are used with
weld symbols to show how the face of the weld is formed. Set this property to NONE for all weld types.

IJWeldingSymbol::PrimarySideFinishMethod

Indicates the method to use for forming the contour of the weld. A finish method shows
the method of finish, not the degree of finish. For example, a C is used to indicate
finish by chipping, an M indicates machin\-ing, and a G indicates grinding. This property
is set to NONE for all weld types. This sets the finishing method (usually a machining operation)
to achieve the needed contour.

IJWeldingSymbol::SecondarySideFinishMethod

Indicates the method to use for forming the contour of the weld. A finish method shows
the method of finish, not the degree of finish. For example, a C is used to indicate
finish by chipping, an M indicates machin\-ing, and a G indicates grinding. This property
is set to NONE for all weld types. This sets the finishing method (usually a machining operation)
to achieve the needed contour.

IJWeldingSymbol::PrimarySideRootOpening

Specifies the primary side root opening. This property dimensions the space between
the joint to be welded and is placed inside the weld symbol. For all butt types, set
this property to full opening.

IJWeldingSymbol::SecondarySideRootOpening

Specifies the secondary side root opening. This property dimensions the space between
the joint to be welded and is placed inside the weld symbol. For all butt types, set
this property to zero.

IJWeldingSymbol::PrimarySideGrooveAngle

Specifies the total included angle of the groove between parts joined by a groove
weld in the primary side. The groove angle is also placed inside the weld symbol and
is given in degrees.

IJWeldingSymbol::SecondarySideGrooveAngle

Specifies the total included angle of the groove between parts joined by a groove
weld in the secondary side. The groove angle is also placed inside the weld symbol
and is given in degrees.

IJWeldingSymbol::PrimarySideNumberOfWelds

Specifies the number of welds on the arrow side. This property is valid only for intermittent
welds.

IJWeldingSymbol::SecondarySideNumberOfWelds

Specifies the number of welds on the other side. This property is valid only for intermittent
welds.

IJWeldingSymbol::PrimarySideActualLegLength

Specifies the leg length of a fillet weld from the primary side. This property is
valid only for fillet welds.

IJWeldingSymbol::SecondarySideActualLegLength

Specifies the leg length of a fillet weld from the secondary side. This property is
valid only for fillet welds.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Welded Beam Attachment Bolt - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306813?contentId=KVGBMM7BGilN9CtENINTMA)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.S3DWBABolt  
Part Name: Welded Beam Attachment Bolt  
Part Description: Welded Beam Attachment Bolt SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EtRdSr4NokssWZevtA2qRQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f6663c98aa8f4ac7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EtRdSr4NokssWZevtA2qRQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Welded Beam Attachment Bolt SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign combined with a tool, suggesting an option for adding or editing: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Beam Attachments > Welded Beam Attachment Bolt/Pin
   - Eye Connection as shown below.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nGCu7Bj8btkBeZFPapyvrw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8dd44cd00379a5bd)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nGCu7Bj8btkBeZFPapyvrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image presents a technical diagram showcasing a three-dimensional object, likely a mechanical component. On the left side, there is a front view of the component illustrating a surface and a bolt or pin hole marked at specific locations. The right side features a top view of the same component, depicting its orientation with respect to the three-dimensional axes: X, Y, and Z. The Z axis points upwards, suggesting it is the vertical dimension, while the X axis is horizontal. This illustration is useful in engineering or design contexts to communicate how the part is oriented and how it connects to other components through the bolt or pin hole. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~0rYtmabFCgAeuoe91tmRA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~0rYtmabFCgAeuoe91tmRA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Part Selection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306818?contentId=mzCZeYbJI~s6C0YXVjfN~w)
These properties are used for the part selection rule. They are not used for creating
graphics. You must enter the values when the part needs to be selected by the part
selection rule.


None:  For these properties, the default unit of distance is mm. Specify in at the end of the dimensional value to use inches (for example 10in).

IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of rod fittings that attach to the welded beam attachment.
This value is used by part selection rules for choosing the correct welded beam attachment
part.

IJUAhsSize::Size

Specifies the size of the strut for the part selection rule. This property is optional.
The value is used only when the part selection rule is not based on the rod diameter,
for example, struts or restraint end connections.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Sides Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306820?contentId=lMaV~niiX20kk3dKeuiTAg)
Specify the attributes of the two vertical side plates of the welded beam attachment.
Both side plates must be included.


None:  For these properties, the default unit of distance is mm. Specify in at the end of the dimensional value to use inches (for example 10in).

IJUAhsGap1::Gap1

Specifies the inside gap between the two side plates. The value can be zero but cannot
be negative.


Image:[Image-Analysis: The image depicts a schematic representation of a mechanical or electrical setup, likely showcasing a control mechanism for two distinct components. On the left side, there is a diagram of what appears to be a valve or a similar device with a vertical orientation and a visible actuator with a red dot indicating a control point. Below this component, there is a horizontal layout, suggesting a base or support structure. On the right side, there is another component that resembles a reservoir or a container with a circular element, again marked with a red dot. This design might indicate a connection between the two components, possibly involving flow direction or control signals. The red dots throughout the diagram may signify points of operation or activation that are crucial for the system’s functionality, highlighting their importance in controlling the flow or action within the setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fXCbYRk_78~CsKvXPgkc_Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fXCbYRk_78~CsKvXPgkc_Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the two side plates. The value must be positive.


Image:[Image-Analysis: The image depicts a simple schematic representation of an electrical circuit or a control system, consisting of two distinct vertical sections. The section on the left shows a rectangular block with vertical and horizontal lines, indicating components such as switches or current flow controllers. There’s a small rectangular component with a red dot, suggesting a part that could be a switch or an indicator light. The section on the right features a similar rectangular block but with an added circular indicator, again marked by a red dot that could represent a button or another type of indicator. The red dots likely signify points of interaction, control, or monitoring within the circuit. The overall layout suggests a focus on the organization of components and their functions in the system being depicted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QOmHRKvEujFPOYa3zaw24g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QOmHRKvEujFPOYa3zaw24g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the total height of the side plates, including the base plate. The value
must be positive.


Image:[Image-Analysis: The image shows a diagram with two vertical sections. On the left side, there is a vertical arrangement of rectangular shapes representing units with two red dots, possibly indicating specific components or interaction points. The right side features a similar vertical rectangle with a circle at the bottom and a red dot inside it, which suggests a connection or relationship between these rectangles and the components in the right section. There are directional arrows indicating movement or flow between the two sections, suggesting they are related or part of a system that needs to be examined together for functional understanding. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AwJ94Q7Z2K0XwnMezjHWkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AwJ94Q7Z2K0XwnMezjHWkg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the width of the side plates. The value must be positive.


Image:[Image-Analysis: The image shows two different structures or configurations that are likely related to mechanical or engineering elements. On the left, there is a vertical alignment of parts that appears to be a type of clamp or mount, with prominent red indicators showing positions or adjustments. The part on the right is more compact and features a circular component, which could indicate a pivot or connection point. In both configurations, the red marks suggest importance in positioning or operational settings. The arrows at the bottom imply movement or adjustment options, highlighting a connection between both configurations where adjustments can be made for different applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBvkORPndS6vheFd8KFKlg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBvkORPndS6vheFd8KFKlg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the left-to-right offset of the side plates from the bolt center. This value
is used when the welded beam attachment bolt part is used for non-symmetrical beam
attachments. The edge of the side plates will be located at the specified distance
from the bolt centerline. The value must be positive. If the value is set to zero,
the side plates are centered.


Image:[Image-Analysis: The image consists of two primary diagrams. On the left, there is a schematic representation of a mechanical device, possibly a lever or a slide with labeled points at the top and a highlighted point at the bottom. This part often indicates attachment points or pivot locations. The right side illustrates a linear movement, marked by arrows indicating direction, lateral movement capabilities, and a circular section with a labeled point in the center, which might represent a fulcrum or rotational axis. The presence of arrows and highlighted points indicates the function and interaction between these components, displaying how movement is initiated and controlled in the mechanism. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/od2Yj5T9PZ7_9Q1wt6a4vg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/od2Yj5T9PZ7_9Q1wt6a4vg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Base Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306827?contentId=~JYtSvHyizDz2SBhjyGPVw)
These properties specify the attributes of the horizontal base plate of the welded
beam attachment which will be attached to the existing structure. The base plate must
be included.


None:  For these properties, the default unit of distance is mm. Specify in at the end of the dimensional value to use inches (for example 10in).

IJUAhsWidth2::Width2

Specifies the width of the base. The value must be positive. If the value is set to
zero, the Width1 value will be used by the software.


Image:[Image-Analysis: The image depicts two vertical boxes, each representing a different design or component. On the left is a rectangular box with a grid layout. It consists of three main sections: two smaller compartments at the base and a larger section above, all enclosed within the outer box that has a red dot marker on the top. The right box is a narrow, taller structure, similar in design, but with a round opening at the bottom and a red dot marker located at the top. Both boxes are aligned vertically with a dashed line indicating a division or relationship between them, possibly illustrating a comparison or a stacking arrangement. The red dots may serve as indicators or buttons on both designs. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dYLOz2RcLThWlfLYLgxO1A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dYLOz2RcLThWlfLYLgxO1A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the length of the base. The value must be positive. If the value is set
to zero, then the software sets the value by calculating Gap1 + 2 x Thickness1.


Image:[Image-Analysis: The image depicts two sets of geometric shapes and measurements. On the left side, there are rectangular boxes with red dots indicating specific points of interest on the structures. One of the boxes is wider and has two smaller boxes beneath it, suggesting a hierarchical relationship between the elements; the larger box might represent a main or overarching structure while the smaller boxes are sub-components. There are arrows above indicating the width measurement of the larger box, giving a visual representation of length. On the right side, there is a single rectangular shape with a circular element at the bottom also marked with a red dot, possibly indicating a different structural form or a base component related to the left side. This separation indicates different functionalities or categories of shapes, suggesting a comparison or contrasting of cell structures or components in a larger system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Su~Kv5G2Mcf5Cia8gkxCIA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Su~Kv5G2Mcf5Cia8gkxCIA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the base. The value must be positive. If the value is set
to zero, then the Thickness1 value will be used by the software.


Image:[Image-Analysis: The image depicts two mechanical or engineering components, likely representing a type of machine or assembly. The left component has a rectangular shape with a vertical orientation, featuring a detailed internal structure that hints at its function, potentially relating to mechanical movement or support. There are small red dots indicating points of interest or attachment on both components. The right component appears to have a cylindrical shape with a circular base and also includes a red dot, possibly representing a connection point or an interface with another part. Arrows are indicating movement or force direction. This suggests a dynamic relationship between the two components, likely involving motion transfer in an engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XSeO~tiOOIvdPtokpuxPcg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XSeO~tiOOIvdPtokpuxPcg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset2::Offset2

Specifies the left-to-right offset of the base from the bolt center. The value must
be positive. The edge of the base will be located the specified distance from the
bolt centerline. If the value is set to zero, the base plate will be centered. This
value is used when the welded beam attachment bolt part is used for non-symmetrical
beam attachments.


Image:[Image-Analysis: The image illustrates two distinct mechanical systems. On the left, there is a depiction of a clamp or vice mechanism, which consists of two parallel plates that can be tightened together, typically used to hold objects securely in place. The red symbols indicate points of adjustment or pressure. On the right, a different mechanism is displayed, possibly a type of lever or a mechanical linkage system. It features a horizontal rod connected to a pivot point, allowing for rotational movement. The circular symbol with a red dot may represent a movable or adjustable part in this mechanism. The two systems are connected through their common function of managing and directing mechanical force, highlighting their importance in various engineering applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VzT9easmRGU2dZ3rrqYltg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VzT9easmRGU2dZ3rrqYltg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap2::Gap2

Specifies the inside gap between the two side plates. If the value is set to zero,
the wings will not be drawn.


Image:[Image-Analysis: The image depicts two vertical structures resembling lockers or storage units. On the left side, there are two open locker-like compartments, with a red dot inside the top compartment indicating they are empty. The right side shows a single vertical structure which is also a locker with a red dot indicating an object is present inside, and a circular graphic at the bottom. The presence of the red dots suggests a connection or distinction, potentially indicating that the lockers on the left side are inactive or empty, while the one on the right is active or occupied. The overall arrangement of these structures might imply a comparison between them, highlighting differences in their status or function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8yog7ebwXm4qVvXcUdIqxQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8yog7ebwXm4qVvXcUdIqxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Concrete Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306834?contentId=rW_36IqhHwnHK1n5~~fHAw)
Specify the attributes of the concrete attachment plate. Concrete attachment is an
optional geometry. These properties are also optional. You must enter values only
when the concrete attachment plate is needed.


None:  For these properties, the default unit of distance is mm. Specify in at the end of the dimensional value to use inches (for example 10in).

IJUAhsWidth3::Width3

Specifies the width of the plate. If the value is set to zero or negative, the plate
will not be drawn.


Image:[Image-Analysis: The image depicts two types of clamps or fixtures. On the left side, a more complex clamp design is shown with multiple parts, which includes an adjustable mechanism indicated by the red dots. This clamp is designed for a more versatile range of applications, allowing for different sizes and shapes to be secured in place. The right side shows a simpler clamp design, which appears to be used for holding items with a single vertical post and a circular base, also indicated by the red dots. Both clamps are illustrated with side profiles to indicate how they may work, with arrows showing movement or adjustment features. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UQcUUtZz_KluiK8ukSbsrg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UQcUUtZz_KluiK8ukSbsrg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3

Specifies the length of the plate. If the value is set to zero or negative, the plate
will not be drawn.


Image:[Image-Analysis: The image shows technical diagrams of a mechanical component, likely a type of clamp or bracket system used in engineering. On the left, there are two different configurations or views of the component. The first view shows a side view with horizontal arrows indicating a distance measurement, which could represent the adjustment range or size of the clamps. There are red dots that might indicate points of application or attachment for bolts or screws. The lower part features a broader base with colored indicators, possibly signifying the placement of fasteners. The right side displays a top view of another configuration of the component, emphasizing the vertical structure and its circular attachment point indicated by the red dot. The overall purpose of these diagrams typically serves to demonstrate the utility and fitting of the component in mechanical applications, showing how it can clamp or hold materials together. Additionally, the use of colors and arrows aids in guiding the user in understanding where specific connections are made and necessary measurements taken. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GV5AgDOv5AgYfoNOGAJoPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GV5AgDOv5AgYfoNOGAJoPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the plate. If the value is set to zero, the plate will
not be drawn. If a positive value is set, then the inside face of the plate will be
on the outside face of the base. If a negative value is set, then the outside face
of the plate will be on the outside face of the base, so the plate will be embedded
into the base. The surface port will always be located on the outward-most face of
the plate or base.


Image:[Image-Analysis: The image depicts a mechanical diagram or schematic that illustrates two different structures which appear to have parts that can be adjusted or moved. On the left side, there is a structure with labeled red dots potentially indicating points of interaction or movement, such as joints or connection points. The left structure consists of a rectangular base from which vertical components rise, indicating a form of assembly or machine design. The right side mirrors the left in terms of design, representing a similar mechanical device. The diagram typically represents a comparison or contrast between these two devices or parts, highlighting how they may function in relation to each other or how they vary in design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LsWaodtmWTK7_svX0ZsOkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LsWaodtmWTK7_svX0ZsOkg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset3::Offset3

Specifies the left-to-right offset of the plate from the bolt center. If the value
is set to zero, the plate will be centered. If a positive value is set, then the edge
of the plate will be located the specified distance from the bolt centerline. This
value is used when the welded beam attachment bolt part is used for non-symmetrical
beam attachments.


Image:[Image-Analysis: The image shows two technical diagrams related to a mechanical component. On the left side, there's a depiction of a part that resembles a fixture or a clamp, identified with red dots, possibly indicating important points for measurement or adjustment. The right side illustrates a side view of another mechanical element with a similar red dot to signify a critical feature. The arrows in the top section suggest a range of movement or adjustment in the component's operation. Overall, these diagrams represent how certain parts interact functionally, with the emphasis on specific points of interest in adjusting or assessing the components for performance. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y4Bp04HqOuXP2ASIsVdYNw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y4Bp04HqOuXP2ASIsVdYNw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin/Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306993?contentId=WPLrVufcw_ES5~aLSzrr3g)
Specify bolt/pin properties of the welded beam attachment. You must enter these values
to set the pin or bolt size and to set the port location.


None: 

* For these properties, the default unit of distance is mm. Specify in at the end of the dimensional value to use inches (for example 10in).
* If Pin1diameter and Pin1Length are set to zero, then the pin or bolt will not be drawn. If that is the case, then
  the port needs to be changed to an appropriate hole type in the XLS and a separate
  bolt or pin will need to be modeled.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_sDDMPA8l117YXip5h7DMA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0e207b6f7b9180dd)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_sDDMPA8l117YXip5h7DMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt or pin. Use this property as the connection diameter
from AIR when you join the welded beam attachment bolt to an eye nut. An AIR that
joins a welded beam attachment bolt to an eye nut will read the Pin1Diameter property from the welded beam attachment bolt and pass the value into the PinDiameter prompt of the eye nut. If the value is set to zero, then the pin will not be drawn.


Image:[Image-Analysis: The image depicts a mechanical apparatus, likely representing a simple version of a hydraulic system or a control mechanism. On the left side, there are two rectangular boxes that could symbolize hydraulic cylinders with a series of ports at the bottom for fluid entry/exit. The small red dots may denote pressure input locations. The central arrow indicates the direction of force or movement. The right side features a similar cylinder with a circular indicator, suggesting it might be displaying pressure levels or status. The arrangement indicates a relationship where the left apparatus could control the pressure or flow leading to the right apparatus for some operational purpose. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_MBu0nb99YVtgxhnM5gAgQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_MBu0nb99YVtgxhnM5gAgQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the bolt or pin. If the value is set to zero, then the pin
will not be drawn. The length will always be centered on the port location.


Image:[Image-Analysis: The image consists of two main diagrams that appear to depict mechanical systems with emphasis on their components. On the left, there is a rectangular structure with vertical and horizontal elements, suggesting a framework or a machine design. It includes red dots, likely indicating positions for adjustment or connection points. The diagram includes small boxes representing parts of the machine that may contribute to its function. On the right, there is a simpler depiction of another system, presumably representing a container or a part of a machine, with an accompanying red dot indicating a focal point of operation possibly related to the system's mechanism. The elements presented may function together in a larger mechanical context, where the left side could be a base or support structure and the right side a mechanism or control unit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ozCly4DNsqVPaX6ZlhZPqw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ozCly4DNsqVPaX6ZlhZPqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the height of the bolt centerline, relative to the top of the base. This
value determines the location of the bolt graphic and the location of the port.


Image:[Image-Analysis: The image depicts a simple schematic of a control mechanism involving red dots and lines, possibly illustrating a switching or signaling system. On the left side, there is a set of boxes with red indicators at different points, suggesting that they might represent inputs or outputs in a circuit. The arrangement of thick and thin lines indicates connections or pathways of information or power. The right side features a similar structure with clear directional indicators, implying a relationship between the two sections. Moreover, the presence of arrows indicates movement or flow, which is essential for understanding the functionality of the system being illustrated. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KV_Qmhj~wx0gOC8t4ORqZg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KV_Qmhj~wx0gOC8t4ORqZg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape Top Left/Right Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306998?contentId=cAh4Slxyezw3T_Bpk19z~w)
These properties specify the corner attributes for the side plates. These properties
are optional. You must enter these values when these various corner shapes of side
plates are needed.

Plate shape functions are used for the side plates for top left and top right shape
settings. Because the bottom of the sides are attached to the base, when you flip
the graphic over, the top is the edge farthest away from the base as shown in the
following example.


Image:[Image-Analysis: The image illustrates a structural relationship between two cylindrical objects, each represented as a vertical rectangle. The left rectangle has a red square and a circle, indicating two distinct points of interest at different positions. The left structure is labeled with a red square at the top center, and another red square at the bottom. The right rectangle features a similar red square at the bottom, but also has a circle at the top. There’s an arching arrow connecting the two shapes, which suggests a movement or a relationship between their points. The labels "Top", "Left", and "Right" around the arrow might indicate directional references regarding the positions of the red squares and circles. Overall, this visual seems to describe how one shape can interact with another, emphasizing key areas of interest in the details of their structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/shjzY__1WKY8hoCiCKeJFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/shjzY__1WKY8hoCiCKeJFw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1GTdFIj20JGNvwhFxTxTRw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ec088b5751b9828a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1GTdFIj20JGNvwhFxTxTRw-_PVFQNoCl4XmjAxWO0f7XQ/content)

The following types of corner for top left or top right shapes are supported:

* Rectangular notch corner
* Angled notch
* Round notch (Convex)
* Round (Concave)

You need to select a corner type and enter the values accordingly. For information
about the properties, see the following topics:

* [Rectangular Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/i1wFT1LPNd6uaLi4uJ7TPA)
* [Angled Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/xlbY6lPqkivZiNfAUwMfNA)
* [Rounded Notch Corner (Convex)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/rrDa~b4FQoekBpLff_X3Qw)
* [Round Corner (Concave)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/GkgMm0vafTQG4l3YXPFPmw)


None:  Descriptions of the Shape Top Left properties are the same as those for Shape Top Right, but the difference is in the corners as shown below.

|  |  |
| --- | --- |
| Shape Top Left | Shape Top Right |
| [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4F2VDIIy4~VMnzjASBoMCg-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y5F1~XMCx7ByVnq3532mPg-_PVFQNoCl4XmjAxWO0f7XQ/content) |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rectangular Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307022?contentId=JjF47a4_OhhqZ0kPZBB1Eg)
IJUAhsTLCorner::TLCornerType - Specifies the corner type. Enter codelist value 1 for this corner type. Valid codes
are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet.

Codelist hsCornerShape 1 – Rectangular Notch


look for an icon that resembles a blank document with a folded top corner: 

IJUAhsTLCorner::TLCornerX

Specifies the horizontal size of the rectangular notch. The value must be positive
and less than the Width1 value.


Image:[Image-Analysis: The image depicts a symbol that represents a "TL Corner" (Top Left Corner) in relation to a graphical or user interface layout. It consists of arrows pointing towards a central vertical line, which indicates that the corner can adapt or change based on some dynamic element. The corner itself is outlined and seems to indicate a designated area or frame where content may be placed or adjusted. The reference to "X" after the label suggests there might be additional details or functionalities related to this corner, possibly indicating a close or exit option. It visually conveys how content can be organized or aligned within a graphical interface. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BFcjUXt53QBcmvYtGUyQVw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BFcjUXt53QBcmvYtGUyQVw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerY

Specifies the vertical size of the rectangular notch. The value must be positive and
less than the Height1-Thickness1 value.


Image:[Image-Analysis: The image represents a simple graphical illustration of a corner layout in a diagram or interface labeled "TLCornerY." It indicates a top-left corner positioning, suggested by the upward arrow and horizontal line. The diagram is likely used in a context where graphical representation of layout alignment is necessary, showing how different components may fit together in that corner. The shape on the right represents a boundary or a container that may be positioned in relation to the top-left corner described. The upward arrows can suggest movement or orientation, emphasizing the top part of the layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/plH8rSYt1m6a46QZX37HEA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/plH8rSYt1m6a46QZX37HEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerRadius

This value is ignored.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Angled Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307023?contentId=9o5cmtivGvNVhJmL~Y7m6A)
IJUAhsTLCorner::TLCornerType

Specifies the corner type. Enter codelist value 2, 3, 4, or 5 for this corner type.
Valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet.

Codelist hsCornerShape 2 – Angled Notch


icon description of a document or paper sheet with a slightly torn edge at the top: 

IJUAhsTLCorner::TLCornerX

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Codelist Value | 2 | 3 | 4 | 5 |
| Corner Type | XY Chamfer | XY Edges | X with Angle | Y with Angle |
| X | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PFphWB3fk0ItoGR4100P3A-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3VAdHzdYMLMBEpOw21wbAQ-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YjFqc7kbGPCysJbWxHn_VQ-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8hh4_ig1KP15Tg4Ou~734A-_PVFQNoCl4XmjAxWO0f7XQ/content) |
| Description of X | Size of chamfer | Size of straight edge | Size of chamfer | Angle from vertical |
| Limits on X | X > 0 | X >= 0 | X > 0 | X > 0 (angle in degrees) |
| X <= Width1 | X < Width1 | X <= Width1 | Calculated X <= Width1 |

IJUAhsTLCorner::TLCornerY

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Codelist Value | 2 | 3 | 4 | 5 |
| Corner Type | XY Chamfer | XY Edges | X with Angle | Y with Angle |
| Y | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yLq3NoeoAk9IZG3MPsqtHQ-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pWbS8cc9OFavLDQdQGmq1w-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cC09dR2lnuc3BJXFLt6Hxw-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YkfTr8ZlVkEuTPumc7YqFQ-_PVFQNoCl4XmjAxWO0f7XQ/content) |
| Description of Y | Size of chamfer | Size of straight edge | Angle from vertical | Size of chamfer |
| Limits on Y | Y > 0 | Y >= 0 | Y > 0 (angle in degrees) | Y > 0 |
| Y <= Length | Y <  Length | Calculated Y <= Length | Y <= Length |

IJUAhsTLCorner::TLCornerRadius

Specifies the radius of the angled notch shape. Enter this value when the two outside
points of the notch need to be rounded using this radius. You must set the radius
small enough to allow tangents on top, left, and slanted face. If this value is set
to zero, then a sharp corner will be drawn by the software. The value cannot be negative.


Image:[Image-Analysis: The image shows two tablets or stone-like structures that resemble the Ten Commandments, typical in religious imagery, specifically in Judeo-Christian contexts. Each tablet features two sets of elements denoted by the letters "X" and "Y" arranged in a way that suggests either the commandments or laws associated with these letters. The structure of the tablets indicates a hierarchy or distinction between the commandments or laws represented, as well as their divided nature, which is common in their presentation to signify different aspects or categories of rules or principles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lkejH4aCq9fAjoXOrgypYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lkejH4aCq9fAjoXOrgypYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rounded Notch Corner (Convex) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307024?contentId=3tZbF8Q~_oSocDsH6TIfYg)
IJUAhsTLCorner::TLCornerType

Specifies the corner type. Enter codelist value 6 for this corner type. Valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet.


look for an icon that resembles a blank sheet of paper or a document with a corner cut out: 

IJUAhsTLCorner::TLCornerX

Specifies the horizontal offset of the round notch center point. You cannot offset
the round notch off the plate in either direction. If you want both corners to be
round notch as shown below, then the value must be less than Width1 divided by 2.


icon-description of a shape resembling a rectangle with a curved top edge, possibly representing a header or a banner: 

If this value is set to zero, then the notch center will be aligned with the corner
point. The notch shape will be a quarter-circle arc.

X = 0, Zero Offset


icon that resembles a document or note with a plus sign, indicating an option to add or create something: 

If a positive value is set, then the software will move the center point into the
plate horizontally. This adds a flat landing in addition to the quarter-circle arc.

X > 0, Positive Offset


Image:[Image-Analysis: The image depicts a schematic or diagram that represents a valve. The valve appears to be in a closed position, as indicated by the lines and arrows showing the flow direction. There are arrows pointing towards the valve from both left and right, suggesting that it controls the flow of a fluid or gas in a specific direction. The rounded part of the valve signifies the opening where the fluid or gas can pass through when the valve is opened. Overall, this image illustrates the key features and functionality of a valve in a fluid system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kIdKyIGRPqM7gqauMpSpPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kIdKyIGRPqM7gqauMpSpPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

If a negative value is set, then the software will move the center point away from
the plate horizontally. This will reduce the sweep angle of the notch shape so it
will be less than a quarter-circle and the joint with one edge is no longer perpendicular.

X < 0, Negative Offset


Image:[Image-Analysis: The image depicts a simple drawing of a rectangle with a cut or notch at the top, possibly representing a sheet of paper or a document. There are arrows on both sides of the image, indicating movement or placement towards the center. The intersection of the vertical and horizontal lines suggests a grid or guide for alignment. The notch in the rectangle could signify a specific way to orient or present the document, like how a tab would function on a folder. The plus sign might indicate addition or focus, but its specific role isn’t clear without additional context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kNi~ztWptgbkX5M1CzPILw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kNi~ztWptgbkX5M1CzPILw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerY

Specifies the vertical offset of the round notch center point. You cannot offset the
round notch off the plate in either direction.

If this value is set to zero, then the notch center will be aligned with the corner
point. The notch shape will be a quarter-circle arc.

Y = 0, Zero Offset


icon-description is a simple outline of a document or notepad with a '+' sign, suggesting an action of adding or creating something new: 

If a positive value is set, then the software will move the center point into the
plate vertically. This adds a flat landing in addition to the quarter-circle arc.

Y > 0, Positive Offset


Image:[Image-Analysis: The image depicts a basic schematic representation of a capacitor in electrical engineering. The capacitor is shown symbolically with two parallel lines indicating the plates of the capacitor and a curved line representing the dielectric or insulating material between them. The '+' sign indicates the positive terminal, while the '-' sign indicates the negative terminal of the capacitor. This symbol is commonly used in circuit diagrams to represent capacitors, which store electrical energy in an electric field. The arrows pointing towards the capacitor suggest the flow of charge, indicating how capacitors interact with electric circuits by charging and discharging. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ndeyMO9NAWdLVDUHoPG6jQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ndeyMO9NAWdLVDUHoPG6jQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

If a negative value is set, then the software will move the center point away from
the plate vertically. This will reduce the sweep angle of the notch shape, so it will
be less than a quarter-circle and the joint with one edge is no longer perpendicular.

Y < 0, Negative Offset


icon-description: looks like a diagram with arrows indicating movement, possibly representing a flow or process of addition or augmenting within a bounded area (illustrated with a square): 

IJUAhsTLCorner::TLCornerRadius

Specifies the radius of the round notch shape.

If the radius is needed in X + direction, the value must be greater than zero and
less than that of available Width1.

If the radius is needed in Y + direction, the value must be greater than zero and
less than that of available Height1-Thickness1.

If this value is set to zero, then the software will create a sharp corner edge.


Image:[Image-Analysis: The image depicts a simple diagram illustrating a process of folding or turning a sheet or paper. It features a rectangular shape with a corner turned over, indicated by an arrow. There is a plus sign symbol, suggesting a possible action of adding or creating something as a result of the folding process. This kind of illustration is often used in contexts such as origami, document folding, or design techniques, highlighting how a flat object can be transformed into a different form by bending a corner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiDgsIRtGHZBebeMBvxeSw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiDgsIRtGHZBebeMBvxeSw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Round Corner (Concave) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307032?contentId=fsHzl2beH157EKzx1OKH9Q)
IJUAhsTLCorner::TLCornerType

Specifies the corner type. Enter codelist value 7 for this corner type. Valid codes
are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet.

Codelist hsCornerShape 7- Rounded Corner (Convex)


look for an icon that resembles a rounded rectangle or a corner cut-out: 

IJUAhsTLCorner::TLCornerX

Specifies the horizontal offset of the round notch center point. The value must be
negative. If a positive value is entered, the software will use the equivalent negative
value.

If this value is set to zero, then the rounded corner will be tangent with each edge.
The notch shape will be a quarter-circle arc.

X = 0, Zero Offset


look for an icon that resembles a plus sign on a vertical bar with rounded edges, often associated with adding or creating new items: 

If a negative value is set, then the software will move the center point away from
the plate horizontally. This will reduce the sweep angle of the notch shape, so it
will be less than a quarter-circle and the joint with one edge is no longer perpendicular.

X < 0, Negative Offset


Image:[Image-Analysis: The image shows a diagram with arrows pointing inward toward what appears to be a rectangular shape with a rounded corner. This likely represents a squeeze or compress operation, where the arrows indicate the direction of compression towards the center of the rectangle. The crossed lines in the center suggest a possible constraint or pause in the process, highlighting the importance of a specific point of action. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m1EfBkyzmqVGuF2HNvDmag-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m1EfBkyzmqVGuF2HNvDmag-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerY

Specifies the vertical offset of the round notch center point. The value must be negative.
If a positive value is entered, the software will use the equivalent negative value.

If this value is set to zero, then the rounded corner will be tangent with each edge.
The notch shape will be a quarter-circle arc.

Y = 0, Zero Offset


icon-description of a plus sign inside a rounded rectangle, often represents addition or an action to create something new: 

If a negative value is set, then the software will move the center point away from
the plate vertically. This will reduce the sweep angle of the notch shape, so it will
be less than a quarter-circle and the joint with one edge is no longer perpendicular.

Y < 0, Negative Offset


Image:[Image-Analysis: The image illustrates a simple electrical circuit symbol for a capacitor, which is represented by a pair of parallel lines. The left side depicts a rectangular shape that often symbolizes a capacitor's shell or body. The configuration indicates that the capacitor is connected in a circuit where it can store and release electrical energy. The arrows point to a vertical line with a variable symbol, possibly indicating changes in voltage or charge. Overall, this symbol helps in understanding the positioning of a capacitor within an electrical schematic. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MRZu5VG8yT1mjZP4E6l0mA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MRZu5VG8yT1mjZP4E6l0mA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerRadius

Specifies the radius of the round notch shape.

If the radius is needed in X + direction, the value must be greater than zero but
less than that of available Width1.

If the radius is needed in Y + direction, the value must be greater than zero but
less than that of available Height1-Thickness1.

If this value is set to zero, the software will create a sharp corner edge.


look for an icon that resembles a sheet of paper with a folded corner and an arrow pointing towards the paper: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307001?contentId=_Q1JE2DgtH1kJ2cO2phbmw)
These properties specify the port attributes.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yZK~fpPJ0HcJP~1mwSO30g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3be0a8de4878ded1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yZK~fpPJ0HcJP~1mwSO30g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Welded Beam Attachment Bolt


Image:[Image-Analysis: The image consists of two diagrams representing a structural component, likely in the context of engineering or construction. The diagram on the left illustrates a structure that has several vertical elements and includes a notation for a bolt, pin, or hole indicated by a red square. The structure is labeled as "Structure". The right diagram appears to represent a close-up or a different orientation of a vertical component of this structure, also indicating the positions of the coordinate axes, X and Z. The arrows show the upward and downward orientations of these axes. The diagrams likely serve to explain how certain elements, like bolts or pins, are situated in the structure and how to reference them directionally in relation to the coordinate system depicted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/klx8FqLETO63YKsC3_BUlg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/klx8FqLETO63YKsC3_BUlg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Structure

Location: (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - Steel | N/A - Use 0 | -9999 | 9999 |

Port 2 - Bolt/Pin/Hole

Location: (0, 0, -Height2-Thickness3)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1005 – Bolt / Pin  1005 – Hole for Bolt or Pin | Bolt/Pin/Hole diameter | 0 | Gap1 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Welded Beam Attachment Hole - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307758?contentId=d1kG9FlRFn_uw76p72QpGA)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.S3DWBAHole  
Part Name: WBA Hole  
Part Description: WBA Hole SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B2FV5YCnu9dcNShDAuC1Eg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=77aac4785b577166)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B2FV5YCnu9dcNShDAuC1Eg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample WBA Hole SmartPart delivered with the catalog:

1. Click Tasks > Hangers and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity: , and then select the design support.
4. In the Select Part dialog, select a part from Parts > SmartParts > S3D Standard > Beam Attachments > WeldedBeamAttachement-Inverted-Rod
   Connection in Hole as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical structure representing various components categorized under "SmartParts." At the top level, there are main categories such as "S3D Standard" and "Beam Attachments." Under "Beam Attachments," there are subcategories for different types of beam connections, including "Welded Beam Attachment Bolt/Pin - Eye Connection" and other attachment methods like "Clevices," "Pipe Clamps," and so on. The highlighted entry indicates a specific type of welded beam attachment known as "Inverted: Rod Connection in Hole," showcasing its importance or relevance within this organizational structure. This format helps users navigate through different attachment options related to beams in a systematic manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h3EWmfKZIPKcnVO06gTn3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/h3EWmfKZIPKcnVO06gTn3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image shows a technical drawing of a cylindrical object with a hole, displaying its dimensions in a three-dimensional coordinate system. On the left side, there are two vertical rectangular shapes with a dashed line running between them, indicating a context where they possibly relate to each other or are part of a larger assembly. The terms "Surface" and "Hole" are labeled, giving specific features of the object: the "Surface" represents the outer area of the cylinder, while the "Hole" indicates an opening or cavity within it. On the right side, a cylindrical representation is shown alongside a 3D coordinate system, indicating the directions of the X and Z axes, which are marked in red. This setup is often used in engineering or design contexts to clarify the orientation and dimensions of components in three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~sRoTBXwo1YrSVUqUFDJLA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~sRoTBXwo1YrSVUqUFDJLA-_PVFQNoCl4XmjAxWO0f7XQ/content)

When using the Place Part command, the WBA Hole shows up in the most frequently used orientation with the above
coordinate system.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [WBA Hole General Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307777?contentId=LbUdvstas0pmM45lqKlMSQ)
These properties specify the general properties for the WBA Hole that are used for
the part selection, WBA Hole configuration, and the port location.


Image:[Image-Analysis: The image depicts a table titled "WBA Hole General." This table contains four columns that list various attributes related to a "WBA Hole Config." The columns are labeled as follows: 1) "IUJAhsRodDiameter::RodDiameter," which likely pertains to the diameter of a rod used in the WBA hole; 2) "IUJAhsSize::Size," indicating the size of the WBA hole; 3) "IUJAhsWBA-HoleConfig::WBAHoleConfig," suggesting a configuration related to WBA holes; and 4) "IUJAhsOffset::Offset," which appears to describe the offset measurements relevant to the WBA hole. Each entry in the columns is associated with specific attributes, implying their importance in defining the characteristics of the WBA holes in a structured manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jBhwoSvJeGQRlLmxCC6rEw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jBhwoSvJeGQRlLmxCC6rEw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodDiameter::RodDiameter

Enter the outside diameter of rod fittings that attach to the welded beam attachment.
This value is used for part selection rules for choosing a right welded-beam attachment
part and is not used for creating graphics.

IJUAhsSize::Size

Enter the size to be used for the part selection rule that is not using the RodDiameter. For example, C&P parts are based on size, not diameter. This value is not used for
creating graphics.

IJUAhsWBAHoleConfig::WBAHoleConfig

This codelisted value specifies whether the part is made from one continuous shape
or by separate plates. The value for this column is a codelist number, and valid codes
are listed in the HS\_S3DParts\_Codelist.xls workbook in the hsWBAHoleConfig sheet. The continuous option does not include the rod attachment. If a base plate
is added when continuous is being used, the base plate is not part of the continuous
graphic. It is a separate plate on top of the continuous graphic. The flat spot of
the WBA is 90% of Gap1.

1 = Continuous

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pQMzseMtyoV9ytIiGqxI1A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=de5e205d355da967)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pQMzseMtyoV9ytIiGqxI1A-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 = Plates

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ew7nV6SYhoo39rs4PDC1yQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=40f0ebde6431e68f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ew7nV6SYhoo39rs4PDC1yQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Enter the vertical offset of the hole port from the lowest edge of the WBA (Height1). If this value is set to zero, the hole port is flush with the lowest edge of the
WBA. Only positive values are acceptable.


Image:[Image-Analysis: The image depicts a basic diagram illustrating a mechanical system involving a moving mass. It shows a rectangular frame with two vertical lines on the sides, indicating boundaries. There are two marked red dots, which likely represent the positions of forces acting on the system. Below the rectangular frame, there’s a horizontal line that may represent a surface or baseline. The arrow pointing downwards suggests a force acting downwards, possibly indicating gravity or a weight being applied to the mass within the frame. Overall, this image seems to be demonstrating basic principles of mechanics involving forces and motion within a defined space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nsE6GCdrlpgqVqDgcn~OXg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nsE6GCdrlpgqVqDgcn~OXg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307852?contentId=oCBlKxfJGltqh9ibS8dUWQ)
These properties specify the two vertical side plate properties of the welded beam
attachment. Both side plates always need to be included.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lo5~UrlhGxnuclgFLj1azA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1a535d5447454359)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lo5~UrlhGxnuclgFLj1azA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Enter the inside gap between the two side plates. This value can be zero but not a
negative. If this value is set to zero, the sides are not drawn.


Image:[Image-Analysis: The image depicts a two-sided structure with arrows indicating horizontal measurement. It shows a vertical rectangle, possibly representing a freestanding device or object, with two smaller rectangles at the bottom, which could represent a base or supporting structure. There are red dots aligned vertically, indicating specific locations or points of interest. This illustration might be used in a context where dimensions are relevant, such as in construction, design, or engineering, to represent the space or clearance required for the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pE8RmSXF~xRixhIuW49eQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pE8RmSXF~xRixhIuW49eQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Enter the thickness of the two side plates. Only positive values are acceptable. If
this value is set to zero, the sides are not drawn.


Image:[Image-Analysis: The image depicts a basic schematic representation of a container (or tank) with a structure resembling an open top and two sides. It contains a couple of red dots, which might represent sensors or critical points of interest. There are also arrows present that indicate a flow direction, suggesting that something is moving into or out of the container. The design is minimalistic and seems aimed at conveying concepts related to fluid dynamics or container management. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gvUGRGrc_5azJuOfwBxn7Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gvUGRGrc_5azJuOfwBxn7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Enter the total height of the side plates, including the base plate. Only positive
values are acceptable. This value is the total height of the WBA Hole, not including
the height of the extra rod connection. If a base plate or top feature is included,
the height is included in Height1 (not added to it). Also, if the bottom plate is specified so that it overlaps the
side plates, the thickness is not added to Height1.


Image:[Image-Analysis: The image appears to show a technical diagram, likely representing some sort of mechanical or structural component. It includes two sections, the upper part and the lower part, which seem to depict different views or aspects of the same component. The upper section shows two vertical lines connected by arrows that suggest measurements, indicating the height of the component, while the lower section has horizontal lines with markers that might represent dimensions or structural supports. The red dots could serve as reference points for measurement or connection locations. Overall, the image conveys important spatial and dimensional information regarding the design of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vv7OllJXQhfyluXzafUmtA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vv7OllJXQhfyluXzafUmtA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Enter the width of the side plates. Only positive values are acceptable.


Image:[Image-Analysis: The image depicts two geometric shapes: on the left, there is an upright rectangular box, and on the right, there is a similar box oriented horizontally. Each box includes small red dots at different positions. The dots seem to indicate specific markings or points of interest within the shapes. The inclusion of arrows between the boxes suggests a comparison or alignment between the vertical and horizontal orientations, highlighting how the boxes are different in their arrangement but related in size. This suggests a context of geometry or measurement related to these shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SKhjfrt_A8PvZup3KoEP3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SKhjfrt_A8PvZup3KoEP3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset2::Offset2

Enter the front-to-back offset of side plates from the hole center. If this value
is set to zero, then the side, top, and bottom plates are centered. Only positive
values are acceptable. The edge of the side plate is located at a specified distance
from the hole centerline. This value is used when WBA Hole part is used for non-symmetrical
beam attachments.


Image:[Image-Analysis: The image depicts two tanks represented by rectangular outlines. Each tank has a red dot indicating a liquid level or a point of measurement within it. The left tank is labeled as "Tank A" and appears to be closed at the top, while the right tank is labeled as "Tank B" and has an inlet or outlet with arrows indicating movement or flow toward it. The dashed line separating the tanks suggests that they may be connected or part of a system that allows flow from one tank to the other. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1wrQjg6AReLwJnfkIkRiGw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1wrQjg6AReLwJnfkIkRiGw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307873?contentId=JpwO5OHnvu_MwLnSi88uJg)
These properties specify the horizontal bottom plate properties of the welded beam
attachment that has a rod hole. If Gap1 = 0, then side and bottom plates are not shown.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j8PLNZNkTKOUk2IUd~AMIw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c10604489ccf25cf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j8PLNZNkTKOUk2IUd~AMIw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Enter the width of the bottom plate. If the value is set to less than Width1, then Width1 is used.


Image:[Image-Analysis: The image shows a simple illustration comparing two arrangements of objects. On the left side, there are two structures with rectangular tops and a base. The first arrangement is taller and wider, while the second arrangement is shorter and narrower. Both have red dots, likely indicating points of interest or focus. On the right side, two additional illustrations are shown – the first a taller rectangle that is shaded or filled in gray, and the second one similar to the left, but appearing to highlight its width compared to its height. Overall, the image contrasts two sets of stacked rectangles, emphasizing their differing dimensions and possibly suggesting concepts of height vs. width or volume. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XZzFnV6hToICjbYVZYl8hQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XZzFnV6hToICjbYVZYl8hQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Enter the length of the bottom plate. If this value is set to less than Gap1, then Gap1 is used. If this value is set to greater than Gap1, then Thickness2 is subtracted from Height1 of the side plates, and the bottom plate is overlapped with the side plate.


Image:[Image-Analysis: The image shows two sets of structures, each consisting of a rectangular frame that appears to be open at the top. The frames are labeled with dotted lines indicating height (H1) and other measurements, along with small red dots positioned within the frames. The upper frame is aligned vertically while the lower frame is wider and aligned horizontally. The lower structure has arrows on each side indicating a possible motion or placement direction, suggesting that it could represent a dynamic system that involves height and width adjustments. The image seems to depict a comparison or relationship between two architectural or engineering elements based on their dimensions and orientations. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FpIf7D91eeUXA8IS7doG~A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FpIf7D91eeUXA8IS7doG~A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Enter the thickness of the bottom plate. Only positive values are acceptable. If this
value is set to zero, Thickness1 is used. This thickness is not added to Height1.


Image:[Image-Analysis: The image consists of two rectangular shapes that seem to represent a hydraulic press mechanism. Each rectangular structure is outlined with vertical sides and a horizontal base. Within each rectangle, there is a small red dot at the top and a red dot at the bottom, indicating the points where the force is applied or where pressure is exerted. Below the bottom rectangle, there is an arrow pointing downwards, which likely signifies the direction of pressure application in the hydraulic system. Overall, this illustrates how a hydraulic press compresses materials by exerting force in a downward direction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aD5j_ls4GOq15OFGbV~5zA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aD5j_ls4GOq15OFGbV~5zA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307879?contentId=r0wSjlLOC6HFL0e5CHb58g)
These properties specify the horizontal top plate properties of the welded beam attachment
that attaches to the structure. This is an optional plate and may not be needed. Enter
these values only if the plate is needed.

If you need continuous geometry, enter the same thickness as the rest of the attachment
for the top plate. When Gap1 = 0, the side and bottom plates are not shown.


Image:[Image-Analysis: The image is a diagram that displays a structured layout, likely representing a three-dimensional object or a data model with parameters for length, width, and thickness. At the top of the diagram, there is a label indicating the section named "Top". Below this label, there are three vertical columns. Each column contains identifiers followed by parameters: Width3, Length2, and Thickness3. These represent various dimensions related to a specific object or design. The hierarchical relationship suggests that these dimensions are attributes of a larger entity, with the potential for use in design or engineering contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9fa4Td4b~QNvIEbs9Nb1Uw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9fa4Td4b~QNvIEbs9Nb1Uw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Enter the width of the top plate. If this value is zero, then Width1 is used.


Image:[Image-Analysis: The image depicts two rectangular boxes (labeled as containers) stacked vertically. Each box has a red dot located in the center at the top and the bottom, which likely represents some kind of reference point or marker. The horizontal arrows indicate that the boxes can be adjusted or moved horizontally, suggesting flexibility in their position. The dashed lines near the bottom suggest that there may be a structural relationship between the top and bottom boxes, particularly in how they align or connect with one another. Overall, the image illustrates the concepts of adjustment and alignment between two stacked components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V7l8XcHR2uQ39sRGcTjZlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V7l8XcHR2uQ39sRGcTjZlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Enter the length of the top plate. If this value is negative, the top plate is not
shown. However, if this value is less than Gap1, the ears of the top plate are drawn inside the U. When the value is greater than
Gap1 plus two times the value of Thickness1, the top plate is drawn as ears.


Image:[Image-Analysis: The image presents a comparison of two dimensional relationships involving lengths and gaps. At the top, there is a rectangular box with a label "Length2 ≥ Gap1" indicating that the measurement of Length2 is greater than or equal to that of Gap1. Arrows are drawn to illustrate the spatial relationship between these elements. The bottom part features a broader structure with two vertical lines, suggesting that Gap1 exists between them. The red dots placed beneath these elements likely denote points of interest or reference within the measurements. Overall, the image seems to be illustrating the condition of spatial dimensions relating to gaps and lengths. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2EJ__fixDfwbCvHNrVYhLg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2EJ__fixDfwbCvHNrVYhLg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Enter the top plate thickness. Only positive values are acceptable. If this value
is zero, Thickness1 is used. This thickness is not added to Height1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Concrete Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307900?contentId=ymB7_6076gfvvImvzkdI2w)
These properties specify concrete attachment plate properties. Concrete attachment
is an optional geometry setting. Enter these values only when concrete attachment
plates are necessary.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7vi2LH5vHgAOAX_yGn0yzw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1affbc522db4f4e9)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7vi2LH5vHgAOAX_yGn0yzw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3

Enter the concrete plate length. If this value is zero or a negative, the concrete
plate is not drawn. However, if SimpShapeType is round, then Length3 is the diameter of the plate.


Image:[Image-Analysis: The image illustrates a basic diagram of a beam supported at both ends. It consists of a horizontal line representing the beam itself, and two vertical lines represent the supports at each end. The red dots indicate specific points of interest, possibly the locations of forces or supports. The arrows pointing outward at the top suggest a consideration of the span or width of the beam. Overall, this diagram is typically used in structural engineering to analyze the behavior of beams under load. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6x0DR6sRpaP9kRwGcYpwrA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6x0DR6sRpaP9kRwGcYpwrA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Enter the plate width. If this value is zero or negative, the concrete plate is not
drawn. If SimpShapeType is round, then Width4 is ignored.


Image:[Image-Analysis: The image depicts a simple diagram that illustrates a system involving a cylindrical object, likely representing a piston or similar component, situated between two arrows that indicate movement or force direction. Above the cylinder, there is a rectangular box, possibly denoting a chamber or a container for fluid or gas, with an indication of pressure or some other measurement shown by a red dot in between. The arrows at the top suggest that the system allows for expansion and contraction or the movement of substances in and out of the cylinder. The setup likely represents the mechanics of a hydraulic or pneumatic system where forces are applied and directed. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jXeL7sUXJsZXPBAXeAYRUw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jXeL7sUXJsZXPBAXeAYRUw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness4::Thickness4

Enter a positive value for the concrete plate thickness. If this value is zero, the
concrete plate is not drawn. The surface port is always located on the upper-most
face of the concrete, top, or side plates. This thickness value is not added to Height1.


Image:[Image-Analysis: The image depicts a basic schematic of a beam subjected to a downward force. The beam is shown as a horizontal line with supportive columns at both ends. There are red dots which likely indicate points of load application or support. The arrows pointing downward suggest a force acting on the beam, possibly due to weight or pressure. This representation generally illustrates basic principles of structural engineering, highlighting how forces interact with a beam structure and the need for support in maintaining structural integrity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4TnO~ipFyuOQyN3sn8FK~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4TnO~ipFyuOQyN3sn8FK~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset3::Offset3

Enter the left-to-right offset of the concrete plate from the hole center. If this
value is zero, the concrete plate is centered. If this value is positive, the plate
edge is located a specified distance from the hole centerline. This value is used
when WBA Hole part is used for non-symmetrical beam attachments.


Image:[Image-Analysis: The image depicts a mechanical setup showing a beam interacting with a structure. There is a horizontal arrow pointing left and right, typically indicating a force applied to the beam. The beam is shown above a grey block-like structure, which may represent a support or a pillar. A red square is highlighted, possibly indicating a point of interest such as a load application point or a reaction point on the beam or at the supports. The image suggests a scenario in physics or engineering where forces are applied to a beam supported by a structure and might be relevant to problems concerning equilibrium, bending, or structural analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j1esXosGFBmE~099wlwhHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j1esXosGFBmE~099wlwhHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSimpShapeType::SimpShapeType

Specifies the concrete plate graphic shape. The value for this column is a codelist
number; valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook in the hsSimpShapeType sheet. Enter the shortName of the codelist for readability in XLS.

1 - Round


Image:[Image-Analysis: The image depicts a circular shape with a square inside it. The square is filled with a light gray color, and there is a smaller circle at its center filled with a red dot. This arrangement can illustrate concepts such as hierarchical relationships where the outer circle represents a larger context or system, and the inner square signifies a specific bounded area within that context. The red dot at the center might symbolize a focal point or an important aspect within the square, indicating something significant within the confined area. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/acrsVTQLmfft2ZhVmT50IA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/acrsVTQLmfft2ZhVmT50IA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Rectangle


Image:[Image-Analysis: The image depicts a diagram showing concentric shapes. At the center, there is a small circle with a red dot, surrounded by a larger gray rectangle. This design may symbolize different layers or levels of information, with the inner circle representing a core concept or focus area, while the larger rectangle signifies a broader context or environment. Such visuals are often used to illustrate hierarchy or importance, where the central element is of primary relevance, and the surrounding area provides additional context or support. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5Z_Je1JjqJvNHkO~y4vM~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5Z_Je1JjqJvNHkO~y4vM~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Extra Rod Connection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307950?contentId=b8_DuI0klId9o7WbXKzSDg)
These properties specify extra rod connection properties for welded beam attachments.
This is an optional geometry that is used to create the nipple-type object seen on
some bolted ceiling flanges.

These properties are also used in conjunction with the side, top and bottom plate
graphics to create isolation dampers. The extra rod connection is inside the WBA Hole
graphics instead of below. This is most commonly used with only the concrete plate.

An extra rod connection cannot exist individually. It must either have a concrete
plate or WBA Hole graphics.


Image:[Image-Analysis: The image displays a table with a header labeled "Extra Rod Conn." Below this header are three entries that appear to be related to measurements or parameters for a specific component, likely in a technical or engineering context. Each entry is formatted to show certain attributes or properties: 1. "IJUAHsWidth::Width5" suggests it indicates a width measurement with a value of 5, 2. "IJUAHsThickness::Thickness5" implies a thickness measurement also with a value of 5, 3. "IJUAHsShapeType::ShapeType" indicates a variable related to the shape type but lacks a specific value. The use of "::" may suggest a coding or programming context where these attributes are defined or referenced. Overall, the table organizes essential dimensions related to the "Extra Rod Conn" in a systematic way for easy reference. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x61EUTmW2E6GwCJxl0AvMA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/x61EUTmW2E6GwCJxl0AvMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShapeType::ShapeType

This value specifies the graphic shape to be used for the extra rod connection. The
value for this column is a codelist number and valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook of the hsShapeType sheet. Enter the shortName of codelist for readability in the workbook.


Image:[Image-Analysis: The image consists of two separate frames or blocks, each with a rectangular shape in a soft gray color. The top frame contains a larger rectangle and has additional outlines that may suggest it is a component or a section of a structure. Centered in both frames is a smaller rectangle at the bottom, which is notably connected to the larger gray area above it. There are small red circles positioned within each frame, which likely represent points of interest or elements requiring attention. The image may illustrate a systemic or functional relationship between these components, suggesting that the upper section relies on or interacts with the lower section in some way, possibly indicating a stacking or layering of components in a system design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ghytFCCSlzXL9lscga_lZw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ghytFCCSlzXL9lscga_lZw-_PVFQNoCl4XmjAxWO0f7XQ/content)

1 - Round


Image:[Image-Analysis: The image shows a circular diagram with a gray background. In the center, there is a smaller white circle containing a bright red dot. The inner circle may represent a concept or a focal area, while the outer gray region may symbolize a surrounding or less important context. The red dot indicates emphasis or a key element within the central circle, suggesting it is significant in relation to the overall image. However, without additional context, the specific meanings of the colors or shapes cannot be determined. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YI6XUg34adKagzs~sNboiw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YI6XUg34adKagzs~sNboiw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a nested structure consisting of three rectangles. The outermost rectangle is filled with a light gray color and has a black outline. Inside this outer rectangle, there is a second rectangle which is white with a black outline, and inside this rectangle is a small red square. This configuration creates a sense of hierarchy, where the outer rectangle represents a broader context or container, the middle rectangle symbolizes a specific area or section within that context, and the innermost red square represents a focal point or key element within that section. The placement of the red square suggests it is of particular importance relative to the surrounding shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Me7VK1MTDLUdk4KvPqdJkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Me7VK1MTDLUdk4KvPqdJkg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image displays a hexagon, which is a six-sided geometric shape, drawn within a rectangle. The hexagon is colored grey with a black outline, and it features a small red square located at its center. This design can be interpreted as a compositional relationship where the hexagon is situated inside a larger, enclosing rectangle, signifying perhaps a focus on the hexagon itself. The red square at the center of the hexagon may symbolize a point of interest or a reference mark within the hexagonal shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/A1Mnz9QJjEIDMABW2ZtPww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/A1Mnz9QJjEIDMABW2ZtPww-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness5::Thickness5

Enter the thickness of the extra rod connection shape from the lower face of the base
plate to the lower face of the extra rod connection. If this value is set to a negative,
the thickness is started at the upper surface of the base plate bottom and extends
up. If this value is zero, the extra rod connection is not shown.


Image:[Image-Analysis: The image displays a series of geometric shapes and lines. At the top, there is a rectangular shape with a red dot positioned in the center, representing a specific point of interest. Below it, there is a larger rectangular shape that contains a smaller rectangle within it, also centered, along with another red dot. Lines with arrows indicate vertical measurement or connections between the shapes. The red dots seem to signify important points in the geometrical layout, potentially used for referencing dimensions or alignment in design. The vertical and horizontal lines suggest a focus on symmetrical structuring, making it likely that this diagram relates to architectural or engineering plans, emphasizing height and central alignment of the shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EL_ZbV6UlYLOZXO7kMPIVA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EL_ZbV6UlYLOZXO7kMPIVA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth5::Width5

Enter the outside dimension of the extra rod connection shape.

1 - Round


Image:[Image-Analysis: The image shows a diagram depicting a circular object, illustrated with a black outline and a red center, positioned within a rectangular area. Horizontal arrows are shown on either side of the circle, suggesting measurement or alignment. This design indicates that the circle is either constrained within the rectangle or is being used to illustrate a specific concept related to spacing or positioning within a bounded area. The arrows likely represent an instruction to measure the distance across the diameter of the circular object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gjaNxuPWUO~p0AkRYwgkdw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gjaNxuPWUO~p0AkRYwgkdw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a rectangular area with a smaller square located inside it. The outer rectangle is likely representing a bounding box or a frame within which the inner square is positioned. The inner square contains a small red square, which appears to indicate a specific position inside the larger square. There are arrows on the upper side, suggesting that the inner square can be moved horizontally, and there are indications of possible movement limits within the outer rectangle. This setup is often used to demonstrate alignment, positioning, or movement mechanisms in user interfaces or graphical designs. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GKcimcq5h~h~~2IdzRPbXA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GKcimcq5h~h~~2IdzRPbXA-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image depicts a hexagonal shape with a dotted outline indicating its boundaries, placed within a rectangular area. The rectangle appears to represent some context or container for the hexagon. There are arrows on the top indicating a measure of distance or movement between the two outer edges of the rectangle. Inside the hexagon, there is a red dot, which may signify a specific point of interest within the hexagonal space. This design could represent a geometric measurement or a spatial relationship between different shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UavEZHihVpcVi2G0VEEefQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UavEZHihVpcVi2G0VEEefQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308085?contentId=OfvZbZUt6vt5887uIJmhrg)
These properties specify the port properties.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zT5RwNSXImV6DDIMWtnlOA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3860045c33ab3ecf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zT5RwNSXImV6DDIMWtnlOA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image shows a technical diagram consisting of two parts that describe a structure with a hole. On the left side, there are two vertical bars labeled "Structure" with a red dot representing the "Hole" positioned below them. This suggests a conceptual area where the hole is located within the structure. On the right side, there is a vertical cylinder that has arrows indicating the X and Z directions. The arrows signify the coordinate system used in relation to the structure, with the Z axis oriented vertically and the X axis horizontally. The presence of both parts indicates a relationship between the graphical representation of the structure and its spatial orientation in a coordinate system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1tsAgUoDJDN84J~EHW3CUg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1tsAgUoDJDN84J~EHW3CUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Structure (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 – Steel | N/A – Set to 0 | N/A – Set to -9999 | N/A – Set to 9999 |

Port 2 - Hole (0, 0, -Height1 +Offset1)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004 – Rod Hole | RodDiameter | 0 | Offset1 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Yoke Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307520?contentId=n_L79~JnlH6xvV7c8gnpIw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.YokeClamp  
Part Name: Yoke Clamp  
Part Description: Yoke Clamp SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r62mU2zjLrSxIOSQ3dcPEg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3371a2115f20c3ba)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r62mU2zjLrSxIOSQ3dcPEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in   
[Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in   
[Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample Yoke Clamp SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a price tag, indicating an addition or increase in price or value: , and then select the design support.
4. In the Select Part dialog box select a part from Parts > SmartParts > S3D Standard > Pipe Clamps > Yoke Clamp as shown below.

   
Image:[Image-Analysis: The image shows a hierarchical tree structure related to a system or catalog named "SmartParts." At the top level, it begins with the "S3D Standard," which branches into several categories such as "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Struts," and "U-Bolts." Under the "Pipe Clamps" category, there are further subcategories including "Pipe Clamp - Medium 2-Bolt," "Riser Clamp," "Split Pipe Ring," and a highlighted item "Yoke Clamp," which indicates a direct selection or feature of interest in this list. This structure suggests a classification system for various parts or components, likely used in engineering or assembly contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KaY20m85ifnm3JMKMH8N6Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KaY20m85ifnm3JMKMH8N6Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dsdfn85ny8v3~dcyis7zTw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=cb136c585a9fd297)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dsdfn85ny8v3~dcyis7zTw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Yoke Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307535?contentId=0VdOoubqo4KUICWYavg42g)
IJUAhsDiameter1::Diameter1

Specifies the pipe diameter.

IJUAhsSize::Size (Optional)

This value is only used by the Part Selection rule for choosing a Yoke Clamp part. It is not included in the yoke clamp’s graphics.

IJUAhsPinOrLug::PinOrLug

Specifies whether the connection type is a lug or a pin.

This property uses the codelist number defined in the hsPinOrLug sheet in the HS\_S3DParts\_Codelist.xls.

1 - Pin


Image:[Alt-Text: Basic Yoke Properties - 1 - Pin 
Image-Analysis: The image depicts a mechanical system possibly related to a type of valve or a mechanical regulator. On the left side, there is a circular component representing a diaphragm or a membrane system, indicated by the circular shape and shaded area. The red dots likely signify points of interest or connections for operation. Above the circular component, there are two guide mechanisms or levers that likely manipulate the diaphragm in some way. On the right side, there is a vertical structure with controls or indicators at the top, possibly representing a control panel or interface to operate the mechanism. Overall, the image illustrates how different mechanical elements might work together to control a fluid or pressure system, with specific focus on the central circular diaphragm. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jcP4Rwp6wSQmqOJDRmgeAQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Basic Yoke Properties - 1 - Pin](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jcP4Rwp6wSQmqOJDRmgeAQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Lug


Image:[Alt-Text: Basic Yoke Properties - 2 - Lug 
Image-Analysis: The image depicts a technical diagram of a circular valve system, highlighting its operational mechanism. On the left side, the diagram illustrates the valve assembly, showing a circular valve in the center with a prominent red dot indicating the valve stem position. The valve is flanked by control mechanisms represented by vertical elements that connect to the valve body. The right side of the image shows a detailed view of the valve control, which possibly indicates a user interface or manual operation feature, evidenced by an upward pointing arrow at the top. The hierarchical relationship in this image suggests that the control element operates the central valve component, emphasizing the role of the user in regulating the flow through the valve. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e9iq20bc1CY2_SiBuPN3lg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Basic Yoke Properties - 2 - Lug](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e9iq20bc1CY2_SiBuPN3lg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Top Block

![Basic Yoke Properties - 3 - Top Block](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CGsNUp8VRrk7T5~caX5kgg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=675325bf59f0a31d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CGsNUp8VRrk7T5~caX5kgg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOrientation::Orientation

Specifies how the connection type is oriented with respect to the pipe. This is applicable
to both pin and lug top types.

This property uses the codelist number defined in the hsOrientation sheet in the HS\_S3DParts\_Codelist.xls.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iHA1A_NfOiFOxizab_js9A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=cc4deddbdf93db3a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iHA1A_NfOiFOxizab_js9A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance from the pipe centerline to the pin or lug centerline. This
value is always greater than 0.5 times the Diameter1 plus 0.5 times the Pin1Diameter.


Image:[Image-Analysis: The image depicts a mechanical component, likely a valve or a mechanism for extracting a rod. It shows the entity from a side view, highlighting a circular part at the bottom which seems to represent a moveable element. The mention of “RodTakeOut” indicates that this mechanism is involved in a process where a rod is removed or extracted from a certain position. The arrows on the right indicate the movement direction of the rod, emphasizing an operational function. The red dots may signify key points for operation or focus areas of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBhuf03HITUeVdzkkQ~RyQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBhuf03HITUeVdzkkQ~RyQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Detail Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307559?contentId=kPMGCofj0EeTOlMZyb5UIA)
These properties define the geometry of the yoke portion of the yoke clamp.

IJUAhsHeight3::Height3

Specifies the distance from the pipe centerline to the lower face of the yoke.

If the distance is <= 0 then the software sets 0.25 times the Diameter1 to the default value for this property.


Image:[Image-Analysis: The image depicts a technical illustration featuring a cylindrical object, which is shaded in grey. This object is flanked by vertical bars or supports on either side, leading up to a horizontal structure at the top, indicated by the two upward extensions. One notable feature is the marked point (indicated by a red dot) at the center of the grey circle, which likely represents the focal point of measurement or attention. The term "Height3" in bold font suggests that it is related to a dimensional measurement, possibly indicating the overall height of the cylindrical object or space. Overall, the image appears to be a schematic representation related to engineering or design, focusing on the dimensional aspect of the cylindrical shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6OZmGQS~GkS5TZxAZfQJzg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6OZmGQS~GkS5TZxAZfQJzg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight4::Height4

Specifies the distance from the pipe centerline to the lower flat spot of the yoke.

This value is always greater than Height3. If it is less than or equal to Height3, then the software sets Height3 plus 2 times Pin1Diameter as the default value for this property.


Image:[Image-Analysis: The image depicts a mechanical or engineering drawing of a circular object, likely a valve or actuator, which features a central circular component shaded in grey. There are two symmetrical structures on either side that may represent additional mechanical parts or connections. Above these structures, there is a small red square indicating a specific point of interest or a marker. To the right, there is a label "Height4," suggesting a measurement or specific dimension related to the height of the outlined components. The drawing uses lines and shapes to convey dimensional information, which may be important for assembly or manufacturing purposes. The overall layout indicates a focus on balance and symmetry in the design of the components involved. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uPl_EzaaiaB~gZkIPFbPhg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uPl_EzaaiaB~gZkIPFbPhg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight5::Height5

Specifies the distance from the pipe centerline to the top flat spot of the yoke.

This value is always greater than 0.5 times Diameter1. If it is less than or equal to 0.5 times Diameter1, then the software sets 0.5 times Diameter1 plus (Height4 minus Height3) as the default value for this property.


Image:[Image-Analysis: The image depicts a mechanical component that features a circular body, possibly representing a valve or a gauge. There are several key points of interest: at the center, a large gray circle is shown, which may symbolize a piston, ball, or disk. Surrounding this central feature, there are two protruding structures labeled "Height5" and red markers indicating specific measurements or points of interest. These markers could denote reference points for calibration or operation. The entire configuration suggests a design intended for measuring or controlling fluid dynamics in a technical or engineering context. The height measurement is also critical in understanding the distance or pressure needed for the operation of this component. Overall, the image represents engineering details crucial for understanding the functionality and dimensions of the device. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RJY0n7M0G3dMgMsdRuSsbQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RJY0n7M0G3dMgMsdRuSsbQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight6::Height6

Specifies the distance from the pin or lug centerline to the top of the yoke.

This value is always greater than 0.5 times Pin1Diameter. If it is less than or equal to 0.5 times Pin1Diameter, then the software sets 1.5 times Pin1Diameter as the default value for this property.

Type 1 & 2


Image:[Alt-Text: Top Detail Properties - IJUAhsHeight6::Height6 - Type 1 & 2 
Image-Analysis: The image depicts a mechanical diagram likely representing a component with a circular shape, which could be a wheel or disk situated below a rectangular section. There is an indication of a height measurement labeled "Height6", which suggests the height of the component is 6 units. The diagram contains red dots which could represent key points or reference markers. The various lines and shapes imply a relationship where the circular component is connected to other elements in the structure above it, possibly indicating movement or alignment. Overall, the image provides a simplified technical representation of a mechanical component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DV~c45XUc_RbrjsqY~RJpg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Top Detail Properties - IJUAhsHeight6::Height6 - Type 1 & 2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DV~c45XUc_RbrjsqY~RJpg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type 3 - Specifies the height of top block.

![Top Detail Properties - IJUAhsHeight6::Height6](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fCeyqH3DtMrywhMjN2pKzg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=43d9fe2e50ef00f0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fCeyqH3DtMrywhMjN2pKzg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight7::Height7

Specifies the distance from the pipe centerline to the lower face of the yoke.

If Height7 is less than or equal to 0, then the software sets Height7 to Height5 minus (Height4 minus Height3) as the default value for this property.

If Height7 is less than 0.5 times Diameter1 and Height7 greater than 0, then the software sets Height7 to 0.5 times Diameter1 as the default value for this property.

![Top Detail Properties - IJUAhsHeight7](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AcnoaZHo0AmN9wTp4JMPug-_PVFQNoCl4XmjAxWO0f7XQ/content?v=987d9dd58c2dc00f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AcnoaZHo0AmN9wTp4JMPug-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3

Specifies the overall span of the yoke.

This value is always greater than UboltWidth plus UboltRodDia. If it is less than or equal to UboltWidth plus UboltRodDia, then the software sets UboltWidth plus 2 times UboltRodDia as the default value for this property.


Image:[Image-Analysis: The image illustrates a technical diagram, likely representing a piece of machinery or a mechanical component with a circular section in the middle. It features a rounded gray part, which is centrally marked with a small red dot. This central dot may indicate a focal point or point of interest in the design. The diagram includes annotations, with a label "Length3" at the bottom, suggesting the dimension or measurement related to the component's length. There are also structural components depicted on either side of the circular section, which could represent attachment points or additional parts of the machinery. The overall design is likely for engineering or manufacturing purposes, detailing specifications for assembly or construction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3tJK0w1nPvxG~u0G32VerQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3tJK0w1nPvxG~u0G32VerQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength4::Length4

Specifies the overall span of the upper attachment.

Case 1: if hsPinOrLug equals 1

* It is always greater than zero.
* If it is less than or equal to 0, then the software sets 1.5 times the Hole1Diameter as he default value for this property.

Case 2: if hsPinOrLug equals 2

* It is always greater than zero.
* If it is less than or equal to 0, then the software sets 0.5 times the Hole1Diameter as the default value for this property.

Case 3: If hsOrientation equals 2, then these dimensions are oriented parallel to the route.

* It is always less than or equal to Width3.
* If it is greater than Width3, then the software sets Width3 as the default value for this property.

hsPinOrLug = 1


Image:[Alt-Text: Top Detail Properties - IJUAhsLength4::Length4 - 1 
Image-Analysis: The image depicts a schematic representation of a pressure vessel. It consists of a cylindrical tank with a domed top and bottom, indicated by a thick black outline. On the left and right sides, there are two pipes (or nozzles) emerging horizontally, which are typically for input and output connections. The vessel is designed to hold gases or liquids under pressure, and the red dots may represent pressure measurement points or indicators on the surface of the vessel. The design showcases the internal structure and various connections integral to the operation of the pressure vessel, highlighting its functionality in industrial applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ2kpJxGAmCw5k_x1pF_xA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Top Detail Properties - IJUAhsLength4::Length4 - 1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SZ2kpJxGAmCw5k_x1pF_xA-_PVFQNoCl4XmjAxWO0f7XQ/content)

hsPinOrLug = 2


Image:[Alt-Text: Top Detail Properties - IJUAhsLength4::Length4 - 2 
Image-Analysis: The image depicts a mechanical device or system, likely a schematic representation of a valve or some kind of hydraulic component. In the center, there is a large circular shape indicated as a chamber that is filled and shaded, which implies it might contain a fluid or other material. The smaller rectangular shapes connected to the sides appear to represent inlet and outlet ports, suggesting the flow of material into and out of the chamber. The structure above the chamber has various elements that could signify operational controls or indicators. The overall design seems to illustrate how the component functions within a larger system, showcasing connections and potential directions of flow, thus providing a visual representation of mechanical function or operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SExGr8WK1ICcX3XmTxUqSQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Top Detail Properties - IJUAhsLength4::Length4 - 2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SExGr8WK1ICcX3XmTxUqSQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

hsPinOrLug = 3

![Top Detail Properties - IJUAhsLength4::Length4 - 3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ocVdz5P7EEmlNPRz8V5KvA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=79197dfca8390248)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ocVdz5P7EEmlNPRz8V5KvA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength5::Length5

Specifies the inside span of the upper attachment.

Case 1 if hsPinOrLug equals 1

* It is always greater than zero and less than Length4.
* If it isless than or equal to 0 or greater than Length4, then the software sets Hole1Diameteras the default value for this property.

Case 2: if hsPinOrLug equals 2 it is ignored.

Case 3: If hsOrientation equals 2, then these dimensions are oriented parallel to the route.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jv0HH4tvfhdKJGxVPzbzUQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7ac68275c539d5dc)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jv0HH4tvfhdKJGxVPzbzUQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength6::Length6

Specifies the inside span of the lower flat spot.

This value is always less than or equal to Length3 and greater than or equal to Length7. If it is zero or greater than Length3, then the software sets Length3 as the default value for this property.

If it is not equal to zero and less than Length7, then the software sets Length7 as the default value for this property.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w8vMvCDDQRasT0hW3rNDxA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2b5f269b197964c7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w8vMvCDDQRasT0hW3rNDxA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength7::Length7

Specifies the overall span of the top flat spot.

This value is always greater than or equal to Length5 and less than or equal to Length3. If it is less than Length5, then the software sets Length5 as the default value for this property.

If it is greater than Length3, then the software sets Length3 as the default value for this property.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zq5RHzZnDtaDp3gPgUrkNg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=32e03579316b731e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zq5RHzZnDtaDp3gPgUrkNg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the width of the yoke body.

This value is always greater than or equal to Pin1Diameter. If it is less than Pin 1Diameter, then the software sets two times the Pin1Diameter as the default value for this property.


Image:[Image-Analysis: The image illustrates a technical drawing that features a circular shape, symbolizing a component that is potentially part of a larger mechanical system. The main circle appears to be gray, with red dots in specific locations, likely indicating pivotal points or reference markers. There are different components indicated at the top of the image, which could represent mounting or connection points for the circular shape. The right side of the image displays a section view, with the label "Width3" suggesting a dimension or measurement related to the circular component. The overall structure seems designed for clear representation of spatial relationships and measurements in engineering or manufacturing contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9xZfGmHn1_abfsIICGO6BA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9xZfGmHn1_abfsIICGO6BA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Specifies the width of the pin or lug attachment.

This value is always greater than or equal to the Pin1Diameter. If it is less than Pin 1Diameter, then the software sets Width3 as the default value for this property.

If hsOrientation = 2, then these dimensions are also oriented perpendicular to the route.


Image:[Image-Analysis: The image appears to be a technical diagram showing a mechanical system, likely related to a drum or a cylinder that is part of a larger apparatus. On the left side, there is a circular component, which is shaded and appears to have a red dot indicating a focal point or a specific measurement point. This circular component is connected to various elements such as vertical and horizontal lines indicative of support structures or mounting points. The right side of the image illustrates additional features or controls that might be associated with the mechanical system, including a pneumatic or hydraulic actuator shown through vertical components and other indicators. The red dots may signify points for measurement or adjustment in the mechanical process. Overall, the diagram seems to show the relationship between different components necessary for the operation of the described system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tSYPuwkp_EEfHb37l3Tr8A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tSYPuwkp_EEfHb37l3Tr8A-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Alt-Text: Top Detail Properties - IJUAhsWidth4::Width4 - 2 
Image-Analysis: The image depicts a schematic representation of a connector, often used in electrical or electronic applications. It shows a vertical alignment of components, including a sliding mechanism and a central pin, which is likely responsible for the connection. The red dots indicate connection points or signal indicators, and the arrows at the top suggest the direction of insertion or movement. The entire design can be interpreted as a guide for how to properly orient and connect the components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tGnhi6ilZtk~vF0Fa3qYlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Top Detail Properties - IJUAhsWidth4::Width4 - 2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tGnhi6ilZtk~vF0Fa3qYlA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin and Lug Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307604?contentId=R4cMaNZL~24qDUW0u_Tdtw)
These properties define the geometry of the pin or lug at the top of the yoke clamp.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt or lug.

If hsPinOrLug = 2 the hole is not shown in the graphics. To represent it, set Pin1Length equal to Length4 and Pin1Diameter less than Width4.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOBVLPK9Sb4c2Ocp7eSXvw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4d11c65c95cf76e2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOBVLPK9Sb4c2Ocp7eSXvw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the pin. This value is always greater than Length4.

If hsPinOrLug equals 2, then set this value to Length4. If hsPinOrLug equals 1 and it is less than Length4, then the software sets Length4 plus Pin1Diameter as the default value for this property.


Image:[Image-Analysis: The image depicts a mechanical diagram, likely related to a pin or connector assembly. At the top, there is a label indicating "Pin1Length," which suggests that the diagram is measuring a specific length associated with "Pin 1". The central circular shape represents a pin or a similar component, possibly with a focus point in red, indicating a critical measurement or positioning. The structure surrounding it seems to be an assembly that might involve a clip or other mechanical fittings. The two vertical lines with arrows appear to represent distance measurement relative to the pin. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sQB_AgI19eVfHZyBAl1vlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sQB_AgI19eVfHZyBAl1vlA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307615?contentId=PCgb3jEjgdr23RXC55IaCg)
These properties define the u-bolt portion of the yoke clamp.

IJUAhsUBolt::UBoltWidth

Specifies the center to center distance between the legs of the u-bolt.

This value is always greater than UBoltRodDia. This value determines the spacing of the vertical legs of the u-bolt as well as
the bend radius for the curved part of the u-bolt. The nominal bend radius is equal
to half the UBoltWidth dimension.


Image:[Image-Analysis: The image illustrates a U-bolt, which is a type of fastener commonly used in various applications. The U-bolt is depicted with a semi-circular top and two vertical ends. The red dots indicate points of measurement, likely representing the width between the two vertical sides of the bolt. Below the U-bolt, there is a label that reads "UBoltWidth," which suggests that the width of the U-bolt is being specifically referenced or measured in this context. This measurement is crucial for ensuring that the bolt fits properly in its intended use. The arrows on either side indicate that the measurement is taken across a distance, emphasizing the importance of the width measurement in applications such as securing objects together. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5lPkrNci3Zfq5iWU0GbURg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5lPkrNci3Zfq5iWU0GbURg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltCenterToEnd

Specifies the distance from the pipe centerline to the end of the u-bolt legs.


Image:[Image-Analysis: The image depicts a diagram of a U-bolt and includes some specific measurements or notation related to it. The U-bolt is represented by a curved line with two vertical lines at the ends. There are two red dots that likely indicate specific positions or reference points on the U-bolt. Additionally, the diagram includes an arrow pointing towards a distance measurement labeled "UBoltCenterToEnd," which suggests that the image is used to illustrate the distance from the center of the U-bolt to one of its ends. This kind of diagram is typically used in mechanical engineering or fabrication contexts to convey important dimensions for the installation or discussion of U-bolts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LAQmu1mIFRo8_2fejJUTOw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LAQmu1mIFRo8_2fejJUTOw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltRodDia

Specifies the diameter of the round stock used to make the u-bolt.

If this value is set to zero none of the u-bolt shape is drawn unless the UBoltDia2 is non-zero.


Image:[Image-Analysis: The image features a simple illustration of a U-bolt, which is shaped like the letter "U". The red dots in the center indicate points of interest or notes regarding the dimensions of the U-bolt. Below the U-bolt, there is a horizontal line with arrows indicating the diameter of the bolt rod, which is a key measurement for understanding the size of the U-bolt. The label "VBoltRodDia" likely refers to the diameter of the rod used in the U-bolt, which is an important specification in construction and engineering contexts. This imagery is structured to give a clear visual representation of a U-bolt and to highlight specific measurements related to its construction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xN~zS3lWgClPoU6Nb1Hm5A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xN~zS3lWgClPoU6Nb1Hm5A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2

Represents a diameter change for round insulation, coatings, or to delete the curved
part of the u-bolt.

If this value is greater than 0, the software changes the diameter of the curved part
of the u-bolt starting at the position UBoltDia2Start as shown in Fig.1.

This value can be larger or smaller than UBoltRodDia. If it is equal to 0, it defaults to the same diameter as UBoltRodDia. If it is less than 0, then the curved part of the u-bolt is not visible in the graphics
starting at the UBoltDia2Start as shown in Fig. 2.


Image:[Image-Analysis: The image depicts a technical diagram, specifically a representation of a U-bolt, which is a type of fastener used to secure objects together. The main features of the U-bolt are outlined, including its curved shape and straight legs. There is a notation "UBoltDia2" which likely refers to a specific dimension or designation related to the diameter of the U-bolt. Alongside this, a small red square is shown, possibly indicating a reference point or measurement location. Additionally, "Fig. 1" in blue at the bottom suggests that this is the first figure within a larger document, serving as a reference to discuss the U-bolt further in the text. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k0i1RPwNQXFeHUudOsZNrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k0i1RPwNQXFeHUudOsZNrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2Start

Specifies the start position of a diameter change. This value is used to represent
round insulation, coatings, or to delete the curved part of the u-bolt.

If UBoltDia2 is zero or the same value as UBoltRodDia, this has no effect because there is no change in the rod diameter.


None: 

IJUAhsUBolt::UBoltFlatSpot

If UBoltDia2 is negative this is ignored because, there is no curved part of the u-bolt to have
a flat spot.

This value also adds a flat spot to the shape of the rectangular wrap or strap.

If it is set to zero, no flat spot is shown in the curved part of the u-bolt. If it
is set to a positive value, a flat spot is shown in the curved section of the u-bolt.
This also reduces the bend radius and center points for the curved part of the u-bolt.

This value is always less than BoltCenters1 - UBoltRodDia.


None: 

IJUAhsUBolt::UBoltTopGap

Specifies the gap between the outside of the pipe and the inside of the u-bolt (the
gap is based on UBoltRodDia. It is not based on UBoltDia2).

This value affects the vertical position of the center of the bend radius for the
curved portion of the u-bolt.

IJUAhsUBolt::UBoltOneSided

This property is not applicable to yoke clamp.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307630?contentId=1OXfqbiN6bcWmkxGnOvDwg)
There are four different nuts, all having similar properties.

* Nut1 is positioned immediately above the right side of the yoke body.
* Nut2 is positioned above Nut1.
* Nut3 is positioned immediately above the left side of the yoke body.
* Nut4 is positioned above Nut3.

IJUAhsShape1::Shape1Type

Determines the graphic shape used for the nut or washer. It uses the codelist number
defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls.


Image:[Image-Analysis: The image displays three geometric shapes labeled with their respective names and numbers. The first shape is a round circle identified as "1 - Round." The second shape is a square depicted with the label "2 - Square." The third shape is a hexagon shown with the label "3 - Hex." Each shape is drawn with a dotted line, indicating their outlines. This image could be used for educational purposes to teach different types of geometric shapes and their identifiers. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jjy8ZR08swLYISz_AxqrXw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jjy8ZR08swLYISz_AxqrXw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the nut or washer.


Image:[Image-Analysis: The image displays three different geometric shapes, each labeled with a number and a name. The shapes are: 1. A round shape (circle), which is represented with a circular outline; 2. A square shape, which is depicted with a square outline; and 3. A hexagonal shape, shown with a hexagon outline. Each shape includes a dashed line in the center that may represent the dimensional measurements or the inner component of the shapes. The purpose of this image is likely to show the differences in form between these common geometric shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qv3o1Uvjm0aQMnWlRXfckg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qv3o1Uvjm0aQMnWlRXfckg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Image-Analysis: The image displays a comparative overview of three different geometric shapes and their effects or characteristics. Each shape is labeled with a number: 1 for "Round", 2 for "Square", and 3 for "Hex". Under "Round", there is a drawing of a circle with dimensions indicated by horizontal lines, suggesting its diameter or size. The "Square" section shows a square shape, also with similar dimension lines. Notably, the "Hex" shape is not depicted but is stated to have "No effect", implying it does not have the same dimensions or characteristics as the previous two shapes. This illustration appears to be aimed at contrasting the properties of these geometric figures, possibly in a scientific or design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/txyFpLLRAyNPA7nKTTINnA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/txyFpLLRAyNPA7nKTTINnA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the thickness of the nut or washer.


Image:[Image-Analysis: The image depicts two arrows pointing towards a central object, which appears to be a rectangular shape with a division in its middle. The arrows suggest movement or a compressive force being applied towards the center from both sides. The rectangular object is outlined and has two red circles indicating critical points or areas of interest, possibly showing where the force is applied or where results are measured. This representation could illustrate a concept related to forces acting on an object, such as compression or tension in a material. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8h7CZEnER2_rHPwThZ29iw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8h7CZEnER2_rHPwThZ29iw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Block Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307640?contentId=uZaWYwvQ1ZY4XBrgDhxUmg)
These properties are optional and can be used to specify two stacked rectangular blocks
that represent slide plates, shims, insulation pads, cradles, and so on. Enter the
values for these properties only when block geometry is required.

The position of Block1 is exactly Gap1 below the bottom of the pipe. The position of Block2 is on top of Block1. Both blocks have similar input properties – height, width and length. These blocks
will not be included if any of these properties are set to zero.


Image:[Image-Analysis: The image depicts a mechanical component, likely a part of a machinery or apparatus, that includes a spherical upper section and several labeled elements. The main components are: "Block 1" and "Block 2," indicating distinct parts that might serve specific functions or are used for adjusting or holding mechanisms. The "Yoke Body" is another important part that often serves as a structural support or connection between parts. The overall design illustrates how these components are arranged and connected to facilitate movement or stability in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/38Z~UWGj4vDp3B_8sW3tHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/38Z~UWGj4vDp3B_8sW3tHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1 (Optional)

Specifies the distance between the bottom of the pipe and the top of Block1.

This value can be negative, zero, or positive value. If it is set to zero no gap exists
between the pipe and Block1. If it is set to a positive value there is a gap of the specified value between the
pipe and the top of Block1. If it is set to negative value Block1 is partially embedded into the pipe.


Image:[Image-Analysis: The image depicts a technical drawing of a yoke body, which is a component in machinery or equipment. The yoke body is illustrated from a front view, showing its key features and dimensions. There are two primary annotations: one labeled "Yoke Body" indicating the main component, and another marked "Gap1" representing a specific measurement between parts of the assembly. The image includes a circular element at the top center, potentially indicating a bearing or similar part, and the overall structure appears to consist of various sections that could define its function in an engineering context. The presence of dimensions suggests this drawing might serve for manufacturing or assembly purposes, emphasizing precise gap measurements critical for the correct functioning of the mechanism. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JIE~7iHI1wFQ_LSuvOiy1A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JIE~7iHI1wFQ_LSuvOiy1A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1 (Optional)

Specifies the height of the block.


Image:[Image-Analysis: The image depicts a technical drawing of a device, specifically focusing on two labeled parts: "Yoke Body" and "Height1." The drawing features a circular top view of the device, which likely is a component of a larger assembly. The arrows indicate the dimensions related to the "Height1," which refers to a vertical measurement, while "Yoke Body" denotes a crucial structural element. This could suggest that the device serves a mechanical purpose where the yoke plays a significant role in supporting or connecting parts together. The red points might indicate specific reference points or are essential for alignment in assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZSG5Syu28gQZ~7oUzRd6zQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZSG5Syu28gQZ~7oUzRd6zQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1 (Optional)

Specifies the width of the block.


Image:[Image-Analysis: The image is a technical drawing showing a component, likely related to mechanical or engineering design. It depicts the top view of a component with labels indicating key features. The term "Width1" is marked, suggesting a measurement of the width of the component. Additionally, there is an annotation pointing to the "Yoke Body," which is a specific part of the component. The yoke body typically serves as a support or housing for other parts. The drawing includes a circular element at the top, possibly indicating a circular feature or mounting point, and red dots indicating specific points of interest or alignment. Overall, it gives an overview of the component's structure and dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Car1MbtGfrb5ZdGmBPjWCQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Car1MbtGfrb5ZdGmBPjWCQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1 (Optional)

Specifies the length of the block in the direction of the pipe.


Image:[Image-Analysis: The image depicts a mechanical or structural diagram with an existing steel component. The left side shows a front view of the existing steel which includes a circular part and two bolts below it. The text "Existing Steel" is highlighted, suggesting that this is a reference to a specific part of the diagram. On the right side, there is a visual representation of "Length1," which appears to indicate a measurement related to this steel part. Overall, the image is likely detailing a component used in construction or engineering, highlighting its structure and dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6QplhSILITuZX4rLRyjE1w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6QplhSILITuZX4rLRyjE1w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt Multi Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307653?contentId=lLBPWCkcTlDRNpyrFU2_ug)
These properties can be used to specify the quantity of u-bolts and how to locate
them (by center or by edge), and the location value.

IJUAhsMulti1::Multi1Qty

Specifies the quantity of u-bolts. U-bolts are not shown on the yoke clamp body when
Multi1Qty is set to zero.


Image:[Image-Analysis: The image displays two types of U-Bolts: a Single U-Bolt on the left and a Double U-Bolt on the right. The Single U-Bolt is depicted with one curved section that allows it to wrap around a single pipe or object, while the Double U-Bolt consists of two parallel U-shaped sections, enabling it to secure two components side by side. Each type has a distinct application based on the number of objects it needs to hold, with the Single U-Bolt being suitable for simpler fastening needs and the Double U-Bolt providing more stability for securing two parallel objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cPx~20GAhRMYNLM3ura~dw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cPx~20GAhRMYNLM3ura~dw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the distance for exact location of the u-bolts depending on Multi1LocateBy and Multi1Qty.

This value can be either a distance to the edge or a center-to-center spacing.


Image:[Image-Analysis: The image depicts a simple diagram with a rectangular box and a circle placed at the center along a dotted vertical line. The rectangle represents a certain area or container, while the circle may indicate a focal point or reference within this area. Below the diagram, there are three descriptive lines: "MultiQty = 1", which suggests there is a quantity of one object or entity; "MultiLocatedBy = Center", indicating that this object is centered within the space; and "MultiLocation = 0", which could mean that there are no additional locations for placing this entity. The overall setup could be used in contexts such as design layout, architectural planning, or conceptual modeling where spatial arrangement is being illustrated. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BlsuvkQfjdG0Ll4jSCMviA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BlsuvkQfjdG0Ll4jSCMviA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image presents a diagram illustrating the placement of multiple circular objects (labeled as "x") within a rectangular boundary. The key points highlighted in the diagram are: 1. "MultiQty greater than 3 (5 shown)" indicates that there are five circular objects placed in the center of the rectangle, and it suggests that the quantity of the objects can exceed three. 2. "MultiLocatedBy = Center (only valid choice)" establishes that the arrangement of these objects should be centered within the rectangular area. 3. "MultiLocation = x" means that the specific locations of these objects are marked by "x". There are also dashed vertical and horizontal lines that likely represent alignment guides for positioning the circles accurately within the given dimensions of the rectangular space. This setup could be relevant in contexts like product design or layout planning. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GN9UyVz_iKBoYYXnXKsSyg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GN9UyVz_iKBoYYXnXKsSyg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307659?contentId=PnaidLYleDFSBPfGioFHAQ)
These properties are optional and can be used to represent rectangular insulation,
U-Bolt band combinations, or strap-shaped liners, with or without wings. Enter the
values for these properties only when strap geometry is required.

IJUAhsStrap::StrapWidthInside (Optional)

Specifies the inside distance between the legs of the strap. This value is greater
than PipeOD.


None: 

IJUAhsStrap::StrapHeightInside (Optional)

Specifies the inside height from the base of the strap to the top.


Image:[Image-Analysis: The image depicts a curved design, resembling a strap or a hook, with an indication of measurements related to the "Strap Height Inside." There are red markers positioned to highlight specific points, likely where the measurement for the height of the strap's inside section is taken. The arrows next to the vertical lines illustrate the height being measured. The graphic serves to visually present how to ascertain the inside height of the strap, indicating that the measurement is crucial for fitting purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QAai9Ina2A5M5BWTwTuOYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QAai9Ina2A5M5BWTwTuOYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapThickness (Optional)

Specifies the thickness of the rectangular stock used to make the strap. This value
cannot be zero.


Image:[Image-Analysis: The image illustrates the concept of "Strap Thickness" with a simplistic diagram. It depicts a curved shape resembling a strap or loop, with two red dots indicating points of measurement for the thickness of that strap. The black lines represent the directional flow of measurement, showing that the thickness can be observed vertically. The word "StrapThickness" is labeled at the bottom to denote that this is the focus of the measurement being illustrated. This provides a visual understanding of how the thickness of a strap can be measured and conceptualized in a geometric form. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eO2vHMLyI9coIi3kbAhKfA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eO2vHMLyI9coIi3kbAhKfA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapStockWidth (Optional)

Specifies the width of the rectangular stock used to make the strap. This value cannot
be zero.


Image:[Image-Analysis: The image illustrates the concept of strap stock width in a diagrammatic form. On the left side, there is a semicircular shape depicting a strap, which likely represents a component that can be flexible, possibly in a mechanical context. Within this shape, there are two red squares positioned, indicating specific points of interest related to the strap. The right side of the image features a rectangular shape that likely denotes the width of the strap stock. It emphasizes the measurement aspect, likely intending to convey how the width of the strap correlates with its design or application. The term "Strap Stock Width" is prominently displayed at the top, indicating that this is the main focus of the illustration. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1ljSQstP3vNSBrne_vRPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1ljSQstP3vNSBrne_vRPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapFlatSpot (Optional)

Adds a flat spot in the curved part of the strap.

This value can be less than or equal to StrapWidthInside. If it is set to zero no flat spot is shown on the curved part of the strap. If it
is set to a positive value, it adds a flat spot in the curved section of the strap
as shown in Fig. 1. If it is set to StrapWidthInside the strap is drawn like three plates with no corner rounding as shown in Fig.2.


Image:[Image-Analysis: The image illustrates a diagram titled "StrapFlatSpot." It depicts a curved shape with arrows pointing towards each other at the top, indicating a pressure or closing motion at the ends. There are two red dots aligned vertically beneath the curved shape, and below them is a label "Fig. 1" in blue font. The diagram likely represents a component or feature related to the design or function of a strap or similar object, with an emphasis on flatness and perhaps pressure points where the strap is intended to be effective. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L_foMXyP1_Lni_S_eyPYAA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L_foMXyP1_Lni_S_eyPYAA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStrapGap::StrapTopGap (Optional)

Specifies the gap between outside of pipe and inside of the strap


Image:[Image-Analysis: The image depicts a schematic diagram illustrating a concept referred to as "StrapTopGap." In this diagram, there is a curved structure that appears to resemble a strap or a band, possibly encircling a circular object represented in the center. There are two arrows indicating a gap above the circular object, which likely represents the vertical space between the strap and the object below it. Additionally, there are small red markers indicating specific points on the strap and the circular object, which may denote measurements or focal points of interest within this gap. This type of illustration is commonly used in engineering or design contexts to convey measurements, tolerances, or spacing specifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iv7Pcgo_PzfbvN3tsQG2hA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iv7Pcgo_PzfbvN3tsQG2hA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapWidthWings (Optional)

Specifies the width to the outside of the wings.

If this value is set to zero or less than StrapWidthInside plus 2 times the StrapThickness, the strap wings are not shown.


Image:[Image-Analysis: The image is a diagram illustrating a specific component termed as "StrapWidthWings". The top portion depicts a rounded shape which could represent a connector or a strap interface. There are two red dots positioned vertically, suggesting points of measurement or reference. Below the rounded part, there are horizontal arrows that indicate the width of the strap, signifying that the width can be measured across the two wings extending outward. The main focus of the image is to provide a visual representation of the dimensions and characteristics related to the StrapWidthWings component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gS0ucrHqWAROu_KWoo4SfQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gS0ucrHqWAROu_KWoo4SfQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapOneSided (Optional)

Standard Yes or No codelist. If this value is set to Yes, the right side of the strap is not shown below the tangent point.

Wings, bolts and gussets are not included in the right side if StrapOneSided is set to Yes.


Image:[Image-Analysis: The image depicts a simple outline of a water flow system or drainage setup. It includes various components represented by lines and arcs, indicating pipes or channels for directing water. The red dots along the lines might represent points of interest such as joints or valves. The system is designed to manage the flow of water, possibly indicating connections to different sections of a building or landscape. The arrangement suggests a hierarchical or interconnected structure where water can be directed from one point to another, likely for purposes such as drainage or irrigation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w2C6s3zJS_jRyYqZ1w75ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/w2C6s3zJS_jRyYqZ1w75ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitGap (Optional)

Specifies the gap at the top and splits the strap into two parts.


Image:[Image-Analysis: The image depicts a diagram labeled "StrapSplitGap." It features a central section with two arrows pointing toward a narrow gap, indicating a split. The diagram shows curved edges on the sides that suggest a strap-like structure, integrating two components on the bottom indicated by red squares. This structure suggests the design or layout of a device or mechanical part that might involve some form of connection or separation, typically used in engineering or technical contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jedQ1NTVr878ylDPyAdXJQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jedQ1NTVr878ylDPyAdXJQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapSplitExtension (Optional)

Specifies the length of the tabs from the top inside of the strap to the end of the
tabs.


Image:[Image-Analysis: The image illustrates a component with a design labeled "StrapSplit Extension." This component features a distinct shape resembling a U or bell-like form with two upper sections that appear to split apart at the top. There are vertical measurements indicated which suggest that the height of these extensions is important. Additionally, there are two red dots at the bottom of the structure, potentially marking points for reference or attachment. The overall purpose of this illustration could be related to a technical aspect of a device or machinery that utilizes this extension. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bm4z4gKt3alTE2LFUR_Ctw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bm4z4gKt3alTE2LFUR_Ctw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Multi Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307664?contentId=kXcrygvLhE_IllJkUoiE1Q)
These properties can be used to specify the quantity of straps, how to locate them
(by center or by edge), and the location value.

IJUAhsMulti2::Multi2Qty

Specifies the quantity of straps. Straps are not shown on the yoke clamp body when
Multi1Qty is set to zero.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DxyKyYmugcAfPd4JFoZ5yQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=fa123d38992bbc28)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DxyKyYmugcAfPd4JFoZ5yQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti2::Multi2LocateBy

Specifies the location of the straps. Individual straps can be located in two ways.

1- Relative to center of the group.  
2 - Relative to the edge.

The exact meaning depends on the quantity of straps. This value can be 0 (nothing), 1 (center) or 2 (edge).

IJUAhsMulti2::Multi2Location

Specifies the distance for the exact location of the straps depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge or a center-to-center spacing.


Image:[Image-Analysis: The image illustrates a rectangular shape with a circle positioned at the center, as indicated by the dashed vertical line. Below the shape, there are some textual annotations that specify properties of the shape: "MultiQty" indicates there is 1 of this shape, "MultiLocatedBy" specifies that it is located by the center, and "MultiLocation" is set to 0, possibly referencing the absence of multiple locations or instances. The diagram likely serves to convey layout or design information, potentially in a technical or architectural context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Xl93Y4XsBQx9pvSWS4g~zg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Xl93Y4XsBQx9pvSWS4g~zg-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image illustrates a diagram for a multi-location setup. It includes multiple circular objects aligned vertically, showing how the arrangement is centered. The key points are indicated by some text at the bottom. The text conveys three main instructions: "MultiQty greater than 3" implies there should be more than three items (five are shown), "MultiLocatedBy = Center" states that the valid arrangement should be centered, and "MultiLocation = x" indicates the specific placement or coordinate defined by "x". The dashed lines suggest symmetry and balance in the arrangement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/E2cHViPiQEaWiScMbYe0fA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/E2cHViPiQEaWiScMbYe0fA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307686?contentId=xTxbku5qqTqdzhoduTIXgw)
These properties are used to specify the different port types and their sizes for
the yoke clamp.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8FApGSFVHhUe6XNAWeJr3g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f83b1639f0fbe621)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8FApGSFVHhUe6XNAWeJr3g-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QFjI9ISSsk3OycKiyazBFQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=65aaeeffad0a2ea7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QFjI9ISSsk3OycKiyazBFQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1016 - Pipe Clamp | Diameter1 | Diameter1 | Diameter1 |

Port2 – Pin (0, 0, RodTakeOut)

If hsPinOrLug = 1 then

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1005 - Pin | Pin1Diameter | Pin1Diameter | Pin1Diameter |

If hsPinOrLug = 2 then

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1008 - Single Lug | Length4 | Zero | Pin1Diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shapes for SmartParts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325980?contentId=FwyAV5pQZtqqsrbIsiZuEA)
The following topics describe properties that define various types of shape parts.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Beam Clip Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/329731?contentId=aEeXtjk9EJBpqMpYaJK1Bw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Clip Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/329781?contentId=FpdX64jRd5dxsjOOu3JRXw)
These properties define the geometry of the beam clip body.


None:  For these properties, millimeters (mm) is the default unit of distance. Use "in" at the end of the dimensional value to specify inches.

IJUAhsClip::ShapeType

Specifies the codelist number of the clip shape type as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook. The shape origin is shown by 
look for a round icon that is solid red in color, similar to a dot or circular shape: 

The valid values include:

![Basic Properties ( Beam Clip Shape) 1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_99FQTEfcYjo9cfLFhaR1g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=163678fde89f864d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_99FQTEfcYjo9cfLFhaR1g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClip::ClipWidth1

Specifies the first width of the beam clip. This value must be greater than or equal
to zero.

For Shape P and Q, if ClipWidth1 is not given or Zero, then ClipWidth1 is calculated in the code as shown below.

ClipWidth1 = FlangeWidth/2+ClipGap-Gap/2

IJUAhsClip::ClipWidth2

Specifies the second width of the beam clip. This value must be greater than or equal
to zero.

![ClipWidth2( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K_VbB8wA0~UgJJ4bMoAR0w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9bb1a7ab59ff4284)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K_VbB8wA0~UgJJ4bMoAR0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Shape P and Q, if ClipWidth2 is not given, then it is calculated in the code as shown below.

For P,

ClipWidth2 = FlangeWidth/2+ClipGap - Gap/2 + ClipThickness

For Q,

ClipWidth2 = FlangeWidth/2 + ClipGap - Gap/2

IJUAhsClip::ClipWidth3

Specifies the third width of the beam clip depending on the shape of the clip. This value must be greater than or equal to zero.

![ClipWidth3( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hEQXNzumogvN924kwg~JUg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9ae8e207957daee7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hEQXNzumogvN924kwg~JUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Shape Q, if ClipWidth3 is not given, then it is calculated in the code as shown below.

ClipWidth3 = Gap + ClipThickness

IJUAhsClip::ClipThickness

Specifies the first thickness of the beam clip shape. This value must be greater than
zero.

![ClipThickness( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aa6GZKs8e12mi2JCe5vovw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8bf4ee03877b8410)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aa6GZKs8e12mi2JCe5vovw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClip::ClipThickness1

Specifies the second thickness of the beam clip shape. This value must be greater
than zero.

![ClipThickness1 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7PrPh6FYElfRDL74HJNNTw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a95e81e7eceb7f82)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7PrPh6FYElfRDL74HJNNTw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClip::ClipThickness2

Specifies the third thickness of the beam clip shape. This value must be greater than
zero.

![ClipThickness2 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WZ_UGhvvVt3Ck3kW0aORCQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ed70efd1c2455974)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WZ_UGhvvVt3Ck3kW0aORCQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClip::ClipHeight1

Specifies the first height of the beam clip shape. This value must be greater than
or equal to zero.

![ClipHeight1 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dGVntvirtQQrqfXcXl6y0w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=310e894a03ca5de1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dGVntvirtQQrqfXcXl6y0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Shape P and Q, if ClipHeight1 is not given, then it is calculated in the code as shown below.

ClipHeight1 = FlangeThickness + 2\*ClipThickness

IJUAhsClip::ClipHeight2

Specifies the second height of the beam clip shape. This value must be greater than
zero.

![ClipHeight2 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GAPGtXONMdAUauzBAPGwxg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ba480cdc93e4a0bc)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GAPGtXONMdAUauzBAPGwxg-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Shape P, if ClipHeight2 is not given, then it is calculated in the code as shown below.

ClipHeight2 = Height3 + 2\*ClipThickness# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/329782?contentId=tUyY8DF2e2fRMRkZwPGZsA)
The following properties are used to set the dimensions and location of the bolt.

IJUAhsClipBolt::BoltLength

Specifies the length of the bolt used in the beam clip.


Image:[Alt-Text: boltlength (beam clip shape) 
Image-Analysis: The image features a large red letter "T" which appears to be a stylized or artistic representation. The letter is outlined with a red stroke, and there are two small teal markers, one positioned above and one below the vertical line of the "T." These markers can indicate measurement points, suggesting that the height of the letter "T" is being measured. The overall composition highlights the letter prominently, possibly emphasizing its form or usage in a design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7XRT4UADbR5eczcMq9Di8w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![boltlength (beam clip shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7XRT4UADbR5eczcMq9Di8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClipBolt::BoltDiameter

Specifies the diameter of the bolt used in the beam clip.


Image:[Alt-Text: BoltDiameter (beam clip shape) 
Image-Analysis: The image depicts a large letter "T" that occupies the central part of the image. The letter is outlined in red and appears to be quite bold. On either side of the vertical line of the "T", there are small arrows directed towards the edges, which could suggest a notion of expansion or direction. This configuration might symbolize a concept in mathematics or physics, where the letter "T" is often used to represent various parameters or values, and the arrows could indicate movement or change related to the structure. Overall, the image seems to represent the letter "T" in a way that emphasizes balance and direction, possibly hinting at its significance in a specific context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ep~45wKBCl1VhTNVOd~v6Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BoltDiameter (beam clip shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ep~45wKBCl1VhTNVOd~v6Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClipBolt::HeadType

Specifies the shape of the bolt's head.

Allowed values are:


Image:[Alt-Text: HeadType( Beam Clip Shape) 
Image-Analysis: The image displays three geometric shapes labeled with numbers and corresponding names. The first shape is a round circle labeled "1 – Round". The second shape is a square, labeled "2 – Square". The third shape is a hexagon, labeled "3 – Hex". Each shape features a dot in the center, which may suggest a common design element or emphasize their geometric properties. This format could be used for comparison, categorization, or educational purposes related to basic geometric shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y8EXCQVwZYaPGUTrtqFptQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadType( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y8EXCQVwZYaPGUTrtqFptQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClipBolt::HeadThickness

Specifies the thickness of the bolt head. If this value is either zero or negative,
the bolt head is not modeled.


None: 

IJUAhsClipBolt::HeadWidth

Specifies the width of the bolt head. If this value is either zero or negative, the
bolt head is not modeled.

Allowed values are:

![HeadWidth( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6YNQcKUeuF5uda_pBST90A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6cc435451f85789b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6YNQcKUeuF5uda_pBST90A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClipBolt::BoltOffset

Specifies the offset of the bolt from the origin of the beam clip shape. Following
graphics show BoltOffset for different beam clip shapes.

![BoltOffset( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1okSwtRacqmoQ12C4CX0KA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c0ce0e0296459fa2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1okSwtRacqmoQ12C4CX0KA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/329783?contentId=GXC5oTQLHZfOpFu5f6beIg)
The following properties are used to set the dimensions and location of the nut used
in the beam clip.

JUAhsShape1::Shape1Type

Specifies the graphic shape used for the nut or washer. This value uses the codelist
number defined in the hsShapeType sheet of the HS\_S3DParts\_Codelist.xls workbook.


Image:[Alt-Text: HeadType( Beam Clip Shape) 
Image-Analysis: The image displays three geometric shapes labeled with numbers and names indicating their types: 1 is a Round shape, 2 is a Square shape, and 3 is a Hexagon shape. Each shape is shown with a dotted outline and a small central circle. This may suggest a categorization or comparison of these basic geometric forms. The arrangement of the shapes side by side implies that they are part of a common grouping, possibly for educational or analytical purposes, illustrating the differences between these shapes in a visual format. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HRgotLitphqfEXlQiZmZ8w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadType( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HRgotLitphqfEXlQiZmZ8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shap1Width1

Specifies the outside dimension of the nut or washer.


Image:[Alt-Text: Shap1Width1 ( Beam Clip Shape) 
Image-Analysis: The image displays three geometric shapes along with corresponding labels. The first shape is a circle labeled "1 - Round," indicating it is a round shape. The second shape is a square labeled "2 - Square," representing a square shape. The third shape is a hexagon labeled "3 - Hex," illustrating a hexagonal shape. Each label associates with its respective shape to clarify their identities. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lrjE351b9~LyMBhWJ0L8Kw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Shap1Width1 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lrjE351b9~LyMBhWJ0L8Kw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Alt-Text: Shap1Width2 ( Beam Clip Shape) 
Image-Analysis: The image illustrates three different shapes: Round, Square, and Hex, each labeled with a number (1, 2, 3) and a brief description. The shapes correspond to specific characteristics or effects indicated in the text. The Round shape is labeled as "1 - Round," suggesting it may have a particular effect related to being circular. The Square shape is labeled as "2 - Square," indicating it might have a different effect associated with being square. The Hex shape is labeled "3 - Hex - No effect," which implies that it does not produce any noticeable effect. The relationship between these entities lies in their geometric properties and the effects they may or may not have. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mwJJn~vCNC~mtVjdiHjDnw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Shap1Width2 ( Beam Clip Shape)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mwJJn~vCNC~mtVjdiHjDnw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the length of the nut or washer.


Image:[Image-Analysis: The image depicts a schematic representation of an electronic component, likely a switch or a relay. At the top, there are two arrows indicating the opening and closing mechanism, suggesting a functionality that allows or interrupts the flow of current. Below this, there is a rectangular box that signifies the switch's body, with two horizontal lines inside it that could represent the contacts of the switch. Additionally, there are two red squares at the bottom which may symbolize activation buttons or indicators. Overall, the image illustrates the concept of a switch, indicating how it is operated and its basic structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wdNFCJy9sSgUFC8D5HL_Pw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wdNFCJy9sSgUFC8D5HL_Pw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325981?contentId=rVEQRwt3ATjQDaDg~Km2LA)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clevis Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328456?contentId=Dwsk339F_8TbZx3iT1QbmA)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsOpening1::Opening1

Specifies the distance from the pin centerline to the inside face of the end nut.


Image:[Image-Analysis: The image depicts two types of mechanical components, likely related to machinery or engineering. On the left side, there is a vertical hydraulic or pneumatic cylinder, characterized by a piston within a cylindrical housing. The red dots indicate points of interest, possibly representing ports for fluid entry or exit. The arrows suggest movement, implying that the cylinder can extend or retract based on the pressure applied. On the right side, there’s a rotary actuator or wheel mechanism, indicating a different type of movement, likely rotational. The black arrows between the two components denote a connection or relation, suggesting that one component may work in tandem with the other, possibly for a mechanism that converts linear motion into rotary motion or vice versa. There is also a circular shape at the bottom, likely representing a wheel or pulley, which is involved in the mechanism’s movement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yhaXJV0N8lAdWNH8oopPCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yhaXJV0N8lAdWNH8oopPCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Type

Specifies the codelist number of the shape type as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

1 - Round


Image:[Image-Analysis: The image depicts a mechanical device, possibly a type of valve or actuator. At the top, there is a circular component, which resembles a knob or a spherical cap, indicating it might be the actuator head. Below this, there is a rectangular body with a patterned interior suggesting an enclosure for mechanisms. There are red dots on the image, indicating points of interest or connection. The structure consists of vertical cylindrical parts on either side, which could represent guides or supports for the actuator. The base appears wider and has a more robust structure, possibly signifying a mount or foundation for stability. Overall, the image suggests a device that may control fluid flow or actuation in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XYCxhVAeJhkliu9BXC3_dA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XYCxhVAeJhkliu9BXC3_dA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image shows a diagram of a mechanical component, likely depicting some sort of hydraulic or pneumatic cylinder system. It consists of a rectangular box at the top with a circular hole, suggesting an area where a rod or another component can pass through. Below this, there is a main cylindrical structure with two vertical lines, indicating the sides of the cylinder, and it contains red dots that possibly represent key positions or points of interest in the mechanism. At the bottom, there are two additional components on either side, which could be base plates or attachment points, providing stability and support to the overall system. The dashed line above the cylinder indicates a separation between the upper and lower components, and the striped pattern on the cylinder may represent layering or different materials used in the assembly. Overall, the image provides a schematic representation of how the parts fit together in a mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZMcan1vJmPnOEtxHnzNoKw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZMcan1vJmPnOEtxHnzNoKw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image depicts a mechanical or structural component, possibly a type of fastening system or assembly. At the top, there is a hexagonal nut represented, which is typically used to secure bolts or screws. Below the nut, a square block is illustrated, which could represent a base or a mounting plate. The block has hatched shading, indicating it may be made from a different material or may have a specific function in the assembly. There are also red dots positioned beneath the block, likely indicating attachment points or bolt holes where screws or bolts would be inserted to secure the assembly. The overall structure suggests a relationship between fasteners (the nut and bolts) and a base component that holds or connects different parts together in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2xAYhFYUgKhUKGinslmG3g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2xAYhFYUgKhUKGinslmG3g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the end nuts. If this value is zero, the end nut
shapes are not displayed.

1 - Round


Image:[Image-Analysis: The image shows a diagrammatic representation of a mechanical system. At the top, there is a round element that may represent a bearing or a wheel. Below it, there is a vertical structure resembling a piston or a cylinder with a rectangular top portion. The red dots highlighted in the diagram likely indicate points of interest or specific locations pertaining to the operation or function of this mechanical system. The dotted line above the cylinder suggests a connection or tension above it, possibly indicating a load or force acting downward. The lower part of the cylinder connects to what appears to be a base, suggesting that this assembly is meant for vertical movement or hydraulic function. Overall, it represents elements typical in mechanical engineering or fluid mechanics, showcasing how parts may interact or function together. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tmiqZUHFmEzUaOnnMKxO3A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tmiqZUHFmEzUaOnnMKxO3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a mechanical or engineering design, specifically a type of assembly or structure involving a set of linked parts. At the top, there is a square component with a circular opening, which could suggest a fitting or a bearing mount. Below this, connected by a dashed line, is a rectangular body with vertical lines indicating the structure's height. There are also red dots at specific points in the structure, possibly indicating key locations for bolts or mounts. The base of the design features two side components that could represent stabilizers or supports, making this a visual representation of a mechanical assembly, likely used in applications that require mounting or support. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QFBdM_CyRW80UgVPlVA99A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QFBdM_CyRW80UgVPlVA99A-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image illustrates a mechanical assembly that appears to be a cross-section of a machine component, likely a type of mechanical press or clamping mechanism. At the top of the image, there is a hexagonal nut. Below the nut, there is a square component with diagonal hatching, indicating it might be a block or a faceplate of some sort. The square block is positioned above a cylindrical body which likely represents the main shaft or support structure of the mechanism. There are red squares highlighted on the structure, which may indicate points of interest, potentially indicating areas for application of force or attachment points. The dashed line above suggests a horizontal plane, and the vertical arrangement suggests that the system is designed to apply downward pressure or clamping force, making it suitable for various mechanical operations. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V~lyxKrHmOufFOxbhhcF0w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V~lyxKrHmOufFOxbhhcF0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the value only for NutShape2 (square). This value is used to create a rectangular nut instead of a square nut.
If the value is zero, or is not specified, NutShape2 is drawn as a square.


Image:[Image-Analysis: The image depicts a mechanical apparatus likely related to a piston mechanism or a similar engineered device. It consists of a top section represented by a rectangular block with a circular hole, indicating it may be a housing or guide for a piston. Below it, there is another rectangular section, which seems to be a piston or a similar component that fits into the upper area. The dashed line suggests there is movement involved between these parts, likely indicating how the piston operates within the cylinder. The red dots may represent key points for attention or measurement locations such as mounting points or centers of rotation. Overall, this image shows important relationships between parts in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ph3Sw6GSbdE_hnSY0TyV8A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ph3Sw6GSbdE_hnSY0TyV8A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the thickness of the end nut shape. Only positive values are acceptable.
If this value is zero or negative, the end nut shape is displayed.


Image:[Image-Analysis: The image depicts a hydraulic lift system, which is commonly used for lifting heavy objects. It features a rectangular hydraulic cylinder at the top, with a checkered pattern indicating a component, likely the piston. The vertical arrows next to the cylinder suggest motion, pointing upward and downward, indicating the lift's ability to raise and lower an object. Below the cylinder, there are two cylinders connected by a horizontal bar, representing the hydraulic actuator that provides the lifting mechanism. The red dots likely indicate points of interest or operational markers. This hydraulic system operates based on Pascal’s principle, where pressure applied to a confined fluid in a hydraulic system is transmitted undiminished throughout the fluid, resulting in the lifting action. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EHLFDDC_cOZJl34hXdL~BA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EHLFDDC_cOZJl34hXdL~BA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter2::Diameter2

Specifies the outside diameter of the round ends of the clevis. If this value is negative
or zero, the round ends are not drawn.


Image:[Image-Analysis: The image illustrates a simple engineering mechanism featuring a hydraulic press. It consists of several key parts: two large rectangular blocks labeled as the bodies of the press, depicted in a vertical arrangement. The hydraulic press functions by applying pressure to materials placed between these blocks. There is also a circular shape at the bottom right, which likely represents a pressure gauge or a component related to the functionality of the press. The image shows red dots that may indicate points of pressure application or key features to focus on for assembly or operation. Arrows are present to indicate directionality of movement or force within the mechanism. This design highlights the relationship between the components and the intended function of compressing materials. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ibO3sfIMxtZp8Hcq2hZpFg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ibO3sfIMxtZp8Hcq2hZpFg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the round ends of the clevis. If this value is negative,
then zero is used.


Image:[Image-Analysis: The image depicts a hydraulic system consisting of a hydraulic cylinder and a hydraulic piston. The left side shows a typical hydraulic cylinder with a fluid chamber and a piston rod extending from it. It has red markers indicating points of interest, possibly for assembly or operational indications. The right side features a simplified view of the hydraulic piston, illustrating its connection to the hydraulic system. This relationship indicates that fluid pressure is applied to the cylinder, resulting in the movement of the piston, which can perform work such as lifting or pushing objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v~uOlemPc4eBFK0bUjNpUw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v~uOlemPc4eBFK0bUjNpUw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap2::Gap2

Specifies the gap between the round ends of the clevis. If this value is negative,
then zero is used.


Image:[Image-Analysis: The image depicts a mechanical assembly that includes two hydraulic cylinders on the left side and a round component on the right side. The left part has two vertical cylinders connected by a horizontal element with a red dot indicating a specific point of interest, possibly as a reference or highlight. Each cylinder has a base with a mechanism for pushing and pulling, while the right side features a circular component that may signify a joint or pivot point. The arrows at the bottom likely illustrate movement directions, indicating how the components interact in a mechanical system. Overall, it appears to represent a part of a machine allowing linear and rotary motion. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kkAb9fGozp5KlJsbPKPlQw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kkAb9fGozp5KlJsbPKPlQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the width of the side blocks. If this value is negative or zero, the side
blocks are not drawn.


Image:[Image-Analysis: The image illustrates a hydraulic system. On the left, there is a hydraulic cylinder represented with two ends, shown in a vertical orientation. It contains two chambers and a red dot indicating a port. The arrows suggest that the hydraulic fluid can move in and out, controlling the cylinder's motion. On the right, there's a hydraulic pipe depicted in a horizontal orientation with arrows indicating the flow of hydraulic fluid. It connects to the cylinder, and the circular end possibly suggests another connected component, like a reservoir or another valve. This system shows how hydraulic force can be applied to create movement in mechanical applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GWddopucPyc5uPtOfD5d4w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GWddopucPyc5uPtOfD5d4w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the side blocks. If this value is zero, the software uses
the value defined for Thickness2. If this value is negative, the side blocks are not drawn. If both Thickness2 and Thickness3 values are 0, the side blocks are not drawn and a warning is displayed.


Image:[Image-Analysis: The image depicts two types of hydraulic components: on the left, there is a schematic representation of a hydraulic cylinder, and on the right, there is an illustration of a hydraulic piston. The left side shows a rectangular block with ports for hydraulic fluid entry and exit, indicating the working mechanism of the cylinder that enables linear motion. The arrows suggest the movement direction of the piston as fluid pressure varies. The right side illustrates a piston which is typically housed within the cylinders, showing how it moves when hydraulic fluid is introduced. The red squares likely represent the hydraulic fluid entry points or pressure indicators. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eW3c1DWfjfvYA3obGRYtOQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eW3c1DWfjfvYA3obGRYtOQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the amount by which the side blocks are to extend beyond the inside face
of the end nut shape.


Image:[Image-Analysis: The image depicts two types of hydraulic cylinders. On the left side, there is a double-acting hydraulic cylinder which has a piston that can move in both directions—indicated by the arrows showing force applied in either direction. It features two red dots likely representing ports for hydraulic fluid entry and exit. The right side shows a single-acting hydraulic cylinder which extends in one direction and relies on a spring or gravity to return to the initial position. Just below it, there is a circular icon which may signify the fluid reservoir or another component of the hydraulic system. This comparison emphasizes the different functionalities of double-acting versus single-acting hydraulic cylinders. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1JX_CDPHIzqYZauIFHLqTg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1JX_CDPHIzqYZauIFHLqTg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength2::OverLength2

Specifies the amount by which the side blocks are to extend beyond the bolt or pin
centerline. OverLength values are used when there is no need for a round end shape, resulting in the rectangular
side blocks being extended to hold the bolt or pin. This value can be positive or
negative. If a positive value is used, no round ends are shown.


Image:[Image-Analysis: The image depicts two hydraulic cylinders (also known as hydraulic actuators) shown in a side-by-side arrangement. Each cylinder consists of various components: the main body, a piston, and seals. The left cylinder has an identification marker in the form of red dots that indicate key components or positions. The arrows suggest the direction of motion of the pistons inside the cylinders when hydraulic fluid is applied. The left cylinder seems to focus on compression or retraction, while the right cylinder is shown in an extended position, demonstrating the movement capability of these hydraulic systems. Understanding the operation of hydraulic cylinders is fundamental in many mechanical systems where they are used for lifting or moving heavy loads. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NZGbKahcO6qlRtz44UlUJQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NZGbKahcO6qlRtz44UlUJQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt or pin. Use this property as a connection diameter
from the assembly information rule when joining between the clevis and eye nut. If
this value is zero, the pin is not drawn.


None:  An assembly information rule that joins a clevis to an eye nut reads Pin1Diameter from the clevis and passes it to the PinDiameter prompt of the eye nut.


Image:[Image-Analysis: The image depicts a basic schematic diagram of a hydraulic system, showcasing two hydraulic cylinders. On the left side, there's a vertical cylinder with a red dot indicating a position or measurement point, connected to a smaller rectangular base. On the right side, there’s a similar cylinder but presented differently, possibly implying a different mechanism or function, also with a red dot. At the bottom, a horizontal beam connects the two setups, indicating a shared base or supply line. The arrows on the diagram suggest the direction of fluid or force, illustrating the operation of the hydraulic system and its components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/p8MoQ8oZgv9__7EhDs9wWQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/p8MoQ8oZgv9__7EhDs9wWQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the bolt or pin. If this value is zero, the pin is not drawn.


Image:[Image-Analysis: The image consists of two mechanical parts that seem to be related to machinery or mechanical design. On the left, there's a representation of a linear actuator or a similar component, illustrated with three blocks stacked vertically and with red dots indicating points of movement or attachment. The central section has a rectangular base, suggesting it is grounded or fixed to a surface. The right side depicts a cylindrical object, possibly a bearing or a joint, connected to the actuator. The design emphasizes functionality in mechanism acts, where one part likely enables movement in a linear direction while the other allows rotation or pivoting, indicating a relationship between linear and rotational motion in machinery. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IwaLsHY4tYYhW581a5YG2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IwaLsHY4tYYhW581a5YG2w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dummy Leg Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361563?contentId=uxdC3yyyd4So4koqxDDz5Q)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dummy Leg shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361565?contentId=t89LfTDQn5i1L_1Zh7jjjw)
IJUAhsDummyShape::DummyShape

Specifies the dummy leg shape.

Allowed values for DummyShape are shown below. Allowed values are codelisted values from hsDummyStanc sheet of HS\_S3Dcodelist.xls.


Image:[Image-Analysis: The image displays two geometric shapes with corresponding numbers and labels. On the left side, there is a representation of a cylinder, indicated by "1=Cylinder," and on the right side, there is a representation of a square or rectangle, indicated by "2=Square/Rect." Each shape has small red squares at the top and bottom, likely indicating the bases or ends of the shapes. This visual comparison facilitates understanding the differences between these two 3D and 2D shapes, highlighting their distinct characteristics in form. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tLAqZcTqyyDf4xgKx6UedQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tLAqZcTqyyDf4xgKx6UedQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDummyHeight::DummyHeight

Specifies the total height of the dummy leg shape excluding base plate height. If
DummyHeight is not specified, then the shape is of variable length.


Image:[Image-Analysis: The image shows two similar diagrams that appear to represent mechanical systems involving circles and vertical structures. The left diagram features a circular object at the top, with vertical lines and solid connections below it. There are arrows indicating movement or measurement, suggesting a relationship between the two components. The right diagram shows a similar circular object and vertical structure but has different indications of movement, which could imply a different setup or configuration. The two diagrams likely illustrate different scenarios or states of the same mechanical system, showcasing how the relationships or dimensions between the objects change based on their configurations. The red squares in both diagrams might denote specific points of interest or areas where forces are acting in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NIoUjE6Yxd8gRszREyhgMA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NIoUjE6Yxd8gRszREyhgMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDummyWidth::DummyWidth

Specifies the width of the dummy leg. DummyWidth must be a positive value. If the dummy leg shape is round, then DummyWidth is used as the diameter.


Image:[Image-Analysis: The image depicts two types of electrical circuits or configurations involving coils (indicated by the circles) and possibly their magnetic fields or connections. The left configuration shows a simple straight vertical coil connected to a base, while the right one features a more complex arrangement with multiple connections and elements. Both configurations have marks or indications (possibly red marks) on key components, which likely denote points of interest such as connection nodes or points of measurement. The arrows at the bottom suggest a directionality or flow, possibly indicating current flow or the direction of signals within the circuits. Overall, the image highlights different electrical circuit setups and their complexities. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AYxyjvI3Xcu7tKgMCvQQQw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AYxyjvI3Xcu7tKgMCvQQQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDummyDepth::DummyDepth

Specifies the depth of the dummy leg shape. If the dummy leg shape is round, then
DummyDepth is not used.


Image:[Image-Analysis: The image shows two diagrams representing stress analysis in a structural element. The top diagram illustrates a vertical cut through a beam or structural member, with arrows indicating internal forces or stresses acting laterally at the cut. The presence of the red dots likely indicates points of application or locations of interest where these forces are analyzed. The lower diagram presents a similar setup but may represent a different state of stress or a different configuration, with the same overall approach to illustrating forces acting on the element. The side arrows in both diagrams suggest the direction of applied forces or reactions. Overall, these diagrams are used in engineering mechanics to analyze how structures respond to loading conditions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8vdoTuv8QBjGQfT0ChisEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8vdoTuv8QBjGQfT0ChisEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDummyDia::Diameter

Specifies the diameter of the pipe connected to the dummy leg. If Diameter is not specified, it is overridden by Diameter1 from the Dummy Leg part class.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Properties (Dummy Leg) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361570?contentId=aTSdbYQ_KVgI1KG2zZC3Ew)
IJUAhsDummyPlate::PlateShape

Specifies the plate shape. The top of the base plate is always attached to the bottom
of the dummy leg shape. If PlateShape is not specified, then the plate is not drawn.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties (Dummy Leg Shape) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361572?contentId=B5rNVjGUmKYEB1N4dKh1ZA)
IJUAhsIncludeBolts::IncludeBolts

Specifies whether bolts are included. Allowed values for IncludeBolts are

1- No bolts  
2- Bolts for bottom plate only  
3- Bolts for top plate only  
4- Bolts for both top and bottom plates

Allowed values are codelisted values from the hsIncludeBolts sheet of the HS\_S3Dcodelist.xls workbook.

IJUAhsPin1::Pin1Diameter

Specifies the pin diameter for all the bolts.

IJUAhsPin1::Pin1Length

Specifies the pin length for all the bolts.

IJUAOffset1::Offset1

Specifies the offset of each bolt row from the top shape.

IJUAhsMulti1::Multi1Qty

Specifies the quantity of bolts on one side of the plate. For example, when Multi1Qty is set to 2, the number of bolts on the plate are 4, 2 on each side of the plate. Bolts are not shown when Multi1Qty is set to zero.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0WCtr7Zcz1Biu8x702o2cQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=54008e8ce8d17e20)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0WCtr7Zcz1Biu8x702o2cQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Eye Nut Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328844?contentId=WatU1u3LVoAOU~mCKUcb4w)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsShape1::Shape1Type

Determines the graphic shape used for the nut or washer. Specifies the codelist number
in the hsShapeType sheet of the HS\_S3DParts\_Codelist.xls.


Image:[Image-Analysis: The image showcases three different geometric shapes: a circle, a square, and a hexagon. They are labeled numerically from 1 to 3. The first shape is a round circle, labeled as "1 - Round." The second shape is a square, labeled as "2 - Square." Lastly, the third shape is a hexagon, labeled as "3 - Hex." Each shape is outlined, with a smaller circle dot indicated in the center of each, possibly representing a focal point or an internal feature common to all shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/thJqjWfu_wzVPaiiXUnXbw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/thJqjWfu_wzVPaiiXUnXbw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the width of the oval shape that represents the threaded base of the eye
nut.


Image:[Image-Analysis: The image appears to depict a technical drawing or diagram showing a shape with a specific width. At the top, there is a rectangular shape that has a hole in it, labeled "Shape1Width". Below it, there is a stylized representation of the same shape, possibly indicating the view from a different angle. There are several red dots indicating specific points of interest, likely representing measurements or reference points on the shape. The dashed line could represent a measurement guide or a reference line for further drawings or construction details. This diagram may be used in engineering, design, or manufacturing contexts to convey precise dimensions of the shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c0nWjR_CGzChcov_V~1akg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c0nWjR_CGzChcov_V~1akg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer. This value can be used
to create a rectangle shape instead of a square. If this value is zero, negative,
or blank, Shape1Width1 is used.


Image:[Image-Analysis: The image depicts a technical drawing or diagram with two distinct sections. The left side illustrates a shape with various components, characterized by an outlined hexagonal-like figure with red dots indicating key points or measurements. This shape appears to have a width specified as "Shape1Width2", suggesting a relationship to dimensions or parameters being defined. On the right side of the image, a vertical rectangular shape is presented, which is likely a detailed view of the width or another section related to the first shape. The arrows indicate measurements or dimensions being adjusted or compared, emphasizing the importance of width in the design or analysis of these shapes. Overall, this image likely serves as a reference for understanding the dimensions and relationships between these two shapes, possibly in a engineering or architectural context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FEwAkHpa2NsTaTbdol6UsA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FEwAkHpa2NsTaTbdol6UsA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the height of the oval shape that represents the threaded base of the eye
nut.


Image:[Image-Analysis: The image depicts two different shapes, each represented in a side view. On the left, a shape labeled as "Shape1" is shown, with a rectangular central section and attachments that create a sort of frame. It has several red dots indicating key points or connections. On the right, there is a simplified version of the shape, emphasizing the length aspect of "Shape1." The arrows suggest measurement or movement, pointing to the height and length components of the shape. Overall, this image illustrates the structural characteristics of "Shape1" and its dimensional properties, which might be relevant in a mechanical or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FDitj6bJaBigaKq2O0rqoQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FDitj6bJaBigaKq2O0rqoQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness or outside diameter of the cylindrical stock that is used
to form the eye shape.


Image:[Image-Analysis: The image consists of two diagrams that illustrate a mechanical component, likely a fixture or gauge used to measure thickness. The left diagram shows a part being measured with dimensions and markers indicating key points (notably marked in red), including possible contact points or measurement locations. The right diagram demonstrates another view, emphasizing the thickness measurement with labeled arrows pointing to important features. The relationship between these diagrams suggests they represent different aspects or sides of the same component. The thickness indicated appears to be a crucial specification, which is detailed on the right side of the image. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sgWPjSyxQVsgBMS7vwUAGA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sgWPjSyxQVsgBMS7vwUAGA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerWidth1

Specifies the inside width of the eye shape at the oval threaded base.


Image:[Image-Analysis: The image consists of two panels illustrating a mechanical or structural component, likely a type of clamp or fixture. The left panel features a highly detailed view showing different parts of the component, marked with red dots indicating key points of interest. It highlights the "InnerWidth1," which is indicated by a blue arrow pointing to the gap between two vertical lines, suggesting a measurement within the component. The right panel is a simplified side view of the same component, providing a clearer perspective on its shape and function without the intricate details. Overall, the image serves to convey the dimensions and structure of this mechanical part as well as specific measurements that may be important for design or manufacturing. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZSzaLQEaLgCFs_XXE7dUfg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZSzaLQEaLgCFs_XXE7dUfg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerWidth2

Specifies the inside width of the eye shape at the InnerLength1 position along the inside of the eye.


Image:[Image-Analysis: The image presents a technical diagram depicting a mechanical or structural component with two parts shown side by side. On the left, there is a detailed illustration of a shape that seems to be a bracket or support structure, characterized by inner width labeled as "InnerWidth2," indicated by a blue arrow pointing to the measurement between the two wider sections of the figure. The red dots appear to mark specific points of interest on the structure, possibly representing attachment points or reference markers. On the right side of the image is a simpler representation or an orthographic view of the same component, emphasizing its overall shape without the detailed measurements seen on the left. The diagram provides a visual understanding of the component's physical dimensions and layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iaKmgTa52ImY2osYzUAWKg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iaKmgTa52ImY2osYzUAWKg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerLength1

Specifies the length at the position of InnerWidth2.


Image:[Image-Analysis: The image depicts a technical diagram likely related to engineering or design, featuring two different shapes: a hexagonal form and a rectangular form. The hexagonal shape is shown on the left with red markers indicating specific points of interest or measurement, shaded in red. The term "InnerLength1" is labeled next to an arrow pointing horizontally from the hexagon to demonstrate a measured distance, possibly referring to the internal dimension of the hexagon. On the right, there’s a rectangular shape that seems to be aligned with the hexagonal form. The vertical annotation next to the rectangle suggests measurements are being compared or noted between the two shapes, distinguishing their respective lengths. Overall, the diagram aims to clarify dimensions and relationships between these geometry forms. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2vw_ftrKSFI2fijc_0BK0A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2vw_ftrKSFI2fijc_0BK0A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerLength2

Specifies the inside of the eye shape.


Image:[Image-Analysis: The image depicts a diagram illustrating a mechanical component with various measurements labeled. On the left side, there is a hexagonal shape representing the inner structure of the component with dimensions marked by the red dots, which may indicate specific points of interest such as the corners or important connection points. The term "InnerLength2" is mentioned, likely referring to a specific measurement related to this inner shape. On the right side, there seems to be a rectangular component indicated, possibly showing a related outer dimension or a different aspect of the design. The arrows alongside suggest there are height or length measurements, helping the viewer understand the spatial relationships between the inner and outer components. Overall, this image serves as a technical reference for understanding the geometric and dimensional properties of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q81j_3uPoaOluShor3~w6A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q81j_3uPoaOluShor3~w6A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the amount that the rod extends past the oval threaded base.


Image:[Image-Analysis: The image illustrates a mechanical or structural configuration involving a central component labeled "OverLength1." This component is shown within a hexagonal shape, which may suggest a connection or relationship with other parts. The red dots indicate specific points of interest or measurements relevant to the structure's dimensions. The lines and arrows imply a focus on the lengths, possibly indicating that "OverLength1" is a critical measurement within the context of this design. The image helps convey the idea of how different lengths and components are related spatially, potentially in an engineering or architectural context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tfbSR3h_Chi~rAIQxNmP3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tfbSR3h_Chi~rAIQxNmP3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPinDiameter::PinDiameter

Specifies the diameter of the pin. The eye port represents the center of the connecting
pin and is located at one half of the PinDiameter value. It can also be an occurrence attribute and is editable on the property page.
This value can override the default location of the eye port.


Image:[Image-Analysis: The image depicts a diagram illustrating the concept of "Pin Diameter." On the left side, there is a detailed view of a pin assembly that includes a hexagonal body, with dimensions represented by lines and red dots indicating key measurement points. The terms "Pin Diameter" is labeled at the bottom, emphasizing the connection between the visual elements and the term. The right side of the image shows a simplified view of the pin assembly, which helps to clarify the overall shape and design of the pin. The relationship between the two views helps to convey the measurements and specifications needed for understanding pin diameter effectively. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vqyVLXk81y8u06DXaPoIhw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vqyVLXk81y8u06DXaPoIhw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Guide Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325984?contentId=zk9ZE6YnhTT0Kdm2YlQ78A)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fowWFetzWfrXQdEb2coLzw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9db30d0eda8944f7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fowWFetzWfrXQdEb2coLzw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Base Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325986?contentId=KrQqRNNG_yMQEafjYf5w_w)
IJUAhsWidth1::Width1

Defines the width of the base plate. Width1 is required if Thickness1 is greater than zero.

IJUAhsLength1::Length1

Defines the length of the base plate. Length1 is required if Thickness2 is greater than zero.

IJUAhsThickness1::Thickness1

Defines the thickness of the base plate. If Thickness1 is less than zero, the base plate is not included.


Image:[Image-Analysis: The image shows two rectangular blocks or components, one positioned on top of the other. The upper block has two red rectangular shapes (indicating some features or extensions) on its top surface, and the dimensions of the upper block are labeled with "Thickness1." The lower block has two red rectangular shapes on its sides, and it has dimensions labeled as "Length1" and "Width1." Together, the dimensions help in understanding the size and shape relationships of the components, with Thickness1 indicating the thickness of the upper block and Length1 and Width1 indicating the length and width of the lower block, respectively. This image likely serves as a technical reference or specification for these components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/orEgIZx3Lln_IYoF5a1ANQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/orEgIZx3Lln_IYoF5a1ANQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Vertical Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325988?contentId=9Mnvz1MZFeUB0rPB6b3i_g)
JUAhsWidth2::Width2

Specifies the width of the vertical plate.

IJUAhslength2::Length2

Specifies the length of the vertical plate.

IJUAhsThickness2::Thickness2

Specifies the thickness of the vertical plate.

IJUAhsGap1::Gap1

Specifies the gap between the two vertical plates.

IJUAhsOffset1::Offset1

Specifies the distance between the edges of the horizontal and vertical plates.


Image:[Image-Analysis: The image presents two diagrams that illustrate a structural component with measurements. In the top section, there is a vertical plate with dimensions for Offset1, Thickness2, and Gap1 labeled. These annotations signify the position and measurement of the vertical piece in relation to the base. The bottom section displays a rectangular shape with Length2 and Width2 indicated, highlighting its dimensions. The two diagrams are connected because the vertical plate is likely a part of the larger rectangular structure represented below, suggesting a mechanical or architectural design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NZBiT_QvlCgRN_rXJuwObw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NZBiT_QvlCgRN_rXJuwObw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsVerPlSecStand::VerPlSecStand

Specifies the section standard for the vertical plate.

IJUAhsVerPlSecSize::VerPlSecSize

Specifies the section size for the vertical plate.

IJUAhsVerPlSecType::VerPlSecType

Specifies the section type for the vertical plate.

IJUAhsAngle1::Angle1

Specifies the rotation angle of the first vertical section along its x-axis.

IJUAhsAngle2::Angle2

Specifies the rotation angle of the second vertical section along its x-axis.

IJUAhsConnection1::Connection1

Specifies the cardinal point of the first vertical section, which determines the connection
point of the steel section. For more details, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls workbook.

IJUAhsConnection2::Connection2

Specifies the cardinal point of the second vertical section, which determines the
connection point of the steel section. For more details, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls workbook.

IJUAhsMirrored1::Mirrored1

Specifies whether the first vertical steel section is mirrored or not. If you do not
specify, the software considers the section is not mirrored.

IJUAhsMirrored2::Mirrored2

Specifies whether the second vertical steel section is mirrored or not mirrored. If
you do not specify, the software considers the section is not mirrored.

IJUAhsSecConfig::SecConfig

Specifies orientation of the vertical steel section, vertical or horizontal. Enter
a codelist number from hsVertHoriz sheet of the HS\_S3DParts\_Codelist.xls workbook.


Image:[Image-Analysis: The image displays two configurations labeled "Horizontal" and "Vertical." On the left side, the "Horizontal" configuration consists of two structures side by side, represented by two shorter rectangular shapes connected by a red base. This design emphasizes a wide layout. On the right side, the "Vertical" configuration shows two taller rectangular shapes stacked on top of each other, also connected by a red base, illustrating a more upright arrangement. The contrasting orientations indicate different possible layouts for organizing space or elements, with "Horizontal" being more spread out and "Vertical" focusing on height. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bj65992ivys70pdVdcZxrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Bj65992ivys70pdVdcZxrw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Horizontal Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325991?contentId=MP~qLVYltz~PbgudS~j2Eg)
IJUAhsWidth3::Width3

Defines the width of the horizontal plate.

IJUAhsLength3::Length3

Defines the length of the horizontal plate.

IJUAhsThickness3::Thickness3

Defines the thickness of the horizontal plate.


Image:[Image-Analysis: The image displays a technical drawing with measurements for a structural element. The drawing features a horizontal plate supported by two vertical elements, with annotated dimensions for width and thickness. The upper section indicates the width and thickness of the horizontal plate, while the lower section provides a view showing the length of the element. The connection of these elements is critical for understanding the overall design, highlighting the hierarchical relationship between the horizontal plate and its supports. Each dimension is labeled to ensure clarity and precision in construction or fabrication. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PqLXJ3nP7XzTrtr8onsqSA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PqLXJ3nP7XzTrtr8onsqSA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHorPlSecStand::HorPlSecStand

Defines the section standard for the horizontal plate.

IJUAhsHorPlSecSize::HorPlSecSize

Defines the section size for the horizontal plate.

IJUAhsHorPlSecType::HorPlSecType

Defines the section type for the horizontal plate.

IJUAhsAngle3::Angle3

Specifies the rotation angle of the first horizontal section along its x-axis.

IJUAhsAngle4::Angle4

Specifies the rotation angle of the second horizontal section along its x-axis.


Image:[Image-Analysis: The image displays two sets of vertical structures on the left and right sides. On the left, there are two vertical bars connected by a horizontal red line. This aligns with concepts related to support or balance, possibly symbolizing stability. The right side has a similar vertical structure, with a square base depicted, suggesting a different arrangement or configuration. Above this structure, there is an arrow indicating movement or a relationship from one point to another, possibly illustrating a concept of connection, flow, or interaction between the two vertical structures. The overall design appears to depict a comparison or contrast between two systems or entities, emphasizing their structural and functional differences. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUNgDXs2onEr3EOK8LMuCg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUNgDXs2onEr3EOK8LMuCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsConnection3::Connection3

Specifies the cardinal point of the first horizontal section, which determines the
connection point of the steel section. For more details, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls workbook.

IJUAhsConnection4::Connection4

Specifies the cardinal point of the second horizontal section, which determines the
connection point of the steel section.

IJUAhsOffset2::Offset2

Specifies the offset of the horizontal section from the connection point.


Image:[Image-Analysis: {explanation='The image depicts a technical drawing or diagram that details a component or structure related to a system identified as "Offset2." At the top of the image, there are arrows pointing in both directions, which may indicate movement or adjustable settings. Below that is a central vertical element (likely a guide or rod) that connects to a broader rectangular section below it, which is outlined in red. The red rectangle possibly represents a base or a platform for the component above it. The dashed lines in the vertical element may suggest measurements or parameters for adjustment. Overall, the image seems to illustrate the geometry and relationships of different parts involved in the function of "Offset2."} 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wrcJWETamVaCMKrWqosHLA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wrcJWETamVaCMKrWqosHLA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Solid Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325995?contentId=RCj~xbM5HQCILH1pDGA4Sw)
IJUAhsSolidBaseVerPl::SolidBaseVerPl

Determines whether the base plate and the vertical plate is one solid shape. If you
specify Yes, the base plate and the vertical plate is one solid shape. If you specify No, separate solid shapes are used to create the base plate and the vertical plate.


None:  
Image:[Image-Analysis: The image shows a simple diagram with two vertical rectangles placed on top of a horizontal rectangle. Above this horizontal rectangle, there is the word "NO" written in a clear font. This could suggest a structured decision-making process, perhaps indicating that the conditions represented by the vertical rectangles do not meet the criteria for a positive result as suggested by the word "NO." The vertical rectangles might represent specific conditions, parameters, or options that are being evaluated in this context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5SlK8Ap~VamDSpvj1fc8Cg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5SlK8Ap~VamDSpvj1fc8Cg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSolidVerHorPl::SolidVerHorPl

Determines whether the horizontal plate and the vertical plate is one solid shape.
If you specify Yes, the horizontal plate and the vertical plate is one solid shape. If you specify No, separate solid shapes are used to create the horizontal plate and the vertical plate.


None:  
None: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328412?contentId=SIX2M7jP510ZmdTjLBAsxw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsShape1::Shape1Type

Specifies the graphic shape used for the nut or washer. This value uses the codelist
number defined in the hsShapeType sheet of the HS\_S3DParts\_Codelist.xls workbook.


Image:[Image-Analysis: The image depicts three distinct geometric shapes along with their respective labels. The shapes are as follows: 1 - Round, represented by a circle; 2 - Square, represented by a four-sided figure; and 3 - Hex, represented by a hexagon. Each shape has a small circle in the center, indicating a point or detail relevant to the shape. This image serves to categorize and differentiate these basic geometric forms. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/38HHfnHgs5l0NYYwtMSgQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/38HHfnHgs5l0NYYwtMSgQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shap1Width1

Specifies the outside dimension of the nut or washer.


Image:[Image-Analysis: The image features a diagram that presents three different geometric shapes, each labeled and described numerically. The shapes included are: 1. A Round shape, represented by a circle; 2. A Square shape, represented by a square; and 3. A Hex shape, represented by a hexagon. Each shape has a corresponding number to identify it and includes lines indicating the dimensions of the shapes. The use of different shapes suggests varying applications or classifications in a design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XeKhT_nnrex9cw3HqGLtsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XeKhT_nnrex9cw3HqGLtsg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Image-Analysis: The image presents a comparison of three different shapes: a round shape, a square shape, and a hexagonal shape (referred to as "Hex"). Each shape is numbered 1 to 3 for identification. The round shape is indicated as having a specific effect, while the square shape also shows a similar indication. The hexagonal shape is noted to have "No effect." This implies that the shapes may be related to some functional mechanism or design context, where the round and square shapes have effects while the hex does not. The arrangement visually distinguishes the three types and their classifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/d5OwvfiX48St1LYCRFZxnA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/d5OwvfiX48St1LYCRFZxnA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the length of the nut or washer.


Image:[Image-Analysis: The image depicts a simple electrical circuit layout. At the top, there are two arrows pointing towards a central component, indicating a flow of electric current towards the component. The arrows suggest a two-way flow, which implies that this component can handle current from both directions. Below the arrows is a rectangular box that represents a component of the circuit, possibly a switch or a relay. Inside the box, there are two red squares on top of parallel horizontal lines. This indicates a potentially switchable connection that can open (allow current to pass) or close (stop the flow of current) based on the position of the component. The design illustrates the functionality and control mechanism of an electrical circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wdNFCJy9sSgUFC8D5HL_Pw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wdNFCJy9sSgUFC8D5HL_Pw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328417?contentId=Vk7r0rOyvZxVpuYN4ZfAfg)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsPin1::pin1Diameter

Specifies the diameter of the pin. This value cannot be zero.


Image:[Image-Analysis: The image illustrates a technical diagram depicting the dimensions related to "Pin1Diameter." It features two shapes: one rectangular and one circular. The top part shows a rectangle with directional arrows indicating width, suggesting a rectangular pin with specified width dimensions. The bottom part presents a circle, also with directional arrows, indicating diameter dimensions for a circular pin. The term "Pin1Diameter" implies that these measurements pertain to the first pin in a mechanical or electrical context, likely for connectors or components where pin sizes are critical for functionality and compatibility. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bCj2KuUMnO5doe83rkt8Fg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bCj2KuUMnO5doe83rkt8Fg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the pin. This value cannot be zero.


Image:[Image-Analysis: The image illustrates a schematic or diagram likely related to an electronic component or connector. It features a vertical elongated shape that represents a pin or connector with a specified dimension labeled as "Pin1Length". There are two circular shapes, possibly indicating the ends of the pin, each of which may have a specific connotation, such as holes or connection points. Below the pin depiction, there is a horizontal dashed line, which could signify a reference plane or ground connection, leading to a smaller circular shape. This lower section appears to represent another component or a base connection for the pin. The relationship between these elements shows how the pin's length (Pin1Length) is a crucial measurement for its functionality and positioning within the context of the overall design or circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OraB1HM11hCRDJsk5jNvrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OraB1HM11hCRDJsk5jNvrw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325471?contentId=9YhARrQw18D4f3Hhmz6c9Q)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rod Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328436?contentId=MkqT1lYBcMTrI9TdjAyssQ)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsLength::Length

Defines the fixed length of the rod. You cannot modify this value during placement.


Image:[Image-Analysis: The image shows a rectangular shape with two red dots at both ends, and a horizontal line connecting them. Below this rectangle, the word "Length" is written, indicating that the image is demonstrating the concept of length as a measurement. To the right, there is a small circle, which likely represents a point or a location in space. The overall image visually represents the measurement of distance between the two red dots, emphasizing the concept of length in a geometrical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L49erM9hS9U~odAP6MgRog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/L49erM9hS9U~odAP6MgRog-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodDiameter::RodDiameter

Defines the outside diameter of the rod.


Image:[Image-Analysis: The image shows a diagram that explains the concept of "Rod Diameter." On the left, there is a rectangular shape with red dots on either side, which likely represents a rod or a shaft. On the right, there are symbols indicating measurement: a measuring line with arrows pointing down, implying that the dimension will be taken from that line. Below it, there is a circle, which might be indicating the cylindrical shape of the rod itself. The text "Rod Diameter" indicates that this diagram is focused on understanding or measuring the diameter of a rod. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fG_cncI0k4WElhch3_cziw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fG_cncI0k4WElhch3_cziw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shield Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325472?contentId=KFz3oW8nmexKR5ThY_96KQ)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Multi Position - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325473?contentId=kFsZC5b3KR9VrS3Kqhiqsw)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iVcMkO3rLynlmo_JHogsBw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4b65f316a963be96)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iVcMkO3rLynlmo_JHogsBw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QqIWYBzbWn8jrYIZGOForQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6e8f5698e069c639)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QqIWYBzbWn8jrYIZGOForQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shoe Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325447?contentId=gWWZG03pi5ac4pWQwhgfJw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsShoeType::ShoeType

Specifies the type of shoe. Enter a codelist number from the hsShoeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ooGAjrlsbRwX2UfxQPcuCQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dfe076cb81581e3d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ooGAjrlsbRwX2UfxQPcuCQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeHeight::ShoeHeight

Specifies the total height of the shoe including the base.


Image:[Image-Analysis: The image illustrates a simple system involving a pole and a circle with a dashed line around it, which seems to indicate a static equilibrium scenario where an unknown object or force is being analyzed, likely in a physics context. There is a vertical line labeled "Height," which may indicate the distance between the base of the pole and the top of the pole or another relevant height pertaining to the system. The small red squares present at the top and the bottom of the pole could represent specific points of interest or measurement in relation to the height discussed. The circular area might symbolize a space where an object is being observed or a field effect is present. Overall, this setup serves to evaluate heights and forces within this simple structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LFQeR2FEAveJ58D33zO4Lg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LFQeR2FEAveJ58D33zO4Lg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeWidth::ShoeWidth

Specifies the width of the shoe. You must enter a positive value.


Image:[Image-Analysis: The image depicts a diagram that illustrates a concept related to width in a technical context. At the top, there is a circular shape with a central point that is marked, indicating a feature or measurement point related to the main structure below. The main structure appears to be a vertical pole, which connects to a horizontal bar at the bottom, with arrows pointing outward to denote width. The label "Width" clearly indicates that the focus is on measuring the width of the horizontal component of the structure, likely in a mechanical or engineering context. The overall design helps in conceptualizing the relationship between height (implied by the pole) and width, which is specifically emphasized at the bottom of the image. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FD72U4Z3ODKAytm8asM5fg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FD72U4Z3ODKAytm8asM5fg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeLength::ShoeLength

Specifies the length of the shoe. You must enter a positive value.


Image:[Image-Analysis: The image visually represents a rectangular shape, presumably a block or a beam, with a clear indication of its length. There are red dots at both ends of the length measurement, emphasizing the start and end points of the length being measured. The word “Length” is prominently displayed beneath the rectangle, indicating that the main focus of the image is to illustrate this specific dimension. The dashed lines above the rectangle could indicate a top view or a detailed measurement line, further emphasizing the importance of the length measurement in this representation. Overall, the image serves as a simple educational diagram for understanding the concept of length in relation to a rectangular object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i~70U6hpenPdlrr3F1xygQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i~70U6hpenPdlrr3F1xygQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeShape::ShoeAngle

Specifies the slope angle of the pipe. Extension plates are sloped using this angle.

IJUAhsShoeSpaceFrm::ShoeSpaceFrm

Specifies the codelist value for the leg spacing. The following codelist values are
supported:

* 1 - Leg space is measured from the edge
* 2 - Leg space is measured from the center

IJUAhsVerticalLeg::LegLowerSpacing

Specifies the spacing of the legs at the bottom. This property is used with ShoeType
7. This value must be less than the ShoeSpacing value. For type 7, ShoeSpacing is the space of the legs at the top.

IJUAhsShoeTapLength::TaperedLength

Specifies the spacing upper side length of the leg.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lu4qrKOthu3IpqIc7VgEvw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=cad41baf15c2bebb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lu4qrKOthu3IpqIc7VgEvw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeTapAng::TaperedAngle

Specifies the angle of taper of the vertical leg.


Image:[Image-Analysis: The image shows a geometric shape referred to as a "Tapered Angle." It is represented as a truncated cone or frustum, with the top being narrower than the bottom. There is an arrow indicating a possible movement or rotation at the top left, which suggests that the shape can rotate along a vertical axis. The red dot at the bottom represents a point of interest, likely the center of the base of the shape. This configuration is often used in engineering and design contexts to discuss angles and shapes that taper from one width to another, which can influence structures or flow dynamics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5Vj1u3JTQU_QNAZBRSgJXw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5Vj1u3JTQU_QNAZBRSgJXw-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  Use TaperedLength or TaperedAngle to get tapered vertical members.

IJUAhsTaperStartFrom::TaperStartFrom

Specifies the length from the point at which the leg member starts.

IJUAhsTaper:Ends:TaperEnds

Defines the length from the point at which the tapering of the leg member ends from
the top of the leg.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yokQtdlbCxsvnddtH3jjCQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=660740a54608a44b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yokQtdlbCxsvnddtH3jjCQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsContinous::Continous

Specifies whether the shoe shape is continuous. Enter a codelist number from the hsYesNo sheet in the HS\_S3DParts\_Codelist.xls workbook.


None:  The Continuous option is not available for tapered shoe.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Vertical Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325453?contentId=iq1UJ8fEbtwqxDed1btSBQ)
IJUAhsShoeThickness1::ShoeThickness1

Specifies the thickness of the vertical plate. The value must be positive.


Image:[Image-Analysis: The image illustrates a geometric figure containing a vertical line, which represents a medium with a specific thickness referred to as "Thickness1." There are arrows on either side of the vertical line indicating the measurement of the thickness. Above the line is a dashed circle, possibly representing an area of interest or a related feature. The red dots at the base and in the center of the thickness line suggest points of reference or specific locations relevant to the geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AD3eWzCTrjxgOxEzSCOfcA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AD3eWzCTrjxgOxEzSCOfcA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsVertPlLen::VerticalPlateLength

Specifies the length of the vertical plate. The property is used only if plates are
used.


Image:[Image-Analysis: The image depicts a diagram labeled “VerticalPlateLength.” It shows a horizontal plate with arrows pointing to the left and right, indicating measurement or length. Beneath the plate, there is a small red dot likely representing a point of reference or measurement origin. The entire setup is focused on understanding the length of the vertical plate, suggesting that the image is likely part of a technical explanation related to measurements or specifications in a design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiBTWMxtTIz2Lisuc97BQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiBTWMxtTIz2Lisuc97BQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLegHeight::LegHeight

Specifies the height of the leg from the base of the shoe. If the value is blank,
the leg height is calculated automatically from the symbol code.


Image:[Image-Analysis: The image depicts a simple diagram that illustrates the concept of "Leg Height". There is a horizontal line representing the top of a piece of furniture (such as a table or chair) and a vertical arrow indicating the height of its legs. A red dot highlights a specific point, likely the point at which the height is measured. The term "Leg Height" is labeled at the bottom, suggesting that this measurement is important for understanding how tall the legs of an object are. This could be relevant for furniture design, ergonomics, or fitting furniture in a particular space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iZXXsxNUV1aVIL5s7hdObg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iZXXsxNUV1aVIL5s7hdObg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Base Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325457?contentId=HllFvwXD7x3NgD9IlXR0dQ)
IJUAhsShoeThickness2::ShoeThickness2

Defines the thickness of the base plate. The value must be positive; if it is zero,
the sides are not shown.


Image:[Image-Analysis: The image depicts a technical drawing or schematic that illustrates a component with a specific thickness indicated as "Thickness2." It includes an upper circular feature with a dashed line, suggesting it may be a hole or a cutout above a horizontal rectangular base. The base has a small red square, probably indicating a reference point or attachment location. Additionally, there are vertical arrows beside "Thickness2," which likely denote measuring dimensions related to the thickness of the rectangular base or the overall height of the component. This drawing is likely used in engineering or design contexts to specify dimensions of a part clearly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RnOLTazxzjfDsy8TbLBT4g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RnOLTazxzjfDsy8TbLBT4g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHorPlLen::HorizontalPlateLength

Defines the length of the horizontal plate.


Image:[Image-Analysis: The image depicts a horizontal plate with a length measurement indicated. At the top, there is a rectangle representing the plate itself, and at the center of the rectangle is a red dot. Beneath the plate, there are arrows pointing left and right to illustrate the length of the plate. The text "HorizontalPlat eLength" is positioned below, indicating that this is a diagram related to the horizontal plate's length. The red dot may signify a reference point for the measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c9_dWTnHmPjhfhunqhrEBA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c9_dWTnHmPjhfhunqhrEBA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Extension Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325460?contentId=E7OIzJ9rQgVijm0Ji5HI3w)
IJUAhsTopPlate::TopPlateThickness

Specifies the thickness of the top plate.


None: 

IJUAhsTopPlate::TopPlateHeight

Specifies the height of the top plate. If the value is zero, the height is calculated
from the symbol code based on the specified Gap and TopPlateOffset.


None: 

IJUAhsTopPlate::TopPlateLength

Specifies the length of the top plate.


Image:[Image-Analysis: The image depicts a diagram related to the measurement of a component labeled "TopPlateLength." It includes a rectangular shape that represents the top plate, with arrows at both ends indicating that a measurement is being taken. There are dashed lines that suggest a focus on the length between the two opposing arrows, emphasizing the distance across the top plate. The red dot at the bottom could indicate a specific reference point or origin for measurement. Overall, the diagram is likely used in a technical or engineering context to clarify how to measure the length of the top plate accurately. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MA34w_iVa2lSz6ZjbXb7WQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MA34w_iVa2lSz6ZjbXb7WQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTopPlate::TopPlateGap

Specifies the gap between the top of the shoe and the bottom of the pipe.


None: 

IJUAhsTopPlate::TopPlateOffset

Specifies the vertical downward offset of the extension plate from the top of the
shoe.


None: 

IJUAhsTopPlate::Inside

Determines whether the extension plate is attached to the inside or outside the vertical
plates. Enter codelist value 0 for inside or 1 for outside. The coldelist values are defined on the hsExtensionType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsTopPlate::Extension

Specifies if the extension plate is used or not. Extension plates are not supported
for ShoeTypes 7, 8, 9 and 10.


look for icon that looks like a laptop or computer with a screen and keyboard: 

IJUAhsExtPltOff::ExtensionPlateAxialOffset

Specifies a value to offset the extension plate along the x-axis of the pipe.


Image:[Image-Analysis: The image illustrates the concept of "Axial Offset," which is represented visually through a simple diagram. The diagram features a rectangular block positioned above a base with an indication of movement to the left and right. The arrows, along with the dashed lines, typically indicate the range of the offset in the axial direction. Below this, there is a red dot, which might represent a reference point or center. Overall, the image aims to convey how an object can be offset from a central or original position along its axis, which is an important consideration in various engineering and mechanical contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aqcyV6c7kpqb6QgmGDBn_g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aqcyV6c7kpqb6QgmGDBn_g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Steel Section Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325468?contentId=eph866EuNP9uGbPOWWQ9wg)
IJUAhsSteelSection::SteelName

Specifies the steel section name.

IJUAhsSteelSection::SteelType

Specifies steel section type name.


None:  If SteelType is set to Pipe, then the section is placed in a vertical orientation. All other types
place in a horizontal orientation.

IJUAhsSteelSection::SteelStandard

Specifies steel section standard.

IJUAhsSteelCPoint::SteelCpoint

Specifies the cardinal point of the steel section.

Cardinal points

Cardinal points specify anchor locations on a steel section. The following 15 cardinal
positions are available. They are defined on the CrossSectionCardinalPoints codelist sheet in the Allcodelists.xls workbook.

1. Bottom Left
2. Bottom Center
3. Bottom Right
4. Center Left
5. Center
6. Center Right
7. Top Left
8. Top Center
9. Top Right
10. Centroid (Center of Gravity)
11. Centroid Bottom
12. Centroid Left
13. Centroid Right
14. Centroid Top
15. Shear Center

The location of cardinal points 10 (center-of-gravity) and 15 (shear center) depend
on the section shape. The local z-axis of the member and the center-of-gravity point
of the section define cardinal points 11 and 14. The local y-axis of the member and
the center-of-gravity point of the section define cardinal points 12 and 13. The locations
of the cardinal points are shown below for the different steel sections. Because cardinal
points 10 to 15 are specific to each section shape, only cardinal points 1 to 9 are
shown in the images:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Rqzim4ER70Mmj5peQXq7SQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=31e2942d2889e205)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Rqzim4ER70Mmj5peQXq7SQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhssteelAngle::SteelAngle

Specifies the rotation angle of the steel section along its x-axis. The property determines
the angle by which the steel section is rotated along its length. The steel section
is anchored on the specified cardinal point when it is rotated. In the image shown
below, the T-section is anchored at cardinal point 2. After the angle of the steel
is rotated by 90 degrees, the steel section is positioned where the dotted line is
located.


Image:[Image-Analysis: The image depicts a simple flowchart or diagram consisting of horizontal and vertical lines, resembling a T-junction. The green line at the top represents a horizontal pathway that leads to a vertical pathway below it, forming a "T" shape. The point marked with a red square labeled "2" indicates a specific position on the diagram where perhaps an analysis, decision, or an action may take place. Following the vertical pathway from "2," there is a dashed line indicating a connection to another vertical segment on the right side of the image, suggesting that there may be additional processes or decisions branching out from this point. Overall, the diagram appears to illustrate a process or pathway, indicating how different components relate and connect with one another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6Z2vJtXa4jLd7XfJc1~dlw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6Z2vJtXa4jLd7XfJc1~dlw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Slide Plate Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/326000?contentId=L8I7yRFflbnlSrlG7bjBKw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Stanchion Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361424?contentId=s48jqBwfOi5UJ8GXKgZHTw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

For stanchion shape, IsStanchion is always to set to Yes.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Stanchion Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361427?contentId=~R59gBvKNLzaFa~TiIaP0Q)
IJUAhsStanShape::StanShape

Specifies the stanchion shape. Stanchion shape can be used as either top shape or
bottom shape of the part. Stanchion shape can be used in IJUAhsBotShape::BotShape or IJUAhsTopShape::TopShape (at part class level). Allowed values are

1 - Cylinder  
2 - Square/Rectangle  
3 - Standard Steel

The above values are codelisted values from the hsDummyStanc sheet of the HS\_S3Dcodelist.xls workbook.

Bottom Shape


Image:[Image-Analysis: The image displays a legend defining three different shapes used in a technical or engineering context. Each shape is labeled with a number and a description: 1 represents a "Cylinder," 2 identifies a "Square/Rect" shape, and 3 signifies a "Standard Steel Shape." The shapes are accompanied by red dots, likely indicating points of interest or connection in a diagram where these shapes may be used. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_GqznEL6Iq_4hlKGQLTzqw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_GqznEL6Iq_4hlKGQLTzqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Top Shape


Image:[Image-Analysis: The image contains three labeled shapes with corresponding numbers, indicating different types of structural shapes used in engineering or construction. Each shape is illustrated with a diagram and has a specific numeric identifier: 1 indicates a Cylinder, displayed as a solid vertical cylinder, 2 represents a Square/Rectangle shape, shown as a rectangular box, and 3 denotes a Standard Steel Shape, also depicted as a rectangular form. Each shape is marked with red dots at both ends, likely to indicate connection points or specific features related to the structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1Xih24XEe1shRBDDny8unw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1Xih24XEe1shRBDDny8unw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStanHeight::StanHeight

Specifies the total height of the stanchion shape excluding the plate height. If StanHeight is not specified, then the shape is of variable length.


Image:[Image-Analysis: The image features two labeled diagrams representing different shapes: "Bottom shape" and "Top Shape." Each diagram illustrates a cylindrical object with a dashed outline, red dots indicating significant points, and vertical lines demonstrating measurements. The "Bottom shape" diagram shows the cylindrical form oriented horizontally, while the "Top Shape" diagram presents it in a vertical orientation. The connection between these two shapes is likely related to their applications, measurements, or transformations in design or engineering contexts, emphasizing the geometrical characteristics of the cylindrical object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MVpRhHpJplp14EU0P~2XKA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MVpRhHpJplp14EU0P~2XKA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStanWidth::StanWidth

Specifies the width of the stanchion. StanWidth must be a positive value. If the stanchion shape is round, then StanWidth is used as the diameter. If the stanchion shape is set to standard steel, then StanWidth is not used.


Image:[Image-Analysis: The image shows two distinct shapes labeled "Bottom shape" and "Top Shape." Each shape consists of a combination of circles and rectangles, with specific markings. The "Bottom shape" features a circular component at the top with a red dot inside, followed by a rectangular section with red dots at the bottom and horizontal arrows indicating movement or flow. The "Top Shape" is similar but oriented differently, with the circular component on top of another rectangular section, also containing red dots and horizontal arrows. Both shapes likely represent different configurations or orientations of a system, emphasizing the relationship between the components and their structural significance. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LJhEz9m1keUW1SFp6iwDKA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LJhEz9m1keUW1SFp6iwDKA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStanDepth::StanDepth

Specifies the depth of the stanchion shape. If the stanchion shape is either round
or standard steel, then StanDepth is not used.


Image:[Image-Analysis: The image depicts a diagram of a pneumatic cylinder with connectors at the top and bottom. The cylinder is represented by a rectangular shape in the center, with dashed lines indicating the outline of the cylinder. There are arrows pointing toward the cylinder from the left and right, which signify the air pressure entering from both sides. At the bottom, there are two horizontal arrows indicating the movement of the piston within the cylinder, suggesting that it can move up and down. The red dots symbolize points of air entry or seals on the cylinder. This type of setup is commonly used in machinery for various applications, such as automation and actuation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QB781jTQTVWEkC3g9o4M6w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QB781jTQTVWEkC3g9o4M6w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Steel Section properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361562?contentId=JuYD1sPcKPty54dWNHHJCw)
If StanShape = 3, use the below properties.

IJUAhsSteelSection::SteelName

Specifies the steel section name.

IJUAhsSteelSection::SteelType

Specifies the steel section type.

IJUAhsSteelSection::SteelStandard

Specifies the steel section standard.

IJUAhsSteelAngle::SteelAngle

Specifies the rotation angle of the steel section along its X-axis.

IJUAhsSteelCPoint::SteelCpoint

Specifies the cardinal point of the steel section.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361558?contentId=4HK76WSP2Rfzs4derdJaSQ)
IJUAhsPlate1::Plate1Shape

Specifies the base plate shape. The top of the base plate shape is always attached
to the bottom of the stanchion shape. If Plate1Shape is not specified, then the base plate is not drawn.


Image:[Image-Analysis: The image depicts a simple schematic of a vertical structure resembling a pole or tower with a circular top, which is often indicative of a simple antenna or a stand with a signaling device. The top of the structure has a circular element, which might represent an antenna disk, and there are red colored points, potentially signaling function points or areas of interest on the antenna. The base of the pole is rectangular, suggesting some form of grounding or support for the vertical element above. The overall structure appears to represent a conceptual model for an antenna system, illustrating the relationship between the antenna itself and its base. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bAa9WKAc7vVnchC4_uBzjA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bAa9WKAc7vVnchC4_uBzjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPlate::Plate2Shape

Specifies the load plate shape. The bottom of the load plate is always attached to
the top of the stanchion shape. Plate2Shape is optional if two stanchion shapes are used. If Plate2Shape is not specified, then the load plate is not drawn.


Image:[Image-Analysis: The image depicts a simplified diagram of a basic mechanical system. It illustrates a vertical shaft labeled with a red dot at the top, indicating a point of rotation or motion. Below the shaft, there is a rectangular base structure, along with a dashed line suggesting movement or support. The overall design implies a simple mechanical component, possibly a simplified representation of a machine part or a basic pivot point. The use of red dots might indicate points of interest or specific areas that involve action or focus in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cBp7erRCtbaH1rLwniIsXw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cBp7erRCtbaH1rLwniIsXw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties (Stanchion Shape) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361561?contentId=dvMRZYG1l2JzA6bkGeFyZw)
IJUAhsIncludeBolts::IncludeBolts

Specifies whether bolts are included. Allowed values for IncludeBolts are

1- No bolts  
2- Bolts for bottom plate only  
3- Bolts for top plate only  
4- Bolts for both top and bottom plates

Allowed values are codelisted values from the hsIncludeBolts sheet of the HS\_S3Dcodelist.xls workbook.

IJUAhsPin1::Pin1Diameter

Specifies the pin diameter for all the bolts.

IJUAhsPin1::Pin1Length

Specifies the pin length for all the bolts.

IJUAOffset1::Offset1

Specifies the offset of each bolt row from the top shape.

IJUAhsMulti1::Multi1Qty

Specifies the quantity of bolts on one side of the plate. For example, when Multi1Qty is set to 2, the number of bolts on the plate are 4, 2 on each side of the plate. Bolts are not shown when Multi1Qty is set to zero.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0WCtr7Zcz1Biu8x702o2cQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=54008e8ce8d17e20)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0WCtr7Zcz1Biu8x702o2cQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325983?contentId=mJlspurTb9NyFizA04n~eQ)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Turnbuckle Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328642?contentId=LQLkRbcV5n_Nw0MgRe07eQ)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsOpening1::Opening1

Specifies the inside distance between the two units. This value can be zero.


Image:[Image-Analysis: The image depicts a basic schematic of an electrical double-layer capacitor, also known as a supercapacitor. It shows two main capacitor plates (represented by the horizontal rectangular shapes) with red dots indicating the presence of charge. The arrows on the top indicate the direction of the electric field between these plates. This type of capacitor is designed to store and release electrical energy quickly. The lines connecting the plates suggest the electrical connections to a circuit, demonstrating how supercapacitors can be integrated into electronic designs for energy storage and release applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eTEdO1btVfHZqDhGGkZUUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eTEdO1btVfHZqDhGGkZUUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Type

Specifies the codelist number of the shape type as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.


None:  In each of the following examples, the end nut shape is drawn with hatched lines.

1 - Round


Image:[Image-Analysis: The image consists of two parts: on the left side is a diagram depicting a cylindrical component known as a coupling, which typically connects two shafts in a mechanical system. It features two parallel bars on either end with red dots indicating connection points, suggesting the alignment or the place where the shafts will be inserted. The right side of the image shows a top view of this coupling, illustrating its circular shape and confirming its role in providing rotational movement between two parts while allowing for some misalignment. Overall, this image is highlighting the functional aspect of couplings in machinery. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0U90rzZy4MbLMXsn6JRlww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0U90rzZy4MbLMXsn6JRlww-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a mechanical assembly consisting of two main components: a cylindrical connector and a square component. The cylindrical connector is shown with textured surfaces and is likely designed for fitting into another part, such as a pipe or a shaft. The red dots may indicate points of interest, such as attachment points or sensors. The square component on the right appears to be a housing or connector point, possibly for electrical or hydraulic connections. This illustration suggests a mechanical system where the two components interact, possibly for transmitting force or signals. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/szjxZjaz~ayqfKoDdG3NTg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/szjxZjaz~ayqfKoDdG3NTg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image displays two components typically found in mechanical or engineering contexts. On the left, there is a representation of a coupling mechanism, which shows a cylindrical part connected to two flanged ends. This component is used to connect two shafts together in machinery. The red dots may indicate alignment marks or points that need to be considered during installation. On the right, there is a depiction of a hexagonal nut which is used in conjunction with a bolt to fasten components together securely. The hexagonal shape allows for a wrench to grip the nut effectively, providing leverage for tightening or loosening. Together, these components illustrate the relationship between connecting shafts and securing them using fasteners in mechanical systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/F7GQVbMULV6J15aupn83yw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/F7GQVbMULV6J15aupn83yw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the end nuts. If this value is zero, the end nut
shape is not displayed.

1 - Round


Image:[Image-Analysis: The image depicts a mechanical component called a "coupling," which is used to connect two shafts together for the purpose of transmitting power. The left part of the image shows a side view of the coupling, illustrating the two shafts that it connects. The red dots may indicate points where adjustments or alignments can be made. The right part of the image provides a top view, highlighting the inner and outer structure of the coupling as well as how it fits around the shafts. The arrows indicate the movement or alignment directions for maintenance or adjustments. Overall, the image shows both the assembly and the operational context of a coupling in machinery. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZzH9_5tjI7mD_z4WPoTjaA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZzH9_5tjI7mD_z4WPoTjaA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image depicts a mechanical device that appears to involve a coupling or connection between two components. On the left side, there are two sections that seem to represent two shafts being connected, indicated by the horizontal lines and the visible divider in the middle. The two red dots may signify points of alignment or connection. On the right side, there is a vertical movement shown with an arrow pointing up and down, suggesting that this device may allow for some sort of movement or adjustment between the connected shafts. Overall, the image illustrates a mechanism designed for coupling two separate elements while allowing for flexibility or movement, which may be important in various engineering or mechanical applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/je4QwWlm4p6LKx47rXRWpw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/je4QwWlm4p6LKx47rXRWpw-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image appears to depict a mechanical component, specifically a type of coupling used in machinery. On the left side, there are two cylindrical parts which represent the ends of a shaft that are joined by the coupling. The red dots likely indicate points where the coupling connects to these shaft ends. The right side shows a cross-section of the coupling with measurements indicated, suggesting how it is designed to accommodate motion or transmission of torque between the two shafts. The upward and downward arrows likely represent movement or alignment features of the coupling, while the hexagonal shape indicates where a tool might be used to tighten or loosen the coupling. This component is essential in ensuring that rotational motion is efficiently transferred from one shaft to another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YgInMOGG3qwmcdwq_tKQDQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YgInMOGG3qwmcdwq_tKQDQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the outside length of the end nut shapes. If this value is zero, the value
specified in Shape1Width1 is used. This value is not used for the hex shape.

1 - Round


Image:[Image-Analysis: The image depicts a cylindrical object (possibly a spool or a tank) represented by an oval shape on top, with arrows on either side indicating horizontal expansion or movement. This suggests functionality related to storage or transport, as the arrows indicate the ability to extend or retract horizontally. The circular shape on top may imply a central opening or the possibility of rotation, adding to the utility of the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HX5gKkj5Y5wt~fodQngPEw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HX5gKkj5Y5wt~fodQngPEw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


icon that looks like a horizontal slider control or adjustment knob, often used for adjusting width or size: 

IJUAhsShape1::Shape1Length

Specifies the thickness of the end nut shape. If the value is negative, the end nut
shapes are located within Opening1. If this value is set to zero, the end nut shape is not displayed.

Shape1Length < 0 (Negative)


Image:[Image-Analysis: The image depicts a mechanical or structural component with a central opening labeled "Opening1." This opening is flanked by two rectangular shapes, which likely represent some kind of fixture or support structure. The arrows on either side indicate movement or flow, possibly suggesting that the central mechanism or opening allows for passage or alignment of parts. The two small red dots inside the central area might indicate specific points of interest, contact points, or connections to other components. Overall, this illustration seems to focus on the dimensions and alignment of the central opening in relation to the surrounding structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vIYb9zRfpluqdMxEdSMiYg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vIYb9zRfpluqdMxEdSMiYg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Shape1Length > 0 (Positive)


Image:[Image-Analysis: The image depicts a basic electrical circuit featuring a capacitor. The circuit diagram has two distinct parts: on the left, there is a symbol resembling a battery or power source, and on the right, there are two capacitor symbols, which are rectangular shapes with parallel lines. In the center of the diagram, there are red dots indicating the connection points of the capacitors. The diagram illustrates how the capacitors are arranged within the circuit, highlighting the flow of electricity and the role of capacitors in storing electrical energy. This setup is commonly used in various electronic applications, where capacitors act to smooth out voltage fluctuations and provide energy storage. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Gp3WiTk6zoXqjtKvA5qPJg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Gp3WiTk6zoXqjtKvA5qPJg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the length of the side blocks. If this value is zero, the side blocks are
not displayed.


Image:[Image-Analysis: The image appears to be a technical drawing or schematic of a cylindrical object, possibly a component like a coupling, bearing, or shaft, used in mechanical applications. It displays multiple views of the object: a side view that shows its length with dimensions indicated by double-headed arrows, and a cross-sectional view that reveals its internal structure. The red dots in the side view may indicate points of interest or critical dimensions. The right side illustration is a front view of the object, which helps to understand its circular profile. The surrounding box with dashed lines likely denotes the space or housing where this component will be installed, giving an idea of how it fits within a larger assembly or system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOI01A42lKAzcuBelpFSFg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOI01A42lKAzcuBelpFSFg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the width of the side blocks. If this value is zero, the side blocks are
not displayed.


Image:[Image-Analysis: The image depicts a schematic of a DC motor and its connection to a power supply. On the left side, there is a representation of the DC motor with its armature bars shown in a cylindrical form. It has terminals where connections are made, indicated by small squares. The motor is illustrated with red dots at the terminals, signifying where the electrical connections are established. The right side shows a simple diagram of the motor's electrical connections with arrows indicating the flow of current. This implies the directional nature of current in relation to the motor's operation, which is essential for understanding how the motor turns and performs work when powered. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6ek0xFxd4eSptOmW59GV7Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6ek0xFxd4eSptOmW59GV7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the side blocks. If this value is zero, the side blocks
are not displayed.


Image:[Image-Analysis: The image depicts a schematic of a solenoid valve. On the left side, the structure of the valve is shown with arrows indicating the flow direction of a fluid. The valve contains a spool that moves up and down as represented by the arrows, controlling the flow through the valve's ports. The red squares likely indicate actuator positions or flow control points. On the right side, there is a simplified top view of the valve showing its circular outline, which can represent the valve's orientation and structure from above. The image visually explains how the solenoid valve functions to control the passage of fluids based on the movement of the internal components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/En03RiCuIG1chK132Vlb6w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/En03RiCuIG1chK132Vlb6w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOpening2::Opening2

Specifies the opening between the two side blocks. Ignore this value to prevent blocks
from being displayed.


Image:[Image-Analysis: The image presents a diagram that illustrates a control system involving two elements: a controller and a process. In the center, there is a block (representing a controller) that receives input signals and adjusts the output accordingly. The red elements indicate points where the input and output are being measured or fed back into the system. The surrounding blocks symbolize different processes or components that are being regulated by the controller. The arrows demonstrate the direction of signal flow, indicating that the controller influences the processes based on the feedback received. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5qmmcd~1IutLiEKFMs8w7g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5qmmcd~1IutLiEKFMs8w7g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

This value is optional. Specifies the diameter of the round center tube. This property
is normally used for a turnbuckle without side blocks, but it can be used for either.
The tube is modeled with the same length as the Opening1 value and is fitted between the two nut end shapes. If this value is zero, the center
tube is not displayed.


Image:[Image-Analysis: The image depicts a basic representation of a mechanical component, likely a coupling. It features two rectangular shapes on the left and right, which represent the ends of shafts or components to be connected. The central section shows a cylindrical connector with arrows indicating the direction of force or torque transmission between the two components. The arrows suggest that the coupling facilitates motion or force transfer from one side to the other. Overall, this image illustrates the concept of connecting two parts to function as a single unit in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vgEzijMXX8ZpvR61vof4bA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vgEzijMXX8ZpvR61vof4bA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325982?contentId=4qQBd7ZCq2P~Nmk_8p90fQ)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. Enter a codelist number from the HS\_S3DParts\_Codelist.xls workbook on the hsSmartShapeType sheet.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Welded Beam Attachment Shape - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328883?contentId=nexn74USRDCUSDsjc59LDw)
IJUAhsSmartShapeType::SmartShapeType

Specifies the classification of the shape. This property uses the codelist number
defined in the hsSmartShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Legal Information - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/989785?contentId=_caTzT5a2mgqLAPlhkSXIw)
# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Copyright Notice - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/90257?contentId=UoLLc_VFD7Bj~kzOLRT3GQ)
Copyright

Copyright © 2001-2025 Hexagon AB and/or its subsidiaries and affiliates.

This computer program, including software, icons, graphic symbols, documentation,
file formats, and audio-visual displays; may be used only as pursuant to applicable
software license agreement; contains confidential and proprietary information of Intergraph
Corporation or a Hexagon Group Company and/or third parties which is protected by
patent, trademark, copyright law, trade secret law, and international treaty, and
may not be provided or otherwise made available without proper authorization from Hexagon AB and/or its subsidiaries and affiliates.

Portions of this software are owned by Spatial Corp. © 1992-2025. All Rights Reserved.

Portions of the user interface Copyright © 2008-2025 Progress Software Corporation
and/or its subsidiaries or affiliates. All Rights Reserved.

U.S. Government Restricted Rights Legend

Use, duplication, or disclosure by the government is subject to restrictions as set
forth below. For civilian agencies: This was developed at private expense and is "restricted
computer software" submitted with restricted rights in accordance with subparagraphs
(a) through (d) of the Commercial Computer Software - Restricted Rights clause at
52.227-19 of the Federal Acquisition Regulations ("FAR") and its successors, and is
unpublished and all rights are reserved under the copyright laws of the United States.
For units of the Department of Defense ("DoD"): This is "commercial computer software"
as defined at DFARS 252.227-7014 and the rights of the Government are as specified
at DFARS 227.7202-3.

Unpublished - rights reserved under the copyright laws of the United States.

Intergraph Corporation, Hexagon's Asset Lifecycle Intelligence Division  
305 Intergraph Way  
Madison, AL 35758

Documentation

Documentation shall mean, whether in electronic or printed form, User's Guides, Installation
Guides, Reference Guides, Administrator's Guides, Customization Guides, Programmer's
Guides, Configuration Guides and Help Guides delivered with a particular software
product.

Other Documentation

Other Documentation shall mean, whether in electronic or printed form and delivered
with software or on Smart Community, SharePoint, box.net, or the Hexagon documentation
web site, any documentation related to work processes, workflows, and best practices
that is provided by Hexagon as guidance for using a software product.

Terms of Use

1. Use of a software product and Documentation is subject to the Software License Agreement
   ("SLA") delivered with the software product unless the Licensee has a valid signed
   license for this software product with Intergraph Corporation, Hexagon’s Asset Lifecycle
   Intelligence Division ("Hexagon"), a Hexagon Group Company. If the Licensee has a
   valid signed license for this software product with Hexagon, the valid signed license
   shall take precedence and govern the use of this software product and Documentation.
   Subject to the terms contained within the applicable license agreement, Hexagon gives
   Licensee permission to print a reasonable number of copies of the Documentation as
   defined in the applicable license agreement and delivered with the software product
   for Licensee's internal, non-commercial use. The Documentation may not be printed
   for resale or redistribution.
2. For use of Documentation or Other Documentation where end user does not receive a
   SLA or does not have a valid license agreement with Hexagon, Hexagon grants the Licensee
   a non-exclusive license to use the Documentation or Other Documentation for Licensee’s
   internal non-commercial use. Hexagon gives Licensee permission to print a reasonable
   number of copies of Other Documentation for Licensee’s internal, non-commercial use.
   The Other Documentation may not be printed for resale or redistribution. This license
   contained in this subsection b) may be terminated at any time and for any reason by
   Hexagon by giving written notice to Licensee.

Disclaimer of Warranties

Except for any express warranties as may be stated in the SLA or separate license
or separate terms and conditions, Hexagon disclaims any and all express or implied
warranties including, but not limited to the implied warranties of merchantability
and fitness for a particular purpose and nothing stated in, or implied by, this document
or its contents shall be considered or deemed a modification or amendment of such
disclaimer. Hexagon believes the information in this publication is accurate as of
its publication date.

The information and the software discussed in this document are subject to change
without notice and are subject to applicable technical product descriptions. Hexagon
is not responsible for any error that may appear in this document.

The software, Documentation and Other Documentation discussed in this document are
furnished under a license and may be used or copied only in accordance with the terms
of this license. THE USER OF THE SOFTWARE IS EXPECTED TO MAKE THE FINAL EVALUATION
AS TO THE USEFULNESS OF THE SOFTWARE IN HIS OWN ENVIRONMENT.

Hexagon is not responsible for the accuracy of delivered data including, but not limited
to, catalog, reference and symbol data. Users should verify for themselves that the
data is accurate and suitable for their project work.

Limitation of Damages

IN NO EVENT WILL HEXAGON BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL INCIDENTAL,
SPECIAL, OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO, LOSS OF USE OR PRODUCTION,
LOSS OF REVENUE OR PROFIT, LOSS OF DATA, OR CLAIMS OF THIRD PARTIES, EVEN IF HEXAGON
HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

UNDER NO CIRCUMSTANCES SHALL HEXAGON'S LIABILITY EXCEED THE AMOUNT THAT HEXAGON HAS
BEEN PAID BY LICENSEE UNDER THIS AGREEMENT AT THE TIME THE CLAIM IS MADE. EXCEPT WHERE
PROHIBITED BY APPLICABLE LAW, NO CLAIM, REGARDLESS OF FORM, ARISING OUT OF OR IN CONNECTION
WITH THE SUBJECT MATTER OF THIS DOCUMENT MAY BE BROUGHT BY LICENSEE MORE THAN TWO
(2) YEARS AFTER THE EVENT GIVING RISE TO THE CAUSE OF ACTION HAS OCCURRED.

IF UNDER THE LAW RULED APPLICABLE ANY PART OF THIS SECTION IS INVALID, THEN HEXAGON
LIMITS ITS LIABILITY TO THE MAXIMUM EXTENT ALLOWED BY SAID LAW.

Export Controls

To the extent prohibited by United States or other applicable laws, Intergraph Corporation,
Hexagon's Asset Lifecycle Intelligence division ("Hexagon"), and a Hexagon Group Company's
commercial-off-the-shelf software products, customized software, Technical Data, and/or
third-party software, or any derivatives thereof, obtained from Hexagon, its subsidiaries,
or distributors must not be exported or re-exported, directly or indirectly (including
via remote access) under the following circumstances:

1. To Cuba, Iran, North Korea, Syria, or the Crimean, "Donetsk People's Republic", "Luhansk
   People's Republic," or Sevastopol regions of Ukraine, or any national of these countries
   or territories.
2. To any person or entity listed on any United States government denial list, including,
   but not limited to, the United States Department of Commerce Denied Persons, Entities,
   and Unverified Lists, the United States Department of Treasury Specially Designated
   Nationals List, and the United States Department of State Debarred List. Visit www.export.gov
   for more information or follow this link for the screening tool: <https://legacy.export.gov/csl-search>.
3. To any entity when Customer knows, or has reason to know, the end use of the software
   product, customized software, Technical Data and/or third-party software obtained
   from Hexagon, its subsidiaries, or distributors is related to the design, development,
   production, or use of missiles, chemical, biological, or nuclear weapons, or other
   un-safeguarded or sensitive nuclear uses.
4. To any entity when Customer knows, or has reason to know, that an illegal reshipment
   will take place.

Any questions regarding export/re-export of relevant Hexagon software product, customized
software, Technical Data, and/or third-party software obtained from Hexagon, its subsidiaries,
or distributors, should be addressed to Hexagon’s Export Compliance Department, 305
Intergraph Way, Madison, Alabama 35758 USA or at exportcompliance@hexagon.com. Customer
shall hold harmless and indemnify Hexagon and a Hexagon Group Company for any causes
of action, claims, costs, expenses and/or damages resulting to Hexagon or a Hexagon
Group Company from a breach by Customer.

Trademarks

Intergraph®, the Intergraph logo®, Intergraph Smart®, SmartPlant®, SmartMarine®, SmartSketch®, SmartPlant Cloud®, PDS®, FrameWorks®, I-Route, I-Export, Isogen®, SPOOLGEN, SupportManager®, SupportModeler®, SAPPHIRE®, TANK, PV Elite®, CADWorx®, CADWorx DraftPro®, GTSTRUDL®, and CAESAR II® are trademarks or registered trademarks of Intergraph Corporation or its affiliates,
parents, subsidiaries. Hexagon and the Hexagon logo are registered trademarks of Hexagon
AB or its subsidiaries. Microsoft and Windows are registered trademarks of Microsoft
Corporation. ACIS is a registered trademark of SPATIAL TECHNOLOGY, INC. Infragistics,
Presentation Layer Framework, ActiveTreeView Ctrl, ProtoViewCtl, ActiveThreed Ctrl,
ActiveListBar Ctrl, ActiveSplitter, ActiveToolbars Ctrl, ActiveToolbars Plus Ctrl, and ProtoView are trademarks of Infragistics, Inc. Incorporates portions of 2D DCM, 3D
DCM, and HLM by Siemens Product Lifecycle Management Software III (GB) Ltd. All rights
reserved. Gigasoft is a registered trademark, and ProEssentials a trademark of Gigasoft, Inc.
VideoSoft and VXFlexGrid are either registered trademarks or trademarks of ComponentOne LLC 1991-2024, All
rights reserved. Oracle, JD Edwards, PeopleSoft, and Retek are registered trademarks
of Oracle Corporation and/or its affiliates. Tribon is a trademark of AVEVA Group
plc. Other brands and product names are trademarks of their respective owners.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Anti-Piracy Statement - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/96409?contentId=FnUOJ16bpYY9wpNR8~W~bA)
When you purchase or lease Hexagon’s Asset Lifecycle Intelligence division software,
Hexagon, or its affiliates, parents, subsidiaries retains ownership of the product.
You become the licensee of the product and obtain the right to use the product solely
in accordance with the terms of the Intergraph Corporation, doing business as Hexagon’s
Asset Lifecycle Intelligence division, Software License Agreement and applicable United
States and/or international copyright laws.

You must have a valid license for each working copy of the product. You may also make
one archival copy of the software to protect from inadvertent destruction of the original
software, but you are not permitted to use the archival copy for any other purpose.
An upgrade replaces the original license. Any use of working copies of the product
for which there is no valid Intergraph Corporation, doing business as Hexagon’s Asset
Lifecycle Intelligence division, Software License Agreement constitutes Software Piracy
for which there are very severe penalties. All Hexagon software products are protected
by copyright laws and international treaty.

If you have questions regarding software piracy or the legal use of Hexagon software
products, please call the Legal Department at 256-730-2362 in the U.S.

Updated June 2022

Document No. DDGL562C0# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Customer Support - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/96433?contentId=BLyrZtoIV3NqIAB0LpvpdA)
For the latest support information for this product, go to the [Smart Community](https://hexagon.com/support-success/asset-lifecycle-intelligence/community) site.