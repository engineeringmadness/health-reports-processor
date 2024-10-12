import os
from workflow.utils.agent import get_claude_agent
from prefect import task
from workflow.data_storage.repo import save_raw_data

@task(name='OCR', description='Extracting the text of the document using Claude Vision API')
def extract_text_from_doc(image: str, image_type: str, document_id: str)-> str:
    print('Image type: ' + image_type)
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
    save_raw_data(raw_data, document_id)
    return raw_data
