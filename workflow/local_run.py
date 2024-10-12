from workflow.prefect_flow import main_flow
import sys
import uuid

if __name__ == '__main__':
    file_path = sys.argv[1]
    file_extension = sys.argv[2]
    main_flow(file_path, file_extension, str(uuid.uuid4()))