conda activate medicine
pip install -r requirements.txt
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
prefect config set PREFECT_API_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:$env:PG_PASSWORD@localhost:5432/prefect"
prefect config set PREFECT_RESULTS_PERSIST_BY_DEFAULT=true
prefect config set PREFECT_LOCAL_STORAGE_PATH='../results/'
Start-Process powershell 'prefect server start'
