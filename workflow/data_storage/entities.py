import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PrescriptionAttributes(Base):
    __tablename__ = 'prescription_attributes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doctor_name = db.Column(db.String(256),
                           primary_key=True)
    prescription_date = db.Column(db.Date)
    prescription_id = db.Column(db.String(256))
    doctor_address = db.Column(db.Text)
    diagnoses = db.Column(db.Text)


class PrescriptionSchedule(Base):
    __tablename__ = 'prescription_schedule'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prescription_id = db.Column(db.String(256))
    medicine_name = db.Column(db.Text)
    frequency = db.Column(db.Text)

class OcrOutput(Base):
    __tablename__ = 'document_parsing'

    document_id = db.Column(db.String(256), primary_key=True)
    raw_data = db.Column(db.Text)
    ocr_cost = db.Column(db.Double)
    json_dump = db.Column(db.Text)
    json_cost = db.Column(db.Double)
