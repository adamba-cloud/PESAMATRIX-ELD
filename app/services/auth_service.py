import sqlite3
from flask import current_app

def get_db():
    return sqlite3.connect(current_app.config["DATABASE"])


def authenticate(phone, password):

    conn = get_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    user = cur.execute(
        "SELECT * FROM users WHERE phone=? AND password=?",
        (phone, password)
    ).fetchone()

    conn.close()
    return user


def set_admin(phone):

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET role='admin'
        WHERE phone=?
    """, (phone,))

    conn.commit()
    conn.close()
