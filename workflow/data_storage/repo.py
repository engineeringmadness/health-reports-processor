from workflow.data_storage.db import db
from workflow.data_storage.entities import PrescriptionSchedule, PrescriptionAttributes

def save_extracted_data(attributes: dict[str, str], prescription_id: str):
    master = PrescriptionAttributes(
        doctor_name=attributes['doctorName'],
        prescription_date=attributes['prescriptionDate'],
        prescription_id=prescription_id,
        doctor_address = attributes['doctorAddress'],
        diagnoses = attributes['diagnoses']
    )

    session = db.get_session()
    session.add(master)
    session.commit()

def save_schedule(schedule: list[dict[str, str]], prescription_id: str):
    session = db.get_session()

    for entry in schedule:
        line_item = PrescriptionSchedule(medicine_name=entry['medicineName'],
                                         frequency=entry['medicineFrequency'],
                                         prescription_id=prescription_id)
        session.add(line_item)

    session.commit()
