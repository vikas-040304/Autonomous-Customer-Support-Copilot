import sqlite3

DB_PATH = "database/tickets.db"


def init_ticket_db():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            ticket_id TEXT PRIMARY KEY,
            question TEXT,
            category TEXT,
            priority TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_ticket(ticket_id, question, category, priority):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO tickets
        (ticket_id, question, category, priority, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        ticket_id,
        question,
        category,
        priority,
        "Open"
    ))

    conn.commit()
    conn.close()


def get_all_tickets():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tickets
        ORDER BY rowid DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_ticket_status(ticket_id, status):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tickets
        SET status=?
        WHERE ticket_id=?
    """, (
        status,
        ticket_id
    ))

    conn.commit()
    conn.close()