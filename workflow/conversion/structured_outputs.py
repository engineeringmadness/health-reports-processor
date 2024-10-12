import json
from workflow.utils.agent import get_claude_agent
from prefect import task
import os

@task(name='Structured Outputs', description='Translate the provided text into JSON schema')
def convert_to_json(doc_text: str, schema_file: str, specific_prompt)-> dict:
    agent = get_claude_agent()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(current_dir, '..', 'schemas', schema_file), 'r')
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
                    }
                ]
            }
        ]
    )

    return json.loads(response.content[0].text)
