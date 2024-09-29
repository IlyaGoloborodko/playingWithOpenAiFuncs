import os

from dotenv import load_dotenv
from openai import OpenAI

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(project_root, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ai_calling(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return completion

