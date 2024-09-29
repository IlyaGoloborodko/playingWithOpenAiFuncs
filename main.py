import json

from ai_calls import ai_calling, send_func_result
from funcs_for_openai.get_delivery_date import get_delivery_date


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
        if response.tool_calls:
            tool_call = response.tool_calls[0]
            arguments = json.loads(tool_call.function.arguments)
            order_id = int(arguments.get('order_id'))
            delivery_date = get_delivery_date(order_id)

            result_message = {
                "role": "tool",
                "content": json.dumps({
                    "order_id": order_id,
                    "delivery_date": delivery_date.strftime('%Y-%m-%d %H:%M:%S')
                }),
                "tool_call_id": tool_call.id
            }

            messages.append(response)
            messages.append(result_message)

            response = send_func_result(messages)

        assistant_message = response.content
        messages.append({'role': 'assistant', 'content': assistant_message})

        print(assistant_message)


