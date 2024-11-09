FROM prefecthq/prefect:3.0.8-python3.12

WORKDIR /root
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /root/flows
COPY workflow ./workflow

ENV PYTHONPATH="${PYTHONPATH}:/root/flows/workflow/"

CMD ["python", "workflow/deploy_main_flow.py"]