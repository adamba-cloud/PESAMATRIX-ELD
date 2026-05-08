import sqlite3
from flask import request, current_app


# =========================
# REQUEST LOGGER
# =========================
def log_request(response):

    try:
        conn = sqlite3.connect(current_app.config["DATABASE"])
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO request_logs
            (ip, method, path, status, user_agent, referer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            request.remote_addr,
            request.method,
            request.path,
            response.status_code,
            request.headers.get("User-Agent"),
            request.referrer
        ))

        conn.commit()
        conn.close()

    except Exception as e:
        print("Logging error:", e)

    return response
