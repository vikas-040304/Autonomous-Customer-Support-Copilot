import sqlite3

DB_PATH = "database/orders.db"


def init_orders():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            order_id TEXT PRIMARY KEY,
            customer TEXT,
            status TEXT,
            delivery_date TEXT
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO orders
        VALUES
        ('12345','Tony','Shipped','18 July 2026')
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO orders
        VALUES
        ('45678','Rahul','Delivered','10 July 2026')
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO orders
        VALUES
        ('78910','Vikas','Processing','20 July 2026')
    """)

    conn.commit()
    conn.close()


def get_order(order_id):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM orders WHERE order_id=?",
        (order_id,)
    )

    order = cursor.fetchone()

    conn.close()

    return order