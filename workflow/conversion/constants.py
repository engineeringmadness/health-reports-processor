from workflow.schemas.MedicalReport import MedicalReport
from workflow.schemas.Prescription import Prescription


class SpecificPrompts:

    PRESCRIPTION = """
    From the below text of a medical prescription, extract the precise medicine names 
    and their frequencies and doctor details in the json format.                        
    """

    REPORT = """
    From the below text of a medical report, extract the precise Test names, values, units,
    reference intervals along with basic patient details in json format.
    """

    @classmethod
    def get_prompt(cls, model):
        if model == PydanticModels.PRESCRIPTION:
            return cls.PRESCRIPTION
        elif model == PydanticModels.REPORT:
            return cls.REPORT


class PydanticModels:
    PRESCRIPTION = "Prescription"
    REPORT = "Report"

    @classmethod
    def get_model(cls, model):
        if model == cls.PRESCRIPTION:
            return Prescription
        elif model == cls.REPORT:
            return MedicalReport