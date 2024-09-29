import json
import os
import datetime

from typing import Optional

GET_DELIVERY_DATE_DEFINITION = {
    "type": "function",
    "function": {
        "name": "get_delivery_date",
        "description": "Get the delivery date for a customer's order."
                       " Call this whenever you need to know the delivery date,"
                       " for example when a customer asks 'Where is my package'",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "integer",
                    "description": "The customer's order ID.",
                },
            },
            "required": ["order_id"],
            "additionalProperties": False,
        }
    }
}


def load_orders():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    json_path = os.path.join(project_root, 'json_data', 'ordersData.json')
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data['orders']  # возвращаем список заказов


def get_delivery_date(order_id: int) -> Optional[datetime.datetime]:
    """
    :param order_id: ID заказа
    :return: Дата доставки, если заказ найден
             Иначе None
    """

    # Загружаем данные из JSON
    orders = load_orders()

    # Ищем заказ по order_id
    for order in orders:
        if order['order_id'] == order_id:
            # Преобразуем строку даты в объект datetime
            delivery_date = datetime.datetime.strptime(order['date'], '%Y-%m-%dT%H:%M:%S')
            return delivery_date

    return None
