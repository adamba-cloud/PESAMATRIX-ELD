import sqlite3
import uuid
from flask import current_app

def get_db():
    return sqlite3.connect(current_app.config["DATABASE"])


# =========================
# CREATE USER (FIXED)
# =========================
def create_user(name, phone, email, password):

    conn = get_db()
    cur = conn.cursor()

    account_number = str(uuid.uuid4())[:8]

    cur.execute("""
        INSERT INTO users (name, phone, email, password, account_number)
        VALUES (?, ?, ?, ?, ?)
    """, (name, phone, email, password, account_number))

    conn.commit()
    conn.close()

    return account_number


# =========================
# AUTHENTICATE USER
# =========================
def authenticate(phone, password):

    conn = get_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    user = cur.execute("""
        SELECT * FROM users
        WHERE phone=? AND password=?
    """, (phone, password)).fetchone()

    conn.close()
    return user
