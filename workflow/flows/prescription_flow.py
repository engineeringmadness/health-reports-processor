from markdown_it.rules_inline import image
from prefect import flow
from workflow.conversion.prescription_structured_outputs import convert_to_json
from workflow.extraction.common_ocr import extract_text_from_doc
from workflow.data_storage.db_save import save_data_to_db
import base64

@flow(name="rx-e2e-flow")
def main_flow(image_path: str, extension: str, prescription_id: str):
    print('Working on file' + image_path)
    # Load image
    image_file = open(image_path, "rb")
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # OCR
    text = extract_text_from_doc(image=encoded_image, image_type=extension.lower())
    print('========================================')
    print(text)

    # Convert to JSON
    json = convert_to_json(text)
    print('========================================')
    print(json)

    # Save data to DB
    save_data_to_db(json, prescription_id)
    image_file.close()
