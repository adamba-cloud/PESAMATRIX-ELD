import sqlite3

def create_log_table(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY,
        action TEXT,
        user TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()
