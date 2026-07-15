import sqlite3

DB_PATH = "database/feedback.db"


def get_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM feedback")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM feedback WHERE feedback='Helpful'")
    helpful = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM feedback WHERE feedback='Not Helpful'")
    not_helpful = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        satisfaction = 0
    else:
        satisfaction = round((helpful / total) * 100, 2)

    return helpful, not_helpful, total, satisfaction