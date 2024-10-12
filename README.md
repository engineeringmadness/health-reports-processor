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

1. Install Miniconda python runtime - https://docs.anaconda.com/miniconda/. While installing ensure to check the box for adding miniconda to path or add the location manually to path variable
![image](https://github.com/user-attachments/assets/04d4a847-73c0-4fa2-b5ed-0c267f07ba1d)
2. Create a new conda environment
> conda create -n medicine
3. Install required dependencies
> conda activate medicine

> pip install -r requirements.txt
3. Prefect library requires a server and worker node to be running for viewing and executing flows. use the starter scripts to spin up both
> .\start_prefect.ps1
4. Start core workflow application
> Run file workflow\deploy_flow.py from Pycharm or VS code if you want to use GUI to trigger flow

> Run file workflow\local_run.py from Pycharm or VS Code if you want to run the flow from command line itself

5. Navigate to http://localhost:4200/ and go to deployments tab

![image](https://github.com/user-attachments/assets/7b576e5c-1980-47a1-bd84-6d6b9a85051e)

6. Click on 3 dots -> quick run -> Feed in required parameters and click Run
![image](https://github.com/user-attachments/assets/f06fcfaa-a39d-44db-82e2-38cf6cbd259a)

7. Go to runs tab to see execution
![image](https://github.com/user-attachments/assets/392b150a-1b94-4ee8-95b2-3377f3999c6b)



