from workflow.data_storage.db import db
from workflow.data_storage.entities import PrescriptionSchedule, PrescriptionAttributes, OcrOutput
from workflow.schemas.Prescription import Prescription


def save_extracted_data(attributes: dict[str, str], prescription_id: str):
    """
    Save master data attributes from the prescription image and schedules
    :param attributes: dictionary created from JSON outputs
    :param prescription_id: primary key of prescription coming from BFF
    :return:
    """
    session = db.get_session()

    master = PrescriptionAttributes(
        doctor_name=attributes['doctorName'],
        prescription_date=attributes['prescriptionDate'],
        prescription_id=prescription_id,
        doctor_address = attributes['doctorAddress'],
        diagnoses = attributes['diagnoses']
    )
    for entry in attributes['medicines']:
        line_item = PrescriptionSchedule(medicine_name=entry['medicineName'],
                                         frequency=entry['medicineFrequency'],
                                         prescription_id=prescription_id)
        session.add(line_item)

    session.add(master)
    session.commit()
    session.close()


def save_extracted_data_typed(prescription: Prescription, prescription_id: str):
    """
    Save prescription model into DB
    :param attributes: Pydantic model representing prescription
    :param prescription_id: primary key of prescription coming from BFF
    :return:
    """
    session = db.get_session()

    master = PrescriptionAttributes(
        doctor_name=prescription.doctorName,
        prescription_date=prescription.prescriptionDate,
        prescription_id=prescription_id,
        doctor_address = prescription.doctorAddress,
        diagnoses = prescription.diagnoses
    )
    for entry in prescription.medicines:
        line_item = PrescriptionSchedule(medicine_name=entry.medicineName,
                                         frequency=entry.medicineFrequency,
                                         prescription_id=prescription_id)
        session.add(line_item)

    session.add(master)
    session.commit()
    session.close()


def save_raw_data(text: str, prescription_id: str, cost):
    """
    Save raw text from OCR layer in case of reprocessing or backfilling
    :param text: raw text output
    :param prescription_id: primary key of prescription coming from BFF
    :param cost: cost of tokens (input + output)
    :return:
    """
    session = db.get_session()
    data = OcrOutput(document_id=prescription_id, raw_data=text, ocr_cost=cost)
    session.add(data)
    session.commit()
    session.close()

def update_raw_data(json_dump: str, prescription_id: str, cost):
    """
    Saves the structured output layer json in case of reprocessing or backfilling
    :param json_dump: json output
    :param prescription_id: primary key of prescription coming from BFF
    :param cost: cost of tokens (input + output)
    :return:
    """
    session = db.get_session()
    data: OcrOutput = session.query(OcrOutput).get(prescription_id)
    data.json_dump = json_dump
    data.json_cost = cost
    session.commit()
    session.close()