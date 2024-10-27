from pydantic import BaseModel, Field
from typing import Optional

class Medicine(BaseModel):
    medicineName: Optional[str] = Field(description='Name of medicine')
    medicineFrequency: Optional[str] = Field(description='Frequency of medicine')


class Prescription(BaseModel):
    doctorName: Optional[str] = Field(description='Name of the doctor writing the prescription'),
    prescriptionDate: Optional[str] = Field(description='Date of prescription'),
    doctorAddress: Optional[str] = Field(description='Address of doctor'),
    diagnoses: Optional[str] = Field(description='Key Diagnosis of patient'),
    medicines: Optional[list[Medicine]] = Field(description='Medicines prescribed by doctor')