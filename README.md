# Core Workflow

This repo contains batch jobs which will process the incoming scan of medical prescriptions / reports etc. The jobs are defined as workflows using Prefect library which supports local development as well as
docker / kubernetes deployments.

## Dependencies
1. prefect (workflow library)
2. anthropic (Claude LLM)
3. psycopg2 (PostgreSQL)
4. sqlalchemy (ORM)

## Basic Design
![Prefect Architecture](https://github.com/user-attachments/assets/92e9a94a-b004-46c3-b93c-e931bdad1e97)


## Get Started

### Prerequisites

- Install and setup Rancher Desktop, Miniconda, IDE of your choice for PostgreSQL and Python
- PG_PASSWORD & ANTHROPIC_KEY needs to be set as environment variable in windows.

### Database initial setup
> docker compose up postgres

2. Login to DB and execute content of ddl.sql

### Run Server and DB

> docker compose up postgres server healthcheck

### Run entire system via docker

> docker build -t rx-flow:0.1.0 .

> docker compose up

### To Run Flow code only via IDE (Skip if you want to run entire system via docker compose)

1. Install Miniconda python runtime - https://docs.anaconda.com/miniconda/. While installing ensure to check the box for adding miniconda to path or add the location manually to path variable
![image](https://github.com/user-attachments/assets/04d4a847-73c0-4fa2-b5ed-0c267f07ba1d)
2. Create a new conda environment
> conda create -n medicine
3. Install required dependencies
> conda activate medicine

> pip install -r requirements.txt

4. Start core workflow application
> Run file workflow\deploy_main_flow.py from Pycharm or VS code if you want to use GUI to trigger flow

### Run flow for sample image
1. Navigate to http://localhost:4200/ and go to deployments tab 
![image](https://github.com/user-attachments/assets/7b576e5c-1980-47a1-bd84-6d6b9a85051e)

2. Click on 3 dots -> quick run -> Feed in required parameters and click Run
![image](https://github.com/user-attachments/assets/f06fcfaa-a39d-44db-82e2-38cf6cbd259a)

3. Go to runs tab to see execution
![image](https://github.com/user-attachments/assets/392b150a-1b94-4ee8-95b2-3377f3999c6b)
