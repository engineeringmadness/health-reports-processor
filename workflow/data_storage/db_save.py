from prefect import task, get_run_logger
from workflow.data_storage.repo import save_extracted_data


@task(name='Database Sink', description='Map and save attributes from JSON into Postgres tables')
def save_data_to_db(data: dict, prescription_id: str):
    logger = get_run_logger()
    logger.info('Saving basic attributes')
    save_extracted_data(data, prescription_id)