from extractor import extract_data
from mapper import map_to_excel_fields
from excel_engine import fill_sheet

# IMAGE_PATH = "test_images/sample_plate.png"
IMAGE_PATH = input("Enter the path to the image: ")
TEMPLATE_PATH = "templates/Input_Parts.xlsx"
OUTPUT_PATH = "Output_Plate_POC.xlsx"

def run():

    print("Detecting part type and extracting data from image...")
    Part_json, Part_Type = extract_data(IMAGE_PATH)

    print(f"Part type detected: {Part_Type}")
    print("Mapping fields...")
    mapped_data = map_to_excel_fields(Part_json, Part_Type)

    print("Filling Excel template...")
    fill_sheet(TEMPLATE_PATH, OUTPUT_PATH, mapped_data, Part_Type)

    print("POC completed successfully.")

if __name__ == "__main__":
    run()