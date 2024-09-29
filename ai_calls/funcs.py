import os

from dotenv import load_dotenv
from openai import OpenAI

from funcs_for_openai.gpt_funcs_definitions import GET_DELIVERY_DATE_DEFINITION

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(project_root, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Определяем функции, которые может вызывать OpenAi
tools = [GET_DELIVERY_DATE_DEFINITION]


def ai_calling(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
    )

    return completion.choices[0].message


def send_func_result(messages):
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages
    )
    return completion.choices[0].message
