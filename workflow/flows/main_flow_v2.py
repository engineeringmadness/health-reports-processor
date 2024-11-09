from prefect import flow, get_run_logger
from workflow.conversion.constants import SpecificPrompts, PydanticModels
from workflow.conversion.structured_outputs_v2 import convert_to_pydantic
from workflow.extraction.common_ocr import extract_text_from_doc
from workflow.data_storage.db_save_v2 import save_data_to_db
from PIL import Image
import base64
from workflow.schemas.Prescription import Prescription


@flow(name="rx-e2e-prescription-flow")
def main_flow(image_path: str, extension: str, prescription_id: str, model: str):
    logger = get_run_logger()
    logger.info('Working on file' + image_path)
    # Load image
    image_file = open(image_path, "rb")
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    img = Image.open(image_path)
    width, height = img.size
    img.close()
    image_file.close()

    # OCR
    text = extract_text_from_doc(image=encoded_image,
                                 width=width,
                                 height=height,
                                 image_type=extension.lower(),
                                 document_id=prescription_id)
    logger.info('Done extracting text from image')

    # Convert to Pydantic Model
    data: Prescription = convert_to_pydantic(doc_text=text,
                           model=model,
                           specific_prompt=SpecificPrompts.get_prompt(model),
                           document_id=prescription_id)
    logger.info('Done extracting model from text')

    # Save data to DB
    save_data_to_db(data, prescription_id, model)