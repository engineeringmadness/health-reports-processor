from workflow.schemas.MedicalReport import MedicalReport
from workflow.schemas.Prescription import Prescription


class SpecificPrompts:

    PRESCRIPTION = """
    From the below text of a medical prescription, extract the precise medicine names 
    and their frequencies and doctor details into provided schema.                        
    """

    REPORT = """
    From the below text of a medical report extract the test results which are given in 
    test name: test value (ref interval) format in the
    below text, along with patient name, patient age and the doctor name which has performed the tests
    into provided schema.
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