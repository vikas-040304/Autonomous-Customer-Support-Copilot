import pandas as pd
from chatbot.ticket_db import get_all_tickets


def load_ticket_table():
    tickets = get_all_tickets()

    columns = [
        "Ticket ID",
        "Question",
        "Category",
        "Priority",
        "Status"
    ]

    return pd.DataFrame(tickets, columns=columns)