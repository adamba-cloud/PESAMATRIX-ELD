import sqlite3
import requests
from time import sleep

DB = "app.db"

# 🔑 PUT YOUR TELEGRAM BOT TOKEN HERE
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# =========================
# GET ACTIVE USERS ONLY
# =========================
def get_active_users():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    users = cur.execute("""
        SELECT phone FROM users WHERE status='active'
    """).fetchall()

    conn.close()
    return users


# =========================
# GET LATEST SIGNAL
# =========================
def get_latest_signal():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    signal = cur.execute("""
        SELECT * FROM signals ORDER BY id DESC LIMIT 1
    """).fetchone()

    conn.close()
    return signal


# =========================
# SEND TELEGRAM MESSAGE
# =========================
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })


# =========================
# BROADCAST SIGNAL
# =========================
def broadcast_signal():
    signal = get_latest_signal()

    if not signal:
        return

    message = f"""
📊 NEW SIGNAL ALERT

Asset: {signal[1]}
Entry: {signal[2]}
TP: {signal[3]}
SL: {signal[4]}
Status: {signal[5]}
"""

    users = get_active_users()

    for u in users:
        phone = u[0]

        # ⚠️ IMPORTANT:
        # In real system, phone must be mapped to telegram chat_id
        # For now we assume phone = chat_id

        send_message(phone, message)


# =========================
# LOOP (LIVE BOT ENGINE)
# =========================
if __name__ == "__main__":
    while True:
        broadcast_signal()
        sleep(60)  # every 1 minute
