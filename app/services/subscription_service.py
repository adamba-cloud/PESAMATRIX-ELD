import sqlite3
from datetime import datetime

def is_active(user):
    return user["status"] == "active"


def activate_user(db, phone):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute("""
        UPDATE users SET status='active' WHERE phone=?
    """, (phone,))

    conn.commit()
    conn.close()


def expire_check(user):
    # placeholder for expiry logic (future upgrade)
    return True
