import sqlite3
import time
import requests
import os
from app.config import Config


# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


# =========================
# DB CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# GET PAID + ACTIVE USERS ONLY
# =========================
def get_paid_users():

    try:
        conn = get_db()
        cur = conn.cursor()

        users = cur.execute("""
            SELECT DISTINCT u.telegram_id
            FROM users u
            JOIN payments p
            ON u.phone = p.phone
            WHERE u.status = 'active'
            AND u.telegram_id IS NOT NULL
            AND p.status = 'approved'
        """).fetchall()

        conn.close()

        return [u["telegram_id"] for u in users]

    except Exception as e:
        print("DB error (paid users):", e)
        return []


# =========================
# SEND TELEGRAM MESSAGE
# =========================
def send_message(chat_id, text):

    try:
        requests.post(API_URL, data={
            "chat_id": chat_id,
            "text": text
        }, timeout=10)

    except Exception as e:
        print(f"Telegram send error -> {chat_id}:", e)


# =========================
# FORMAT SIGNAL
# =========================
def format_signal(signal):

    return f"""
📊 NEW TRADE SIGNAL

📌 Asset: {signal['asset']}
💰 Entry: {signal['entry']}
🎯 TP: {signal['tp']}
🛑 SL: {signal['sl']}

📡 Status: {signal['status']}

⚡ PESAMATRIX PRO
"""


# =========================
# GET LATEST SIGNAL
# =========================
def get_latest_signal():

    try:
        conn = get_db()
        cur = conn.cursor()

        signal = cur.execute("""
            SELECT *
            FROM signals
            ORDER BY id DESC
            LIMIT 1
        """).fetchone()

        conn.close()
        return signal

    except Exception as e:
        print("DB error (signals):", e)
        return None


# =========================
# BOT LOOP (SMART BROADCAST)
# =========================
def watch_signals():

    print("🤖 SaaS Telegram Bot Started...")

    last_sent_id = None

    while True:

        signal = get_latest_signal()

        # ONLY NEW SIGNALS
        if signal and signal["id"] != last_sent_id:

            last_sent_id = signal["id"]

            message = format_signal(signal)

            users = get_paid_users()

            print(f"📤 Sending signal ID {signal['id']} to {len(users)} paid users")

            for chat_id in users:
                send_message(chat_id, message)

            print("✅ Broadcast complete")

        time.sleep(5)


# =========================
# START BOT
# =========================
if __name__ == "__main__":
    watch_signals()
