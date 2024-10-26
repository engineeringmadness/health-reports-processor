import json
from workflow.utils.agent import get_claude_agent
from prefect import task, get_run_logger
from tokencost import calculate_prompt_cost, calculate_completion_cost
from workflow.data_storage.repo import update_raw_data
import os


@task(name='Structured Outputs', description='Translate the provided text into JSON schema')
def convert_to_json(doc_text: str, schema_file: str, specific_prompt: str, document_id: str) -> dict:
    logger = get_run_logger()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(current_dir, '..', 'schemas', schema_file), 'r')
    schema = f.read()
    f.close()
    logger.info('Transformation Schema: ')
    logger.info(schema)

    agent = get_claude_agent()

    prompt = f"""
                {specific_prompt}
                If any attribute is not found in the text extract output it as empty string in the JSON.
                Do not give any extra text in the output apart from the JSON.

                ###
                JSON Structure -
                {schema}

                ###
                Text -
                {doc_text} 
    """

    response = agent.messages.create(
        model=os.environ['STRUCTURED_OUTPUTS_MODEL'],
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    json_output = response.content[0].text
    total_cost = calculate_total_cost(logger, prompt, json_output)
    update_raw_data(json_output, document_id, total_cost)
    return json.loads(json_output)


def calculate_total_cost(logger, prompt: str, json_output: str):
    cost1 = calculate_prompt_cost(prompt, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    cost2 = calculate_completion_cost(json_output, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    total_cost = cost1 + cost2
    logger.info("Response Token Cost: " + str(total_cost))
    return total_cost
