from prefect import task, get_run_logger
from workflow.data_storage.repo import save_extracted_data, save_schedule

@task(name='Database Sink', description='Map and save attributes from JSON into Postgres tables')
def save_data_to_db(data: dict, prescription_id: str):
    logger = get_run_logger()
    logger.info('Saving basic attributes')
    relevant_keys = [i for i in data.keys()]
    relevant_keys.remove('medicines')
    basic_attributes = {x:data[x] for x in relevant_keys}
    save_extracted_data(basic_attributes, prescription_id)

    logger.info('Saving medicine schedule')
    save_schedule(data['medicines'], prescription_id)