from workflow.conversion.constants import PydanticModels
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

    prescription_schema = PydanticModels.get_model(model).model_json_schema()
    tools = [
        {
            "name": "build_object_model",
            "description": f"Build the {model} object",
            "input_schema": prescription_schema
        }
    ]
    prompt = f"""
                {specific_prompt}
                If any attribute is not found in the text extract output it as empty string in the JSON.
                Do not give any extra text in the output apart the usage of provided tool.

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

    if model == PydanticModels.PRESCRIPTION:
        return Prescription.model_validate(output)


def calculate_total_cost(logger, prompt: str, json_output: str):
    cost1 = calculate_prompt_cost(prompt, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    cost2 = calculate_completion_cost(json_output, os.environ['STRUCTURED_OUTPUTS_MODEL'])
    total_cost = cost1 + cost2
    logger.info("Response Token Cost: " + str(total_cost))
    return total_cost
