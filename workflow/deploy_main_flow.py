from workflow.flows.prescription_flow_v2 import main_flow
import uuid

if __name__ == '__main__':
    main_flow.serve(name='rx-deployment',
                    description='Rx OCR pipeline',
                    parameters={"image_path": "",
                                "extension": "jpeg",
                                "prescription_id": str(uuid.uuid4())})