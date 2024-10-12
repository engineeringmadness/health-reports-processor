import json
from workflow.utils.agent import get_claude_agent
from prefect import task
import os

@task(name='Structured Outputs', description='Translate the provided text into JSON schema')
def convert_to_json(doc_text: str)-> dict:
    agent = get_claude_agent()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(current_dir, 'schema.json'), 'r')
    schema = f.read()
    f.close()

    response = agent.messages.create(
        model=os.environ['STRUCTURED_OUTPUTS_MODEL'],
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                            From the below text extract of a medical prescription the precise medicine names and their frequencies and doctor details in the json format.
                            Do not give any extra text in the output apart from the JSON.

                            ###
                            JSON Structure -
                            {schema}

                            ###
                            Text -
                            {doc_text} 
                        """
                    }
                ]
            }
        ]
    )

    return json.loads(response.content[0].text)
