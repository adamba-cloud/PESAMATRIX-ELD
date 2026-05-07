from app import create_app
import sqlite3

app = create_app()

DB = app.config["DATABASE"]


# =========================
# INIT DATABASE TABLES
# =========================
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # USERS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT,
        password TEXT,
        role TEXT,
        status TEXT,
        account_number TEXT,
        telegram_id TEXT
    )
    """)

    # PAYMENTS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY,
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
        id INTEGER PRIMARY KEY,
        asset TEXT,
        entry TEXT,
        tp TEXT,
        sl TEXT,
        status TEXT
    )
    """)

    # CONTENT (IMAGES / VIDEOS / LINKS / NEWS)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        link TEXT
    )
    """)

    # LOGS
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


# =========================
# START APP
# =========================
if __name__ == "__main__":
    print("🚀 Starting PESAMATRIX PRO SaaS...")

    init_db()

    print("✅ Database ready")
    print("🌐 Server running on http://127.0.0.1:5000")

    app.run(debug=True)
