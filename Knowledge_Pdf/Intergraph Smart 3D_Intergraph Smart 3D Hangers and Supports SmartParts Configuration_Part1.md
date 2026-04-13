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

###### [What's New in Hangers and Supports SmartParts Configuration Reference - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/812313?contentId=TrTxNFdSov9_u6BXaVx3Rw)
The following changes have been made to Hangers and Supports SmartParts configuration
reference data.


look for a gradient image that transitions from green to blue: 

Version 14 Update 4 (available August 2025)

* No changes were made to the documentation for this release.


look for a gradient image that transitions from green to blue: 

Version 14 Update 3 (available May 2025)

* No changes were made to the documentation for this release.


look for a gradient image that transitions from green to blue: 

Version 14 Update 2 (available February 2025)

* No changes were made to the documentation for this release.


look for a gradient image that transitions from green to blue: 

Version 14 Update 1 (available November 2024)

* No documentation changes were made for this release.


look for a gradient image that transitions from green to blue: 

Version 14 (available September 2024)

* No documentation changes were made for this release.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [SmartParts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306573?contentId=jMg0cKRimW58YcY80sUkkA)
This is a comprehensive set of support parts from Hexagon Asset Lifecycle Intelligence. They have been designed with more flexibility so that they can be configured without
any programming.

Copy and rename part sheet into your own workbook and edit the supplied attributes
in the workbook to model your part accordingly. Section 1 describes all of the attributes
available for each part type. The actual parts delivered in HS\_S3DParts.xls are not
real vendor parts. They are examples of some of the parts that can be made with the
SmartPart concept. For actual vendor SmartParts, see the SmartParts for Vendors described
in Section 2 of this document. More vendor parts will continually be added in future
versions of the software.

|  |  |
| --- | --- |
| Workbook | HS\_S3DParts.xls |
| Codelist | HS\_ S3DParts\_Codelist.xls |

Prerequisites

Make sure that the following base bulkload files in [Product Folder]\CatalogData\BulkLoad\DataFiles\ are already bulkloaded:

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelist.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.


None:  All the SmartParts share a set of common properties. For more information on general
properties, see [Common SmartPart Attributes](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/fBNaj2LeE_aS00dKYo9Jqw).

[Customer Support](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/CNr79AuyrLtoA53q4KF0fg)  
[Anti-Piracy Statement](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/c4oVaOboHagkhJQohvAmsA)  
[Copyright](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/XWkxxCXG8s_7C6Ncc17xRQ) © 2001-2025 Hexagon Asset Lifecycle Intelligence and/or its subsidiaries and affiliates  
Version 14 Update 4  
Published on 6/25/2025 at 5:29 PM# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Common SmartPart Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/334116?contentId=v9xVLFXpDcxVL8W65xMSRg)
IJOAhsMaterialEx::MaterialType

Type a value from the MaterialType column of Material sheet. The Material sheet is in the AllCommon.xls workbook.

IJOAhsMaterialEx::MaterialGrade

Type a value from the MaterialGrade column of Material sheet. The Material sheet is in the AllCommon.xls workbook.

IJCoatingInfo::CoatingRequirement

Type a codelist number or text from the CoatingType sheet of the AllCodeLists.xls workbook.

IJCoatingInfo::CoatingType

Type a codelist number or text from the CoatingType sheet of the AllCodeLists.xls workbook.

IJCoatingInfo::CoatingColor

Type a codelist number or text from the CoatingColor sheet of the AllCodeLists.xls workbook.

IJUAhsCatalog::Catalog

Type a codelist number or text from the hsSupCatalog sheet of the HS\_System\_Codelist.xls workbook.

NDFrom

Type the minimum nominal diameter for which the part can be used. This option is only
used for a part used for conduit and pipe assemblies.

NDTo

Type the maximum nominal diameter for which the part can be used. This option is only
used for a part used for conduit and pipe assemblies.

NDUnitType

Type the units for the NDFrom and NDTo values.

DryWeight

Type the dry weight of the support component. For variable length parts (for instance,
Strut parts) implement IJHgrSymbolWCGServices interface and use the IJHgrSymbolWCGServices\_EvaluateLocalWCG function to calculate the weight of the part. For parts that have a constant weight
plus some variable length component, add IJUAhsWtPerLen::WtPerLen and IJUAhsWeight::Weight columns in the Partclass sheet. DryWeight = (WtPerLen \* VarLength) + Weight. Here, weight is the dry weight of the constant length part.

DryCogX

Type the X-axis location of the dry center-of-gravity.

DryCogY

Type the Y-axis location of the dry center-of-gravity.

DryCogZ

Type the Z-axis location of the dry center-of-gravity.


None:  If DryCogX, DryCogY, and DryCogZ values are not provided, the software automatically calculates these values. WetCogX, WetCogY, and WetCogZ have the same values as DryCogX, DryCogY, and DryCogZ respectively.

MirrorBehaviorOption

Type the code that represents the mirror behavior for the part. Valid codes are listed
in the AllCodeLists.xls workbook on the MirrorBehaviorOption sheet in the Codelist Number column. This option is not valid for hanger parts and
hanger assemblies.

IJHgrBOMDefinition::BOMType

Type the code that defines how the BOMDescription attribute for this part will be
set. Valid codes are listed in the AllCodeLists.xls workbook on the HngSupBOMType sheet. If no value is entered, the BOM description for the part defaults to the PartDescription
text. For smart parts, use BOMType as 2 to set the BOM description to the PartDescription
value.

IJOAhsEmbeddedPart::EmbeddedPart

This is a True/False value that is common to all smart parts. It should be set to
True if the part is embedded in concrete. It is used for reporting purposes.

IJOAhsComponentNotes::ComponentNotes

This is a text field in which the user can type any text that is common to all smart
parts. A report can then be written to display any special notes on a part. Also,
the MTO report on a drawing could be extended to add a column to show these notes
if needed.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Beam Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/330168?contentId=WXEh2Xa4_OMSgamgNBaiGA)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.BeamClamp  
Part Name: Beam Clamp  
Part Description: Beam Clamp SmartPart

![Beam clamp](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RvF~3lH32NoLAivVtsrq8Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6914c9aa71733001)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RvF~3lH32NoLAivVtsrq8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Beam Clamp SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Beam Attachments > Beam Clamp as shown below.

![beam clamp part placement](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1FAhowP0RziKd3F8oApcgg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=171b19c3dd116948)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1FAhowP0RziKd3F8oApcgg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Alt-Text: Local Coordinate System 
Image-Analysis: The image shows a technical drawing or diagram related to a structural design or machining setup. On the left side, there is a depiction of a component with a point of interest marked in red. This is likely showing how the component fits or interfaces with another part. The right side presents a view that outlines the coordinate reference system used for the structure, indicating the X, Y, and Z axes. The "Structure: 0,0,0" notation specifies a reference point or origin in a 3D space, which is critical for understanding positioning and alignment in machining or structural analysis. The use of different views helps in visualizing the relationship and orientation of components in the context of the specified coordinate system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/67D6vNiFj6FiXwzNVVDFfw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Local Coordinate System](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/67D6vNiFj6FiXwzNVVDFfw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Beam Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/330172?contentId=UfwOPPYgmN2Wx2QENguidA)
These properties define the geometry of a beam clamp.


None:  For these properties, millimeters (mm) is the default unit of distance. Use "in" at the end of the dimensional value to specify inches.

IJUAHsBeamClamp::LeftClipShape

Specifies the name of the beam clip shape that is placed on the left side of the steel.
If no value is specified then there will not be any left clip in the beam clamp.


Image:[Alt-Text: LeftClipShape (Basic Beam Clamp Properties) 
Image-Analysis: The image displays two block letters "C" and "T" designed in an outline format. The letter "C" appears on the left side, formed by a single stroke that curves around, open to the right. On the right, the letter "T" is shown, which consists of a vertical line that extends downwards and a horizontal line at the top. This style of representation emphasizes the shapes of the letters using minimalistic outlines without any fill color or additional details. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1eCaP0RLLny5yXM4ZYoHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![LeftClipShape (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b1eCaP0RLLny5yXM4ZYoHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

For more information on beam clip shape, see [Beam Clip Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/0lNV9sR6jdS5pncW~Um9kQ).

IJUAhsBeamClampGap::LeftClipGap

Specifies the gap between steel and left clip. If this value is zero, then there is
no gap between the clip and the steel.


Image:[Alt-Text: LeftClipGap (Basic Beam Clamp Properties) 
Image-Analysis: The image depicts a mechanical clamp system used for holding workpieces securely during machining or assembly. It shows a vertical screw mechanism that applies pressure to a workpiece by pushing it against a horizontal surface. The arrow indicators at the bottom suggest the clamp's adjustable nature, allowing it to move inwards or outwards to accommodate different sizes of materials. The combination of the clamp's screw and the base provides stability to hold the workpiece firmly in place while work is being performed on it. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BydI2d3KV9~CJbYFKNSJ3A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![LeftClipGap (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BydI2d3KV9~CJbYFKNSJ3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsBeamClampHOff::LeftOffsetH

Specifies the horizontal offset where the RodEnd1 port needs to be placed on left clip. Both, positive and negative values are allowed.
If LeftOffsetH is not provided then the RodEnd1 port is at bottom.

If the LeftOffsetH value is positive,


Image:[Alt-Text: LeftOffsetH 1 (Basic Beam Clamp Properties) 
Image-Analysis: The image contains two diagrams that illustrate mechanical or structural components, likely related to piping or flow systems. The left side presents a setup with components including a valve depicted with a solid line and a dotted line indicating a connection, possibly showing different flow directions or closed/open states. There are indicators with red dots that might represent operational states or key monitoring points of the system. The right side of the image appears to be another system layout demonstrating a similar configuration but arranged differently. Arrows at the bottom suggest directional flow or operational constraints, highlighting how components may interact within the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H0jjoU~HD1u02JyBq0ZASQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![LeftOffsetH 1 (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H0jjoU~HD1u02JyBq0ZASQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the LeftOffsetH value is negative,

![LeftOffsetH 2(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HzhyO2Gnklnnss3FJzXPAA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=daa5719f2c66e30c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HzhyO2Gnklnnss3FJzXPAA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsBeamClampVOff::LeftOffsetV

Specifies the Vertical offset from where the RodEnd1 port needs to be placed on left clip. It is used to locate the J Bolt and Left /
Right Bolts. Both, positive and negative values are allowed.

If the LeftOffsetV value is positive,


Image:[Alt-Text: LeftOffsetV 1(Basic Beam Clamp Properties) 
Image-Analysis: The image illustrates a mechanical system including various components and their interactions. It appears to show a sequential process involving movement along vertical and horizontal axes indicated by arrows. The arrows pointing up and down signify movement or the potential for a force action, while the horizontal line represents a guided structure or pathway for one or more parts. The rectangular shapes likely depict mechanical parts such as pistons or blocks, with some being highlighted or colored for emphasis (e.g., the blue part). The relationship between these components indicates an assembly where movements might translate into a sequential action, potentially in a manufacturing or engineering context. Dotted lines might imply either hidden components or paths for electric signals or force transfer that aren't depicted in solid lines, creating a layered understanding of how energy, movement, and system functions are interconnected. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VPxUyiowYY_fY_qsH3nHEw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![LeftOffsetV 1(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VPxUyiowYY_fY_qsH3nHEw-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the LeftOffsetV value is negative,

![LeftOffsetV 2(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HDbr2Hu4aMw3J6avQzybGQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=43985628223d5600)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HDbr2Hu4aMw3J6avQzybGQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsBeamClamp::RightClipShape

Specifies the clip shape to be placed on the right side of the steel. If the RightClipShape value is not specified, no right clip is placed on the beam clamp.


Image:[Alt-Text: RightClipShape(Basic Beam Clamp Properties) 
Image-Analysis: The image features a stylized drawing of the number "1" alongside the number "2", both represented in a unique, artistic font. The "1" is more prominent and appears to be in a vertical position, while the "2" is at a lower and slightly off-centered position, suggesting a visual hierarchy where "1" is more significant. This arrangement could imply a sequential relationship, potentially indicating a ranking or an ordered list, where "1" denotes the first position and "2" the second. The simplicity of the design removes distractions, focusing attention on the numerical representation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_tYM2g3T57RA3C2VWtvTwg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RightClipShape(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_tYM2g3T57RA3C2VWtvTwg-_PVFQNoCl4XmjAxWO0f7XQ/content)

For more information on beam clip shape, see [Beam Clip Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/0lNV9sR6jdS5pncW~Um9kQ).

IJUAhsBeamClampGap::RightClipGap

Specifies the gap between steel and the right clip. If this value is not set, then
the default value assigned is zero and there is no gap between the right clip and
the steel.


Image:[Alt-Text: RightClipGap(Basic Beam Clamp Properties) 
Image-Analysis: The image depicts a technical diagram likely related to a mechanical or structural component. It shows a T-shaped beam or support, with a detail of a joint or connection point at the top. The arrows at the bottom imply some kind of movement or adjustment, possibly indicating the tension or compression within the structure. The lines and shapes are typical for engineering drawings, which often delineate parts, connections, and stresses within an assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wiyR2JefdzWShy4axUMdPw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RightClipGap(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wiyR2JefdzWShy4axUMdPw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsBeamClampHOff::RightOffsetH

Specifies the horizontal offset from where the RodEnd2 Port needs to be placed on right clip. Both, positive and negative values are allowed.
If RightOffsetH is not provided then the RodEnd2 Port will be at bottom port.

If the RightOffsetH value is positive,


Image:[Alt-Text: RightOffsetH 1(Basic Beam Clamp Properties) 
Image-Analysis: The image consists of two mechanical diagrams illustrating the assembly of a clamp or fastening mechanism. The left diagram depicts a side view of the structure, showing the hierarchy of elements including a base and two attachment points indicated by small red circles. The blue line suggests a connection or flow, while the dashed line may represent a separate or flexible part that is not in direct contact with the main components. The right diagram presents a more solidified view with clearer definitions of parts, including a bolt at the top and compartments indicated by arrows that suggest movement or adjustment along the horizontal axis. The arrows on both ends of the right diagram imply that the fastening mechanism may allow for tightening or shifting, emphasizing the functional aspect of these components in maintaining a secure hold. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/erVq~1UbkrZCcj2TQ_Bxtg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RightOffsetH 1(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/erVq~1UbkrZCcj2TQ_Bxtg-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the RightOffsetH value is negative,

![RightOffsetH 2(Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jyqsJYyWXPxCKsReyK2PqA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=536cd27eec414d02)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jyqsJYyWXPxCKsReyK2PqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsBeamClampVOff::RightOffsetV

Specifies the vertical offset from where the RodEnd1 port needs to be placed on right clip. The offset is calculated between the origin
of the clip, the Top port (the blue colored point on the left shape). If RightOffsetV is not provided, then the RodEnd1 Port will be on horizontal offset (if RightOffsetH is provided) from Bottom port.

If the RightOffsetV value is positive,


Image:[Alt-Text: RightOffsetV 1 (Basic Beam Clamp Properties) 
Image-Analysis: The image depicts a technical diagram that appears to represent a system of elements, possibly in an engineering or architectural context. It includes multiple geometrical shapes such as rectangles and lines, indicating different components or levels of a system. The shapes' arrangements also suggest a hierarchical structure, where components are organized according to their function or position. The red and blue markers may indicate specific points of interest or connection, possibly denoting inputs or outputs in the system. Additionally, there are arrows at the top and bottom, which might represent the flow of information or resources. Overall, this image seems to illustrate relationships between various elements in a structured manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/icP1s__ACPaABKXVMvdB2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RightOffsetV 1 (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/icP1s__ACPaABKXVMvdB2w-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the RightOffsetV value is negative,

![RightOffsetV 2 (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6KiTEnYM76k1U0otr72yPg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b73d95a67b67cb25)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6KiTEnYM76k1U0otr72yPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsBottomShape::BottomShape

Specifies the bottom shape of the beam clamp. A beam clamp can have one or two beam
clips and an optional bottom shape. The value for this column is a codelist number,
and valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook in the hsBeamClampBotShape sheet.


Image:[Alt-Text: BootomShape (Beam clamp Properties 
Image-Analysis: The image displays a diagram illustrating the shapes of three different letters: I, C, and U. Each letter is represented visually, with numerical labels indicating their corresponding numbers (1, 2, and 3). The letter "I" is shown with two vertical lines connected by a horizontal line at the top, representing the letter's structure. The letter "C" is displayed as a curved line open on one side, while the letter "U" is represented with two vertical lines connected at the bottom by a horizontal line, forming a U shape. This visual representation likely serves as a mnemonic or educational tool to help recognize or learn these letters based on their distinct shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GFK9KWzC0TM6A8IDb6W~rA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BootomShape (Beam clamp Properties](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GFK9KWzC0TM6A8IDb6W~rA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies the gap between the two clip shapes. It is only applicable to P and Q type
clip shapes.


Image:[Alt-Text: beam clamp_gap 
Image-Analysis: The image represents a technical diagram, likely pertaining to a mechanical or structural component. It features a prominent central part that resembles a shape similar to a T or cross. The diagram includes several red dots that likely indicate points of interest, such as measurement points or connection points. The surrounding lines appear to create a detailed layout, suggesting joints or fittings, possibly associated with plumbing or piping systems. Additionally, two horizontal arrows at the bottom imply a measurement width or separation between parts, underscoring the importance of spacing in the design. This configuration may highlight how different components relate and connect to each other within a larger assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ASqP1GRjOhp9a_ofp2uRxg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![beam clamp_gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ASqP1GRjOhp9a_ofp2uRxg-_PVFQNoCl4XmjAxWO0f7XQ/content)

![beam clamp_gap_1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BCe8Zxu4AKIJHdQfdsS~BQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=79210960c0e32ed2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BCe8Zxu4AKIJHdQfdsS~BQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/331054?contentId=pztW9GRcTIKnoUK2X3j03A)
These properties define the geometry of the bottom shape of the beam clamp.

IJUAhsThickness1::Thickness1

Specifies the thickness of the bottom shape.


Image:[Alt-Text: Thickness1 (Basic Beam Clamp Properties) 
Image-Analysis: The image consists of various types of arrows and shapes that represent different forms of forces or directions in a mechanical or structural context. The top section shows two horizontal lines with arrows indicating movement or force direction. In the middle section, there are two arrows positioned horizontally, suggesting tension or compression. The bottom section illustrates a U-shaped or L-shaped object with arrows indicating possible forces acting on it. Overall, the image likely conveys concepts related to physics or engineering, particularly focusing on the effects of forces on different structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lo1D9rAxAafN60Del5DQjQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Thickness1 (Basic Beam Clamp Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lo1D9rAxAafN60Del5DQjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the width of the bottom shape.


Image:[Alt-Text: Width1 (Beam Clamp) 
Image-Analysis: The image depicts a physics or engineering concept. On the left, there is a rectangular shape, which likely represents a beam or a similar structural element. On the right, there are two arrows pointing downwards, which indicate the direction of force being applied to the beam. This setup suggests that the beam is experiencing vertical loading. The implication is that the theory or principle being illustrated is likely related to how beams react to applied forces, possibly in the context of stress, strain, or deflection in structural analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b29DxI0r7WWecX7FU_SGgQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Width1 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b29DxI0r7WWecX7FU_SGgQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the first height of the bottom shape. For shape I, this property will be
ignored.


Image:[Alt-Text: Height1 (Beam Clamp) 
Image-Analysis: The image depicts a schematic design that appears to represent a connection or a flow diagram involving two horizontal structures connected by vertical elements. The diagram shows a top view of two rectangular shapes, which might represent containers or pathways, with arrows indicating a direction of flow or movement. The arrows point downward, suggesting a gravitational influence or a flow downwards from the upper structures to the lower area, where it likely collects or distributes something. This diagram could be indicative of a system in engineering or physics, for instance, illustrating a fluid flow or material pathway in a machinery design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XQPlbfkxQJWDzvLpPtDbyQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Height1 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XQPlbfkxQJWDzvLpPtDbyQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the second height of the bottom shape. For shape I and shape C, this property
will be ignored.


Image:[Alt-Text: Height2 (Beam Clamp) 
Image-Analysis: The image depicts a schematic representation of a cross-section of a specific type of container or channel, likely related to fluid dynamics or mechanical design. It features two vertical walls on either side, with a horizontal bottom and two angled sections leading up to vertical sections at both ends. There are arrows indicating vertical measurements, suggesting a focus on height or depth of the internal area, which may represent the levels of liquid or other materials. This layout could be commonly associated with U-shaped channels or containers, often used in various engineering applications for fluid flow or holding substances. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wQuaUvtzowueQXAZTVZcpA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Height2 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wQuaUvtzowueQXAZTVZcpA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the first length of the bottom shape.


Image:[Alt-Text: Length1 (Beam Clamp) 
Image-Analysis: The image consists of four different diagrams that illustrate various types of joints or connections, commonly seen in engineering or technical design. The top-left diagram shows a linear connection with arrows indicating movement or force in both directions. The top-right diagram displays a similar linear connection but with a more complex shape, suggesting a different type of connection that might allow for rotation or bending. The bottom-left diagram depicts a trough-like structure with arrows indicating a two-directional force. The bottom-right diagram shows a more intricate connection with additional features, including flared ends, indicating a specialized type of joint. Each diagram visually represents how structures may connect or interact with each other, emphasizing different shapes and joint functionalities. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WyBYnDgaYvY2k03I5GcKyQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Length1 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WyBYnDgaYvY2k03I5GcKyQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the second length of the bottom shape. For shape I and shape U, this property
will be ignored.


Image:[Alt-Text: Length2 (Beam Clamp) 
Image-Analysis: The image displays two different types of mechanical joints or connections. On the left, there is a representation of a simple lap joint which consists of two pieces connected over a small section, allowing for alignment and support. The arrows indicate the direction of force transmission. The joint on the right illustrates a more complex joint, potentially a T-joint, where two components intersect, creating a sturdy connection that often resists twisting. These kinds of joints are critical in construction and engineering for maintaining structural integrity and stability in assemblies. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OqdjX7gBYPTB7IOjMK3SRA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Length2 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OqdjX7gBYPTB7IOjMK3SRA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance between the structure port and the RodEnd port. If no value
is set to RodTakeOut, then, both, the structure port and the RodEnd port will be aligned on the same horizontal
line.


Image:[Alt-Text: RodTakeOut (Beam Clamp) 
Image-Analysis: The image depicts a schematic diagram of a valve or similar mechanical device. It shows a cross-section of the valve with various components, including a cylindrical housing, inlet and outlet ports, and a movable internal mechanism (likely a piston or gate). The diagram features several arrows indicating directions of movement or flow, demonstrating how the valve operates. There are red markings indicating critical points, possibly for adjustment or connection. The presence of dashed lines suggests potential movement areas or paths. Overall, this image illustrates the structural and functional aspects of the device, useful for understanding how it controls fluid flow. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mjftqYumUBBYnz3kKccPxg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RodTakeOut (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mjftqYumUBBYnz3kKccPxg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  RodEnd port is created only if BottomShape is assigned a defined value.

IJUAhsAngle1::Angle1

Specifies the angle between the structure and the bottom shape. Both, positive and
negative values are allowed. It is required only for sloped steel configuration.


Image:[Alt-Text: Angle1 (Beam Clamp) 
Image-Analysis: The image consists of two diagrams that illustrate concepts related to angles. On the left side, labeled "If Positive Angle," it shows a square tilted positively, indicating an angle of inclination to the right. There is a line (presumably representing a lever or an arm) and an indication of how it moves at the pivot point, suggesting a clockwise motion. On the right side, labeled "If Negative Angle," a similar square is tilted negatively, indicating an angle of inclination to the left, with a similar arm structure that implies a counterclockwise movement. Both depictions help explain the concept of positive and negative angles in relation to a pivot point. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uGOyZqTuTtjHHQzsJxdRWg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Angle1 (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uGOyZqTuTtjHHQzsJxdRWg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  This property is applicable only for U shape bottom type.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt/Pin Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/331065?contentId=yKHhuwNMTkeDaOKrMbXwUg)
These properties define the geometry of the bolts/pins of the beam clamp.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt/pin. If this is used as a bolt, then bolt diameter
should be same as the pin diameter.


Image:[Alt-Text: Pin1Diameter ( Beam Clamp ) 
Image-Analysis: The image depicts a technical diagram of a valve system. It shows a cross-sectional view of a valve, which includes various parts such as the valve body, inlet and outlet ports, and internal mechanisms such as stems and seats. The arrows indicate the direction of flow and movement within the valve system, suggesting how the valve operates to control fluid passage. The presence of red marks may indicate points of interest or specific components that require attention, such as connections or control points. This diagram is likely used for understanding the functional aspects of the valve, including how it can regulate flow based on its position. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hPZRcWi_tlv9XwQw4RM2jQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Pin1Diameter ( Beam Clamp )](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hPZRcWi_tlv9XwQw4RM2jQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of bolt/pin. If this is used as a bolt, then bolt length should
be same as the pin length.


Image:[Alt-Text: Pin1Length ( Beam Clamp ) 
Image-Analysis: The image depicts a cross-sectional view of a mechanical assembly, possibly a fitting or connector, showing various components like a housing and seals. The structure is outlined, indicating where parts may be attached or fit together. Red arrows emphasize points of interest, likely indicating flow or pressure directions, or critical assembly points. The drawing suggests a systematic approach to assembly or design, likely for mechanical engineering purposes, illustrating the relationship between different components and how they interact within the assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iNEeg2Tpkg_V912vmG2etg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Pin1Length ( Beam Clamp )](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iNEeg2Tpkg_V912vmG2etg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  Pin1Length should be greater than or equal to Length1 of the bottom shape.

IJUAhsHeight3::Height3

Specifies the distance of the pin from the top port of the clip to center of the pin.


Image:[Alt-Text: Pinheight3 ( Beam Clamp ) 
Image-Analysis: The image depicts a technical drawing of a component, likely part of a mechanical assembly. The focus is on a valve or a similar device that includes an upper section with two arrows indicating the flow direction – one pointing downwards and the other upwards. There is a horizontal line representing a base or connection point, along with dotted lines suggesting hidden features or sections not visible. The red markings highlight specific points or measurements that are critical for understanding the part's functionality or assembly. Overall, this schematic layout emphasizes the relationship between various components and their proposed interactions, likely within a larger system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/X3QJMSyyLFnUwNsUolXUzg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Pinheight3 ( Beam Clamp )](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/X3QJMSyyLFnUwNsUolXUzg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Left Clip Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/331967?contentId=jypVEqpwkr2A684Vg0cF1w)
These properties are used to set the external bolt on the left clip.

IJUAHsLeftClipBolt::BoltLength1

Specifies the length of the bolt used in the beam clamp for left beam clip. If this
value is less than or equal to zero, no bolt is drawn.


Image:[Alt-Text: BoltLength1 (LeftClip Bolt Properties) 
Image-Analysis: The image depicts a schematic diagram related to electrical engineering, particularly focusing on a circuit design. It illustrates various components such as resistors, likely including a potential divider at the upper left, and connections with nodes indicated. The red dots appear to signify specific connection points or measurement points within the circuit. The highlighted and dashed lines suggest various voltage levels or signal pathways within the circuit. The overall layout presents a complex structure with clear segmentation of different sections, including inputs and outputs, which are commonly analyzed in circuit functionality and signal flow. The connections demonstrate the relationship between these components and how they impact overall circuit operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZvSiVeQK6oq6V~N5BcxPhg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BoltLength1 (LeftClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZvSiVeQK6oq6V~N5BcxPhg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsLeftClipBolt::BoltDiameter1

Specifies the diameter of the bolt used in the beam clamp for left beam clip. If this
value is less than or equal to zero, no bolt is drawn.


Image:[Alt-Text: BoltDiameter1 (LeftClip Bolt Properties) 
Image-Analysis: This image represents a simplified electrical circuit diagram. It includes several components: a switch symbol on the left, indicating a way to control the flow of electricity, and a resistor symbol shown in the circuit part. The circuit also has nodes (red dots) showing where connections are made. Additionally, there are lines indicating the pathway of current flow. The dashed lines signify that there are connections that are not directly part of the main flow of the circuit. Overall, the image illustrates how these components interact within an electrical circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_EM0uoe_iGQnP0MX7S1rsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BoltDiameter1 (LeftClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_EM0uoe_iGQnP0MX7S1rsg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsLeftClipBolt::HeadType1

Specifies the shape of the bolt's head. Allowed values are:


Image:[Alt-Text: HeadType( Beam Clamp) 
Image-Analysis: The image displays three geometric shapes along with their corresponding labels. Each shape has a number and a name: 1 is labeled as "Round," 2 as "Square," and 3 as "Hex." Each shape is a simple outline, with the round shape being circular, the square being four equal straight sides, and the hexagonal shape having six sides. This organization suggests a classification system based on the type of shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b_DZpcN5skpWCPIomHfaow-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadType( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b_DZpcN5skpWCPIomHfaow-_PVFQNoCl4XmjAxWO0f7XQ/content)

If this value is either zero or not specified, then no bolt head is modeled.

IJUAHsLeftClipBolt::HeadThickness1

Specifies the thickness of the bolt head. If this value is less than or equal to zero,
no bolt is drawn.

IJUAHsLeftClipBolt::HeadWidth1

Specifies the width of the bolt head. If this value is less than or equal to zero,
no bolt is drawn.


Image:[Alt-Text: HeadWidth1 ( LeftClip Bolt Properties) 
Image-Analysis: The image displays three different geometric shapes, each labeled with a number and a name. The shapes and their descriptions are as follows: 1 - Round, which is a circle; 2 - Square, which is a square shape; and 3 - Hex, which refers to a hexagon. Each shape is represented with a center dot and appropriate outlines, illustrating their distinct forms. This visual representation may be used to categorize or select shapes based on their geometric properties. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IAJAoaSmyQouMrqvPVpRXQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadWidth1 ( LeftClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IAJAoaSmyQouMrqvPVpRXQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Right Clip Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/332014?contentId=HUX1yieO2P1mKmKzKs1x_w)
These properties are used to set the external bolt on the right clip.

IJUAHsRightClipBolt::BoltLength2

Specifies the length of the bolt used in the beam clamp for right beam clip. If this
value is less than or equal to zero, no bolt is drawn.


Image:[Alt-Text: BoltLength2 (RightClip Bolt Properties) 
Image-Analysis: The image appears to be a schematic diagram of a mechanical or engineering system, possibly representing a system involving pipes or fluid flow. It includes different components such as valves, pipes, and measurements indicated by a layout that reflects their proximity and connections. The diagram also shows points of interest marked with red symbols that may represent measurement or control points within the system. Along the right side, there are arrows pointing upwards and downwards, which might indicate the direction of flow or pressure changes within the system. Overall, this schematic provides a visual representation of how different parts are interconnected and may function together in a larger setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2ATh9ZKMHR_qGxok5ORP2g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BoltLength2 (RightClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2ATh9ZKMHR_qGxok5ORP2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsRightClipBolt::BoltDiameter2

Specifies the diameter of the bolt used in the beam clamp for right beam clip. If
this value is less than or equal to zero, no bolt is drawn.


Image:[Alt-Text: BoltDiameter2 (RightClip Bolt Properties) 
Image-Analysis: This image appears to be a schematic or diagram of an electrical circuit or mechanical system. It features a combination of lines representing connections and components. The symbols and connections suggest the presence of various elements such as resistors, potential dividers, or other electronic components. The use of red dots likely indicates points of interest, such as terminals or connection points. The presence of arrows at the bottom suggests directionality, possibly indicating current flow or mechanical movement. Overall, this diagram illustrates the layout and functional relationships between different entities in the system being represented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uM8SrJOvqG3Rb49nFG_qmQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BoltDiameter2 (RightClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uM8SrJOvqG3Rb49nFG_qmQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsRightClipBolt::HeadType2

Specifies the shape of the bolt's head. Allowed values are:


Image:[Alt-Text: HeadType( Beam Clamp) 
Image-Analysis: The image displays three geometric shapes: a Round shape, a Square shape, and a Hexagonal shape. Each shape is numbered sequentially from 1 to 3, highlighting their distinct characteristics. The Round shape is indicated as number 1, the Square as number 2, and the Hexagonal shape as number 3. Each shape has a dotted circle in the center, possibly representing a focal point or indicating some form of measurement related to the shapes. This layout may suggest a comparison or categorization of different shapes based on their attributes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hsefSjQ0oIvg0bJ_2jTyRw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadType( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hsefSjQ0oIvg0bJ_2jTyRw-_PVFQNoCl4XmjAxWO0f7XQ/content)

If this value is either zero or not specified, then no bolt head is modeled.

IJUAHsRightClipBolt::HeadThickness2

Specifies the thickness of the bolt head. If this value is less than or equal to zero,
no bolt is drawn.


Image:[Alt-Text: HeadThickness2 (RightClip Bolt Properties) 
Image-Analysis: The image represents a schematic diagram illustrating an electrical circuit. This circuit involves components such as resistors and possibly semiconductors, indicated by specific symbols. The lines denote connections between different elements, creating a pathway for electrical flow. The dashed lines may suggest connections that are not as direct or implied, serving to clarify the layout. Additionally, the diagram displays various arrow symbols which often represent the direction of current flow. The red dots likely indicate points of interest such as nodes or component connections that are crucial for the operation of the circuit. Overall, this image presents a structured layout of how different electronic components interact within the circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_QX~l~0kVy3NO2l2aShhtQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadThickness2 (RightClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_QX~l~0kVy3NO2l2aShhtQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAHsRightClipBolt::HeadWidth2

Specifies the width of the bolt head. If this value is less than or equal to zero,
no bolt is drawn.


Image:[Alt-Text: HeadWidth2 ( RightClip Bolt Properties) 
Image-Analysis: The image displays three geometric shapes with corresponding labels and numbers. The first shape, labeled "1 - Round," is a circle with a dotted line in the center, suggesting it has a certain radius or diameter. The second shape, labeled "2 - Square," is a square also featuring a central dot, indicating it has equal sides. Finally, the third shape, labeled "3 - Hex," is a hexagon, characterized by its six sides and a central dot. This arrangement likely serves as a reference for identifying different geometric shapes, possibly for a design, manufacturing, or educational purpose. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2I0ZKoBxRg3BUdCu2aGXsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![HeadWidth2 ( RightClip Bolt Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2I0ZKoBxRg3BUdCu2aGXsg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clip with U-Bolt / J-Bolt - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/332024?contentId=wC2t3B50m3LJaPP7HUkuYQ)
These properties define the geometry of the beam clamp that has a clip with a U-Bolt/J-Bolt.

IJUAhsJUBolt::UBoltWidth

Specifies the center to center distance between the legs of the U-Bolt. This value
determines the spacing of the vertical legs of the U-Bolt and the bend radius for
the curved part of the U-Bolt. UBoltWidth value must be greater than UBoltRodDia and lesser than the depth of the clip shape.

![UBoltWidth (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ismuWjmFZams_~H9tpGffQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=57e7bb41fef7b018)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ismuWjmFZams_~H9tpGffQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsJUBolt::UBoltLength

Specifies the distance from bottom to top end of the U-Bolt legs.


Image:[Alt-Text: UBoltLength (Beam Clamp) 
Image-Analysis: The image depicts a semicircular arch with a vertical line on the right side indicating height. There is a small red square positioned towards the bottom center, which could represent a point of reference or a load at the base of the arch. The arch itself symbolizes structural integrity, common in architecture, and the height marker suggests a dimension or clearance needed for something passing under the arch. The relationship between the arch and the red square implies that the square may represent an object that requires a specific height clearance under the arch, highlighting the importance of considering both the shape and the dimensions in design contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TipfCixFaGi8~D2w1OtDOg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![UBoltLength (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TipfCixFaGi8~D2w1OtDOg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsJUBolt::UBoltRodDia

Specifies the diameter of round stock used to make the U-Bolt. If this value is zero,
no U-Bolt shape is drawn.


look for icon that resembles an arch or curved structure with arrows pointing outward, indicating expansion or release: 

IJUAhsJUBolt::UBoltFlatSpot

Adds a flat spot to the shape of the rectangular wrap/strap. If UBoltFlatSpot is zero, no flat spot is added to the curved part of the U-Bolt. If UBoltFlatSpot is positive, a flat spot is added to the curved section of the U-Bolt. This also
reduces the bend radius and center points for the curved part of the U-Bolt.


icon-description of a bridge with arrows indicating passage or flow: 

IJUAhsJUBolt::IsJBolt

Specifies whether it is a J-Bolt or U-Bolt. It uses hsYesNo codelist. If IsJBolt is set to Yes, then the right side of the U-Bolt graphic below the tangent point is
not drawn.


Image:[Alt-Text: IsJBolt (Beam Clamp) 
Image-Analysis: The image shows two distinct components related to machinery or mechanical applications. On the left, there is a simple arc or hook shape, likely representing a type of hook or a bent wire. On the right, there is a more complex metal hook or clamp-like structure that has a curved hook end and a mounting bracket. This may suggest a connection point for secure fastening or support. The two images together might depict different types of hooks used in assembly or construction tasks, showing their variations in design and function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xXsRPjItlvG7N68LBj6JzA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![IsJBolt (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xXsRPjItlvG7N68LBj6JzA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [User Prompts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/334427?contentId=ZlaQjGpzQlS3Er~ilSMl_A)
You can edit these properties on the corresponding properties page. If the part is
used within an assembly, they the properties automatically populate from the assembly
code.

IJOAhsClampThick::ClampThickness

Specifies the flange thickness of the structure in which the beam clamp needs to be
attached.


Image:[Alt-Text: user prompts (clampThickness) 
Image-Analysis: The image appears to depict a mechanical component, likely a part of a machine or assembly, illustrating a section view of an object with various dimensions and features. The presence of arrows indicates movement or force directions, potentially showing how the part interacts under load. The red marks seem to highlight critical points or measurements that are necessary for assembly or machining processes. The dashed lines represent sections that could indicate hidden or internal features of the part, while the solid lines outline the exterior features. Overall, the image is a technical drawing commonly used in engineering or manufacturing contexts to convey important specifications and relationships between different components of a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dco6Sja3EN45c~NhanXk~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![user prompts (clampThickness)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Dco6Sja3EN45c~NhanXk~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStructWidth::StructWidth

Specifies the flange width of the structure in which the beam clamp needs to be attached.


Image:[Alt-Text: user prompts (StructWidth) 
Image-Analysis: The image depicts a technical diagram, likely related to mechanical engineering or design. It shows a 2D view of a component, featuring various elements such as a rectangular frame, a vertical rod, and a horizontal protrusion. There are red dots indicating points of interest or critical measurement locations, possibly signifying connection points, mounting holes, or areas for further detailing. The dashed lines suggest outlines for sections that may not be fully visible or need to be noted for dimensional constraints. The horizontal arrows at the bottom represent measurements or dimensions, signifying the widths associated with the component's design. The diagram is tailored for individuals familiar with technical drawings, illustrating relationships between the features and their geometric dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjOJqUj3yKT~jw0jV47cuA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![user prompts (StructWidth)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjOJqUj3yKT~jw0jV47cuA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/332032?contentId=c4dVm20e2OpEaJ2xu~mL~A)
These properties specify the different port types and their sizes for the beam clamp.

![port details Beam Clamp](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/78~wlmIgQndNaxWMvK2w7A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=735458e67dc1b9a3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/78~wlmIgQndNaxWMvK2w7A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Beam Clamp Ports

![Beam Clamp Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fhg_u2UjCjhjKQdrAv6l8Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=797af310ffaa2fbe)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fhg_u2UjCjhjKQdrAv6l8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

A beam clamp can have the following ports.

1. Structure port (this is the origin of the beam clip)
2. Bottom port
3. Top port
4. RodEnd1 port
5. RodEnd2 port (If a second clip shape is present)
6. RodEnd port (if two clips and a shape are present)


None: 

If the beam clamp has one beam clip shape then, there will be four ports: Top, Bottom,
Structure, and BoltPort1. In the graphic shown below, both the beam clamps have only
one beam clip with external bolt. For such beam clamps only four ports are added.


Image:[Alt-Text: Port details 1( Beam Clamp) 
Image-Analysis: The image consists of two side-by-side diagrams that illustrate mechanical or structural elements, likely related to a specific engineering or architectural concept. Each diagram resembles a series of interconnected components, with lines denoting their connections and red dots indicating points of interest or interaction. The differences between the left and right diagrams suggest variations in the arrangement or function of these components, possibly demonstrating different operational states or configurations. Understanding the relationships between these parts is essential for interpreting their purpose, whether it be in mechanical design, load distribution, or structural integrity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/S4c_igB0jXmDdc5~AY~3_A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Port details 1( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/S4c_igB0jXmDdc5~AY~3_A-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the beam clamp has two beam clip shapes then, there will be five ports: Top, Bottom,
Structure, RodEnd1 and RodEnd2. The RodEnd1 will be assigned to left clip and RodEnd2
will be assigned to right clip. Graphic below is an instance where the beam clamp
has right clip, left clip, bottom shape, and two external bolts on each beam clip.
RodEnd1 will be on left clip and RodEnd2 will be on right clip.


Image:[Alt-Text: Port details 2( Beam Clamp) 
Image-Analysis: The image is a schematic diagram that represents a mechanical or structural assembly. It appears to show a system of connections with various components, as indicated by the different shapes and lines. The central part, depicted with dashed lines, likely represents a core or main element being supported by surrounding structures. The use of red squares suggests points of interest or stress locations where forces may be applied or monitored. The arrangement indicates interactions between these components that contribute to overall stability and function. The horizontal lines at the top and bottom could be components that provide additional support or linkage, reinforcing the structure. Overall, this seems to illustrate how various parts come together to form a cohesive system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XVcD48cVogrORH7UszoMYA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Port details 2( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XVcD48cVogrORH7UszoMYA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Top Port


Image:[Alt-Text: port orientations (Beam Clamp) 
Image-Analysis: The image depicts a technical drawing illustrating coordinate systems used in a 3D space, typically found in engineering or manufacturing. It shows two structures, each labeled with axes: X, Y, and Z, which define the 3D orientation. The left side indicates the Y axis aligned vertically, the Z axis pointing up, and mentions a "Top" reference, which likely signifies the top surface of the object. The right side also features the Z axis at the top and shows the additional X axis, suggesting an orientation that incorporates lateral movement. The image is used to help visualize spatial relationships, angles, and measurements crucial for precise machining, assembly, or modeling tasks. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sfnIQewTzPfFRQpSk7TSrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![port orientations (Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sfnIQewTzPfFRQpSk7TSrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1- Top

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 - Other | 0 | -9999 | 9999 |

Bottom Port


Image:[Alt-Text: port orientations - Bottom(Beam Clamp) 
Image-Analysis: The image shows two different configurations of a setup, likely related to a machining or engineering process. Both configurations feature labeled axes, where the left side uses Y and Z axes while the right side uses X and Z axes. They include references to a "Bottom" point, indicating a position of interest in relation to the setup. The vertical measurement indicated by the Z axis suggests the height or depth, while the horizontal measurements indicated by Y and X depend on the respective configurations. The two configurations may represent different orientations for operations or measurements, emphasizing the importance of understanding how to interpret these axes in relation to the physical setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gl1QvqMEY4beQCc9Usu5wA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![port orientations - Bottom(Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gl1QvqMEY4beQCc9Usu5wA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Alt-Text: port orientations - Bottom 2(Beam Clamp) 
Image-Analysis: The image depicts a 3D geometric figure, likely representing a shape with a base and protruding elements. At the bottom, there is a rectangular block that serves as the base of the shape. There is a vertical line or stick shape extending upwards from the base. Near the top, there are additional geometric elements, including a horizontal bar that intersects with the vertical line. The image includes red dots at crucial points, which may indicate specific measurement locations or reference points on the structure. Additionally, the word "Bottom" is labeled, indicating the orientation of the shape. This suggests that the figure may have applications in engineering or design, likely showing how components fit together in a spatial arrangement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4GwF2hiNZT~Elai6JiRQ1A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![port orientations - Bottom 2(Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4GwF2hiNZT~Elai6JiRQ1A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 2 - Bottom

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 - Other | 0 | -9999 | 9999 |

Structure Port


Image:[Alt-Text: Port orientations Strucure port ( Beam Clamp) 
Image-Analysis: The image illustrates two different 3D structures, each represented on a separate side. On the left, there is a structure with labeled axes (Y and Z) and a point marked at (0,0,0), which indicates the origin in a Cartesian coordinate system. The red arrows indicate the directions of the Y and Z axes. The Y-axis extends horizontally, while the Z-axis extends vertically downward. The left structure appears to have an additional component or extension not fully depicted. On the right, another structure is shown with labeled axes (X and Z), and it also marks the origin at (0,0,0). Here, the X-axis extends horizontally, while the Z-axis is again vertical. This setup suggests a comparison between two structural elements along different orientations or configurations, highlighting the importance of coordinate systems in spatial representation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/s4O8C4m9lz2K3r~b5yicaw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Port orientations Strucure port ( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/s4O8C4m9lz2K3r~b5yicaw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 3 - Structure

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 - Structure | -1 | -9999 | 9999 |

RodEnd1Port

![Port Orientations - RodEnd1Port ( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WSwO07Qf1evOEp6IHZVO3A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=54ed7e3c10c2400f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WSwO07Qf1evOEp6IHZVO3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 4 - RodEnd1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1002 - External Thread, LH  1000- External Thread, RH  1005- Pin | LeftBolt diameter\ RightBolt diameter\ Rod diameter  LeftBolt diameter\ RightBolt diameter\ Rod diameter  Pin1Diameter | LeftBolt diameter\ RightBolt diameter \ Rod diameter  LeftBolt diameter\ RightBolt diameter\ Rod diameter  Pin1Diameter | LeftBolt diameter\ RightBolt diameter\ Rod diameter  LeftBolt diameter\ RightBolt diameter\ Rod diameter  Pin1Diameter |

RodEnd2 Port

RodEnd2 has port orientation similar to that of RodEnd1 but it is on the right clip.

Port 5 - RodEnd2

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1000 - External Thread, RH  1002 - External Thread, LH | RightBolt diameter\ Rod diameter | RightBolt diameter\ Rod diameter | RightBolt diameter\ Rod diameter |

RodEnd Port

![Port orientations - RodEnd port( Beam Clamp)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZsRU7PgCgklgLcCRPJG8JA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=38f50a0573fd1c57)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZsRU7PgCgklgLcCRPJG8JA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 6 - RodEnd Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1000 - External Thread, RH | Rod diameter | Rod diameter | Rod diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Block Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313190?contentId=GeIxYV5O98VJcyygUoHslw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.BlockClamp  
Part Name: Block Clamp  
Part Description: Block Clamp SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~9F_pV1nXw~BFJKlUlMH4g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4b9a43ebad6147c0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~9F_pV1nXw~BFJKlUlMH4g-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Block Clamp SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part command, and then select the design support.
4. In the Select Part dialog, select a part from Parts > SmartParts > S3D Standard > Pipe Clamps > Block Clamp as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical structure, resembling a directory tree, illustrating various categories and subcategories within a system referred to as "SmartParts." The top level is labeled "SmartParts," which serves as the main category. Within this, there are subcategories such as "S3D Standard," "Beam Attachments," "Clevises," "Miscellaneous," "Pin," and "Pipe Clamps." The "Pipe Clamps" category further branches into two specific types: "Adjustable Swivel Ring" and "Block Clamp." This structure demonstrates how different items and their corresponding types are systematically organized under broader categories, enabling easier navigation and identification of items in the SmartParts system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ovOwUaf7XeoV1YvAOJtTbQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ovOwUaf7XeoV1YvAOJtTbQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image consists of two diagrams illustrating routing concepts with specific labels and directional arrows. In the first diagram (top), there is a circular node labeled "Route" that connects to two paths: one leading to "Y" and another downward leading to "Z". The arrows indicate the direction of the routes from the "Route" node. In the second diagram (bottom), there is again a "Route" node, but this time it connects to "X" horizontally with a downward path leading to "Z". Both diagrams show the relationships between these entities, with emphasis on how the "Route" node directs traffic towards the other entities "Y", "X", and "Z". The overall structure suggests a routing system where the paths and connections are key for navigation in a network or process. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vIrbsq0z8ceBwGW4SYDtlQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vIrbsq0z8ceBwGW4SYDtlQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Block Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313197?contentId=vshKAM0KO25s6vXFsfIR9A)
These properties define the geometry of the block clamp.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of the dimensional value to use inches (for example 10in).

IJUAhsSize::Size

Specifies a string attribute that selects the correct block clamp. This needs to be
reported for BOMs.

IJOAhsDiameter1::Diameter1

Specifies the diameter of the first pipe of the block clamp.


Image:[Image-Analysis: The image depicts a technical diagram showing two circles, which likely represent objects or components, labeled "Diameter1". The circles are positioned on a horizontal line, indicating a measurement related to their diameter. There are arrows pointing horizontally, suggesting that the measurement of the diameter is being highlighted or showcased. This diagram could be used in contexts such as engineering, design, or manufacturing, where dimensions and spacing are critical. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_VMK2rc8FeIKAzj4de~w0A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_VMK2rc8FeIKAzj4de~w0A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsDiameter2::Diameter2

Specifies the diameter of the second pipe of the block clamp, if there is one.


Image:[Image-Analysis: The image depicts two circles positioned horizontally, each representing a circular object, likely spheres or cylinders, with a given diameter labeled as "Diameter2." The circles are shaded gray, indicating they may be solid shapes, and they are aligned along a horizontal axis. The dimension "Diameter2" is indicated with arrows pointing horizontally, suggesting that this label refers to the width or measurement across the circles. The circles are positioned above a horizontal line, possibly representing a base or surface. Overall, this image may be used in a technical or engineering context to illustrate the size or placement of cylindrical objects with respect to one another. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eGbr~XLfBsi1kPiSzyQWCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eGbr~XLfBsi1kPiSzyQWCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight3::Height3

Specifies the distance from the bottom of the block clamp to the pipe centerline of
the second pipe, if there is one.


Image:[Image-Analysis: The image shows a simple diagram depicting a structure that consists of a rectangular box and two overlapping circles placed above it. The box has labels indicating it has a "Height3." This suggests a height measurement in a geometric context. The circles can represent certain features or components, possibly related to the rectangular box. The arrangement might be indicative of a relationship where the circles are situated above the box, suggesting a support or containment concept. This could be part of a technical drawing relating to engineering or architectural design, illustrating how different components relate spatially. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hy1NCkkOGQ7o33T3vtrjFQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Hy1NCkkOGQ7o33T3vtrjFQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance from the pipe centerline to the rod connection point.


Image:[Image-Analysis: The image shows a diagram illustrating the process of removing a rod from a cylindrical object. It features a side view of the cylindrical object, which includes a circular cross-section indicating the rod's position. There are directional arrows indicating movement ("RodTakeOut") which suggests the rod should be pulled or taken out from the cylinder. The diagram appears to be technical, possibly related to machinery or mechanical engineering, where understanding the correct removal process is crucial. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xVMNf3yX07BChdAfETt6wg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xVMNf3yX07BChdAfETt6wg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313208?contentId=H7Qd~mojm_D4q8tYiyOvvQ)
These properties specify the plate properties for the block clamp.

IJUAhsThickness1::Thickness1

Specifies the thickness of the top plate. If this value is set to zero, the top plate
is not shown.


Image:[Image-Analysis: The image illustrates a mechanical or geometric concept involving a circular element situated between two rectangular shapes. The circular shape is colored gray and appears slightly smaller than the surrounding rectangles, suggesting it may represent a part like a disc or spacer. The notation "Thickness1" is indicated alongside an arrow pointing downwards, which likely specifies the thickness measurement of the upper or lower rectangular shape or the overall setup. Furthermore, a small red dot is marked at the center of the circle, potentially indicating the center point for further calculations or references. The layout indicates a system where these components interact based on the illustrated dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7ESyf95TPW2ltMsW_hfjzQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7ESyf95TPW2ltMsW_hfjzQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of the top plate.


Image:[Image-Analysis: The image illustrates a component with two circular elements positioned horizontally, potentially representing a mechanical or structural part like a pipe fitting or connector. It features a labeled dimension "Length1" that indicates the distance between the two ends of the circular components. The circular elements are depicted with a gray background, signifying they might be different in material or function compared to the white rectangular parts above and below them. The overall configuration suggests a symmetrical design, commonly found in engineering contexts where precise measurements are crucial for fitting parts together. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/luGao0SN_cxnsw_uv7fpdQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/luGao0SN_cxnsw_uv7fpdQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the width of the top plate.


Image:[Image-Analysis: The image depicts a geometric arrangement that includes a rectangle with a circular shape situated at its center. The rectangle is oriented vertically, with two horizontal edges defined, while the circular shape overlaps with the rectangle. The label "Width1" is positioned above the rectangle and indicates a measurement corresponding to the horizontal span of the rectangle. The diagram appears to be illustrative, likely used in mathematical or engineering contexts to convey dimensions and arrangements between different shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iJFuiRFUbAt3k2HaclZJiA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iJFuiRFUbAt3k2HaclZJiA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the bottom plate. If this value is set to zero, the bottom
plate is not shown.


Image:[Image-Analysis: The image depicts a technical diagram showing a circular object with a specified thickness, labeled as "Thickness2." The circular shape is represented in the center of the image, surrounded by two horizontal lines that likely represent the boundaries or surfaces of a material or component. The thickness measurement is indicated by the vertical arrows pointing towards the circular object, suggesting a context where dimensional specifications are important, such as in engineering or manufacturing design. The presence of a red dot may denote a reference point or a specific feature of the circular shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/POsw~tsKB34NxL1WylZD6Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/POsw~tsKB34NxL1WylZD6Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the length of the bottom plate.


Image:[Image-Analysis: The image depicts a diagrammatic representation of two rectangular shapes positioned one over the other, with a connecting middle section that is shaded in gray. The rectangles seem to indicate that they are some form of blocks or sections that might be aligned in a mechanical or structural setup. The base of the diagram features a label "Length2" situated between arrows pointing outward, suggesting this is the measurement of the horizontal distance between the two rectangles. The arrangement illustrates how the components are related spatially, with a focus on their dimensions and positioning. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Tr3L3S~c9xwIJ9mBvN55dQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Tr3L3S~c9xwIJ9mBvN55dQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the width of the bottom plate.


Image:[Image-Analysis: The image depicts a geometric representation that includes a circle and two rectangular shapes positioned above and below the circle. The circle is centered horizontally with a red dot located at its center. The rectangles are labeled as having a width denoted by "Width2," indicated by arrows on either side of the bottom rectangle. This suggests that the element marked "Width2" refers to a measurement relevant to the rectangular shapes. Overall, the image appears to convey a concept related to geometry or perhaps a physical object with specific dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KLUH4Rjj46_3I2wkyvblJQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KLUH4Rjj46_3I2wkyvblJQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMidPlateBotShape::MidPlateBotShape

Specifies the name of the middle bottom plate shape. If more than two pipes are supported,
the pipe holes or dents are not shown.


Image:[Image-Analysis: The image shows a diagram with three main components. At the top, there is a rectangular box which might represent a title or header. Below that, there is a larger circle in the middle filled in gray, which could symbolize a central concept or entity. Within this gray circle, there is a small red dot, possibly indicating a point of focus or a specific feature of the central concept. At the bottom, there are two rectangular boxes with a patterned design, suggesting additional information, details, or supporting entities related to the main concept in the center. Overall, the diagram appears to show a structure where a central idea is supported by various related elements or information. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/95rBNNRGFAxXJDiPT5qkqw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/95rBNNRGFAxXJDiPT5qkqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

The following middle bottom shapes are supported:


Image:[Image-Analysis: The image consists of three rectangular frames, each containing a grey circle. The circles are positioned differently within the frames. The first frame shows the circle aligned to the top, the second frame shows it centered, and the third frame shows the circle aligned to the bottom. The presence of a small red marker or dot in each circle may indicate a point of interest or an action to be taken regarding the circles. This configuration might suggest a comparison or consideration of different positions for the same entity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W4cvDS0~lS9H7HmUTIPhdA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W4cvDS0~lS9H7HmUTIPhdA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMidPlateTopShape::MidPlateTopShape

Specifies the name of the middle top plate shape. If more than two pipes are supported,
the pipe holes or dents are not shown.


Image:[Image-Analysis: The image depicts a figure that includes a circular shape in the center, shaded grey, representing most likely a focal point. Surrounding the circle, there are rectangular shapes above and below, which may signify sections or compartments, but they remain empty in the visual representation. The circular shape could indicate an object or concept that is central to the context, while the rectangles may represent categories or layers of information related to that central idea. There is also a small red dot at the center of the circle, potentially highlighting or marking the exact point of interest. Overall, this image likely illustrates a structured or organized schema, where the grey circle is the primary focus situated between two subordinate areas represented by the rectangles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QJiLacqbR7yopccHLGNbBg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QJiLacqbR7yopccHLGNbBg-_PVFQNoCl4XmjAxWO0f7XQ/content)

The following middle top shapes are supported:


Image:[Image-Analysis: The image consists of four diagrams organized in a 2x2 grid. Each diagram illustrates the interaction between a circular object (depicted in gray) and various surrounding shapes. The diagrams depict different configurations of the circular object: 1) A circle fitting within a rectangular outline, suggesting a containment scenario. 2) A circle partially overlapping with a rectangular shape, indicating potential movement or interaction beyond just containment. 3) Another representation of a circle, this time depicted at a different position with a similar surrounding rectangle as the first diagram. 4) Finally, the circle is shown in a more confined rectangular space, indicating varying degrees of spatial relations with the shapes around it. Overall, these diagrams likely represent concepts related to geometry, mechanics, or design of circular objects in relation to other forms. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/scALUvdgFGifO7eIlwN6NA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/scALUvdgFGifO7eIlwN6NA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the base plate. If this value is set to zero or not provided,
the base plate is not shown.


Image:[Image-Analysis: The image depicts a technical drawing or diagram, likely related to a component or assembly. The top part outlines a rectangular shape, possibly representing the top view of an object with defined measurements. Below that is a circular shape with a gray fill, possibly indicating a hole or feature within the main object. The red point in the center could denote a reference point for positioning or alignment. There are arrows pointing vertically, suggesting that the measurement labeled "Thickness3" pertains to the vertical dimensions of the component or the thickness of specific layers. This indicates a focus on the dimensional properties and possibly the functional aspect of the object being represented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yU8iGV3BvurqDmvGi~El5g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yU8iGV3BvurqDmvGi~El5g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength3::Length3

Specifies the length of the base plate.


Image:[Image-Analysis: The image depicts a schematic representation of a component, likely in a mechanical or engineering context. It shows a central rectangular block, which might represent the main part of a device or system. There are two shaded rectangles on the sides that could represent additional components or mounts. The central part is labeled with a red dot, possibly indicating a specific point of interest or measurement within the component. Below the main structure, there is a small section that seems to represent a base or pedestal, possibly where the component will be mounted or connected to another system. The image includes a dimension annotation labeled "Length3," which suggests that this is a measurement related to the overall length of the component or its parts, providing critical information for assembly or fitting. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RjWn9XrhU0dhTGgP8ySp3A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RjWn9XrhU0dhTGgP8ySp3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the width of the base plate.


Image:[Image-Analysis: The image illustrates a simple geometrical shape layout with a central circular area (represented as a grey circle) and a rectangle around it. The rectangle has a label at the bottom indicating "Width3," which likely signifies the dimension of the rectangle. The arrangement suggests a shape with defined widths and a focal element at the center (the circle), possibly indicating a design or structural drawing where specific measurements and alignments are important. The red dot inside the circle may represent a key point of interest or a center of attention in the design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HQbRCQCMCrT24qedkCMzuA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HQbRCQCMCrT24qedkCMzuA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness4::Thickness4

Specifies the thickness of the vertical plate or stanchion. Thickness4 must be greater than zero, or the vertical plate or stanchion is not shown.


Image:[Image-Analysis: The image depicts a technical drawing focusing on the concept of "Thickness4," which likely refers to a measurement of material thickness in a particular context, possibly engineering or construction. The vertical lines represent the material, while the rectangles on the sides could symbolize components or sections of a larger structure. The arrows indicate direction or movement, possibly illustrating how the thickness applies to or affects those components. The red dot may highlight a specific point of interest in the thickness measurement. Overall, the image is structured to convey important dimensional information in a systematic and clear way. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RKbT1wmufrStMz~aTVuKwA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RKbT1wmufrStMz~aTVuKwA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength4::Length4

Specifies the length of the vertical plate. If Length4 is set to zero, a stanchion is drawn instead of a vertical plate.


Image:[Image-Analysis: The image depicts a simplified schematic diagram, likely representing a rectangular object with a specified length. It has two side panels (highlighted in gray) and a central rectangular area divided into horizontal sections. The dimensions are indicated, specifically with "Length 4" written at the bottom, suggesting that the overall length of the object is 4 units. Additionally, a red dot is marked in the center area, which may represent a point of interest, such as a reference point for measurements or a focal point on the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WmPASA26FkbpGOw2cwKVhQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WmPASA26FkbpGOw2cwKVhQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Specifies the width of the vertical plate. If Length4 is set to zero, Width4 specifies the diameter of the stanchion.


Image:[Image-Analysis: The image depicts a simple diagram illustrating a geometric shape, specifically a circle, centered within a rectangular structure. The rectangle is labeled 'Width 4', indicating that the width of the rectangle is four units. The circle appears to have a grey fill with a small red dot in the center, suggesting it may represent a point of interest or a coordinate within the shape. There are also horizontal lines within the rectangle, which may indicate sections or divisions within the overall structure. This illustration could be used to demonstrate concepts in geometry or design, such as area, shape arrangement, or measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lJXBh0psP~5JR0D_uDHCqg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lJXBh0psP~5JR0D_uDHCqg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness5::Thickness5

Specifies the thickness of channel clips. Channel clips are only shown when Thickness5 is greater than zero.


Image:[Image-Analysis: The image presents a technical drawing of a component, likely a cross-section of a cylindrical object with labeled features. At the top, there are two small rectangles that could represent controls or connection points. The central portion displays a circular shape filled with gray, indicating a material or an internal part. Below the circle, there are horizontal lines that may represent layers or divisions within the component. The lower part has two horizontal lines with a label indicating "Thickness5," which likely specifies the thickness of a certain layer or the overall dimension of the design. Overall, this drawing conveys technical specifications for engineering or manufacturing purposes, particularly emphasizing the geometry and structural elements of the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o5YI6F4KTbFHOzIts_6UCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o5YI6F4KTbFHOzIts_6UCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength5::Length5

Specifies the length of channel clips.


Image:[Image-Analysis: The image depicts a schematic representation of a mechanical device, potentially a container or part of a machine. It shows a rectangular shape with dimensions labeled. There are two gray sections on either side, which could represent the ends of the device, while the central section is marked with horizontal lines that may indicate different compartments or levels. A red dot appears to mark a reference point within the central section. Below the rectangular shape, there is a measurement labeled "Length5," suggesting a specific dimension of the entire structure. The arrows at the bottom indicate length measurement, pointing to both sides of the device to reinforce that the total length measures 5 units. The overall layout implies a design used in a technical or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Z89PHQ3iMHFR4hOajYPUQg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Z89PHQ3iMHFR4hOajYPUQg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth5::Width5

Specifies the width of channel clips.


Image:[Image-Analysis: The image illustrates a rectangular figure with dimensions labeled. The rectangle has a width of 5 units, indicated by an arrow and the text "Width5" at the bottom, showing the horizontal measurement. Inside the rectangle, there is a circle that is filled in grey, with a red dot positioned internally. The rectangle appears to have an upper part with two small rectangles at the top, possibly representing handles or supports, while the main body is wider and rectangular with a hollow middle area containing the circle. This image could represent a technical drawing or schematic, possibly for understanding the dimensions and layout of an object or piece of equipment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C87ygo8vEe3su4~1xOcgtg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/C87ygo8vEe3su4~1xOcgtg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth6::Width6

Specifies the distance between channel clips.


Image:[Image-Analysis: The image illustrates a technical diagram of a cylindrical shape with specified dimensions. The cylinder is represented in a side view with the width indicated at the bottom as "Width6", suggesting its width measurement is 6 units. At the center, there is a filled circle which likely represents the circular face of the cylinder. The top part of the diagram features two small protrusions, possibly indicating mounting points or structural features. The entire diagram provides a simplified visual reference for understanding the shape and dimensions of the cylinder. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_RR5O9zO7BFSAOMT9B9SXg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_RR5O9zO7BFSAOMT9B9SXg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the bolt. Pin1Diameter and Pin1Length must be greater than zero for the bolts to be shown.


Image:[Image-Analysis: The image illustrates a technical drawing or diagram that depicts a mechanical component with specified measurements. The component appears to have two parallel rectangular sections at the top and bottom, with a circular shape in the middle featuring a small red dot, possibly indicating a reference point or a pin location. There is a dimension labeled "Pin1Length" positioned vertically to the right, suggesting that this is the measurement for the length of the pin associated with the component. The overall structure conveys a clear representation of the component's features and dimensions, which could be important for assembly or design purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/brFEGSrR91H2I6jlWkgP~g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/brFEGSrR91H2I6jlWkgP~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt. Pin1Diameter and Pin1Length must be greater than zero for the bolts to be shown.


None: 

IJUAhsHeight1::Height1

Specifies the distance from the pipe centerline of the first pipe to the top of the
block clamp.


Image:[Image-Analysis: The image depicts a diagram showing the relationship between two rectangular boxes and a circular object. The upper box is labeled with a height measurement labeled as "Height1", indicating the vertical dimension of the boxes. In the center, a circular shape is shown, which appears to represent a section or cross-section of a cylindrical object that fits within the boxes. The circular object is shaded gray with a small red dot at its center, possibly indicating a point of interest or reference. The lower box is aligned with the upper box, suggesting that both boxes may serve as containers for the circular object. Overall, the image illustrates the spatial relationship and dimensions between the boxes and the circular entity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/huty8do5XIZR6xC52DJ8Dg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/huty8do5XIZR6xC52DJ8Dg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the distance from the pipe centerline of the first pipe to the bottom of
the block clamp.


Image:[Image-Analysis: The image depicts a geometric representation involving a circular shape and rectangular boxes. There are two rectangular outlines, one on top and one below, with a gray circle positioned in between them. This circle appears to be centered within the rectangular shapes. To the right of the image, there is a vertical line labeled "Height2" pointing toward the bottom of the image, suggesting it measures the vertical distance between the two rectangles or relevant features in the illustration. The visual representation indicates a relationship between the circular object and the two rectangles, possibly implying a cross-sectional view or a design where the circle fits within the rectangles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0bCw759Qpbme7JbO6owuFA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0bCw759Qpbme7JbO6owuFA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the lateral offset of block clamp if it is not centered on the pipe. If
there is more than one pipe, Offset1 specifies the distance between the pipes.


Image:[Image-Analysis: The image illustrates two configurations involving circular objects from a side view. The top part depicts a single circular object centered between two parallel plates, with an indicated offset distance labeled "Offset1." The red dot likely marks a reference point or center of the circle. The bottom part shows a configuration with two circular objects positioned side by side, again aligned with the plates and sharing the same offset distance "Offset1." This comparison highlights the relationships between the positions of the circular objects in relation to the plates and their alignment, showcasing the differences in layout between having one versus two circular objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MjJwFdV51_sI1Ybfuy0mQg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MjJwFdV51_sI1Ybfuy0mQg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset2::Offset2

Specifies the lateral distance from the center of the pipe to the edge of the block.
Offset2 is used if there is only one pipe and Offset1 is set to zero.


Image:[Image-Analysis: The image appears to be a technical diagram showing two rectangular shapes positioned above each other, with a circular object placed between them. The top shape is labeled "Offset2," indicating that this might relate to a diagram concerning offsets in mechanical or engineering contexts. The arrows pointing left and right suggest that there is movement or positioning involved, and the presence of the circle between the rectangles might represent a component or part that is being offset or adjusted. The details hint at a design consideration where the alignment or spacing of components is critical, possibly in machinery or manufacturing. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KATfvyjTYbDjU_X2RYcEiQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KATfvyjTYbDjU_X2RYcEiQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset3::Offset3

Specifies the distance between blocks. Offset3 is used only if there are two blocks. If Offset3 is less than the block Width, then only one block is shown. Also, if Offset3 is greater than or equal to the block Width, then two blocks are shown.


Image:[Image-Analysis: The image depicts a simple schematic design featuring four vertical rectangles positioned above a horizontal rectangle, which has a darker gray fill. The horizontal rectangle appears to represent a base or a system, while the vertical rectangles could symbolize objects or components related to the system. The term "Offset3" is indicated below the structure, suggesting a specific measurement or spacing related to the design. This could relate to the positioning of the components in relation to each other, indicating that their placement has an "offset" or gap defined as "3". The overall design could represent a configuration in engineering or system design, where the relationship and spacing between the components are crucial for functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zh~JRsqjiGbGtQ5KjHG2cg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zh~JRsqjiGbGtQ5KjHG2cg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Row Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313283?contentId=kRsGwLqV4nprnhj3qrc1BQ)
These properties specify the bolt row properties for the block clamp. Two rows of
bolts are allowed. Each row can have a different offset distance from the center of
the block, a different quantity of bolts in the row, and different configurations
and spacing of bolts in the row.


Image:[Image-Analysis: The image depicts a mechanical or structural component with two bolt rows indicated on either side. There are two labeled areas: "Bolt Row 1" is positioned above and "Bolt Row 2" is below the central component. The image visually represents the arrangement of bolts, suggesting that the component is designed for fastening purposes. The small circular dots within the bolt rows likely signify the locations where bolts would be inserted. This setup typically indicates a connection point where two or more parts are securely joined together. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VTzddLbkPgb6ullJrOl7dQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VTzddLbkPgb6ullJrOl7dQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset4::Offset4 and IJUAhsOffset5::Offset5

Specifies the distance from the center of the block clamp to the center of the bolt.
Offset4 offsets bolts in bolt row 1. Offset5 offset bolts in bolt row 2.


Image:[Image-Analysis: The image represents a mechanical or structural diagram featuring two elements labeled "Offset4" and "Offset5." These offsets are indicated by two blue arrows showing movement or distance adjustments between the elements. The diagram implies that the two components can be aligned or adjusted in relation to each other, which is possibly important for precision in assembly or operation. The shaded areas may represent supports or surrounding structures where these offsets are applied. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ohIaAtdUt_xkfX9h2QY65w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ohIaAtdUt_xkfX9h2QY65w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty

Specifies the quantity of bolts in each bolt row. If Qty1 is zero for any row, bolts are not seen in that row.

IJUAhsMulti2::Multi2Qty

Specifies the quantity of bolts in each bolt row. If Qty2 is zero for any row, bolts are not seen in that row.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti2::Multi2LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the spacing of the location based on the LocateBy attribute.

IJUAhsMulti2::Multi2Location

Specifies the spacing of the location based on the LocateBy attribute.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Thread Connection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313291?contentId=GtzsHTefXabGCYZ385akDw)
These properties specify the thread connection properties for the block clamp.

IJUAhsShapeType::ShapeType

Specifies the type of shape to use for the top connection graphic. Enter a codelist
number from the HS\_S3DParts\_Codelist.xls workbook on the hsShapeType sheet. Allowed codelist numbers for hsShapeType are:

* 1 - Round
* 2 - Square (Rectangle)
* 3 - Hex

IJUAhsThickness6::Thickness6

Specifies the thickness of the top (down) connection shape, which is defined as the
outside face of the clamp to the outside face of the side connection.


Image:[Image-Analysis: The image depicts a technical drawing of a circular object showing its thickness as indicated by the label "Thickness6". The drawing has a cylindrical shape with a circle at its center, suggesting that it could represent a cross-section of a cylindrical part. The dimensions and details about the circular part are likely relevant to its manufacturing or design specifications. There are also arrows indicating direction, signifying the thickness measurement vertically, while the horizontal lines suggest a boundary or extent of the object. Various elements in this drawing imply the need for precise manufacturing tolerances, which is important in engineering and design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MqBZdu1M_iVDIBb6ZMSMUg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MqBZdu1M_iVDIBb6ZMSMUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth7::Width7

Specifies the outside dimension of the top (down) connection shape.

1 - Round


Image:[Image-Analysis: The image depicts a rectangular shape indicating a part with a specified width of 7 units. In the center of the rectangle, there is a circle that appears to have a small red dot in the middle, which might represent a specific reference point or feature of the design. On either side of the rectangle, there are smaller circles that might suggest mounting holes or connectors. This design could be indicative of a mechanical or structural component where the measurements and reference points are essential for accurate placement or assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EHDO42u3b4ucVrqoNonF9A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EHDO42u3b4ucVrqoNonF9A-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Image-Analysis: The image displays a rectangular object with a width measurement labeled as "Width7". There are circular features on either side of the rectangle, which may represent connectors or attachment points. Additionally, there is a small red square located within a centered rectangular area. This suggests a central point of focus, possibly indicating a feature or component that is vital to the functionality of the object. The overall design and markings appear technical, likely representing a schematic or blueprint of the object for engineering or architectural purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dfAhuEcmHJg3garu4guOfg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dfAhuEcmHJg3garu4guOfg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Image-Analysis: The image illustrates a mechanical part, specifically a plate or block that includes features for fastening or positioning. At the top of the image, the term "Width7" indicates that the width of the part is 7 units (the units, such as millimeters or inches, are not specified). The main body of the part is shown as a rectangular shape with two circular holes located towards the ends, which are typically used for mounting or fastening the part to another piece. In the center, there is a hexagonal recess depicted, possibly intended for a screw or bolt. The red dot in the hexagon might signify a critical point of reference or the location for a component that interacts with this piece. Overall, this image provides a detailed view of the dimensions and key features of the mechanical part, highlighting its functional aspects for assembly or integration in a larger system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CYhBuFNrNm~ggWlSZtilDQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CYhBuFNrNm~ggWlSZtilDQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth8::Width8

Specifies the width of the inside connection shape. For ShapeType2 (square), use Width8 to create a rectangle instead of a square. If this value is zero or not specified,
ShapeType2 is a square shape.


Image:[Image-Analysis: The image depicts a rectangular shape with a defined width, labeled as "Width8." Inside the rectangle, there is a smaller rectangle located at the center, which is marked with a red square. This indicates that the focus is on the specified width of the outer rectangle, possibly to illustrate a measurement or a layout design. The arrows pointing up and down suggest vertical alignment or centering of the inner rectangle within the outer one. The overall interpretation suggests a design or engineering context where precise measurements and alignment are crucial. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2AkkLkEYTsj2v8Nh1ScQcw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2AkkLkEYTsj2v8Nh1ScQcw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313300?contentId=UW5bhbOAxuk52C50yqcxrQ)
These properties are used to specify the different port types and their sizes for
the block clamp.

Route Port


Image:[Image-Analysis: The image consists of two diagrams illustrating routing paths labeled "Route". The first diagram shows a routing scenario where route "Y" is directed upward, and route "Z" is directed to the left. This indicates the direction of the routes relative to some unspecified entity. In the second diagram, route "X" is directed to the right while route "Z" remains directed downward, suggesting a different routing scenario. Both diagrams emphasize the changes in routing directions for the specified routes with respect to their coordinates. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0thZMpyAjAGu4ulNXnjGwg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0thZMpyAjAGu4ulNXnjGwg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Route

The x-axis of the route port should be parallel to the length of the block clamp.
The z-axis should be pointing in the downward direction.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1016 (Pipe Clamp) | Diameter1 | Diameter1 | Diameter1 |

Structure Port

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pj0fA45QMv3RK09rTI7kuA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=759361430f66ef45)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pj0fA45QMv3RK09rTI7kuA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 2 - Structure

Connects the block clamp to the structure.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 (Steel) | 0 | -9999 | 9999 |

Rod Port


Image:[Image-Analysis: The image illustrates two different orientations of a rod in relation to defined axes. The top section shows a rod in a vertical position with the Y-axis pointing up and the Z-axis directed upwards. The circular outline signifies the rod's circular cross-section. The bottom section presents the rod positioned horizontally with the Z-axis still vertical but now the X-axis is horizontal. This representation helps visualize how the rod's orientation affects its positioning in a three-dimensional space, demonstrating the relationship between its axis of rotation and the defined coordinate system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/89kkpI_J8MkzOUVeOhKZVg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/89kkpI_J8MkzOUVeOhKZVg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 3 - Rod

Connects the block clamp to a hung nut. This port is only included if a threaded connection
is used.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 (IntThdRH) 1003 (IntThdLH) | 0 | 0 | Thickness6 |

Weld Port


Image:[Image-Analysis: The image depicts various welding symbols and orientations used in engineering and manufacturing. It shows four different views of welded joints: two from the top and two from the front. The symbols indicate where welding is applied, denoted by the term "Weld." The arrows labeled "Y" and "Z" represent dimensions or directions relevant to the welding operation. The top two images, with circular components, suggest a type of joint assembly, while the bottom images show side views with lateral elements that provide a deeper understanding of how the parts are joined. Overall, the image illustrates different welding orientations and their respective placements in a mechanical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZDKtiGTdCi12hUpz8j4Paw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZDKtiGTdCi12hUpz8j4Paw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 4 - Weld

Specifies the location on the supporting structure where the part is welded. The port
orientation is the same as the route port.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 (Other) | -9999 | -9999 | -9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773452?contentId=CFVRJ5~~1QBfj3Jw2loIxQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Bolt  
Part Name: Bolt  
Part Description:  
Bolt of <Diameter>mm Rod Diameter with Hexagonal / Square / Rectangular / Circular / Oval Head  
Anchor of 16mm Rod Diameter with Hexagonal/Square Nut

![Bolt SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/emuhQskJijETCRtn4aub8w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=751a90d026969467)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/emuhQskJijETCRtn4aub8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample bolt SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.

   ![S3D Bolt and Anchors SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QsMasvRbe73nqM55JFGKMw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=405cf3b960cf3edf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QsMasvRbe73nqM55JFGKMw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

The default units for bolt parts is millimeters (mm). Type "in" at the end of the
dimensional values to specify inches. Ports are shown as points highlighted in red.

Local Coordinate System

![Bolt SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I~NmbGbnTYkL8xT5IeKZrQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1389e9f855bd7c60)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I~NmbGbnTYkL8xT5IeKZrQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |
| --- | --- |
| 1 | Bolt Head |
| 2 | Port1:RodEnd1  (0,0,TWPlateCount \* Thickness3) |
| 3 | Rod |
| 4 | Port2:RodEnd2  (0,0,TWPlateCount \* Thickness3 + Gap1) |
| 5 | Nut |
| 6 | Bottom Washer Plates |
| 7 | Top Washer Plates |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Head Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773459?contentId=5OsT6DSM0krs6GgIgHqZ9w)
Specifies the shape and structure of the bolt head. The following properties are categorized
under bolt head attributes:

IJUAhsBHShape::Shape1Type

Specifies the shape of the bolt head. This property uses the following codelist values:

1 - Round


icon-description of a circular loading or progress indicator: 

2 - Square


look for icon that looks like a loading or spinner indicator: 

3 - Hex


look for icon that resembles a hexagon with a circle in the center, typically representing an empty space or a placeholder: 

4 - Anchor Type 1


look for an icon that resembles a funnel or a conical shape, which may indicate a process of directing or focusing something: 

5 - Anchor Type 2


look for icon that resembles a megaphone or loudspeaker: 

IJUAhsBHShape::Shape1Width1

Specifies the outer dimension of the bolt head. This property uses the following codelist
values:

1 - Round


Image:[Alt-Text: Bolt Head Attribute - Shape - Round 
Image-Analysis: The image depicts a vertical arrow next to a circle. The vertical arrow suggests movement or measurement in a vertical direction, while the circle could represent various concepts such as a target, object, or a component in a system. This combination implies a relationship where the circle is likely subject to measurement, analysis, or adjustment in the vertical direction, which could be relevant in fields like geometry, engineering, or physics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B2Mk_84hNy5SvL5a79qJnw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape - Round](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B2Mk_84hNy5SvL5a79qJnw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Alt-Text: Bolt Head Attribute - Shape - Square 
Image-Analysis: The image consists of two diagrams. The first diagram on the left shows a vertical double-headed arrow, indicating movement or scaling in the vertical direction. This could represent resizing or adjusting height in a graphical user interface. The second diagram on the right features a circle with a dotted outline, which typically represents a placeholder for an object or a graphical element that can be populated or filled in, such as an image or a button. Together, these diagrams suggest a user interface context where vertical adjustments are coupled with placeholders for content. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DXLAmKwqFEP5on9YOfcIiQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape - Square](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DXLAmKwqFEP5on9YOfcIiQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


Image:[Alt-Text: Bolt Head Attribute - Shape - Hex 
Image-Analysis: The image depicts a hexagonal shape with arrows pointing outward on both ends. This configuration suggests a process or flow where something is being expanded or pushed outward from the center. The central hexagon likely represents a process or a component, while the arrows indicate an outward flow or communication in two directions. This could symbolize a network or connection extending from the central element, often associated with collaboration or distribution in graphical representations. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tnyLTO9eNvSAhS1lkgEaEg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape - Hex](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tnyLTO9eNvSAhS1lkgEaEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

4 - Anchor Type 1


Image:[Alt-Text: Bolt Head Attribute - Shape - Anchor 
Image-Analysis: The image shows a diagram of a funnel, which is typically used to channel liquids or fine-grained substances into containers with a small opening. The funnel is depicted in a simple outline, and it indicates a measurement scale on the right, suggesting varying heights. The wide opening at the top facilitates the pouring process, while the narrow spout at the bottom allows for precise deposition of the contents. This represents a common object used in both kitchen and laboratory settings, with connections to tasks involving transferring liquids or powders without spilling. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zJbURu3lhtEUF0jzfSEAEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape - Anchor](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zJbURu3lhtEUF0jzfSEAEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 - Anchor Type 2


Image:[Alt-Text: Bolt Head Attribute - Shape - Anchor Type 2 
Image-Analysis: The image depicts a simple line drawing of a tube and a chamber, likely illustrating a basic component of a fluid dynamics system or a gas flow mechanism. The left side shows a long, straight tube leading into a geometric chamber that has a slight tapering shape, suggesting a change in cross-sectional area. This can indicate the principle of flow through a constriction, which can affect pressure and velocity. The diagram is typically used in engineering or physics to explain how substances move through a different structured path. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QPCt0ngZwACB5hMFGpTVrQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape - Anchor Type 2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QPCt0ngZwACB5hMFGpTVrQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsBHShape::Shape1Width2

Specifies the outer dimension of the bolt head. This property uses the following codelist
values:

1 - Round


look for icon that resembles a circle with arrows pointing left and right, indicating movement or sliding: 

2 - Square


icon-description showing a circular shape with arrows indicating horizontal movement or stretching, suggesting the concept of resizing or dragging an object.: 

3 - Hex


icon that looks like a hexagon with arrows indicating width or dimensions: 

4 - Anchor Type 1


Image:[Alt-Text: Bolt Head Attribute - Shape1Width2 - Anchor 
Image-Analysis: The image depicts a simplified diagram of a pipe or nozzle, where the left end is wider and the right end is more narrow, suggesting a tapered shape. The vertical arrows indicate the potential flow direction and various diameter sizes of the nozzle, which is commonly used in fluid dynamics to illustrate how fluid velocity increases as it travels through a narrowing section. This concept is significant in various applications such as fluid mechanics, engineering designs, and aerodynamics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vI4YzEzYWoH789bvmQAHHA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Shape1Width2 - Anchor](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vI4YzEzYWoH789bvmQAHHA-_PVFQNoCl4XmjAxWO0f7XQ/content)

5 - Anchor Type 2

IJUAhsThickness1::Thickness1

Specifies the thickness of the bolt head.

Bolt head


Image:[Alt-Text: Bolt Head Attribute - Bolt Head Thickness 
Image-Analysis: The image depicts a simple mechanical system involving a structure (represented by the rectangular box) and two arrows on either side indicating forces or movements towards the box. The arrows signify a compressive force being applied towards the box from both left and right, illustrating that the box is the object being acted upon by these forces. The red dots at the base of the rectangle may indicate points of interest or specific points where the forces are received or measured. Overall, the image conveys a concept of compression in a mechanical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NJSbyhZY3abBi4C2PHAdIQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Bolt Head Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NJSbyhZY3abBi4C2PHAdIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Anchor head


Image:[Alt-Text: Bolt Head Attribute - Anchor Head Thickness 
Image-Analysis: The image depicts a simple line drawing of a nozzle shape, which is wider at one end and tapers to a narrow end, typically used in various technical contexts such as engineering, physics, or fluid dynamics. Adjacent to the nozzle, there is a scale indicator showing a length measurement, possibly denoting the width or some dimension related to the nozzle design. This image may be used to convey concepts in aerodynamics, fluid flow, or nozzle design principles, indicating how fluid might behave as it passes through the narrowing section. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wgjsUAOmZIsnqS3wJTPyQg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Head Attribute - Anchor Head Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wgjsUAOmZIsnqS3wJTPyQg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rod Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773507?contentId=XHRkpfA2JoEOvmgDu11Bdg)
IJUAhsRodDiameter1::RodDiameter1

Specifies the rod diameter in the bolt. This property is used in the part selection
rule.


Image:[Alt-Text: Bolt Rod Attribute - Rod Diameter 
Image-Analysis: The image depicts a simplified diagram of a measuring tool, possibly related to the concept of checking dimensions. On the left, there is a vertical scale marked with black dots and two red indicators at different heights. This indicates measurements being marked, possibly showing a range. To the right, there is a rectangular box which could represent a measured object or space, along with two small icons representing measurement endpoints, suggesting that it is a tool used for taking precise measurements between points. The image emphasizes the relationship between the scale and the measurement being taken, illustrating how distance is quantified in varying increments. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fxSMQ~zuSD8HPezDaOPK2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Rod Attribute - Rod Diameter](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fxSMQ~zuSD8HPezDaOPK2w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength::Length

Specifies the total length of the bolt including the bolt head thickness.


Image:[Alt-Text: Bolt Rod Attribute - Rod Length 
Image-Analysis: The image illustrates a mechanical component, likely a bolt or screw assembly, showing its various parts and their relationships. The main components labeled include: Head, Rod, Nut, and Length. The Head is at one end, securing the assembly, while the Nut is at the other end, providing a fastening mechanism. The Rod represents the shaft of the bolt or screw. 'Length' refers to the total length of the assembly measured from the Head to the Nut. Additionally, 'OverLength' could indicate the portion of the Rod that extends beyond the Nut, which may be relevant in specific applications for fitting or securing purposes. Understanding these components and their measurements is crucial for applications in mechanical engineering, construction, or assembly tasks. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8zdQp85kid9eqcLOZYSK_w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Rod Attribute - Rod Length](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8zdQp85kid9eqcLOZYSK_w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the length of the rod that extends past the RodEnd1 or ends before RodEnd1. This property uses the following codelist values:

If OverLength > 0


Image:[Alt-Text: Bolt Rod Attribute - OverLength > 0 
Image-Analysis: The image illustrates a cross-section diagram of a concrete slab with a specific element referred to as the "Head." The diagram includes labels that indicate various components: the "Length" is marked at the bottom, showing the span of the slab, while "Concrete/Slab" is indicated on the right side, denoting the material and structure being addressed. The "Head" is a rectangular block positioned within the slab, likely representing a structural element or support feature. The arrows suggest dimensions and directions of measurement related to the slab and its elements. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kVsTMuMeN0_WYSWQDhwC_w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Rod Attribute - OverLength > 0](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kVsTMuMeN0_WYSWQDhwC_w-_PVFQNoCl4XmjAxWO0f7XQ/content)

If OverLength < 0


Image:[Alt-Text: Bolt Rod Attribute - OverLength < 0 
Image-Analysis: The image illustrates a simple diagram of a concrete or slab structure. It features a rectangular block representing the slab, labeled as "Concrete/Slab." The diagram also includes two key dimensions: "Length" marked on the horizontal axis and "Head" on the vertical section. The "Length" measurement indicates the extent of the slab horizontally, while the "Head" dimension indicates a vertical measurement related to the height or thickness of the slab. The arrows suggest that these dimensions can be measured or adjusted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YE0QpSgDgXuWZsqfQeXXNw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Rod Attribute - OverLength < 0](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YE0QpSgDgXuWZsqfQeXXNw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773523?contentId=NTPG0UUfzw5AHdHurTYKXA)

Image:[Alt-Text: Bolt Nut Attributes - Thickness 
Image-Analysis: The image appears to be a technical diagram of a mechanical component, likely a type of shaft or coupling. It features numbered parts that may denote different features or sections of the component. The numbers (1 to 7) are surrounded by circular callouts, which indicate that they are points of interest or reference. For instance, point 1 might represent a specific feature at the top section, while point 2 could indicate another key area above the main body. The lines connecting these points suggest there may be measurements or relationships depicted between these reference points. Point 6 is highlighted to show a vertical dimension, implying a measurement related to the overall height or length of the component. This diagram is likely used for engineering or manufacturing purposes to communicate specifications or assembly instructions for the component in question. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oRJxpUbswMeiE9BVthit5Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Nut Attributes - Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/oRJxpUbswMeiE9BVthit5Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

1 - Port2:HeadEnd  
2 - Bolt Head  
3 - Top Washer Plates  
4 - Rod  
5 - Bottom Washer Plates  
6 - Nut  
7 - Port1:RodEnd

IJUAhsNutShape::Shape2Type

Specifies the shape type of the nut. This property uses the following codelist values:

1 - Round


icon-description of a circular loading or progress indicator: 

2 - Square


look for icon that looks like a loading or spinner indicator: 

3 - Hex


look for an icon that resembles a hexagon with a circle in the center: 

IJUAhsNutShape::Shape2Width1

Specifies the outer dimension of the nut shape. This property uses the following codelist
values:

1 - Round


Image:[Alt-Text: Bolt Nut Attributes - Shape Width - Round 
Image-Analysis: The image displays a diagram that consists of two primary shapes: a vertical double-headed arrow on the left, indicating a measurement of height or verticality, and a circle on the right, which may represent a cylindrical object or a measurement of diameter. The vertical arrow suggests that the height of something is being measured or compared, while the circle indicates a cross-sectional view, possibly denoting diameter or circular motion. This image could be used in contexts such as engineering or physics to illustrate concepts related to dimensions or motion. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OSalfxW~Qj1WB7u2rqoWNw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Nut Attributes - Shape Width - Round](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OSalfxW~Qj1WB7u2rqoWNw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Alt-Text: Bolt Nut Attributes - Shape Width - Square 
Image-Analysis: The image depicts two different icons. On the left, there is an icon representing vertical movement, indicated by two vertical arrows pointing upwards and downwards. This typically signifies a function related to moving or adjusting items along a vertical axis. On the right, there is a simple outline of a square with a circular shape inside it. This can represent various concepts but is often used to indicate a placeholder, a loading graphic, or as an element for interaction in user interface design. The juxtaposition of these two icons may suggest functionality where one controls a vertical aspect while the other represents an object or activity within a defined space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/msxCNlqYeN4enggQIakSvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Nut Attributes - Shape Width - Square](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/msxCNlqYeN4enggQIakSvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


icon-description: hexagon with arrows on either side indicating a directional flow or movement, possibly representing a process or a cycle.: 

IJUAhsNutShape::Shape2Width2

Specifies the outer dimension of the nut shape. This property uses the following codelist
values:

1 - Round


icon-description of a circular dial with arrows indicating horizontal movement or adjustment: 

2 - Square


icon that indicates a slider or adjustable element, featuring a circular knob and arrow indicators on both ends: 

3 - Hex


icon-description: hexagon with arrows on either side indicating a directional flow or movement, possibly representing a process or a cycle.: 

IJUAhsThickness2::Thickness2

Specifies the thickness of the nut.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Washer Plate Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773632?contentId=84mSyxRjBroCx362k3y2bA)
![Bolt Washer Plate Attributes - Gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Wq41bOSJ5X8Pp5VV3YX99w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=72f1e85fcce57d9d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Wq41bOSJ5X8Pp5VV3YX99w-_PVFQNoCl4XmjAxWO0f7XQ/content)

1 - Port2:RodEnd2  
2 - Bolt Head  
3 - Top Washer Plates  
4 - Rod  
5 - Bottom Washer Plates  
6 - Nut  
7 - Port1:RodEnd1

IJUAhsWPlateShape::Shape3Type

Specifies the attributes for the washer plate shape types. This property uses the
following hsShapeType codelist values:

1 - Round


icon-description of a circular loading or progress indicator: 

2 - Square


look for icon that looks like a loading or spinner indicator: 

3 - Hex


look for an icon that resembles a hexagon with a circle in the center: 

IJUAhsWPlateShape::Shape3Width1

Specifies the outer dimension of the washer plate shape. This property uses the following
codelist values:

1 - Round


Image:[Alt-Text: Bolt Nut Attributes - Shape Width - Round 
Image-Analysis: The image depicts a vertical line with an arrow pointing up and down, indicating measurement or scaling of height. To the right of this line, there is a circle, which seems to represent another measurement, possibly suggesting a relationship between the two elements as height and diameter or radius. This design could be used in contexts such as engineering, geometry, or physics to convey measurements or sizes of circular objects in relation to their height. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OSalfxW~Qj1WB7u2rqoWNw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Nut Attributes - Shape Width - Round](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OSalfxW~Qj1WB7u2rqoWNw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Square


Image:[Alt-Text: Bolt Nut Attributes - Shape Width - Square 
Image-Analysis: The image consists of two parts. On the left, there is an icon illustrating a vertical double arrow, which typically represents resizing or adjusting from top to bottom. It implies movement or change along the vertical axis. On the right side, there is a square outline with a small circle inside it. This may indicate a button or a toggle switch that can be activated or selected. The circle could represent an option that is currently selected or an interactive element within the square area. Together, these elements suggest functionality related to user interface elements for changing dimensions or toggling selections. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/msxCNlqYeN4enggQIakSvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Bolt Nut Attributes - Shape Width - Square](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/msxCNlqYeN4enggQIakSvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

3 - Hex


icon-description: hexagon with arrows on either side indicating a directional flow or movement, possibly representing a process or a cycle.: 

IJUAhsWPlateShape::Shape3Width2

Specifies the outer dimension of the washer plate shape. This property uses the following
codelist values:

1 - Round


icon-description of a circular dial with arrows indicating horizontal movement or adjustment: 

2 - Square


icon that indicates a slider or adjustable element, featuring a circular knob and arrow indicators on both ends: 

3 - Hex


icon-description: hexagon with arrows on either side indicating a directional flow or movement, possibly representing a process or a cycle.: 

IJUAhsThickness3::Thickness3

Specifies the thickness of the washer plate.

IJUAhsTWPlateCount::TWPlateCount

Specifies the number of washer plates above the plate or the existing steel.

IJUAhsBWPlateCount::BWPlateCount

Specifies the number of washer plates below the plate or the existing steel.

IJOAhsGap1::Gap1

Specifies the gap between the top and the bottom washer plates. The top washer plate
is always attached to the bottom of the bolt head. The bottom washer plate is always
attached to the top of the nut (if a nut exists).

If no washer plates exist, the gap is calculated as the offset value between the bolt
head and the nut. You can set this value using CSD.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773637?contentId=ph3KI9QU0Yr_PCqOSpnQ5g)
The following graphic illustrates the orientation of the port types and their sizes
for the beam clamp:

![Bolt SmartPart - Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2bmUexCUS47IJJZSbvShLw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=fcf8a2c357851c55)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2bmUexCUS47IJJZSbvShLw-_PVFQNoCl4XmjAxWO0f7XQ/content)

The bolt SmartPart has two ports, RodEnd1 and RodEnd2. The port RodEnd1 is usually
connected to an external nut and the port RodEnd2 is connected to an anchor plate,
an existing steel, or any other part.

Port details and their orientation

Port1:RodEnd1

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 - Other | 0 | -9999 | 9999 |

Port2:RodEnd2

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 - Other | 0 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/773640?contentId=9plI7wggWg0QDwGc2X9VtQ)
The BOM description must only use the part description. It is not defined in the symbol
code and the value for the IJHgrBOMDefinition::BomType property is set to 2.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clevis - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307490?contentId=tdTiWFsehebzTVuSj4pz5Q)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Clevis  
Part Name: Clevis  
Part Description: Clevis SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yoLjrqEt35t2EOKISLTBQg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=312c987ac88a1b94)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yoLjrqEt35t2EOKISLTBQg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Clevis SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Clevises > Clevis with Pin as shown in the following example:

   ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZR0ZsWUJo0PHkdn1OyZNHg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c1fa6410f04f9e80)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZR0ZsWUJo0PHkdn1OyZNHg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a technical illustration related to mechanical components, showing two different views of an assembly. On the left side, there is a vertical representation of a mechanism with labels indicating different parts: "Surface" at the top, "RodEnd" at the bottom, and several elements marked with a red square symbol indicating "Bolt/Pin/Hole". This suggests these parts are critical points for assembly or connection. On the right side, a side view includes a circular part labeled with "Z" and "X" axes, illustrating the orientation and potentially highlighting the direction of movement or force within the system. The labeled axes help clarify spatial relationships and mechanics in operation. This overall composition indicates how the various components connect and function within a mechanical system, likely for engineering or design purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jZAhDxVwQnETNABykHCWog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jZAhDxVwQnETNABykHCWog-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Clevis Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307491?contentId=DaWL7gF4oJPPwCcWFs1Whg)
The following properties are used for the part selection rule and the location of
the ports. You must enter the values to get a correct port location and for the selection
of clevis part based on part selection rule.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of dimensional value to use inches.

IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of the rod that attaches to the eye nut. This value
is used only for part selection rules for choosing the correct clevis part and has
no impact on creating graphics.


Image:[Image-Analysis: The image displays a diagram of a hydraulic system with two parts: a vertical component on the left and a horizontal component on the right. The left side illustrates a piston-like mechanism with a cylinder and rods, showing movement directions through arrows. The red dots highlight specific points on the device, possibly representing pressure points or measurement markers. The right side depicts a circular component, which may serve as a reservoir or a wheel connected to the hydraulic system. The overall setup suggests a relationship between these elements in a hydraulic application, demonstrating how force or fluid is transferred through the system to perform work. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VU8cdh76~iLcINVmpDJs~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VU8cdh76~iLcINVmpDJs~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance between the pin port and the port at the end of the rod. This
value represents the amount that the clevis takes out of the overall rod lengths.


Image:[Image-Analysis: {
  explanation="The image depicts a mechanical system consisting of several components, including various cylinders, a connector with a triangular indicator, and a circular component at the bottom. The left side shows two vertical cylinders with red markers at the top, indicating points of interest. The middle section illustrates a connection represented by lines and the triangular indicator, which might suggest direction or flow between components. At the bottom, a circular shape is present, possibly representing a rotational component or a physical element, which connects the hydraulic or pneumatic systems indicated by the cylinders."
} 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hbSIk7wL_rIlCDtpNK0KoA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hbSIk7wL_rIlCDtpNK0KoA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOpening1::Opening1

Specifies the distance from the pin centerline to the inside face of the end nut.


Image:[Image-Analysis: The image depicts two hydraulic cylinders, commonly used in machinery to provide linear motion. The left cylinder shows a double-acting hydraulic actuator with an extended rod. The red dots indicate the points where fluid pressure enters or exits the cylinder, controlling the movement of the piston inside. The right cylinder is a single-acting type, which has a different mechanism as it uses pressure to move in one direction and relies on gravity or a spring to return. Both cylinders are connected to their respective control mechanisms, illustrated by the arrows indicating the flow of hydraulic fluid. The schematic gives a visual representation of how these components interact in a hydraulic system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bnwBf27G1rGBMbybjaV~Jg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bnwBf27G1rGBMbybjaV~Jg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Nut Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307492?contentId=6TgV_GuwGtLs9jLv48MQxw)
These properties specify the end nut shape properties for the clevis.

IJUAhsShape1::Shape1Type

Specifies the codelist number of the type of shape as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

* 1 - Round


Image:[Image-Analysis: The image illustrates a mechanical system consisting of a cylindrical body with a top component resembling a disk and a rectangular base. The top disk has a hole in the center, indicating it might be a view from the top of a component like a washer or bearing. Below the disk, there is a reference to a rectangular box representing a main body or housing of the entire mechanical setup. The red dots highlight key points of interest within the mechanical assembly, possibly indicating areas for measurement or attachment. The overall design suggests a system where rotational or linear motion may occur, common in machines or mechanical devices. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QHmWPdRew2ZFAVbrQ27ZqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QHmWPdRew2ZFAVbrQ27ZqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: Could not explain Image because of Safe AI filtering issues. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_O3wznbjbYZLwTXqnH1rUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_O3wznbjbYZLwTXqnH1rUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image appears to be a technical diagram showing a mechanism or device, likely a type of actuator or control valve. The upper part is indicated by a hexagonal shape, possibly representing a screw or a cap, while below it is a housing featuring connections or ports. Red dots are present at strategic points, perhaps indicating specific areas of interest or attachment points. The dashed line symbolizes a boundary or separating line that could represent different sections of the device. The two rectangular shapes at the bottom may depict supports or mounting bases for stability. Overall, the image illustrates a controlled flow or actuation system, highlighting its structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrlJD_EvMoVMnBBrFw3eFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrlJD_EvMoVMnBBrFw3eFw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the end nuts. If this value is set to zero, then
the end nut shape is not displayed.

* 1 - Round


Image:[Image-Analysis: The image illustrates a mechanical system consisting of a cylindrical body with a top component resembling a disk and a rectangular base. The top disk has a hole in the center, indicating it might be a view from the top of a component like a washer or bearing. Below the disk, there is a reference to a rectangular box representing a main body or housing of the entire mechanical setup. The red dots highlight key points of interest within the mechanical assembly, possibly indicating areas for measurement or attachment. The overall design suggests a system where rotational or linear motion may occur, common in machines or mechanical devices. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QHmWPdRew2ZFAVbrQ27ZqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QHmWPdRew2ZFAVbrQ27ZqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: Could not explain Image because of Safe AI filtering issues. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_O3wznbjbYZLwTXqnH1rUA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_O3wznbjbYZLwTXqnH1rUA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image appears to be a technical diagram showing a mechanism or device, likely a type of actuator or control valve. The upper part is indicated by a hexagonal shape, possibly representing a screw or a cap, while below it is a housing featuring connections or ports. Red dots are present at strategic points, perhaps indicating specific areas of interest or attachment points. The dashed line symbolizes a boundary or separating line that could represent different sections of the device. The two rectangular shapes at the bottom may depict supports or mounting bases for stability. Overall, the image illustrates a controlled flow or actuation system, highlighting its structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrlJD_EvMoVMnBBrFw3eFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrlJD_EvMoVMnBBrFw3eFw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the value only for NutShape2 (square). This value is used to create a rectangular
nut instead of a square nut. If this value is set to zero or is not specified, then
NutShape2 is drawn as a square.


Image:[Image-Analysis: The image depicts a schematic representation of a mechanical device, possibly a hydraulic or pneumatic actuator, showing its main components and their relationships. At the top, there is a square section with a circular hole, representing the cylinder or housing. Below this, two vertical lines, which likely signify pistons or rods, extend downward from the cylinder, indicating moving parts that translate motion. The dots highlighted in red may represent key points of interest or connection points. The overall image illustrates how these components interact, emphasizing the direction of force or motion within the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/26SCS7VZ9BwF3bOCZNiUZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/26SCS7VZ9BwF3bOCZNiUZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the thickness of the end nut shape. Only positive values are acceptable.
If this value is set to zero or to a negative, then the end nut shape is displayed.


Image:[Image-Analysis: The image depicts a mechanical component, possibly a suspension or linkage mechanism, represented in a simplified schematic format. It shows a central element (likely a shock absorber or a similar part) with a striped zone at the top signifying a compressible material, probably to absorb shocks. Below this central component are two ends resembling mounts or supports that are connected to it. The red dots indicate key points of interest, likely where force or movement is being applied. The vertical arrows suggest movement, indicating that the central element can extend or compress, which is crucial for understanding how the device functions in response to external forces. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mijaPrqy~5l5JmbaSuLyeQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mijaPrqy~5l5JmbaSuLyeQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Round Ends Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307493?contentId=yIPENoilCQfziZzo0G82GQ)
These properties define the round block properties at the ends of the two sides used
for holding the pin/bolt. If no values are provided, then the side blocks are extended
to hold the pin/bolt.

IJUAhsDiameter2::Diameter2

Specifies the outside diameter of the round ends of the clevis. If this value is set
to zero or to a negative, then the round ends are not drawn.


Image:[Image-Analysis: The image illustrates a simple hydraulic system involving a pump and a hydraulic cylinder. It demonstrates how force can be transmitted through a fluid, as indicated by the arrows showing direction and flow. The system features a pump on the top right, which likely pushes fluid through the lines, leading to a hydraulic cylinder on the left. This cylinder is indicated to change its position due to hydraulic pressure. The small red squares suggest measurement points or control points for pressure readings within the system. The circular shape at the bottom right may represent an actuator or wheel, indicating motion or output from the hydraulic action. Overall, the elements are connected in a way to show how energy transfer can move mechanical components in applications like machinery or vehicles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Q~rI3XUuOyDtq_mhE_t5KQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Q~rI3XUuOyDtq_mhE_t5KQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the round ends of the clevis. If this value is set to a
negative, then zero is used.


Image:[Image-Analysis: The image depicts a mechanical system that consists of two main components: a double-acting cylinder on the left and a single-acting cylinder on the right. The double-acting cylinder, which is taller and has a red indicator or marking, can push and pull due to fluids acting on both sides of its piston. This allows for movement in both directions, making it versatile for various applications. The single-acting cylinder, seen on the right, operates using pressure to extend but relies on gravity or a spring to retract, which is less complex. The relationship between these two components lies in their functionality; they are both types of actuators used in mechanical systems, but they operate differently depending on the system's design needs. Additionally, arrows at the bottom suggest that there is movement involved in this assembly, indicating a mechanism meant for action or mechanical work involving linear displacement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JONH1EWZaVZamKB3qevODw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JONH1EWZaVZamKB3qevODw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap2::Gap2

Specifies the gap between the round ends of the clevis. This value can be set to zero;
negative values, however, are not acceptable. If this value is set to a negative,
then zero is used.


Image:[Image-Analysis: The image depicts a mechanical setup involving two different components: a vertical assembly on the left and a cylindrical structure on the right. The left side illustrates a rectangular unit with an upper part and a lower part connected by a vertical element, which implies it may represent a piston or a similar device in a hydraulic or mechanical system. The colored dots might indicate operational points or key areas of focus in the mechanism. The right component appears to represent a cylinder, which could also function as a piston or similar mechanism, suggesting a linkage or operational relationship to the left unit. The arrows at the bottom indicate potential movement or adjustment directions, emphasizing interaction between the two elements in the context of motion or force application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/F3JGl6~F8FGS0serqK7_Xg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/F3JGl6~F8FGS0serqK7_Xg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Blocks Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307494?contentId=mX6J4IKQCuI43TKet97uig)
These properties specify the rectangular block properties for the two sides of the
clevis. The default length is from the pin centerline to the inside face of the end
nut shape. While the length can be extended by key-in values for the two overlength
properties, there is no way to taper or angle the blocks. The drawings are shown with
the round ends, but based on the needs of the side plates used as either side blocks
or round ends and side blocks.

IJUAhsWidth3::Width3

Specifies the width of the side blocks. If this value is set to zero or to a negative,
then the side blocks are not drawn.


Image:[Image-Analysis: The image appears to represent two types of machinery or mechanical components. On the left side, there's a hydraulic actuator design, often used in systems that require linear motion. The two rectangular boxes at the top represent the housing, and the vertical bar suggests the shaft or cylinder that moves. The red dots likely indicate points of interest or connections, such as mounting points or fluid entry/exit points. On the right, there's a representation of a valve mechanism, signified by the cylindrical shape with arrows indicating direction of flow. This suggests it may regulate fluid movement. Both components seem to connect through a tube-like structure, integral for fluid transfer in hydraulic systems. Overall, the connection signifies a hydraulic system where the actuator performs work on the fluid regulated by the valve. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/owTGDdftrWf0ZcndtZif~g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/owTGDdftrWf0ZcndtZif~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

JUAhsThickness3::Thickness3

Specifies the thickness of the side blocks. If this value is set to zero, then the
software uses the value defined for Thickness2. If this value is set to a negative, then the side blocks are not drawn. If both Thickness2 and Thickness3 values are set to zero, then the side blocks are not drawn and a warning is displayed.

IJUAhsGap3::Gap3

Specifies the gap between the rectangular side blocks. If this value is set to zero,
then the software uses the Gap2 value. If Gap2 is set to zero, then zero is used.

.
Image:[Image-Analysis: The image depicts a schematic representation of two types of hydraulic components. On the left, there is a hydraulic cylinder illustrated, characterized by a rectangular body with input and output ports marked by red dots. It shows a piston mechanism, indicated by arrows that suggest the direction of the piston's movement within the cylinder—this movement creates force. On the right is a hydraulic accumulator, depicted as a cylindrical shape at the bottom with a circular top. The accumulator stores hydraulic fluid under pressure, as indicated by the dotted outline of the circular top, suggesting it can expand and contract. The relationship between these two components is that a hydraulic cylinder uses fluid pressure to generate linear motion, while an accumulator helps maintain pressure and supply fluid as needed, ensuring smooth operation in a hydraulic system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bCXhucPlohFW2OlhbOkApQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bCXhucPlohFW2OlhbOkApQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the amount by which the side blocks are to extend beyond the inside face
of the end nut shape.


Image:[Image-Analysis: The image depicts a hydraulic system with two main components: a hydraulic cylinder on the left and a pneumatic cylinder on the right. The hydraulic cylinder is shown with its sections labeled, including a rod and a body, and it appears to have red indicators, possibly denoting pressure points or fluid entry points. On the right side is the pneumatic cylinder, which consists of a movable piston inside a cylinder body, also represented with a circular end that likely indicates the extending or retracting motion of the piston. The arrows between the two cylinders suggest a connection or relationship, possibly indicating that the operation of one affects the other, as both are mechanisms used in fluid systems for motion control. The arrangement hints at an illustration meant to explain the differences or functionality within hydraulic and pneumatic systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PFQe9hey2EhoU~rORFXLNQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PFQe9hey2EhoU~rORFXLNQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength2::OverLength2

Specifies the amount by which the side blocks are to extend beyond the bolt/pin centerline.
Over length values are used when there is no need for a round end shape, resulting
in the rectangular side blocks being extended to hold the bolt/pin. This value can
be set to a positive or a negative. If a positive value is used, no round ends are
shown.


Image:[Image-Analysis: The image depicts two hydraulic cylinders, which are commonly used in machinery and equipment for lifting or pushing objects. Each cylinder consists of a cylindrical body that houses a piston. The left cylinder has a piston positioned inside it, with red dots indicating the positions of the pistons. The arrows pointing up and down suggest the movement of the pistons as hydraulic fluid is injected or drained, causing them to extend or retract. The right side features a larger cylinder, possibly indicating a secondary system or a different application. Overall, this setup illustrates the principle of hydraulic force in engineering applications, demonstrating how pressure can be utilized to perform work. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5_Mxc7d4lPNsjajx9vbw2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5_Mxc7d4lPNsjajx9vbw2w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin/Bolt Properties (Clevis) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307495?contentId=UIkY7VGDgrV9HQSCHcKp9A)
These properties specify bolt/pin properties of a welded beam attachment and are used
to set the pin/bolt size and the port location.


None:  If Pin1diameter and Pin1Length are set to zero, then the pin/bolt is not drawn. You must change the port to an appropriate
hole type in the HS\_S3DParts.xls workbook and a separate bolt/pin will need to be modeled.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt/pin. Use this property as a connection diameter
from AIR when joining between the clevis and eye nut. If this value is set to zero,
then the pin is not drawn.


None:  An AIR that joins a clevis to an eye nut reads Pin1Diameter from the clevis and passes it into the PinDiameter prompt of the EyeNut.


Image:[Image-Analysis: The image depicts a mechanical hydraulic system with two main components: a vertical cylinder on the left and a hydraulic piston on the right. The vertical cylinder is oriented upright, apparently equipped with two small rectangular boxes at the top and middle, possibly indicating points for measurement or connection to other systems. The hydraulic piston on the right consists of a vertical positioning system used to control the movement. A connection line between the two systems, along with arrows, suggests that the system is engineered for controlled movement, likely facilitating the transfer of force through a hydraulic medium. The image also includes red dots, which may represent points of interest or connection in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sQfEQ~KOGT0iIN_Dw8kBHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sQfEQ~KOGT0iIN_Dw8kBHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the bolt/pin. If this value is set to zero, then the pin is
not drawn.


Image:[Image-Analysis: The image depicts two mechanical components that appear to be some form of couplings or linkages used in engineering. On the left side, we see a structural element that resembles a sliding element connected by vertical rods allowing movement. The red dots might indicate points of mechanical interest or pivot points. The right side displays a circular element with a central hole and a pin, suggesting it may be used in rotational applications or as a coupling joint. The overall diagram likely aims to illustrate how these components can interact or be assembled in a mechanism. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OexYSnGyGO1sxb2wCWA9tQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OexYSnGyGO1sxb2wCWA9tQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307496?contentId=3uB3Ch4c9p1TfvSbzQLhMQ)
These properties are used to specify the different port types and their sizes for
the clevis

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vPhzdOPunc6J~u36h~k5zg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=63c22c525f481a2e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vPhzdOPunc6J~u36h~k5zg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Clevis


Image:[Image-Analysis: The image presents a mechanical diagram illustrating the components of a system with a focus on spatial orientation represented by coordinate axes. On the left, there are two vertical elements that seem connected by a central component. The right side of the image showcases a detailed view of a rod end, indicating the locations and orientations of axial directions – X, Y, and Z. The arrows signify the direction of the axes: X suggests horizontal direction, Z indicates vertical direction, and Y is implied as depth direction. The diagram also highlights a circular component labeled "Bolt/PIN/Hole" at the bottom of the right section, further enforcing the understanding of how these elements might fit together in a mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xTIpeVPdo43LdAGQ0~CuYA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xTIpeVPdo43LdAGQ0~CuYA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 - Pin or Hole  Location (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1005 -- Pin (or) 1007 -- Eye | Pin -- Pin1Diameter  Hole -- Hole Diameter | Use 0 | Pin -- Pin1Diameter  Hole -- Hole Diameter |

Port2 - RodEnd Location: (0, 0, RodTakeOut)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001 – IntThdRH (or) 1003 – IntThdLH | * The diameter of the rod that connects other components. * Enter the same value as RodDiameter. | Use 0 | Use 9999 |

Port3 - Surface  Location: (0, 0, Opening1 + Thickness1)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable for this type port. Use 0. | Not applicable for this type port. Use -9999. | Not applicable for this type port. Use 9999. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clevis Hanger - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308136?contentId=~IThp9MgtQ2WNLeXbn1uaQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ClevisHanger  
Part Name: Clevis Hanger  
Part Description: Clevis Hanger SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TENpyul8KuMbTCC9Yu7gdw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0c3078831501bbdb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TENpyul8KuMbTCC9Yu7gdw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Clevis Hanger SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Clevises > Adjustable Clevis Hanger as shown in the following example:

   
Image:[Image-Analysis: The image depicts a hierarchical structure representing different categories and subcategories of components under the title "SmartParts." At the top level, there is the category "S3D Standard," which branches into "Beam Attachments" and further into "Clevises." Under "Clevises," there are three subcategories: "Adjustable Clevis Hanger," "Clevis - no Pin or Bolt," and "Clevis with Pin." In addition to "Clevises," there are other miscellaneous components listed, such as "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Struts," and "U-Bolts." This organization provides a clear overview of part types and their relationships, indicating that the main focus is on different types of clevises and their specific features. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1~nzmSbC8E68KAG6cYwYhw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1~nzmSbC8E68KAG6cYwYhw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W756ObEK0Qr~JrTwfP2bDQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d571e9f18bf935c4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W756ObEK0Qr~JrTwfP2bDQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Clevis Hanger Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308139?contentId=C1kd4Fp2RYrCpcULkKhZvQ)
IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of the rod that is attached to the clevis hanger.

IJUAhsSize::Size (Optional)

Used for part selection rules for choosing a correct clevis hanger part and is not
used for creating graphics.

IJUAhsMinRod::MinRod (Optional)

Specifies the minimum amount of rod required by the clevis hanger. This value is not
used for creating graphics.

IJOAhsAngle1::Angle1

Specifies the slope of the pipe on which the clevis hanger part is being used. By
default, this value is set to zero. If it is not equal to zero, the clevis hanger
will pivot about the bolt with the given angle as shown in Fig. 2.


None: 

IJUAhsClevisTopShp::ClevisTopShp

Specifies the top shape of the clevis hanger. The value for this column is a codelist
number, and valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook in the hsClevisTopShape sheet.

* 1 = Shape 1


Image:[Image-Analysis: The image represents a basic mechanical structure, likely a simplified illustration of a lifting device or crane. It features a rectangular base with vertical supports on either side, which could be indicative of a frame or a stand. At the top, there is a horizontal bar that appears to be a component for lifting or suspending an object. The central pillar is shaded and marked with a red dot at its base, suggesting a point of activation or a feature such as a winch or pivot. This structure could be utilized in various applications, such as construction or manufacturing, where lifting or moving heavy objects is necessary. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T10CdmgXvTOfvVSsxd~Hng-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T10CdmgXvTOfvVSsxd~Hng-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 = Shape 2


Image:[Image-Analysis: The image depicts a simplified representation of a mechanical or structural element, likely a type of mechanical arm or crane. There is a vertical component in the center, which appears to be holding a horizontal beam, suggesting that this structure is capable of lifting or manipulating objects. The two horizontal lines extending from the sides indicate the base or supports on which this arm rests, possibly implying a stable foundation. The red dot at the bottom could signify a pivot point or anchor that provides stability and enables movement of the vertical component. Overall, the elements in the image suggest a design intended for lifting or moving items in a controlled manner, with a clear focus on balance and structural integrity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NqJsgMJWnmQDhLuwI4dxIA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NqJsgMJWnmQDhLuwI4dxIA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 = Shape 3


Image:[Image-Analysis: The image depicts a caliper, an instrument used to measure internal and external dimensions, as well as depths, of objects. The caliper shown has a main body with two arms: one of which is a measuring point while the other is an adjustable end to grasp the object being measured. The red dot likely indicates a measurement marker or reference point. The structure is typically used in various fields such as engineering, metalworking, and woodworking for precise measurements. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e8l2Jy73yslqPl4jKQQ4MA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e8l2Jy73yslqPl4jKQQ4MA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClevisBotShp::ClevisBotShp

Specifies the bottom shape of the clevis hanger. The value for this column is a codelist
number, and valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook in the hsClevisBotShape sheet.

* 1 = Round


Image:[Image-Analysis: The image depicts a U-shaped structure resembling a tube or funnel, with two vertical lines representing the sides and a curved bottom. At the center of the curved bottom, there is a small red dot. This shape is often associated with various scientific or engineering applications, such as fluid dynamics or magnetic fields, where the U-shape could symbolize a path of flow or direction of force. The red dot may represent a point of interest or focus within the system, potentially indicating a specific measurement or a point of interaction within the context represented by the U-shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~t8lwn8hggCLGjeu90HqHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~t8lwn8hggCLGjeu90HqHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 = Vee

* 3 = None - Used to create a hanger roller, as shown below:


Image:[Image-Analysis: The image shows a diagram of a mechanical device, possibly illustrating a mechanical press or a similar apparatus. It features two vertical sides framing a large circular component in the center, which could represent a pressure plate. At the top, there is a smaller, vertical component that appears to be a handle or lever, suggesting a manual operation. The red dot in the center of the circular component may indicate a focal point or an area of interest, such as where pressure is applied or monitored. The base of the apparatus shows a rectangular platform, likely serving as the foundation or support for the entire structure. This diagram could be related to concepts in engineering or mechanical design, illustrating how pressure is distributed through the device when operated. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iiudHVoAL5QifJbSsasRjQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iiudHVoAL5QifJbSsasRjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance from the pipe centerline to the end of the rod that attaches
to the clevis hanger. This value is always greater than 0.5 \*Diameter1 + Pin1Diameter.


Image:[Image-Analysis: The image depicts a mechanical component that appears to be a type of pulley or a mechanism for lifting. The central part is a circular object, possibly representing a wheel or gear, with a highlighted red dot indicating a specific point of interest. Above the circular component, there is a vertical rod or shaft that could represent an actuator or a lifting mechanism. To the right of the drawing, there is an annotation labeled "RodTakeOut," which likely indicates how to adjust or remove the rod for maintenance or technical procedures. The layout suggests a simple mechanical relationship where the rod controls the movement or function of the circular component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qd2WIVjJuxd_7dMGi0H9bA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qd2WIVjJuxd_7dMGi0H9bA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the distance from the pipe centerline to the top of the clevis hanger. This
value is always greater than RodTakeOut.


Image:[Image-Analysis: The image illustrates a simple pulley system featuring a wheel with a belt and a load at the bottom. The pulley is shown from a side view, and there are two labeled measurements: Height1, which suggests the vertical distance from the top of the pulley to a reference point, likely the center of the wheel. Additionally, a red dot is marked at specific points, indicating locations that may denote where to attach or observe load distribution. The wheel has a circular shape at the bottom, which represents the pulley itself, while the rectangle above it signifies the housing or frame that supports the pulley system. This image portrays basic mechanical principles used in lifting systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u1yBGn3Oukj58B4I4uUZcw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u1yBGn3Oukj58B4I4uUZcw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the total inside diameter of the clevis hanger. If ClevisBotshp = 3, set this value the same as the pipe diameter.


Image:[Image-Analysis: The image depicts a mechanical device often used to measure the diameter of circular objects or holes. At the bottom, there is a circle representing the object whose diameter is being measured. The term "Diameter1" is indicated at the bottom, suggesting this measurement is specifically concerned with this dimension. The vertical component above suggests a possible measuring rod or a gauge that provides a reference point for the measurement process. There are also red dots denoting measurement points or reference markers for clarity in finding the diameter. Overall, the image is schematic and serves the purpose of demonstrating the measurement of diameter in a clear and precise manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dAejvPMr3hTGIgsT87Y5AA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dAejvPMr3hTGIgsT87Y5AA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308140?contentId=hI5jPvHuDZnaS59NaG2Ctw)
These properties define the geometry of the top shape of the clevis hanger.

IJUAhsWidth1::Width1

Specifies the width of the top portion of the clevis hanger. This value is always
greater than RodDiameter. In cases where it is less than or equal to zero, the software sets Width2 to its default value.


Image:[Image-Analysis: The image depicts a vertical diagram that illustrates a structural component characterized by a section labeled as "Width1" at the top. The upper part of the component is shown wider than the lower part, which has a slightly different design. There are two marked points at the top and bottom of the component, indicated by red dots, that could represent key measurement points or features. The upper part appears to taper towards a narrower section, while the lower part is solid and wider. The design suggests a focus on structural proportions and possibly functionalities related to width measurements in a construction or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cWzUdhFvFDceNi8hD5EW1w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cWzUdhFvFDceNi8hD5EW1w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the top portion of the clevis hanger. This value must always
be greater than zero. In cases where it is less than or equal to zero, the software
sets Thickness2 to its default value.


Image:[Image-Analysis: The image depicts a mechanical device, likely a cylindrical component or a pulley, with specific emphasis on a dimension labeled "Thickness1" indicated by arrows pointing to the thickness between two parts. The device has a circular body at the bottom, likely representing a wheel or a circular pulley. Above the wheel, there's a frame structure attached, and the entire assembly is shown from a top-down perspective. The red dots at the center suggest a focal point, possibly indicating the axis of rotation or a key feature of the design. The illustration highlights the importance of measuring the thickness, which is crucial for ensuring the proper fit and function of the parts involved. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5nhfRXxNa3wi3fhTynEVLw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5nhfRXxNa3wi3fhTynEVLw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight3::Height3

Specifies the height from the lowest part of the top section of the clevis hanger
to the flat spot on top.

* If ClevisBotShp ¹ 3 and Height3 is less than RodTakeOut - (Height2 - PinDiameter / 2), then the software sets Height1 - (Height2 - 1.5 \* Pin2Diameter) as the default value.


Image:[Image-Analysis: The image depicts a mechanical pulley system that includes a circular part (representing a pulley) and a height measurement labeled as "Height3." The pulley is represented in a simplified schematic form with various components indicated, including a frame and a central axis. The red dots likely signify specific points of interest or dimensions in the system. The relationship highlighted here is between the height of the pulley system and the pulley itself, indicating that the height measurement is relevant to the mechanics of the pulley. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JV6oyoGX2PFt1CuGyz8F8g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JV6oyoGX2PFt1CuGyz8F8g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* If ClevisBotShp = 3 and Height3 is less than Height1 + Height2, then the software sets Height1 + (2 \* Height2) as the default value.


Image:[Image-Analysis: The image depicts a schematic representation involving a cylindrical system where a circular object (grey circle) is situated inside a vertical container. The top of the container is open, allowing access to the object inside. There are marked points, illustrated with red dots, which might indicate specific measurement points or reference points along the vertical axis. On the right side, there is a dimension labeled "Height3," indicating a specific height measurement, possibly relevant to the context of the image. The overall structure suggests a focus on understanding the object's position or measurement in relation to the container. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pODZAZXFwvgtg4SFGiu~9w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pODZAZXFwvgtg4SFGiu~9w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight4::Height4

Specifies the height from the lowest part of the top section of the clevis hanger
to the corner where the top angles in.

* If ClevisBotShp ¹ 3 and Height4 is either less than Height3 or less than RodTakeOut - (Height2 - PinDiameter / 2), then the software sets 3 \* Pin1Diameter as the default value.


Image:[Image-Analysis: The image depicts a mechanical setup, likely a pulley or a similar device. It shows a circular object (probably a pulley wheel) at the bottom with a rod extending vertically above it. There is a rectangular frame structure at the top connecting to the vertical rod. The height from the top structure to a reference point (indicated by a red dot) is labeled as "Height4," suggesting a specific measurement that can be crucial for understanding the dimensions of the setup. The use of the red dots might indicate key points or centers of rotation for precise mechanical applications. This image provides a basic visual representation of mechanical components and their arrangement, useful in engineering or physics contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nG8QuZ2V9wCS72WC8osaCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nG8QuZ2V9wCS72WC8osaCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* If ClevisBotShp = 3 and Height4 is either less than Height3 or less than Height1 + Height2, then the software sets Height3 - (3 \* Pin1Diameter) as the default value.


Image:[Image-Analysis: The image depicts a schematic representation of a tank or container that includes a circular object, presumably a liquid body or a solid sphere, at its bottom. Above this circular object, there is a vertical element, possibly a rod or a pipe that reaches the top of the tank, indicated by the height measurement labeled "Height4". This likely signifies that the height of the tank is being measured from the bottom of the circular object to the top of the vertical element. The circle is marked with a red dot at its center, possibly indicating a focal point or a specific reference spot for measurement. Overall, the image illustrates a setup where a height measurement is relevant to the circular object inside the tank. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sUBARuvHiEu2VgbJlE2p6Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sUBARuvHiEu2VgbJlE2p6Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

* If ClevisTopShp = 3, then Height4 is ignored.

IJUAhsLength1::Length1

Specifies the length of the top flat spot. If this value is less than RodDiameter, then the software sets 3 \* RodDiameter as the default value.


Image:[Image-Analysis: The image illustrates a mechanical assembly or device, possibly a type of clamping or fastening mechanism. At the top, there is a rectangular component resembling a handle or lever, which is oriented vertically. Below this, a horizontal part extends outward, likely indicating a range of motion or function. The central part shows a circular body, probably a coupling or holding area, depicted in gray with a red dot at the center, possibly indicating a focal point or pivot. Alongside, there are additional details indicating a measurement called "Length1", suggesting the importance of the distance between two given points in the assembly. The entire image represents an assembly where different components interact, highlighting a relationship between the parts for operational functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/urIKRK2OHQ8pbS1YoDkPvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/urIKRK2OHQ8pbS1YoDkPvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the top inside length, depending on which set of conditions is true:

* Condition A

  + If ClevisBotShp ¹ 3 and Length2 is less than Length1 and ClevisTopShp = 1, then the software sets Diameter1 + 2 \* Thickness2 as the default value.

    OR
  + If Length2 ¹ Length1 and ClevisTopShp = 3, then the software sets Length1 as the default value.


Image:[Image-Analysis: The image depicts a mechanical setup that appears to be a pulley or a similar device, showcasing a circular element at the center labeled with a red dot indicating its center. The structure has a rectangular frame on top and two side supports, giving it a sturdy appearance. The term "Length2" is labeled at the bottom, suggesting that it may refer to a measurement related to the device or its components. Overall, the image provides a clear representation of the device's configuration and measurements, possibly for educational or instructional purposes in mechanics or physics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBXNI_9qteEye16G5bLhRw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YBXNI_9qteEye16G5bLhRw-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Condition B:

  + If ClevisBotShp = 3 and Length2 is less than Length1 and ClevisTopShp = 1, then the software sets Diameter1 + 2 \* Thickness2 as the default value.

    OR
  + If Length2 is not equal to Length1 and ClevisTopShp = 3, then the software sets Length1 as the default value.

IJUAhsLength3::Length3

Specifies the length of the lower flat spot. This value is used only when ClevisTopShp = 2. If this value is less than or equal to zero and ClevisTopShp = 2, then the software sets 0.125 \* Length1 as the default value.


Image:[Image-Analysis: The image depicts a mechanical setup, likely related to a pulley or a similar system. At the top, there are two supports connected to what appears to be a rod (indicated by the small vertical line) that likely serves to guide or control movement. The circular shape at the bottom represents a wheel or pulley, which is typically used to change the direction of force or to lift objects. The red dots might indicate important points of interest, such as pivot points or focus points of measurement. The term "Length 3" suggests that there might be a specific measurement related to this system, potentially referring to the length of the rod or the distance between components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5j4nkqTqbHgjPEakIBdQTw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5j4nkqTqbHgjPEakIBdQTw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308142?contentId=MPHQvHUjaFWBpRvj0xJ9IA)
These properties define the geometry of the bottom shape of the clevis hanger.

IJUAhsWidth2::Width2

Specifies the width of the bottom portion of the clevis hanger. This value is always
greater than Pin1Diameter. If this value is less than or equal to Pin1Diameter, then the software sets Width1 as the default value.


Image:[Image-Analysis: The image illustrates a schematic representation that shows a vertical rectangular shape, which could represent a component or a cross-section of an object. At the top, there is a narrower section highlighted with some shading, indicating a possible key feature or component. Below that, there is a larger, solid area that is filled with a gray color. The area contains two red dots that appear to represent points of interest, likely denoting specific markers or references within this shape. The overall dimensions of the object are labeled as "Width1," and arrows are shown indicating horizontal measurements, suggesting that this section might be relevant for design or construction purposes. This visualization might be used in engineering or architectural contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvUM6tVE4JJpGZtIQywgwg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvUM6tVE4JJpGZtIQywgwg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the bottom portion of the clevis hanger. This value is
always greater than or equal to zero. If this value is equal to zero, then the software
sets Thickness1 as the default value.


Image:[Image-Analysis: The image depicts a technical diagram focusing on a circular object represented in gray, surrounded by a structural element resembling a clamp or holder. The diagram includes a bold arrow indicating a specific measurement labeled "Thickness2," which likely refers to the thickness related to the circular object or the distance between the components of the clamp. The red dots present in the diagram may signify key points of interest or measurement locations. Overall, the diagram illustrates the relationship between the clamp mechanism and the circular object, emphasizing the measurement aspect. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EF_TFBQjIr0TCGb7h5tmmg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EF_TFBQjIr0TCGb7h5tmmg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight5::Height5

Specifies the height from the pipe centerline to the top-most edge of the bottom section
of the clevis hanger. If this value is less than 0.5 \* Diameter1 + Pin1Diameter, then the software sets RodTakeOut - 5 \* Pin1Diameter as the default value.


Image:[Image-Analysis: The image depicts a mechanical apparatus for lifting a spherical object, likely a ball or a weight. The apparatus consists of a frame that supports the sphere-shaped object below it. There are vertical guides or tracks that help to keep the sphere stable while being lifted. Red dots are indicated, possibly marking points of interest or connection. The image also includes a dimension labeled "Height5," which suggests that the height measurement is important for understanding the setup. This height may refer to the distance from the base of the apparatus to the top point of the lift or the maximum height to which the object can be raised. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ytXurBhMG5jHnd6oMoCAvQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ytXurBhMG5jHnd6oMoCAvQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight6::Height6

Specifies the height from the pipe centerline to the top edge of the angled section
of the clevis hanger. Presuming the vee is a 45-degree angle, if ClevisBotShp = 1, then this value is ignored; however, if this value is less than or equal to 0, then
the software sets Height7 - 0.5 \* Diameter1 as the default value.


Image:[Image-Analysis: The image depicts a mechanical setup involving a circular object (a ball) suspended below a structure that appears to resemble a grappling or lifting mechanism. The ball is colored grey and has a red dot that indicates its center. Below the ball, there are two vertical arrows labeled "Height" indicating a measurement related to the ball's position within the apparatus. This setup may illustrate a physics concept related to mechanics, possibly involving center of mass, equilibrium, or force application, depending on how the apparatus interacts with the ball. The overall configuration suggests a system of balance and measurement in a mechanical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eOB2hTRBzwrWbyFlZ8KdWQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eOB2hTRBzwrWbyFlZ8KdWQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight7::Height7

Specifies the height from the pipe centerline to the bottom of the angled section
of the clevis hanger. Presuming the vee is a 45-degree angle, if ClevisBotShp = 1, then this value is ignored; however, if this value is less than or equal to 0, then
the software sets Height7 - 0.5 \* Diameter1 / sin(45) as the default value.


Image:[Alt-Text: Height7 
Image-Analysis: The image depicts a mechanical setup involving a circular object, likely a sphere, positioned within a frame. The frame is designed to support and possibly manipulate the circular object, as indicated by the overhead structure that appears to be a lifting mechanism. The circular object is represented in gray, showing its position within the frame. A dotted line labelled "Height7" suggests that this setup has a specific height measurement tied to it, possibly indicating the distance from the base of the frame to the top of the circle. Red dots are used to highlight critical points of interest, such as the center of the circle and a point on the overhead structure, which may denote where force is applied or measured. This image likely represents a concept in physics or engineering, potentially related to the dynamics of objects within a specific height or gravitational context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tTHNrtSaOY1Ismp53iC12g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Height7](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tTHNrtSaOY1Ismp53iC12g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308144?contentId=kDNNGmDLAbIC9xZwajGtfA)
These properties define the geometry of the bolt.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the bolt. If this value is less than or equal to zero, then
the software sets RodDiameter as the default value.


Image:[Image-Analysis: The image depicts a diagram of a component that likely relates to mechanical engineering or assembly. At the center is a circular shape labeled "Pin1Diameter," which indicates a focus on the diameter measurement of a pin. Above the pin, there is a rectangular structure with vertical lines, which suggest the pin's placement within a housing or mechanism. The arrows pointing up and down beside the pin could indicate movement or location in relation to other components. Overall, this image is used to illustrate how the pin's diameter is crucial to the function of the assembly, potentially affecting fit, stability, and operation within a larger mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3ccR4S8LB6yQIstL9C8AQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3ccR4S8LB6yQIstL9C8AQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the bolt. If this value is less than or equal to zero, then
the software sets 1.25 \* (Diameter1 + 2 \* Thickness1 + 2 \* Thickness2) as the default value.


Image:[Image-Analysis: The image depicts a mechanical or structural component, likely a type of clamp or support mechanism. The main focus is on a circular element, indicated in gray, which appears to be held in place by vertical components that are part of a rectangular frame. There is a red dot on the circular element, possibly indicating a reference point or a critical location for measurements. The bottom of the image features a label "Pin1Length", suggesting that there is a specific measurement related to the length of a pin or the space between parts of this mechanism. Overall, the image visually represents a component that is likely part of a larger assembly aiming to stabilize or secure a round object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/X4Dky0RMO3s4Hcy7LrQO9A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/X4Dky0RMO3s4Hcy7LrQO9A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the height of the bolt from the pipe centerline to the centerline of the
bolt. If this value is less than or equal to zero, then the software sets RodTakeOut - 1.5 \* Pin1Diameter as the default value. If ClevisBotShp = 3, then the software interprets this value as a negative distance from the pipe centerline.
If this value is less than or equal to zero and ClevisBotShp = 3, then the software sets 0.75 \* Diameter1 as the default value.

* ClevisBotShp ¹ 3


Image:[Image-Analysis: The image depicts a mechanical apparatus, possibly a type of pulley system, where a spherical object (represented in grey) is positioned inside a circular frame. The diagram includes measurements indicated by the term "Height2," which likely refers to the vertical distance from a reference point in the frame to the center of the spherical object. The image may illustrate principles of physics related to mechanics, such as forces or equilibrium, and the relationships between the components of the setup. The red dots in the image likely highlight specific points of interest or measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QpoLvy31jOFSSTEKeBHQcA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QpoLvy31jOFSSTEKeBHQcA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* ClevisBotShp = 3


Image:[Image-Analysis: The image illustrates a mechanical apparatus that involves a cylindrical container with a spherical object inside. The container has a top section that seems to accommodate a measuring device or a gauge, indicated by the vertical element above the sphere. The sphere is likely resting on a horizontal platform or surface in the lower section, from which it is supported. The image highlights a measurement labeled as "Height2," which is marked with upward and downward arrows indicating that this height can vary. This suggests the setup could be used for measuring the height of the sphere or the liquid level in relation to the apparatus, potentially in a physics or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b33j9psn8IV5B9F8CBky4A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b33j9psn8IV5B9F8CBky4A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Liner Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308146?contentId=4CqG~Y~tVKbLiQni5St0Zg)
These properties define the geometry of the liner, which is an optional component.
Values for these properties are necessary only when liner geometry is required.

IJUAhsThickness3::Thickness3 (Optional)

Specifies the thickness of the liner from the inside edge of the clevis hanger.


Image:[Image-Analysis: The image illustrates a mechanical component that appears to involve a circular object (possibly a bearing or a wheel) positioned within a frame or holder. The frame has a specified thickness indicated as "Thickness3" on the left side of the image. There are arrows suggesting that the space between the circular object and the frame is important, likely indicating measurements for clearance or fitting. The red dots and the small cylindrical part at the top may represent a part of a mechanism used to adjust or secure the circular object. Overall, this image seems to focus on the dimensions and fitment of a circular object within a given thickness of a surrounding frame. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3gt5oEEAUYMQANECWVIFmA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3gt5oEEAUYMQANECWVIFmA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight8::Height8 (Optional)

Specifies the height from the pipe centerline to the top of the liner. This value
is always less than Height5.


Image:[Image-Analysis: The image depicts a schematic or technical drawing of a mechanical device, likely a type of clamp or lifting mechanism. At the center, there is a circular object representing a ball or sphere, highlighted in gray, which may indicate that this component is the focus of the mechanism. Surrounding the sphere are two vertical bars that appear to grip the spherical object, with additional elements depicted above that may suggest a lifting mechanism. The image also indicates a measurement labeled "Height8," which likely refers to the height of the mechanism or the vertical distance between components, marked horizontally with arrows illustrating the height measurement. Overall, the image captures the mechanical setup for manipulating or holding the spherical object in place. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YDJmvgrQfGLybKNzk69upg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YDJmvgrQfGLybKNzk69upg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness4::Thickness4 (Optional)

Specifies the overall thickness if the liner is a wrap. If this value is less than
or equal to Thickness3, then the software just draws a liner.


Image:[Image-Analysis: The image depicts a mechanical system that seems to showcase a cross-section view of a device, possibly related to measuring or assessing the thickness of materials. The central round object appears to be a cylinder, and the text "Thickness4" suggests that this device can measure or relate to an aspect of thickness at this specific point. The horizontal arrows indicate a measurement or movement based on thickness, while the red dots may represent specific points of interest or measurement on the device. The overall structure suggests a mechanical setup that might involve pressure or contact to gauge material properties. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HVFxDr6RzBpzm61bj5_DOQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HVFxDr6RzBpzm61bj5_DOQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Spacer/Roller Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308147?contentId=IeV7bT0fTt2QZRNAe_rTbg)
These properties define the geometry of the spacer/roller, which is an optional component
when ClevisBotShp equals 1 or 2. Values for these properties are necessary only when spacer/roller geometry
is required.

IJUAhsPin2::Pin2Diameter (Optional)

If ClevisBotShp is not equal to 3, this value specifies the diameter of the bolt. If ClevisBotShp is equal to 3, then this value specifies the small diameter of the roller. This value
is always greater than Pin1Diameter; otherwise, the spacer is not included. If this value is less than or equal to Pin1Diameter, then the software sets 0.5 \* Diameter1 as the default value.

* ClevisBotShp = 1 or 2


Image:[Image-Analysis: The image depicts a mechanical component, likely a pin or coupling mechanism, possibly used in machinery or mechanisms that require secure fastening. At the center, there is a circular component that seems to represent a pin or axle, indicated with red markings. The term "Pin2Diameter" is specified above it, suggesting a measurement related to the diameter of the pin featured in the image. The arrows pointing up and down likely indicate movement or measurement in relation to the pin's dimensions. Overall, the image provides information about the dimensions and mechanics involved in the design of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nP~SxYTj4IjlXLFEMKxz5Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nP~SxYTj4IjlXLFEMKxz5Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

* ClevisBotShp = 3


Image:[Image-Analysis: The image depicts a mechanical assembly that illustrates the relationship between a pin and a circular object, likely a bearing or a shaft. The top part shows a vertical pin secured in a housing, while below it is a circle that represents the outer diameter of the circular object. Red dots are marked to indicate specific reference points, possibly highlighting the diameter of the circular object in relation to the pin. The label "Pin2Diameter" suggests this image is intended to convey information on how the diameter of the circular object interacts or is measured in relation to the pin, which could be relevant in mechanical design or engineering applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nMSe5b0OAQp7XxePHY9pXg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nMSe5b0OAQp7XxePHY9pXg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin2::Pin2Length (Optional)

Specifies the length of the spacer/roller. If this value is equal to zero, then the
software sets Diameter1 as the default value. If ClevisBotShp = 1 or 2, this value is always less than the smaller of Diameter1 or Length1. If ClevisBotShp = 3, this value is always less than or equal to Length2.

* ClevisBotShp = 1 or 2


Image:[Image-Analysis: The image depicts a diagrammatic representation of a mechanical component, possibly related to a pin and its length. At the top, there is a mechanism that indicates movement or adjustment, represented by the structure surrounding the pin. The central aspect of the diagram features a circular shape, likely denoting a pin, with a clear labeling of "Pin2Length". This indicates the measurement or distance from the bottom of the pin to a point that is presumably critical for the function of the mechanism. This illustration is likely used in engineering or mechanical applications where precise measurements are important. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jo2PGhgOnDjmg_Ug7KK8RQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jo2PGhgOnDjmg_Ug7KK8RQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* ClevisBotShp = 3


Image:[Image-Analysis: The image depicts a technical diagram, likely illustrating a mechanical assembly that includes a pin and a circular object, possibly a bearing or wheel. The pin is positioned above the circular shape, which is centered within a rectangular enclosure. The term "Pin2Length" is labeled beneath the assembly, suggesting it is a measurement related to the length or positioning of the pin in relation to the circular object. The red dots could signify critical points of interest, such as connection points or measurement locations. Overall, the image serves as a schematic for understanding the spatial relationship and lengths involved in the assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOpDtyA4BI9rFj~DuU0NUg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KOpDtyA4BI9rFj~DuU0NUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter2::Diameter2 (Optional)

If ClevisBotShp = 3, this value is the larger diameter of the roller. If this value is less than or equal
to zero, then the software sets 2 \* Pin2Diameter as the default value. If ClevisBotShp = 1 or 2, this property value is not used.


Image:[Image-Analysis: The image illustrates a vertical setup involving a cylinder and a circle. The cylinder appears to have a weight being suspended from its upper part. Below, there is a circular object labeled with a highlight at its center, suggesting that it can be moved or displaced. The term "Diameter2" at the bottom indicates that the size (diameter) of the circular object is significant, likely in a mathematical or engineering context. The visual shows the relationships between the cylinder, weight, and circular object, while also implying that the measurement of the circular object is important for the analysis being conducted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eWKs1D~j4MfOIHBtwiE6iA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eWKs1D~j4MfOIHBtwiE6iA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/308151?contentId=SsG8NsR1AtfYKxXS42QjdQ)
These properties are used to specify the different port types and their sizes for
the clevis hanger.


Image:[Image-Analysis: The image displays a table with four columns labeled as "Port 1: Route", "Port 2: RodEnd", "Port 3: Bolt1", and "Port 4: Bolt2". Each column represents different ports with associated characteristics. For Port 1, there are attributes including "Name", "Size", "MinSize", and "MaxSize", indicating that it contains various properties about a route symbol port. Port 2 has similar attributes related to a "RodEnd", while Port 3 and Port 4 are focused on "Bolt1" and "Bolt2" respectively, with the same types of attributes: "Name", "Size", "MinSize", and "MaxSize". This table is likely used in engineering or technical specifications to categorize and detail different port types and their dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c1Z7bL5ImERQF5SI6i~ToA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/c1Z7bL5ImERQF5SI6i~ToA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Clevis Hanger

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jb9aTOzX81XBjwujimsg2Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=71e4b79012b4d9d0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jb9aTOzX81XBjwujimsg2Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1016 | Diameter1 | Diameter1 | Diameter1 |

Port2 – RodEnd (0, 0, - Height1 – Thickness3 + offset2)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1004 | RodDiameter | 0 | Height1 - RodTakeOut |

Port3 – Bolt1 (0, -Pin1Length/2, Height2)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001-IntThdRH | Pin1Diameter | 0 | 9999 |
| 1003-IntThdLH | Pin2Diameter | 0 | 9999 |

Port4 – Bolt2 (0, Pin1Length/2, Height2)

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001-IntThdRH | Pin1Diameter | 0 | 9999 |
| 1003-IntThdLH | Pin2Diameter | 0 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Concrete Lug Plate - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776603?contentId=ZtfS0FUUi3Z9cpg3rOz3fw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.LugPlate  
Part Name: Concrete Lug Plate  
Part Description: Concrete Single Flat Lug Plate, Hole Dia <Diameter>"  
 Concrete Single Curved Lug Plate, Hole Dia <Diameter>"

![Concrete Lug Plate SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RA9GWatwDukFkeYThVvIww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bee6701c826205b5)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RA9GWatwDukFkeYThVvIww-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Concrete Lug Plate SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Concrete Lug Plate > Concrete Lug Plate as shown below.

   ![S3D Concrete Lug Plate SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ioSv2GA4UEMaBHdIie1tDg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=085f39634503e69b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ioSv2GA4UEMaBHdIie1tDg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Alt-Text: Concrete Lug Plate SmartPart - LCS 
Image-Analysis: The image provides a graphical representation of two structures with coordinates. On the left, there is a horizontal bar placed at the top with coordinates labeled (0,0,0). Beneath it, there is a vertical structure with the coordinates (0,0,-Offset1) and a circular element represented at the bottom. A red dot is used to indicate key points, including the top of the bar and the circular element. The right side displays a vertical bar, likely representing a different structure or view, but it lacks specific coordinates or additional context. The main relationship depicted involves how these two structures are aligned relative to their respective coordinates in a three-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qm3QeBIPv5V1fhgpcUcQKg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Qm3QeBIPv5V1fhgpcUcQKg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Plate Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776617?contentId=fX77zAMAXPyiQdGLUxb65g)
IJUAhsLength1::Length1

Specifies the length of the top plate.

IJUAhsWidth1::Width1

Specifies the width of the top plate.

IJUAhsThickness1::Thickness1

Specifies the thickness of the top plate.

Front View Right View


Image:[Alt-Text: Concrete Lug Plate - Top Plate - Length/Thickness 
Image-Analysis: The image illustrates a technical diagram displaying the dimensions of a rectangular object. The top part, marked as "Length1," indicates the horizontal measurement, while the vertical measurement, labeled "Thickness1," specifies the thickness of the object. The diagram emphasizes the proportions and relationships between the length and thickness, demonstrating how they relate to each other in the context of the object's structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ljmZBEEGIdR7rKUOjgMtsw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Top Plate - Length/Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ljmZBEEGIdR7rKUOjgMtsw-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Alt-Text: Concrete Lug Plate - Top Plate - Width 
Image-Analysis: The image depicts a simple diagram with a rectangular block at the top labeled "Width 1," and a vertical line extending downward, representing a T-shaped configuration. The rectangle signifies the width measurement, while the vertical line could represent a depth or height associated with this width. This type of illustration is often used in engineering or architectural contexts to convey dimensions and proportions in a clear manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l7kXwu10ayTuNiwh6wKFkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Top Plate - Width](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l7kXwu10ayTuNiwh6wKFkg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Lug Plate Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776856?contentId=9bg5BrKXCagYL2uLROGMGA)
IJUAhsWidth2::Width2

Specifies the width of the lug plate.

IJUAhsHeight2::Height2

Specifies the height of the lug plate.


Image:[Alt-Text: Concrete Lug Plate - Lug Plate - Width/Height 
Image-Analysis: The image depicts a simple geometric diagram that illustrates measurements for a rectangular shape. The rectangle is oriented vertically, and it includes labeled dimensions: "Height2" indicating the vertical measurement of the shape, and "Width2" indicating the horizontal measurement at the bottom. The top of the rectangle has a horizontal line that does not appear to have any dimensions annotated on it. This layout is typically used in design or construction to communicate size specifications clearly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6jqB2q9EAhmVVemH2Nbx4A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Lug Plate - Width/Height](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6jqB2q9EAhmVVemH2Nbx4A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the lug plate.


Image:[Alt-Text: Concrete Lug Plate - Lug Plate - Thickness2 
Image-Analysis: The image depicts a simplistic technical drawing of a shape resembling a T. At the bottom of the T structure, there is a vertical line serving as the stem, and the horizontal line at the top represents the crossbar. Alongside the vertical line, the term "Thickness2" is labeled, indicating that this is likely a designation for the thickness measurement of the vertical section of the T. The arrows pointing toward each side of the word 'Thickness2' suggest the measurement is meant to convey the width or thickness of that part of the structure. Overall, this image seems to be related to engineering or design specifications for a component or material. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3kUb8m5m3R44b1b~r2~Tgg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Lug Plate - Thickness2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3kUb8m5m3R44b1b~r2~Tgg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the vertical distance of the hole from the top plate to the center of the
hole.


Image:[Alt-Text: Concrete Lug Plate - Lug Plate - Offset1 
Image-Analysis: The image depicts a technical diagram showing two components: a rectangular bar and a circular base. The bar is positioned horizontally above the base, which includes a circular section. A red dot is indicated atop the horizontal bar, illustrating a point of interest or attachment. Additionally, there is a measurement labeled "Offset1", which signifies the vertical distance from a reference point to the top of the circular base. This type of diagram might be used in engineering or design to clarify spatial relationships and measurements between the components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jt~kAl3S0DgIFsybEjh2~g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Lug Plate - Offset1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jt~kAl3S0DgIFsybEjh2~g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHoleDiameter::HoleDiameter

Specifies the diameter of the hole in the lug plate.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape of Sides - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776864?contentId=CVHnWA4H~bE0spXGuYOVWQ)
You can use some of the plate shape attributes to assign optional shapes to the sides.
Since the bottom of the sides is attached to the base, the top left and the top right
shape settings are used.


Image:[Alt-Text: Concrete Lug Plate - Shape of Sides 
Image-Analysis: The image shows two cylindrical objects, possibly containers, with red indicators on both the top and bottom ends. There is an arrow connecting the two cylinders, indicating a movement or transition from the left cylinder (labeled "Top Left") to the right cylinder (labeled "Top Right"). This could represent a process of shifting contents or reordering elements from one position to another, highlighting the relationship between the two positions. The positioning of the red dots suggests specific points of focus or importance in this transition. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I_xRDygFD847upeQP2eprA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate - Shape of Sides](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I_xRDygFD847upeQP2eprA-_PVFQNoCl4XmjAxWO0f7XQ/content)

These properties specify the corner attributes for the side plates. These properties
are optional. You must enter these values when these various corner shapes of side
plates are needed.

Plate shape functions are used for the side plates for top left and top right shape
settings. Because the bottom of the sides are attached to the base, when you flip
the graphic over, the top is the edge farthest away from the base as shown in the
following example.

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

Shape Top Left


Image:[Image-Analysis: The image is a diagram showing the settings for adjusting the corners of a rectangular shape. It features two main elements: "CornerX settings" which is oriented horizontally, and "CornerY" which is oriented vertically. The shape has a yellow corner, indicating it can be adjusted in terms of its corner radius, affecting how rounded the corners are. There is also a small red dot indicating the anchor point of the shape, which likely represents its position or origin in a coordinate system. The direction arrows suggest that users can manipulate the settings horizontally and vertically to create desired corner effects on the shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4F2VDIIy4~VMnzjASBoMCg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4F2VDIIy4~VMnzjASBoMCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Shape Top Right


Image:[Image-Analysis: The image depicts a diagram illustrating the settings for CornerX and CornerY. It shows a rectangular shape representing an object with a circular feature and two colored indicators—one at the corner marked in yellow and another red at the base. The arrows indicate the measurement directions for CornerX (horizontal) and CornerY (vertical), suggesting these settings might adjust the positioning or shape attributes of the object. This diagram is likely used in a context related to graphical user interface design or design software. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y5F1~XMCx7ByVnq3532mPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y5F1~XMCx7ByVnq3532mPg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777028?contentId=JMa76ZZdx_ss3BViAJr9dg)
The following graphic illustrates the orientation of the port types and their sizes
for the concrete lug plate:


Image:[Alt-Text: Concrete Lug Plate SmartPart - Ports 
Image-Analysis: The image depicts two mechanical structures with coordinate systems. The left structure has a vertical part with X, Y, and Z axes indicated: the Z axis points up, the Y axis points right, and the X axis is seen in the circular cut-out, emphasizing a cylindrical shape in a vertical position. The right structure features a similar top part but with a point where only the Z axis is shown extending downwards. This likely represents a technical drawing focusing on coordinates for engineering or design purposes, illustrating how different axis alignments affect the structures in space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xgFydKYZ_cfK_BW8iWiY4g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Concrete Lug Plate SmartPart - Ports](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xgFydKYZ_cfK_BW8iWiY4g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port details and their orientation

Port1:Structure (0, 0, 0)


None:  The ports must have the same name and orientation as the port on the structural lug.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - Structure | N/A - use 0 | N/A - use 9999 | N/A - use 9999 |

Port2:Hole (0, 0, -Offset1)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1005 - Hole | HoleDiameter | 0 | HoleDiameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777032?contentId=IxILUZPkB1rM3f5R5Kj9rA)
The BOM description must use the part description.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Constant Spring - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328241?contentId=I_qJMbZO_V2q7gkhFmcXHg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HS\_S3DConstant.TypeA, HS\_S3DConstant.TypeB, HS\_S3DConstant.TypeC, HS\_S3DConstant.TypeD,
HS\_S3DConstant.TypeE, HS\_S3DConstant.TypeF, HS\_S3DConstant.TypeG, HS\_S3DConstant.TypeU.  
Part Name: Constant Spring  
Part Description: - Constant Spring SmartPart

Type A Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EXP52L3kagmKWxoDWT2HXA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=fed7151befe5ff1c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EXP52L3kagmKWxoDWT2HXA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type B Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0iy5oVF41fDdGUnh3Ui4XA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9c686fe4448f7456)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0iy5oVF41fDdGUnh3Ui4XA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type C Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJyd0G5GTZazx_1fm8CNZQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bcbbaff7daa43101)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJyd0G5GTZazx_1fm8CNZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VnNDCx8mnRD7WLAQinTtUw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8ca49a6ed182f7b4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VnNDCx8mnRD7WLAQinTtUw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YPvClGgu1i77pWjU7eLNtw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9ddaa913fe3b14a8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YPvClGgu1i77pWjU7eLNtw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Tse98YvU1gk2sHqvw~~yIQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=156a99077bb581d6)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Tse98YvU1gk2sHqvw~~yIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mk8Ujc71UBkKNzWfl2qp6g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a2142c778be3f61d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mk8Ujc71UBkKNzWfl2qp6g-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type U Spring

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~3~SzFzgenglElZ5wszQFQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4080a5e2b6e609ae)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~3~SzFzgenglElZ5wszQFQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ are already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place different types of sample constant spring SmartParts delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part
look for icon that looks like a plus sign combined with a tag: , and then select the design support.

In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Constant Supports > Constant Support – TypeA as shown below. Follow the same procedure to place other types of constant springs.


Image:[Image-Analysis: The image depicts a hierarchical file structure or a tree diagram related to "SmartParts". At the top level, there is a category called "SmartParts", which contains subcategories such as "S3D Standard", "Beam Attachments", "Clevises", and "Constant Supports". Under "Constant Supports", there are multiple specific types listed (Type A, Type B, Type C, Type D, Type E, Type F, Type G, Type U). This structure illustrates the organization of different support types within the broader category of constant supports, allowing for easy navigation and identification of various components. The layout suggests an emphasis on categorization and classification of items, likely for engineering or design purposes involving piping or structural supports. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XYbmSIvbUls~usBfAnROCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XYbmSIvbUls~usBfAnROCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red 
look for an icon that resembles a red prohibition or stop sign, typically used to indicate an important warning or refusal: .# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Part Info Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328256?contentId=18bZca9CNK7oAo2apJ7pgg)
IJUAhsSpringType::SpringType

Specifies the type of spring. Common types are: A, B, C, D, E, F, G and U.

IJUAhsSize::Size (Optional)

This value is only used by the Part Selection rule for choosing a constant spring
part. It is not included in the corresponding graphics.

IJUAhsFigureNumber::FigureNumber

Specifies the manufacturer figure number.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Reference Tables - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328257?contentId=y~5RKSRBnVPNeApSLv0i0w)
The constant spring SmartPart has several properties for dimensions and shapes. Each
property can be determined for a given size, travel, and load combination in one of
three ways;

* Size
* Total travel
* Load

Because of this, each property can be placed on one of three dimension tables. The
part class will then reference these tables to get the values for each property.

IJUAhsSizeTable::SizeTable

Enter the sheet name of the hanger service class used to store properties which are
strictly dependent on the size of the constant support.

IJUAhsTravelTable::TravelTable

Enter the sheet name of the hanger service class used to store properties, which are
dependent on total travel, or total travel and size of the constant support.

IJUAhsLoadTable::LoadTable

Enter the sheet name of the hanger service class used to store properties, which are
dependent on the load of the constant support.

IJUAhsSelectionTable::SelectionTable

Enter the sheet name of the hanger service class used to store the travel, size, and
load data used for part selection rule.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shape Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328261?contentId=6edN7Q6Fx84uVDHIP2VofQ)
Each spring type is made up of several shapes. Each shape has a property associated
with it where you can specify a shape name. The name must represent a row in a corresponding
shape table. The shapes available for each type are shown below.

Type A, B, and C

The type A, B, and C constants consist of the following shapes.


Image:[Image-Analysis: The image depicts a mechanical assembly involving several components, including three plates (Plate1, Plate2, and Plate3) and a LoadColumn. The assembly features a Casing that surrounds the plates. It indicates various components and their connections: the PivotPin connects FramePlate to the LeverPlate which is associated with the LoadPin. The configuration suggests a lever mechanism that may serve to lift or adjust loads positioned by the LoadColumn. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7u6nwXuFqzEJHtyRWTa1XQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7u6nwXuFqzEJHtyRWTa1XQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 1 - Vertical: Casing above Frame


Image:[Image-Analysis: The image depicts a mechanical assembly with several labeled components, likely illustrating a load-bearing system or mechanism. It includes a casing and multiple plates arranged vertically: Plate1 at the bottom, Plate2 above it, Plate3 at the top, and a FramePlate connecting the upper structure. Attached to this assembly is a LeverPlate, which pivots around the PivotPin, suggesting it acts as a lever to apply or regulate a load. The LoadColumn connects to a LoadPin, indicating where force is applied. This design may be used in machinery where balancing or distributing weight is necessary. The relationship among these components highlights their functionality in supporting and managing mechanical loads. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vhde_fQEOolkW8cxtl5dCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vhde_fQEOolkW8cxtl5dCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 2 - Vertical: Casing below Frame

In addition to the shapes shown above, the type A, B, and C constants have the top
shapes shown below. The type A constant has an optional nut top. The type B constant
has a single lug top. The type C constant has a double lug top.

Type A Top

The type A constant allows an optional nut shape for the top.


Image:[Image-Analysis: The image depicts two arrangements of nuts, which are fasteners used to secure bolts or screws. On the left, there is a single nut being placed onto a surface, indicated by an arrow showing downward movement. On the right, there are two nuts arranged in a more complex structure, suggesting that they might be connected or working together in some way, as shown by the lines that indicate their relationship. The label "Nut" is present above each arrangement to identify the components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yj_c_F0NJuG~b4KOQqbo6A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yj_c_F0NJuG~b4KOQqbo6A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 4 - Type A Nut Top Shape: Single and Double Suspension

Type B Top

The type B constant has a required lug plate shape, along with an optional pin shape.


Image:[Image-Analysis: The image illustrates a mechanical connection involving a pin and a lug. There are two diagrams shown side by side, each depicting a different configuration of the pin with respect to the lug. In the left diagram, a pin is positioned to be inserted into the lug, indicated by arrows showing the direction of insertion. In the right diagram, the positioning of the pin within the lug is shown with arrows depicting movement or adjustment of the pin to fit the lug. These representations are commonly used in mechanical designs to demonstrate how components fit together, either by insertion or alignment. The lug serves as a structural element to receive the pin, which may be used for fastening or pivoting components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SGg9XkahMzpTjbHWEljVeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SGg9XkahMzpTjbHWEljVeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 5 - Type B Single Lug Top: Single and Double Suspension

Type C Top

The type C constant has a required lug plate shape, along with an optional pin shape.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MuAhyy2rkaTIOavMHp0ZPQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=384e87929ba070ea)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MuAhyy2rkaTIOavMHp0ZPQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 6 - Type C Double Lug Top: Single and Double Suspension

Type C for Horizontal Case

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qnk7WddQguzk9hwQgyvE7g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6ddba7a3ee486a9f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qnk7WddQguzk9hwQgyvE7g-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Type C horizontal case, you can place a single lug and a double lug for double
suspension. If you specify only Lug2Shape, a single lug and a double lug are placed for double suspension. If you specify Gap2 and Offset6 values along with Lug2Shape, then two double lugs are placed for Type C double suspension.

Additional Top Connections

The type B and C constants allow for an additional top connection shape. This can
be a lug, WBA, clevis, or eye nut depending on the type. The additional top shapes
are specified on the StructAttachment attribute.

The type B allows the addition of a WBA or a clevis.


Image:[Image-Analysis: The image features two mechanical objects that appear to be the same type of device, possibly some sort of clamp or connector. They are positioned side by side. The device on the left seems to have a more complex structure with multiple parts, while the one on the right appears simpler or may have fewer moving parts. This suggests a comparison between two designs or versions of the same device, potentially showcasing an evolution in design or functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WED59GaclzRflvKbwMUIGQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WED59GaclzRflvKbwMUIGQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 7 - Type B Single Lug Top with Clevis or WBA Additional Top Connection

The type C allows the addition of a lug or an eye nut.


Image:[Image-Analysis: The image displays two sets of weightlifting equipment. On the left side, there are two vertical weight plates represented with lines, resembling the typical depiction of weights on a barbell, indicating a standard weightlifting setup. On the right side, there is a more complex weight arrangement with additional plates stacked. The design suggests these are tools for strength training, often used in gyms. The left represents a basic weight configuration, while the right suggests a more advanced or heavier setup for experienced lifters. This may indicate a progression from simpler to more complex weight exercises in strength training routines. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fHxomDnoQg6_KqAwJTiRfA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fHxomDnoQg6_KqAwJTiRfA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 8 - Type C Double Lug Top with Lug or Eye Nut Additional Top Connection

If Type C has single lug in Lug2Shape for double suspension, then you can place it with WBA and Clevis.

Type D and E

The type D and E constants consist of the same general shapes as the type A, B, and
C constants.

Type D

The type D constant includes optional ear plates when the spring is above the frame.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ex8h9yCPhkA~qVHMh8cOUg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2046333b5284e4f2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ex8h9yCPhkA~qVHMh8cOUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 9 - Type D Vertical: Casing above and below Frame


Image:[Image-Analysis: The image appears to illustrate a mechanical or structural component, likely part of a pivoting or sliding mechanism. The representation shows a rectangular block (possibly a container or a drawer) with a blue top surface, which suggests it can lift or be accessible from above. The dashed line indicates the movement of a lever or arm that may assist in opening or closing this block. The vertical component on the right could be a support rod or hinge, showing how this assembly is anchored or operates in relation to the surrounding structure. Overall, the image depicts a mechanical assembly designed for potential movement or access, likely in a furniture or machinery context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YZVmrbsMmTJYVG22AwVwBg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YZVmrbsMmTJYVG22AwVwBg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 10 - Type D Horizontal

Type E

The type E constant includes optional stiffener/gusset plates when the casing is below
the frame. It has an optional fourth plate when the casing is beside the frame.


Image:[Image-Analysis: The image shows two diagrams of a mechanical component, likely related to a structural support or pivot mechanism. The left diagram illustrates the component in a two-dimensional view with various parts, including what appears to be a vertical cylinder and connections, symbolized by dashed lines, possibly indicating movement or adjustment mechanisms. The right diagram focuses on a specific feature called a "Gusset Plate," which is highlighted in blue at the base of the cylindrical structure. Gusset plates are typically used to strengthen the joint connections between structural elements, providing stability and support. Overall, the connection between the two views helps visualize how the Gusset Plate integrates with the assembly to enhance structural integrity. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nn_~2_QIpzFmD~RyiRN4Ug-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nn_~2_QIpzFmD~RyiRN4Ug-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 11 - Type E Vertical: Casing above and below Frame


Image:[Image-Analysis: The image depicts a mechanical or structural diagram involving four plates. Plate3 is illustrated at the bottom in blue, indicating its role or function in the assembly. Above it, Plate4 is shown, likely representing another component that interfaces with Plate3. The diagram also includes an arrow suggesting movement or direction and a dashed line indicating a pivot or rotational mechanism related to Plate4. This design might be part of a lever mechanism or sliding system where the interaction between the plates is crucial for functionality. However, the image lacks detailed annotations for full clarity on the specific application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7HUXCWUPA7P6MqHTK8Uvgw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7HUXCWUPA7P6MqHTK8Uvgw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 12 - Type E Horizontal

Type F

The type F constant includes a second lever plate shape.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r1c9AjvrXD8jB1ZXrQi~bQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=070b90c3cfa26859)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r1c9AjvrXD8jB1ZXrQi~bQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 13 - Type F Vertical: Casing below and above Frame


Image:[Image-Analysis: The image depicts a mechanical assembly that includes multiple plates and levers. There are four plates labeled Plate1, Plate2, Plate3, and Plate4, arranged in a way that suggests they are part of a larger mechanism. The lever system consists of LeverPlate2 and another lever, which likely interact with the plates. This design may indicate a device where the levers can apply force to the plates, possibly allowing for movement or pressure application, indicative of a mechanical or engineering concept. The arrangement and labeling suggest a focus on how these parts interact in a functional assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j32_Vd4AQW1ZCxHW0GYSTg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j32_Vd4AQW1ZCxHW0GYSTg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 14 - Type F Horizontal: Casing beside Frame

Type U

The Type U constant are used to model up-thrust constant supports.


Image:[Image-Analysis: The image depicts a part labeled "UpThrustPlate," which seems to be a mechanical or engineering diagram. The UpThrustPlate is represented in a simplified manner, positioned near a larger rectangular component. There is an arrow pointing from the label to the UpThrustPlate, indicating its location or importance in the assembly. The image shows some alignment of structural elements such as a rectangle to the right that might be a casing or housing, and at the bottom, there is a blue rectangular base that suggests stability or support for the plate. Overall, the diagram provides a clear identification of the UpThrustPlate's position within a larger mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GZ_~CCm5T_IAaIfu_ECkVg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GZ_~CCm5T_IAaIfu_ECkVg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 15 - Type U Horizontal

Type G

The type G constant consists of two standard constant supports connected by a steel
section. The shape properties are identical to the A, B, and C constants with the
addition of a steel cross section as shown below.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mp88HtDH5UcE3~9ZDQdB4A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=384e69693e20dbb9)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mp88HtDH5UcE3~9ZDQdB4A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 16 - Type G# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Load Column - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328281?contentId=q1ePCqNC_HBo3rw~lzs1YQ)
IJUAhsIncLoadColumn::IncludeLoadColumn

Specifies whether or not to include the load column graphics. Acceptable values are
True and False.

See Also

[Included Load Column](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/sXSWSyZL88Ij55SafCNtkQ)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Included Load Column - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776427?contentId=fU3lWn35_gYltM0rLnmGgg)
You can customize the load column by specifying different combinations of shapes.
Currently, the following combinations are supported for the standard constants. In
the figure below, the clevis shape can be used to model a yoke.


Image:[Image-Analysis: The image displays a technical illustration of a column assembly, which includes four labeled components: ColumnPin, ColumnRod, ColumnNut, and ColumnEnd. The ColumnRod is the main vertical element depicted in the center, connected at the top by the ColumnPin, which secures the rod's position. At the bottom, the ColumnNut is shown, which likely fastens the assembly and provides stability, while the ColumnEnd is the terminus of the vertical rod. This schematic provides a clear representation of how these components interact in a structural application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wjmNEf4KddYSmEizOmz0sQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wjmNEf4KddYSmEizOmz0sQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 17 - Rod Coupling Load Column


Image:[Image-Analysis: The image displays a mechanical assembly consisting of four main components labeled as follows: 1) ColumnPin - located at the top of the assembly and typically used to connect or stabilize the structure; 2) ColumnRod - a long vertical component that serves as a central support or connector; 3) Turnbuckle - situated just above the ColumnNut, this part is used for adjusting tension or length in a cable or rod; and 4) ColumnNut - located at the bottom, this component is usually threaded onto the ColumnRod to secure it in place. Each part has a specific function within the assembly, contributing to its overall structural integrity and adjustability. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/906YhGNkVwx9ciV5P_UfmA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/906YhGNkVwx9ciV5P_UfmA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 18 - Load Column with Rod and Turnbuckle


Image:[Image-Analysis: The image is a labeled diagram depicting a mechanical assembly that includes several components: ColumnPin, ColumnClevis, ColumnRod, Turnbuckle, and ColumnNut. The ColumnPin is located at the top, which connects to the ColumnClevis. Below the ColumnClevis is the ColumnRod, a vertical component that likely provides structure or support. At the bottom of the diagram, there is a Turnbuckle, which is typically used to adjust tension or length, and beneath it, the ColumnNut is positioned to secure the assembly. This diagram illustrates the relationship and hierarchy between these components, showing how they fit and interact within a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4yYV_PHvg6u_t3Sf1MbxAw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4yYV_PHvg6u_t3Sf1MbxAw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 19 - Load Column with Clevis, Rod, and Turnbuckle

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r2cV0b8b6hI71U18e8MoEA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=810443a8b618d946)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r2cV0b8b6hI71U18e8MoEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 20 - Type F Load Column Shapes


Image:[Image-Analysis: The image depicts a labeled diagram of a component that includes a vertical rod with a circular top attachment. The label “TopAttachment” indicates the purpose of the curved section at the top, which likely functions as a connector or holder for another element. The vertical rod has visible screws or attachment points, suggesting that it is designed to be secured to a base or another structure. Overall, this component seems to be part of a larger assembly or device, possibly related to construction or mechanical systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tOzB9kmeR3Yw3S_XXEw3ng-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tOzB9kmeR3Yw3S_XXEw3ng-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 21 - Type F Load Column with Curved Plate Top Attachment# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Separate Load Column - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776433?contentId=bmpWsz0NT0iVU_sT02a7Ug)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DPArts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ConstantLoadColumn  
Part Name: Constant Load Column  
Part Description: Constant Load Column SmartPart

![separate load column](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y9XG0IGEr8LjjyJlpHpFBg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=09cabadd4e257918)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y9XG0IGEr8LjjyJlpHpFBg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ are already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Part Placement

To place a sample constant load column SmartPart delivered with the catalog:

1. Click Tasks > Hangers and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign combined with a tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Constant > Constant Load Column as shown below:

   
Image:[Alt-Text: constant load column_select for placement 
Image-Analysis: The image depicts a hierarchical structure, resembling a tree diagram, detailing various components under a category labeled "SmartParts." At the highest level, it includes a section named "S3D Standard," which contains a list of subcategories including "Beam Attachments," "Bolt," "Clevises," "Concrete Lug Plate," and "Constant Supports." The latter category, "Constant Supports," further branches into specific types labeled "Constant Support - Type A" through "Constant Support - Type U." Highlighted within this category is a specific component labeled "Constant Load Column," indicating its significance or current selection. This organization serves to categorize parts and components in a systematic manner, useful in assessing and locating specific items within an engineering or construction context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ICBFYsj~mrecC3CFbcsmWg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![constant load column_select for placement](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ICBFYsj~mrecC3CFbcsmWg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red 
look for an icon that resembles a red prohibition or stop sign, typically used to indicate an important warning or refusal: .

ProgID

HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ConstantLoadColumn

Example: S3Dhs\_CONST\_COL sheet in HS\_S3DParts.xls

Local Coordinate System


Image:[Alt-Text: separate load column_local coordinate system 
Image-Analysis: The image depicts a vertical bar or shaft, indicated by the long vertical line with red dots at certain positions. These red dots likely represent points of interest or reference marks along the bar. To the right of the bar, there are labeled arrows indicating the Y and Z axes of a coordinate system. The Y-axis is oriented vertically upwards, while the Z-axis is oriented horizontally to the right. This representation likely illustrates a 3D space where the vertical bar extends in the Y-direction while the Z-axis denotes lateral movement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UsOXlOhH7hS9flO4Q0ZQgw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![separate load column_local coordinate system](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UsOXlOhH7hS9flO4Q0ZQgw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Constant Part Properties

IJUAhsLoad::Load

Specifies the load of the load column. The load value must be greater than or equal
to zero. This value is required.

IJUAhsMovement::Movement

Specifies the movement of the load column. This value is required.

IJUAhsMovementDir::MovementDirection

Specifies the direction of movement for the load column. Accepted values are Up and Down. This property uses the codelist value defined in the hsSpringMovementDir sheet of the HS\_S3DParts\_Codelist.xls workbook.

Port Details

These properties specify the different port types and their sizes for the constant
load column.

![separate load column_port details](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lwXzy6lt0fsbO6nGa0gJQA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=19b73a196b77578e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lwXzy6lt0fsbO6nGa0gJQA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Alt-Text: separate load column_hole 1 
Image-Analysis: The image displays a mechanical or engineering diagram focusing on a specific rod or shaft component. It shows a vertical rectangular shape that is representative of the rod. There are labeled points indicating "Hole1" at the top, "RodEnd" at the bottom, and "Surface" near the bottom of the rod. This implies that there is a hole located at the upper part of the rod, while the rod end refers to the bottom part where it may connect to other components. To the right of the rod is a 3D coordinate axis system, with arrows indicating the Y and Z axes. The Y axis is vertical and points upwards, while the Z axis is horizontal pointing to the right. This coordinate system provides context for understanding the orientation and placement of the rod in a 3D space, which is crucial for any applications involving movement or assembly of mechanical parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CyMN7tIj1ich~SRmrD0kSA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![separate load column_hole 1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CyMN7tIj1ich~SRmrD0kSA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Hole 1 - Hole1

The hole ports are aligned so that they easily connect to the pipe. The X axis of
the route port is aligned along the length of the insulation, and the Z axis is pointing
in the downward direction.

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1009 - Double Lug | Use -1 | Use -9999 | Use 9999 |

Hole 2 - RodEnd

The rod end is aligned so that it easily connects to the pipe. The X axis of the route
port is aligned along the length of the insulation. The Z axis should point in the
downward direction.

| PortType | Size | MinSize | MaxSize |
| --- | --- | --- | --- |
| 1001 - External Thread, RH | Use -1 | Use -9999 | Use 9999 |

Top 1 - Surface

The surface is aligned so that it easily connects to the pipe. The X axis of the route
port should be aligned along the length of the insulation. The Z axis should point
in the downward direction.

| PortType | Size | MinSize | MaxSize |
| --- | --- | --- | --- |
| 1200 - Other | Use -1 | Use -9999 | Use 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dimension Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328295?contentId=Vrpb_sOj7Vb2dT4egea9qA)
Each spring type has a set of dimensions. Most are common to all spring types, while
others only apply to certain types. The supported dimensions for each spring type
are shown below.


None:  The ports are shown as 
look for an icon that resembles a red prohibition or stop sign, typically used to indicate an important warning or refusal: .

General Dimensions

The general dimensions shown below are common to the standard constant spring. They
are defined for all of the types.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XzXXgdKdpetNPKBFcs8yfg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f7ff3604662b27a8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XzXXgdKdpetNPKBFcs8yfg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 22 - General Dimensions: Vertical Orientation with Casing above Frame

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bNY_QYsZl7oyHDv_zncIbw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b8a53bba4eff90f2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bNY_QYsZl7oyHDv_zncIbw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 23 - General Dimensions: Vertical Orientation with Casing below Frame

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rZm_pdCD1_rpuRuZzAC2jg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ab5e30dcae1ebadb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rZm_pdCD1_rpuRuZzAC2jg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 24 - General Dimensions: Horizontal Orientation

The FramePlate, LeverPlate, GussetPlate, ColumnPlate, and UpThrustPlate each have a spacing attribute that specifies the spacing between the two plates.

Alternate Top Dimensions

The following figure depicts how the common set of dimensions defining the tops is
interpreted for each type.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8MJKBdIZ2XdUVoqrrKM5pQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=29bf9bb2ba4a71a1)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8MJKBdIZ2XdUVoqrrKM5pQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

For Type C constant, if you do not specify Gap2 for a given Lug2Shape, then a single lug is placed for double suspension.

Additional Top Connection Ports

Type A, B, and C constants have an additional Top port. For type A, this port is at the top of the nut or the top surface. For type
B and C, this port location based on the additional top connection shape as shown
below.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IXbjdF8PV9O2AxvNHiQrUg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=852bc62073b6fbf9)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IXbjdF8PV9O2AxvNHiQrUg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Load Column Dimensions - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328303?contentId=c1lU3107BMqY8Kzky3Pn5g)
The following figures show how the load column dimensions are interpreted:

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RySEOP7S8rF9r0n0tyShQw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e64b42d383018c05)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RySEOP7S8rF9r0n0tyShQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 25 - Standard Load Column Dimensions

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nQmAIce9UwsJJK_CuFFJ9Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=aac39f91572a1e4e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nQmAIce9UwsJJK_CuFFJ9Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 26 - Type F Load Column Dimensions# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Type G Dimensions - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328305?contentId=SFu5Bu7xBL0Rhduv~bN3Pg)
The following figure shows additional dimensions for a type G constant.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wq7JIHQTSWsbDjjsombzvQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=956478adfe1b60cb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wq7JIHQTSWsbDjjsombzvQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 27 - Additional Dimensions for the Type G Constant: Vertical Casing below Frame

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/es5HKc4_Z0nBa8zeWqcpzQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6b40d5eeb59779a3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/es5HKc4_Z0nBa8zeWqcpzQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Figure 28 - Type G Constant: Vertical Casing above Frame# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Properties Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328307?contentId=NDNoxrgIIT2AyN9Jz3rmoQ)
The properties associated with the constant spring SmartPart exist on several different
sheets. The main part class contains all the occurrence properties and general data.
Dimensions and other properties that depend on size, total travel, or load are located
on the corresponding sheets such as \_Size, \_Travel and 
\_Load.

IJUAhsShoeHeight::ShoeHeight

Specifies the height of the shoe. This property can be used by type F and G springs
to control the location of the route port.

IJOAhsPipeOD::PipeOD

Specifies the pipe outer diameter. This property can be used by the type F and G springs
to control the location of the route port.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Configuration Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328308?contentId=M19XBAX~yJzAUKVh6KrQxg)
IJUAhsConstantConfig::ConstantConfig

Specifies the orientation of the constant support along with the spring casing location
with respect to the frame. It uses codelist value defined in the hsConstantOrientation sheet of the HS\_S3DParts\_Codelist.xls workbook.

Acceptable codelist values are as follows:


Image:[Image-Analysis: The image displays three technical illustrations of different types of casings in relation to a frame. Each illustration is labeled with a specific description: 1) "Vertical Casing above Frame," which indicates that the casing is positioned above the frame; 2) "Vertical Casing below Frame," suggesting that the casing is placed directly underneath the frame; and 3) "Horizontal Casing beside Frame," showing that the casing is oriented horizontally adjacent to the frame. This visual representation helps in understanding the placement and orientation of the casings in relation to the frame structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hMPZ2QlDrH8ca3l6sAj3JQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hMPZ2QlDrH8ca3l6sAj3JQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsSuspensionType::SuspensionType

Specifies whether the constant has single or double suspension. It uses the codelist
value defined in the hsConstantSuspension sheet of the HS\_S3DParts\_Codelist.xls workbook.

Acceptable codelist values are as follows:


Image:[Image-Analysis: The image illustrates two types of suspension systems commonly used in various engineering applications. The first section labeled "1 – Single Suspension" shows a simple setup where a single point of suspension holds a load above a surface. In contrast, the second section labeled "2 – Double Suspension" depicts a more complex arrangement with two points of suspension, which allows for greater stability and distribution of weight. These depictions can be useful in understanding the mechanics behind how different suspension systems operate and their applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jabnBukNVPG6iIMTVNaI7g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jabnBukNVPG6iIMTVNaI7g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTopAlignment::TopAlignment

Specifies the alignment of top attachments. It uses codelist values defined in the
hsConstantAlignment sheet of the HS\_S3DParts\_Codelist.xls workbook.

Acceptable codelist values are as follows:


Image:[Image-Analysis: The image shows two geometric relationships, labeled "1 - Perpendicular" and "2 - Parallel." The left side depicts the concept of perpendicular lines: one line intersects another at a right angle, represented by the cross sign indicating the intersection. The right side illustrates parallel lines, which run alongside each other and never intersect, as shown by a vertical line relative to a horizontal line. This highlights the differences in their orientations and relationships in geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QzHU~wpp7IvJxY12m2j7Zg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QzHU~wpp7IvJxY12m2j7Zg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Input Data - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328312?contentId=iRToa6Wgz9jYuMfyvCRQmw)
IJUAhsCC::CC

Specifies the distance between the centerlines of the rods connected to a type G spring.


Image:[Image-Analysis: The image depicts a technical diagram or schematic showing a structural arrangement involving two upright supports or columns on either side. The supports are connected by a horizontal element, which may indicate a beam. There is a measurement indicated as "CC" which likely stands for "center to center," referring to the distance between the centers of the two supports. The diagonal dashed lines suggest that there may be some form of connection or bracing between the supports. This type of diagram is often used in engineering or architectural contexts to illustrate load-bearing structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bSEUMzCbP_IGuXAtcbRVoQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bSEUMzCbP_IGuXAtcbRVoQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLoad::Load

Specifies the actual load supported by the constant support.

IJUAhsMovement::Movement

Specifies the amount of thermal displacement of the pipe when moving from the installed
(cold) to operating (hot) conditions.

IJUAhsMovementDir::MovementDirection

Specifies the direction of the displacement when moving from the installed to operating
conditions. It uses codelist value defined in the hsSpringMovementDir sheet of the HS\_S3DParts\_Codelist.xls workbook.

IJUAhsTTIncrement::TTIncrement

Specifies the increments between total travels. For example, if total travel goes
up in ½ inch increments, set this value to 0.5.

IJUAhsTTIncrementByRule::TTIncrementByRule

Specifies the rule that the software uses to get the total travel increment value.
The total travel increment value from the TTIncrementByRule overrides TTIncrement value.

IJUAhsTTUnitType::TTUnitType

Specifies the units of the total travel.

IJUAhsValidTravels::ValidTravelList

Specifies the name of a codelist table that lists all the valid total travel values
for the constant support. If you specify a codelist table, then the software selects
the total travel value from the list instead of using TTIncrement. Use this for vendors with Total Travel values that do not increase by a consistent
value.


None:  Store the total travel as a numeric value in the ShortDescription column of the codelist table.

IJUAhsOverTravelMin::OverTravelMin

Specifies the minimal amount that the total travel must exceed the movement/actual
travel.

IJUAhsOverTravelPercent::OverTravelPercent

Specifies the percentage amount that the total travel should be greater than the movement.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Output Data - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328314?contentId=4DLPnZWfa8G~8VMdS8tWqg)
The following properties are outputs and should be left as blank on the part XLS sheet.
These properties are calculated and set by the SmartPart symbol code.

IJUAhsRodTakeOut::RodTakeOut

Specifies rod take out at the installed position.

IJUAhsTotalTravel::TotalTravel

Specifies the required total travel for the given movement.

This is calculated by taking the maximum of the following two values:

Movement + OverTravelMin

OR

Movement(1 + OverTravelPercent)

IJUAhsRodDiameter::RodDiameter

Specifies the diameter of the rod. RodDiameter value is determined based on size, total travel, or load from the Dimension Reference
tables.

IJUAhsHoleDiameter::HoleDiameter

Specifies the diameter of the hole. HoleDiameter value is determined based on size, total travel, or load from the Dimension Reference
tables.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Reference Dimension Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328321?contentId=Y1VJ5YIn4KFCw9xQjSTVpg)
The following properties are selection properties, which are useful to get the correct
data about the current size, total travel, and load for the main part.

IJUAhsMinSize::MinSize

Specifies the minimum size to which the property values in this row apply.

IJUAhsMaxSize::MaxSize

Specifies the maximum size to which the property values in this row apply. The size
properties must be included on all three reference tables. For example, if the Min Size = 1, Max Size = 4, and the current Size = 3, then the property values will be selected from this row.

IJUAhsMinTT::MinTT

Specifies the minimum travel to which these property values in this row apply.

IJUAhsMaxTT::MaxTT

Specifies the maximum travel to which these property values in this row apply. The
TT properties must be included on the Travel Reference table. For example, if the
MinTT = 1, MaxTT = 4, and the current TT = 3.5, then the values will be selected from this row.

IJUAhsTTUnitType::TTUnitType

Specifies the units of the total travel.

IJUAhsMinLoad::MinLoad

Specifies the minimum load to which these property values in this row apply.

IJUAhsMaxLoad::MaxLoad

Specifies the maximum load to which these property values in this row apply. The load
properties must be included on the Load Reference table. For example, if the MinLoad = 0lbs, MaxLoad = 800lbs and the current Load = 750 lbs, then the values will be selected from this row.

IJUAhsRodDiameter::RodDiameter

Specifies the required rod diameter for the given size, total travel, or load.


None: 

IJUAhsHoleDiameter::HoleDiameter

Specifies the required hole diameter for the given size, total travel, or load.


None: 

IJUAhsLugHoleOffset::LugHoleOffset

Specifies the offset for the hole centerline from the edge of the lug. If it is set
to zero or negative, the hole is centered on the lug.


None: 

IJUAhsGap1::Gap1

Specifies the required spacing between the double lugs of a type C constant.


None: 

IJUAhsGap2::Gap2

Specifies the required spacing between the double lugs of a type C constant for Lug
2 Shape.


Image:[Image-Analysis: The image illustrates a technical setup with two gaps labeled as "Gap 2" located between two vertical elements or stakes. The drawing appears to emphasize measurements, showing the distance between these entities, likely for engineering or construction purposes. There are two vertical lines (possibly representing rods or framework) on either side of Gap 2, indicating that this structure may be part of a larger construction or mechanical system. The central base appears to have a series of horizontal lines, possibly indicating a stable foundation. Overall, the diagram highlights a specific distance measurement between structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GSvu62W0WPWNGdDsV~GXpw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GSvu62W0WPWNGdDsV~GXpw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength::Length

Specifies the total length of the frame and casing. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset1::Offset1

Specifies the offset from the top connection port to the surface. For more information,
see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset2::Offset2

Specifies the offset of the port from the surface of the load column. For more information,
see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset3::Offset3

Specifies the offset from the edge of the load column to the center of the load column’s
pivot pin. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset4::Offset4

Specifies the offset from the edge of the lever arm to the pivot pin. For more information,
see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset5::Offset5

Specifies the offset from the edge of the cross section of the column pin for Type
G constant. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsOffset6::Offset6

Specifies the offset from the top connection port to the surface. Offset6 is used only when lug2 shape is provided for Type C constant. For more information,
see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsLength2::Length2

Specifies the length of the lever arm. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsPlate1Offset::Plate1Offset

Specifies the position of Plate1. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsPlate2Offset::Plate2Offset

Specifies the position of Plate2. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsPlate3Offset::Plate3Offset

Specifies the position of Plate3. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsPlate4Offset::Plate4Offset

Specifies the position of Plate4. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsFrameOffset::FrameOffset

Specifies the offset of the frame from the casing. For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsCaseCLOffset::CaseCLOffset

Specifies the offset from the main pivot pin to the center line of the spring casing.
For more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsTopOffset::TopOffset

Specifies the offset from the main pivot pin to the top connection port. For more
information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsPivotOffset::PivotOffset

Specifies the offset from the pivot to the edge of the frame. For more information,
see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsTopSpacing::TopSpacing

Specifies the distance between the two top connection ports if the constant is double
suspension. If the constant is single suspension, then this value is ignored. For
more information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsFrameSpacing::FrameSpacing

Specifies the distance between the two frame plates. If this value is zero or negative,
then only one plate is modeled.

IJUAhsLeverSpacing::LeverSpacing

Specifies the distance between the two lever plates. If this value is zero or negative,
then only one plate is modeled.

IJUAhsLever2Offset::Lever2Offset

Specifies the vertical distance between the pins of the first and second levers in
a type F constant.

IJUAhsGussetSpacing::GussetSpacing

Specifies the distance between the two gusset plates. If this value is zero or negative,
then only one plate is modeled.

IJUAhsColumnSpacing::ColumnSpacing

Specifies the distance between the two column plates. If this value is zero or negative,
then only one plate is modeled.

IJUAhsCCMin::CCMin

Specifies the minimum rod center to center distance for a type G constant.

IJUAhsCCMax::CCMax

Specifies the maximum rod center to center distance for a type G constant.

IJUAhsAngleHigh::AngleHigh

Specifies the angle of the lever arm from horizontal in the high position. For more
information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsAngleLow::AngleLow

Specifies the angle of the lever arm from horizontal in the low position. For more
information, see [Dimension Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/AW3kq1nYUxjr_r1hEEQC3g).

IJUAhsRodTakeOutHigh::RodTakeOutHigh

Specifies the rod take-out in the high position.

IJUAhsRodTakeOutLow::RodTakeOutLow

Specifies the rod take-out in the low position.

IJUAhsPlate1Shape::Plate1Shape

pecifies the name of a plate shape used to model Plate1. For more information, see
[Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsPlate2Shape::Plate2Shape

Specifies the name of a plate shape used to model Plate2. For more information, see
[Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsPlate3Shape::Plate3Shape

Specifies the name of a plate shape used to model Plate3. For more information, see
[Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsPlate4Shape::Plate4Shape

Specifies the name of a plate shape used to model Plate4. For more information, see
[Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsCasingShape::CasingShape

Specifies the name of a generic shape used to model the spring casing. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsFrameShape::FrameShape

Specifies the name of a plate shape used to model the frame. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsEarShape::EarShape

Specifies the name of a plate shape used to model the ears on a type D constant. For
more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsGussetShape::GussetShape

Specifies the name of a plate shape used to model the gusset plates. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsLeverShape::LeverShape

Specifies the name of a plate shape used to model the lever plates. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsLever2Shape::Lever2Shape

Specifies the name of a plate shape used to model the second lever in a type F constant.
For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsUpThrustShape::UpThrustShape

Specifies the name of a plate shape used to model the up-thrust plates on a type U
constant. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsPivotPinShape::PivotPinShape

Specifies the name of a pin shape used to model the main pivot pin. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsColumnPinShape::ColumnPinShape

Specifies the name of a pin shape used to model the load column pin. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsColumnShape::ColumnShape

Specifies the name of a rod shape used to model the load column. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsColumnEndShape::ColumnEndShape

Specifies the name of a nut shape used to model the end of the load column. For more
information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsColumnNutShape::ColumnNutShape

Specifies the name of a nut shape used to model the nut at the bottom of the load
column. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsClevisShape::ClevisShape

Specifies the name of a clevis shape used to model a clevis or yoke at the top of
the load column. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsTurnbuckleShape::TurnbuckleShape

String specifying the name of a turnbuckle shape used to model a turnbuckle or coupling
at the bottom of the load column rod. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsColumnPlateShape::ColumnPlateShape

String specifying the name of a plate shape used to model the load column. For more
information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsTopAttachment::TopAttachment

Specifies the top of the type F load column. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsNutShape::NutShape

Specifies a nut to be used with the type A constant. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsLugShape::LugShape

Specifies the lug used with a type B or C constant. For more information, see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsLug2Shape::Lug2Shape

Specifies the lug used with a Type C Constant. Lug2Shape is used only when a single lug is required for Type C constant. For more information,
see [Plate](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/o_vq3Q6dVScXQ1w0gTpIGg).

IJUAhsPinShape::PinShape

Specifies a pin used with the lug2 shape of a type C constant. For more information,
see [Pin](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/0t9priCNcP7eu3zcO~~tIA).

IJUAhsPin2Shape::Pin2Shape

Specifies a pin used with the lug shape of type B or C constant. For more information,
see [Shape Details](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/NfX9cO4O1AfTP0e1ikwmFQ).

IJUAhsStructAttachment::StructAttachment

Specifies an optional structural attachment, such as a WBA or lug, which connects
to the pin of a type B or C constant.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Local Coordinate System and Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328387?contentId=Q6C28TjoAEw1IAlXqZsIZA)
Type A, B, & C

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZQuyjmDv5_K86w1eWDD7DA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=40ec4833c6dc118a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZQuyjmDv5_K86w1eWDD7DA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type D

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dmy7ehTYRcRqgfmatKy4ug-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ed264c33f94cc453)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dmy7ehTYRcRqgfmatKy4ug-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type E

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Uxv1mXUSOxq20ymSQdBwZw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e3fc3b32d7900547)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Uxv1mXUSOxq20ymSQdBwZw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type F

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GXH6IlEPJb98RJ1EVZerYw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=70965cb8b0bc248d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GXH6IlEPJb98RJ1EVZerYw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QSivmIV8qlHBysMn0XOh0w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=41b6015c55651648)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QSivmIV8qlHBysMn0XOh0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Type G


Image:[Image-Analysis: The image illustrates a mechanical system involving two surfaces positioned on the left and right. Each surface is connected to a component labeled "RodEnd," which suggests a linkage or joint in the system. A vertical central line indicates the "Z" axis representing the vertical dimension, and a horizontal line labeled "Route" connects the two surfaces at a midway point. Below the "Route," there is a component labeled "Steel," likely indicating the material or structural component that binds or supports the system. Overall, this can represent a mechanism or assembly where motion or connection between the surfaces and RodEnds is crucial, typically found in mechanical engineering contexts such as robotics or machinery. The design suggests a focus on joint functionality and material selection. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y_rJLyqtyrQU1FSY65Gn4g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Y_rJLyqtyrQU1FSY65Gn4g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328400?contentId=vH4NG~Mk7qqtDlYA8vv1gw)
RodEnd Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001 – Internal Thread RH OR 1003 – Internal Thread LH | Rod Diameter | Minimum Rod Diameter | Maximum Rod Diameter |

Surface Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 - Other | Use -1 | Use -9999 | Use 9999 |

Top Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| Depends on the top type. | Depends on the top type. | Depends on the top type. | Depends on the top type. |

Hole Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 - Eye OR 1008 - Single Lug OR 1009 - Double Lug | Hole Diameter | 0 | Maximum Hole Diameter |

Structure Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 3 - Structure | Use -1 | Use -9999 | Use 9999 |

Route Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 - Route | Pipe OD | Minimum Pipe OD | Maximum Pipe OD |

Steel Ports

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 - Steel | Use -1 | Use -9999 | Use 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/328409?contentId=ULTS65MXBA8Li_4ciWe3eQ)
The standard delivered BOM description function provides the BOM description in the
following format:

+  +  +  +  +
 +

The Part Description should include any additional information required for ordering
purposes, including spring type, size, figure/travel series, and so on.

Units can be set by rules on the HgrBOMRules sheet in the HS\_System.xls workbook. These rules set the units, precision type, and precision.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Dummy Leg - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361766?contentId=YIvOJsErBlP69kZLe2HZWA)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.DummyLeg  
Part Name: Dummy Legs  
Part Description: Dummy Leg SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wlrywdxdeodSrW9869DmEg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=aa891339f849abec)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wlrywdxdeodSrW9869DmEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kxwebMzkenWTcEp3jDBsw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e3f6f6ad4de2e68c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0kxwebMzkenWTcEp3jDBsw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample Dummy Leg SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Dummy Legs as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical structure, likely representing a file or component organization within a parts management system. At the top level, there are several categories, including "Parts," "SmartParts," and "S3D Standard." Under "S3D Standard," there are various subcategories such as "Beam Attachments" and "Clevises." Within the "Dummy Legs" section, components are further organized, showing specific parts like "Dummy Leg," "Stanchion," "Variable DummyLeg," and "Variable Stanchion." This layout illustrates a classification system where each category can contain multiple subcategories or components, indicating a nested relationship among the parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LVdLlW7TpaGrq0D3AJSBiQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LVdLlW7TpaGrq0D3AJSBiQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image contains two diagrams that illustrate concepts related to mechanical systems or structures. The left diagram depicts a spooled element attached to a vertical shaft, and it seems to indicate some form of rotational or lateral movement involving axes (marked as Z and V). The right diagram shows a different type of element, possibly a cylindrical shape attached to a vertical column, with axes labeled as Z (vertical) and X (horizontal). The diagrams likely represent how different forces or motions interact with the specified axes in mechanical applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XK9w1GZNuyzdvU9wMMXftg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XK9w1GZNuyzdvU9wMMXftg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Dummy Leg Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361767?contentId=9VVlRpvu3qApFLopJ83ncQ)
IJUAhsBotShape::BotShape

Specifies the dummy leg/stanchion shape to use.

IJUAhsTopShape::TopShape

Specifies the dummy leg/ stanchion to use. TopShape is optional.

IJUAhsLength::Length or IJOAHgrOccLength::Length

Specifies the total height of the dummy leg from the pipe centerline to the bottom
of the centerline including all the plates. Length must be positive and greater than half the Diameter1. If length is not specified for IJOAHgrOccLength::Length, then the part is of variable length.


Image:[Image-Analysis: The image depicts a mechanical system often used to illustrate concepts in physics, specifically related to motion and forces. It shows two vertical rods, with the one on the right having an upward arrow indicating a force (possibly tension or lift). Above the right rod, there is an arc that represents a circular motion, hinting that the system might be describing a pendulum or rotational motion. The left rod appears to be stationary or fixed at the bottom, while the right rod seems to be moveable, suggesting a point of rotation at the top where the arc starts. The red elements likely signify points of interest such as forces or position markers, emphasizing the action or direction of motion in the system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ht7k0f4xNoINBXAUo9bIjQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ht7k0f4xNoINBXAUo9bIjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsDiameter1::Diameter1

Specifies the diameter of the pipe. Diameter1 is optional but must be greater than zero.


Image:[Image-Analysis: The image depicts a simple mechanical system that appears to show the concept of a pendulum. The pendulum consists of a circular motion represented by a dashed circular path, with a point at the top depicting the pivot or fixed point. Below the pivot, there is a vertical line that represents the rod of the pendulum. There are arrows pointing downward which might indicate the direction of gravitational force acting on the pendulum. Additionally, there is a red dot highlighted on the pendulum, which could represent the mass or bob of the pendulum, important for understanding its motion. Overall, the image illustrates the basic elements and forces at play in a pendulum system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OaEsOxsV57eQ7dOgvy1BRw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OaEsOxsV57eQ7dOgvy1BRw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsElbow::ElbowRadius

Specifies the radius of the elbow. ElbowRadius is optional and must be greater than zero. If you do not specify this parameter,
the dummy leg is made for a straight pipe.


Image:[Image-Analysis: The image appears to be a technical or architectural drawing illustrating a structure that resembles a pillar or column. It has an ark-shaped top that may represent a semi-circular or rounded top, commonly used in classical architecture. Connecting arrows indicate the direction of flow, potentially suggesting measurement or dimensions of the structure. The red dots may indicate points of interest or measurement markers on the pillar design. The structure seems to have a base and could be indicative of columns supporting a larger structure or roof above. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Os~NS1bXUPF9pqEKs7rdkQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Os~NS1bXUPF9pqEKs7rdkQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsElbow::FaceToCenter

Specifies the face to center distance of the elbow. For a short tangent elbow, FaceToCenter is same as ElbowRadius. FaceToCenter is optional but and must be greater than zero. If you dot specify this parameter,
the dummy leg is made for a straight pipe.


Image:[Image-Analysis: The image depicts a schematic or technical drawing of a mechanical component, likely a part of a machine or structure. It shows a curved outline on the left, possibly representing a cross-section of a larger object. The red dots indicate specific points of interest that may represent measurement points or features within this design. The vertical and horizontal lines suggest dimensions, with arrows pointing to various parts indicating height and connection points. This type of drawing is typically used in engineering and design to convey complex information in a simplified visual format, allowing for better understanding and communication of specifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUJvi1b9HD90NQ4756QXfw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NUJvi1b9HD90NQ4756QXfw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsOffset1::Offset1

Specifies the offset from the pipe centerline to the dummy leg centerline. Offset1 is required and can be either positive or negative. If you do not specify this parameter,
the software uses zero as the default offset. Offset1 is only applicable for elbows.


Image:[Image-Analysis: The image depicts a technical diagram likely related to a component or system. It shows a specific shape, probably a half-cylinder or a curved feature, indicated by the curved line on the left. To the right, there is a vertical line signifying a pillar or support. At the top, there are directional arrows, which suggest movement or flow, possibly indicating the direction of forces or materials. A box at the bottom represents a base or foundation, which is integral to the overall structure. The red dots may depict points of interest or connection points within the structure. This image appears to illustrate a structural element, focusing on its dimensions and interaction with other components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_toRoEUKrSKifprKGx1AAA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_toRoEUKrSKifprKGx1AAA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRepadShape::RepadShape

The repad shape has not been implemented for the Dummy Leg SmartPart. This property
can be ignored. If you require a repad for your dummy support, you will need to add
it as a separate part in your standard support. See [Reinforcement Pad (Repad)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/fpsH62yxyg1wszzMLuiRug) for details on how to create a new repad part.


Image:[Image-Analysis: The image depicts a simple representation of an electrical circuit component known as a capacitor. The circular shape at the top represents the positive terminal of the capacitor, while the line extending downwards indicates the lead that connects to the circuit. The dashed lines around the circle may symbolize the electric field generated by the capacitor when it stores energy. The component is connected downward with another line which might suggest its integration into a larger circuit. The red square inside the circular part could indicate a specific voltage rating or value associated with the capacitor, but details on this are not provided in the image. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/waQGsRLXdUQlS2pkQqo2Sg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/waQGsRLXdUQlS2pkQqo2Sg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStanchion::IsStanchion

Specifies whether the part is a stanchion. If IsStanhcion is set to Yes - 1, then both the bottom and top shapes are stanchion shapes. If IsStanhcion is set to No - 2, then one of the shapes is a dummy leg. If the part has bottom and top shapes, the
top should be a dummy leg shape. If the part has only a bottom shape, then the bottom
shape should be a dummy leg shape.


Image:[Image-Analysis: The image presents two engineering concepts labeled "Stanchion" and "Dummy Leg." Each concept includes a simplified diagram that visually represents its structure. The "Stanchion" is depicted with a vertical post featuring a dashed circular shape above it, possibly indicating a support structure, with a red point suggesting a key joint or connection. Conversely, the "Dummy Leg" also has a vertical component, but it emphasizes a length adjustment or connection represented by arrows, illustrating its operational flexibility or motion range. The use of red points in both diagrams likely signifies important connection points or load points, indicating their functional aspects in structural applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rsZe7B74mIikORSyRZyQ~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rsZe7B74mIikORSyRZyQ~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset2::Offset2

Specifies the offset with which the top shape and the bottom shape overlap each other.
Offset2 must be greater than or equal to zero. If Offset2 is zero, then the two shapes are butted to each other. If Plate1Shape or Plate2Shape are specified, then Offset2 is ignored. The dummy legs butt up against the plates.


Image:[Image-Analysis: The image depicts a simple electrical circuit with a capacitor and a switch. The circuit includes a power source represented at the bottom, with a red square symbol indicating the positive terminal. The circuit leads to a capacitor denoted by a rectangular shape, which is connected to a switch. Above the switch, there is a representation of an electric field or oscillation, indicated by the dashed circular lines. This suggests that the circuit can generate oscillating electric fields, which are often associated with resonant circuits or Tesla coils. The bottom part of the image has two vertical arrows pointing downward, possibly indicating the flow of current or the direction of force related to the electric field. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_usyLEqLx_h1G7kyvCeebQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_usyLEqLx_h1G7kyvCeebQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStanGap::StanGap

Specifies the distance between the bottom of the pipe and the top of the stanchion
shape or load plate. StanGap must be greater than or equal to zero. StanGap is used only when IsStanchion is set to Yes.


Image:[Image-Analysis: The image depicts a mechanical or engineering concept involving a pulley system. At the top, there is a circular motion indicated by dashed lines, suggesting movement around a central point. Below this circular mechanism is a vertical line representing a vertical component of the system, possibly a rope. The two arrows pointing downwards indicate the direction of force or motion, possibly referring to the load being lowered. The rectangular shape at the bottom could signify the base or ground support of the entire system, and the small red dots may represent the positions of forces or connection points within the mechanism. Overall, this image illustrates how different components of a pulley system interact and the directional nature of the applied forces. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ebHN7eBrGqNHuaXhuJw4jw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ebHN7eBrGqNHuaXhuJw4jw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMinLen::MinLen

Specifies the minimum length of the dummy leg. If MinLen is not specified, then a default value of -9999 can be used.

IJUAhsMaxLen::MaxLen

Specifies the maximum length of the dummy leg. If MaxLen is not specified, then a default value of 9999 can be used.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details (Dummy Leg) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/361780?contentId=eUFq_GItxqIDj~lCdCcUjQ)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TP32lnvsxi08uaZnWkY1eQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5ca87bb7e6bd0c6c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TP32lnvsxi08uaZnWkY1eQ-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image shows two mechanical structures: a Dummy Leg and a Stanchion. Each structure is represented in a schematic format with labeled parts and directional axes (x, y, z). The 'Dummy Leg' is shown above with a circular 'Route Port' on top, connected to a 'Steel Port' below, illustrating a vertical orientation with the z-axis pointing upwards and x and y axes in the horizontal plane. Below it, the 'Stanchion' structure is depicted with dual 'Route Ports' (top and connected to 'Surface Port') and a 'Steel Port' at the bottom, emphasizing a more complex design with multiple ports. Both designs indicate key structural components and their relationships, such as the orientation and connection of the ports, perhaps for fluid or structural support systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/68WQDshwG26k9Adn6kV0vA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/68WQDshwG26k9Adn6kV0vA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Route Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Steel Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 | -1 | -9999 | 9999 |

Additional port for Stanchion

Surface Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 | -1 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Insulation Aspect - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/722583?contentId=3hSd9MvxLShIWaXrQJBzmw)
To use the insulation aspect for dummy legs, you must define the following attributes
in the part worksheet:

IJOAhsCreateInsAspect::CreateInsulationAspect

Specifies a boolean value for the inspection aspect of the Dummy Leg.

IJOAhsInsulationTh::InsulationTh

Specifies the insulation thickness for the part.

IJUAhsPipeRunInsTh::PipeRunInsulationThickness

Specifies the insulation thickness for the pipe run.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Elbow Lug - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/353460?contentId=2SJ9tIiizFgtFgTVdmc0cQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ElbowLug  
Part Name: Elbow Lug  
Part Description: Elbow Lug SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Q_RcLIsg79iT9dWjelJLxQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=643f32e145d1c1ab)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Q_RcLIsg79iT9dWjelJLxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample Elbow Lug SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Elbow Lugs > Elbow Lug as shown below.

   
Image:[Image-Analysis: The image presents a hierarchical folder structure related to a project or system called "SmartParts." At the top level, there are two primary folders: "Bergen-Power NF09.3" and "S3D Standard." Under "S3D Standard," there are various subcategories related to engineering or mechanical components. These include "Beam Attachments," "Clevises," "Elbow Lugs," and several others such as "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Struts," and "U-Bolts." Notably, the "Elbow Lug" folder is highlighted, indicating it may be of particular importance or relevance within this structure. This layout suggests the organization of different parts or components used in a design or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/t4IYRLi5nRMxs21iUlovkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/t4IYRLi5nRMxs21iUlovkg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a geometric shape with a rounded top edge and a curved bottom edge, possibly representing a component or abstract shape in a technical drawing. There is a hollow circle towards the upper section, possibly indicating a hole or other feature. Below the shape, there is a red coordinate system depicted with arrows indicating the X and Z axes. The X axis extends horizontally to the right, while the Z axis extends vertically upwards. This coordinate system is likely used for referencing positions or dimensions related to the shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1GHYbuRGjX1CiXKEcemZWw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1GHYbuRGjX1CiXKEcemZWw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Elbow Lug Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/353461?contentId=CJHJWB08KuqxBDIuDroR3g)
IJUAhsRodDiameter::RodDiameter

Specifies the rod diameter that is used by the elbow lug. This property does not affect
the graphics and is used by the part selection rule.

IJOAhsPipeOD::PipeOD

Specifies the diameter of pipe that is used with the elbow lug.

IJOAhsElbow::ElbowRadius

Specifies the radius of the elbow where the part is placed.


Image:[Image-Analysis: The image appears to be a technical diagram illustrating a geometric concept related to angles and curves. It contains a right-angled shape in the top left corner with a circular arc that starts at the corner and curves around. There is a dashed red line outlining part of the circular arc, indicating a specific angular measurement. A blue arrow is drawn pointing toward an intersection point on the arc, suggesting the direction or the action of measuring the corresponding angle or radius. The overall composition indicates a relationship between the linear form represented by the right-angle corner and the curved form denoted by the arc, likely emphasizing the concept of angular measurement in geometry. The dashed and solid lines signify different elements or paths in the diagram, potentially distinguishing between theoretical and practical aspects of the construction or measurement process. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B26937qC3jxRt74wky6FUw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B26937qC3jxRt74wky6FUw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsElbow::FaceToCenter

Specifies the distance between the face of the elbow and the center. For a short tangent
elbow, face to center distance is same as the elbow radius.

Long Elbow


Image:[Image-Analysis: The image depicts a technical drawing of a pipe elbow with various annotations and dimensional lines. It features a 90-degree bend typically found in piping systems. The dotted lines indicate the outline of the elbow's profile and the center point where the bend occurs. There is a dimension indicated in blue, which likely represents the height or vertical measurement associated with the elbow. The red dashed line may depict the actual flow path through the elbow. Overall, the image illustrates the geometry and dimensions important for understanding the elbow fitting in engineering or plumbing contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SBNec8T_kUatM0jiFAOtFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SBNec8T_kUatM0jiFAOtFw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Short Elbow


Image:[Image-Analysis: The image appears to be a technical diagram, likely representing a specific component or mechanical part. It features a curved edge and a corner profile, with elements such as dashed lines indicating different aspects or dimensions related to the design. The blue arrows suggest a vertical measurement is being indicated, although the exact measurement is not shown. Additionally, the dashed red line may represent another measurement or contour that is important for the component's fabrication or assembly. Overall, this image seems to provide insights into the geometry of a part used in engineering or manufacturing contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Z_ONMDtYwibC5G~3I8gCbg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Z_ONMDtYwibC5G~3I8gCbg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::TopShape

Specifies the graphic shape used for the top of the lug.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XKnjMRu64fmNQkPFvGJwEQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7673fb375f09ae05)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XKnjMRu64fmNQkPFvGJwEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance between the horizontal pipe center line and the top lug port.


Image:[Image-Analysis: The image depicts a technical drawing or schematic representing a curvature or a bend in a material or mechanical component. It has a few notable elements: a curved section with a highlighted red dashed line that might indicate a specific path or area of interest, while the black bold lines represent solid outlines or areas of the component. There is an indication of a linear measurement shown by a blue vertical arrow which likely symbolizes a dimension that is significant, possibly the height or depth of the component. Additionally, dotted lines intersecting with the geometry may suggest a grid or reference points that are essential for understanding positional relationships in the design. Overall, the image is highly technical and likely used in engineering or design contexts to communicate specifications clearly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIbYuItN7BB~iLEJgz7gPw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TIbYuItN7BB~iLEJgz7gPw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle1::Angle1

Specifies the angle between the top curve start and end point. If the top shape is
not curved, then the software ignores this property. Angle1 must be positive, and
greater than 90 degrees and less than 270 degrees. Else, a warning message displays
and Angle1 is reset to 180 degrees. If no value is assigned, a default value of 180 degrees
is used.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y_ILnp5w2FKGOL~7_8~m8w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=08ad2072600c566f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y_ILnp5w2FKGOL~7_8~m8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the top width of the elbow lug. If Width1 is set to zero, then, Width2 is used. If Width2 is also set to zero, then PipeOD is used.


Image:[Image-Analysis: The image shows a technical drawing with two main sections. The top section features a circular arc and a horizontal line with arrows indicating measurement, suggesting that this part is concerned with the dimensions of a curve or rounding. The presence of a small circle above the arc likely indicates a dimension point, possibly for radius. The bottom section depicts a more complex shape with a rounded corner and a small circular detail, which might denote a hole or a specific feature. Both sections seem to represent different parts or views of a mechanical component or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mHL6JNGuAvGQArro4pdrcQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mHL6JNGuAvGQArro4pdrcQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the bottom width of the elbow lug. If this value is set to zero and Angle 3 is set to zero, then Width1 is used instead of Width2. If both the width values are set to zero, then PipeOD is used. If the left tapered portion does not intersect with the elbow, then the
lug extends down along the pipe per Angle4. The bottom of the lug is drawn back to the pipe in line with the center of the radius
of the turn with an angle of Angle4.


Image:[Image-Analysis: The image depicts two different views of a shaped object, possibly a manufacturing or design component. The top view shows a curved edge along with a circular hole near the top, while the bottom view portrays a different angle of the object with a straight edge and a curved portion. A dashed line suggests a division of the object, and at the bottom of the image, the term "Width2" indicates a measurement related to the width of the object, which could be important for understanding its dimensions in a practical application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VtUtcO9dHYdpp8s0lhHtrA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VtUtcO9dHYdpp8s0lhHtrA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle2::Angle2

Specifies the angle of the left tapered portion. Angle2 must be assigned a positive value and should less than 30 degrees. Else, an error
message is displayed. If Angle2 is set to zero, then the left line is drawn as global vertical.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Os8fKIitrofMBqjDkngIUg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b40406b500336d00)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Os8fKIitrofMBqjDkngIUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3

Specifies the angle of the right tapered portion. Angle3 must be assigned a positive value less than 30 degrees. Else, an error message is
displayed. Angle3 overrides the WIdth2 property to get the tapered bottom point.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HmKtYOBuWxU4y2EOc9QVyw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e097f5f1b93c5927)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HmKtYOBuWxU4y2EOc9QVyw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle4::Angle4

Specifies the angle of the bottom tapered portion. Angle4 must be assigned a positive value less than 45 degrees. Else, an error message is
displayed. If the left tapered portion does not intersect with the elbow, then the
lug extends down along the pipe per Angle4. If no value is assigned, Angle4 is set to 45 degrees.


Image:[Image-Analysis: The image depicts a geometric figure that appears to illustrate a relationship between a rectangle and a circle. The key elements include a tall, thin rectangle on the left side with a slight indication of an upper border, suggesting it might represent a geometric figure or an object. To the right, there is a circular shape which is likely depicting a part of the geometry adjacent to the rectangle. The dashed lines connecting the rectangle and the circle may indicate measurements or relationships such as tangents or angles. There are also marked points and directional indicators (possibly angles), which seem to represent some specific properties of the shapes involved. Overall, this image seems to convey mathematical or geometric concepts related to the dimensions and relationships of the depicted shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hmOpyygos9Zm73nOmk5keg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hmOpyygos9Zm73nOmk5keg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the lug.


icon that looks like an adjustable or variable width element with arrows pointing inward and outward, indicating a resize or adjust functionality: 

IJUAhsGap1::Gap1

Specifies the gap between lug components of a double lug.


Image:[Image-Analysis: The image depicts two vertical rectangles with arrows on both sides pointing towards the rectangles. This suggests a visual representation of adjusting or aligning two items, possibly indicating options to align their size or position. The arrows may signify a mechanism for shrinking or compressing the rectangles toward each other, which could relate to functions in user interfaces, resizing elements, or adjusting space between objects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FBCink62DTC_0dkj_JGijA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FBCink62DTC_0dkj_JGijA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerOffset

Specifies the offset of the stiffener between the two components of a double lug.
StiffenerOffset is set from center of PIN port.


Image:[Image-Analysis: The image depicts a mechanism involving a red rectangular element, which seems to represent a movable part in a system. Surrounding it are two larger rectangles, indicating a structural frame or housing. There are arrows pointing down, which likely indicate a force or movement direction, suggesting that the red element can move downward. The dashed red rectangle around the red element may indicate its operational zone or area of influence. The image seems to represent a basic mechanical system with a focus on movement dynamics, potentially relevant in engineering contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5FU7Th7VD1Hal9b0QmS5Eg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5FU7Th7VD1Hal9b0QmS5Eg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerHeight

Specifies the height of the stiffener between the two components of a double lug.


Image:[Image-Analysis: The image depicts a mechanical or structural system with two vertical bars on the sides and a horizontal member in the center. The central part is represented by a dashed line, suggesting it might be a support or connection point. Below the central member, there are downward arrows, indicating a force or weight being applied downward. This could represent a load being supported by the two side bars, which could be part of a frame or beam structure in engineering or architectural contexts. Overall, it visually illustrates how forces are transmitted through structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bUJPdHToVQsOzscwHXkJ2g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bUJPdHToVQsOzscwHXkJ2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::StiffenerLength

Specifies the length of the stiffener between the two components of a double lug.


Image:[Image-Analysis: The image depicts a geometric drawing tool called a compass, which is used for drawing circles and arcs. The compass features two legs: one has a pointed end that serves as the pivot point to anchor the compass on paper, while the other leg has a pencil attached to draw. The red dashed rectangle indicates a specific area around the compass, possibly signifying a region of interest or a measurement guideline related to the drawing action. The circular arc at the bottom suggests the path that can be drawn by the pencil leg as the compass is rotated around the pivot point. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KKfhVB6_6yn3fVHWPquamw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KKfhVB6_6yn3fVHWPquamw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the distance between the top port and the top of the lug. When TopShape is set to 1 - Curved, Offset1 is used for the eye radius.


Image:[Image-Analysis: The image depicts a geometric shape that appears to be a curved line or arc. At the top, there are two arrows pointing upwards, suggesting a possible indication of the orientation or direction of the shape. The red dot near the center may represent a specific point of interest or a pivot. The curved line subsequently shows how it connects or transitions towards a horizontal line. Overall, this image could represent concepts in physics or engineering, such as trajectories or forces applied to a curved surface. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qV6SUt2ulLoMkJZI5L6J_Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qV6SUt2ulLoMkJZI5L6J_Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLug::ChamfLength

Specifies the length of the chamfered edges. This property is valid only when TopShape is set to 4 - Chamfered.


look for an icon that resembles a corner bracket or a folded corner of a page with an indication of an adjustment or modification, often used in design or layout contexts: 

IJUAhsLug::RadiusActual

Specifies the required radius of the bottom arc of the elbow lug.


Image:[Image-Analysis: The image illustrates a diagram that likely pertains to the concepts of angles, geometry, or perhaps drafting related to arcs and tangents. It features a shape, possibly a corner or a section of a design feature, with a dashed curve indicating an arc. The presence of a solid red line suggests a specific direction or path that might be significant in a construction or mechanical context. The arrows pointing in different directions could indicate motion or the angles formed by the intersecting lines. Overall, the image seems to relate to geometry or engineering principles, focusing on how arcs and angles interact. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8Ieyfam_6ZiBx4b7xt1j3Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8Ieyfam_6ZiBx4b7xt1j3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the pin. If this property is set to zero, then, pin is not
drawn.


Image:[Image-Analysis: The image depicts a stylized representation of a bird's head and neck, outlined in black. The main features include the head, which is somewhat rounded at the top, tapering into a pointed beak. There is a red dot indicating an eye, positioned near the top-left of the head. Below the head, there is a curved line that suggests the neck. Additionally, there are two arrows pointing upwards at the top right and downwards at the bottom right, indicating some form of measurement or direction related to the bird. This image may represent a concept of bird anatomy or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tW2JZK5cJN0rwNt6laXuUQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/tW2JZK5cJN0rwNt6laXuUQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin1::Pin1Length

Specifies the length of the pin. Pin1Length should be greater than Gap1 + 2\*Thickness1.


Image:[Image-Analysis: The image displays a schematic representation of a simplified electrical circuit component, possibly a relay. At the top of the image are two arrows pointing left and right, indicating a movement or function. Below the arrows, there are two vertical rectangles that represent the main parts of the component, likely the coils or switches. Each rectangle is depicted as an empty shape, suggesting it's a diagram rather than a physical model. The red dotted lines below may indicate the contacts or links between these components, essential for understanding how the circuit completes when activated. The base shows a shaded area, suggesting a physical housing for this component where it would connect to other parts of an electrical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1lcB4JaftyUFlJRNWA40ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1lcB4JaftyUFlJRNWA40ZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details (Elbow Lug) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/353484?contentId=3i85kdU4aWMknj~FikhUpg)

Image:[Image-Analysis: The image presents a comparison table with two main categories: "Route" and "Bolt/Pin/Hole". Under the "Route" category, there are several attributes listed, including "Name", "PortType", "Size", "MinSize", and "UnitType", which seem to be properties related to a component or a path. Conversely, the "Bolt/Pin/Hole" category mirrors this structure with similar attributes: "Name", "PortType", "Size", "MinSize", and "UnitType". The layout illustrates a side-by-side comparison between the characteristics of routes and bolts/pins/holes, suggesting a detailed examination of both components in terms of naming, types, sizes, and units. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cTnEV8jKNxWhSnlw0HbhTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cTnEV8jKNxWhSnlw0HbhTA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image depicts a 3D object likely used in engineering or design, showcasing a component referred to as a "Lug." It illustrates the coordinate axes (X, Y, Z) that are important for understanding the orientation and dimensions of the Lug. The red dots signify specific points of interest or reference on the Lug's geometry. Furthermore, there is a labeled section titled "Route," which suggests a second object or pathway related to the Lug, possibly indicating a point of connection or flow direction. The image emphasizes the relationship between these two components through their alignment along the defined axes, highlighting their relevance in a spatial context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7rnljIXXpu4N7DLuE6POpA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7rnljIXXpu4N7DLuE6POpA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Lug Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1008 - Single Lug | Can be set according to your specification. | Smallest size that can connect. Can be set according to your specification. | Largest size that can connect. Can be set according to your specification. |
| 1009 - Double Lug | Can be set according to your specification. | Smallest size that can connect. Can be set according to your specification. | Largest size that can connect. Can be set according to your specification. |
| 1005 - Pin | Can be set according to your specification. | Smallest size that can connect. Can be set according to your specification. | Largest size that can connect. Can be set according to your specification. |

Route Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 - Route | 1 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Eye Nut - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307453?contentId=YVDswIO_Ywbu0ZgqTF_Btw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.EyeNut  
Part Name: Eye Nut  
Part Description: Eye Nut SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xFamOEA0Q2rl0fvYoaAmSw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3a162f766bb62bab)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xFamOEA0Q2rl0fvYoaAmSw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ are already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample Eye Nut SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Rod Fittings > Forged Steel Weldless Eye Nut –
   RH Thread as shown below.

   
Image:[Image-Analysis: The image displays a hierarchical structure of items within a category called "SmartParts." Under this category, there is a subcategory titled "S3D Standard," which contains various types of components such as "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," and "Rod Fittings." The "Rod Fittings" subcategory further breaks down into specific items including "Forged Steel Weldless Eye Nut - LH Thread," "Forged Steel Weldless Eye Nut - RH Thread," and a "Turnbuckle" which has a note mentioning it has an opening of approximately 6 inches. The organization reflects a clear hierarchy where broader categories are divided into more specific items. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PGVIE0pQmR5y_ZTG17xCSg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PGVIE0pQmR5y_ZTG17xCSg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image displays a diagram that outlines a three-dimensional coordinate system, commonly used in engineering and robotics. It shows a specific component or mechanism with labeled parts. The labels indicate the orientation of the axes: X (horizontal left-right) and Z (vertical up-down). The "RodEnd: 0,0,0" indicates a reference point or an origin in this coordinate space, typically signifying the position of the rod's end in 3D space. The "Eye" is likely a point of observation or a reference point, possibly for sensor placement or visual referencing. The arrangement and labeling suggest an emphasis on understanding the spatial relationships and functionalities of the components shown in terms of engineering applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aazKTsFj0acO0aZBjwgHdA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/aazKTsFj0acO0aZBjwgHdA-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  Throughout this discussion, the eyenut body graphic is represented in angular shape
as shown in graphic A, whereas, the actual eyenut body graphic uses curved shapes
as shown in graphic B.

A B


Image:[Image-Analysis: The image shows a simple flowchart or diagram representing a product or component design, possibly a type of dispenser or bottle based on the rounded bottom and the narrower neck at the top. It suggests a contained item with a cylindrical body and a flat base, indicating that it is designed for standing. The top section seems to imply a closure or opening mechanism, which could be for pouring or dispensing the contents. Overall, the image is abstract, focusing on the shape and structure without specific details about materials or functions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vvUCCnhVkZt~kfsvVf8z4A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vvUCCnhVkZt~kfsvVf8z4A-_PVFQNoCl4XmjAxWO0f7XQ/content) 
look for icon that resembles a clamp or fastening tool, typically used for holding objects together: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Eye Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307463?contentId=J9uh78~0FNeTarX8tw6KfQ)
These properties define the geometry of the eye nut.

IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of rod that attaches to the eye nut.

This value is used only in the Part Selection Rule for choosing an Eye Nut part. The rod is not included in the eye nut’s graphics.


Image:[Image-Analysis: The image depicts a diagram related to "Rod Diameter". It shows a structure, likely a clamp or holder, with several components indicating connection points and a rod that is positioned in the middle. The diagram includes arrows suggesting measurement or adjustment directions. There are red dots highlighting specific areas of interest, such as the rod's diameter, and it appears to emphasize points requiring attention for proper measurement or installation. Overall, the visual is likely intended for users needing to understand how to measure or adjust the diameter of a rod in the specific context of the assembly shown. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XWOcUdqKk0I1WVrue3~K0A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XWOcUdqKk0I1WVrue3~K0A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness or outside diameter of the cylindrical stock that is used to form the eye shape.


Image:[Image-Analysis: The image illustrates two different types of measurement tools: a pair of calipers on the left and a more simplified thickness gauge on the right. The calipers have a movable part that can measure inner and outer dimensions as well as depths, indicated by the indicators marked with red dots. The accompanying arrows suggest how to read the measurements for thickness. The right side shows a simple rectangular gauge designed specifically for measuring thickness, likely with a focus on capturing the thickness measurement more straightforwardly. The label "Thickness1" at the bottom indicates that this measurement tool is defined for a specific thickness measurement purpose. Overall, the image compares a multi-function measuring tool to a more specific thickness measurement tool. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1pYeZMwcRBv7AvcoKp6dEQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1pYeZMwcRBv7AvcoKp6dEQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerWidth1

Specifies the inside width of the eye shape at the oval threaded base.


Image:[Image-Analysis: The image appears to be a technical diagram illustrating a component with defined dimensions, specifically called "InnerWidth1." The diagram shows a central structure with multiple sections and indicates the width measurement between certain parts, as highlighted by the blue arrow. There are red dots that likely denote reference points for measurement, and the component is compared to a simplified view on the right side. The arrangement of the components suggests they may be part of a mechanical or architectural design, where understanding the inner width is critical for fitting or compatibility with other parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WQciLaGpPtnNSKda027efQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WQciLaGpPtnNSKda027efQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerWidth2

Specifies the inside width of the eye shape at a position InnerLength1 along the inside of the eye.


Image:[Image-Analysis: The image depicts a mechanical or structural element, likely a gripper or clamp mechanism. It has two main views: a front view showing the inner width (noted as "InnerWidth2") and a side view. The front view illustrates the opening mechanism, with an indication of the inner width distance marked by arrows. The structure consists of several angled elements converging towards the center to grip an object placed below. The red dots may represent pivot points, while the blue arrow indicates the measurement for the inner width. This design is typically used in automation or robotics for securely holding and manipulating items. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vSOrwV7k6vqW2AHT1oUVHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vSOrwV7k6vqW2AHT1oUVHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerLength1

Specifies the length at the position of InnerWidth2.


Image:[Image-Analysis: The image illustrates a geometric figure that seems to depict a mechanical part or a shape with specific dimensions. On the left side, there is a hexagonal structure with red markers indicating certain points of interest, likely representing connection or joint points. The measurement labeled "InnerLength1" suggests a specific internal length measurement associated with this shape. The right side of the image appears to show a vertical cylindrical shape or rod connected to the hexagonal figure, which might indicate how this part interfaces with another component. The lines and arrows point out dimensions and relationships, clarifying how the two shapes relate in terms of size and position. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QsQeWdnyBlA5MAgeFp2U2g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QsQeWdnyBlA5MAgeFp2U2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsElongatedEye::InnerLength2

Specifies the inside length of the eye shape.


Image:[Image-Analysis: The image appears to depict a mechanical component, likely a type of gripper or clamp mechanism. It shows two different configurations side by side. On the left, a hexagonal shape is formed with various parts connected to it, and there are visual indicators (red dots) suggesting points of measurement or connection. The right side seems to highlight a vertical element, which could represent the length adjustment feature of the mechanism. The label "InnerLength2" suggests it may refer to a specific measurement related to the inner dimensions of the device, implying that there are critical lengths to consider in its operation or design. Overall, the image illustrates how the two configurations of the mechanism relate, likely providing insights into its functionality and dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e_K8th9DHnYAqiCQsrSxyg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e_K8th9DHnYAqiCQsrSxyg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the amount that the rod extends past the oval threaded base.


Image:[Image-Analysis: The image consists of two sections. On the left, there is a hexagonal shape with red dots at various positions, indicating points of interest or measurements. The central part of the hexagon is labeled "OverLength1," which suggests that this may refer to a measurement, possibly in a structural or engineering context. The interconnected lines and shapes imply a relationship between these points, guiding the viewer's attention to the specifics of length or dimensionality. On the right side of the image, there is a vertical rectangular shape, which is likely representing a standard or reference length. The layout indicates that the measurement represented on the left may exceed or relate to the length indicated on the right, highlighting a comparison or critical dimension in a design or analysis scenario. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kokCo4MCrOPD~K85wO1IGg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kokCo4MCrOPD~K85wO1IGg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPinDiameter::PinDiameter

Specifies the diameter of the pin.

The eye port is located half the PinDiameter above the bottom cylinder and represents the center of the connecting pin.

It can also be an occurrence attribute and editable on the property page. It can be
used to override the default location of the eye port.


Image:[Image-Analysis: The image depicts a mechanical diagram illustrating the concept of "Pin Diameter." It shows a device, possibly a clamp or a gripper, with a pin highlighted in red at its center. The diagram on the left displays the device's top view, indicating how the components are arranged around the pin. There is an arrow pointing to the pin, labeling its diameter. The right side features a side view of the same device, reinforcing the understanding of how the pin fits into the structure. This image conveys the importance of the pin's diameter in relation to the device's functionality and design, suggesting that precise measurements are critical for effective operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ukFCZr5aCywdozUVLxAmFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ukFCZr5aCywdozUVLxAmFw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307476?contentId=B69LsTec3vgQOy~O2oaaXw)
These properties define the geometry of a nut.

IJUAhsShape1::Shape1Type

Specifies the graphic shape that is used for the nut or washer.

Uses the codelist number defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls.


Image:[Image-Analysis: The image displays three different geometric shapes with corresponding labels indicating their type and number. From left to right, the shapes are: 1. A round shape (circle) labeled as "1 - Round," 2. A square shape labeled as "2 - Square," and 3. A hexagonal shape (hexagon) labeled as "3 - Hex." Each shape has a small dot in the center, illustrating that all shapes are similar in having an inner point, but different in their outer geometrical form. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qFly6x_Sm_Uuj8XN2hx2XQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qFly6x_Sm_Uuj8XN2hx2XQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the Width of the oval shape representing the threaded base of the eye nut.


Image:[Image-Analysis: The image presents a technical diagram featuring a shape identified as "Shape1" with annotations for its dimensions and aspects. The upper part illustrates a rectangular shape with a circular hole in it, accompanied by dimension arrows indicating width measurements. Below, there's another representation of the shape, which appears to depict a more complex structure with multiple lines and points marked in red to indicate specific measurement points or centers of interest. The layout suggests a logical flow from the design elements to their respective dimensions, indicating the importance of precise measurements in technical drawings. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gp2xjk2fJsmdz8rKhbsKwg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gp2xjk2fJsmdz8rKhbsKwg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer. You can use the Shape1Width2 to create a rectangle shape instead of a square.

If it is set to zero, negative, or not specified, Shape1Width1 is used as Shape1Width2.


Image:[Image-Analysis: The image depicts two shapes: on the left, there is a hexagonal or polygonal shape with a wider rectangular top and a narrow rectangular base, and on the right, there is a narrower, square shape. The left shape seems to be labeled "Shape1Width2," indicating that it may relate to a specific width or dimension relevant in a design or engineering context. The red dots could signify critical points of interest or measurement points within the design. The contrast between the two shapes suggests a comparison of widths, likely focusing on design parameters in engineering or architecture. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GX7VmLzuPskAJjA5OZEnqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GX7VmLzuPskAJjA5OZEnqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the Height of the oval shape representing the threaded base of the eye nut.


Image:[Image-Analysis: The image illustrates two shapes, presumably from a technical or engineering perspective. On the left, there is a shape labeled as "Shape1," which features a complex outline with various connecting points, indicated by small red dots. These red dots might signify measurement points or connection points. The shape on the right appears to be a simplified representation, focusing on dimensions with labels showing the "Length" of the shape. The two shapes possibly represent a comparison of a more complex figure against a simplified version, emphasizing the importance of measurements in understanding the dimensions and relationships of the shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vv64pSJbwmkdmbKxJWozMQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vv64pSJbwmkdmbKxJWozMQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307483?contentId=9SZ1VFNGnehXLmYCVTzF4A)
These properties are used to specify the different port types and their sizes for
the eye nut.


Image:[Image-Analysis: The image presents a table divided into three columns labeled as Port 1: RodEnd, Port 2: Eye, and Port 3: Surface. Each port has corresponding attributes listed, which include Name, PortType, Size, MaxSize, and UnitType. The table appears to categorize different connection points (ports) and their specifications. The connections between the ports may indicate how they interact with each other or contribute to a larger mechanical or engineering assembly. The use of varying colors in the header sections distinguishes each port, suggesting they have unique functions or characteristics. Overall, this layout helps in comparing the specifications and understanding the role of each port in a system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Mkzk8~4LXygQaM_y6WZx_w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Mkzk8~4LXygQaM_y6WZx_w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – RodEnd – Located at 0, 0, 0

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1001 – IntThdRH | * The diameter of the rod, for connecting to other components. * It is same as the RodDiameter property. | Not applicable for this port type. Use zero. | Not applicable for this port type. Use 9999. |
| 1003 – IntThdLH | * The diameter of the rod, for connecting to other components. * It is same as RodDiameter property. | Not applicable for this port type. Use zero. | Not applicable for this port type. Use 9999. |

Port2 – Eye – Located at 0, 0, OverLength1 – InnerLength2 + PinDiameter / 2.0

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1007 – Eye | The thickness of the eye to be compared against the opening in the connecting item. This lets you verify that the thickness of the eye fits into the opening.  It is same value as Thickness1 property. | The smallest pin or bolt that will fit inside the eye. Usually, this value is zero. | The largest pin or bolt that will fit inside the eye, from the catalog specs. |

Port3 – Eye – Surface – Located at 0, 0, OverLength1 + Height1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 - Other | Not applicable for this port type. Use zero. | Not applicable for this port type. Use -9999. | Not applicable for this port type. Use 9999. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Grip Pipe Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777038?contentId=1C0AOM9Rf0ta0Gn0K6CqDA)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.GripClamp  
Part Name: Grip Pipe Clamp  
Part Description: GripPipeClamp, Nominal Dia <Diameter>"

![Grip Pipe Clamp SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OcJUG577SR1kSqsTX9a4Mw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5f786a02c7e83b5a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OcJUG577SR1kSqsTX9a4Mw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Horizontal Traveler SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.

   ![S3D Grip Pipe Clamp SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XbNR4_pXlWpAIyHKJTCnsA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=815a59383405e3d2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XbNR4_pXlWpAIyHKJTCnsA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System

![Grip Pipe Clamp SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/10UbvSMy3fUx95SSSqsfGA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=cfe12b65d060eba7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/10UbvSMy3fUx95SSSqsfGA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777039?contentId=Qa8vee2Wxhr1Yz3aX4Zcqg)
The following graphic illustrates the orientation of the ports for the grip pipe clamp:

![Grip Pipe Clamp SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/itCJT8S5Deps1LUlNgKpRg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6e7b362c40b06e40)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/itCJT8S5Deps1LUlNgKpRg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port details and their orientation

Port1:Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1016 - Pipe Clamp | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2: Lug Port (0, 0, RodTakeOut)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004 - Hole | Pin/Bolt Diameter | 0 | Pin/Bolt Diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777043?contentId=OxU8R0HOfKHzf09UJHZlfw)
The BOM description must use the PartDescription and sets the property IJHgrBOMDefinition::BomType value to 2.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Grout - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/581651?contentId=bV3UklTThzdJny_fsX5nEQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Grout  
Part Name: Grout  
Part Description: Grout Smart Part

![Grout](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BawZZCchNgVx848u4ss8ww-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0a3bca879e4c73df)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BawZZCchNgVx848u4ss8ww-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Ensure that the following workbooks are available in the following location before
you place the parts:

[Product Folder]\CatalogData\BulkLoad\DataFiles\

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

The HS\_S3DParts.xls file provides sample smart part data and is available from the following location:

[Product Folder]\CatalogData\BulkLoad\DataFiles

Part Placement

To place a sample Grout SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a price tag, indicating an addition or increase in price or value: , and then select the design support.
4. In the Select Part dialog box select a part from Parts > SmartParts > S3D Standard > Miscellaneous > Grout > Grout as shown below.

   ![Grout_UI-SmartPart - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j0smovyAT85qCA1tyV110A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=607728e82bf7def4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j0smovyAT85qCA1tyV110A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Alt-Text: Local Coordinate System - Grout 
Image-Analysis: The image depicts a geometric shape (a trapezoid) with labeled coordinates and structures. It shows two structures: Structure1 and Structure2, both defined at the coordinate (0, 0, 0) for Structure1 and (0, 0, ShapeHeight) for Structure2. The axes are labeled x and z, indicating a three-dimensional coordinate system. The z-axis is vertical, pointing upwards, while the x-axis is horizontal. This image is likely used to explain a mathematical or engineering concept involving the positioning and dimensions of structures in a 3D space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fkb9hJ3XmpJjX76NiOWeDg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Local Coordinate System - Grout](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fkb9hJ3XmpJjX76NiOWeDg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Grout Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/581688?contentId=buGhJL_5LxR1GcVc0Ev~Vg)
Specifies the shape and structure of the Grout. The following properties are categorized
under Basic Grout Attributes:

IJUAhsGroutShape::ShapeType

Specifies the graphic shape to use for the Grout. This property uses the following
hsGroutShapeType codelist values:

1 – Round


Image:[Alt-Text: Round - Grout hsGroutShapeType - New H&S Guide 
Image-Analysis: The image shows two concentric circles. The larger circle surrounds a smaller circle at the center. This visual could represent concepts such as relationships, gradation, or differences in size and scale, suggesting a theme of inclusion or containment where the smaller circle is nested within the larger one. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yuKpPOe51rn3hh5EAN2OCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Round - Grout hsGroutShapeType - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yuKpPOe51rn3hh5EAN2OCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Rectangle


Image:[Alt-Text: Rectangle - Grout hsGroutShapeType - New H&S Guide 
Image-Analysis: The image depicts a 3D shape resembling a rectangular prism or a cuboid, viewed from an angle that reveals its three-dimensional attributes. The outer edges are defined with straight lines, tapering towards the base of the shape, creating an illusion of depth and perspective. This shape could represent various concepts in geometry or be used as a visual representation in design or architectural contexts. The empty central space suggests it may be used to illustrate a placeholder or frame for additional content or information. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_RG5aG2AbOGFAC58bXwnmg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Rectangle - Grout hsGroutShapeType - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_RG5aG2AbOGFAC58bXwnmg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGroutBotWidth1::BottomWidth1

Specifies the bottom dimension of the Grout. If the property value is 0, the Grout
placement fails.

1 – Round


Image:[Alt-Text: BottomWidth1_ Round - Grout - New H&S Guide 
Image-Analysis: The image depicts two concentric circles. The larger circle is drawn with an outer edge, while the smaller circle is enclosed within. To the left, there are vertical lines indicating a measurement, likely representing the diameter of the larger circle, as well as the diameter of the smaller circle. This potentially illustrates the concept of interior and exterior dimensions in a geometric context, often used in fields like engineering or architecture to show measurements related to round objects or shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b4yTCK27gds4heN8~jsPSg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BottomWidth1_ Round - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b4yTCK27gds4heN8~jsPSg-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Rectangle


Image:[Alt-Text: BottomWidth1_ Rectangle - Grout - New H&S Guide 
Image-Analysis: The image depicts a rectangular shape with dimensions indicated by vertical and horizontal arrows. The left side has a vertical arrow showing height, while the bottom has a horizontal arrow representing width. The rectangular object is hollow and appears to have its edges rounded, indicating it may represent a three-dimensional object or a frame. The dimensions are crucial in understanding the size and proportions of the rectangle, which could relate to various fields such as geometry, design, or architecture. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WunUSM4O5O59hFx5nPfyHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BottomWidth1_ Rectangle - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WunUSM4O5O59hFx5nPfyHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGroutBotWidth2::BottomWidth2

Specifies the bottom dimension of the Grout. If the BottomWidth2 and BottomWidth1 property values are not equal, the BottomWidth2 value is ignored.

1 – Round


Image:[Alt-Text: BottomWidth2_ Round - Grout - New H&S Guide 
Image-Analysis: The image depicts a diagram illustrating the dimensions of a circular object. At the center, there is a smaller concentric circle within a larger circle. There are horizontal arrows on either side of the outer circle, indicating the diameter measurement from one edge of the circle to the other. This diagram is typically used to represent the dimensions of objects in geometric contexts, showing the relationship between the inner and outer circles, as well as providing a visual cue for measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fDmjNiEwthF92Ig6dbhWCw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BottomWidth2_ Round - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fDmjNiEwthF92Ig6dbhWCw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Rectangle


Image:[Alt-Text: BottomWidth2_ Rectangle - Grout - New H&S Guide 
Image-Analysis: The image presents a rectangular shape with a border that has arrows on either side pointing left and right, indicating a horizontal movement or flow. The outer rectangle appears to be a selection area or container that encompasses an inner rectangle. The arrows suggest that the content within the inner rectangle can be adjusted, resized, or moved horizontally. This could represent an interface element used in design, suggesting drag functionality or adjustable parameters often seen in software layout or user interfaces. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uPlcZ5q8H7gJX7R4qskGSA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![BottomWidth2_ Rectangle - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uPlcZ5q8H7gJX7R4qskGSA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGroutTopWidth1::TopWidth1

Specifies the top dimension of the Grout. If the property value is 0, the Grout placement
fails.

1 – Round


Image:[Alt-Text: TopWidth1_ Round - Grout - New H&S Guide 
Image-Analysis: The image presents a diagram consisting of two concentric circles: one larger outer circle and a smaller inner circle. There are vertical lines drawn from the outer circle to the inner circle, indicating the dimensions or radii of the circles. This setup suggests that the image is likely used to illustrate concepts such as diameters, radii, or perhaps the relationship between different sizes of circles, which may be relevant in geometry or physics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k5zmEHsz4lUsMZUwhmPeTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![TopWidth1_ Round - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/k5zmEHsz4lUsMZUwhmPeTA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Rectangle


Image:[Alt-Text: TopWidth1_ Rectangle - Grout - New H&S Guide 
Image-Analysis: The image depicts a rectangular shape with a smaller, solid rectangle inside. The outer rectangle has rounded corners, and the inner rectangle is positioned centrally within the outer rectangle. There are vertical arrows pointing to the top and bottom edges of the inner rectangle, indicating its height (denoted as "h"). The image could be illustrating a concept related to dimensions, specifically the measurement of height, which is commonly used in technical drawings, design, or geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H38JwA6QycpDQBCgUYnX_w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![TopWidth1_ Rectangle - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H38JwA6QycpDQBCgUYnX_w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGroutTopWidth2::TopWidth2

Specifies the top dimension of the Grout. If the TopWidth2 and TopWidth1 property values are not equal, the TopWidth2 property value is ignored.

1 – Round


Image:[Alt-Text: TopWidth2_ Round - Grout - New H&S Guide 
Image-Analysis: The image depicts a circular shape with a smaller concentric circle inside it, connected by two vertical lines representing a relationship or connection between the two circles. The arrows pointing to the sides suggest measurement, possibly indicating the diameter of the outer circle or a relationship in size between the inner and outer circles. This could signify a concept in geometry or physics, illustrating the difference or relation in size between two circular entities. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4472nyHGmQrbZS9PRUu2lA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![TopWidth2_ Round - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4472nyHGmQrbZS9PRUu2lA-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 – Rectangle


Image:[Alt-Text: TopWidth2_ Rectangle - Grout - New H&S Guide 
Image-Analysis: The image depicts a rectangular shape with an inner rectangle and double-headed arrows on the top, indicating measurement or relationship between two dimensions. The outer shape represents a three-dimensional object, while the inner rectangle indicates a specific area or section within that object. The arrows suggest that there may be a measurement or adjustable space that can expand or contract between these two areas, showcasing a connection or relationship between the sizes of the two rectangles. This type of diagram is commonly used in technical drawings or architectural designs to illustrate dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5ep7~A2cq0lMNDLW95XTOg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![TopWidth2_ Rectangle - Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5ep7~A2cq0lMNDLW95XTOg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGroutHeight::GroutHeight

Specifies the height of the Grout. If the property value is 0, the Grout placement
fails.


Image:[Alt-Text: GroutHeight_Grout - New H&S Guide 
Image-Analysis: The image depicts a trapezoid, which is a four-sided polygon (quadrilateral) with at least one pair of parallel sides. The upper portion of the shape is wider than the lower part. There are also two arrows indicating a height measurement, suggesting the vertical distance from the top base to the bottom base. This height is crucial in calculating the area of the trapezoid, which can be determined by the formula: Area = (1/2) * (Base1 + Base2) * Height, where Base1 and Base2 are the lengths of the two parallel sides. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjDnIIeAmkX3NdtPoUVHPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![GroutHeight_Grout - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjDnIIeAmkX3NdtPoUVHPg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/581657?contentId=XfPZ6dtUSaaRimc7Tziwdg)
These properties are used to specify the different port types and their sizes for
the grout. A grout can have the following ports:

* Structure1
* Structure2


Image:[Alt-Text: Grout Port Properties - New H&S Guide 
Image-Analysis: The image presents a comparative layout between two ports, labeled Port1 and Port2, which are displayed side by side. Each port has several attributes directly associated with it. Under Port1, the attributes include Name, PortType, Size, MinSize, MaxSize, and UnitType, each associated with the symbol "HgrSymbolPort(1)". Similarly, Port2 has the same set of attributes—Name, PortType, Size, MinSize, MaxSize, and UnitType—featured with the symbol "HgrSymbolPort(2)". This layout likely indicates a structured comparison of characteristics for two different ports in a system, highlighting similarities and differences in their specifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XmHG9cOk_0LZ3P_gn23O7w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Grout Port Properties - New H&S Guide](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XmHG9cOk_0LZ3P_gn23O7w-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Alt-Text: Port Details - Grout 
Image-Analysis: The image illustrates two structures labeled as Structure1 and Structure2. Each structure has a coordinate system defined by axes labeled x and z, with the z-axis pointing upwards. The relationship between the two structures is likely functional or positional based on their orientation in the coordinate system. The axes are drawn in red to highlight the directional reference for plotting or understanding spatial relations between these structures. The diagram may represent a geometric or engineering concept where the two structures are compared or analyzed in relation to their respective axes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PSpl98tTf3M9hXKL9qpPOw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Port Details - Grout](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PSpl98tTf3M9hXKL9qpPOw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port details and orientation

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| Structure1  3 | N/A  Use 0 | N/A  Use -9999 | N/A  Use 9999 |
| Structure2  3 | N/A  Use 0 | N/A  Use -9999 | N/A  Use 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Guide - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/378412?contentId=suTaLp5tXPolcy7pEjFg1A)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Guide  
Part Name: Guide  
Part Description: Guide SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vC5JCXJ4Y8Bq5cFS5wSEsw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=0f1ac23086bbd755)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vC5JCXJ4Y8Bq5cFS5wSEsw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample Guide delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Guides > Guide as shown below.

   
Image:[Image-Analysis: The image is a hierarchical diagram representing a structure of different parts categorized under the main heading "Parts". This structure indicates a nested organization where "Parts" is the top-level category. Under "Parts", there are multiple subcategories including "AISC LRFD-3.1 Steel", "Anvil", "Load Rated Parts", "Sample 3DAPI Plates", and "SmartParts". The "SmartParts" category further expands to include "Bergen-Power NF09.3" and "S3D Standard", which has its own subcategories: "Beam Attachments", "Clevises", "Constant Supports", "Elbow Lugs", "Guides", and "Guide". The diagram suggests a well-organized inventory or database of various components used in construction or engineering tasks, emphasizing the relationship and hierarchy among the different types of parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4LZztX_KLGhQUTW1Hi8zKQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4LZztX_KLGhQUTW1Hi8zKQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bRREHLbbeqMIEyD9UPgGqw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=63c9afe19b545769)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bRREHLbbeqMIEyD9UPgGqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Plate Dimensions

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3wlGhUPR4xrYwsp~BQXbkQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b03f7cd7d393e3c8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3wlGhUPR4xrYwsp~BQXbkQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Spacing Dimensions


Image:[Image-Analysis: The image presents a technical diagram showing a structure with measures including "Offset1," "Gap1," and "Guide Height." The diagram includes two vertical elements on either side, with horizontal bars at the top that appear to represent some kind of brackets or supports. The central component looks to be a smaller rectangle positioned below the horizontal bars, possibly implying it serves a specific function along with the accompanying measurements. The labels indicate the distances and heights related to the structure, which would be important in understanding the arrangement and spacing of the elements for assembly or installation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bAVPdkoiE8QTJd4aY5DEBw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bAVPdkoiE8QTJd4aY5DEBw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Gusset Dimensions

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I1ntSggPFpBwhcqm0O4TSQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=e241faf6379188b2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/I1ntSggPFpBwhcqm0O4TSQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Guide Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/378413?contentId=XEI3WyGf2yA0hRlVHAigYQ)
The following properties define the basic geometry of the guide.

IJUAhsWidth1::Width1

Specifies the width of the base plate. Width1 is required if Thickness1 > 0.

IJUAhsLength1::Length1

Specifies the depth of the base plate. Length1 is required if Thickness2 > 0.

IJUAhsThickness1::Thickness1

Specifies the thickness of the base plate. If Thickness1 < 0, the base plate is not included.

IJUAhsWidth2::Width2

Specifies the width of the vertical plate.

IJUAhslength2::Length2

Specifies the length of the vertical plate.

IJUAhsThickness2::Thickness2

Specifies the thickness of the vertical plate.


None: 

* Thickness2 is required if vertical steel is not used.
* Thickness2 is required if vertical steel is used and section configuration is vertical.

IJUAhsWidth3::Width3

Specifies the width of the horizontal plate.

IJUAhsLength3::Length3

Specifies the depth of the horizontal plate.

IJUAhsThickness3::Thickness3

Specifies the thickness of the horizontal plate. Thickness3 is used only when GuideHeight is less than Thickness2.

IJUAhsWidth4::Width4

Specifies the width of the block plate.

IJUAhsLength4::Length4

Specifies the depth of the block plate.

IJUAhsThickness4::Thickness4

Specifies the thickness of the block plate.

IJUAhsOffset1::Offset1

Specifies the distance between the edges of the horizontal and the vertical plate.

IJUAhsGap1::Gap1

Specifies the gap between two vertical plates or between the cardinal points of the
steel sections.

IJUAhsGuideHeight::GuideHeight

Specifies the distance between the bottom edge of the vertical plate and top edge
of the horizontal plate.When the GuideHeight is provided, Thickness3 value is ignored and calculated as Thickness3 = GuideHeight - Thickness2.


Image:[Image-Analysis: The image is a technical diagram showing the relationship between different components, likely part of a mechanical or structural system. It features two rectangular blocks on top and a larger base below. The smaller block in the center appears to be a guide or positioning reference. The diagram includes measurements labeled as "Offset," "Gap1," and "Guide Height," indicating the dimensions and positioning of the blocks relative to each other. "Offset" likely refers to the lateral distance between the blocks, while "Gap1" indicates the distance separating the center block from the blocks on either side. "Guide Height" is a vertical measurement that could denote the height of the blocks or the distance from the base to the top of the blocks, suggesting a three-dimensional relationship among the components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YRyDKexanqmO7JYiQcmm~Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YRyDKexanqmO7JYiQcmm~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  VerPlSecStand, VerPlSecSize and VerPlSecType are optional if vertical steel sections are not used.

IJUAhsVerPlSecStand::VerPlSecStand

Specifies the section standard for the vertical plate.

IJUAhsVerPlSecSize::VerPlSecSize

Specifies the section size for vertical the plate.

IJUAhsVerPlSecType::VerPlSecType

Specifies the section type for vertical the plate.

IJUAhsAngle1::Angle1

Specifies the rotation angle of the first vertical section along its longitudinal
axis.

IJUAhsAngle2::Angle2

Specifies the rotation angle of the second vertical section along its longitudinal
axis.


Image:[Image-Analysis: The image illustrates two different angles, labeled as Angle1 and Angle2, associated with two 'L' shaped figures. The left figure shows Angle1, which is an acute angle, while the right figure shows Angle2, which appears to be a right angle. The arrows indicate the measurement direction of the angles. This comparison highlights the difference in degrees between acute and right angles, providing a visual understanding of angular relationships. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WPfIWh18iQobMx7Dvh00iA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WPfIWh18iQobMx7Dvh00iA-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image depicts a maze-like structure with pathways and junctions. It appears to contain a starting point indicated by the red dot, which presumably represents a position or point of interest within the maze. The layout consists of straight and curved paths that lead off in different directions, illustrating various pathways that can be taken. The green path likely represents a main route, while the purple dashed lines could indicate alternative routes or paths that can be followed. The number "2" marked on the junction suggests a possible reference point or goal within this maze. Overall, the image illustrates decision-making in navigating through a complex layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rHZfwVLX7dHlzhgDorDZnw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rHZfwVLX7dHlzhgDorDZnw-_PVFQNoCl4XmjAxWO0f7XQ/content)


None: 

* Each angle is applied about the cardinal point specified.
* The angle is ignored if the section is not specified or a plate is used instead.

IJUAhsConnection1::Connection1

Specifies the cardinal point of the first vertical section. It determines the connection
point of the steel section.

SHARED Tip
 For more information, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls.

IJUAhsConnection2::Connection2

Specifies the cardinal point of the second vertical section. It determines the connection
point of the steel section.

SHARED Tip
 For more information, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls.

IJUAhsMirrored1::Mirrored1

Indicates whether the first vertical steel section is mirrored about the specified
cardinal point. If not specified, the section is not mirrored.


Image:[Image-Analysis: The image contains a visual representation of the letter "T" constructed in a grid format. The left side features a dashed outline of the letter "T" filled with a dark purple color, while the right side shows a solid green version of the same letter "T." Below the two letters there is a small red square. This composition highlights the difference in shading and style between the dashed and solid representations of the letter "T," with the red square possibly indicating a point of interest or focus in the lower part of the image. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jAqpY6Ibh4Ctdc1lv76bYA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/jAqpY6Ibh4Ctdc1lv76bYA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMirrored2::Mirrored2

Indicates whether the second vertical steel section is mirrored about the specified
cardinal point.If not specified, the section is not mirrored.

IJUAhsSecConfig::SecConfig

Specifies if the vertical steel section is vertical or horizontal.


Image:[Image-Analysis: The image presents a comparison between two orientations: Horizontal and Vertical. On the left side, there are stacked structures labeled as "Horizontal," indicating they are organized side by side. On the right side, there are structures labeled as "Vertical," which are arranged one on top of the other. The distinction is visually represented by the orientation of the icons and the respective labels beneath each arrangement. This could relate to various fields, such as architecture, design, graphs, or layout planning. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KnPDISuBXfBNxkdalOGfhA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KnPDISuBXfBNxkdalOGfhA-_PVFQNoCl4XmjAxWO0f7XQ/content)


None: 

* Length2 is required if SecConfig is horizontal.
* Thickness2 is required if SecConfig is Vertical.

IJUAhsHorPlSecStand::HorPlSecStand

Specifies the section standard for the horizontal plate.

IJUAhsHorPlSecSize::HorPlSecSize

Specifies the section size for the horizontal plate.

IJUAhsHorPlSecType::HorlSecType

Specifies the section type for the horizontal plate.

IJUAhsCPXOffset::CPXOffset

Specifies the offset of the cross section shape with respect to the cardinal point
horizontally. CPXOffset is required when cross section is rotated.

IJUAhsCPYOffset::CPYOffset

Specifies the offset of the cross section shape with respect to the cardinal point
vertically.


Image:[Image-Analysis: The image depicts a technical diagram that illustrates two entities represented by U-shaped paths on either side. Each path has a labeled point marked "CP", indicating a control point or a significant point of reference. Between the two paths, there is a labeled gap, which may refer to the distance or space between the two entities. Additionally, on the lower side, there are parameters labeled "CPOffsetY" and "CPOffsetX", which suggest adjustments or offsets along the Y and X axes respectively, indicating a spatial relationship in terms of positioning. This setup is likely used in a context where precise placement or alignment of components is critical, such as in engineering or computer graphics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fXhpPazJYEXsGZJutZIUTQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fXhpPazJYEXsGZJutZIUTQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3

Specifies the rotation angle of the first horizontal section along its longitudinal
axis.


Image:[Image-Analysis: The image illustrates a comparison between two different bar graphs. On the left, there are two vertical bars of equal height representing the same category or value. The bars are elevated above a red horizontal line which might signify a baseline or threshold. On the right, there is a different bar that is shorter, also placed above a similar horizontal red line. This suggests a discrepancy in values between the two graphs. In addition, there is an arrow indicating a possible decrease or a directional change, which may highlight a transitional metric or trend connecting the two sets of data. The visual layout effectively portrays a comparison of size and value between these two metrics, making it clear that one set is less than the other. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hrelHBEXVHFGMkTYUWYqBQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hrelHBEXVHFGMkTYUWYqBQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle4::Angle4

Specifies the rotation angle of the second horizontal section along its longitudinal
axis.

IJUAhsConnection3::Connection3

Specifies the cardinal point of the second horizontal section. It determines the connection
point of the steel section.

SHARED Tip
 For more information, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls.

IJUAhsConnection4::Connection4

Specifies the cardinal point of the second horizontal section. Determines the connection
point of the steel section.

SHARED Tip
 For more information, see the CrossSectionCardinalPoints codelist in the Allcodelists.xls.

IJUAhsOffset2::Offset2

Specifies the offset value of the horizontal section from the connection point.


Image:[Image-Analysis: The image depicts a hydraulic press mechanism. At the top, there are two arrows indicating a force being applied, which suggests that pressing down will generate pressure. The cylindrical object in the center represents the hydraulic cylinder, which utilizes pressurized fluid to exert force. Below it, there is a rectangular area outlined in red, which appears to serve as the base or platform that might be used to hold the material or object being pressed. The design emphasizes the principle of hydraulic compression, where force is magnified, allowing for heavy objects to be crushed or shaped with relatively little input force. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/frDQUHsC2Qo6VxI9bGgFww-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/frDQUHsC2Qo6VxI9bGgFww-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  HorPlSecStand, HorPlSecSize and HorPlSecType are optional and not required if Length3, Width3 and Thickness3 are defined. Length3 and Thickness3 are optional and not required if HorPlSecStand, HorPlSecSize and HorPlSecType are defined.

IJUAhsSolidBaseVerPl::SolidBaseVerPl

Specifies which solid shapes would be used to create the base plate and the vertical
plate. This attribute uses the YES/NO codelist.


None:  
None: 

* YES – Base plate and vertical plate are one solid shape.
* NO –Separate solid shapes are used to create base plate and vertical plate.

IJUAhsSolidVerHorPl::SolidVerHorPl

Specifies which solid shapes are used to create horizontal plate and vertical plate. This attribute uses the YES/NO codelist.


None:  
None: 

* YES – Vertical and horizontal plates are one solid shape.
* NO –Separate solid shapes are used to create the horizontal and the vertical plate.


None:  Using the above properties different combinations of base, horizontal and vertical
plates can be defined.


icon-description of a connector or interconnection between two blocks or nodes:  
look for icon that resembles a layout or structure, similar to a building or a section of a structure: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Gusset Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/380447?contentId=6fRbQpmTJlsur4WBdMbk0Q)
The following properties define the basic geometry of the optional gusset.

IJUAhsWidth5::Width5

Specifies the primary width of the gusset. This value must be greater than zero, or
no gussets are modeled.

IJUAhsLength5::Length5

Specifies the primary length of the gusset. This value must be greater than zero,
or no gussets are modeled.

IJUAhsThickness5::Thickness5

Specifies the primary thickness of the gusset. This value must be greater than zero,
or no gussets are modeled.

IJUAhsWidth6::Width6

Specifies the secondary width of the gusset. This value must be greater than or equal
to zero.

IJUAhsLength6::Length6

Specifies the secondary width of the gusset. This value must be greater than or equal
to zero.

IJUAhsOffset3::Offset3

Specifies the horizontal position of the gusset's corner.

IJUAhsOffset4::Offset4

Specifies the vertical position of the gusset's corner.

IJUAhsMulti1::Multi1Qty

Specifies the quantity of gussets on each side. Gussets are not shown when Multi1Qty is set to zero.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the distance for the exact location of the gussets depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the end or a center-to-center spacing between
the gussets.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/380448?contentId=~oMIV34X_OyILK5_~48lZg)
The following section specifies how to determine the port type and the size information
for each of the ports when generating the catalog data for your parts.

Surface Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1200 – Other | N/A – Use 0 | N/A – Use -9999 | N/A – Use 9999 |

Structure Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 3 – Structure | N/A – Use 0 | N/A – Use -9999 | N/A – Use 9999 |

Route Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 – Route | Pipe OD | Pipe OD | Pipe OD |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Horizontal Traveler - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774063?contentId=zwKifRZXgP1ZembXMSzK1g)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.HorizontalTraveler  
Part Name: Horizontal Traveler  
Part Description: Horizontal Traveler, Hole Dia <Diameter>"

![Horizontal Traveller - SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qB6TsEc89rFye4MJkEeypg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=542fae2f7afe0c7a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qB6TsEc89rFye4MJkEeypg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Horizontal Traveler SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Horizontal Traveler > Horizontal Traveler as shown below.

![S3D Horizontal Traveler SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CW6ia6Iim7W890gOWKCwMA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bec10f0192d09d20)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CW6ia6Iim7W890gOWKCwMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Alt-Text: Horizontal Traveler SmartPart - LCS 
Image-Analysis: The image depicts a schematic representation of a structural object with an outlined shape and a hole. On the left side, there is a rectangular structure labeled "Structure" and a smaller rectangular shaped hole labeled "Hole" extending downward. The hole is associated with the structure. On the right side, a view of the object is displayed, showing the object from a different angle where the axes are marked with X and Z directions, indicating a reference for orientation in three-dimensional space. This may suggest a technical drawing likely used in engineering or architectural contexts, showing how the structure relates to its spatial dimensions and features. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9plL5YvczeOQRnxnrmRYiw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9plL5YvczeOQRnxnrmRYiw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [General Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774454?contentId=j3gTOFWfyJTuM86XJUjv2w)
The general attributes of a horizontal traveler might not include the two end plates
and the lug plate.


icon-description: look for icon that resembles a signpost or a directional sign, often used to indicate direction or provide information: 

IJUAhsThickness1::Thickness1

Specifies the thickness of both the sides of a horizontal traveler and must be a positive
number. If the thickness is zero, the sides must not be shown.


Image:[Alt-Text: Horizontal Traveler - General Att - Thickness 
Image-Analysis: The image depicts a diagram illustrating a hydraulic or pneumatic system, likely showing the movement of a piston. The main components include two vertical cylinders on the left and right, each with a red dot representing a piston or valve. The lines with arrows indicate the direction of movement, suggesting that the pistons can be pushed or pulled, creating pressure or force in the attached system. The bottom section appears to be a base or reservoir connected to the components above. This type of setup is commonly used in mechanical engineering for machines that depend on force generation through fluids or gases. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7T1HHMKF3A96AfcxLSZYrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - General Att - Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7T1HHMKF3A96AfcxLSZYrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height of both the sides of the horizontal traveler, includes the thickness
of the base plate, and must be a positive number.


Image:[Alt-Text: Horizontal Traveler - General Attr - Height1 
Image-Analysis: The image depicts a mechanical device known as a hydraulic lift or hydraulic jack. The lift consists of a large rectangular platform (gray), supported by vertical pillars on either side, which are used to elevate the platform. At the base of the image, there is a smaller rectangular component (represented in white) that includes two vertical red dots, likely indicating the control or connection points for the hydraulic system. The arrows on the right side suggest a vertical movement, indicating that the platform can move up and down to lift heavy objects. The hydraulic mechanism relies on pressure to raise or lower the platform, illustrating efficiency in lifting heavy loads, commonly used in garages and warehouses. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vg5EUlV43pKH6JAJV_6ViQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - General Attr - Height1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vg5EUlV43pKH6JAJV_6ViQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of the horizontal traveler and excludes end plates. This value
must be a positive number.


Image:[Image-Analysis: The image depicts a diagram showing a structural element, likely a beam, supported at its ends. Above the beam, there are arrows pointing outward, indicating applied forces or reactions at the supports. The vertical dashed lines suggest areas where measurements might be taken, such as from the beam to the ground or to additional structures. There are also red dots which could represent points of interest, such as load application points or support locations. The sketch emphasizes the beam’s position and its interaction with the support structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Adj_HFYR~0CUWqOVt~T7Gg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Adj_HFYR~0CUWqOVt~T7Gg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Plate Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774752?contentId=Q~ecFKc1IRrWiDqCUIJJMA)
IJUAhsThickness2::Thickness2

Specifies the thickness of the end plate. This is an optional value and a zero value
indicates that no end plates are modeled.


Image:[Alt-Text: Horizontal Traveler - End Plate Attributes - Thickness2 
Image-Analysis: The image depicts a mechanical setup involving a rectangular beam (indicated by the solid lines) with a support (represented by the dashed lines) at one end. The support appears to be a flexible or pivoting type, indicated by the dotted line representation. The arrows imply that there is a force acting on the beam, likely showing its direction. The red dots may indicate points of interest or specific locations of load application or support. This type of diagram is typically used in engineering to analyze forces and moments acting on structural elements. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zxSl7zGUeB1794k7mr8Thg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - End Plate Attributes - Thickness2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zxSl7zGUeB1794k7mr8Thg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the height of the end plate. This is an optional value and a value less
than or equal to zero indicates that no end plates are modeled.


Image:[Alt-Text: Horizontal Traveler - End Plate Attributes - Height2 
Image-Analysis: The image depicts a rectangular shape or box above a smaller, elongated rectangular shape, which appears to be aligned vertically below the larger box. The smaller rectangle, located in the center, has an additional red dot, possibly indicating a focal point or a specific value of interest. There are dashed lines and arrows on the sides, which indicate measurements or dimensions related to the heights of these shapes. This setup suggests a focus on geometry or possibly mechanics, illustrating relationships between different geometric figures, their dimensions, and a specific point of interest within the structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EjysPDI7nj6zGJfIgGJVxg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - End Plate Attributes - Height2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EjysPDI7nj6zGJfIgGJVxg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the width of the end plate. This is an optional value and a value less than
or equal to zero indicates that no end plates are modeled.


Image:[Alt-Text: Horizontal Traveler - End Plate Attributes - Width2 
Image-Analysis: The image depicts a simple schematic representation of two arrows pointing towards a rectangular box from above, indicating an inflow or an incoming resource towards a process or an object represented by the box. Below the box, there is a vertical line descending into a smaller rectangle, which could represent an output or a continuation of the process. The arrows suggest that something is being directed or moved into the box, while the red squares could indicate specific points of interest or variables in this process. The overall layout implies a flow of information or material into a system that may process or transform it. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zK7IG8bOY2kJCozc8RJF5A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - End Plate Attributes - Width2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zK7IG8bOY2kJCozc8RJF5A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Lug Plate - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774756?contentId=FMIiu49tg1AiiyciI6JDWA)
IJUAhsWidth3::Width3

Specifies the width of the lug plate and must be a positive number.

Specifies the thickness of the end plate. This is an optional value, and a zero value
indicates that no end plates are modeled.


Image:[Alt-Text: Horizontal Traveler - Lug Plate Attributes - Width3 
Image-Analysis: The image illustrates a schematic representation of a mechanism or structure involving an upper rectangular component and a lower buttress or connector piece. The upper rectangle is solid, while the lower rectangular section is shown with openings or gaps to imply movement or connection. The central dashed lines indicate alignment or guides, and the arrows on the lower part suggests motion or adjustment capabilities, indicating that the lower section can be adjusted horizontally. The red dots likely signify points of interest or connection points. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b85BPM9Cv_IpAH7~lBjVew-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - Lug Plate Attributes - Width3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/b85BPM9Cv_IpAH7~lBjVew-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight3::Height3

Specifies the height of the lug plate and must be greater than Height2.


Image:[Alt-Text: Horizontal Traveler - End Plate Attributes - Height2 
Image-Analysis: The image appears to depict a schematic representation of a connection between two objects or components. There are directional arrows indicating a vertical flow of information or energy, which suggests a hierarchical or functional relationship. The structure has a rectangular box at the top, which may represent a primary component or system, and a smaller box below that seems to indicate a subordinate or related element connected by a line. The presence of dots and different line styles could imply varying types of connections or data flow between these entities, highlighting interaction patterns or dependencies within a larger system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8DYFwBIT_k0wh1SL1sOIbQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - End Plate Attributes - Height2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8DYFwBIT_k0wh1SL1sOIbQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the lug plate and must be a positive number.


Image:[Image-Analysis: The image represents a simple electronic circuit or system, possibly demonstrating a switch mechanism. At the top, there is a rectangular box, which could symbolize a component like a battery or a power source, indicated by the red dot. Below this component is a vertical line, which appears to represent wires or connections leading to a switch or relay located at the center. The arrows pointing left and right at the bottom suggest that the switch can either connect or disconnect the circuit effectively, controlling the flow of electricity in either direction. This setup may be used in various applications where control over an electrical circuit is necessary. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WQtenxb5TIb72QV5IOTHjQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WQtenxb5TIb72QV5IOTHjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the offset of the hole port from the top of the horizontal traveler.


Image:[Alt-Text: Horizontal Traveler - Lug Plate Attributes - Offset1 
Image-Analysis: The image depicts a diagram representing a hydraulic lift or elevator system. It includes a large rectangular shaded area, indicating the platform that moves vertically. Connected to this platform are two vertical lines, which symbolize the lifting mechanism, likely hydraulic cylinders. The lines also have arrows at the ends, representing the direction of movement, indicating that the platform can be raised or lowered. There is a smaller rectangle at the bottom, suggesting the base or ground level of the lift system, which supports the entire structure. The entire setup symbolizes how hydraulic lifts operate, using fluid pressure to move the platform up and down. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Te8DcIOCmiZw~lZi3g7Onw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - Lug Plate Attributes - Offset1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Te8DcIOCmiZw~lZi3g7Onw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHole1Diameter::Hole1Diameter

Specifies the diameter of the hole port on the lug plate. This property is used by
the part selection rule.

IJUAhsLugEndType:LugEndType

Specifies the end shape of a lug plate using a codelist value.

1 - Round


look for icon that looks like a paint roller: 

2 - Rectangle


Image:[Alt-Text: Horizontal Traveler - Lug Plate Attributes - Lug End Type 2 - Rectangle 
Image-Analysis: The image depicts a schematic representation of a block or a container with an outlet. It features a rectangular box at the top, indicating perhaps a body or main section, with dashed lines suggesting a boundary or limit. Below the rectangular box, there is a smaller rectangular section connected by a straight line, which could represent a conduit or opening. The small red circles at the top and bottom might represent attachment points or indicators. Overall, this design likely signifies a mechanism for the flow of materials or information from the main block to the outlet below. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~kLCvj0YqOfhxfgVgdYMgw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler - Lug Plate Attributes - Lug End Type 2 - Rectangle](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~kLCvj0YqOfhxfgVgdYMgw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774874?contentId=7QUsFhvzBXGkS0YcUCEIhQ)
These properties specify the different port types and their sizes for the horizontal
traveler.


Image:[Alt-Text: Horizontal Traveler SmartPart - LCS 
Image-Analysis: The image depicts a technical diagram with a structure and a hole at the bottom. On the left side, there is a rectangular structure labeled "Structure," which is hollowed out at the bottom where it connects to another smaller rectangle labeled "Hole." This indicates that the hole is a part of the overall structure, likely for functionalities like fastening or drainage. On the right side, the diagram includes an orientation view of the structure showing axes labeled "X" and "Z," with the Z-axis pointing upwards. This suggests a spatial reference for the structure, which is important in three-dimensional modeling or engineering contexts. The overall diagram gives insights into the shape and holes within an engineering component, likely used in manufacturing or construction designs. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9plL5YvczeOQRnxnrmRYiw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Horizontal Traveler SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9plL5YvczeOQRnxnrmRYiw-_PVFQNoCl4XmjAxWO0f7XQ/content)

The bolt SmartPart has two ports, RodEnd1 and RodEnd2. The port RodEnd1 is usually
connected to an external nut, and the port RodEnd2 is connected to an anchor plate
or an existing steel or any other part.

Port details and their orientation

Port1:Structure

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - Steel | N/A  Use -9999 | N/A  Use -9999 | N/A  Use -9999 |

Port2:Hole

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004 - Rod Hole | Hole1Diameter | 0 | Hole1Diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774877?contentId=kCfub7dJt8MN5HtpZlk1Pw)
The BOM description must use the part description.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Insulation - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776354?contentId=TTQRTp2plj65mgzyqN_aNQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Insulation  
Part Name: Insulation  
Part Description: Insulation SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Op5ySkBXueAEHr6kFenZ5w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=35a3b12fa0d6ee78)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Op5ySkBXueAEHr6kFenZ5w-_PVFQNoCl4XmjAxWO0f7XQ/content)

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

To place a sample insulation SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part, and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Insulation > Polyurethane Insulation as shown below:

   
Image:[Image-Analysis: The image presents a hierarchical structure, likely from a software tool or library called "SmartParts." At the top level, there is a category labeled "S3D Standard," which serves as a parent node. Under this category, various subcategories are listed, each represented by a folder icon. These subcategories include "Beam Attachments," "Bolt," "Clevises," "Concrete Lug Plate," "Constant Supports," "Duct Clamp," "Dummy Legs," "Elbow Lugs," "Grip Pipe Clamp," "Guides," "Horizontal Traveler," "Insulation," and a specific item, "Polyurethane Insulation," highlighted with a blue background. This suggests that the focus is on insulation types, with "Polyurethane Insulation" being emphasized among other structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/n~4Jgm5gfjRhR_Qb0bMT7A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/n~4Jgm5gfjRhR_Qb0bMT7A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

ProgID

HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Insulation

Example: S3Dhs\_Insulation sheet in HS\_S3DParts.xls

Local Coordinate System


Image:[Image-Analysis: The image presents a diagrammatic representation of routes in a two-dimensional space. The upper portion illustrates a circular route, labeled "Route," along with three directional indicators: Y pointing to the right, Z pointing downward, and a notable red point in the center. The lower portion depicts a rectangular shape, also labeled "Route," with similar directional indicators, where X points to the right, Z points downward, and the red point maintains its central position. This structure suggests the depiction of routes or pathways in different views, possibly indicating how they function or connect in a spatial manner. It highlights the relationships in directionality (Y, X, and Z) and how they correspond to the depicted routes, suggesting a potential planning or navigation context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/liWY_ZkAzzExZJJB~bspdQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/liWY_ZkAzzExZJJB~bspdQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

When using the Add Part command, the insulation displays in the most frequently used orientation with the
above coordinate system. The route port remains at the origin (0,0,0).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [General Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776355?contentId=YTkpGTNHNEPkVjRA3kgy4g)
IJOAhsPipeOD::PipeOD

Specifies the outside diameter of the pipe to which the insulation is connected. This
value is required and must be greater than zero.


Image:[Image-Analysis: The image depicts a setup to illustrate the relationship between two shapes: a circle and a rectangle. At the top, there is a circle that is surrounded by a larger, empty circle, indicating that the smaller circle is contained within the larger one. Below this, there is a rectangle that appears to have a corresponding point marked in red. The red point in both shapes likely represents a specific location or measurement, emphasizing the connection between the two shapes in terms of their spatial relationship. There are also small arrows suggesting movement or a connection between the top circle and the bottom rectangle. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mx8nb~~_eXdvsTctKGVGhg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mx8nb~~_eXdvsTctKGVGhg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the outer diameter of the insulation. This value is required and must be
greater than zero.


Image:[Image-Analysis: The image depicts two geometric shapes: a circle and a rectangle. The upper portion shows a circle, which is inside two horizontal arrows indicating movement or a relation across the width of the circle, possibly suggesting a function of expansion or compression. This circle is filled with grey, and there is a small red dot at its center, likely indicating a specific point of interest or focus within the circle. Below the circle, there is a rectangle which appears similar in size, and it contains a red dot positioned towards its center as well. This arrangement could imply a comparison or connection between the two shapes, possibly demonstrating different properties or behaviors in a mathematical or physical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PsVtrkFfBuKYGvTOIAYfRA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PsVtrkFfBuKYGvTOIAYfRA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength::Length

Specifies the length of the insulation. This value is required and must be greater
than zero.


Image:[Image-Analysis: The image displays two geometric shapes: a circle above and a rectangle below. The circle is filled with light gray and contains a small red dot centered within it, symbolizing a point of focus or a center of attention. The rectangle is outlined and also contains a small red dot at its center, indicating symmetry or a point of reference. There are horizontal arrows at the bottom of the rectangle, suggesting the presence of movement or measurement along width. These shapes may represent concepts such as focus points in different dimensions (2D vs 1D) and the red dots could symbolize critical points in various applications such as design, physics, or mathematics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u8e1PLA4vQ2s9ED365eE~w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u8e1PLA4vQ2s9ED365eE~w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Cradle/Base Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776356?contentId=9EgFyRG6sjcuxV5n5kfW2A)

None:  The insulation can have a base or cradle. Not all dimensions are required. If a dimension
is blank or equal to zero, the part creates the dimension based on the provided rule.
If no rule is provided, the part ignores the dimension.

IJUAhsWidth1::Width1

Specifies the width of the cradle base. This value is optional. If Width1 is equal to zero, then the base graphics are not included.


Image:[Image-Analysis: The image shows two different views of an object or system. The top part illustrates a top-down view, where a circular shape is depicted with a inner circle, possibly representing a wheel (the larger circle) and an axle or hub (the smaller circle). Below the circular shapes are horizontal lines that indicate the width of the object. The red dot in the center could represent a focal point or reference point for measurement. The bottom part presents a side view, showing a rectangular object that could represent a box or a platform, with the same red dot positioned centrally. This setup suggests a relationship between the components where both the top-down view and side view give complementary information about the dimensions and placement of the object in a physical space, illustrating its geometry clearly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zSD6YavBqg3GZIAC9B64qA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zSD6YavBqg3GZIAC9B64qA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height of the cradle base from the centerline of the pipe. This value
is required. If Width1 is greater than or equal to zero, the software ignores Height1.


Image:[Image-Analysis: The image consists of two parts. The top part features a circular shape with a smaller circle inside it, suggesting a cross-sectional view of a spherical object. A red dot indicates the center, and there are arrows showing vertical movement. This could represent something like a bearing or a spherical bearing housing, highlighting how it rotates or moves vertically. The bottom part displays a rectangular shape, resembling a base or housing with a similar red dot at its center. The arrangement suggests that the top spherical part may fit within this rectangular base. Overall, the image illustrates the relationship between a spherical object and a rectangular housing, possibly in a mechanical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mFrO6lU8u6ciao7eLCbGgg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mFrO6lU8u6ciao7eLCbGgg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of the cradle base. This value is optional. If Width1 is equal to zero, the software ignores Length1. If Width1 is greater than zero and Length1 is equal to zero, then the base length is equal to Length. Otherwise, the base length is equal to Length1.


Image:[Image-Analysis: The image consists of two distinct sections. The top section features a circular object with a shaded inner circle and a small rectangle beneath it. The shaded circle is positioned at the center and has a red dot inside, which emphasizes the central point. This could symbolize a focal point in a system or an object of interest. The bottom section displays a rectangular box, similar to the rectangle above, but it stretches horizontally with red arrows pointing outward. The arrows indicate extension or a range, perhaps suggesting that the box represents a span or area that can be expanded or measured. Overall, this image seems to illustrate concepts of central focus and spatial extension. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iDppPgO2wn13e5PXl8OaaA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iDppPgO2wn13e5PXl8OaaA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Strap Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776357?contentId=xIXK~4NF7xaBD2Zxf3J2Jg)

None:  If the straps are included, then you always have two round straps. The strap graphic
is covered by the base graphic if the base graphic is included. Both straps have the
same dimensions. Not all dimensions are required. If a dimension is blank or equal
to zero, the part creates the dimension based on the provided rule. If no rule is
provided, the part ignores the dimension.

IJUAhsWidth2::Width2

Specifies the width of the straps. This value is optional. If Width2 is equal to zero, then the strap graphics are not included.


Image:[Image-Analysis: {explanation='The image contains two distinct parts. The upper section features a circular diagram with a larger outer circle and a smaller inner circle, both centered around a small red dot. This configuration suggests a concept of layers or levels, likely indicating the relationship between a larger whole and a smaller component within it. The larger circle might represent an overarching system or category, while the smaller circle and the red dot could signify a specific element or focus point within that system. 

The lower section features a rectangular shape divided into smaller segments, creating three vertical sections. Each section contains vertical lines that indicate some form of division or separation, while a red dot appears near the center of one of the segments. The arrows pointing left and right suggest a movement or interaction between these sections. This could infer a connection or comparison between different components within this part of the diagram.

Overall, the image seems to illustrate hierarchical relationships or interactions within two systems: one represented by circles, emphasizing a layered perspective, and another by rectangles, focusing on subdivisions or classifications.'} 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZdAOz6Rs34RyNgpJfBgNXw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZdAOz6Rs34RyNgpJfBgNXw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the straps. This value is optional. If Thickness2 is equal to zero, then the value is ignored. If Width2 is greater than zero and Thickness2 is equal to zero, then the straps are the same diameter as the insulation. If both
Width2 and Thickness2 are greater than zero and there is more than one layer, the software applies the thickness
based on the diameter of the outermost layer as shown below:


Image:[Image-Analysis: The image consists of two distinct sections. The top section presents a circular diagram that illustrates a central point, indicated by a small red dot, surrounded by a larger gray area, suggesting a layered or concentrated focus on a core component situated within a boundary. The arrows may imply movement or directionality, possibly denoting a process or flow within this structured diagram. The bottom section features a rectangular rendering that depicts vertical divisions, showcasing compartmentalization or separation of elements within it. The red dot again emphasizes a focal point, indicating a significant aspect in the composition. Overall, the image represents a relationship between a core element and its environment, along with structured organization in the lower section for clarity and functional arrangement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V6vBsz37SUyodwa3D22mMg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V6vBsz37SUyodwa3D22mMg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset2::Offset2

Specifies the offset from the end of the insulation to the straps. This value is optional.
If Offset2 is equal to zero, then the value is ignored. If there is more than one layer, then
the offset is applied based upon the length of the outermost layer.


Image:[Image-Analysis: The image shows two distinct parts. The top section features a large circle with a smaller shaded circle inside it, indicating a focus point or a target. The red dot within the smaller circle suggests emphasis on that specific area. The bottom section displays a rectangular shape that appears to be a box or a table with four distinct panels, separated by two vertical lines and a horizontal line at the bottom. The horizontal arrows at the bottom suggest movement or interaction with the rectangular shape, possibly indicating expansion or contraction of the box. The red dot in the center highlights an area of interest, connecting it with the functionalities implied by the arrows below, potentially indicating directional actions related to the box. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MEanMETaOEkd5tSPmK2jDw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MEanMETaOEkd5tSPmK2jDw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Insulation Layers Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776358?contentId=CaOsR7~tDVuHRC4s8kBdkQ)

None:  The software adds equally spaced layers using the data below. The insulation layers
do not increase the overall length of the insulation. The outer layers are shorter
than Length. Not all dimensions are required. If a dimension is blank or equal to zero, the part
creates the dimension based on the provided rule. If no rule is provided, the part
ignores the dimension.

IJUAhsLayerQty::LayerQty

Specifies the number of layers to be shown. This value is optional. Valid values are
from 1 to 5. If LayerQty is equal to one, then do not show any additional layers. If LayerQty is greater than one, then add the layers as shown. The diameter of the layers is calculated
using the below function:


None: 


Image:[Image-Analysis: The image displays a simple diagram consisting of two circles at the top and a rectangular shape at the bottom. The upper circle is larger and depicts an outer outline with a smaller, filled circle in the center—likely representing a target or focal point. The small red dot in the center signifies a specific target location within the larger area. Below, the rectangular shape indicates an object or component that is possibly overlapping with some features related to the upper circles. This arrangement suggests a relationship where the top circle might signify a broader context or influence while the bottom rectangle represents a specific entity or function related to the sphere above. The diagram conveys that the circular component plays a pivotal role, targeting or influencing the rectangular aspect below. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LtnlJOlVFpQ8i62VBGt59Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LtnlJOlVFpQ8i62VBGt59Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the offset of the layers from the length of the insulation. This value is
optional. If LayerQty is equal to one, then this value is ignored. If LayerQty is greater than one, then each layer is an inset by the same offset from the previous
layer. The layer closest to the pipe contains length = Length. Subsequent layers contains their length calculated using the below function:


None: 


Image:[Image-Analysis: The image depicts a diagram related to a mechanical or electrical system. At the top, there's a circular diagram representing a motor with a smaller circle in the center, which likely indicates a rotor or a magnetic component. The larger circle suggests the stator, which is the stationary part of the motor. Below this circular diagram, there are rectangular blocks representing the housing or casing of the motor and additional components connected to it. The arrows on the left and the right might indicate the flow of energy or movement direction. Overall, the image illustrates the structure and basic functioning principles of a motor system, highlighting the relationship between the stator and rotor. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjUPVHInu71FJDtSJZi25w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IjUPVHInu71FJDtSJZi25w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/776359?contentId=RA1GCfW4~2hXC~eIvvY8vw)
These properties specify the different port types and their sizes for the insulation.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KF6A7QljvlmT1EOG6eKczw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7847c327b67e0a65)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KF6A7QljvlmT1EOG6eKczw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bcxn7voPwxJb8NGGlxTKqg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=17df2af23a7e7783)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bcxn7voPwxJb8NGGlxTKqg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 – Route (0, 0, 0)

To connect easily to pipe, the X axis of the route port should be aligned along the
length of the insulation. The Z axis should be pointing in the downward direction.

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Minimum Size | Maximum Size |
| 2-Route | PipeOD | PipeOD | PipeOD |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Malleable Beam Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337188?contentId=s4FrC1w1HIWj9m02zlUn9Q)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Malleable  
Part Name: Malleable Beam Clamp  
Part Description: Malleable Beam Clamp SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOByxs_ToaaKcksNApNPrw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a04b70974e963f95)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LOByxs_ToaaKcksNApNPrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Malleable Beam Clamp SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Beam Attachments > Malleable Beam Clamp as shown below.

   
Image:[Image-Analysis: The image depicts a hierarchical structure of categories and subcategories, likely from a software interface related to a product or engineering designs. At the top level, there is a main category labeled "SmartParts," followed by a subcategory named "S30 Standard." Under "S30 Standard," there is a primary section titled "Beam Attachments," which includes various types of beam attachment elements. Among them, "Malleable Beam Clamp" is highlighted, indicating it may be the currently selected item. Other attachments listed under "Beam Attachments" include "Beam Clamp," "Welded Beam Attachment Bolt/PIN - Eye Connection," and "Welded Beam Attachment - Inverted - Rod Connection in Hole." Further sections include "Clevises" and "Constant Supports," suggesting additional categories related to structural components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G87nJ0L1hUNxlXsEn7n10A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G87nJ0L1hUNxlXsEn7n10A-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a mechanical system involving pulleys and a ring. There are three key components outlined: the upper structure, which includes a pulley system, the horizontal surface underneath, and the ring element. The system appears to be designed to demonstrate forces acting on the ring. Two red arrows are marked: one indicated as "Y," pointing to the right on the horizontal plane, and the other indicated as "Z," pointing downward, suggesting these arrows represent force directions or tension paths in the system. The relationship between them suggests an interaction of forces in a mechanical context, likely showing how load is distributed or how tension operates within this setup. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o5Wgp7a4iNsJFl1h3mDcmg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/o5Wgp7a4iNsJFl1h3mDcmg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Selection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337195?contentId=tqKvJH9_A6DAcfpIIuT~Kg)
These properties are used for part selection rule and BOM for malleable beam clamp.

IJUAhsSize::Size

A string specifying the size of the clamp that may be used in part selection rules
to select the appropriate malleable beam clamp. This property may be used in reporting
BOMs.

IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of the rod that attaches to the beam clamp. The rod
is not included in the Beam Clamp’s graphics. This does not affect the graphics and
is used by Part Selection Rules for choosing a malleable beam clamp.


Image:[Image-Analysis: The image illustrates a mechanism that resembles a tension or lifting device. It consists of a horizontal bar supported by two curved guides on either end. These guides suggest the motion of the bar being able to move vertically or horizontally. Below the horizontal bar, there is a box-like component that appears to be adjustable, possibly allowing for tension control. The two arrows at the bottom indicate that the distance between two points can be adjusted or that there is a force being applied from those points. The dashed lines suggest that there could be potential movement or adjustment not visible within the solid lines, indicating a schematic rather than an actual physical depiction. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/op7ty1Xtt6oJ2tcXrO_P6A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/op7ty1Xtt6oJ2tcXrO_P6A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Malleable Beam Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337196?contentId=UmBiM0Y4Qzn7EuGUzDpdWw)
These properties define the geometry of the malleable beam clamp.

IJUAhsMalleableClamp::MalleableConfig

Specifies the malleable beam clamp configuration to show if the clamp has nut, eyenut,
or no rod attachment. It uses the hsMalleableConfig codelist.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ulv_00ytQbQKoO5_vQt9UQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=631b5b9461264cd0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ulv_00ytQbQKoO5_vQt9UQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMalleableClamp::TopWidth

Specifies the top width of malleable beam clamp from starting of flange till the inner
malleable clamp touches the flange. This is a double value. This value must be positive.
If the TopWidth value is not specified, then an error is thrown.


Image:[Image-Analysis: The image illustrates a simplified schematic of a mechanical device that suggests a type of pressure or mechanical system involving a central vertical component and two symmetrical horizontal components. The image visually represents an object that may be involved in compressing or moving materials, characterized by the distinctive arrows indicating movement or force direction. The arrows on the sides may represent the lateral movement or adjustment mechanisms, indicating the flexibility or capability of the device to adapt to different conditions. This diagram often depicts industrial machinery or mechanisms in manufacturing contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RiNlCJTpfIjFQrI9MrKwvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RiNlCJTpfIjFQrI9MrKwvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMalleableClamp::Depth

Specifies the depth of the beam clamp. This value must be positive. If the depth value is not specified, then an error is thrown.


Image:[Image-Analysis: The image depicts a simple circuit diagram showing two capacitors connected in parallel. There are two vertical lines that represent the capacitors; each has a positive terminal (indicated by arrows pointing upwards) and a negative terminal (indicated by arrows pointing downwards). The parallel connection is represented by horizontal lines connecting the two capacitors at their respective terminals, suggesting that these components share the same voltage across them while allowing for greater overall capacitance in the circuit. This configuration is commonly used in electrical engineering to store and manage electrical charge. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7b3PRK3gorqr~BQXNo1ytg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7b3PRK3gorqr~BQXNo1ytg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMalleableClamp::Thickness

Specifies the thickness of the clamp. This value must be positive. If the Thickness value is not specified, then an error is thrown.


Image:[Image-Analysis: The image depicts a mechanical part involving a roller and a guiding mechanism. There are two circular elements which resemble rollers on either side, indicating that they may be used to guide something that passes between them. The central part, which looks like a rectangular or square section, is likely the main component that is being supported or moved. The arrows suggest direction, indicating that there is motion involved or an action taking place, such as pressing or guiding an object through the central space. This setup is commonly used in machinery to facilitate the movement of materials or components while ensuring they are directed properly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hUpiXDTL3rPuy2cSZJFMAA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hUpiXDTL3rPuy2cSZJFMAA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodTakeOut::RodTakeOut

Specifies the distance between the flange surface to starting of nut/eyenut surface. This is a double value
and must be greater than zero.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~MA~fDg2olBUWg8gERmS2A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=91edcea75e4e4755)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~MA~fDg2olBUWg8gERmS2A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMalleableClamp::NutShape

String specifying the name of the nut shape. NutShape value is optional. If this value
is specified, then nut shape is added to the malleable beam clamp.


Image:[Image-Analysis: The image depicts a simple mechanical balance scale. It consists of a horizontal beam supported at its center, with two pans hanging from either end. The central support point allows the beam to pivot, which is essential for comparing weights. The pans or trays are used to hold objects or weights that need to be compared against each other. The image likely illustrates the fundamental principle of balance, where equal weights on both sides will keep the beam level, indicating equilibrium. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WhCvQLtt~X0_wMEym367lQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WhCvQLtt~X0_wMEym367lQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMalleableClamp::EyeNutShape

String specifying the name of the eyenut shape. EyeNutShape value is optional. If
this value is specified, then eyenut shape is added to the malleable beam clamp.


Image:[Image-Analysis: The image depicts a mechanical component, likely a type of fixture or a part of a machine that is used in various engineering applications. The top view illustrates how different elements, such as a clamp, support arms, and a central guide, are arranged. The lines represent the symmetry and the intended paths for adjustment or movement within the device. The central part appears to be designed to offer stability, with the adjustable arms suggesting it may be used to hold or guide objects in place. This assembly could be useful in manufacturing processes or mechanical setups where precise positioning is necessary. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~7oubTEA9ZhC2SZtus95zA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~7oubTEA9ZhC2SZtus95zA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsAngle1::Angle1

Specifies the angle between the structure center line and eyenut shape. It is used
for sloped steel configuration. Both positive and negative values are accepted. This
is applicable only for malleable configuration with eyenut. If the value specified
for configuration is other than eyenut, then the angle will be ignored and the graphics
are not updated.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KrE2ufmtocY8rzmrN9FjdQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=468e0e4ae062f4f2)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/KrE2ufmtocY8rzmrN9FjdQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOverLength1::OverLength1

Specifies the amount that the rod extends past the threaded base of nut/eyenut. This
value is used to ensure that rod take-out calculations are correct.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/d9XBw1KbqxkFp9HKk6RYgA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5c95e041ce845b88)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/d9XBw1KbqxkFp9HKk6RYgA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337199?contentId=Vxs0Z5EQjAqK7Uk078q7Pg)
These properties are used to create top and bottom pin for the malleable beam clamp.

IJUAhsPin1::Pin1Length

Specifies the length of the inner rod which comes along with the malleable beam clamp.
If Pin1Length value is not specified, then the pin is drawn.

If Pin1Length value is less than StructWidth+2\*Thickness, then a warning message is displayed and the value is reset to StructWidth+4\*Thickness.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the inner rod which comes along with the malleable beam clamp. If Pin1Diameter value is not specified, then the pin is not drawn.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ohVgwK_oB5_NEGRLYOHpEA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=31945a0d7fae83c4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ohVgwK_oB5_NEGRLYOHpEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin2::Pin2Diameter

Specifies the diameter of the pin. This value must be less than the thickness of the
clamp. Else, a warning message is displayed. If Pin2Diameter value is not specified, then the pin is not drawn.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ffs3F73ytsGqez7ZdmHDZw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=41a93d878b3fd832)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ffs3F73ytsGqez7ZdmHDZw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPin2::Pin2Length

Specifies the length of the pin. This value must be greater than the depth of the
clamp. Else, a warning message is displayed. If Pin2Length value is not specified, then the pin is not drawn.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3An23qXqIkx~eWNNCNE3Ag-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a824f0619a9719a5)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3An23qXqIkx~eWNNCNE3Ag-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [User Prompts - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337428?contentId=mkPQuge5XyWOKv5CSC2MJw)
These are the occurrence properties.

IJOAhsClampThick::ClampThickness

Specifies the thickness of the flange. If no value is specified for ClampThickness, an error is thrown.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hFOugiS9nPxFJVveC~vZrw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9f1e5e40f68d4987)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hFOugiS9nPxFJVveC~vZrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsStructWidth::StructWidth

Specifies the width of the flange. If no value is specified for StrcutWidth, an error is thrown.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G~sUD3ovrvGOwL3XrkiLRg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b9a11af8eeb8c6cb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/G~sUD3ovrvGOwL3XrkiLRg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/337431?contentId=izZDKHJ74ES6zFBj6bwyvQ)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2a8kVcA7GhwizHR2moUfcQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1904fff1f2437d3b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2a8kVcA7GhwizHR2moUfcQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Structure Port

Port1 is a Structure Port located at 0, 0, 0. For this symbol, it is a local co-ordinate
system.

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1011 - Steel | 0 | -9999 | 9999 |

Rod End Port


Image:[Image-Analysis: The image depicts a mechanical system, likely a representation of a pulley or suspension mechanism. It shows a horizontal platform from which a vertical shaft descends. This shaft connects to a loop or eye at the bottom, and the system is supported by two curved structures on the sides, which suggest bearings or supports. The image details three axes: Y, Z, and a vertical axis, which could represent different directions of movement or forces acting on the system. The red arrows indicate the directions along the Y and Z axes, suggesting how forces may be distributed or how the system may rotate or swing. This setup may be relevant for understanding mechanics in structures, forces in equilibrium, or dynamics in machinery. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qWiHwJ28WN7v1RxdVddkrw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qWiHwJ28WN7v1RxdVddkrw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port2 - RodEnd Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1000 - External Thread, RH  1002 - External Thread, LH | RodDiameter | RodDiameter | RodDiameter |

Pin Port


Image:[Image-Analysis: The image depicts a mechanical system that likely represents a type of pulley or a motion guide. It features a central vertical support through which a pin or shaft appears to be connected to a pulley system. The pulley sits atop a horizontal bar, with arcs on either side suggesting rotational movement or tension applied through ropes or cables on the left and right sides. The red arrows labeled "Z" suggest a directional force or movement indicative of tension applied in the horizontal direction within the system. This setup could be a part of a larger study on mechanics, force transmission, or motion dynamics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UZjjwcnbp_Ht~tQ2Ucx4nQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UZjjwcnbp_Ht~tQ2Ucx4nQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 3 - Pin Port

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1005 - Pin | Pin2Diameter | Pin2Diameter | Pin2Diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307404?contentId=6cZIMLe0Po~Z8sul2y2WxQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Nut  
Part Name: Nut  
Part Description: Nut SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8AU2ZgDomVn3ZaTt5Uqtkw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2b7db9fc21c9fd92)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8AU2ZgDomVn3ZaTt5Uqtkw-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Nut SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog, select a part from Parts > SmartParts > S3D Standard > Miscellaneous > Nuts > Hex Nut as shown below.

   
Image:[Image-Analysis: The image displays a hierarchical structure or a tree diagram representing categories and subcategories of various components related to SmartParts and the S3D Standard. At the top level, there are two main categories: "SmartParts" and "S3D Standard." Under "S3D Standard," there are multiple subcategories including "Beam Attachments," "Clevises," "Miscellaneous," and "Bolts." Within the "Bolts" category, there is a subcategory labeled "Nuts," which includes a highlighted specific item called "Hex Nut." Other categories under "S3D Standard" include "Welds," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Struts," and "U-Bolts." This structure provides an organized way to navigate the types of parts available for engineering or construction purposes, indicating the relationships between general categories and specific items. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j_zLo79A_7VwcOgyNRnFag-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/j_zLo79A_7VwcOgyNRnFag-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as point highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image shows a rectangular shape with labeled axes. The rectangle has coordinates indicated at the Top and Bottom: Top: 0,0, Shape1Length and Bottom: 0,0,0. The axes are labeled X and Z, where X is represented as a horizontal line with an arrow pointing to the right, while Z is a vertical line with an arrow pointing upwards. This likely represents a coordinate system that could be used for graphical or mathematical representation, indicating a location in a three-dimensional space where X is horizontal and Z is vertical. The image may be relevant in contexts such as computer graphics, physics, or engineering, where understanding spatial orientation is important. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/seXGlpQIVtLbnMDVRliaZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/seXGlpQIVtLbnMDVRliaZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Nut Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307409?contentId=qIMWpQYZoJ75WzC8aHwLsw)
These properties define the geometry of the Nut.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of the dimensional value to use inches (for example 10in).

IJUAhsRodDiameter::RodDiameter

Specifies the outside diameter of the rod that attaches to the nut. This value is
only used by the Part Selection Rule for choosing the correct Nut part. The rod is
not included in the graphics.


None: 

IJUAhsShape1::Shape1Type

Specifies the graphic shape used for the nut or washer. This value uses the codelist
number defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.


Image:[Image-Analysis: The image contains three distinct geometric shapes with corresponding labels. The first shape is a circle, labeled as "1 - Round." The second shape is a square, labeled as "2 - Square." The third shape is a hexagon, labeled as "3 - Hex." Each shape has a center point indicated by a small dot, which serves as a visual reference. This image likely illustrates basic geometric shapes for educational or identification purposes, each with a unique identifier (number and name) that can be used in different contexts such as mathematics or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FRYnSihJekj6uKJ0_uflTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FRYnSihJekj6uKJ0_uflTA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the nut or washer.


Image:[Image-Analysis: The image displays three different geometric shapes, each represented with a corresponding label and visual depiction. The shapes shown are: 1) A round shape (circle) labeled as "1 - Round", which is depicted with a circular outline and a dot in the center; 2) A square shape labeled as "2 - Square", which has a square outline also with a dot in the center; 3) A hexagonal shape labeled as "3 - Hex", illustrated with a hexagon outline and a central dot. The image is likely meant to communicate the differences between these basic geometric forms for educational or reference purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MbmFpjB_bdFcZ3FfDsND0w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MbmFpjB_bdFcZ3FfDsND0w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Image-Analysis: The image presents three different shapes: a round shape, a square shape, and a hexagon shape. Each shape is labeled with a number indicating its order and an accompanying description. The first shape (1) is a round circle, noted as "Round," and it is accompanied by double horizontal arrows indicating its diameter. The second shape (2) is a square, described as "Square," also featuring arrows that suggest its width. The third shape (3) is a hexagon labeled "Hex," which is noted to have "No effect," suggesting it does not influence the context compared to the other shapes. This hierarchical presentation may imply a comparison of the shapes in terms of their geometric properties or their effects in a given context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wAIFwuC0ju26c82SkTjLUg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wAIFwuC0ju26c82SkTjLUg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShape1::Shape1Length

Specifies the length of the nut or washer.


Image:[Image-Analysis: The image depicts a simple schematic representation likely related to a mechanical or electronic switch mechanism. At the top, there are two arrows indicating movement or flow, suggesting that something can move in or out. Below the arrows, there is a box-like structure with two red squares (possibly buttons or indicators) at the bottom, highlighting an action or state change. The design suggests an interface where input (indicated by the arrows) interacts with an output (represented by the box with red squares), potentially in a control or signaling context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4slgzVAtUDpZzxl_P9Oqkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4slgzVAtUDpZzxl_P9Oqkg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307415?contentId=FxU~Tz~qoc6dmm9kgLIb8w)
These properties define the different Nut port types and their sizes.


Image:[Image-Analysis: The image displays a comparison between two ports, labeled as Port 1 (Top) and Port 2 (Bottom). Each port is represented in a structured format with several attributes outlined for each. For Port 1, the attributes include Name, PortType, MinSize, MaxSize, and UnitType, all related to HgrSymbolPort(1). Conversely, Port 2 contains similar attributes (Name, PortType, MinSize, MaxSize, and UnitType) related to HgrSymbolPort(2). The layout suggests that both ports have identical types of attributes, providing a clear and direct comparison between the two. The organization is color-coded, with Port 1 highlighted in green and Port 2 in pink, which aids in distinguishing between the two ports visually. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q7DxFpyeqThD547LQO2phg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q7DxFpyeqThD547LQO2phg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port 1 - Top

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 – IntThdRH    1003 – InThdLH    1004 – Rod Hole | Not applicable for this port type.  Use the distance that the threaded rod penetrates into the nut (Shape1Length). If hole is not completely through nut, then use the depth of the hole. | Enter the smallest rod or bolt size that can be connected to this port.  Use same value as RodDiameter attribute for threaded nuts. | Enter the largest rod or bolt size that can be connected to this port.  Use same value as RodDiameter attribute for threaded nuts. |

Port 1 - Bottom

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 – IntThdRH    1003 – IntThdLH    1004 – Rod Hole | Not applicable for this port type.  Use the distance that the threaded rod penetrates into the nut (Shape1Length). If hole is not completely through nut, then use the depth of the hole. | Enter the smallest rod or bolt size that can be connected to this port.  Use same value as RodDiameter attribute for threaded nuts. | Enter the largest rod or bolt size that can be connected to this port.  Use same value as RodDiameter attribute for threaded nuts. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pin - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307066?contentId=9AY5_qMVSMOC0b_23q_8Bw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Pin  
Part Name: Pin  
Part Description: Pin SmartPart

![1)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O~Lg3SAHf4H2BK4XAlE56A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1a2c791d7be998d8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O~Lg3SAHf4H2BK4XAlE56A-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Pin SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Miscellaneous > Pins > Pin with Cotter Pins as shown in the following example:

   ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FFb6SfeIITPtMBpscaXCBQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7e2699237735da63)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FFb6SfeIITPtMBpscaXCBQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image illustrates a 3D coordinate system along with a representation of a pin located at the origin point (0, 0, 0). The pin is shown as a red dot within a gray circle, indicating its position in space. The axes of the coordinate system are labeled: the x-axis is horizontal, extending to the right, and the z-axis is vertical, pointing upwards. The arrangement suggests that the pin is at the intersection of these axes, serving as a reference point in the 3D space defined by the x, y, and z coordinates. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EVGBfcrEXaoenXTnaeGIEg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EVGBfcrEXaoenXTnaeGIEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

These properties define the geometry of the Pin.

IJUAhsPin1::Pin1Diameter

Specifies the diameter of the Pin. This value cannot be set to 0.


None: 

IJUAhsPin1::Pin1Length

Specifies the length of the Pin. This value cannot be set to 0.


Image:[Alt-Text: Pin1Length 
Image-Analysis: The image depicts a technical diagram possibly related to an engineering or manufacturing process. It includes a rectangular object on the left with two arrows pointing vertically, suggesting measurement along the height, labeled "Pin1Length," indicating that this length is significant in the context. To the right, there is a circular shape with a smaller rectangle under it, possibly representing a pin or a connector. The circular object is labeled with a dashed line beneath it, which may indicate its base or bottom view. The overall layout suggests a focus on the dimensions and specifications of parts in a mechanical assembly or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RV3ye3QJjZ9IS1pETk~04Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Pin1Length](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RV3ye3QJjZ9IS1pETk~04Q-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Cotter Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307096?contentId=HszhgaxEC9fayudFwRu56Q)
IJUAhsCotter1::CotterDia

Specifies the diameter of the cotter pin. This value cannot be zero.


Image:[Alt-Text: CotterDiameter 
Image-Analysis: The image is a technical diagram depicting a cotter pin mechanism. At the top, there is a vertical rectangular component with arrows indicating a direction, possibly showing the application of force or movement. Below this rectangle, a circular icon is displayed, which likely represents a hole or anchor point where the cotter pin would be inserted. Below it, the word "CotterDia" indicates that this is referring to the diameter or specifications of the cotter pin being described. Overall, the image visually communicates the relationship and interaction between the various components within the context of a cotter pin usage or installation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Txpyz5nRw3duvaVBvFkZzQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![CotterDiameter](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Txpyz5nRw3duvaVBvFkZzQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCotter1::CotterLength

Specifies the length of the cotter pin. This value cannot be zero.


Image:[Alt-Text: CotterLength 
Image-Analysis: The image illustrates a mechanical component labeled "CotterLength." It shows a vertical rectangular shape at the top, which likely represents a part of a fastening mechanism. Below it, there is a circular shape denoting a cotter pin or a similar fastener, indicated by the dimensions pointing up and down with arrows, suggesting a measurement or specification for its length. The connection between the two shapes emphasizes that the CotterLength measurement pertains to this fastening component, indicating its critical role in assembly or mechanical applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7sr3Ui9oblmRKW88u8GAiQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![CotterLength](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7sr3Ui9oblmRKW88u8GAiQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCotter1::CotterOffset

Specifies the distance between cotter pin center and pin edge.


Image:[Alt-Text: CotterOffset 
Image-Analysis: The image depicts a technical drawing that includes a vertical rectangular shape at the top, labeled as "CotterOffset." Below the rectangle, there is a circular shape with a smaller rectangle at the top connected to it. The drawing features dashed lines indicating measurements or offsets related to the "CotterOffset." The visual elements suggest a mechanical or engineering context, possibly related to the positioning of cotter pins or similar hardware components. The circular part may represent a pivot or attachment point in the assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J3vtL2Os6GdwgurO6g49PQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![CotterOffset](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J3vtL2Os6GdwgurO6g49PQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/307106?contentId=lGrhKUEobN9uA_H3Hq9xSQ)
These properties are used to specify the different port types and their sizes for
the pin.


Image:[Image-Analysis: The image presents a structured representation of a hardware port, specifically "Port 1," detailed through various attributes listed vertically. Each attribute relates to the characteristics of this port: \n- HgrSymbolPort(1):Name indicates the name of the port. \n- HgrSymbolPort(1):PortType describes the type of the port. \n- HgrSymbolPort(1):Size specifies the size of the port. \n- HgrSymbolPort(1):MinSize and HgrSymbolPort(1):MaxSize provide the minimum and maximum sizes the port can accommodate. \n- HgrSymbolPort(1):UnitType identifies the measurement unit for size specifications. \nThis organization aids in understanding the functionalities and specifications associated with the particular port. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RPkfhDMYgJN6HwJ3yupn7Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RPkfhDMYgJN6HwJ3yupn7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Pin


Image:[Alt-Text: Port1 Pin 
Image-Analysis: The image illustrates a rectangular object with two circular elements positioned at its top and bottom, with a small red square in the center. Below this rectangular object, there is a horizontal dashed line and an accompanying coordinate system labeled with the axes X and Z. The Z-axis is represented by a vertical line through the rectangular object, while the X-axis is shown pointing horizontally. This suggests a three-dimensional representation where the rectangular object is positioned within a 3D space, possibly indicating its orientation relative to the X and Z axes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u9e6k2fmXlR9XCeftPwnMw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Port1 Pin](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u9e6k2fmXlR9XCeftPwnMw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1:Pin

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1005 - Pin | Pin1Diameter | 0 | Pin1Diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pipe Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306580?contentId=WtpiwEbW6cR24x~fw6WgAw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PipeClamp  
Part Name: Pipe Clamp  
Part Description: Pipe Clamp SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mkotCbY6y_rutv95DX~iXg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8e8fd057c1ed4399)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mkotCbY6y_rutv95DX~iXg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Pipe Clamp SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part command, and then select the design support.
4. In the Select Part dialog, select a part from Parts > SmartParts > S3D Standard > Pipe Clamps as shown below.

   
Image:[Image-Analysis: The image represents a hierarchical structure, likely from a software interface or a folder organization, showing various categories of components related to "SmartParts." At the top level, there is the "S3D Standard" category, which further branches into subcategories like "Beam Attachments," "Clevises," "Miscellaneous," and "Pipe Clamps." The "Pipe Clamps" category is highlighted, indicating it may be a focal point or that it is currently selected. Below these, additional subcategories include "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Struts," and "U-Bolts," which represent different types or families of parts that can be found within the SmartParts library. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sUy0e3nCr606cA3xfMqAqQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sUy0e3nCr606cA3xfMqAqQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a technical drawing related to a pipe system. On the left side, there is a circular diagram of a pipe with a swirling flow indicated in the center, suggesting fluid movement or rotation within the pipe. To the right, there is a vertical representation of a pipe structure accompanied by a set of axis indicators labeled X and Z. Additionally, there is a notation below the diagram stating "Pipe: 0,0,0," which likely references the coordinates or parameters related to the positioning or dimensions of the pipe system. Overall, the image communicates information pertinent to understanding the flow and structural attributes of the pipe in a technical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rwDjuxu8WZVYU4R~T~FFpw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rwDjuxu8WZVYU4R~T~FFpw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306603?contentId=azgO~Dc3HmvaIcypNsB~fQ)
These properties define the geometry of the pipe clamp body.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of the dimensional value to use inches (for example 10in).

IJUAhsDiameter1::Diameter1

Specifies the inside diameter of the pipe clamp body. It is the same as the outside
diameter of the pipe.


Image:[Image-Analysis: The image depicts a technical illustration of a circular component with a labeled measurement. It shows a circular shape (likely a pipe, bearing, or similar mechanical part) with some internal structure indicated by the red dots within the circular section. The label "Diameter1" points to the measurement of the diameter of this circular component. It also features two vertical lines on either side, which suggests that it is part of a larger assembly, perhaps indicating the connections to other parts. This implies a relationship where this component fits into a system that may require specific diameter specifications for compatibility with other components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~ffo~3gAry6g0KCHrA_~xA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~ffo~3gAry6g0KCHrA_~xA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of stock, which is used to make the pipe clamp body. It also
specifies the thickness of the top and bottom tabs.


Image:[Image-Analysis: The image shows a circular object that represents a component, likely in a mechanical or engineering context. There are red dots that probably indicate important features or connection points on the component. Two arrows point upward and downward, suggesting a measurement for the object’s thickness, with the label "Thickness1" next to it. This indicates a specific parameter important for the design or analysis of the component. The overall layout implies that the component might interact with other parts, with the thickness measurement being crucial for ensuring proper fit and function within a larger assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y0xHB0aPjWCAfbUx4lNCAg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y0xHB0aPjWCAfbUx4lNCAg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsInsulationThickness::InsulationThickness

Specifies the insulation thickness of the stock, which is used to make the pipe clamp
body.

IJUAhsWidth1::Width1

Specifies the width of the clamp body. In general, both the left and right halves
of the clamp are of the same width, unless Width2 is specified. If Width1 is negative, the left half of the clamp is not displayed. Width1 cannot be zero or undefined.


Image:[Image-Analysis: The image depicts a mechanical or electrical diagram featuring two components. On the left, there is a circular element labeled with "L" and "R," which likely represents a part with left (L) and right (R) designations, possibly referring to orientation or functionality in a system. Inside the circle, there are red dots, which may indicate points of interest or connections. To the right of this circular element is a rectangular component labeled "Width1." This component appears to have an adjustable or fixed width based on the diagram, connected by arrows that suggest a relationship between the circular and rectangular elements. Overall, this image illustrates a specific structural or functional relationship between these two components, possibly in a mechanical or electrical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0yifj00bt1PuguyF6YZx6A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0yifj00bt1PuguyF6YZx6A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the second width of the clamp body. It is the optional width. Both halves
of the clamp are of the same width if Width2 is zero. Both halves of the clamp are of different widths if Width2 is specified with a reasonable value. The right half of the clamp is not shown if
Width2 is negative. Width2 is ignored when Angle1 is set to 360-degrees.


Image:[Image-Analysis: The image illustrates a technical diagram involving a circular component on the left and a rectangular component on the right. The circular component appears to represent switches or connections labeled "L" and "R," indicating left and right, possibly referring to directional flow or orientation. Inside the circle, there is a red dot central to its design, which may symbolize a point of operation or control. The rectangular component is labeled with the word "Width2," suggesting a dimension related to its size or configuration. Arrows indicate a relationship between the circular component and the rectangular component, possibly showing the direction of movement or connection between the two. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dWzVEe4~~XH109hRj2cjsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dWzVEe4~~XH109hRj2cjsg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height from pipe center to top of clamp. The value of Height1 cannot be zero or less than the outside diameter of the clamp body.


Image:[Image-Analysis: The image depicts a mechanical drawing that includes a circular component with inner details, indicated by a spiral or wave pattern inside. Surrounding this circular component are horizontal lines that suggest measurement. An arrow points upwards next to the text "Height1," indicating that this term refers to a specific vertical measurement from the lowest point to the highest point of the circular part. To the right of the circular section is a vertical rectangular shape, likely representing a housing or casing for the circular component. Overall, the image illustrates a mechanical part and its dimensions, highlighting the importance of the specified height in relation to the component's design or placement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mlBYZsipMPnqfaplWT0xKg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mlBYZsipMPnqfaplWT0xKg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the height from pipe center to the bottom of the clamp. The value of Height2 cannot be zero or less than the outside diameter of clamp body. It is ignored when
Angle1 is set to 360-degrees.


Image:[Image-Analysis: The image depicts a technical diagram that includes a circular component on the left featuring a spiral shape inside and two red points, which may represent connection points or electrical contacts. Next to it, there is an arrow pointing to the word "Height2," indicating a measurement related to the component's dimensions. On the right side, there’s a rectangular shape with a circular opening at the top and bottom, likely depicting another component that is connected to the circular part. The diagram focuses on the relationships between these parts, highlighting measurements and alignment aspects crucial in engineering designs. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AGf5mlNLWv5uP2aMaJPsVQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AGf5mlNLWv5uP2aMaJPsVQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap1::Gap1

Specifies the gap between the two top tabs. This value is always greater than or equal
to zero.


Image:[Image-Analysis: The image depicts a schematic representation of a component called "Gap1." It features a central circular section with a marked area that likely indicates a gap or space, typically related to electromagnetic or electronic devices. The component has connections illustrated by lines extending to the left and right, suggesting how it interfaces with other components in a circuit. The red elements might represent specific points of interest, such as connections or indicators within the component. This type of diagram is common in technical fields like electronics or engineering, where visual representation helps in understanding the functionality and layout of components in a system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qPV8tSc8XZK_A7QhWLRF7A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qPV8tSc8XZK_A7QhWLRF7A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGap2::Gap2

Specifies the gap between the two bottom tabs. This value is always greater than or
equal to zero. It is ignored when Angle1 is set to 360-degrees.


Image:[Image-Analysis: The image depicts a circuit component, likely a coil or inductor, identified with the label "Gap2" at the bottom. It features a circular design with a central area that appears to be the gap in the coil, indicated by the red dots which could represent specific points of interest or connections. The two vertical lines at the top and bottom could symbolize connections to other circuit elements. The overall schematic shows the flow of current or magnetic lines of force through the component, emphasizing its role in the circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6UyeUru0qqNY4CpugbjZ4g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6UyeUru0qqNY4CpugbjZ4g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle1::Angle1

Specifies the sweep angle between the top and bottom tabs. When Angle1 is set to 360-degrees, only the left half of the clamp is displayed and Gap1 is used for the tab space. In this case, the pipe clamp looks like this:


look for icon that resembles a stopwatch or timer with circular lines and a small red dot, indicative of a timing mechanism or countdown: 


Image:[Image-Analysis: The image depicts a mechanical element that can be related to rotational motion or hydraulic systems. It shows a round component labeled with the term "Angle1", which suggests it may be measuring or indicating an angle of rotation. The orientation arrows indicate a rotational direction with the labels "L" (Left) and "R" (Right), possibly signifying the movement directions or positions of certain components. There are also two points marked as "1" and "2", which could represent specific locations, reference points, or perhaps the positions of actuators, sensors, or connectors associated with this angular measurement or adjustment system. This setup seems to be a simplified schematic for conveying rotational angles or movements in mechanical assemblies or hydraulic systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNm6p8yWrnM9oAoNEPvw7A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNm6p8yWrnM9oAoNEPvw7A-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306633?contentId=3P3rfyQ~As33rHumRO86Ow)
These properties are used to set the bolt quantities and their positions.

IJUAhsPin1::Pin1Diameter

Specifies the pin diameter for all bolts.

IJUAhsPin1::Pin1Length

Specifies the pin length for all bolts. In general, Pin1Length is greater than larger of Gap1 + 2 \* Thickness1, or Gap2 + 2 \* Thickness1 to be visible.


Image:[Image-Analysis: The image illustrates a technical diagram showing a pin and its measurements. To the left, it labels two dimensions: "Pin1Diameter," which indicates the diameter of a pin, and "Pin1Length," which indicates the length of that pin. The pin itself is depicted in a circular form with a red dot, possibly indicating a feature or reference point on the pin. To the right, there is a simple line drawing of a component that may represent a connection point or housing for the pin, which also suggests there is a slot for the pin to be inserted. The diagram is likely used in a technical context, such as electronics or mechanical engineering, for referencing the specifications of a pin used in a device or assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZUyubJbH9zyp~GJNMeZcwA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZUyubJbH9zyp~GJNMeZcwA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Row Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306636?contentId=HwVofSVJujo0LLWJB5dnTQ)
Six rows of bolts are allowed for pipe clamp. Each row consists of different offset
distance from the pipe centerline and a different quantity of bolts in the row.

Bolts can be of different configurations and spacing in the row. All of the bolts
are drawn with the same size, Pin1Diameter x Pin1Length.


Image:[Image-Analysis: The image displays a diagram illustrating a switching system with two main components: a rotary switch and a representation of connections on a board. On the left side, the rotary switch is shown with a circular center labeled "L" and "R" representing left and right positions respectively. The numbers 1 through 6 are indicated along the vertical lines, possibly suggesting different positions or settings of the switch. These numbers may correspond to specific functions or circuits engaged when the switch is turned. The right side displays a grid layout with two sets of pairs of circles, where the circles might represent connections or terminals associated with the switch. The presence of red dots indicates active connections or points in the circuit on the right side. Overall, this image likely serves as a schematic representation for understanding electrical connections and functionalities related to the rotary switch. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/otCu5f_QQg4~Az30edu2Kg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/otCu5f_QQg4~Az30edu2Kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Row 1 is the connection bolt for clamps and generally used in Rod hangers.

* For Rod hanger pipe clamps, the quantity of bolts in row 1 cannot be zero.
* The left-most bolt in row 1 is the connection bolt where the port is located.


Image:[Image-Analysis: The image displays two different types of diagrams commonly related to circuit symbols. On the left, there are two symbol representations: the first (labeled "1") shows a coil or inductor, which is typically used to store energy in a magnetic field, and it includes two connection points. The second (labeled "2") appears to be a switch or relay symbol, indicating a control mechanism where either the circuit is open or closed. On the right side of the image, there is a vertical layout that resembles a combination of a switch with indicator lights at the top and bottom, suggesting a status indication for the operating state of the device, likely indicating whether it’s on or off. The red dots signify points of electrical connection or activation. The arrangement of these symbols illustrates how they interrelate in an electrical circuit, providing insights into how power and signals may flow through a system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GyE93iSVKgx_vjvXI5mbJg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GyE93iSVKgx_vjvXI5mbJg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Rows 1 and 2 are the connection bolts for Riser clamps used in Rod hangers.
* For Riser clamps used in Rod hangers, the quantities of bolts in row 1 and 2 cannot
  be zero.


Image:[Image-Analysis: The image depicts a mechanical component, likely related to an electrical or electronic schematic. On the left side, there is a circular device labeled with the letters "L" and "R," which could indicate left and right connections, respectively. Alongside are numerical labels from 1 to 6 on the left, suggesting a connection scheme or pin configuration for the component. On the right side, there are two domino-like structures, where one has a red dot next to the letter "R," possibly indicating a special function or active connection at that position. The entire layout hints at a circuit component or switch with specific designation for connections and functionalities. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6gXUoSFRQ~CQ24FtPRQdRA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6gXUoSFRQ~CQ24FtPRQdRA-_PVFQNoCl4XmjAxWO0f7XQ/content)

The following properties are similar for all Bolt rows 1 through 6.

IJUAOffset1::Offset1

Specifies the offset of each bolt row from the pipe centerline.


None: 

* These offsets are always positive. Rows 1, 3 and 5 are always "above" the pipe centerline
  and Rows 2, 4, and 6 are always "below" the pipe centerline. Do not specify negative
  offset values.
* Bolt rows 2, 4, and 6 cannot be used when Angle1 is set to 360-degrees.
* Bolts are not shown on the clamp body when Multi1Qty is set to zero.
* If Bolt row 1 contains more than one bolt, the port is located on the left-most bolt,
  as shown in the drawing with points that are highlighted in red.


Image:[Image-Analysis: The image provides a schematic representation of a mechanical or electrical component layout. On the left side, there are two parallel lines with labels numbered from 1 to 6 vertically, indicating different points or segments related to an offset mechanism represented by the term 'Offset1' placed between the two lines. The central circular shape suggests a connection point or junction. On the right side, there are vertical stacks with round dots marked by 'R' and a few more red dots, possibly representing specific components or configurations that are associated with the left representation. This layout is likely used in engineering or design contexts where positioning and connection points are crucial for functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pPaE97p6n77SbY1veUpAGA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pPaE97p6n77SbY1veUpAGA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty

Specifies the quantity of bolts. Bolts are not shown on the pipe clamp body when Multi1Qty is set to zero. Valid cases are shown below.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

Valid cases are shown below.

IJUAhsMulti1::Multi1Location

Specifies the distance for the exact location of the bolts, depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge, or a center-to-center spacing.
Valid cases are shown below.

Valid Multi1Qty, Multi1LocateBy, Multi1Location Cases


Image:[Image-Analysis: The image depicts a diagram with a rectangular shape that has a circle centered on its top part. A dashed vertical line runs through the middle of the rectangle and the circle, indicating a relationship of central alignment. There are also annotations at the bottom providing additional details: "MultiQty = 1" suggests there is one of this object; "MultiLocatedBy = Center" indicates the positioning is based on the center of the circle; and "MultiLocation = 0" likely refers to a specific location parameter, which in this context might mean the object is located at a default or zero position. Overall, the image seems to illustrate a design or technical drawing concept related to object placement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zCkGTQChOqyMiEuFLZ4KjQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zCkGTQChOqyMiEuFLZ4KjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)
Image:[Image-Analysis: The image displays a technical drawing or diagram showing a vertical rectangular shape with two circular holes at the top. The circles are symmetrically placed along the vertical center line of the rectangle. Below the rectangle, there are annotations that describe the properties of the holes: "MultiQty = 2" indicates there are two holes; "MultiLocatedBy = Center" specifies that the holes are located relative to the center of the rectangle; and "MultiLocation = x" suggests that the positions of the holes are determined by the variable "x", which likely refers to a measurement for their horizontal distance from the center. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ug8dLx0p7V57oGIbtOifuw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Ug8dLx0p7V57oGIbtOifuw-_PVFQNoCl4XmjAxWO0f7XQ/content)
Image:[Image-Analysis: The image depicts a technical drawing or schematic related to a manufacturing or assembly process. It features a rectangular shape with specific dimensions indicated by arrows at the top, suggesting width. Inside the rectangle, there are two circular shapes at the top, likely representing holes or attachment points. The dashed vertical line down the center may indicate a centerline or a point of symmetry. Below the rectangle, there is explanatory text that provides additional details: "MultiQty = 2" suggests that there are two of the item being referenced; "MultiLocatedBy = Edge" implies that the positioning of the components is based on the edge of the rectangle; "MultiLocation = x" suggests the specific location for these features. Overall, the image is likely used in a technical environment, such as engineering or manufacturing, to describe a component's specifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/N6JkxbQuLtclgpaZthBqJA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/N6JkxbQuLtclgpaZthBqJA-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image depicts a diagram illustrating a layout with three circles positioned in a vertical arrangement. Each circle is evenly spaced from one another, indicating a symmetrical layout. The parameters mentioned below the diagram include: "MultiQty = 3," indicating there are three items (circles) in total; "MultiLocatedBy = Center," suggesting that the circles are centrally located within the overall layout; and "MultiLocation = x," which likely refers to the specific point or coordinate where the circles are displaced. This layout could be used in contexts such as user interface design, graphics, or engineering schematics, demonstrating how elements can be organized symmetrically. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0jNaEtPoad4UtzRw8sn9dQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0jNaEtPoad4UtzRw8sn9dQ-_PVFQNoCl4XmjAxWO0f7XQ/content) 
Image:[Image-Analysis: The image depicts a rectangular shape with three circles arranged horizontally along the top edge. There is a dashed vertical line running down the center of the rectangle, indicating symmetry. Below the rectangle, there are annotations with specific parameters: "MultiQty = 3", which suggests that there are three items (the circles), "MultiLocatedBy = Edge", implying that the circles' positions are determined by the edge of the rectangle, and "MultiLocation = x", which indicates the precise location of these circles is marked by "x". This could represent a design or schematic detailing how multiple items are positioned in relation to a reference point, possibly for manufacturing or layout purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YDFrZ21_Dbj5nUHL11kBZw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YDFrZ21_Dbj5nUHL11kBZw-_PVFQNoCl4XmjAxWO0f7XQ/content)


Image:[Image-Analysis: The image appears to illustrate a technical concept related to placement or arrangement of multiple entities (represented as circles) in a horizontal line. There are five circles indicated, suggesting that they represent objects or items that need to be positioned. The diagram shows constraints for their positioning: a specified distance (x) between certain elements, with arrows suggesting that these elements can shift within this distance. There is also text that indicates multi-quantity settings: "MultiQty greater than 3" confirms that there are more than three items (five shown), "MultiLocatedBy = Center" specifies that the only valid alignment for these items is centered, and "MultiLocation = x" means that the distance 'x' is an important measurement for positioning the entities. Overall, the image serves to communicate the relationship between the items and how they should be arranged in terms of quantity and spacing. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4IYjAhcIiSK5HWAaCSM5Mw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4IYjAhcIiSK5HWAaCSM5Mw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp Configuration Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306658?contentId=ElLtyPYsI3JltpSygyllSw)
These properties are used to specify different orientations of the clamp graphic,
the port positions and their orientations.

IJUAhsClampCfg::ClampCfg

Enter the codelist number for the configuration to use as defined in the hsClampCfg sheet in the HS\_S3DParts\_Codelist.xls workbook.


None:  In general, Pipe Clamp Hangers that are bolted to Structural Members uses Clamp configuration
1. For this configuration, the Assembly Information Rule (AIR) calculates the offset
of the top bolt port by using formula ½ x Gap1 + Thickness1


Image:[Image-Analysis: The image depicts two types of electronic components: one is a circular component on the left side, and the other is a rectangular component on the right side. The circular component includes a schematic representation of a potentiometer, indicated by the circular shape and the arrow that shows variable resistance. The red dots indicate connection points. The rectangular component on the right is indicative of a different electronic part, possibly a capacitor or a resistor, represented in a schematic layout with clear terminal points for connections. The left component could be intended for adjusting levels or controls, while the right component likely functions to store or regulate electrical energy. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PzIdrsn~xSaN9gU3atGwsw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PzIdrsn~xSaN9gU3atGwsw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Available configurations:

* 1 - Rod Hanger


Image:[Image-Analysis: The image displays two different designs of a device or component. On the left, there is a circular design labeled with two distinct points (1 and 2) that suggest different functional parts or configurations. It features a central loop and two small red dots indicating specific positions or connections. The right side shows a rectangular design that also has a red dot, possibly representing another component with a different function or orientation. The use of red dots across both designs may indicate points of connection or interfaces within a larger system or circuit. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YP9Xa3ydeh1_7MQpTuJH~w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YP9Xa3ydeh1_7MQpTuJH~w-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Side Mounted

  + On shoe or post

    
Image:[Image-Analysis: The image contains two diagrams that appear to depict components related to a mechanical system. On the left side, there is a circular element supported by a stand, labeled with two points marked with red dots. The circular element seems to represent a wheel or a rotating system, possibly indicating a motion involving pivot points or bearings, as emphasized by the accompanying arrows suggesting movement along a vertical axis. The right side portrays a rectangular structure with a vertical orientation and similarly marked red points, which could represent a block or a stationary element, possibly illustrating a connection or interaction with the rotating system depicted on the left. The arrangement suggests an analysis of motion, possibly revolving around concepts in physics such as torque or rotational dynamics. Overall, the image illustrates relationships between different mechanical elements involved in motion and support. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NqXbGdT7O6DhibqjiDt6fw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NqXbGdT7O6DhibqjiDt6fw-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Hanging with lug, clevis, hole

    
Image:[Image-Analysis: The image appears to be a technical illustration showing a device with two views: a side view and a top view. On the left, the first view includes a circular element (marked as #1) that seems to depict a mechanism with moving parts, indicated by arrows that represent movement. The red squares (#1 and #2) likely denote key components or positions of importance in the mechanism. The second view on the right presents a straightforward side profile of the device, which allows for a clearer representation of its structure. The device may be related to a mechanical assembly, possibly a type of actuator or rotating element, considering the context and presentation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EapyNaxaiHn~cPbmb4hb2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EapyNaxaiHn~cPbmb4hb2w-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Threaded

    
Image:[Image-Analysis: The image appears to be a technical illustration showing a device with two views: a side view and a top view. On the left, the first view includes a circular element (marked as #1) that seems to depict a mechanism with moving parts, indicated by arrows that represent movement. The red squares (#1 and #2) likely denote key components or positions of importance in the mechanism. The second view on the right presents a straightforward side profile of the device, which allows for a clearer representation of its structure. The device may be related to a mechanical assembly, possibly a type of actuator or rotating element, considering the context and presentation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EapyNaxaiHn~cPbmb4hb2w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/EapyNaxaiHn~cPbmb4hb2w-_PVFQNoCl4XmjAxWO0f7XQ/content)
* 3 - Side Mounted-Two Side Ports

  + Angled

    
Image:[Image-Analysis: The image presents a mechanical or fluid system with two main components. On the left, there is a circular section labeled with a swirling symbol, indicative of a rotational or flow process, flanked by two horizontal bars that could represent pipes or tubes. Each bar is marked with a number (1 and 2), indicating two distinct parts or segments connecting to the circular component. The right part of the image shows a rectangular block with three horizontal lines inside it, which might represent a control panel, a sensor, or an indicator related to the system on the left. The relationship suggests that the rectangular block is likely interacting with the circular component to monitor or control its function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lysp3iOGc4tzdtSG_5I_ag-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Lysp3iOGc4tzdtSG_5I_ag-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Straight

    
Image:[Image-Analysis: The image represents a schematic diagram showing two systems, indicated by the circles and lines. On the left side, there are two sets of connections and elements: one labeled "1" (likely referring to one part of a system) and the other labeled "2" (possibly denoting a second part). The circular element in the middle with red dots may indicate points of connection or flow, suggesting interactions between these elements. On the right side, there is a rectangular shape with red dots, which likely represents a different component or status indicator related to the systems on the left, showing that there are two distinct entities in a hierarchical structure, where the left side reflects interconnected parts and the right side highlights additional information or status for one of the systems. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZPKwBjHWABqqhdiV50XMFw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZPKwBjHWABqqhdiV50XMFw-_PVFQNoCl4XmjAxWO0f7XQ/content)
* 4 - Direct Bolted


Image:[Image-Analysis: The image consists of two diagrams that appear to illustrate electrical or mechanical components. On the left, there are two vertical bars labeled "1" and "2," with a circular component between them that has a spiral design at its center, possibly representing a coil or inductor. The red dots may indicate connection points or points of interest, possibly where voltage is applied or where readings are taken. The right side shows a similar vertical structure but with a more streamlined design, possibly indicating a different form or configuration of the same component. The two diagrams suggest variations in a system that may be involved in electromagnetism or mechanical motion, highlighting how different setups can achieve similar functions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fp8HYFx2r_PVIxifm2WLGg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fp8HYFx2r_PVIxifm2WLGg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 5 - Riser Rod Hanger


Image:[Image-Analysis: The image depicts a simple representation of a mathematical number line focusing on the numbers 1 and 2. It shows two positions: one at the left labeled "2" and the other at the right labeled "1." Between these two positions is a square in red color, which likely indicates the point that is between 1 and 2 on the number line. This representation suggests a number line visualization where the position of the red square represents a value that is less than 2 and greater than 1. It illustrates the concept of numbers and their relative positions on a line as well as the continuity of values between whole numbers. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PR4uv53bo5hyWUd_xoY64Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PR4uv53bo5hyWUd_xoY64Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 6 - Riser on Structure

  + Socket Clamp

    
Image:[Image-Analysis: The image presents a visual representation of a domino configuration. There are two dominoes visible, labeled with the numbers 1 and 2 at the top. The left domino shows two dots on both the top and bottom halves, indicating a value of 2. The center section is empty, which represents a blank side of a domino. The right domino displays two dots, indicating a value of 1, also on both the top and bottom halves. The arrangement reveals that one domino has a value connected to '2' and the other to '1', representing a common way of denoting points or values in a game involving dominoes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yj5nBLLGYoIqv0P~LjWXRw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yj5nBLLGYoIqv0P~LjWXRw-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Underground Clamp

    
Image:[Image-Analysis: The image represents a simplified version of a queue or stack structure, which consists of three sections or slots. At the top, there are numbers "2" and "1", likely indicating specific values or states related to the items represented in the queue/stack. The middle section has a filled red dot, which might indicate a current active item or point of focus in the sequence, while the outer sections contain empty circles, which could indicate available or empty slots. The arrangement suggests an organizational layout where items are being managed, possibly indicating binary options between two values or states represented by the numbers. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1aRjGST_kEK9zq0OndwcNQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1aRjGST_kEK9zq0OndwcNQ-_PVFQNoCl4XmjAxWO0f7XQ/content)
* 7 - Offset Pipe Clamp


Image:[Image-Analysis: The image appears to depict a mechanical or engineering schematic related to a system with two main components. On the left, there is a representation of a circular element located between two segments labeled "1" and "2." This circular element likely represents a rotating component such as a flywheel or rotor, typically used in machinery to maintain angular momentum. The lines behind it suggest structural supports or guides for the rotating mechanism. On the right, there is a vertical arrangement with several stacked rectangles, which may represent a support frame or housing structure for the components on the left. The numbered labels "1" and "2" indicate specific points or sections within the system that may require attention or connection. The use of red dots suggests points of interest or connection in the layout, highlighting the relationships between different parts of the schematic. Overall, the schematic aims to convey the layout and structure of a mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zOAqZwsKX0BsKzIHrxwctQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zOAqZwsKX0BsKzIHrxwctQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3

The purpose of Angle3 depends on ClampCfg.

* For ClampCfg 1 and 5, Angle3 rotates the clamp route port about its x-axis.
* For ClampCfg 2 and 3, Angle3 rotates the clamp from horizontal.
* A positive Angle3 rotates the clamp body counter-clockwise when looking along the positive X direction
  of the pipe port. Negative Angle3 rotates the clamp body clockwise.
* The rotation is actually achieved by rotating the orientation of the pipe port in
  the opposite direction by Angle3.


Image:[Image-Analysis: The image shows two diagrams, likely related to a mechanical setup involving angles and positions. On the left, there is a structure resembling a goniometer or protractor, indicated by the circular component. The lines and markers labeled as "Angle3" and numbers 1 and 2 suggest measurements or configurations related to this angle. The red dots likely represent important positions or measurement points. On the right, a simplified column structure is depicted, possibly representing a vertical reference point or a part of the setup that interacts with the first diagram. The two diagrams might connect, with the left possibly measuring angles related to the position or orientation of the vertical right structure in a physical experiment or engineering application. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zzYY6bfZMoIdl0G5K3FISQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zzYY6bfZMoIdl0G5K3FISQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

The purpose of Width3 depends on ClampCfg.

* For ClampCfg 2 (side mounted), Width3 specifies the outside width of the post or shoe that the clamp rests on. If this
  value is set, the ClampSide port is retracted so that the post or shoe can be connected
  directly to the port, and its edges are matched up with the curved face of the clamp.
  If both Height3 and Width3 are set, Height3 is used to set the port location.


Image:[Image-Analysis: The image appears to illustrate a mechanical design or schematic involving a circular component with a specified width (Width3) indicated between two arrows. The left side depicts a circular element with two sections numbered 1 and 2, suggesting a division or specification of parts within the circle. The center of the circle has a design that resembles a spiral or a dual-helical configuration. The right side shows a simpler representation, possibly indicating a side view or another angle of the main circular component. Overall, the image combines measurements and designs that are typical in engineering drawings, connecting the dimensions of the component with its physical representation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/97oZU1aUD32fHxnXPlTPEw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/97oZU1aUD32fHxnXPlTPEw-_PVFQNoCl4XmjAxWO0f7XQ/content)

* For ClampCfg 3 (side mounted, two ports), if Width3 is specified, the ports are located on the side of the clamp. They are separated
  by the specified width, with orthogonal ports orientated as shown. Width3 must be less than the outside diameter of the clamp body (that is, less than Diameter1 + 2 x Thickness1). If both Width3 and Angle2 are specified, Width3 can be used.


Image:[Image-Analysis: The image consists of two different components demonstrating a part of a mechanical design or system. The left image shows a rounded component with two labeled points (1 and 2), indicating specific locations to pay attention to, possibly for assembly or measurement. It also shows a base with a dimension labeled "Width3." The right image represents a cylindrical shape, positioned vertically, also with a marked point (indicated by a red spot). This suggests that both images are related to a mechanical assembly or fitting where spatial arrangements and measurements are crucial, likely indicating where bolts or fittings should be placed. The overall design may involve connecting these two parts, with specific attention to the marked points for alignment or functionality. The presence of width dimension indicates the importance of size in this assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xk_U5H1ga2RShuVQSNcdCg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xk_U5H1ga2RShuVQSNcdCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* For ClampCfg 4 (direct bolted), the ports are separated by Width3, and centered in the clamp body.


Image:[Image-Analysis: The image depicts a technical diagram showing two views of a component. On the left, there are two vertical lines labeled "1" and "2" connected by a circular element in the center, which has a swirling design inside it. Below this, there is a measurement labeled "Width3," indicating a distance between the vertical elements. On the right side, there is a more simplified view of the same component, showing it from a different angle. The use of red dots may indicate key connection points or features to note for assembly or understanding the component's function. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mTQly7ylAcIrQJsH~4KsIQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/mTQly7ylAcIrQJsH~4KsIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* For ClampCfg 6 (riser on struct), the bottom ports are separated by Width3.


Image:[Image-Analysis: The image depicts a diagram showing two boxes with numbered labels on top (2 and 1) and red dots located on the bottom. The dashed horizontal line connecting the two boxes is labeled "Width3", indicating the distance between the two boxes. The boxes appear to be schematically representing objects or components, possibly in relation to their measurements or positions. The box on the left has the label "2" above it and the box on the right has the label "1", suggesting a hierarchical or sequential order. The arrangement and annotation suggest a focus on the physical relationship and dimensions between these two elements. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H9nfBVTktMVFh0QG3_~77g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H9nfBVTktMVFh0QG3_~77g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* For ClampCfg 7 (offset pipe clamp), Width3 sets the overall width of the wings. If it is zero, unspecified, or less than Height1 plus Height2, the wings are not drawn.


Image:[Image-Analysis: The image displays a mechanical or engineering drawing featuring a central cylindrical component, indicated by the circular object with two curves representing a flow or rotation. The drawing includes two horizontal arms or supports labeled as points '1' and '2', which likely represent the attachment or connection points of this component within a system. Below the main assembly, there is a horizontal measurement line marked 'Width3', indicating the width of the entire setup. On the right, a side view of the component is presented in a simplified manner, demonstrating its height and general shape without detailing the surrounding structures. This type of illustration is typically used in engineering contexts to convey design specifications and structural relationships. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0Ruf49rDWMtNy_dNyzwGGA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0Ruf49rDWMtNy_dNyzwGGA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight3::Height3

The purpose of Height3 depends on ClampCfg.

* For ClampCfg 2 (side mounted), Height3 specifies the distance from the side of the clamp to the ClampSide port. If both
  Height3 and Width3 are set, Height3 can be used.


Image:[Image-Analysis: The image depicts two different views of a mechanical component, possibly a cylinder or a piston. The left side shows a cross-sectional view of the component, highlighting various key points with red dots numbered 1, 2, and 3. The text "Height3" indicates a vertical measurement related to this component. The right side presents a side view of the same component, demonstrating its height and structure in a more straightforward manner. The arrangement suggests a relationship between the different views as representations of the same object from different angles, emphasizing the dimensions crucial for understanding its application or functionality. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JNaxGEg1U9UxPwEx5yaciw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JNaxGEg1U9UxPwEx5yaciw-_PVFQNoCl4XmjAxWO0f7XQ/content)

* For ClampCfg 4 (direct bolted), Height3 specifies the amount to offset the ports from the pipe centerline. A positive offset
  is in the z-direction of the port. Positive, zero, and negative values are allowed.
  A negative value is more commonly used.


Image:[Image-Analysis: The image depicts a schematic representation of a physical system with two components labeled "1" and "2". In the center of the image, there is a circular element, which likely represents a coil or a wire loop, where the positive terminal is indicated by +Z pointing upwards. To the right of the circle, there is an arrow showing a measurement labeled "Height3", suggesting a dimension related to the system's height or spacing. This implies that there could be a relationship between the positioning or dimensions of the components and the area they occupy. The red dots near the components may represent specific points of interest in the measurement or functionality of this system. Overall, the image appears to be illustrating a concept related to physics or engineering, potentially involving magnetic fields or electrical components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1ZKNsmDsELqP3ZSJwjF92Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1ZKNsmDsELqP3ZSJwjF92Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAHgrOccLength::Length Or IJUAhsLength::Length

This property is used only for ClampCfg 7 (offset pipe clamp).

* IJOAHgrOccLength specifies the variable length.
* IJUAhsLength specifies the variable length.


Image:[Image-Analysis: The image depicts a technical illustration that appears to show two numbered points (1 and 2) related to a mechanical or engineering context. There is a circular object in the center that connects these two points with a red dot at each point, possibly representing measurement or a focal point for a system. To the right of the circular object, there is a vertical indication of "Length" with red dots aligning vertically, which suggests a measurement of length associated with the two points and the circular object. This image likely represents a diagram for understanding dimensions or distances in a mechanical assembly or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3GpXCdZ9QAlQGEi95p9H8g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3GpXCdZ9QAlQGEi95p9H8g-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp Liner Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306840?contentId=rqLaT3i~CRgHsmW4FS8xUw)
These properties can be used to specify any kind of pipe wrap, isolating liner, or
a tall narrow rib around the outside of the clamp.

IJUAhsDiameter4::Diameter4

Specifies the outside diameter of the cylinder which is used to represent the clamp
liner. This value cannot be zero or undefined.


Image:[Image-Analysis: The image features a schematic representation of a mechanical part, possibly a bearing or a similar component. The left side shows a circular part that includes internal features (curves and a small red dot, which may indicate a specific position or point of interest). The right side displays a vertical section with the word "Diameter" followed by the numeral "4," indicating the measurement of the diameter, likely of the circular component on the left. The diagram suggests an engineering or technical context, indicating the specifications or dimensions of the part being illustrated. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LvdiL574_hwa9wGjvA2zEA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LvdiL574_hwa9wGjvA2zEA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Specifies the width of the cylinder which is used to represent the clamp liner. This
value cannot be zero or undefined.


Image:[Image-Analysis: The image depicts a mechanical component with two distinct parts. On the left side, there is a circular component featuring a central red point and a curved line, potentially indicating a bearing or a coupling mechanism. This component appears to have channels or grooves for functioning purposes. On the right side, there is a rectangular component labeled "Width4," suggesting its dimensions or a specific size designation. This rectangular part may represent a fitting or a connector that has an opening for attachment, typically used in machinery or assembly contexts. The relationship between these two components likely illustrates how they fit together or operate in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r3YlgN~SuasnHBf1KS_KEg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/r3YlgN~SuasnHBf1KS_KEg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Gussets Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306844?contentId=JE5ihfMKGFqc64vnDzjMag)
These properties are used to specify the gussets on the pipe clamp body.

IJUAhsDim1::Dim1

Specifies the width of gusset at the end of the clamp. The same value is used at both
ends of the clamp, on both sides. This value can be either positive, zero, or negative.


Image:[Image-Analysis: The image showcases two distinct components: a hexagonal structure on the left and a rectangular one on the right. The hexagonal component contains a circular figure at its center, which appears to be a part of a mechanical or engineering design, potentially indicating rotational motion with its swirled pattern. The labels "1" and "2" suggest that there are key points or features that need to be noted on the hexagonal structure. Below this component, the term "Dim1" is annotated, indicating a dimension or measurement that is significant to the overall design. The right rectangular component has red markers as well, possibly indicating points of interest or attachment related to the hexagonal unit. The overall image seems to represent a technical schematic or drawing, where the left side is likely focused on a rotating element, while the right side may specify certain dimensions or points that are relevant to understanding the complete assembly or function of these parts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LjCOG~CnfJLt_9Qemc3UHQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LjCOG~CnfJLt_9Qemc3UHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDim2::Dim2

Specifies the distance that the gusset extends past the clamp body at the center of
the clamp. This value can be either positive, zero, or negative.


Image:[Image-Analysis: The image appears to be a technical diagram or illustration used to indicate dimensions related to a mechanical component, possibly a bearing or gear system. On the left side, there are two numbered callouts (1 and 2) that likely refer to specific features or points of interest within the component. The central circular area might represent a cross-section of the component with an arrow labeling "Dim2," indicating a dimension measurement from one point to another. On the right side of the image, there is a vertical rectangle that likely represents a related dimension or standard size for comparison, with red dots marking key measurement points. Overall, the image seems to serve as a reference for understanding the measurements and features of a mechanical part. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~p1PfjN6eIhXjz8InWsKvg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~p1PfjN6eIhXjz8InWsKvg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the gussets. If it is zero, the gussets are not drawn.
If it is a positive value, the gussets are drawn inside the clamp body. If it is a
negative value, the gussets are drawn outside the clamp body.


Image:[Image-Analysis: The image depicts a technical diagram related to a mechanical or engineering component, possibly showing different views or aspects of a part. On the left side, there are two views represented by the numbers 1 and 2, indicating different orientations of a component with a circular feature (likely a bearing or similar device). In the middle, there appears to be a thickness measurement labeled "Thickness2," which might denote the thickness of a certain section of the component. On the right side, there are two outlines, labeled with "+ve" and "-ve," which could represent different polarity states or configurations of a part. The use of red dots may indicate specific points of interest or critical features in the design. This diagram is likely used for manufacturing, assembly, or inspection of the identified components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yt4oLTveIyGcFdbS6Jhuqw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yt4oLTveIyGcFdbS6Jhuqw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Side Connection Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306849?contentId=KEu2zr4YgpldUiP9eNjytw)
These properties are used to specify the side connection on the pipe clamp body.

IJUAhsShapeType::ShapeType

Enter the codelist number of the shape type as defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.

* 1 - Round


Image:[Image-Analysis: The image depicts a symmetrical layout with three circles. In the center, there is a larger circle filled with a red square at its center, while there are two smaller circles on each side of the larger circle. This arrangement creates a focal point around the central red square, suggesting emphasis or importance. The smaller circles on the left and right may represent auxiliary elements or related concepts that are connected to the central theme represented by the larger circle. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/64ZuMiStJTAo2MS9dqO06w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/64ZuMiStJTAo2MS9dqO06w-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square (also used for rectangle)


Image:[Image-Analysis: The image appears to depict a simple diagram consisting of three boxes arranged in a row. The left and right boxes at the ends contain empty circles, while the middle box has a square outline with a red square located in the center. This could suggest a relationship or process where the outer circles represent inputs or entities that connect to the central square, which may represent a process, function, or data point. Overall, it visually communicates a concept of connectivity or interaction between distinct elements, emphasizing the central importance of the middle box. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K5L5GRaDavcyx~bXSim3HQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/K5L5GRaDavcyx~bXSim3HQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image displays a geometric figure composed of two circles positioned at the ends and a hexagon in the center, forming a layout that resembles a simple symmetrical structure. In the center of the hexagon, there is a small red square, which draws attention to this central part. The circles on either side suggest endpoints or boundaries, while the hexagon indicates a focus or a central point of interest, possibly symbolizing a connection or relationship between the elements represented by the circles and the central hexagon. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BIBQ8F5e2zeb9rr6XFRMHw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BIBQ8F5e2zeb9rr6XFRMHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the side connection shape from the outside face of the
clamp, to the outside face of the side connection.


Image:[Image-Analysis: The image illustrates technical drawings related to a mechanical component, likely involving dimensions and tolerances. On the left side, there is a circular part marked with two reference points (1 and 2), indicating specific locations related to the element's measurements. Arrows pointing up and down suggest that there are dimensional specifications for vertical space. On the right side, there is a block with a label "Thickness3," which refers to a specified dimension for thickness. This block also has vertical arrows indicating the thickness measurement being referenced. The combination of these elements suggests a focus on precise engineering specifications necessary for manufacturing or inspecting the parts in question. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yt2C1IaCj5GNNLnobNVUxA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yt2C1IaCj5GNNLnobNVUxA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth5::Width5

Specifies the outside dimension of the side connection shape.

* 1 - Round


Image:[Image-Analysis: The image depicts a schematic representation of a mechanical component, likely a cylinder or a hole with specific dimensions. The label "Width5" suggests that the component has a total width of 5 units. There are two smaller circles on either side of a larger circle in the center, which could represent holes or ports. The central circle is marked with a red dot, possibly indicating a reference point or a location of interest within the design. The image provides a visual overview of the dimensions and layout of the component, highlighting the central circular area in relation to the side features. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v5nXN9XKLTSNvHL5oHidTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v5nXN9XKLTSNvHL5oHidTA-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 2 - Square


Image:[Image-Analysis: The image depicts a diagram showing a rectangular object with a width labeled as "Width 5". The rectangular object is placed centrally and is surrounded by two circular shapes on either side. The red square in the middle represents some focal point or feature of the rectangle. The diagram seems to illustrate a relationship between these shapes, highlighting that the rectangle's central positioning is important relative to the circular shapes on the left and right sides. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UvqGXqxCuVAUfrJ9Ou5Cyg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UvqGXqxCuVAUfrJ9Ou5Cyg-_PVFQNoCl4XmjAxWO0f7XQ/content)

* 3 - Hex


Image:[Image-Analysis: The image shows a layout of shapes and dimensions. At the center is an octagon, reflecting a shape with eight sides. The dimensions of the overall layout are emphasized by the text "Width 5", which indicates that the total width of the arrangement is 5 units. On either side of the octagon, there are two circles, likely representing connection points or end caps. The octagon features a red square in the center, possibly indicating a focal point or a specific detail that requires attention. The arrows suggest a measurement direction for the width. Overall, the diagram visually conveys a geometric relationship among the shapes and emphasizes the width of the configuration. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PKQ~rK~DpvTKcl8GeWIaQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PKQ~rK~DpvTKcl8GeWIaQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth6::Width6

Creates a rectangle shape instead of a square for NutShape 2 (square). If this value
is zero or not specified, NutShape 2 becomes square shape.


Image:[Image-Analysis: The image depicts a rectangular block with a labeled width of "Width6." This block is placed horizontally and has two circular shapes on either side, which could represent some cylindrical objects or holes, indicated by the unfilled circles. In the center, there is a smaller rectangular shape highlighted in red, possibly representing a keyhole or a central feature of the block. The arrows point in opposite directions along the vertical axis, suggesting a mechanical or spatial relationship to the surrounding circles. The overall structure could be part of a mechanical schematic or engineering drawing, showing how different components relate to one another in terms of width and positioning. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HuywOxacA_fkft7W6jQI7w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HuywOxacA_fkft7W6jQI7w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle2::Angle2

For ClampCfg 2, Angle2 rotates the clamp side port around its z-axis. If it is zero, the clamp side port
is oriented the same as the pipe centerline port. When this clamp side port is used
to represent a lug or a bolt/pin connection, the orientation is important. When it
is used for a hole, or a female-threaded hole, the orientation is not needed although
it can be used. Typically, you can only use 0 (default) or 90-degrees, depending on
the actual orientation of the pin/bolt or lug in the catalog part.


Image:[Image-Analysis: The image illustrates the mechanics of a rotating system, identified as "Angle2". On the left side, there is a diagram showing a circular mechanism with parts labeled as 1 and 2. The circular component likely represents a pivot or a joint that allows for rotation. The arrows indicate the direction of movement, suggesting that the component can rotate around a central axis. There are red dots indicating specific points of interest or focus on the mechanism. On the right side, a side view of the system is displayed, which reinforces the understanding of the overall configuration and how the components relate to one another in this rotational system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNWursx~XkOi5syaf6xydA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNWursx~XkOi5syaf6xydA-_PVFQNoCl4XmjAxWO0f7XQ/content)

ClampCfg 3, Angle2 determines the angle between the two ports on the side of the clamp. The port orientation
also gets angled to simplify joints in assemblies. Angle2 must be less than 180.


Image:[Image-Analysis: The image illustrates a mechanical or engineering concept related to angles. On the left side, there is a diagram showing a circular component with two labels, "1" and "2," indicating points that likely represent positional measurements or features on the object. The labeled angle, "Angle2," is defined between these two points, as indicated by the arrows pointing to the angle's vertex. This suggests a focus on rotational aspects or alignment aspects in engineering design. The right side of the image appears to show a vertical view of the same circular object, enhancing the understanding of its structural composition. Overall, it highlights key measurements relevant to angles and positioning essential for analyzing mechanical functions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RiQW6mWbd0rLETiObKGRZQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RiQW6mWbd0rLETiObKGRZQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Maintenance Aspect - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/722581?contentId=tVUvtj2GtzuzCy8sS78k_w)
IJUAhsCreateMaintAspect::CreateMaintenanceAspect

Specifies a boolean value for the maintenance aspect of the Pipe Clamp.

IJUAhsMaintenanceTh::MaintenanceThickness

Specifies the maintenance thickness.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306863?contentId=29q8Th~a7wG9PygWBcrezA)
![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/epzHu4Hw~7x6d9GezWAv5w-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a1fa1000e201da3e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/epzHu4Hw~7x6d9GezWAv5w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Rod Hanger

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HhGnV5aXUD7X8qivHoa~Rw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=278800d90dfc1f2d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HhGnV5aXUD7X8qivHoa~Rw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1015 (Pin) | Pin or Bolt Diameter | Pin or Bolt Diameter | Pin or Bolt Diameter |

Port3 - Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1200(other) | 0 | -9999 | 9999 |

Side Mounted

Graphics are identical to 1, except they are all rotated 90 degrees + Angle3 around
the local X coordinate (including clamp body, bolts, and so on). The Pin port, at
bolt 1, remains the same. The pipe port orientation changes, so Z points down to the
structure for the pipe port. A ClampSide1 port is required on the side of the clamp, for connection to the shoe or post, with
the same orientation as the pipe port. If Width3 is defined, the ClampSide1 port is retracted so that a shoe or post of Width3 can connect directly to it. If Height3 is defined, a positive offset is in the Z direction of the ClampSide1 port. If both Height3 and Width3 are set, Height3 is used.

* On shoe or post

  + Horizontal Single Shoe or Narrow Post

    
Image:[Image-Analysis: The image illustrates a technical diagram related to a mechanical or structural system. It shows various views of a component, likely part of a larger assembly mechanism. The diagram includes different orientations (Top, Front, and Side views) and labels the axes (X, Y, Z) which are commonly used in engineering to describe three-dimensional space. There is a circular component that likely represents a pivot or a rotational part, with additional notations indicating single shoe or narrow post orientation. The angles, labeled as Angle3 = 0 and other references, suggest specific positional or angular relationships vital for positioning or movement in the assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T3zqL2ApOcZJtpz4oIQpQQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T3zqL2ApOcZJtpz4oIQpQQ-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Angled Single Shoe or Narrow Post

    
Image:[Image-Analysis: The image provides a technical illustration related to mechanical or structural engineering, focusing on a "Single Shoe or Narrow Post, Angled." It features three main views of the component: a top view, a front/side view, and a detailed view of the angled features. The views are labeled with axes (X, Y, Z) indicating the three-dimensional orientation of the object. The illustration also includes an angle measurement (Angle3 = 45°) that likely refers to the angle at which the post or shoe is positioned relative to the base or another reference. The diagrams indicate the relationships between different components and their orientations, essential for understanding the assembly and function of the structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H4AuTHLU9NBu5iFbabzw1A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/H4AuTHLU9NBu5iFbabzw1A-_PVFQNoCl4XmjAxWO0f7XQ/content)
  + Double Shoe or Wide Post

    
Image:[Image-Analysis: The image provides a technical diagram likely depicting a mechanical or engineering component, specifically a "Double Shoe or Wide Post." The diagram includes several views: a top view and front-side view, labeled with axes (X, Y, Z) indicating the three-dimensional orientation. It shows angular measurements, with one labelled as "Angle3=45," suggesting a specific angle related to the component's design. Different marked dimensions (R, L, Width3) indicate physical measurements needed for construction or analysis. The diagram likely serves to guide a reader in understanding the geometric setup and orientation of this component, which may be relevant in structural or machinery applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XKSSD0G65TvfCA~Ck4qNxA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XKSSD0G65TvfCA~Ck4qNxA-_PVFQNoCl4XmjAxWO0f7XQ/content)
* Hanging with Lug, Clevis, Hole, or Threaded hole

  + Side Attachment, Lug, Clevis, Hole, Threaded Shown Upside Down.

    
Image:[Image-Analysis: The image presents a technical drawing that illustrates a mechanical component from multiple views: top, front/side, and side. It depicts a three-dimensional object with a cylindrical feature. The drawing includes dimensions labeled with coordinates (X, Y, Z) to indicate orientations and measurements for accuracy in construction. There are also specific annotations such as Angle3=45, which indicates an angular measurement relevant to the design. The component is described as having features such as a side attachment, lug, clevis, threaded hole, and additional details labeled to show its upside-down orientation. These dimensions and descriptions assist engineers or technical personnel in understanding how to manufacture or use the part in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2USmhP8TAVUiC6sFS21rSw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2USmhP8TAVUiC6sFS21rSw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1015 (Pin) | Pin or Bolt Diameter | Pin or Bolt Diameter | Pin or Bolt Diameter |

Port3 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
|  | Shoes | 0 | -9999 | 9999 |
| Side | 1200 (Other) |
|  | Rod Types | The Diameter of the rod for connecting to other components. And it is same as RodDiameter Property. | 0 | Thickness3 |
| Side | 1001 (IntThdRH) |
|  | 1003 (IntThdLH) |
|  | Pin Type | Dimension not defined. Set to -1 | Dimension not defined. Set to -9999 | Dimension not defined. Set to 9999 |
| Side | 1005 (Pin) |
|  | Lug Types | Dimension not defined. Set to -1 | Dimension not defined. Set to -9999 | Dimension not defined. Set to 9999 |
| Side | 1007 (Eye) |

Side Mounted - Two Side Ports, Angled or Straight

This configuration has two ports on the ClampSide1 and ClampSide2 and it does not
include a port on Bolt 1.

If Angle2 is specified, the ports are located on the side of the clamp, separated by the specified
angle. These angled ports are oriented as shown below. Angle2 is always less than 180.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wxrBscN2hBRXc1sZ1HKFYw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=785643daa64cca19)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/wxrBscN2hBRXc1sZ1HKFYw-_PVFQNoCl4XmjAxWO0f7XQ/content)

If Width3 is specified, the ports are located on the side of the clamp separated by the specified
width and these ports are oriented as shown below. Width3 is always less than the outside diameter of the clamp body (that is, less than Diameter1
+ 2 x Thickness1).

In case if both Width3 and Angle2 are specified, Width3 is used.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v_p9KFyclKiVV8vOLj28RQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c18dd91b6e82cedf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v_p9KFyclKiVV8vOLj28RQ-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  Angle1 and Angle3 can also be used with this configuration.

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1200 (Other) | 0 | -9999 | 9999 |

Port3 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1200 (Other) | 0 | -9999 | 9999 |

Direct Bolted

In Direct Bolted Clamps, the bolt quantities may all be zero since the hanger rods
often takes the place of the bolts. The ports are separated by Width3 and centered in the clamp body and with an offset of Height3 from the pipe centerline as shown below. You can also specify bolts in rows 1 to
6 but the ports are located independently of the bolts in this configuration.


Image:[Image-Analysis: The image depicts a technical diagram that illustrates a cylindrical component with labeled dimensions and directional indicators. The left side shows a side view of the component, which includes the parameters Width3, R (radius), Height3, and L (length). There are two points marked (1 and 2) with directional arrows indicating flow (both marked with 'Y' and 'Z' labels). The right side displays the same component's top view, indicating that the ports are centered. Additionally, there is an annotation stating "Shown Upside Down," suggesting that the orientation of the component is reversed compared to a standard view. This diagram is likely used in engineering or mechanical discussions related to the design or functionality of the component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5f5iIHOE1ec1zNzLWKPqMA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5f5iIHOE1ec1zNzLWKPqMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1004 (Rod Hole) | Dimension not defined. Set to -1 | Dimension not defined. Set to -9999 | Dimension not defined. Set to 9999 |

Port3 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1004 (Rod Hole) | Dimension not defined. Set to -1 | Dimension not defined. Set to -9999 | Dimension not defined. Set to 9999 |

Riser Clamp, Rod Hanger


Image:[Image-Analysis: The image shows a diagram consisting of three rectangular sections. Each section is labeled with axes: X, Y, and Z. In the left section, there is a label '2' along with an arrow indicating the direction of the Z-axis. In the middle section, there is a 'R' label, which typically denotes a rotation, and there are also arrows indicating the Z-axis direction. In the right section, the label '1' is similar to the left section, with an arrow indicating the Z-axis. The layout suggests a comparison or illustration of a rotational system with reference points or states, likely indicating some physical or mathematical relationship along these axes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l0yHKBvXNWU5KtLp0g1Xqw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/l0yHKBvXNWU5KtLp0g1Xqw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1005 (Pin) | Pin or Bolt Diameter | Pin or Bolt Diameter | Pin or Bolt Diameter |

Port3 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1005 (Pin) | Pin or Bolt Diameter | Pin or Bolt Diameter | Pin or Bolt Diameter |

Riser Clamp on Structure, Socket Clamp, Underground Clamp


Image:[Image-Analysis: The image appears to be a technical diagram, possibly related to physics or engineering. It illustrates a structure divided into three sections, labeled with numbers 1, 2, and 3. There are elements within these sections, including circles and arrows. The arrows seem to indicate directions or forces (denoted by X and R), while the letters Z and Y may represent variables or labels pertinent to the dimensions or the elements in the diagram. The section labeled "Width3" seems to indicate a specific measurement or dimension relating to the overall width of the entire structure. In summary, this image likely represents an analytical or experimental setup involving measurements or forces acting on the outlined sections. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4rYfOAROVBrXeixkduz1SA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4rYfOAROVBrXeixkduz1SA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1200 (Other) | 0 | -9999 | 9999 |

Port3 – Wing Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Wing | 1200 (Other) | 0 | -9999 | 9999 |

Offset Pipe Clamp

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ljjECJSbleR0SewYlJjMIQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c0f18f6b789afb87)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ljjECJSbleR0SewYlJjMIQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 – Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 1016 (Pipe Clamp) | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 – Side Mount Point

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Side | 1200 (Other) | 0 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pipe Saddle - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/774990?contentId=e_5Ye_IhP8gbv9JJjIvYnw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PipeSaddle  
Part Name: Pipe Saddle  
Part Description: Pipe Saddle with U-Bolt, Pipe Size <Diameter>"  
 Pipe Saddle, Pipe Size <Diameter>"

![Pipe Saddle SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lXsPg9_AN1S71mN2Sg7N8A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bdf8a84117cb4a82)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lXsPg9_AN1S71mN2Sg7N8A-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Pipe Saddle SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Start the Place Part 
look for icon that resembles a camera with a plus sign, indicating an option to add or upload photos:  command, and then select the design support.
4. In the Select Part dialog, select Parts > SmartParts > S3D Standard > Horizontal Traveler > Pipe Saddle as shown below.

![S3D Pipe Saddle SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/S5WOmvQet35Wj8mT7fs9dQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c04ec84442bc5ebd)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/S5WOmvQet35Wj8mT7fs9dQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System

![Pipe Saddle SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Jf_9XbcxHzJoVygjt6F2Eg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=65af7167752ccf33)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Jf_9XbcxHzJoVygjt6F2Eg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Strap Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775121?contentId=l0JSVyGasqQriHdxGNeCVA)
The basic strap attributes specify the shape and size of the strap.

IJUAhsStrap::StrapWidthInside

Specifies the distance between the legs of the strap. The thickness of both the sides
of a horizontal traveler must be a positive number. If the thickness is zero, the
software does not show the sides.

![Pipe Saddle - Strap Att - Strap Inside Width](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rq13NrzZ9sw6sn68bCk2Kg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8bd87a8c93acb8eb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rq13NrzZ9sw6sn68bCk2Kg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapHeightInside

Specifies the height from the base of the strap to the top of the strap.

![Pipe Saddle - Strap Att - Strap Height Width](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J_PM2bCnj_KYALVMh7ZYEg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5bf1e85fe81022e4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/J_PM2bCnj_KYALVMh7ZYEg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapThickness

Specifies the thickness of the rectangular stock that is used to make the strap. If
the value is zero, the software does not draw a strap shape.

![Pipe Saddle - Strap Att - Strap Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZE1c2JFnHh268VgWYP9IUQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dc0948e203c8a4e7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZE1c2JFnHh268VgWYP9IUQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapStockWidth

Specifies the width of the rectangular stock that is used to make the strap. If the
value is zero, the software does not draw a strap shape.

![Pipe Saddle - Strap Att - Strap Stock Width](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7ZHhrTIVcxLHDMomv9~Z1g-_PVFQNoCl4XmjAxWO0f7XQ/content?v=509fcbb28fd6e2e0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7ZHhrTIVcxLHDMomv9~Z1g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsStrap::StrapWidthWings

Specifies the width of the strap including the wings, if the wings are available.
If the value is either zero or less than StrapWidthInside plus 2 times StrapThickness, (StrapWidthInside + 2 \* StrapThickness), then the software does not draw the wings. This attribute value affects the position
of the gussets.

![Pipe Saddle - Strap Att - Strap Width Wings](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v74mv2fT2ldnhXyCuKt2Jg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a64bfe28735d0101)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/v74mv2fT2ldnhXyCuKt2Jg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Occurrence Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775250?contentId=DuhoP5_eI~p_THUZIivZTg)
IJOAhsPipeOD::PipeOD

Specifies the actual outside diameter of the pipe or the insulation. The Assembly
Information Rule (AIR) in Visual Basic or Custom Support Definition (CSD) in .NET
passes the PipeOD value, but you can manually set the value as well. This attribute is used to position
the strap vertically along with the StrapTopGap.


None: 

* The software displays a warning if the PipeOD value is greater than StrapWidthInside value.
* The software does not display a warning if the rectangular straps or the blocks interfere
  with the pipes.
* The software does not get the PipeOD value from the supported pipe because the strap might be attached to a different
  piece of pipe within the assembly or might need to go outside the insulation.

IJUAhsBottomShapeType::ShapeType

Specifies the codelist value for the bottom shape.

1 - Round  
2 - Rectangular

IJUAhsBottomShapeWidth::Width

Specifies the width of the bottom shape. This value must be greater than zero. If
the bottom shape is 1, round, then the width is equal to the length.

![Pipe Saddle - Occu Att - Bottom Shape Width](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XFiQU1C3oh2dnEYLIP9_Uw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a69b8bf32d906745)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XFiQU1C3oh2dnEYLIP9_Uw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsBottomShapeLength::Length

Specifies the length of the bottom shape. This value must be greater than zero. If
the bottom shape is 1, round, then the width is equal to the length.

![Pipe Saddle - Occur Att - Bottom Shape Lenght](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DGZKSGNyrk~FOP73ku62iw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2ee342ae1037e750)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DGZKSGNyrk~FOP73ku62iw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsBottomShapeHeight::Height

Specifies the height of the bottom shape calculated from the center of the pipe to
the bottom end of the bottom shape. This value must be greater than half the outer
diameter and thickness of the strap.

![Pipe Saddle - Occur Att - Bottom Shape Height](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7FbVQmR8aX8IJzrGkJvPjQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=99b078a23269f9b9)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7FbVQmR8aX8IJzrGkJvPjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic U-Bolt Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775509?contentId=qgxMJiIgPX23Lpc1mYO6CA)
Pipe saddle shares the following basic attributes with [U-Bolt SmartPart](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/TyLCfYNPdpUnjduzePisKg). These properties define the geometry of the U-Bolt.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of the dimensional value to use inches (for example 10in).

IJUAhsUBolt::UBoltWidth

Specifies the center-to-center distance between the legs of the U-Bolt. This value
is always greater than UBoltRodDia and determines the spacing of the vertical legs of the U-Bolt as well as the bend
radius for the curved part of the U-Bolt. The nominal bend radius is equal to half
the UBoltWidth dimension.


Image:[Image-Analysis: The image depicts a U-bolt, which is a type of fastener commonly used in various applications. The diagram shows the U-bolt bent in a U shape with an indication of its width labeled as "UBoltWidth." There are two red dots at the top of the U-bolt, which may signify measurement points for the width. The arrows on the left and right sides indicate the measured width of the U-bolt. This image is likely used to explain how to measure the width of a U-bolt for selection or installation purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJqQSyiRwTC0agczEtLbBA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HJqQSyiRwTC0agczEtLbBA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltCenterToEnd

Specifies the distance from the pipe centerline to the end of the U-Bolt legs.


Image:[Image-Analysis: The image illustrates a U-bolt, commonly used in various applications such as securing or attaching materials. It shows a simplified diagram of the U-bolt with specific elements labeled. The red dots likely indicate measurement points or holes for fastening. The blue arrow points to a dimension labeled "UBoltCenterToEnd," indicating the distance from the center of the U-bolt to its end. This measurement is crucial for ensuring proper fit and alignment in construction or mechanical applications. Overall, the image serves to convey specific dimensional information about the U-bolt. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vz4BrTD5RMOrU2LumLLiWw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vz4BrTD5RMOrU2LumLLiWw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltRodDia

Specifies the diameter of the round stock used to make the U-Bolt. If this value is
zero, none of the U-Bolt shape is drawn (unless the UBoltDia2 is non-zero).


Image:[Image-Analysis: The image depicts a simplified diagram of a U-bolt with two red dots, which likely indicate the points of measurement or key features. Below the U-bolt, the text "UBoltRodDia" suggests that the image pertains to the diameter of the rod of the U-bolt. The U-bolt itself is characterized by its U shape and has two horizontal arms that extend and are secured with nuts. The arrows at the bottom indicate measurements, which may refer to the width or diameter of the bolt or rod. This diagram is useful for understanding the dimensions and specifications required in applications involving U-bolts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvEz4rkVYm8kdjgoUYZ_FA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XvEz4rkVYm8kdjgoUYZ_FA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2

Specifies a diameter change, for round insulation, coatings, or to delete the curved
part of the U-Bolt. If this value is greater than zero, changes the diameter of the
curved part of the U-Bolt starting at the position UBoltDia2Start as shown in Figure 1. This value can be larger or smaller than UBoltRodDia. If the value is zero, defaults to the same diameter as UBoltRodDia. If the value is less than zero, curved part of U-Bolt is not visible in the graphics
starting at the UBoltDia2Start as shown in Figure 2.


Image:[Image-Analysis: The image depicts a technical diagram of a U-bolt, which is a type of fastener commonly used in construction and machinery. The U-bolt has a curved shape with two straight legs extending downwards. There are red dots indicating certain measurement points on the U-bolt, and an arrow pointing to a label 'UBoltDia2', which likely refers to a specific diameter measurement relevant to this U-bolt. Additionally, there is a figure reference 'Fig. 1' in blue, suggesting this is part of a larger document or manual that contains multiple figures. It is important for the user to understand the specifications and measurements when working with U-bolts in their projects. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D10dzZamLGjDyeU7VIOlNA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D10dzZamLGjDyeU7VIOlNA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsUBolt::UBoltDia2Start

Specifies the start position of a diameter change and is used to represent round insulation,
coatings, or to delete the curved part of the U-Bolt. If UBoltDia2 is zero or the same as UBoltRodDia, then this value has no effect because there is no change in the rod diameter.


Image:[Image-Analysis: The image depicts a diagrammatic representation of a U-bolt, which is commonly used in various engineering applications to secure objects together. The U-bolt is shown in a primarily linear format with arrows indicating specific measurements. The red dots on the U-bolt likely represent point markers for alignment or placement, while the text "UBoltDia2Start" suggests a reference or measurement related to the diameter or starting point of the U-bolt. This might be a part of a technical guideline or specification related to dimensions in manufacturing or construction contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpEebZ8RTrkxMnYC3n7iog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/CpEebZ8RTrkxMnYC3n7iog-_PVFQNoCl4XmjAxWO0f7XQ/content)

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
###### [Nut Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775733?contentId=If4~IutK~qSGVrEzM7mobw)
Pipe saddle shares the following nut attributes with [U-Bolt SmartPart](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/TyLCfYNPdpUnjduzePisKg).

You can define properties for four different nuts or washers.


Image:[Image-Analysis: The image depicts a structural connection component involving existing steel. It showcases two cylindrical connectors at either end, which likely represent supports or connection points. The central part of the image includes the text "Existing Steel," indicating that this component connects to a steel member already in place. There are four labeled components (1, 2, 3, and 4) with arrows pointing towards them, suggesting they are parts of the assembly or elements of the connection. Component 1 and 2 could represent the bases of the connectors, while 3 and 4 likely denote additional structural features or markers relevant to the connection design. The red dots could indicate the points of interest or weld locations. Overall, this image serves to illustrate how this connector will interface with existing steel structures, highlighting key areas to focus on in the assembly or installation process. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vxJgF9AE2VHpoNJn9~kr6g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vxJgF9AE2VHpoNJn9~kr6g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Position of Nut 1 is immediately below existing steel
* Position of Nut 2 is below Nut 1
* Position of Nut 3 is Gap1 below bottom of pipe
* Position of Nut 4 is above Nut 3

IJUAhsShape1::Shape1Type

Determines the graphic shape used for the nut or washer using the codelist number
defined in the hsShapeType sheet in the HS\_S3DParts\_Codelist.xls workbook.


Image:[Image-Analysis: The image shows three shapes labeled with corresponding numbers and names. The first shape, labeled "1 - Round," is depicted as a circle. The second shape, labeled "2 - Square," is represented as a square. The third shape, labeled "3 - Hex," illustrates a hexagon. Each shape is outlined, and a small circle is present at the center of each shape, suggesting a point of focus or measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B8Dpm2sO7xpTuSXya5JIkg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/B8Dpm2sO7xpTuSXya5JIkg-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned codelist values are applicable for Shape2Type, Shape3Type, and Shape4Type as well.

IJUAhsShape1::Shape1Width1

Specifies the outside dimension of the nut or washer.


Image:[Image-Analysis: The image displays three geometric shapes along with their corresponding labels. Each shape represents a different category: 1 - Round (a circle), 2 - Square (a square), and 3 - Hex (a hexagon). The shapes are aligned vertically with lines indicating their dimensions, suggesting that the sizes for each shape might be relevant for measurement purposes or design specifications. The round shape is labeled "1," the square "2," and the hexagon "3," indicating a sequential listing or classification of shapes based on their geometry. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QvjRer4FtonQvCImmpWa8Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/QvjRer4FtonQvCImmpWa8Q-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Width1, Shape3Width1, and Shape4Width1.

IJUAhsShape1::Shape1Width2

Specifies the other outside dimension of the nut or washer.


Image:[Image-Analysis: The image illustrates different shapes and their effects, labeled with numbers. The first shape, labeled "1 - Round," is a circle, indicating some effect when the two arrows are placed beside it. The second shape, labeled "2 - Square," is a square, which also has arrows suggesting a similar effect. The third shape, labeled "3 - Hex," is a hexagon, but it states "No effect," indicating that there are no noticeable alterations or properties associated with it compared to the other shapes. The arrows appear to denote measurements or interactions related to each shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gVs~31axm~OXJk~H3S9~_A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gVs~31axm~OXJk~H3S9~_A-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Width2, Shape3Width2, and Shape4Width2.

IJUAhsShape1::Shape1Length

Specifies the thickness of the nut or washer.


Image:[Image-Analysis: The image consists of an arrangement of two arrows on the top, pointing towards a central vertical line, which represents a flow or movement towards something in the center. Below this, there is a rectangular figure divided into three horizontal sections. The top section is unfilled, while the middle section has two red squares, and the bottom section is also unfilled. This could represent a process or a component of a system where inputs are directed towards a certain action or output represented by the rectangular figure. The red squares may indicate a critical state or alert within this process. Overall, the image seems to depict a flow of information or control leading to a significant outcome or operation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/93xtGpp0AAgN0ESJPhWZ9A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/93xtGpp0AAgN0ESJPhWZ9A-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  The above mentioned dimensional notation is applicable for Shape2Length, Shape3Length, and Shape4Length.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt Count - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775734?contentId=mevwesEp0v5lh3eT3Tt~qw)
IJUAhsMulti1::Multi1Qty

Specifies the quantity of U-Bolts for the yoke clamp.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the location value for the U-Bolts.


None:  If the value for the above mentioned attributes is zero, the software does not display
the U-Bolt.

1 - Single


Image:[Alt-Text: U-BOlt 
Image-Analysis: The image is a simple diagram of a clamp mechanism, illustrating how the clamping action works to secure an object. It shows a vertical post with a handle at the top, which can be turned to move the clamping plate up or down. The horizontal plate represents the surface that applies pressure on the object being held. The bottom part is the grip that is attached to the workbench or surface, emphasizing the clamp's function of holding items firmly in place. This design illustrates the basic mechanics of a clamp, useful in various woodworking and metalworking tasks. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BPhti5YFcNzUFzzWYfTLmw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![U-BOlt](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BPhti5YFcNzUFzzWYfTLmw-_PVFQNoCl4XmjAxWO0f7XQ/content)

2 - Double

![Pipe Saddle SmartPart - U-Bolt Count - Double](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P8qOhVJ2MKB7VJMDgc8C~Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6b5721fc4108257f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P8qOhVJ2MKB7VJMDgc8C~Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

For more information about placement options, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775515?contentId=YcZ~RY_4p5HIp~Xcq_Xo_A)
The following graphic illustrates the orientation of the ports and their sizes for
the pipe saddle:

![Pipe Saddle SmartPart - LCS](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0ucCN7w_EyaB3iJqMe7SjQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f6a00fdb098610d8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0ucCN7w_EyaB3iJqMe7SjQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

If RotY is set, the software rotates the route port about its y-axis, tilting the
strap when the strap is joined to the pipe reference port.

Port details and their orientation

Port1 - Route (0,0,0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 2 - Route | Pipe outside diameter | Pipe outside diameter | Pipe outside diameter |

Port2 - Steel (0,0, -Bottom Shape height)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1011 - Steel | N/A - Use 0 | N/A - Use 9999 | N/A - Use 9999 |


None:  If you join the steel port to the structure, the steel port must be at the BottomShapeHeight. To add a plate below, use BottomOfStrap - Gap1 - Block1Height.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/775530?contentId=rWEWEKOU_Ph8KnuRHc69jA)
The BOM description must use the part description and is not defined within the symbol
code. The IJHgrBOMDefinition::BomType attribute is set to 2.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313103?contentId=jKBijHXKs1JNPQC8JYgnOg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgIDs: HS\_S3DPlate.OneStdOneHoleOneRoute, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.RoutePort,
HS\_S3DPlate.RoutePortOnly, HS\_S3DPlate.ThreeHolePort, HSSmartPart,Ingr.SP3D.Content.Support.Symbols.TwoHolePort,
HSSmartPart,Ingr.SP3D.Content.Support.Symbols.TwoStandardPort, HS\_S3DPlate.WithBasePlate,
HSSmartPart,Ingr.SP3D.Content.Support.Symbols.OneStdOneHole, and HSSmartPart,Ingr.SP3D.Content.Support.Symbols.OneStdTwoHole  
Part Name: Plate  
Part Description: Plate SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RR6HKpMb6sojUJdPC0p4Fg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f6d031e14eb34f8f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RR6HKpMb6sojUJdPC0p4Fg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Plate SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity:  and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Plates > Stop Plate - Top End of Steel Section as shown below.


Image:[Image-Analysis: The image represents a hierarchical structure or tree diagram of different components categorized under "Parts." At the top level, there are subcategories including "SmartParts" and "S3D Standard." Within "S3D Standard," there are several categories such as "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," and "Rod Fittings." Under the "Plates" category, there are two items: "Connection Plate - One Hole" and "Connection Plate - Two Hole." Additionally, the "Stop Plate - Top End of Steel Section" is highlighted, indicating it is a specific part under the "Plates" category. Overall, this structure allows for organized navigation through various engineering components and assemblies. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T5yk9sfHZNxG0IodYTBCbg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T5yk9sfHZNxG0IodYTBCbg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches.

Ports are shown as points highlighted in red.

Local Coordinate System

Standard Port

The standard ports are always initially aligned with the X axis on the width of the
plate shape, the Y axis is along the length of the plate shape, and the Z axis is
along the thickness of the plate.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T11~PFDw~lEeVEQRVor3ZA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=b90f6d31d4f5db9b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T11~PFDw~lEeVEQRVor3ZA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Hole Port

The hole ports are aligned so that they should easily connect to other parts that
connect to a hole. The Y axis is through the hole (with the thickness of the plate
shape), the Z axis is along the length of the plate towards the top, and the X axis
is along the width of the plate shape.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WHFAi1QYlIVjqU9BYXNPmQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=9b774a00fcf8007b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WHFAi1QYlIVjqU9BYXNPmQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Route Port

The route port is aligned so that you can easily connect the part to pipe. The X axis
is aligned with the route, the Z axis goes towards the plate shape along the length
of it, and the Y axis is along the thickness of the plate shape.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nNn5ziW4QcyTyulIVex2Ag-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6a0b120e12741794)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nNn5ziW4QcyTyulIVex2Ag-_PVFQNoCl4XmjAxWO0f7XQ/content)

You can alter the port orientations of the plates using the various rotations that
are exposed on the port properties in the XLS.

ProgID Selection

Based on the ports required, select the appropriate ProgID as follows:

|  |  |
| --- | --- |
| ProgID | Description |
| HS\_S3DPlate.OneStdOneHoleOneRoute | Plate with one standard port, one hole port and one route port |
| HS\_S3DPlate.OneStdOneHole | Plate with one standard port and one hole port |
| HS\_S3DPlate.OneStdTwoHole | Plate with one standard port and two hole ports |
| HS\_S3DPlate.RoutePort | Plate with one route port and two standard ports |
| HS\_S3DPlate.RoutePortOnly | Plate with only one route port |
| HS\_S3DPlate.ThreeHolePort | Plate with three hole ports |
| HS\_S3DPlate.TwoHolePort | Plate with two hole ports |
| HS\_S3DPlate.TwoStandardPort | Plate with two standard ports |
| HS\_S3DPlate.WithBasePlate | Plate with a base plate |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313110?contentId=nDCFSvh0RTDRRfop1g1FUw)
These properties define the geometry of the plate.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of dimensional value to use inches.

IJUAhsWidth1::Width1

Specifies the width of the basic rectangular plate shape. This value must be greater
than zero.


None: 

IJUAhsLength1::Length1

Specifies the length of the plate. This value must be greater than zero.


Image:[Image-Analysis: The image depicts a rectangular shape with a label next to it. The label indicates a vertical measurement, titled "Length1". This suggests that "Length1" refers to the height or vertical dimension of the rectangle. The image serves to represent the concept of length as a specific measurement associated with the rectangular shape. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6MwIn9i~4jOsH45wJMn2WA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6MwIn9i~4jOsH45wJMn2WA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the basic rectangular plate shape. This value must be greater
than zero.


Image:[Image-Analysis: The image illustrates two rectangular shapes—one larger on the left and a smaller one on the right—separated by a dashed line. Below the smaller rectangle, there is an arrow pointing towards it, marked with the word "Thickness1." This suggests a graphical representation of thickness measurement of the smaller rectangle, indicating that "Thickness1" refers to the measurement of the dimension separating the two objects, possibly in a technical or engineering context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/piOkRBwl2soBv~c7lYSlPQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/piOkRBwl2soBv~c7lYSlPQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Corner Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313114?contentId=C3yNJ6Ox7n_~BpEIoQdGpQ)
These properties define specifications for each corner and use the following short
codes:

* TL=TopLeft
* TR=TopRight
* BL=BottomLeft
* BR=BottomRight.

The following properties are optional. They are used for different corner shapes for
the plate.


Image:[Image-Analysis: The image depicts a rectangular shape with labeled sides indicating the cardinal directions: Top, Bottom, Left, and Right. It also includes two arrows: one pointing downwards labeled "Z" and one pointing to the right labeled "X". These arrows suggest a defined orientation or direction associated with the rectangle, possibly indicating a coordinate system or the positioning of certain elements within this space. The labels and arrows help in understanding the spatial arrangement and can be used to describe movement or direction within the rectangular area. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fev~JyG6dyEQOngpckuQaw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fev~JyG6dyEQOngpckuQaw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerType

Specifies the corner type for the shape of the top left corner of the plate shape.
The value for this column is a codelist number defined in the hsCornerShape sheet in the HS\_S3DParts\_Codelist.xls workbook. Valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet. Similar properties exist for the other three corners. Codelist number and
CornerType are listed below.

0 – None

1 – [Rectangular Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/5JZpzrokHwtCxyVlbmOGGw)


look for an icon that resembles a piece of paper or a file with a folded corner, indicating a document or file: 

2 – [Angled Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/nypn9~Qx5FL4Qze6ERSBMg) – XY Chamfer

3 – [Angled Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/nypn9~Qx5FL4Qze6ERSBMg) – XY Edges

4 – [Angled Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/nypn9~Qx5FL4Qze6ERSBMg) – X with angle

5 – [Angled Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/nypn9~Qx5FL4Qze6ERSBMg) – Y with angle


look for an icon that resembles a folded piece of paper or a document with a corner turned down: 

6 – [Rounded Notch Corner (Concave)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/1ijNpSOLit587WvACEOABA)


look for a rectangular shape with a cut-out at the top left corner resembling a piece of paper or a legal document: 

7 – [Round Corner (Convex)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/xt5sMRiRzxvxiye0_fElXQ)


look for icon that looks like a rounded rectangle or a partial rectangle with curved top edge: 

IJUAhsTLCorner::TLCornerX

Specifies the horizontal dimension of the corner shape.

IJUAhsTLCorner::TLCornerY

Specifies the vertical dimension of the corner shape.

IJUAhsTLCorner::TLCornerRadius

Specifies the radius for the corner shape.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rectangular Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313120?contentId=5ROcNTcbAhN54KfxT6tFPg)
IJUAhsTLCorner::TLCornerType

Specifies the corner type. Enter codelist value 1 for this corner type. Valid codes
are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsCornerShape sheet.

Codelist hsCornerShape 1 – Rectangular Notch


look for an icon that resembles a blank document with a folded top corner: 

IJUAhsTLCorner::TLCornerX

Specifies the horizontal size of the rectangular notch. The value must be positive
and less than the Width1 value.


None: 

IJUAhsTLCorner::TLCornerY

Specifies the vertical size of the rectangular notch. The value must be positive and
less than the Length1 value.


Image:[Image-Analysis: The image depicts a graphical representation of a corner in a structure, labeled as "TLCornerY". It shows a top-left corner, typically used in design or architectural diagrams. The diagram includes arrows indicating direction and structure orientation. The vertical arrow pointing down suggests a vertical alignment while the horizontal line indicates a boundary or edge at the top. This could represent how different design elements meet at the corner, highlighting a corner joint or transition in a design layout. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GiDZK3pLN4zpwV0r7doZfg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GiDZK3pLN4zpwV0r7doZfg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerRadius

This value is ignored.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Angled Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313123?contentId=XC2f_HU~EVkgV5BDXwLsjg)
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


Image:[Image-Analysis: The image shows two diagrammatic representations that might depict different sets or categories, labeled with X and Y. Each diagram has two sections that could be indicating relationships or intersections between the sets represented by X and Y. This visual may represent concepts such as Venn diagrams, where the regions define the relationship between two entities, or they could symbolize different possible outcomes or choices within a decision-making framework. The positioning of X and Y in relation to each other suggests a focus on their interaction or contrasts, although further context is needed to fully understand their implications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lkejH4aCq9fAjoXOrgypYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/lkejH4aCq9fAjoXOrgypYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rounded Notch Corner (Concave) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313124?contentId=xFzvInHo2UpGGuBOgr7Gfw)
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


Image:[Image-Analysis: The image depicts a simple diagram representing a storage system or container. It shows arrows pointing inwards at the top, indicating input or reception of materials or items, and a curved opening suggesting a space where these items can be added. Below, there is a rectangular base, which may represent the main body of the container that holds the materials. This arrangement signifies a way to collect or receive objects efficiently while possibly implying a mechanism for controlling the amount of material received from the top opening. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kIdKyIGRPqM7gqauMpSpPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kIdKyIGRPqM7gqauMpSpPg-_PVFQNoCl4XmjAxWO0f7XQ/content)

If a negative value is set, then the software will move the center point away from
the plate horizontally. This will reduce the sweep angle of the notch shape so it
will be less than a quarter-circle and the joint with one edge is no longer perpendicular.

X < 0, Negative Offset


Image:[Image-Analysis: The image depicts a simple diagram that illustrates the process of folding a piece of paper or a similar material. The arrows on the left and right sides suggest that the paper is being folded towards the center, indicated by the shape of the folded edge. The plus sign in the middle suggests that there is an additional action or a reference point involved, possibly representing alignment or a crease in the paper where the fold occurs. The final box shape on the right indicates the resulting form after the folding has taken place. Overall, it conveys a straightforward method of paper folding. 
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


Image:[Image-Analysis: The image depicts a simple circuit diagram that appears to represent a capacitor with a connected switch. The vertical line with the arrow at the top signifies the positive side of the circuit, while the horizontal line with the plus sign denotes the positive terminal of the capacitor. The bottom features another line that indicates the negative terminal or ground level, completing the circuit's path. The curved line on the right suggests a rounded edge, which could represent a portion of a larger circuit component, possibly indicating that it is part of a more complex electrical system. Overall, this diagram illustrates the basic connections and polarity associated with a capacitor and how it may be positioned within a circuit. 
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
less than that of available Length1.

If this value is set to zero, then the software will create a sharp corner edge.


Image:[Image-Analysis: The image portrays a schematic representation of a process or system. It includes a rectangular shape representing an object or location, and an arrow pointing towards it from the side, indicating a specific action or movement towards that object. There is also a plus sign next to the arrow, suggesting the addition or entry of something into the rectangular area. The use of the arrow and plus sign collectively signifies a flow of information or resources into the space represented by the rectangle. This could be interpreted in various contexts such as inputting data, adding resources, or even a physical entry point. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiDgsIRtGHZBebeMBvxeSw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IiDgsIRtGHZBebeMBvxeSw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Round Corner (Convex) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313125?contentId=I0ewbliudPDHgOp1I6r13A)
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


Image:[Image-Analysis: The image depicts a diagram illustrating the process of bending or folding. It shows two arrows pointing towards a curved line, suggesting movement or action inwards and the resulting shape of a document or sheet that is being folded. The curved line indicative of the fold is accompanied by a rectangular shape representing the document. This diagram could represent instructions for a manual task, possibly in the context of paper folding or material manipulation. The vertical lines at the top and bottom further imply control or boundaries in this folding action. 
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


Image:[Image-Analysis: The image depicts a basic circuit diagram component known as a capacitor. It features two parallel lines, which represent the plates of the capacitor. The left side shows a vertical rectangle with a label for positive and negative connections, indicating the direction of voltage (with the plus sign representing positive and the minus sign representing negative). The arrows adjacent to the capacitor indicate the flow of current, suggesting the function of the capacitor in storing and releasing electrical energy in a circuit. This diagram highlights the role of capacitors in electronic circuits, particularly in smoothing out fluctuations in voltage. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MRZu5VG8yT1mjZP4E6l0mA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MRZu5VG8yT1mjZP4E6l0mA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner::TLCornerRadius

Specifies the radius of the round notch shape.

If the radius is needed in X + direction, the value must be greater than zero but
less than that of available Width1.

If the radius is needed in Y + direction, the value must be greater than zero but
less than that of available Length1.

If this value is set to zero, the software will create a sharp corner edge.


look for an icon that resembles a sheet of paper with a folded corner and an arrow pointing towards the paper: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Clamp Attributes - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/777221?contentId=QGl1N_~P1xhcmHN6ULf4OA)
IJUAhsDiameter1::Diameter1

Specifies the outside diameter of the pipe.

![Grip Pipe Clamp - Basic Attributes - Diameter1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NS4QK_0o2pu1j7FtZnmumg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bf64de37f718205f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NS4QK_0o2pu1j7FtZnmumg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height from the center of the pipe to the center of the pin at the top
of the clamp.

IJUAhsHeight2::Height2

Specifies the height from the bottom of the clamp to the center of the pipe.

![Grip Pipe Clamp - Basic Attributes - Height1/Height2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~aF8BVRByJd3qD_V_0U6WQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=190ddd34ade0469c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~aF8BVRByJd3qD_V_0U6WQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOffset1::Offset1

Specifies the vertical distance from the center of the pipe to the top end of the
rod, along the central axis of the rod.

IJUAhsOffset2::Offset2

Specifies the vertical distance from the center of the pipe to the bottom end of the
rod, along the central axis of the rod.

IJUAhsOffset3::Offset3

Specifies the distance from the center of the pin to the top of the grip clamp.

![Grip Pipe Clamp - Basic Attributes - Offset1, 2, 3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LzVv7hPKIxVh~JRN1EiiBQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=da827e7aeae09c92)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/LzVv7hPKIxVh~JRN1EiiBQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle1::Angle1

Specifies the angle between the central axis of the rod and the vertical axis of the
clamp at the top end of the clamp, along the perpendicular plane of the pipe axis.

IJUAhsAngle2::Angle2

Specifies the angle between the central axis of the rod and the vertical axis of the
clamp at the bottom end of the clamp, along the perpendicular plane of the pipe axis.

IJUAhsRodDiameter::RodDiameter

Specifies the diameter of the rod that encircles the pipe.

![Grip Pipe Clamp - Basic Attributes - Angle1, 2, RodDiameter](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g5jUSOVRkZ37sNBOv2_dHw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=adc11185d6ceec27)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g5jUSOVRkZ37sNBOv2_dHw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth1::Width1

Specifies the Width1 of the grip pipe clamp.

IJUAhsThickness1::Thickness1

Specifies the Thickness1 of the grip pipe clamp.

IJUAhsWidth2::Width2

Specifies the Width2 of the grip pipe clamp.

IJUAhsThickness2::Thickness2

Specifies the Thickness2 of the grip pipe clamp.

![Grip Pipe Clamp - Basic Attributes - Width1, Thickness1, Width2, Thickness2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8TwOENWoMNEyHyDN_iJt9Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=8babcbe718e775ff)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8TwOENWoMNEyHyDN_iJt9Q-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Curved End Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313126?contentId=R~UV5A4gf4TmrxR0tjfNdw)
These properties define a curved end at top edge.

IJUAhsCurvedEndType::CurvedEndType

Specifies the type of curve end, whether concave or convex and is applicable to TwoHolePort
or RoutePort. This property uses the following codelist values:

1 - Concave


icon-description of a rectangular shape with a semi-circular top cutout: 

2 - Convex


look for icon that looks like a shopping bag with a rounded top: 

IJUAhsCurvedEnd::CurvedEndRad

Specifies the radius of the curved end, concave shape in top edge. This value must
be positive. The curved edge is not seen if this value is zero.


Image:[Image-Analysis: The image depicts a shape with a specific feature called "CurvedEndRad." This shape appears to have a rectangular body with one end featuring a curved cutout. An arrow points towards the curved end, indicating a special attribute or modification at that part of the shape. This representation suggests that the shape is part of a design or graphical representation, possibly used in technical drawings or CAD (Computer-Aided Design) applications to denote a specific curvature at the end of a structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vqwxLC3Ssja_qNC1DHFovQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vqwxLC3Ssja_qNC1DHFovQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCurvedEnd::CurvedEndX

Specifies the horizontal offset of the curve center point. The default position is
center of plate. Positive values offset the center point to the right. Negative values
offset the center point to the left. The end points of the curve must remain on the
top edge that remains after corner treatments are applied.

Positive X offset


Image:[Image-Analysis: The image showcases a geometric representation of a shape tagged "CurvedEndX." This shape includes a rectangular section on the left with a semicircular cutout on the right. The left side has arrows pointing towards the center indicating symmetry, while the dashed vertical line in the middle signifies a central axis. The curved section suggests an end that is rounded, which could be relevant in design contexts where fluidity and a non-angular shape are needed. This depiction might be used in engineering or technical drawings where specific shapes are required for components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RsnPJ59A8w4z2Ct1vTHTTw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/RsnPJ59A8w4z2Ct1vTHTTw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsCurvedEnd::CurvedEndY

Specifies the vertical offset of the curve center point. The default position is top
edge of plate. Positive values offset the center point up, off the plate, as for a
pipe centerline. Negative values offset the center point down, into the plate. The
absolute value of CurvedEndY must be less than that of CurvedEndRad.

Positive Y offset


Image:[Image-Analysis: The image depicts a graphical representation of a shape called "CurvedEndY." It illustrates a curved endpoint where the upper side features a non-linear curve, while the left and right sides appear straight, creating a rectangular-like structure with a rounded end. There are directional arrows indicating the way to manipulate or modify the shape. The top arrow points downward towards the curved section, while the side arrows imply adjustments or dimensions related to the shape. This setup suggests that "CurvedEndY" could be part of a technical diagram or design specification, likely used in engineering or graphic design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9vB7PN96TnIkErDlCPfjMA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/9vB7PN96TnIkErDlCPfjMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Negative Y offset


Image:[Image-Analysis: The image depicts a technical diagram of a "Curved End Y" component. At the top, there is a text label indicating the name of the component, "CurvedEndY." Below the text, there are arrows pointing upwards and downwards, which often represent a flow direction or movement in mechanical drawings. To the right, there is a semi-circular shape with an arrow indicating the arc direction. This suggests that the "Curved End Y" has a design that includes curves, typically found in components that connect different pathways. Overall, the image is likely related to engineering or design, explaining the general shape and function of the component in a schematic format. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rV8v9iKLP5sTlHD0zbMm0w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rV8v9iKLP5sTlHD0zbMm0w-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Base Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313127?contentId=qWMSckk2hYOVBVE_XJZfAA)
By including the following columns in the XLS sheet, you can see additional base plate
or box. The base plate graphic is formed on the perpendicular face of the plate. You
can use the following Prog ID to include the additional base plate.

Prog ID: HS\_S3DPlate.WithBasePlate

IJUAhsWidth2::Width2

Specifies the width of the base plate graphic, along the Width1 of the plate graphic. This value must be greater than zero.


Image:[Image-Analysis: The image shows a simple diagram representing a rectangular shape with an annotation about its width. The rectangle is depicted with arrows on the sides indicating that it has a width measurement of 2 units. The focus is on the dimension labeled as "Width2", which suggests that this is either a graphical representation for a physical object or a conceptual illustration used in design-related contexts. This could be relevant in fields such as construction, architecture, or graphic design, where understanding dimensions is crucial. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kc7WrrbcDw6dGRgwqLNotA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kc7WrrbcDw6dGRgwqLNotA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the length of the base plate graphic, along the Thickness1 of the plate graphic. This value must be greater than zero. If the plate is a fixed
length item, use this interface instead of the previous system occurrence attribute
Length.


Image:[Image-Analysis: The image shows a simple rectangular shape with the label "Length2" next to it. This implies that the height or vertical measurement of the rectangle is being referred to as "Length2". There are also arrows indicating the measurement direction, which suggests that this is an illustration meant to explain how to measure the length of the rectangle along the vertical dimension. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AAsd8QQ5msnXI7Lxp1_5nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AAsd8QQ5msnXI7Lxp1_5nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the base plate graphic, along the Length1 of the plate graphic. This value must be greater than zero.


Image:[Image-Analysis: The image depicts a comparison between two different rectangular objects. On the left, there is a wider rectangular shape, and on the right, there is a narrower, taller rectangular shape. The image includes a label indicating "Thickness2" which suggests that it refers to the thickness measurement of the right rectangle. The visual representation implies a comparison of dimensions, particularly focusing on the thickness of the two shapes, highlighting their differences in thickness and height. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HMfpBR29Xe9BVzr15MuJJw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HMfpBR29Xe9BVzr15MuJJw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bolt Holes Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313128?contentId=Up7aaT2VHwHI6ThdTqQ_uQ)
For base plates with bolt holes, specify the size, quantity and positions using these
properties. The graphics of the plate do not show the bolt holes, but these properties
are used by assemblies.

These properties define the number of bolts and their locations in each row and the
number of rows using two multiple location specifications. Multi1 is positioned along
the width of the plate. Multi2 is positioned along the length of the plate. The Multi1
specification specifies the row; for the example below, Multi1Qty = 3. The Multi2
specification defines how many of these rows there are; for the example below, Multi2Qty
= 2.


Image:[Image-Analysis: The image shows a rectangular shape representative of a physical object, indicating its dimensions with the labels "WIDTH" and "LENGTH." The terms "MULTI1" and "MULTI2" are placed at two sides, possibly referring to either multiplication factors or variables associated with the width and length. The image provides a clear visual reference for understanding the spatial attributes of the rectangle, potentially within a geometrical or mathematical context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ecA0xMS1bCL9J4SU7cPS5Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ecA0xMS1bCL9J4SU7cPS5Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsMulti1::Multi1Qty

Specifies the quantity of bolt holes along the width of the plate.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the location of bolt holes along the width of the plate.

IJUAhsMulti2::Multi2Qty

Specifies the quantity of bolt holes along the length of the plate.

IJUAhsMulti2::Multi2LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti2::Multi2Location

Specifies the location of bolt holes along the length of the plate.

IJUAhsDiameter1::Diameter1

Specifies the bolt hole diameter.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313129?contentId=mKqSaa_6JJYNdOWQsgOyNw)
Standard Port

The maximum limit of standard ports is two. By default, port 1 is placed at the center
of the plate shape on the bottom surface and port 2 is placed at the center of the
plate shape on the upper surface.

IJOAhsStandardPort1::P1xOffset

Enter a value to move the port on the X-axis. Both positive and negative values are
valid.

IJOAhsStandardPort1::P1yOffset

Enter a value to move the port on the Y-axis. Both positive and negative values are
valid.

IJOAhsStandardPort1::P1zOffset

Enter a value to move the port on the Z-axis. Both positive and negative values are
valid.

IJOAhsStandardPort1::P1Rotx

Enter a value to rotate the port about the X-axis.

IJOAhsStandardPort1::P1Roty

Enter a value to rotate the port about the Y-axis.

IJOAhsStandardPort1::P1Rotz

Enter a value to rotate the port about the Z-axis.

IJOAhsStandardPort2::P2xOffset

Enter a value to move the port on the X-axis. Both positive and negative values are
valid.

IJOAhsStandardPort2::P2yOffset

Enter a value to move the port on the Y-axis. Both positive and negative values are
valid.

IJOAhsStandardPort2::P2zOffset

Enter a value to move the port on the Z-axis. Both positive and negative values are
valid.

IJOAhsStandardPort2::P2Rotx

Enter a value to rotate the port about the X-axis.

IJOAhsStandardPort2::P2Roty

Enter a value to rotate the port about the Y-axis.

IJOAhsStandardPort2::P2Rotz

Enter a value to rotate the port about the Z-axis.

Route Port

The route port helps to place a plate to a route. Only one route port per plate is
allowed.


None:  In the descriptions below, there is reference made to Pipe CL (centerline). While
there is no actual Pipe CL, this is the imaginary pipe centerline where you can envision
the pipe that you are connecting to running. The Pipe CL is always located off of
the bottom edge of the plate shape. All of the offsets are in reference to this Pipe
CL.

IJOAhsRoutePort::RPDiameter

Specifies the route diameter. The port is offset from the graphics by this value.


None:  This value does not have to be just the route diameter; it can also include the pad
thickness, insulation thickness, etc.

IJOAhsRoutePort::RPOffsetfromPipeCL

Specifies an offset from the Pipe CL moving perpendicular. If a non-zero value is
entered, the port will be offset and the graphics of the plate will be extended so
that they appear to reach the outside of the diameter specified.

IJOAhsRoutePort::RPOffsetalongPipe

Enter a value to move the port along the Pipe CL. Both positive and negative values
are valid.

IJOAhsRoutePort::RPRotationAroundPipe

Enter a value to rotate the pipe port about its X-axis. Both positive and negative
values are valid.

IJOAhsRoutePort::RPAdjustPlateLength

Enter the codelist value that specifies whether or not the length of the plate will
be adjusted to meet the curve of the route when RPOffsetalongPipe is not 0. Values are 1 meaning yes and 2 meaning no.

Hole Port

The hole port is used only for plates that only connect via holes. This does not include
bolt holes. The hole port cannot be offset but it can be rotated about the X, Y or
Z axis. There can be a maximum of three hole ports. All of them have the same inputs.

IJOAhsHolePort1::HP1Rotx

Enter a value to rotate the port about the X-axis.

IJOAhsHolePort1::HP1Roty

Enter a value to rotate the port about the Y-axis.

IJOAhsHolePort1::HP1Rotz

Enter a value to rotate the port about the Z-axis.

IJOAhsHolePort1::HP1PosX

Enter the position, from the plates bottom left (0,0,0), in the X direction.

IJOAhsHolePort1::HP1PosY

Enter the position, from the plates bottom left (0,0,0), in the Y direction.

IJOAhsHolePort1::HP1Size

Enter the size of the hole.

IJOAhsHolePort2::HP2Rotx

Enter a value to rotate the port about the X-axis.

IJOAhsHolePort2::HP2Roty

Enter a value to rotate the port about the Y-axis.

IJOAhsHolePort2::HP2Rotz

Enter a value to rotate the port about the Z-axis.

IJOAhsHolePort2::HP2PosX

Enter the position, from the plates bottom left (0,0,0), in the X direction.

IJOAhsHolePort2::HP2PosY

Enter the position, from the plates bottom left (0,0,0), in the Y direction.

IJOAhsHolePort2::HP2Size

Enter the size of the hole.

IJOAhsHolePort3::HP3Rotx

Enter a value to rotate the port about the X-axis.

IJOAhsHolePort3::HP3Roty

Enter a value to rotate the port about the Y-axis.

IJOAhsHolePort3::HP3Rotz

Enter a value to rotate the port about the Z-axis.

IJOAhsHolePort3::HP3PosX

Enter the position, from the plates bottom left (0,0,0), in the X direction.

IJOAhsHolePort3::HP3PosY

Enter the position, from the plates bottom left (0,0,0), in the Y direction.

IJOAhsHolePort3::HP3Size

Enter the size of the hole.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/313130?contentId=E4A1MRfvnIS05Wq5nbUz_g)

Image:[Image-Analysis: The image presents a comparison between two sets of entity attributes organized in a tabular format. On the left side, the header is labeled "Hg(SymbolPort(1))", which indicates various attributes related to the first symbol port, while the right side refers to "Hg(SymbolPort(2))", denoting attributes for a second symbol port. Each set contains similar attributes like Name, PortType, Size (with MinSize and MaxSize), and UnitType, which are crucial for defining the characteristics and specifications of the respective symbol ports. This layout suggests a parallel structure comparing the properties of two entities, highlighting their respective attributes for easy comparison and analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TO_~DInvQ3aTT2oc5RSfPA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TO_~DInvQ3aTT2oc5RSfPA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Other | 1200 | N/A - Use 0 | N/A - Use -9999 | N/A - Use -9999 |

Port2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Other | 1200 | N/A - Use 0 | N/A - Use -9999 | N/A - Use -9999 |

Port3 - Route

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Route | 2 | If the plate is made for a specific pipe size, then you need to set the Size, MinSize and MaxSize to that pipe size.  If the pipe size is a user input, set these to N/A. | N/A | N/A |

Port4 - Hole1

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Rod hole | 1004 | The depth of the hole, that is, the thickness of the plate. | 0 | Hole diameter |

Port5 - Hole2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Rod hole | 1004 | The depth of the hole, that is, the thickness of the plate. | 0 | Hole diameter |

Port6 - Hole3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Port Name | Port Type | Size | MinSize | MaxSize |
| Rod hole | 1004 | The depth of the hole, that is, the thickness of the plate. | 0 | Hole diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Plate Pipe Clamp - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724651?contentId=bAUWj1aPl~xfbwGDGsD7eQ)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PlatePipeClamp  
Part Name: Plate Pipe Clamp  
Part Description: Plate Pipe Clamp for Round Lugs / Flat Shear Lugs

![Plate Pipe Clamp](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XrO_dBOck52uEVGHOT3tZA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ab8c5164737b5d7b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XrO_dBOck52uEVGHOT3tZA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Use the following procedure to place a sample Pipe Clamp SmartPart delivered with
the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part, and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Pipe Clamps > Plate Pipe Clamp as shown in the following graphic.

   ![Plate Pipe Clamp - Catalog Location](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_~PhYBbzzYKTbvp24lC6sw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d58670b379aceaaf)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/_~PhYBbzzYKTbvp24lC6sw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image shows a technical diagram related to a pipe system. On the left, there is a circular representation of a pipe with an internal flow path resembling an S-shape or a loop, indicating some kind of fluid dynamics or flow characteristic. On the right side, there is a rectangular block with three axes labeled X, Y, and Z, indicating a 3D coordinate system. Below this system, there is a line of text stating “Pipe: 0,0,0”, which likely denotes a location or specification related to the pipe in a 3D space, possibly referring to its coordinates in a system where the origin point is at (0, 0, 0). This setup is often used in engineering and design to specify the position and orientation of components in a 3-dimensional space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rwDjuxu8WZVYU4R~T~FFpw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rwDjuxu8WZVYU4R~T~FFpw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Plate Pipe Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724654?contentId=BNyTBEWPoSUMFqPdSsNulw)
IJUAHsPltPipeClamp::PipeOD

Specifies the outer diameter of the pipe.


Image:[Alt-Text: Plate Pipe Clamp - Pipe OD 
Image-Analysis: The image depicts a technical diagram, likely related to mechanical or engineering concepts. It features a horizontal rectangular component with a circle at the center labeled "DIA," indicating diameter. The circle is surrounded by dashed lines, suggesting a measurement area or reference point. The two vertical lines in the diagram represent structural supports or guides that may hold or stabilize an object or mechanism. Overall, the image implies a focus on the dimensions and structural elements, important for ensuring proper fit or operation in an assembly or design context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dDXeufqU4BGV707T8BWj4Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Pipe OD](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dDXeufqU4BGV707T8BWj4Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPlatePipeClamp::TrunnionDiameter

Specifies the outer diameter of the trunnion.


Image:[Alt-Text: Plate Pipe Clamp - Trunnion Diameter 
Image-Analysis: The image depicts a technical diagram of a component, likely a mechanical or structural part. The focus is on the "Trunnion Diameter," which is labeled clearly in the diagram. The diagram shows a horizontal layout with a central circular feature representing the trunnion diameter. There are also several holes indicated, which suggest points for bolts or other fixtures. The arrows pointing towards the circle indicate that the dimension being referred to is specifically the diameter of the trunnion feature in the center of the diagram. This could be relevant in contexts such as engineering, manufacturing, or assembly processes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3BW7OcEDQSAq5UV4~s0bUQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Trunnion Diameter](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3BW7OcEDQSAq5UV4~s0bUQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Vertical Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724656?contentId=4i2Waq9am2yUhDxis5AINw)
IJUAhsPPCVerticalPlateShape::VerticalPlateShape

Specifies the vertical plate name required to draw the vertical plate.


Image:[Image-Analysis: The image depicts a technical drawing or schematic representation of a component, likely a type of base or mount used in engineering or machinery. The component shows an elongated rectangular shape with features such as circular and rounded ends. Notable features include two holes on each end, potentially for mounting purposes, and a larger, centrally located circular opening that could be for a shaft or other connection point. This design suggests that the component is meant for securing or supporting other equipment, indicating its role in a larger mechanical assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pXOJi0J7lxNAMZ56ffYk5g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pXOJi0J7lxNAMZ56ffYk5g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPPCVerticalPlateGap::VerticalPlateGap

Specifies the distance between two vertical plates.

![Plate Pipe Clamp - Vertical Plate Gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ydzo_jF5i92twxaB9GLilw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c166736aef759ef4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ydzo_jF5i92twxaB9GLilw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPPCVerticalPlateHeight::VerticalPlateHeight

Specifies the total height of the vertical plate. This value overrides the height
value in the shape service class.


Image:[Alt-Text: Plate Pipe Clamp - Vertical Plate Height 
Image-Analysis: The image is a technical drawing of a rectangular component, which likely represents a mechanical part such as a beam or frame. The drawing features labeled dimensions showing Length and Height, indicating the size of the object. The Length is depicted horizontally across the bottom of the component, while the Height is shown with a vertical arrow on the right side. There are also circular cutouts or holes marked in the center of the component, likely for mounting purposes. Overall, this image serves as a schematic to convey the dimensions and basic features of the component in a clear and precise manner. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iWxYB_GHYdAvVRjofD8czQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Vertical Plate Height](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/iWxYB_GHYdAvVRjofD8czQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPPCVerticalPlateLength::VerticalPlateLength

Specifies the total length of the vertical plate. This value overrides the length
value in the shape service class.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pipe Clamp Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724660?contentId=e5nBE~Cdp2i9wKgLwBCsnQ)
IJUAhsPPCClampPlate::ClampPlateShape

Specifies the name of the clamp plate name required to draw a clamp plate.

![Plate Pipe Clamp - Clamp Plate Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yyCMOF~O85ZnhE8QAvft4A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f1177460dfe28c4d)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yyCMOF~O85ZnhE8QAvft4A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset1X::Offset1X

Specifies the offset for pipe clamp along x-axis of the plate from the initial position
of the pipe clamp.

IJUAhsPPCOffset1Y::Offset1Y

Specifies the offset for pipe clamp along y-axis of the plate from the initial position
of the pipe clamp.

IJUAhsPPCOffset1Z::Offset1Z

Specifies the offset for pipe clamp along z-axis of the plate from the initial position
of the pipe clamp.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Middle Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724666?contentId=yDMKnB7uQujjgWtwygW3Uw)
IJUAhsPPCMiddlePlateShape::MiddlePlateShape

Specifies the name of the middle plate required to draw a middle plate.


look for an icon that resembles a rounded rectangle or a blank label shape: 

IJOAhsPPCMiddlePlateGap::MiddlePlateGap

Specifies the distance between two middle plates.

![Plate Pipe Clamp - Middle Plate Gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GQNqKjJQU0agVmA~eyqsSA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4233f5de9fc72602)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GQNqKjJQU0agVmA~eyqsSA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset2X::Offset2X

Specifies the offset for middle plate along x-axis of the plate.

IJUAhsPPCOffset2Y::Offset2Y

Specifies the offset for middle plate along y-axis of the plate.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724669?contentId=kzO4sNca1DR2OTSHP~_ljw)
IJUAhsPPCEndPlateShape::EndPlateShape

Specifies the name of the end plate required to draw an end plate.


Image:[Alt-Text: Plate Pipe Clamp - End Plate 
Image-Analysis: The image depicts a mechanical component that resembles a clamp or a bracket. It has a defined shape with a rounded top and is likely used for securing or holding objects together. The presence of bolts and threading at the sides suggests it is designed to attach to other materials or components, enabling stability. The circular hole at the top may serve for hanging or mounting purposes, indicating its functional versatility. Overall, this image represents a mechanical part commonly utilized in construction or mechanical assemblies. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~1hqRedOAkgbRDP5wkr63g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - End Plate](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~1hqRedOAkgbRDP5wkr63g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAHsEndPlt::EndPltGap

Specifies the distance between two end plates.

![Plate Pipe Clamp - End Plate Gap](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OEGFJDOFd7~DNBQ9zpCxFw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=10fed94918f98dba)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OEGFJDOFd7~DNBQ9zpCxFw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPPCEndPlateRot::EndPlateRotation

Specifies the angle of rotation for the end plates.

![Plate Pipe Clamp - Plate Rotation](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IFv7XehXEA50zDlFfPqyBQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=073c9ab5a975382a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IFv7XehXEA50zDlFfPqyBQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsPPCEndPlateLocateBy::EndPlateLocateBy

Specifies the location of the end plates:

* 0 - None
* 1 - Sets the location of the end plates to Center
* 2 - Sets the location of the end plates to Edge

You can locate individual bolts using one of the following rules:

1. relative to the center of the group
2. relative to edge

IJUAhsPPCOffset3X::Offset3X

Specifies the offset for the end plate along x-axis.

IJUAhsPPCOffset3Y::Offset3Y

Specifies the offset for the end plate along y-axis.

IJUAhsPPCOffset3Z::Offset3Z

Specifies the offset for the end plate along z-axis.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut1 Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724673?contentId=k82QotHShSp1L7xycUrpUQ)
IJUAhsPPCNut1Shape::Nut1Shape

Specifies the name of the bolt or the nut required to draw the bolt or nut.

![Plate Pipe Clamp - Nut1 Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d5a5fe0e1a826a23)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset4X::Offset4X

Specifies the offset between the first set of bolts from the center of the pipe plate
clamp.

![Plate Pipe Clamp - Nut1 - Offset1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XBW89rxOvhvtvyjpm3wjhA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=2133acccd512abf8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/XBW89rxOvhvtvyjpm3wjhA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset4Z::Offset4Z

Specifies the vertical offset between the first set of bolts from the center of the
pipe plate clamp.


Image:[Alt-Text: Plate Pipe Clamp - Nut1 - Offset1V 
Image-Analysis: The image depicts a technical drawing of a rectangular component, likely a mechanical part. The drawing features specific measurements, including a vertical arrow indicating a distance with a label stating "Offset 42," which suggests an important measurement related to the positioning or alignment of this component. Additionally, there are circular features (indicated by the small circles) which could represent mounting holes or other relevant points of interest. The overall structure is symmetrical, and the design conveys precision typically found in engineering schematics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SEw~BTP9_q0zllwSbTegVw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Nut1 - Offset1V](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SEw~BTP9_q0zllwSbTegVw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCNut1Qty::Nut1Quantity

Specifies the quantity of the bolts. Bolts are not displayed when the Nut1Quantity is set to zero.

IJUAhsPPCNut1Spacing::Nut1Spacing

Specifies the vertical distance between the bolt rows. This option is applicable only
when the Nut1Quantity is set to a value greater than 1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut2 Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724677?contentId=wNip7CYh9kuqk05Lf~dRHg)
IJUAhsPPCNut2Shape::Nut2Shape

Specifies the name of the bolt or the nut required to draw the bolt or nut.

![Plate Pipe Clamp - Nut1 Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d5a5fe0e1a826a23)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset5X::Offset5X

Specifies the offset between the second set of bolts from the center of the pipe plate
clamp.

![Plate Pipe Clamp - Nut2 - Offset](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrifGhlLzEAPHh6rhggJKQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7fa2233aac3a57b7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qrifGhlLzEAPHh6rhggJKQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset5Z::Offset5Z

Specifies the vertical offset between the second set of bolts from the center of the
pipe plate clamp.


Image:[Alt-Text: Plate Pipe Clamp - Nut2 - Offset 2V 
Image-Analysis: The image depicts a technical drawing of a component, likely a mechanical part or assembly. It features a rectangular shape with specific markings indicating dimensions and offsets. The term "Offset 5Z" suggests a measurement or adjustment related to the component's position in a Z-axis orientation (vertical direction in a standard Cartesian coordinate system). Arrows are provided to indicate the direction of measurement for the offset. The circular and possibly symmetrical features shown could imply mounting holes or functional aspects of the design. This drawing serves to provide precise information for manufacturing or assembly processes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vj2Ov2rCvKzfnD7bZEe3GQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Nut2 - Offset 2V](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Vj2Ov2rCvKzfnD7bZEe3GQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCNut2Qty::Nut2Quantity

Specifies the quantity of the bolts. Bolts are not displayed when the Nut2Quantity is set to zero.

IJUAhsPPCNut2Spacing::Nut2Spacing

Specifies the vertical distance between the bolt rows. This option is applicable only
when the Nut2Quantity is set to a value greater than 1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Nut3 Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724680?contentId=wWAOCRr6jWJfvc63ZC8n1Q)
IJUAhsPPCNut3Shape::Nut3Shape

Specifies the name of the bolt or the nut required to draw the bolt or nut.

![Plate Pipe Clamp - Nut1 Shape](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d5a5fe0e1a826a23)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/eQWga8TudtPYOsNXclxpjA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset6X::Offset6X

Specifies the offset between the third set of bolts from the center of the pipe plate
clamp.

![Plate Pipe Clamp - Nut3 - Offset3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Op6N9CxQKQNiRDxv1vl_4A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a78c46b7067049a8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Op6N9CxQKQNiRDxv1vl_4A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCOffset6Z::Offset6Z

Specifies the vertical offset between the third set of bolts from the center of the
pipe plate clamp.


Image:[Alt-Text: Plate Pipe Clamp - Bolt3 - Offset3V 
Image-Analysis: The image appears to be a technical diagram or line drawing of a component, possibly a bracket or mounting plate. It features a horizontal rectangular shape with rounded ends. There are two arrows pointing vertically towards the word "Offset 6Z," indicating a measurement or reference point labeled as "Offset." This suggests that this component has a specific offset dimension which is critical for its application. Additionally, there are two circular holes marked in the center, likely used for mounting purposes. Overall, this image conveys important schematic details necessary for understanding the positioning and specifications of the mechanical component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2mdTQWJyCGPduSJbHcAP2g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Plate Pipe Clamp - Bolt3 - Offset3V](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2mdTQWJyCGPduSJbHcAP2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsPPCNut3Qty::Nut3Quantity

Specifies the quantity of the bolts. Bolts are not displayed when the Nut3Quantity is set to zero.

IJUAhsPPCNut3Spacing::Nut3Spacing

Specifies the vertical distance between the bolt rows. This option is applicable only
when the Nut3Quantity is set to a value greater than 1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Hole Port Offsets - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/725556?contentId=yKoGSnnofuMu8jc11oEyYQ)
IJUAhsPPCOffset7X::Offset7X

Specifies the offset for port 2 along x-axis.

IJUAhsPPCOffset8X::Offset8X

Specifies the offset for port 3 along x-axis.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Maximum and Minimum Values - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/725557?contentId=wNTI2xYiEq2VQEu4lXBK~g)
IJUAhsPPC\_CCMinValue::CCMinimumValue

Specifies the minimum limit of C-C distance.

IJUAhsPPC\_CCMaxValue::CCMaximumValue

Specifies the maximum limit of C-C distance.

IJUAhsPPCMinHeight::MinimumHeight

Specifies the minimum height limit of the Plate Pipe Clamp.

IJUAhsPPCMaxHeight::MaximumHeight

Specifies the maximum height limit of the Plate Pipe Clamp.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724683?contentId=7RRwbnvkV3SuA~XMbgmEVg)
![Plate Pipe Clamp - Port Details](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m7NcPu6X3gHFAzrYSbfFVQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dd6f2da975dbe2cb)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/m7NcPu6X3gHFAzrYSbfFVQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 - Route

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1016 | Pipe outside diameter | N/A | N/A |

Port2 - Hole1

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004 | The depth of the hole, that is, the thickness of the plate. | 0 | Hole diameter |

Port3 - Hole2

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 10004 | The depth of the hole, that is, the thickness of the plate. | 0 | Hole diameter |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [BOM Description - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/724685?contentId=UVFk1BAdRYu~hJV6d8bS_Q)
The BOM description must use just the part description and is not defined in the symbol
code but has the IJHgrBOMDefinition::BomType property set to 2.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Protection Saddle - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317062?contentId=8XMDbmONxlxqd839uvOuZg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ProtectSaddle  
Part Name: Protection Saddle  
Part Description: Protection Saddle SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0Qp3Yy5RE4OVt78RrmaqCA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c13a5edd88b9570a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0Qp3Yy5RE4OVt78RrmaqCA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\ is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample protection saddle SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity:  and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Saddles and Shields> Protection Saddle as shown below:

   
Image:[Image-Analysis: The image presents a hierarchical structure that appears to represent categories and subcategories within a software or organizational framework called "SmartParts". The top-level category is "SmartParts" which contains a middle category labeled "S3D Standard". Under "S3D Standard", there are several subcategories including "Beam Attachments", "Clevises", "Miscellaneous", "Pipe Clamps", "Pipe Straps", "Plates", "Rod Fittings", "Rods", and "Saddles and Shields". Notably, within the "Saddles and Shields" subcategory, there is a specific item called "Protection Saddle". The structure suggests a system for organizing various components, possibly for engineering or design purposes, where "Saddles and Shields" serve as a specific grouping under the broader umbrella of attachment types for structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rqCYoY_YJTqAKlhlbg3C8w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/rqCYoY_YJTqAKlhlbg3C8w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use in at the end of dimensional values to specify inches. Ports are shown as points highlighted
in red.

Local Coordinate System


Image:[Image-Analysis: The image depicts a simplified diagram illustrating a route and its corresponding directional axes. At the center, there is a circular representation labeled "Route" shaded in gray. This indicates a central point or location of interest. Surrounding this central point, there are lines suggesting a pathway or circular route leading towards the outer circle. To the right of the "Route," three directional axes are drawn: X (implicitly, since it is not labeled), Y, and Z. The Y-axis is represented with a red arrow pointing to the right, indicating a positive direction, while the Z-axis is drawn vertically downward with a red arrow. This layout hints at a three-dimensional coordinate system where the route can be assessed in relation to these directional axes, particularly focusing on the movement in the Y and Z directions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2VO3P5tLae~34dXkph8vxQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/2VO3P5tLae~34dXkph8vxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Generic Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317069?contentId=DIQ0qpqI83yPTbmXFfulEg)
IJOAhsPipeOD::PipeOD

Specifies the outside diameter the pipe to which saddle is connected.


Image:[Image-Analysis: The image depicts a schematic representation of a pipe with its outer diameter (OD) indicated. At the top, the text "PipeOD" signifies what is being measured. The two arrows pointing outward from the pipe suggest the measurement of the outer diameter. In the center, there is a gray circle that represents the cross-section of the pipe. The red dot within the circle likely indicates the center of the pipe. The surrounding circular lines signify the pipe's outer edges. Overall, this image illustrates the concept of measuring the outer diameter of a cylindrical pipe. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uGIU5wTbUpPBxHasXaaC3A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uGIU5wTbUpPBxHasXaaC3A-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRadius1::Radius1

Specifies the outer radius of the saddle measured from the center of the pipe to the
bottom of the saddle.

If Radius1=0 then the software sets Radius1 = (PipeOD/2) + Thickness2 + Thichness1 to the default value for this property.


Image:[Image-Analysis: The image depicts a circular diagram illustrating a sphere or circular object with two distinct radii. Inside the larger outer circle is a smaller filled circle, which is likely the inner sphere or core of the larger structure. The left side of the image has two arrows pointing downward and upward, indicating a height or distance measurement, characterized as "Radius1." This suggests that "Radius1" represents one of the measurements of the outer circle or the distance from the center of the inner circle to its edge, potentially highlighting relationships between different dimensions or sections of the object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GO~i5bcfiB0_1HaiNilPeQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GO~i5bcfiB0_1HaiNilPeQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the saddle. It is always greater than zero.


Image:[Image-Analysis: The image depicts a circular object with a central grey area, which is likely a representation of a disc or a similar shape. Surrounding this central area is a larger circle, indicating the outline or boundary of the disc. There's a red marker or dot in the middle of the grey area, possibly indicating a reference point or center. Below the circular object, there are directional arrows pointing upwards and downwards, which could signify measurement or changes in thickness. The label "Thickness1" is positioned to the right of the object, suggesting a measurement related to the thickness of the disc, likely indicating that "Thickness1" refers to the measurement of the distance or capacity related to the object's dimensions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FXQNkmz6HY9miDEI~j1Zbw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/FXQNkmz6HY9miDEI~j1Zbw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsInclStiffener::InclStiffener

Indicates whether or not to include the middle plate. If this value is set to Yes, then the middle plate is drawn. This property uses the codelist value defined in
the hsYesNo sheet in the HS\_S3DParts\_Codelist.xls.


Image:[Image-Analysis: The image depicts a mechanical or structural component with a central grey circle that may represent a disk or hub. There are additional elements surrounding the central circle, indicated by the lines leading outward, which could represent structural supports or reinforcements. The term "Stiffner" is pointed out in blue, suggesting that this component is designed to provide additional strength or rigidity to a structure, likely preventing deformation under loads. The presence of a stiffener typically indicates engineering considerations for load-bearing applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O1LSOYLlhPAsd6awyt7lzQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O1LSOYLlhPAsd6awyt7lzQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the insulation.


Image:[Image-Analysis: The image depicts a diagram illustrating the concept of "Thickness2" in relation to a circular object. The main circular shape is divided into two parts, with the inner shaded circle indicating a central area. Alongside the circle, there are arrows that point vertically, suggesting measurements or dimensions related to "Thickness2," which implies that the illustration is likely focused on a specific thickness measurement associated with the circular object. The presence of arrows emphasizes the idea of measurement in a spatial context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g0d9Y0V3y19pBEYQ_5o~nw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/g0d9Y0V3y19pBEYQ_5o~nw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of the plate. It is always greater than zero.


Image:[Image-Analysis: The image shows a geometric representation of a rectangular shape with a length dimension labeled "Length1" at the bottom. The rectangle is divided into two horizontal sections: the top section appears empty, while the bottom section is shaded gray. In the center of the gray area, there is a small red dot. The line indicating "Length1" is marked by arrows at either end, suggesting it is the measurement of the rectangle’s length. This image seems to represent an object with a specific length and visual distinction between two sections, possibly for illustration of a concept in geometry or physics. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5plphj~c_Cw~6EYHfT3qJA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5plphj~c_Cw~6EYHfT3qJA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Curved Base Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317077?contentId=czHnvlnzfyDm~txWwARVoA)
These properties are used to create curved base geometry of the saddle. If these properties
are left as blank or 0, then the part creates the dimensions based on the rules provided
in the symbol code.

IJUAhsAngle1::Angle1

Specifies the angle from vertical center line of the pipe to the left leg of the saddle.
Angle1 and Angle2 properties define the sweep of the saddle.

If ToEdge is set to Yes, then the sweep angle is calculated to the edge of the leg. Otherwise the sweep angle
is calculated to the center of the leg.

Angle1 plus Angle2 is always greater than or equal to 180 degrees.


Image:[Image-Analysis: The image depicts a diagram related to geometry, specifically concerning angles. In the center, there is a shaded circular area, representing a circle with a center point. Two arrows are shown, indicating an angle measurement that appears to be labeled as "Angle1." The arrows extend from the center point outward, demonstrating the concept of measuring angles from a central point. The diagram visually illustrates how angles can be formed within a circle, with "Angle1" likely representing a specific angle measure between the two arrows. This is a common representation used in mathematics to explain relationships between angles and circles. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/z_vJ~QmMItp69VY_NaIQug-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/z_vJ~QmMItp69VY_NaIQug-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle2::Angle2

Specifies the angle from vertical center line of the pipe to the right leg of the
saddle.


Image:[Image-Analysis: The image depicts a diagram illustrating a circular shape with a central grey circle. A red dot is located at the center, indicating a point of reference or origin. Surrounding the central circle, there are curved lines that form a semi-circular shape, suggesting rotational movement or angles. One of the lines extends outward and is labeled "Angle2," indicating a specific measure of angle related to the component being analyzed. The arrow at the end of this line indicates direction, which may point to a rotational aspect of the angle being discussed. Overall, the diagram appears to focus on angular measurements in geometry or physics, potentially relating to circular motion. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5ENOKjNG1dDnZyvv3SEURA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5ENOKjNG1dDnZyvv3SEURA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle3::Angle3 (Optional)

Specifies the angle from vertical center line of the pipe to the left edge of the
curved plate. Angle3 and Angle4 properties define the sweep of the lower curved plate.

Angle3 is always greater than Angle1, and Angle3 plus Angle4 is always less than or equal to180 degrees.


Image:[Image-Analysis: The image illustrates a circular diagram involving an angle measurement labeled "Angle3." In the center of the circle, there is a grey-filled circle indicating a focal point. From this center point, there is a straight line that extends outward to the edge of the larger circle, which is likely representing a radius. The diagram suggests a relationship between the angles formed by the lines and the radius, possibly indicating the concept of angular measurement in a circular context. The arrows on the radius could be denoting directionality or orientation relevant to Angle3. This type of diagram is commonly used in geometry or engineering to explain angular relationships in circular shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0rPsAu1xqpdz~egCz_EAdg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/0rPsAu1xqpdz~egCz_EAdg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsAngle4::Angle4 (Optional)

Specifies the angle from vertical center line of the pipe to the right edge of the
curved plate.


Image:[Image-Analysis: The image depicts a diagram illustrating a circle with a central point. There is a line from the center to the circumference of the circle, representing a radius. A shaded area indicates a specific section of the circle, and an arrow points to the word "Angle4," indicating that the angle related to this section is designated as "Angle4." This setup suggests a discussion or study related to circular geometry or angles associated with specific sectors of a circle. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZaROy63Tkgz6k5PYQOFSmg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ZaROy63Tkgz6k5PYQOFSmg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsToEdge::ToEdge

Indicates whether or not the software calculates the sweep angle of the saddle from
the edge of the leg. This property uses the codelist value defined in the hsYesNo sheet in the HS\_S3DParts\_Codelist.xls file.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Flat Base Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317169?contentId=K1GiLZk~tYBdmp3JrUvpJQ)
These properties are used to create flat base geometry of the saddle. If these properties
are left as blank or zero, then the part creates the dimensions based on the rules
provided in the symbol code.

IJUAhsWidth1::Width1

Specifies the distance from the vertical center line of the pipe to the left outside
edge of the saddle. The software draws a flat base only if Width1 and Width2 are greater than zero. If Angle1 and Angle2 are specified then the software calculates the length of the base using the angles.


Image:[Image-Analysis: The image depicts a circular object which seems to be part of a mechanical or engineering design, possibly a wheel or a pulley. At the center, there is a filled gray circle, probably representing an axle or a hub. There are arrows indicating horizontal movement, which suggests the object can rotate or has a sliding mechanism. Below this circular object, the label "Width1" is shown, indicating that this dimension is significant for understanding either the size of the object or the spacing around it. This setup implies a relationship where "Width1" is a critical measurement influencing the functionality or design of the circular component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u81GxjD4CNTlb_rkGHAYlA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/u81GxjD4CNTlb_rkGHAYlA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the distance from vertical center line of the pipe to the right outside
edge of the saddle. The software draws a flat base only if Width1 and Width2 are greater than zero. If Angle1 and Angle2 are specified, then the software calculates the length of the base using the angles.


Image:[Image-Analysis: The image illustrates a circular shape with a gray inner circle representing a central object, possibly a hole or a spindle. Surrounding the inner circle is a larger outline, suggesting the structure or container that encompasses it. A vertical line indicates the center point of the inner circle, with a red dot marking the exact center. Below the center point, a horizontal line is labeled "Width2," which likely represents a measurement of width across the inner circle or a related dimension, providing context about the size of the central object. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GOE36mbC21jBhN~br_Zu6w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/GOE36mbC21jBhN~br_Zu6w-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the distance from the vertical center line of the pipe to the left overhang
of the saddle. Width3 is always greater than or equal to Width1.


Image:[Image-Analysis: The image illustrates a circular object (depicted in grey) with a red point at its center, indicating its center of mass or balance point. Surrounding the circle is a dashed line that represents its boundary. Below the circle, there is a horizontal line indicating measurement. The text "Width3" suggests a measurement label, potentially indicating the width of the circle or the diameter of the circular shape being depicted. There's also a double-headed arrow indicating that this dimension is intended to show measurement in both directions. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/as89Zy5GElhHWpOZS0q~0Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/as89Zy5GElhHWpOZS0q~0Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth4::Width4

Specifies the distance from the vertical center line of the pipe to the right overhang
of the saddle. Width4 is always greater than or equal to Width2.


Image:[Image-Analysis: The image depicts a simple mechanical setup. At the center is a circular object representing a wheel or pulley with a shaded interior, signifying that it is not hollow. Surrounding it are lines and arrows indicating its width measurement, labeled as "Width4." This suggests that the width of the wheel or pulley is 4 units. It appears to illustrate a basic concept in mechanics or physics related to rotational motion or force distribution, where understanding the dimensions of the wheel is crucial for analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V3bbpxChf8zcAo0gHMSgjA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/V3bbpxChf8zcAo0gHMSgjA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Concrete Saddle Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317174?contentId=N0TjLh49j69wyaC7f~7s8g)
These properties are used to create concrete geometry of the saddle. If these properties
are left as blank or zero, then the part creates the dimensions based on the rules
provided in the symbol code.

IJUAhsHeight1::Height1

Specifies the height from the base of the concrete saddle to the top of the saddle
curved surface. The concrete saddle is drawn only if Height1 is greater than zero.


Image:[Image-Analysis: The image depicts a circular object that appears to represent a wheel or a disc, which is located above a rectangular base. The circular object has a smaller inner circle (represented in red) that may signify a central point, while the area surrounding it is shaded gray, indicating a different layer or section of the object. Below the circular object, there is a rectangular box labeled "Height1," with arrows pointing downward, suggesting a measurement or dimension related to the height of the rectangular base or the distance between the base and the circular object above. This configuration may imply a relationship between the circular and rectangular components, possibly indicating how they function together in a mechanism or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TJJOfL0RfTSIjXmQzAVCWA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TJJOfL0RfTSIjXmQzAVCWA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight2::Height2

Specifies the height of the concrete saddle footing. The footing is drawn only if
Height1 is greater than zero and Height2 is greater than zero.


Image:[Image-Analysis: The image depicts a cylindrical object (represented by the large circle) positioned above a rectangular base. The circle, which appears to have a filled grey circle in the center, is likely meant to represent a top view of a circular component such as a disc or a wheel. Below this cylindrical object, the rectangular shape likely signifies a support or a platform where this object is placed. To the right of the rectangle is a label that says "Height2," suggesting a measurement related to the vertical distance or height from the base to the top of the cylindrical object. The image provides a simple illustration of a structure where a cylinder is mounted on a rectangular base, with a specific height indicated. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/32La6CF8NVIRRTxsKxG5mg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/32La6CF8NVIRRTxsKxG5mg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength2::Length2

Specifies the length of the footing. If Length2 is not specified then the software sets Length2 equal to Length1 as the default value for this property.


Image:[Image-Analysis: The image depicts a schematic view of a mechanical or structural element with a highlighted central point marked in red. The structure is rectangular and appears to have a length dimension indicated as "Length2" at the bottom. The gray area suggests that it might represent a middle section or an element that is part of a larger assembly, potentially in engineering or architectural contexts. The connection between the highlighted point and the overall structure is critical, possibly indicating the axis of symmetry or a focal point for measurement or assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Wm7vlwdZ_R8Jr3I7WyGPg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Wm7vlwdZ_R8Jr3I7WyGPg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Shape Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317178?contentId=uViUdprgwWcheN9~i~HkcA)
IJUAhsHeight3::Height3

Specifies the height from the bottom of the pipe to the bottom of the saddle. A U-shaped
saddle is drawn only if Height3 is greater than zero and Angle1 and Angle2 are set to zero.


Image:[Image-Analysis: The image depicts a cylindrical shape (represented by a circle at the top) above a rectangular base. The cylinder is shaded in gray, and there is a small red dot in its center. Below the cylinder, there is an arrow pointing downwards, and to the right side of the image, the label "Height3" indicates a measurement or a significant dimension related to this setup. The relationship here suggests that the height of the cylindrical shape is an important factor in the context being illustrated. This could pertain to various physical calculations, such as volume or center of mass, considering the geometric elements presented. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBiQaWsF~50AL0ao0uMJgQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bBiQaWsF~50AL0ao0uMJgQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317180?contentId=VoydYVujDUozCS0lKy8Y7w)
This property can be used to include a pipe clamp. If this property left blank or
set to zero, the clamp is not shown in the graphics.

IJUAhsClampName::ClampName

Specifies the string containing the name of the clamp. The clamp name is required
for the clamp to be drawn.


Image:[Image-Analysis: The image depicts a circular instrument or device, likely indicating a pipe clamp mechanism. It shows a central circular area shaded in gray with a red dot, signifying perhaps a focal point or a point of measurement. An arrow points to the side of the graphic with the label "Pipe Clamp," indicating the part of the device that is specifically identified as a pipe clamp. This suggests that the image is meant to illustrate how a pipe clamp is oriented and its significance in the context of the surrounding circular environment. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8cpkX4rc11kuHa9y6nBPTw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/8cpkX4rc11kuHa9y6nBPTw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/317182?contentId=Lo428MIZN0g2shWoq~nfZQ)
These properties are used to specify the different port types and their sizes for
the pipe saddle.


Image:[Image-Analysis: The image displays a table comparing two sets of ports: Port 1 labeled "Route" and Port 2 labeled "Weld1". Each port has multiple attributes listed vertically. The attributes for Port 1 include Name, PortType, Size, MinSize, and UnitType, while Port 2 includes the same attributes. This suggests a technical context where these ports may pertain to data transfer or connections in a system, with focus on their specifications and characteristics. The pink and green color coding helps to differentiate the two ports visually. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNNTLYZurBQV6mzbNq1JMw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/yNNTLYZurBQV6mzbNq1JMw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 - Route

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 2 Route | Pipe Outside Diameter | Pipe Outside Diameter | Pipe Outside Diameter |

Port2 - Weld1

|  |  |  |  |
| --- | --- | --- | --- |
| PortType | Size | MinSize | MaxSize |
| 1012 - Weld | Pipe Outside Diameter | 0 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rich Hanger Beam - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/390965?contentId=WxVyWD~2m_GWIL0N4kTcpA)
Library Name: Depends on the standard  
Workbook: HS\_Str-.xls  
Codelist: HS\_System\_Codelist.xls, AllCodelists.xls  
ProgID: HS\_HgrStructural.RichHgrBeam  
Part Name: Section Name + Section Standard  
Part Description: Section Name

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zvux48t~Bv5cZ88iFNe9Wg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=6187a5ccb9871231)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Zvux48t~Bv5cZ88iFNe9Wg-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample RichHgrBeam part delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > AISC LRFD-3.1 Steel as shown in the following example:

   
Image:[Image-Analysis: The image depicts a hierarchical file structure related to parts, specifically under a folder named "AISC LRFD-3.1 Steel." At the top level, there is a folder labeled "Parts." Inside this folder, there are various subfolders indicated by yellow folder icons, each representing different categories or types of parts. The subfolders are labeled with abbreviations: 2L, C, HP, HSSC, HSSR, L, MC, MT, PIPE, S, ST, W, and WT. These abbreviations likely correspond to specific types of steel or structural components used in construction or engineering. The organization suggests a relational structure where the "AISC LRFD-3.1 Steel" folder contains detailed classifications of parts typically referenced in design and construction projects, adhering to the AISC (American Institute of Steel Construction) specifications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sYW3Iy~vTGqi1SRf1U5R4w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/sYW3Iy~vTGqi1SRf1U5R4w-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Steel Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/390982?contentId=9tGa54EY7P_oPdorYYLcOQ)
These attributes define the common properties of hanger beam steel.

IJOAHsHgrBeamType::HgrBeamType

Specifies whether the hanger beam is Cutback steel or Snipped steel. HgrBeamType is a codelisted value. Allowed values are from HS\_System\_Codelist.xls are 1- Cutback Steel and 2 - Snipped Steel.


None: 

* Cutback steel is not supported for circular cross sections, such as HSSR and Pipe.
* Snipped steel is only supported for an L cross section.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fjj6_qtgFXOEUPn975VDDA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=bb2a38b07ca9074b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Fjj6_qtgFXOEUPn975VDDA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsOccOverLength:: BeginOverLength

Specifies the over length at the beginning of the steel. BeginOverLength can be either positive or negative.

IJUAhsOccOverLength:: EndOverLength

Specifies the over length at the end of the steel. EndOverLength can be either positive or negative.

IJUAhsOccLength::Length

Specifies the length of the steel. The software calculates Length using the start and end points in the graphic when you place the steel.

IJUAhsVarLength::VarLength

Specifies the cut length of the steel when you apply cutback angles, snip angles,
or overlength on the steel.


Image:[Image-Analysis: The image depicts a diagram related to some kind of object or tool showing two dimensions: "Cut Length" and "Length." The "Cut Length" is drawn as a horizontal line at the top with arrows indicating its measurement, while the "Length" is shown at the bottom with similar arrows for its own measurement. The object seems to be tapered or angled as indicated by the slanted lines leading down to the base. This suggests it may be a box or container where the "Cut Length" refers to a measurement of how much material has been removed or shaped, and the "Length" is the total measurement of the base. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O1CP8MKwHj07mbxXGs_qZw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O1CP8MKwHj07mbxXGs_qZw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Use the following properties to map and retrieve the geometry information from structural
workbook, StructCrossSections-.xls.

HgrRelation(i):ClassName

Specifies the cross section type. Example, L, C, W, and so on.

HgrRelation(i):Standard

Specifies the standard name. It is a codelisted value from HS\_System\_Codelist.xls. For example, AISC, CISC, Japan, China, Aust, and so on.

tHgrRelation(i):SectionName

Specifies the section name. Use the SecionName from StructCrossSections-.xls. For example, HSS32x24x.625, C15x50, L8x8x1-1/8, and so on.

IJOAhsReflect::Reflect

Specifies the plane for the reflection of Rich Hanger Beam. The following codelist
values are available in the hsReflectType sheet of the HS\_S3DParts\_Codelist workbook.

* 0 - No
* 1 - Along Flange Plane
* 2 - Along Web Plane

IJOAhsReflect::ReflectPlaneOffset

Specifies the offset for the Reflect Plane from the Cardinal Point 1 of the section.

![Illustration of Rich Hanger Beam - Reflect Functionality](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4xiL1f1zeCt~qiOJYC4M_Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=cd01a351dc8e104b)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4xiL1f1zeCt~qiOJYC4M_Q-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Cutback Steel Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/391297?contentId=IRnmCaz43f0SYKV4RK8_hQ)
These attributes define the cutback steel properties.

IJOAhsCutback::BeginCutbackAnchorPoint

Specifies the edge for the cutback at the begin face. The codelisted values from the
CutbackAnchorPoint sheet in the HS\_System\_Codelist.xls are 2 - Bottom Center, 4 - Left Center, 6 - Right Center, and 8 - Top Center

IJOAhsCutback::EndCutbackAnchorPoint

Specifies the edge for the cutback at the end face. The codelisted values from the
CutbackAnchorPoint sheet in the HS\_System\_Codelist.xls are 2 - Bottom Center, 4 - Left Center, 6 - Right Center, and 8 - Top Center

IJOAhsCutback:: CutbackBeginAngle

Specifies the start cutback angle for the steel. For CutbackAnchorPoint set to 2 or 8, the face ports rotate by the cutback angle and align along the cutback
face.

IJOAhsCutback::CutbackEndAngle

Specifies the end cutback angle for the steel. For CutbackAnchorPoint set to 2 or 8, the face ports rotate by the cutback angle and align along the cutback
face.

| Angle Value | Attribute Populated | Anchor Point | Result |
| --- | --- | --- | --- |
| +ve | CutbackBeginAngle | 2 | Adds specified degrees |
| +ve | CutbackBeginAngle | 4 | Subtracts specified degrees |
| +ve | CutbackBeginAngle | 6 | Adds specified degrees |
| +ve | CutbackBeginAngle | 8 | Subtracts specified degrees |
| -ve | CutbackBeginAngle | 2 | Subtracts specified degrees |
| -ve | CutbackBeginAngle | 4 | Adds specified degrees |
| -ve | CutbackBeginAngle | 6 | Subtracts specified degrees |
| -ve | CutbackBeginAngle | 8 | Adds specified degrees |
| +ve | CutbackEndAngle | 2 | Subtracts specified degrees |
| +ve | CutbackEndAngle | 4 | Adds specified degrees |
| +ve | CutbackEndAngle | 6 | Subtracts specified degrees |
| +ve | CutbackEndAngle | 8 | Adds specified degrees |
| -ve | CutbackEndAngle | 2 | Adds specified degrees |
| -ve | CutbackEndAngle | 4 | Subtracts specified degrees |
| -ve | CutbackEndAngle | 6 | Subtracts specified degrees |
| -ve | CutbackEndAngle | 8 | Adds specified degrees |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Snipped Steel Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/391298?contentId=fIEsAJzk8~cHievEJqBN_A)
These properties specify the Flange and Web modifications when a hanger is snipped
by various offset values and angles.

IJOAhsSnipedSteel::CutbackBeginAngle1

Specifies the angle with which the begin face of the flange is snipped.

IJOAhsSnipedSteel::CutbackBeginAngle2

Specifies the angle with which the begin face of the web is snipped.

IJOAhsSnipedSteel::CutbackEndAngle1

Specifies the angle with which the end face of the flange is snipped.

IJOAhsSnipedSteel::CutbackEndAngle2

Specifies the angle with which the end face of the web is snipped.

IJOAhsSnipedSteel::BeginCutbackAnchorPoint1

Specifies the edge for the cutback at the begin face of the flange. The following
codelisted values from the CutbackAnchorPoint sheet in the HS\_System\_Codelist.xls are valid:

* 2 - Bottom Center
* 8 - Top Center. BeginCutbackAnchorPoint1 (read-only value)

IJOAhsSnipedSteel::BeginCutbackAnchorPoint2

Specifies the edge for the cutback at the begin face of the web. The following codelisted
values from the hsCutbackAnchorPoint sheet in HS\_System\_Codelist.xls are valid:

* 4 - Left Center
* 6 - Right Center. BeginCutbackAnchorPoint2 (read-only value)

IJOAhsSnipedSteel::EndCutbackAnchorPoint1

Specifies the plane for the cutback at the end face of the flange. The following codelisted
values from the hsCutbackAnchorPoint sheet in HS\_System\_Codelist.xls are valid:

* 2 - Bottom Center
* 8 - Top Center. EndCutbackAnchorPoint1 (read-only value)

IJOAhsSnipedSteel::EndCutbackAnchorPoint2

Specifies the edge for the cutback at the end face of the web. The following codelisted
values from the hsCutbackAnchorPoint sheet in HS\_System\_Codelist.xls are valid:

* 4 - Left Center
* 6 - Right Center. EndCutbackAnchorPoint2 (read-only value)

IJOAhsCutbackOffset::BeginOffsetAlongFlange

Specifies the offset with which the begin face of the flange is snipped.

IJOAhsCutbackOffset::BeginOffsetAlongWeb

Specifies the offset with which the begin face of the web is snipped.

IJOAhsCutbackOffset::EndOffsetAlongFlange

Specifies the offset with which the end face of the flange is snipped.

IJOAhsCutbackOffset::EndOffsetAlongWeb

Specifies the offset with which the end face of the web is snipped.

IJOAhsFacePortOrient::FacePortOrient

Specifies whether the face port orientation is aligned along the flange, or the web
when a snip angle is applied. It is a codelisted value from the hsFacePortOrient sheet in the HS\_System\_Codelist.xls workbook. Allowed values are: 1 - Face Port Orient Along Flange and 2 - Face Port Orient Along Web.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UXu5LV1YFGnW~8hzVdD9iw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=01cb5c1823fbbc42)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UXu5LV1YFGnW~8hzVdD9iw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/391299?contentId=5_ugZ9SFChkVnNTWbfuGLQ)
IJOAhsSteelCP::CP1

Specifies the cardinal point of the BeginCap port. The default location of CP1 is 1.

IJOAhsSteelCP::CP2

Specifies the cardinal point of the EndCap port. The default location of CP2 is 1.

IJOAhsSteelCP::CP3

Specifies the cardinal point of the BeginFace port. The default location of CP3 is 5.

IJOAhsSteelCP::CP4

Specifies the cardinal point of the EndFace port. The default location of CP4 is 5.

IJOAhsSteelCP::CP5

Specifies the cardinal point of the Neutral port. The default location of CP5 is 5.

IJOAhsSteelCP::CP6

Specifies the cardinal point of the BeginFlex port. The default location of CP6 is 8.

IJOAhsSteelCP::CP7

Specifies the cardinal point of the EndFlex port. The default location of CP7 is 8.

IJOAhsBeginCap::BeginCapXOffset

Specifies the offset with which the BeginCap port is moved in the x-axis.

IJOAhsBeginCap::BeginCapYOffset

Specifies the offset with which the BeginCap port is moved in the y-axis.

IJOAhsBeginCap::BeginCapRotZ

Specifies the angle with which the BeginCap port is rotated about its z-axis.

IJOAhsEndCap::EndCapXOffset

Specifies the offset with which the EndCap port is moved in the x-axis.

IJOAhsEndCap::EndCapYOffset

Specifies the offset with which the EndCap port is moved in the y-axis.

IJOAhsEndCap::EndCapRotZ

Specifies the angle with which the EndCap port is rotated about its z-axis.

IJOAhsFlexPort::FlexPortXOffset

Specifies the offset with which the BeginFlex port is moved in the x-axis.

IJOAhsFlexPort::FlexPortYOffset

Specifies the offset with which the BeginFlex port is moved in the y-axis.

IJOAhsFlexPort::FlexPortZOffset

Specifies the offset with which the BeginFlex port is moved in the z-axis.

IJOAhsFlexPort::FlexPortRotX

Specifies the angle with which the BeginFlex port is rotated about its x-axis.

IJOAhsFlexPort::FlexPortRotY

Specifies the angle with which the BeginFlex port is rotated about its y-axis.

IJOAhsFlexPort::FlexPortRotZ

Specifies the angle with which the BeginFlex port is rotated about its z-axis.

IJOAhsEndFlexPort::EndFlexPortXOffset

Specifies the offset with which the EndFlex port is moved in the x-axis.

IJOAhsEndFlexPort::EndFlexPortYOffset

Specifies the offset with which the EndFlex port is moved in the y-axis.

IJOAhsEndFlexPort::EndFlexPortZOffset

Specifies the offset with which the EndFlex port is moved in the z-axis.

IJOAhsEndFlexPort::EndFlexPortRotX

Specifies the angle with which the EndFlex port is rotated about its x-axis.

IJOAhsEndFlexPort::EndFlexPortRotY

Specifies the angle with which the EndFlex port is rotated about its y-axis.

IJOAhsEndFlexPort::EndFlexPortRotZ

Specifies the angle with which the EndFlex port is rotated about its z-axis.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/391130?contentId=wegfhin4cFsgfzsEYyFUoQ)
These properties are used to specify the different port types and their sizes for
RichHgrBeam.

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y9FvLR8o3PEuw4NfrZoWeQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=50a06aaad0c1cb8e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y9FvLR8o3PEuw4NfrZoWeQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/z5VyGUrwxT3SrEWSBPqByQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a165d997385bde6c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/z5VyGUrwxT3SrEWSBPqByQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Reinforcement Pad (Repad) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/728035?contentId=kfXPfmzFvEiLdV4Zk41Lyw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PipeRPad; HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ElbowRPad  
Part Name: Repads  
Part Description: Repads

![Repad SmartPart](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pqUFa5c~xpSHlLhqON7qCg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=a68a71c5fd3bef3f)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pqUFa5c~xpSHlLhqON7qCg-_PVFQNoCl4XmjAxWO0f7XQ/content)

![Repad - Length, Width, Thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MC56rO5f2t3iPTDELdOcuA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dbd18494bbfb1b5e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MC56rO5f2t3iPTDELdOcuA-_PVFQNoCl4XmjAxWO0f7XQ/content)

Use the following procedure to place a sample Reinforcement Pad (Repad) SmartPart
delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
look for icon that looks like a plus sign with a small tag, often used to indicate adding a label or tag:  command, and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Reinforcement Pads as shown in the following graphic:

   ![Reinforcement Pads - Catalog Heirarchy](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IrXfDODMMlub3Sd7a1JXgQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7c48783cc97d2ffe)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/IrXfDODMMlub3Sd7a1JXgQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. To specify inches, place "in" at the end of
the dimensional value. The software shows ports as points highlighted in red.

ProgID:

HSSmartPart,Ingr.SP3D.Content.Support.Symbols.PipeRPad

HSSmartPart,Ingr.SP3D.Content.Support.Symbols.ElbowRPad

Example: S3Dhs\_PipeRPad, S3Dhs\_ElbowRPad sheet in HS\_S3DParts.xls# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Generic Repad Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/728046?contentId=NsD_0fpz3_xJkGnAy5Ti9w)
IJOAhsPipeOD::PipeOD

Specifies the outside diameter of the pipe.

IJOAhsElbow::ElbowRadius

Specifies the bend radius of the elbow pipe component. This setting is used by ElbowRPad.

IJOAhsElbow::FaceToCenter

Specifies the distance between the face of the elbow and the center. For a short tangent
elbow, the face to center distance is the same as the elbow radius.

IJOAhsBendAngle::BendAngle

Specifies the elbow angle.

IJUAhsSize::Size

Specifies the repad part size. The part selection rules use this setting to select
the correct repad part.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Detail Repad Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/728051?contentId=0AMaVyJnTha_U3ljn0642w)
IJUAhsThickness1::Thickness1

Specifies the thickness of the reinforcement pad.

IJUAhsLength1::Length1

Specifies the length of the reinforcement pad along the pipe axis for the PipeRPad
symbol, and the arc length of the pad along the elbow curvature for the ElbowRPad
symbol.

IJUAhsWidth1::Width1

Specifies the width of the Repad. This is the arc length of the pad in the pipe cross
section.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/728071?contentId=bbDq5HrOb2ItwEtuvhfVqQ)
![Repad - Properties](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W2hMiZd7qnGIhUgZBHz3pw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=985fcbe13bda1cf9)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/W2hMiZd7qnGIhUgZBHz3pw-_PVFQNoCl4XmjAxWO0f7XQ/content)

![Repad - Route & Weld](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/f_Lp~uqBDUOkZe8~PpRGSw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=249cb6489c72d0ec)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/f_Lp~uqBDUOkZe8~PpRGSw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Route Port

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 2 - Route | Pipe Diameter | Pipe Diameter | Pipe Diameter |

Weld Port

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | Min Size | Max Size |
| 1200 - Other | 1 | -9999 | 9999 |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rod - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306793?contentId=3xGfuNVK~XnhmCBpwXVPzg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Rod  
Part Name: Rod  
Part Description: Rod SmartPart

![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TDJs~PUKYpdXADmg3~45_A-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5a2b95007260f7d8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/TDJs~PUKYpdXADmg3~45_A-_PVFQNoCl4XmjAxWO0f7XQ/content)

To place a sample Rod SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity:  and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Rods > Rod Continuous Threaded – RH Thread as shown below.

   
Image:[Image-Analysis: The image displays a hierarchical file structure related to a category called "SmartParts." At the top level is "S3D Standard," which contains various subcategories. Under "S3D Standard," the following categories are listed: Beam Attachments, Clevises, Miscellaneous, Pipe Clamps, Pipe Straps, Plates, Rod Fittings, Rods, Struts, and U-Bolts. Among these, the category "Rods" contains an item labeled "Rod Continuous Threaded - RH Thread," which is highlighted, indicating it may be the focus of interest or selection within this structure. This structure organizes various components or parts that are likely used in engineering or manufacturing applications. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4GzXHZ_S_TREl8RBfDYljQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/4GzXHZ_S_TREl8RBfDYljQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches.

Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Image-Analysis: The image illustrates a 3D geometric representation of a line segment, depicting its endpoints and orientation in a three-dimensional coordinate system. The vertical rectangle represents the length of the segment alongside its orientation. The coordinate axes are labeled: X (horizontal, pointing to the right), Y (implied to be inward or out of the plane, not explicitly shown), and Z (vertical, pointing upwards). The endpoints of the segment are described with coordinates: End 1 at (0, 0, 0) which is the origin, and End 2 at (0, 0, Length), indicating the segment extends straight up along the Z-axis from the origin by a certain Length. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WBbgZS2H2frVThD1YF1Mjw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/WBbgZS2H2frVThD1YF1Mjw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Rod Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306932?contentId=r_OaF~rYjSijQ1fi5i7ccw)
These properties define the geometry of the rod.


None:  For these properties, the default unit of distance is "mm". Specify "in" at the end
of dimensional value to use inches.

IJUAhsRodDiameter1::RodDiameter1

Specifies the outside diameter of the rod.


Image:[Image-Analysis: The image depicts an illustration related to the concept of "Rod Diameter". On the left side, there is a rectangular shape which may represent a rod or bar, identified by red dots, possibly indicating measurement points or reference points along the length. On the right side of the image, there are two horizontal arrows pointing downwards towards a circle, suggesting a measurement of the diameter at the center of the rod. Below this graphical representation, the term "Rod Diameter" is labeled, indicating that the image explains how to assess the diameter of a rod. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~R~Y22m6A0SwMPGGz5kU4Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~R~Y22m6A0SwMPGGz5kU4Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAHgrOccLength::Length

Specifies the length of the rod as determined during placement. Length is the distance
between the Port1 and Port2 end ports, excluding the end types.


Image:[Image-Analysis: The image depicts a horizontal line with red markers on each end, representing a measurement of length. Beneath the line, the word "Length" indicates that this illustration is focused on the concept of length. On the right side, there is a small circle, which could represent a point or reference in relation to the length measurement. The image visually communicates how length is measured using endpoints. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DtVVJGCJXpWtDOqYBoKHog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DtVVJGCJXpWtDOqYBoKHog-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength::Length

Specifies the fixed length of the rod. You cannot modify this value during placement.


Image:[Image-Analysis: The image depicts a horizontal line with red markers on each end, representing a measurement of length. Beneath the line, the word "Length" indicates that this illustration is focused on the concept of length. On the right side, there is a small circle, which could represent a point or reference in relation to the length measurement. The image visually communicates how length is measured using endpoints. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DtVVJGCJXpWtDOqYBoKHog-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DtVVJGCJXpWtDOqYBoKHog-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWtPerLen::WtPerLen

Specifies the weight per unit length of the rod, not including the weight due to OverLength1, OverLength2, and RepOverLen1.

IJUAhsWeight::Weight

Specifies the fixed portion of the rod weight that is independent of length, such
as OverLength1, OverLength2, RepOverLen1, or rod ends.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Type and Center Type Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306958?contentId=dCsGogYwv47X8bF1fKgZXw)
These properties define the different combinations of end types and center types for
the rod.

IJUAhsRodEnd1::RodEnd1Type

Defines the shape of an end feature at End1.

IJUAhsRodEnd2::RodEnd2Type

Defines the shape of an end feature at End2.

Valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsRodEndType sheet.


Image:[Image-Analysis: The image presents a chart describing different types of fasteners, each associated with a specific symbol and a label. The fasteners are numbered from 1 to 5, and each corresponds to a distinct shape or type: 1 - Plain (Default) is represented by a simple rectangle with a circle; 2 - Eye is a circular shape; 3 - Spade features a spade-like figure; 4 - Bolt shows a bolted shape; and 5 - Nut (Female) is depicted by a rectangle with a circular shape suggesting a nut. The symbols imply their functional applications in hardware and assembly contexts. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qX7MnaucMi0aDdaR4Mjipg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qX7MnaucMi0aDdaR4Mjipg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodCenterType::RodCenterType

Defines the shape of a center feature. Valid codes are listed in the HS\_S3DParts\_Codelist.xls workbook on the hsRodCenterType sheet.


Image:[Image-Analysis: The image displays a series of shapes categorized by type, each accompanied by a corresponding illustration. The categories are numbered from 1 to 4: 1 represents 'None', depicted by a horizontal rectangle with a small circle next to it; 2 represents 'Round', illustrated with a rounded rectangle and a circle; 3 indicates 'Square', illustrated with a square shape and a circle next to it; and 4 denotes 'Linked Eyes', which consists of a circle linked to a rectangular shape, and an intersection symbol. This format suggests a classification or selection system based on different geometric shapes and their attributes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VwmDN2GNuYr3Lmuv_W6eCA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VwmDN2GNuYr3Lmuv_W6eCA-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Optional Geometry Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306959?contentId=XSrM7aXTeFiX4tHce_HGGQ)
These properties define optional geometry of the rod.

IJUAhsOffset1::Offset1

Specifies the location of the RodCenterType feature shape along the rod.

* If Offset1 is 0, then RodCenterType shape is centered along the rod length.
* Otherwise, Offset1 is calculated from End1:


Image:[Image-Analysis: The image is a technical illustration showing different center types and their corresponding shapes with an offset term associated with each. There are three center types illustrated: 'Center Type 2 - Round', which features rounded shapes; 'Center Type 3 - Square', which shows a square shape; and 'Center Type 4 - Linked Eyes', depicted as two linked shapes resembling eyes. Each type has indications for distance or offset labeled as "Offset" or "Offset1." The image serves as a reference for understanding the visual representation of these center types. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/M0ZRKLqOzXhTJKLXBs5JeA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/M0ZRKLqOzXhTJKLXBs5JeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of RodEnd1Type and RodEnd2Type.


Image:[Image-Analysis: The image displays different end types used in mechanical or structural components. It includes three types of ends: Spade End Type, Bolt End Type, and Nut (Female) End Type. Each type has a visual representation and includes a label for "Thickness1," indicating a relevant dimension for these components. The Spade End Type features a rounded end, while the Bolt End Type shows a rectangular block design. The Nut (Female) End Type displays a hollow end, ideal for receiving a bolt or screw. The image illustrates the variation in design for each end type, which is crucial for their respective applications in fastening or connecting components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vg6EZLejJ1jdX1MVFmzF3g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vg6EZLejJ1jdX1MVFmzF3g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLength1::Length1

Specifies the length of RodEnd1Type and RodEnd2Type. For a spade end, the length is calculated from the port to the base of the spade.
For round and square ends, the length is the same as RodCenterType length.


Image:[Image-Analysis: The image provides a diagram that illustrates three different types of mechanical ends: Spade End, Round Center Type, and Square Center Type. Each type is labeled and includes a graphical representation. The Spade End is depicted with a flat, elongated shape at the end and shows the measurement labeled as Length1, indicating a distance between two points. The Round Center Type features a rectangular body with rounded ends, also referring to Length1 for measurement. Lastly, the Square Center Type is presented as a rectangular bar with square ends, with Length1 indicated as well. Each type seems to be part of a mechanical or structural design, where Length1 is a critical dimension for fitting or connecting purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AUje5wrrSK5IgV619_HKfA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/AUje5wrrSK5IgV619_HKfA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsDiameter1::Diameter1

Specifies the outside diameter of RodEnd1Type, RodEnd2Type, and RodCenterType.

|  |  |
| --- | --- |
| [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qXxh5C9jopa429oQ6JgdHA-_PVFQNoCl4XmjAxWO0f7XQ/content) | [#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BzkyHbC7sJSEk5vev9HwHA-_PVFQNoCl4XmjAxWO0f7XQ/content) |

IJUAhsOverLength1::OverLength1

Specifies the length of RodEnd1Type that extends past or ends before End1.

IJUAhsOverLength2::OverLength2

Specifies the length of RodEnd2Type that extends past or ends before End2.

* If OverLength is 0, the rod end coincides with the port.
* If OverLength is positive, the length of the rod increases beyond the port.

Example: Spade end rod


Image:[Image-Analysis: The image illustrates the concept of "Over Length," which appears to be a technical diagram. It shows a rectangular box with an arrow pointing to the right from a smaller rectangle, indicating that the smaller rectangle extends beyond the end of the larger rectangular box. The two red dots on the smaller rectangle likely represent points of measurement or limits of acceptable lengths. This could imply a condition or situation where the length (or size) of an object exceeds the expected or allowed dimensions, hence the terminology "Over Length." 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VHtLFRonIvEOKpoBzr6d9g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/VHtLFRonIvEOKpoBzr6d9g-_PVFQNoCl4XmjAxWO0f7XQ/content)

* If OverLength is negative, the length of the rod decreases before the port.

Example: Anchor rod embedded in concrete.  

Image:[Image-Analysis: The image illustrates a measurement concept referred to as "Over Length." On the left side, there is a diagram showing a horizontal rectangular shape with red dots indicating measurement points. To the right, there is a different shape that appears to be an oval with a red dot in the center, likely suggesting a reference point for the over length measurement. The term "Over Length" is prominently displayed at the top, indicating that this diagram might be used in a context where precise measurements of lengths are important, such as in engineering, manufacturing, or design. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NbrC~IXVlUc6QAB9VB0S3w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NbrC~IXVlUc6QAB9VB0S3w-_PVFQNoCl4XmjAxWO0f7XQ/content)


None:  Length (reported in the bill of material) is not affected by over length. RepOverLen1 includes the over length.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Length Rules and Bill of Materials Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306960?contentId=6De3t8FSAAnUSyFU1epNew)
These properties define length details of the rod.

IJUAhsMinLen::MinLen

Defines the minimum length permitted for the rod. If Length is less than MinLen, a warning is displayed in the software. The default value is usually 0 in order to avoid warnings.

IJUAhsMaxLen::MaxLen

Defines the maximum length permitted for the rod. If Length is greater than MaxLen, a warning is displayed in the software. The default value is usually 9999 in order to avoid warnings.

IJUAhsRepOverLen1::RepOverLen1

Defines the actual rod length reported in the bill of material by adding or subtracting
OverLength1 and OverLength1 to Length.

* If OverLength is 0, RepOverLength1 is the same as Length.
* If OverLength is positive, it is added to Length to give RepOverLength1.
* If OverLength is negative, it is subtracted from Length to give RepOverLength1.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/306961?contentId=NmjtN4ZIN~GESsPsG9SJIg)
Defines port types and their sizes at End1 and End2 of the rod.


Image:[Image-Analysis: The image presents a comparison of two ports, labeled Port 1 and Port 2. Each port has attributes listed alongside it, indicating details for each port's corresponding attributes. The attributes for Port 1 include Name, PortType, Size, MinSize, and UnitType, while Port 2 has similar attributes: Size, MinSize, and UnitType. The Port 1 attributes suggest it might include descriptive identifiers and settings, whereas Port 2 focuses on dimensions and specifications. This structured format allows for a clear side-by-side comparison of the characteristics of each port, facilitating a better understanding of their functionalities and potential differences. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pjDxOTj1nAjdl4AoK8zdYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/pjDxOTj1nAjdl4AoK8zdYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Plain End - Type 1


Image:[Image-Analysis: The image depicts a vertical line segment with labeled ends. The line runs vertically along the Y-axis, indicated with the labels "End 1" and "End 2," each showing coordinates (0,0,0) and (0,0,Length) respectively, where Length indicates the height of the line. There are arrows indicating the length of the line segment with the letter "Z" repeated twice, suggesting that the line is segmented into equal parts or that the Z position is critical in this context. The horizontal arrows pointing towards X represent the direction along the X-axis. This graphic is likely illustrating concepts related to geometry or physics, focusing on the properties of line segments in a three-dimensional coordinate system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3uSDWxNgIKUALIfO24x7GA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3uSDWxNgIKUALIfO24x7GA-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1000 – ExtThdRH    1002 – ExtThdLH | The diameter of the rod.  Value is the same as RodDiameter. | Minimum threaded length.  Default value is 0. | Maximum threaded length.   * For continuous threaded rod, value is 9999. * For end-threaded rods, value is the same as thread length. |

Eye End - Type 2


Image:[Image-Analysis: The image depicts a three-dimensional object with two ends labeled as "End 1" and "End 2". Both ends are shown with coordinates, where "End 1" is represented at the point (0,0,0) and "End 2" at (0,0,Length). The object appears to be cylindrical given the circular shape at "End 2". There are directional axes indicated: X and Z. The Z-axis is vertical, extending from the base of the cylinder upwards, while the X-axis extends horizontally to the right. The connections suggest a vertical alignment of the cylinder along the Z-axis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/M8vTIqnqk9nSPzlObI3R5Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/M8vTIqnqk9nSPzlObI3R5Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1007 – Eye | The thickness of the eye, for comparison against the opening in the connecting item, to check if the thickness of the eye fits into the opening.  Value is the same as RodDiameter. | The smallest pin or bolt that will fit inside the eye.  Value is usually 0. | The largest pin or bolt that will fit inside the eye.  Value is from catalog specs. |

Spade End - Type 3


Image:[Image-Analysis: The image depicts a diagram of a rod with two ends labeled as End 1 and End 2, showing their respective coordinates. End 1 is positioned at the origin (0,0,0) of a 3D coordinate system, while End 2 is located at (0,0,Length), indicating it is vertically aligned with a specified length. The diagram includes arrows indicating the X and Z axes for clarity. A circular top shape at End 2 suggests a connection point, with potential rotation or support. The diagram emphasizes the orientation and positions of the two ends within a three-dimensional context. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ROiPraSv~s8Z48auBpo5~w-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/ROiPraSv~s8Z48auBpo5~w-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1007 – Eye | The thickness of the spade end, for comparison against the opening in the connecting item, to check if the thickness of the spade end fits into the opening.  Value is the same as Thickness. | The smallest pin or bolt that will fit inside the eye of the spade end.  Value is usually 0. | The largest pin or bolt that will fit inside the eye of the spade end.  Value is from catalog specs. |

Bolt End - Type 4


Image:[Image-Analysis: The image illustrates a simple representation of a linear object or beam with two endpoints labeled as End 1 and End 2. End 1 is positioned at coordinates (0, 0, 0), indicating its starting point in a three-dimensional space, while End 2 is at (0, 0, Length), signifying the endpoint at a specified Length along the Z-axis. The horizontal arrows indicate the X-axis, while the vertical arrows represent movement or length along the Z-axis. The 'Z' labels suggest a vertical orientation, possibly signifying height or depth, while the 'Length' is a dimension of the linear entity being depicted. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NGp7uJQA60gsvKgodj1~qw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/NGp7uJQA60gsvKgodj1~qw-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1200 – Other | Not applicable.  Set to 0. | Not applicable.  Set to -9999. | Not applicable.  Set to 9999. |

Nut (Female) End - Type 5

Defines the end of a strut with a threaded or un-threaded hole.


None:  Port orientation is opposite to all other types so that the orientation is the same
as that of the connected male threaded part.


Image:[Image-Analysis: The image illustrates a 3D coordinate system, specifically showing a vertical line or beam with defined endpoints. At the bottom, it indicates "End 1" with coordinates (0,0,0), signifying the origin point in a Cartesian coordinate system. At the top, "End 2" is noted as (0,0,Length), where "Length" is the distance from the origin along the vertical axis, which is represented as the Z-axis. The X-axis is depicted as horizontal arrows on both ends of the beam, indicating the direction and orientation of that axis, while the Z-axis is shown as vertical arrows, emphasizing its orientation. The relationship between End 1 and End 2 defines the length of the vertical object in 3D space. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MaL7tRCY2vMR3vDPggIAQw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/MaL7tRCY2vMR3vDPggIAQw-_PVFQNoCl4XmjAxWO0f7XQ/content)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1001 – IntThdRH    1003 – IntThdLH | Depth of the threaded hole, for comparison with the threaded length of the connected threaded port. | Minimum diameter of the connected threaded port. | Maximum diameter of the connected threaded port. |# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Riser Lug - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/803573?contentId=IYUS99c_DmpJe9ISxzXMMw)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.RiserLug  
Part Name: Riser Lug  
Part Description: Riser Lug SmartPart

![RiserLug Smart Part Overview](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PTYPi4wDxi9JnwkFxHdYdQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=c3b95bd928cafe81)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/PTYPi4wDxi9JnwkFxHdYdQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Bulk load the following workbooks in the [Product Folder]\CatalogData\BulkLoad\DataFiles\
folder:

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls and is delivered in [Product Folder]\CatalogData\BulkLoad\DataFiles folder.

To place a sample Riser Lug SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part 
icon that looks like a plus sign button, typically used for adding or increasing quantity:  and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Rod Hangers > Riser Lug as shown below:

   
Image:[Alt-Text: RiserLug Location 
Image-Analysis: The image is a hierarchical tree diagram showing a structure for a software or design tool categorized under "SmartParts" and "S3D Standard." At the top level, there is a main category "SmartParts," which contains the subcategory "S3D Standard." Under "S3D Standard," there are various components listed as subcategories, including items like Beam Attachments, Clevises, and Guides. Each of these categories may contain additional components or types related to structural supports and attachments, such as "Rods" and "Riser Lug." The structure is organized to help users navigate through different parts or components available in the software or design tool. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vSQzfmdy5g5ZaVIEbvhveg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug Location](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vSQzfmdy5g5ZaVIEbvhveg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches.

Ports are shown as points highlighted in red.

Local Coordinate System

![RiserLug](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y41YTLGNrmM2I7z6ysmdxQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f96657854f4f18f7)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/y41YTLGNrmM2I7z6ysmdxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Riser Lug Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/803594?contentId=49PWqBnvFGtfNF_PpRslkQ)
IJOAhsPipeOD::PipeOD

Specifies the outer diameter of the pipe.


Image:[Alt-Text: RiserLug Basic Properties - PipeOD 
Image-Analysis: The image depicts a technical diagram of a mechanical component, likely a bearing or support structure, viewed in a cross-section. It shows a central cylindrical part with two end pieces marked as "C" and "D," possibly indicating areas of interest or specific measurements. The arrows pointing towards the central cylinder suggest forces acting inwards, which implies a focus on compression or loading conditions. The connections imply how the parts interact under load, and the structure seems to be designed for stability and strength in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~xyhg2vUNEOn~zzRLWTwSw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug Basic Properties - PipeOD](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~xyhg2vUNEOn~zzRLWTwSw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLugQty::LugQty

Specifies the number of lugs around the pipe.

![RiserLug Basic Properties - LuGQty](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~6JafkS4Vo8KFylV8uzdHg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5879bcc0c06a0c92)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~6JafkS4Vo8KFylV8uzdHg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsLugSpAngle::SpacingAngle

Specifies the angle between the lugs when the quantity is more than 1. If you do not
provide a value or provide zero as a value, then the lugs are equally spaced around
the pipe based on the quantity.

![RiserLug Basic Properties - Spacing Angle](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T2tKPmvX9VpH~LFy8~~3ew-_PVFQNoCl4XmjAxWO0f7XQ/content?v=dcc0b926a3139497)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/T2tKPmvX9VpH~LFy8~~3ew-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRodDiameter::RodDiameter

Specifies the diameter of the hanger rod.

IJUAhsRiserCfgType::ConfigurationType

Specifies the type of the riser lug that is used for the port positions. Uses the
following codelist values:

* Stopper


Image:[Alt-Text: RiserLug Basic Properties - ConfigType - Stopper 
Image-Analysis: The image is a technical drawing of a mechanical part, likely a type of coupling or flange. It shows a side view of the component with various dimensions labeled. The drawing includes important annotations such as T1 and T2, which may refer to specific thicknesses, and other dimension indicators that specify lengths and radii. This image is typically used in engineering to provide detailed specifications that need to be adhered to in the manufacturing or installation of this component, ensuring that it fits correctly with other parts in an assembly. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BvGonwPZC6GcsiY7lNpK1A-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug Basic Properties - ConfigType - Stopper](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BvGonwPZC6GcsiY7lNpK1A-_PVFQNoCl4XmjAxWO0f7XQ/content)

* Hanger


Image:[Alt-Text: RiserLug Basic Properties - ConfigType - Hanger 
Image-Analysis: The image depicts a mechanical drawing or technical diagram that shows a component, likely a type of hinge or connector used in machinery. It features various measurements and dimensions annotated with lines and arrows, which suggest how the parts are connected and how they move relative to each other. The circular and rectangular shapes indicate where parts may pivot or fit together, and the labels (not fully visible in the image) likely specify the sizes or types of materials to be used. This diagram is useful for engineers or designers who need to understand how these components will be assembled and function in a mechanical system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6vn9vK5EqmUDQScN05jhBw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug Basic Properties - ConfigType - Hanger](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6vn9vK5EqmUDQScN05jhBw-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Vertical Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/803614?contentId=cvxUDcb4KcKXM~GqEMHqPQ)
IJUAhsLength1::Length1

Specifies the length of the vertical plate.


Image:[Alt-Text: RiserLug Vertical Plate Properties - Length1 
Image-Analysis: The image depicts a technical illustration of a component with dimensions labeled. The main focus is on the measurement identified as "Length1," which is indicated through an arrow pointing in the direction of the length being measured. The component appears to have a cylindrical shape and possibly has fittings or connections on the side, as suggested by the small circles, which may represent bolts or attachment points. The purpose of the illustration is likely to convey important dimensional information for manufacturing or engineering purposes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1F00CAmB2HKyOd2ARjsu2g-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug Vertical Plate Properties - Length1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/1F00CAmB2HKyOd2ARjsu2g-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsHeight1::Height1

Specifies the height of the vertical plate.


Image:[Alt-Text: RiserLug - Vertical Plate Properties - Height1 
Image-Analysis: The image depicts a technical drawing, likely related to an engineering or architectural component. It includes a side view of a structure with specified height labeled as "Height1". The drawing includes a cylindrical shape, potentially representing a pipe or a mechanism, that connects to a base or a support structure. The arrows pointing towards the vertical line indicate a measurement or dimension related to the height. This representation is typical in plans or specifications where clear visual communication of dimensions and components is essential. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uoviam85UXWtMDt~4EzRqA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Vertical Plate Properties - Height1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uoviam85UXWtMDt~4EzRqA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness1::Thickness1

Specifies the thickness of the vertical plate.

IJUAhsMulti1::Multi1Qty

Specifies the quantity of vertical plates. Vertical plates are not shown when you
set MultiQty to zero.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the vertical plates. Individual vertical plates can be located
in one of the following ways:

* 1 - Relative to center of the group
* 2 - Relative to edge


None:  The meaning of the individual vertical plate location changes based on the quantity
of vertical plates. The value can be 0 (nothing), 1 (center), or 2 (edge).

IJUAhsMulti1::Multi1Location

Specifies the exact location of the vertical plates based on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge, or a center-to-center spacing.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Corner Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/806012?contentId=bZx9M2LTJztNMNsnXVSXIg)
The corner properties define the specifications for each corner and use the following
short codes:

* TL - TopLeft
* TR - TopRight
* BL - BottomLeft
* BR - BottomRight

The following properties are optional and are used for different corner shapes for
the plate:


Image:[Alt-Text: RiserLug - Corner Properties 
Image-Analysis: The image depicts a rectangular box with labeled sides indicating the cardinal directions: Top, Bottom, Left, and Right. Within this rectangle, there are two red arrows. The arrow pointing downwards is labeled "X," and the arrow pointing upwards is labeled "Z." The arrows likely represent vertical dimensions or forces acting in the downward and upward directions, respectively. This arrangement suggests a representation of coordinates or dimensions related to a two-dimensional space within the rectangle, potentially for geometric reasoning or analysis. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q3Co6Aa9gTFWZWTg12PXHg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/q3Co6Aa9gTFWZWTg12PXHg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner1::TLCornerType1

Specifies the corner type for the top left corner of the plate. TLCornerType1 takes a codelist value defined in hsCornerShape sheet of the HS\_S3DParts\_Codelist.xls workbook. Similar properties are applicable for the other three corner types, TR,
BL, and BR. Codelist numbers and the respective corner types are as shown below:

* 0 - None
* 1 - [Rectangular Notch Corner](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/UOnWiKb0y78xRewu16TlUg)


look for an icon that resembles a simple outline of the state of Utah, with a distinctive notch on the upper left side: 

* 2 - [Angled Notch Corner - XY Chamfer](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/paSYp5DkySI1z53m~oB12A)
* 3 - [Angled Notch Corner - XY Edges](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/paSYp5DkySI1z53m~oB12A)
* 4 - [Angled Notch Corner - X with an angle](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/paSYp5DkySI1z53m~oB12A)
* 5 - [Angled Notch Corner - Y with an angle](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/paSYp5DkySI1z53m~oB12A)


look for icon that looks like a folded paper or document: 

* 6 - [Rounded Notch Corner (Concave)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/UdiK0Pn4SYJBO1eRJObvlQ)


look for an icon that resembles a folded paper or a document outline: 

* 7 - [Round Corner (Convex)](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/0ITE59277LM7kA6VLrbPvA)


look for an icon that resembles a rounded corner or edge, commonly used in design or layout contexts: 

IJUAhsTLCorner1::TLCornerX1

Specifies the horizontal size of the corner shape.

IJUAhsTLCorner1::TLCornerY1

Specifies the vertical size of the corner shape.

IJUAhsTLCorner1::TLCornerRadius1

Specifies the radius of the corner shape.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rectangular Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/811942?contentId=LT9kmXSWQrZNku8zheehcQ)
IJUAhsTLCorner1::TLCornerType1

Specifies the corner type for the plate. Use codelist value 1 for this corner type.
See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes.

Codelist hsCornerShape 1 – Rectangular Notch


look for an icon that resembles a blank document with a folded top corner: 

IJUAhsTLCorner1::TLCornerX1

Specifies the horizontal dimension of the rectangular notch.


Image:[Alt-Text: RiserLug - Corner Properties - CornerType1 - Rectangular Notch 
Image-Analysis: The image depicts a design for a corner layout, specifically referring to a "TL Corner," which suggests a top-left corner modification in some graphical or architectural context. The lines illustrate a segmented area, possibly representing how corners are treated in a design or layout structure. The elements in the image include arrows indicating directionality or movement between components, and the mention of "X" may imply a crossing or intersection point. Overall, this design could relate to UI design, architectural drawings, or flow layouts, focusing on how to effectively manage corner spaces. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YV8Dan85tEVEAInKOKNUhQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - CornerType1 - Rectangular Notch](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/YV8Dan85tEVEAInKOKNUhQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner1::TLCornerY1

Specifies the vertical size of the rectangular notch. TLCornerY1 takes a positive value and must be less than the Length1 value.


Image:[Alt-Text: RiserLug - Corner Properties - TL CornerY1 - Rectangular Notch 
Image-Analysis: The image illustrates a simple diagram labeled "TLCornerY", likely signifying a top-left corner position within a coordinate system or a user interface layout. The diagram contains vertical arrows pointing upwards and downwards, suggesting movement or positioning within that corner area. The horizontal line represents an edge of a shape or boundary. The context implies that this could relate to graphical or UI design, where the top-left corner is often used for placing elements or defining starting points. The elements are connected by the arrows indicating their positional relationships. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e~0ezSkjgNf9d58zrMTwEw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - TL CornerY1 - Rectangular Notch](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/e~0ezSkjgNf9d58zrMTwEw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner1::TLCornerRadius1

Specifies the radius of the rectangular notch. TLCornerRadius1 value is ignored.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Angled Notch Corner - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/811938?contentId=wRTvY8znrYuaJ08GoHfs6A)
IJUAhsTLCorner1::TLCornerType1

Specifies the corner type for the angled notch. TLCornerType1 uses codelist values 2, 3, or 5. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes.

Codelist hsCornerShape 2 – Rectangular Notch


look for icon that looks like a folded piece of paper or a document with a corner turned down: 

IJUAhsTLCorner1::TLCornerX1 -

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Codelist Value | 2 | 3 | 4 | 5 |
| Corner Type | XY Chamfer | XY Edges | X with an Angle | Y with an Angle |
| X | RiserLug - Corner Properties - CornerType1 - TL Rectangular Notch[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/~eaVrOSpjXoV0EJcE2~5vg-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - XY Edges[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zioM0bEkuzKsEsL7Eh_ilg-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - X with an Angle[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/fwsflAOae2kp_8LhFxYfQg-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - Y with an Angle[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cC4d2phkOIHAXoJ2pF48Jg-_PVFQNoCl4XmjAxWO0f7XQ/content) |
| Description of X | Size of chamfer | Size of straight edge | Size of chamfer | Angle from vertical |
| Limits of X | X > 0 | X >= 0 | X > 0 | X > 0  (Angle in degrees) |
| X <= Width1 | X < Width1 | X <= Width1 | Calculated X <= Width1 |

IJUAhsTLCorner1::TLCornerY1 -

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Codelist Value | 2 | 3 | 4 | 5 |
| Corner Type | XY Chamfer | XY Edges | X with an Angle | Y with an Angle |
| Y | RiserLug - Corner Properties - TLCornerType1 - XY Chamfer Y1[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/HSpal2UApFlWdAhpIdM_xA-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - XY Edges - Y1[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UOj2Mz4QGiqZft~fTghVlg-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - X with an Angle - Y1[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cu6NrPQdSr_WwmSNATeEAA-_PVFQNoCl4XmjAxWO0f7XQ/content) | RiserLug - Corner Properties - TLCornerType1 - Y with an Angle - Y1[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/6Md2YmO_B8pHXDZgOHXzQw-_PVFQNoCl4XmjAxWO0f7XQ/content) |
| Description of Y | Size of chamfer | Size of straight edge | Angle from vertical | Size of chamfer |
| Limits of Y | Y > 0 | Y >= 0 | Y > 0  (Angle in degrees) | Y > 0 |
| Y <= Length | Y < Length | Calculated Y <= Length | Y <= Lenght |

IJUAhsTLCorner1::TLCornerRadius1

Specifies the radius of the angled notch shape. Use this when the two outside points
of the notch must be rounded using the corner radius value. You must set the radius
small enough to allow tangents on the top, the left, and the slanted face. If this
value is set to zero, then the software draws a sharp corner. This value cannot be
negative.


Image:[Alt-Text: RiserLug - Corner Properties - TLCornerRadius1 
Image-Analysis: The image shows two separate rectangular shapes, each with a rounded top, containing two distinct pieces of text. On the left shape, the letter "X" is positioned at the bottom left corner, while the letter "Y" is located above it towards the center. Similarly, the right shape also features the letter "X" at the bottom left and the letter "Y" slightly above it. This arrangement suggests a similar structure on both sides with a focus on the letters X and Y, which may represent variables or markers in a mathematical or logical context. The alignment of letters could imply a relationship or categorization between the two groups represented by the shapes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qVewKgak485LJydv0~O0vQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - TLCornerRadius1](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qVewKgak485LJydv0~O0vQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Rounded Notch Corner (Concave) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/811943?contentId=wdfgBzcLbDmfPtUaxFIZQQ)
IJUAhsTLCorner1::TLCornerType1

Specifies the corner type for the rounded notch. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. Use codelist value 6 for this corner type.


icon that looks like a rectangular shape with a curved top edge, often representing a piece of paper or document: 

IJUAhsTLCorner1::TLCornerX1

Specifies the horizontal offset of the round notch center point. You can not offset
the round notch off the plate in either direction. For both corners to be rounded
as shown below, set the value to less than half of Width1.


icon-description for a shape resembling a container or rectangular box with rounded corners at the top: 

If the TLCornerX1 value is set to zero then, the notch center is aligned with the top-left corner point
and the notch shape is a quarter circle arc.

X = 0, Zero Offset


look for icon that looks like a shape with an upper corner cut out, with a plus sign in the top left corner: 

If the TLCornerX1 value is set to a positive value then, the software moves the center point into the
plate horizontally and adds a flat landing to the quarter-circle arc.

X > 0, Positive Offset


Image:[Alt-Text: RiserLug - Corner Properties - TLCornerX1 - X>0 
Image-Analysis: The image depicts a basic schematic representation of a capacitor in an electrical circuit. The capacitor is shown on the right side as a rectangular block with a curved top, indicating its function to store electrical energy. On the left side, there are two vertical lines that represent the leads of the capacitor, one of which is marked with a plus sign, indicating the positive terminal. This suggests that the capacitor is polarized, meaning it has a specific positive and negative orientation for connection in a circuit. The overall image conveys fundamental information about the structure of a capacitor and its terminals. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5B~mmfBg2xUxRxlmvfLPcQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - TLCornerX1 - X>0](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/5B~mmfBg2xUxRxlmvfLPcQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the TLCornerX1 value is set to a negative value then, the software moves the center point away from
the plate horizontally. This reduces the sweep angle of the notch shape and is less
than a quarter-circle.

X < 0, Negative Offset


Image:[Alt-Text: RiserLug - Corner Properties - TLCornerX1 - X<0 
Image-Analysis: The image illustrates a schematic representation of an electrical component, likely a capacitor, with two terminals shown on the top left. The two arrows indicate the direction of flow for electrical current while the rectangular shape suggests the case or body of the component. This design emphasizes how the component is integrated into a circuit, highlighting its connections to other components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3lN67rvXUamjIgkvrIqqGg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - TLCornerX1 - X<0](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/3lN67rvXUamjIgkvrIqqGg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner1::TLCornerY1

Specifies the vertical offset of the round notch center point. You can not offset
the round notch off the plate in either direction. If the TLCornerY1 value is set to zero then, the notch center is aligned with the top-left corner point
and the notch shape is a quarter circle arc.

Y = 0, Zero Offset


look for icon that looks like a shape with an upper corner cut out, with a plus sign in the top left corner: 

If the TLCornerY1 value is set to a positive value then, the software moves the center point into the
plate vertically and adds a flat landing to the quarter-circle arc.

Y > 0, Positive Offset


Image:[Image-Analysis: The image depicts a simplified diagram showcasing a mechanical or structural component. It appears to illustrate a section of a beam or plate that has bending moments applied to it, represented by the arrows at the top indicating forces acting downwards. The curved part on the right side suggests that it is illustrating the cross-section of a structure that is experiencing bending, possibly in a way that shows a support (the vertical line) to the left. The horizontal line represents the top of the beam or structural element. This type of diagram is often used in engineering to analyze stresses and forces in beams or similar structures. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xL9VOFc_D6dJLMXqyJGEZA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xL9VOFc_D6dJLMXqyJGEZA-_PVFQNoCl4XmjAxWO0f7XQ/content)

If the TLCornerY1 value is set to a negative value then, the software moves the center point away from
the plate vertically. This reduces the sweep angle of the notch shape and is less
than a quarter-circle.

Y < 0, Negative Offset


Image:[Alt-Text: RiserLug - Corner Properties - TLCornerY1 - Y<0 
Image-Analysis: The image displays a diagram with directional arrows and a rectangular shape that appears to be a container or a box. The arrows indicate movements or relationships - one going upward, pointing at the top, and another pointing downward, signaling a possible flow of information or energy. The rectangular container could represent a storage space or a functional area that interacts with the upward and downward movements represented by the arrows. This suggests a conceptual relationship where something is either entering or becoming emitted from this container, illustrating a process or system of exchange. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gW7sNOoooGGmGnj2A~pFSw-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![RiserLug - Corner Properties - TLCornerY1 - Y<0](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/gW7sNOoooGGmGnj2A~pFSw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner1::TLCornerRadius1

Specifies the radius of the round notch shape.

If you require space in the X direction, the TLCornerRadius1 value must be greater than zero and less than Width1 value.

If you require space in the Y direction, the TLCornerRadius1 value must be greater than zero and less than Length1 value.

If the TLCornerRadius1 value is set to zero, the software creates a sharp corner edge.


look for an icon that resembles a cursor clicking or pointing to a page: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Round Corner (Convex) - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/811944?contentId=bRoyzUG7i9vG6~qbUKi93w)
IJUAhsTLCorner1::TLCornerType1

Specifies the corner type for the rounded notch. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. Use codelist value 7 for this corner type.


look for an icon that resembles a blank corner of a paper with a curved top edge, similar to a note or a sticky note: 

IJUAhsTLCorner1::TLCornerX1

Specifies the horizontal offset of the round notch center point. You can not offset
the round notch off the plate in either direction. If you use a positive value, the
software uses an equivalent negative value.

If you set the value to zero then, the rounded corner is placed tangent with each
edge as shown below. The notch shape is a quarter-circle arc.

X = 0, Zero Offset


look for icon that looks like a plus sign inside a rectangle with rounded corners: 

If the TLCornerX1 value is set to a negative value then, the software moves the center point away from
the plate horizontally. This reduces the sweep angle of the notch shape and is less
than a quarter-circle.

X < 0, Negative Offset


look for icon that resembles a document or note with arrows indicating a flow or direction, suggesting movement or transfer of information: 

IJUAhsTLCorner1::TLCornerY1

Specifies the vertical offset of the round notch center point. You can not offset
the round notch off the plate in either direction. If you use a positive value, the
software uses an equivalent negative value.

If you set the value to zero then, the rounded corner is placed tangent with each
edge as shown below. The notch shape is a quarter-circle arc.

Y = 0, Zero Offset


look for icon that looks like a plus sign inside a rectangle with rounded corners: 

If the TLCornerY1 value is set to a negative value then, the software moves the center point away from
the plate vertically. This reduces the sweep angle of the notch shape and is less
than a quarter-circle.

Y < 0, Negative Offset


look for icon that resembles a battery with a plus and minus sign, indicating charge or power levels.: 

IJUAhsTLCorner1::TLCornerRadius1

Specifies the radius of the round notch shape.

If you require space in the X direction, the TLCornerRadius1 value must be greater than zero and less than Width1 value.

If you require space in the Y direction, the TLCornerRadius1 value must be greater than zero and less than Length1 value.

If the TLCornerRadius1 value is set to zero, the software creates a sharp corner edge.


look for an icon that resembles a corner folded page with an arrow pointing upwards, indicating a potential action such as moving or expanding.: 

IJUAhsBLCorner1::BLCornerType1

Specifies the corner type. Use codelist value 7 for the corner type. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType1 is applicable for all the vertical plates if the plate quantity is greater than 1.

IJUAhsBLCorner1::BLCornerX1

Specifies the horizontal size of the rectangular notch. BLCornerX1 takes a positive value and must be less than the Width1 value.

IJUAhsBLCorner1::BLCornerY1

Specifies the vertical size of the rectangular notch. BLCornerY1 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsBLCorner1::BLCornerRadius1

Specifies the radius of the angled notch shape. Use the BLCornerRadius1 value when the two outside points of the notch must be rounded using the corner radius
value.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Top Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/806039?contentId=JMKz~mR2sEJn4pWxmmQz1g)
IJUAhsLength2::Length2

Specifies the length of the top plate. Length2 is an optional property and if you
do not assign a value, the software does not display the top plate.

![RiserLug Top Plate Properties - Length2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zFylG1V9EUcKzCrag7H7Jg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7a728a72e6530365)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zFylG1V9EUcKzCrag7H7Jg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth2::Width2

Specifies the width of the top plate. Width2 is an optional property and if you do
not assign a value, the software does not display the top plate.

![RiserLug Top Plate Properties - Width2](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uoXctFvPl0ru~b48yZELOw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=4245923f93d203a4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/uoXctFvPl0ru~b48yZELOw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness2::Thickness2

Specifies the thickness of the top plate. Length2 is an optional property and if you
do not assign a value, the software does not display the top plate.

IJUAhsTLCorner2::TLCornerType2

Specifies the corner type of the top plate. Use codelist value 1 for this corner type.
See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType2 is applicable for all the vertical plates if the plate quantity is greater than 1.

IJUAhsTLCorner2::TLCornerX2

Specifies the horizontal size of the rectangular notch. TLCornerX2 takes a positive value and must be less than the Width1 value.

IJUAhsTLCorner2::TLCornerY2

Specifies the vertical size of the rectangular notch. TLCornerY2 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsTLCorner2::TLCornerRadius2

Specifies the radius of the angled notch shape. Use the TLCornerRadius2 value when the two outside points of the notch must be rounded using the corner radius
value.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Bottom Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/806546?contentId=WGG3ZwnYd0msQWhzTf6Eeg)
IJUAhsLength3::Length3

Specifies the length of the bottom plate. Length3 is an optional property and if you do not assign a value, the software does not display
the top plate.

![RiserLug Bottom Plate Properties - Length3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Z4o6RZ~54iRyy8iqA1YHQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d287754d07fe1ce0)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/7Z4o6RZ~54iRyy8iqA1YHQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsWidth3::Width3

Specifies the width of the bottom plate. Width3 is an optional property and if you do not assign a value, the software does not display
the top plate.

![RiserLug](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/N82ezDjqZo87Ncu353YJeA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=5c112ce11fdee017)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/N82ezDjqZo87Ncu353YJeA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsThickness3::Thickness3

Specifies the thickness of the vertical plate. Thickness3 is an optional property and if you do not assign a value, the software does not display
the top plate.

IJUAhsTLCorner3::TLCornerType3

Specifies the corner type of the bottom plate. Use codelist value 1 for this corner
type. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType3 is applicable for all the vertical plates if the plate quantity is greater than 1.

![RiserLug Top Plate Properties - CornerType3](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xU73F0R0_Qq6j5tLNweiMA-_PVFQNoCl4XmjAxWO0f7XQ/content?v=36fe1feb34af7ca8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/xU73F0R0_Qq6j5tLNweiMA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsTLCorner3::TLCornerX3

Specifies the horizontal size of the rectangular notch. TLCornerX3 takes a positive value and must be less than the Width1 value.

IJUAhsTLCorner3::TLCornerY3

Specifies the vertical size of the rectangular notch. TLCornerY3 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsTLCorner3::TLCornerRadius3

Specifies the radius of the angled notch shape. Use the TLCornerRadius3 value when the two outside points of the notch must be rounded using the corner radius
value.

IJUAhsBLCorner3::BLCornerType3

Specifies the corner type of the bottom plate. Use codelist value 1 for this corner
type. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType3 is applicable for all the corner plates if the plate quantity is greater than 1.

IJUAhsBLCorner3::BLCornerX3

Specifies the horizontal size of the rectangular notch. BLCornerX3 takes a positive value and must be less than the Width1 value.

IJUAhsBLCorner3::BLCornerY3

Specifies the vertical size of the rectangular notch. BLCornerY3 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsBLCorner3::BLCornerRadius3

Specifies the radius of the angled notch shape. Use the BLCornerRadius3 value when the two outside points of the notch must be rounded using the corner radius
value.

IJUAhsTRCorner3::TRCornerType3

Specifies the corner type of the bottom plate. Use codelist value 1 for this corner
type. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType3 is applicable for all the corner plates if the plate quantity is greater than 1.

IJUAhsTRCorner3::TRCornerX3

Specifies the horizontal size of the rectangular notch. TRCornerX3 takes a positive value and must be less than the Width1 value.

IJUAhsTRCorner3::TRCornerY3

Specifies the vertical size of the rectangular notch. TRCornerY3 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsTRCorner3::TRCornerRadius3

Specifies the radius of the angled notch shape. Use the TRCornerRadius3 value when the two outside points of the notch must be rounded using the corner radius
value.

IJUAhsBRCorner3::BRCornerType3

Specifies the corner type of the bottom plate. Use codelist value 1 for this corner
type. See the hsCornerShape sheet from the HS\_S3DParts\_Codelist.xls workbook for all the valid codes. CornerType3 is applicable for all the corner plates if the plate quantity is greater than 1.

IJUAhsBRCorner3::BRCornerX3

Specifies the horizontal size of the rectangular notch. BRCornerX3 takes a positive value and must be less than the Width1 value.

IJUAhsBRCorner3::BRCornerY3

Specifies the vertical size of the rectangular notch. BRCornerY3 takes a positive value and must be less than the Height1-Thickness1 value.

IJUAhsBRCorner3::BRCornerRadius3

Specifies the radius of the angled notch shape. Use the BRCornerRadius3 value when the two outside points of the notch must be rounded using the corner radius
value.# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Port Details - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/806555?contentId=17tN9rXwMRXIAC3KvNEVkw)
The following properties are used to specify the different port types and their sizes
for the RiserLug.

![RiserLug Port Properties](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/De5IgSSb_tk7K~2qfj5p3Q-_PVFQNoCl4XmjAxWO0f7XQ/content?v=7762e31f15e95d50)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/De5IgSSb_tk7K~2qfj5p3Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

Port1 - Route (0, 0, 0)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 2 - Route | Pipe outside diameter | Pipe outside diameter | Pipe outside diameter |

Port2 - Hole1/Structure1 (0, 0, Offset)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004/3 - Hole/Structure | Rod Diameter | 0 | RodDiameter/9999 |

Port3 - Hole2/Structure2 (0, 0, Offset)

|  |  |  |  |
| --- | --- | --- | --- |
| Port Type | Size | MinSize | MaxSize |
| 1004/3 - Hole/Structure | Rod Diameter | 0 | RodDiameter/9999 |

Port Positions

![RiserLug - Port Details - Port Positions](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hWigA4jkzm~Qg4WIbJARjg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=75e3d1a058175ce4)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/hWigA4jkzm~Qg4WIbJARjg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Shoe - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325303?contentId=myhM39TB8iAB8VUCets5Pg)
Library Name: SmartParts  
Workbook: HS\_S3DParts.xls  
Codelist: HS\_S3DParts\_Codelist.xls  
ProgID: HSSmartPart,Ingr.SP3D.Content.Support.Symbols.Shoe  
Part Name: Shoe  
Part Description: Shoe SmartPart

![shoe](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DpVu3wICavpMqk6DROwpGw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=73851011e906658e)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/DpVu3wICavpMqk6DROwpGw-_PVFQNoCl4XmjAxWO0f7XQ/content)

Prerequisites

Make sure that the following BulkLoad.xls workbooks in [Product Folder]\CatalogData\BulkLoad\DataFiles\
is already bulkloaded.

* AllCodeLists.xls
* AllCommon.xls
* GenericNamingRules.xls
* HS\_System.xls
* HS\_System\_Codelist.xls
* HS\_S3DParts\_Codelists.xls

Sample SmartPart data is provided in HS\_S3DParts.xls which is delivered in [Product
Folder]\CatalogData\BulkLoad\DataFiles.

Part Placement

To place a sample slide plate SmartPart delivered with the catalog:

1. Click Tasks > Hanger and Supports.
2. Place a design support on a pipe.
3. Click Place Part
look for icon that looks like a plus sign with a price tag, often associated with adding or tagging items related to pricing or promotion: , and then select the design support.
4. In the Select Part dialog box, select a part from Parts > SmartParts > S3D Standard > Shoe Supports > Adjustable Shoe as shown below.


Image:[Alt-Text: shoe (1) 
Image-Analysis: The image illustrates a hierarchical structure or tree diagram representing various components under the category "SmartParts." At the top level, there is "S3D Standard," which branches out into several subcategories. The main subcategories include "Beam Attachments," "Clevises," "Miscellaneous," "Pipe Clamps," "Pipe Straps," "Plates," "Rod Fittings," "Rods," "Saddles and Shields," and "Shoe Supports." The "Shoe Supports" category further expands to include an item labeled "Adjustable Shoe," indicating it is a specific type of shoe support. This structure helps to organize and categorize different parts systematically, making it easier to navigate through various components and their relationship to the broader category. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BqVnLXwTrFL~Gmr~ZUYGMg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (1)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/BqVnLXwTrFL~Gmr~ZUYGMg-_PVFQNoCl4XmjAxWO0f7XQ/content)

Part Properties

Millimeters (mm) is the default unit. Use "in" at the end of dimensional values to
specify inches. Ports are shown as points highlighted in red.

Local Coordinate System


Image:[Alt-Text: shoe (3) 
Image-Analysis: The image depicts a diagram illustrating a pipe and its associated coordinate system. On the left, there is a circular icon suggesting a rotational movement or a cylindrical shape with a central axis, complemented by a base. The right side of the image features a horizontal pipe labeled with coordinates (0, 0, 0), indicating its position in a three-dimensional space. The dimensions of the coordinate system are further defined by two arrows: one pointing horizontally labeled as "X" and the other pointing downward labeled as "Z". This suggests a Cartesian coordinate system where the pipe's position and orientation can be described using these axes. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cZlqRJ_FxzkEPRP8ujmBJg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (3)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cZlqRJ_FxzkEPRP8ujmBJg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Basic Shoe Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325317?contentId=rtdF5~Fm29w2A7Il6ccE9w)
These properties define the shape and structure of the shoe body.

IJUAhsShoeShape::ShoeShape

Specifies shape of the shoe to be used. Enter shoe name associated to a certain shoe
in the shoe shape table. For more information on Shoe shape details, see [Shoe Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/rzC1uNOnkhKbEL~jJiaKag)

IJOAhsShoeHeight::ShoeHeight

Defines the height of the shoe from the bottom of the pipe to the bottom of the shoe,
including all plates, guides, pads, and so on. When ShoeHeight is not set to any value, the shoe height is calculated by combining all the specified
shapes. When set to zero, this value is ignored.


Image:[Alt-Text: shoe (4) 
Image-Analysis: The image depicts a simplified diagram indicating a height measurement. It features a vertical line that represents the height, measured from a base to a specific point above it. The point marked with a red square is likely an indicator of the height being measured. The circular design above may represent a point of interest or an object whose height is being evaluated. The term "Height" is labeled at the side to identify the purpose of the diagram, emphasizing that it pertains to a measurement of vertical distance from the base to the point designated above. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OhNOvlOp_FHUww4NwogOKQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (4)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/OhNOvlOp_FHUww4NwogOKQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeWidth::ShoeWidth - (Override Property)

Defines the width of the shoe which overrides already defined ShoeShape Width.


Image:[Alt-Text: shoe (5) 
Image-Analysis: The image illustrates a diagram with measurements related to width. It features a vertical line with a circular symbol at the top. The circular symbol has a red point indicating a reference point on it. The base of the vertical line is connected to a horizontal line which spans horizontally and is marked with directional arrows indicating the extent of the width. A label "Width" is placed at the bottom of the image, likely identifying the measurement being depicted. This diagram may be used in contexts such as engineering or technical design to understand the dimensions of an object or component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qfFiDeec2aYZWy_D5A00Ew-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (5)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/qfFiDeec2aYZWy_D5A00Ew-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsShoeLength::ShoeLength - (Override Property)

Defines the length of the shoe which overrides already defined ShoeShape Length.


Image:[Alt-Text: shoe (6) 
Image-Analysis: The image depicts a simple diagram illustrating the concept of "Length". At the top, there are dashed lines representing two endpoints connected by a horizontal line. Below, a rectangular shape is shown, which is labeled with the word "Length" at the bottom. The red dots at the ends of the length indicate measurement points, visually emphasizing the distance being represented. This diagram likely serves to explain how to measure the length of an object, highlighting the importance of the endpoints in that measurement. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O49LluD958cBqWGLr6YyCQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (6)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/O49LluD958cBqWGLr6YyCQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsShoeGap::ShoeGap

Specifies distance between the pipe surface and the shoe top edge. This value must
be greater than or equal to zero. Also, ShoeGap must be less than the ShoeHeight.


Image:[Alt-Text: shoe (7) 
Image-Analysis: The image illustrates a technical concept involving a gap between two objects. It shows a horizontal rectangular block positioned beneath a dashed line that represents another object above it. The dashed lines denote a clearance or spacing defined as the "Gap," which is quantified by the vertical arrows indicating the distance between the objects. Additionally, there are red dots marking specific points, potentially indicating reference locations for measurement or analysis of the gap. This type of diagram is often used in engineering or design contexts to ensure adequate spacing for functionality or safety. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kQ8IYEDiYVzCuTHDxOn3Pg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (7)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/kQ8IYEDiYVzCuTHDxOn3Pg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsDiamter1::Diamter1

Defines the nominal diameter of the pipe.


Image:[Alt-Text: shoe (8) 
Image-Analysis: The image depicts a mechanical diagram showing a circular object with a diameter indicated by the label "Diameter1." There is also a vertical arrow next to the circle, suggesting a measurement of height or distance, while the base appears to represent a mounting or support structure for the circular object. This diagram is likely part of a technical or engineering illustration that demonstrates dimensions relevant for the design or analysis of mechanical components. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cc4wknWUWJqYkUTz0rNIYQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (8)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/cc4wknWUWJqYkUTz0rNIYQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsSlopeAngle::SlopeAngle

Specifies slope angle of the pipe supported by the shoe. SlopeAngle overrides the shoe angle specified in the shoe shape xls.

IJUAhsShoeQty::ShoeQty

Specifies the number of shoe shapes and the location of the shoe.

If ShoeQty is

* 1 – Bottom
* 2 – Bottom, Top
* 3 – Bottom, Left, Right
* 4 – Bottom, top, Right, Left

IJOAhsInsulationTh::InsulationTh

Specifies the insulation thickness.


Image:[Alt-Text: insulation thickness 
Image-Analysis: The image depicts a diagram that illustrates a structure with a circular component at the top and a vertical support at the bottom. Inside the circular component, there is a depiction of a swirling line, which may represent a flow or a movement pattern. The diagram includes annotations indicating "Insulation Thickness," suggesting that the image is related to concepts of insulation in a specific context, likely pertaining to thermal or electrical insulation. The vertical support indicates that this structure is standing on a base, implying a physical setup where insulation thickness is a critical measurement in relation to the circular component. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/E3L~KZe6xXYNbygJHDWyXA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![insulation thickness](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/E3L~KZe6xXYNbygJHDWyXA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJOAhsInsulationL::InsulationLength

Specifies the length of the insulation.


None: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Leg Spacing Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/665296?contentId=bIfhKyEqjBw9pcZagxcN~g)
IJUAhsShoeLegSpace::LegSpace

Specifies the spacing between the legs on the upper side but is not applicable for
ShoeType 3 and 9.

When the ShoeType is 3 or 9, the leg spacing depends on the codelist value for [Shoe Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/rzC1uNOnkhKbEL~jJiaKag).

IJUAhsShoeLegLowSpace::LegLowSpace

Specifies the spacing between the legs on the lower side and is applicable only for
ShoeType 7.

![Illustration of Shoe Leg Lower Spacing - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dhQgVzSRl6HdSQjHZmQ6hg-_PVFQNoCl4XmjAxWO0f7XQ/content?v=d1e92d0107875ae3)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/dhQgVzSRl6HdSQjHZmQ6hg-_PVFQNoCl4XmjAxWO0f7XQ/content)

![Illustration of Shoe Space Frm - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D8EI7_qE~9n2Wj8ORLulkQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=ea0e0b3117b9bda8)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/D8EI7_qE~9n2Wj8ORLulkQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [End Plate Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325353?contentId=13LHQnUr3lwY96Jxii6eZg)
IJUAhsShoeEndPlate::EndPlateNum

Specifies the number of end plates. If the value is greater than one, only two end
plates are drawn.

IJOAhsShoeEndPlate::EndPlateHeight (Override Property)

Overrides the height of the end plate defined in the Parts catalog.


Image:[Alt-Text: shoe(End plate properties) 
Image-Analysis: The image depicts a technical illustration showing an end plate's dimensions. It features a rectangular shape representing the end plate with arrows indicating the height measurement. The text "End Plate Height" indicates this is a dimension related to the height of the end plate. Additionally, there are red markers at the top and bottom of the rectangle, which may signify points of measurement or features of interest in the design. The overall focus of the image is to convey specific dimensions related to the height of the end plate structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zESFCvRu7X2_sBb4JL0Qsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe(End plate properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/zESFCvRu7X2_sBb4JL0Qsg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsEndPlateOffset::EndPlateOffset

Specifies offset of the end plate from the center of the shoe along the length.

If EndPlateNum > 1, then the outside edge of the end plate is flush with the end of the shoe (the
default position). EndPlateOffset moves the end plate along the shoe. A positive value moves the end plate toward the
center of the shoe. A negative value moves the end plate away from the center of the
shoe.

IJUAhsShoeEndPlate::PlateShape

Specifies name of the plate. The plate name is required for the plate to be drawn.
For more information on plate shape details, see [Plate Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/mJQkALuDD6MiGWwj0PYgwg).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Pad Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325363?contentId=j97~EaVlzsQMye5wmrYwzQ)
IJUAhsRepadShape::RepadShape

It is the string specifying the name of the repad. The repad name is required for
the repad to be drawn. For more information on shield shape (repad) details, see [Shield Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/zE0Dq8eKkCQI5_YsU~vgQA).

IJUAhsMulti1::Multi1Qty

Specifies the quantity of pads. Pads are not shown when Multi1Qty is set to zero.

IJUAhsMulti1::Multi1LocateBy

Specifies the location of the bolts. Each bolt can be located in two ways.

1 - Relative to center of the group  
2 - Relative to edge.

The exact meaning depends on the quantity of bolts. This value can be 0 (nothing), 1 (center), or 2 (Edge).

IJUAhsMulti1::Multi1Location

Specifies the distance for exact location of the pads depending on Multi1LocateBy and Multi1Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw)

IJUAhsShoePad::RepadOffset1

Offsets the Repad(s) along the x-axis of the pipe.

IJUAhsRepadLength::RepadLength (Override Property)

Specifies the length of the shoe repad which overrides the already defined Repad Shape
Length1, Length 2, and Length 3 properties.


Image:[Image-Analysis: The image shows a schematic representation of a mechanical or structural system, likely illustrating the concept of load distribution along a beam and supports. The two vertical lines on either side represent supports or columns that help support a horizontal member, indicated by the dashed line above. These supports are marked with arrows, suggesting that they are responding to compressive forces directed towards the center of the beam. There is a central red point, which might symbolize a point of application for load or a point of interest in analyzing the forces acting on the system. The image likely aims to explain the relationship between the applied forces, support reactions, and the overall stability of the mechanical structure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i_G1aW9GhIPtnXNj36YKxg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/i_G1aW9GhIPtnXNj36YKxg-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsRepadThickness::RepadThickness

Specifies thickness of the lower curved plate. The RepadThickness overrides the Thickness1 in [Shield Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/zE0Dq8eKkCQI5_YsU~vgQA).

IJUAhsPadLengthSel::PadLengthSel

Specifies the codelist value for the length of the Clamp.

The following values are supported:

1 = Auto - length is based on the length of the Shoe

2 = Input - length is based on the input from the occurrence.

IJUAhsPadLenOvrHng::PadLenOvrHng

Specifies the overhang for the Shoe length. If the codelist value of IJUAhsPadLengthSel::PadLengthSel is 1, then the length is based on the length of the Shoe. You can specify overhang
and the IJUAhsPadLenOvrHng::PadLenOvrHng attribute controls the overhang.


Image:[Alt-Text: Illustration of Pad Length Overhang - Shoe Attributes 
Image-Analysis: The image displays a simple diagram representing a sliding mechanism or a movable drawer. The top rectangle indicates a stationary part, while the lower section, which has arrows pointing left and right, shows that it can slide back and forth. There are also horizontal lines depicting the structure or framework within which this sliding mechanism operates. The absence of labels suggests that it is an abstract illustration, but the arrows clearly communicate the sliding action. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P_f4JH31MEKpBIrrMIjFsg-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Pad Length Overhang - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/P_f4JH31MEKpBIrrMIjFsg-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Clamp Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325367?contentId=gqkmOeOH4fYgDgOFZlErbw)
IJUAhsClampShape::ClampShape

It is the string specifying the name of the clamp. The clamp name is required for
the clamp to be drawn. For more information on clamp shape details, see [Clamp Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/~XTaC6Du53R6Y0iz~BpDRg).

IJUAhsMulti2::Multi2Qty

Specifies the quantity of clamps. Clamps are not shown when Multi2Qty is set to zero.

IJUAhsMulti2::Multi2LocateBy

Specifies the location of the clamps. Individual clamps can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of clamps. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti2::Multi2Location

Specifies the distance for exact location of the clamps depending on Multi2LocateBy and Multi2Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsClampOff::ClampOffset1

Offsets the clamp(s) along the x-axis of the pipe.

IJOAhsClampAngle::ClampAngle

Specifies the angle that a clamp body rotates in counter-clockwise when looking along
the positive X direction of the pipe port. ClampAngle overrides Angle3 in the Clamp Shape.

![Illustration of Clamp Angle - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UVRSrpUUT6bcwTtbqUOEYw-_PVFQNoCl4XmjAxWO0f7XQ/content?v=3803374c7f99b631)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/UVRSrpUUT6bcwTtbqUOEYw-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampWidth1::ClampWidth1

Specifies the width of the lower side of the Clamp.

IJUAhsClampWidth2::ClampWidth2

Specifies the width of the upper side of the Clamp.

![Illustration of Clamp Width1 and Width2 - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bLbaaKqshksHKKA8x~fCwQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=57e9c47995b90f7a)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/bLbaaKqshksHKKA8x~fCwQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampWidthSel::ClampWidthSel

Specifies the codelist value for the length of the Clamp.

The following values are supported:

1 = Auto - length is based on the length of the Shoe  
2 = Input - length is based on the input from the occurrence.

IJUAhsClampLenOvrHng::ClampLenOvrHng

Specifies the overhang for the Shoe length. If the codelist value of IJUAhsClampWidthSel::ClampWidthSel is 1, then the length is based on the length of the Shoe. You can specify overhang
and the IJUAhsClampLenOvrHng::ClampLenOvrHng attribute controls the overhang.


Image:[Alt-Text: Illustration of Clamp Length Overhang - Shoe Attributes 
Image-Analysis: The image depicts a flowchart or a schematic representation related to a mechanical or structural component, possibly illustrating the layout of a mechanism involving movement or connections. There are various horizontal and vertical lines that may indicate pathways or connections. The central rectangular shape at the bottom represents a component that connects to the lines above, suggesting a functional relationship. The arrows indicate direction or movement, emphasizing interactions in the design. Overall, this image likely serves to convey information about a system's configuration or operational procedure. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JDLtCCk_6OeUB4wstrqD7Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Clamp Length Overhang - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/JDLtCCk_6OeUB4wstrqD7Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampDiameter1::ClampDiameter1

Specifies the diameter of the Clamp.


Image:[Alt-Text: Illustration of Clamp Diameter - Shoe Attributes 
Image-Analysis: The image depicts a simple mechanical device that possibly illustrates a mechanism involving a circular object. The main feature is a large circular area, which appears to represent a wheel or disk. Horizontal arrows indicate a distance measurement across the circle, suggesting the diameter is being referenced. There are also elements on either side that resemble mounts or supports, potentially indicating how this circular object would be held in place or rotated. The supports do not touch the circle, highlighting that it is a free-moving item, often seen in diagrams related to engineering or machinery, showcasing the principle of rotation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61IZjNp678Lm7XLaYIccTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Clamp Diameter - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61IZjNp678Lm7XLaYIccTA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampBoltOff1::ClampBoltOffset1

Specifies the offset for Bolt1 from the center of the Shoe.

IJUAhsClampBoltOff2::ClampBoltOffset2

Specifies the offset for Bolt2 from the center of the Shoe.

IJUAhsClampBoltOff3::ClampBoltOffset3

Specifies the offset for Bolt3 from the center of the Shoe.

IJUAhsClampBoltOff4::ClampBoltOffset4

Specifies the offset for Bolt4 from the center of the Shoe.

IJUAhsClampBoltOff5::ClampBoltOffset5

Specifies the offset for Bolt5 from the center of the Shoe.

IJUAhsClampBoltOff6::ClampBoltOffset6

Specifies the offset for Bolt6 from the center of the Shoe.

![Illustration of Clamp Bolt Offset 6 - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vTNkttV8C~5e8nGYIYZ2oQ-_PVFQNoCl4XmjAxWO0f7XQ/content?v=1bb279d6989b274c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/vTNkttV8C~5e8nGYIYZ2oQ-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampDiameter4::ClampDiameter4

Specifies the diameter of the Clamp including the liner.


Image:[Alt-Text: Illustration of Clamp Diameter - Shoe Attributes 
Image-Analysis: The image depicts a simple mechanical device that possibly illustrates a mechanism involving a circular object. The main feature is a large circular area, which appears to represent a wheel or disk. Horizontal arrows indicate a distance measurement across the circle, suggesting the diameter is being referenced. There are also elements on either side that resemble mounts or supports, potentially indicating how this circular object would be held in place or rotated. The supports do not touch the circle, highlighting that it is a free-moving item, often seen in diagrams related to engineering or machinery, showcasing the principle of rotation. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61IZjNp678Lm7XLaYIccTA-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Clamp Diameter - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/61IZjNp678Lm7XLaYIccTA-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsClampWidth4::ClampWidth4

Specifies the length of the liner.


Image:[Alt-Text: Illustration of Clamp Width4 - Shoe Attributes 
Image-Analysis: The image appears to be a technical illustration of a mechanical component, possibly a type of coupling or connector used in machinery. It features several horizontal lines that could represent rods or pipes, along with two arrows pointing outward at the top, possibly indicating directions of movement or flow. At the bottom, there is a rectangular shape that may represent a base or mounting point. The overall structure suggests a design that facilitates the connection of multiple parts while allowing for some adjustable spacing or alignment, which could be important in mechanical assemblies. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nTqKoGD9ASIzS9Xs7VMzxQ-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![Illustration of Clamp Width4 - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/nTqKoGD9ASIzS9Xs7VMzxQ-_PVFQNoCl4XmjAxWO0f7XQ/content)# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [U-Bolt properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325378?contentId=fa2OF~9gr8Ur27WALZd2qA)
IJUAhsUBoltShape::UBoltShape

Specifies the name of the U-Bolt. The U-Bolt name is required for the U-Bolt to be
drawn. For more information on U-Bolt shape details, see [U-Bolt Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/IRCzDjR5EN6GAA675peEDw).

IJUAhsMulti3::Multi3Qty

Specifies the quantity of U-Bolts. U-Bolts are not shown when Multi3Qty is set to zero.

IJUAhsMulti3::Multi3LocateBy

Specifies the location of the U-Bolts.

Individual U-Bolts can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of U-Bolts. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti3::Multi3Location

Specifies the distance for exact location of the U-Bolts depending on Multi3LocateBy and Multi3Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).# [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Gusset Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325382?contentId=Rw9wFJX6a1VQAejKmg3iQA)
IJUAhsGussetPlate::Shape

Specifies the name of the gusset plate. The gusset plate name is required for the
gusset plate to be drawn. For more information on plate (gusset) shape details, see
[Plate Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/mJQkALuDD6MiGWwj0PYgwg).

IJUAhsMulti5::Multi5Qty

Specifies the quantity of gusset plates. Gusset plates are not shown when Multi5Qty is set to zero.

IJUAhsMulti5::Multi5LocateBy

Specifies the location of the gusset plates. Individual gusset plates can be located
in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of gusset plates. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti5::Multi5Location

Specifies the distance for exact location of the gusset plates depending on Multi5LocateBy and Multi5Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsGussetGap::GussetGap

Specifies the gap between the gussets along the width.


None: 

IJUAhsGussetHeight::GussetHeight

Overrides the height of the guides.


look for icon that looks like two columns with horizontal lines, suggesting a grid or list format: # [Intergraph Smart 3D Hangers and Supports SmartParts Configuration](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/1354795)
###### [Guide Properties - Intergraph Smart 3D - Reference Data - Hexagon](https://docs.hexagonppm.com/r/en-US/Intergraph-Smart-3D-Hangers-and-Supports-SmartParts-Configuration/14/325387?contentId=vasy0t5B7j7X2v9ux7p8bQ)
IJUAhsGuideShape::GuideShape

Specifying the name of the guide. The guide name is required for the guide to be drawn.
For more information on guide shape details, see [Guide Shape](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/yn8Ia1Zy6FmL_lWA0kYVmA).

IJUAhsMulti6::Multi6Qty

Specifies the quantity of guides. Guides are not shown when Multi6Qty is set to zero.

IJUAhsMulti6::Multi6LocateBy

Specifies the location of the guides. Individual guides can be located in two ways.

1 - Relative to Center of the group  
2 - Relative to Edge.

The exact meaning depends on the quantity of guides. This value can be 0 (nothing),
1 (center), or 2 (Edge).

IJUAhsMulti6::Multi6Location

Specifies the distance for exact location of the guides depending on Multi6LocateBy and Multi6Qty. This value can be either a distance to the edge, or a center-to-center spacing.
For more information on multi position details, see [Multi Position](https://docs.hexagonppm.com/r/_PVFQNoCl4XmjAxWO0f7XQ/k8HIwbPOyMQcNWTXE6fAtw).

IJUAhsGuide::VerticalOffset

Defines the vertical offset of the guide with respect to structure port.


Image:[Alt-Text: shoe (Guide Properties) 
Image-Analysis: The image depicts a diagram illustrating the concept of vertical offset in a mechanical or structural context. It features a central structure with a rounded top and two vertical supports extending downward. To the right of the main structure, there is a highlighted section with a small red item, indicating a point of interest, likely representing the point of vertical offset. Lines showing vertical measurements are drawn beside this offset area, indicating the distances involved. The term "Vertical Offset" is labeled at the bottom, suggesting this diagram serves to explain how vertical offset affects the positioning or alignment of components in a system. 
Link-to-Image: https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yn8kfGxhCxh6VPNTfyx51Q-_PVFQNoCl4XmjAxWO0f7XQ/content]
 ![shoe (Guide Properties)](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/Yn8kfGxhCxh6VPNTfyx51Q-_PVFQNoCl4XmjAxWO0f7XQ/content)

IJUAhsGuideGap::GuideGap

Specifies the gap between the Guide and the Shoe edge.

![Illustration of Guide Gap - Shoe Attributes](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SYLcu5ogwaeRAyfLC2L9Ig-_PVFQNoCl4XmjAxWO0f7XQ/content?v=f39d5bff904c9a5c)[#Image\_link#](https://docs.hexagonppm.com/api/khub/maps/_PVFQNoCl4XmjAxWO0f7XQ/resources/SYLcu5ogwaeRAyfLC2L9Ig-_PVFQNoCl4XmjAxWO0f7XQ/content)