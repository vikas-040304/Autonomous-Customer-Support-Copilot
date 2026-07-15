import sqlite3
import pandas as pd


def get_all_tickets():

    conn = sqlite3.connect("database/tickets.db")

    df = pd.read_sql_query(
        """
        SELECT
            ticket_id AS 'Ticket ID',
            question AS 'Question',
            category AS 'Category',
            priority AS 'Priority',
            status AS 'Status'
        FROM tickets
        ORDER BY ticket_id DESC
        """,
        conn,
    )

    conn.close()

    return df