import sqlite3

DB = "database/tickets.db"


def update_ticket_status(ticket_id, status):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tickets
        SET status=?
        WHERE ticket_id=?
        """,
        (status, ticket_id)
    )

    conn.commit()
    conn.close()