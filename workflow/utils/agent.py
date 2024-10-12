import os
from anthropic import Anthropic

def get_claude_agent() -> Anthropic:
    api_key = os.environ['ANTHROPIC_KEY']
    return Anthropic(api_key=api_key)