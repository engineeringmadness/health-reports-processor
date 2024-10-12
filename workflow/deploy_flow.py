from workflow.prefect_flow import main_flow
import uuid

if __name__ == '__main__':
    main_flow.serve(name='local-deployment',
                    description='Rx OCR pipeline',
                    parameters={"image_path": "",
                                "extension": "jpeg",
                                "prescription_id": str(uuid.uuid4())})