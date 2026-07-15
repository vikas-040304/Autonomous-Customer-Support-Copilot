import re
from chatbot.orders import get_order


def check_order_query(question):
    """
    Detects an order ID in the user's question and returns order details.
    """

    match = re.search(r"\b\d{5}\b", question)

    if not match:
        return None

    order_id = match.group()

    order = get_order(order_id)

    if not order:
        return "❌ Order not found."

    return f"""
📦 Order Details

Order ID : {order[0]}

Customer : {order[1]}

Status : {order[2]}

Expected Delivery : {order[3]}
"""