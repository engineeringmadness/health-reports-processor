from markdown_it.rules_inline import image
from prefect import flow, get_run_logger
from workflow.conversion.structured_outputs import convert_to_json
from workflow.conversion.prompts import SpecificPrompts
from workflow.extraction.common_ocr import extract_text_from_doc
from workflow.data_storage.db_save import save_data_to_db
import base64

@flow(name="rx-e2e-flow")
def main_flow(image_path: str, extension: str, prescription_id: str):
    logger = get_run_logger()
    logger.info('Working on file' + image_path)
    # Load image
    image_file = open(image_path, "rb")
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # OCR
    text = extract_text_from_doc(image=encoded_image,
                                 image_type=extension.lower(),
                                 document_id=prescription_id)
    logger.info('Done extracting text from image')

    # Convert to JSON
    json = convert_to_json(doc_text=text,
                           schema_file='prescription.json',
                           specific_prompt=SpecificPrompts.PRESCRIPTION)
    logger.info('Done extracting json from text')

    # Save data to DB
    save_data_to_db(json, prescription_id)
    image_file.close()
