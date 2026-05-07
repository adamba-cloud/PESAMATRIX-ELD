import sqlite3
import time
import requests
from app.config import Config

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


# =========================
# DB CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# GET ACTIVE USERS (TELEGRAM ONLY)
# =========================
def get_active_users():
    conn = get_db()
    cur = conn.cursor()

    users = cur.execute("""
        SELECT telegram_id 
        FROM users 
        WHERE status='active' 
        AND telegram_id IS NOT NULL
    """).fetchall()

    conn.close()

    return [u["telegram_id"] for u in users]


# =========================
# SEND MESSAGE
# =========================
def send_message(chat_id, text):
    try:
        requests.post(API_URL, data={
            "chat_id": chat_id,
            "text": text
        })
    except Exception as e:
        print("Telegram error:", e)


# =========================
# FORMAT SIGNAL MESSAGE
# =========================
def format_signal(signal):
    return f"""
📊 NEW SIGNAL ALERT

📌 Asset: {signal['asset']}
💰 Entry: {signal['entry']}
🎯 TP: {signal['tp']}
🛑 SL: {signal['sl']}

⚡ PESAMATRIX PRO
"""


# =========================
# WATCH NEW SIGNALS
# =========================
def watch_signals():
    print("🤖 Telegram Bot Running...")

    last_id = 0

    while True:
        conn = get_db()
        cur = conn.cursor()

        signal = cur.execute("""
            SELECT * FROM signals 
            ORDER BY id DESC 
            LIMIT 1
        """).fetchone()

        conn.close()

        if signal and signal["id"] != last_id:
            last_id = signal["id"]

            message = format_signal(signal)
            users = get_active_users()

            for chat_id in users:
                send_message(chat_id, message)

            print("📤 Signal broadcast sent")

        time.sleep(5)


# =========================
# START BOT
# =========================
if __name__ == "__main__":
    watch_signals()
