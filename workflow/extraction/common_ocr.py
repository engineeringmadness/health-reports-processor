import os
from workflow.utils.agent import get_claude_agent
from prefect import task, get_run_logger
from workflow.data_storage.repo import save_raw_data
from tokencost import calculate_cost_by_tokens, calculate_completion_cost

@task(name='OCR', description='Extracting the text of the document using Claude Vision API')
def extract_text_from_doc(image: str, width: int, height: int, image_type: str, document_id: str)-> str:
    logger = get_run_logger()
    logger.info('Image type: ' + image_type)
    agent = get_claude_agent()

    response = agent.messages.create(
        model=os.environ['OCR_MODEL'],
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": f"image/{image_type}",
                            "data": image
                        }
                    },
                    {
                        "type": "text",
                        "text": "Extract the text from the provided image"
                    }
                ]
            }
        ]
    )

    raw_data = response.content[0].text
    total_cost = calculate_total_cost(logger, width, height, raw_data)
    save_raw_data(raw_data, document_id, total_cost)
    return raw_data


def calculate_total_cost(logger, width: int, height: int, raw_data: str):
    # Formula for image tokens given on https://docs.anthropic.com/en/docs/build-with-claude/vision
    image_tokens = int((width * height)/750)
    cost1 = calculate_cost_by_tokens(image_tokens, os.environ['OCR_MODEL'], 'input')
    cost2 = calculate_completion_cost(raw_data, os.environ['OCR_MODEL'])
    total_cost = cost1 + cost2
    logger.info("Response Token Cost: " + str(total_cost))
    return total_cost
