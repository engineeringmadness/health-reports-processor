from workflow.schemas.Prescription import Prescription


class SpecificPrompts:

    PRESCRIPTION = """
    From the below text of a medical prescription, extract the precise medicine names 
    and their frequencies and doctor details in the json format.                        
    """

class PydanticModels:
    PRESCRIPTION = "Prescription"

    @classmethod
    def get_model(cls, model):
        if model == cls.PRESCRIPTION:
            return Prescription