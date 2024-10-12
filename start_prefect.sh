conda activate medicine
pip install -r requirements.txt
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
nohup prefect server start
nohup prefect worker start -p my-local-machine
