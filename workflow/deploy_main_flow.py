from workflow.conversion.constants import PydanticModels
from workflow.flows.main_flow_v2 import main_flow
import uuid

if __name__ == '__main__':
    main_flow.serve(name='rx-deployment',
                    description='Rx OCR pipeline',
                    parameters={"image_path": "",
                                "extension": "jpeg",
                                "document_id": str(uuid.uuid4()),
                                "model": PydanticModels.PRESCRIPTION})