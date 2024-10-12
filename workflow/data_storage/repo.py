from workflow.data_storage.db import db
from workflow.data_storage.entities import PrescriptionSchedule, PrescriptionAttributes, OcrOutput

def save_extracted_data(attributes: dict[str, str], prescription_id: str):
    """
    Save master data attributes from the prescription image
    :param attributes: dictionary created from JSON outputs
    :param prescription_id: primary key of prescription coming from BFF
    :return:
    """
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
    session.close()

def save_schedule(schedule: list[dict[str, str]], prescription_id: str):
    """
    Save the different medicines included in prescription
    :param schedule: Regimen of medicine and their frequencies
    :param prescription_id: primary key of prescription coming from BFF
    :return:
    """
    session = db.get_session()

    for entry in schedule:
        line_item = PrescriptionSchedule(medicine_name=entry['medicineName'],
                                         frequency=entry['medicineFrequency'],
                                         prescription_id=prescription_id)
        session.add(line_item)

    session.commit()
    session.close()

def save_raw_data(text: str, prescription_id: str):
    """
    Save raw text from OCR layer in case of reprocessing or backfilling
    :param text: raw text output
    :param prescription_id: primary key of prescription coming from BFF
    :return:
    """
    session = db.get_session()
    data = OcrOutput(document_id=prescription_id, raw_data=text)
    session.add(data)
    session.commit()
    session.close()