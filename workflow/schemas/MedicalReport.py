from PIL.ImImagePlugin import number
from pydantic import BaseModel, Field
from typing import Optional

class MedicalTest(BaseModel):
    test_name: Optional[str] = Field(description='Name of test e.g. Haemoglobin, RBC, TLC, LDL, HDL')
    test_value: Optional[str] = Field(description='value of metric for patient')
    unit: Optional[str] = Field(description='units in which value is provided')
    bio_ref_interval: Optional[str] = Field(description='range of healthy values')


class MedicalReport(BaseModel):
    patient_name: Optional[str] = Field(description='Name of the patient whose report is given'),
    patient_age: Optional[int] = Field(description='Age of the patient whose report is given'),
    report_date: Optional[str] = Field(description='Date of report generation'),
    sample_collection_date: Optional[str] = Field(description='Date of collection of sample (blood, urine)'),
    lab_name: Optional[str] = Field(description='Lab which has performed the tests')
    tests: Optional[list[MedicalTest]] = Field(description='Different tests done as part of report')