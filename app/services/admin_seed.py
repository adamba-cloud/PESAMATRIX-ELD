import sqlite3
from app.config import Config


def create_admin():
    conn = sqlite3.connect(Config.DATABASE)
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET role='admin'
        WHERE phone='254717434943'
    """)

    conn.commit()
    conn.close()

    print("✅ Admin user activated")
