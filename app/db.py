import sqlite3
from flask import current_app


# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# INIT DATABASE
# =========================
def init_db():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    # USERS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user',
        status TEXT DEFAULT 'active',
        account_number TEXT,
        telegram_id TEXT
    )
    """)

    # PAYMENTS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT,
        mpesa TEXT,
        amount TEXT,
        plan TEXT,
        status TEXT
    )
    """)

    # SIGNALS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset TEXT,
        entry TEXT,
        tp TEXT,
        sl TEXT,
        status TEXT
    )
    """)

    # CONTENT
    cur.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        title TEXT,
        link TEXT
    )
    """)

    # LOGS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        user TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()
