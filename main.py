import json

from ai_calls import ai_calling


messages = [
    {"role": "system", "content": "You are a helpful customer support assistant."
                                  " Use the supplied tools to assist the user."},
]

if __name__ == "__main__":

    print('Привет, что вы хотите узнать?\n'
          'Остановить процесс можно, введя команду "/stop"')

    while True:
        message = input()
        if message == '/stop':
            break
        messages.append({'role': 'user', 'content': message})

        response = ai_calling(messages)
        # tool_call = completion.choices[0].message.tool_calls[0]
        # arguments = json.loads(tool_call['function']['arguments'])

        assistant_message = response.content
        messages.append({'role': 'assistant', 'content': assistant_message})

        print(assistant_message)


