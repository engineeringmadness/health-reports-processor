from workflow.conversion.constants import PydanticModels
from workflow.schemas.MedicalReport import MedicalReport
from workflow.schemas.Prescription import Prescription
from workflow.utils.agent import get_claude_agent
from prefect import task, get_run_logger
from tokencost import calculate_prompt_cost, calculate_completion_cost
from workflow.data_storage.repo import update_raw_data
import os


@task(name='Structured Outputs V2', description='Translate the provided text into Pydantic model')
def convert_to_pydantic(doc_text: str, model: str, specific_prompt: str, document_id: str):
    logger = get_run_logger()

    agent = get_claude_agent()

    schema = PydanticModels.get_model(model).model_json_schema()
    logger.info("Transcribing into schema: " + str(schema))
    tools = [
        {
            "name": "build_object_model",
            "description": f"Build the {model} object",
            "input_schema": schema
        }
    ]
    prompt = f"""
                {specific_prompt}
                
                Do not add extra attributes to function call apart from the ones specified in schema.
                Do not give any extra text in the output apart the usage of provided tool.
                If any of the fields in schema are not found then give it the value of empty string.
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
        ],
        tools=tools,
        tool_choice={"type": "tool", "name": "build_object_model"}
    )

    output = response.content[0].input
    logger.info(output)
    total_cost = calculate_total_cost(logger, prompt, str(output))
    update_raw_data(str(output), document_id, total_cost)
    return PydanticModels.get_model(model).model_validate(output)


def calculate_total_cost(logger, prompt: str, json_output: str):
    cost1 = calculate_prompt_cost(prompt, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    cost2 = calculate_completion_cost(json_output, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    total_cost = cost1 + cost2
    logger.info("Response Token Cost: " + str(total_cost))
    return total_cost
