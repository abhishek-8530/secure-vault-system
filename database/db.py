import sqlite3

def init_db():
    conn = sqlite3.connect("intruder.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        status TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(status, image_path):
    conn = sqlite3.connect("intruder.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (timestamp, status, image_path) VALUES (datetime('now'), ?, ?)",
        (status, image_path)
    )

    conn.commit()
    conn.close()