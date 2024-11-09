from prefect import task, get_run_logger

from workflow.conversion.constants import PydanticModels
from workflow.data_storage.repo import save_extracted_data_typed, save_extracted_data_typed_report
from workflow.schemas.MedicalReport import MedicalReport
from workflow.schemas.Prescription import Prescription


@task(name='Database Sink [MedicalReport]', description='Map and save attributes from Pydantic into Postgres tables')
def save_data_to_db_report(data: MedicalReport, prescription_id: str):
    logger = get_run_logger()
    logger.info('Saving basic attributes')
    save_extracted_data_typed_report(data, prescription_id)
