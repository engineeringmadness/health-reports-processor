from pydantic import BaseModel, Field
from typing import Optional

class MedicalTest(BaseModel):
    test_name: Optional[str] = Field(description='Name of test e.g. Haemoglobin, RBC, TLC, LDL, HDL')
    test_value: Optional[str] = Field(description='Value of test for patient')
    ref_interval: Optional[str] = Field(description='range of healthy values')


class MedicalReport(BaseModel):
    patient_name: Optional[str] = Field(description='Name of the patient whose report is given'),
    patient_age: Optional[str] = Field(description='Age of the patient whose report is given'),
    report_date: Optional[str] = Field(description='Date of report generation'),
    sample_collection_date: Optional[str] = Field(description='Date of collection of sample (blood, urine)'),
    doctor_name: Optional[str] = Field(description='Doctor name')
    test_results: Optional[list[MedicalTest]] = Field(description='Different tests done as part of report')