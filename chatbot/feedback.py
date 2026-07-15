import sqlite3

DB_PATH = "database/feedback.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            feedback TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_feedback(question, answer, feedback):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO feedback(question, answer, feedback) VALUES (?, ?, ?)",
        (question, answer, feedback)
    )

    conn.commit()
    conn.close()