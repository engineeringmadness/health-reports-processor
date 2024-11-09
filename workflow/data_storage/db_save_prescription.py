from prefect import task, get_run_logger

from workflow.data_storage.repo import save_extracted_data_typed
from workflow.schemas.Prescription import Prescription


@task(name='Database Sink [Prescription]', description='Map and save attributes from Pydantic into Postgres tables')
def save_data_to_db_prescription(data: Prescription, prescription_id: str):
    logger = get_run_logger()
    logger.info('Saving basic attributes')
    save_extracted_data_typed(data, prescription_id)
