from flask import Blueprint, session, redirect, current_app
from app.utils.ui import layout
import sqlite3

signals_bp = Blueprint("signals", __name__)


# =========================
# DB HELPER
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# LOGIN CHECK
# =========================
def login_required():
    return session.get("user_id") is not None


# =========================
# USER SIGNALS (LOCKED SYSTEM)
# =========================
@signals_bp.route("/signals")
def view_signals():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT status FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    # =========================
    # 🔒 LOCK CHECK
    # =========================
    if not user or user["status"] != "active":
        conn.close()

        return layout("""

        <div class="card" style="text-align:center">

            <h1 style="color:#ef4444">
                🔒 SIGNALS LOCKED
            </h1>

            <p>
                Access is only available after payment confirmation.
            </p>

            <p>
                Pay via <b>Lipa Na M-Pesa</b><br>
                Paybill: <b>322372</b><br>
                Account: <b>Your registration account number</b>
            </p>

            <br>

            <a href="/payments/status"
               style="
                background:#38bdf8;
                color:black;
                padding:10px 18px;
                text-decoration:none;
                border-radius:8px;
                font-weight:bold;
               ">
               💳 Check Payment Status
            </a>

        </div>

        """)

    # =========================
    # LIVE SIGNALS
    # =========================
    signals = cur.execute(
        """
        SELECT * FROM signals
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h1 style="color:#38bdf8">
            📊 LIVE TRADING SIGNALS
        </h1>
    """

    for s in signals:

        status_class = s["status"].lower()

        html += f"""

        <div class="card">

            📌 Asset: <b>{s['asset']}</b><br>
            💰 Entry: {s['entry']}<br>
            🎯 TP: {s['tp']}<br>
            🛑 SL: {s['sl']}<br><br>

            Status:

            <span class="badge {status_class}">
                {s['status']}
            </span>

        </div>

        """

    html += "</div>"

    return layout(html)
