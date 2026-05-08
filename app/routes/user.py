from flask import Blueprint, session, redirect, current_app
from app.utils.ui import layout
import sqlite3

user_bp = Blueprint("user", __name__)


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
# USER DASHBOARD
# =========================
@user_bp.route("/dashboard")
def dashboard():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    if not user:
        session.clear()
        return redirect("/login")

    status_color = "#22c55e" if user["status"] == "active" else "#ef4444"

    return layout(f"""

    <div class="card">

        <h1 style="color:#38bdf8">
            📱 USER DASHBOARD
        </h1>

        <div class="card">

            👤 Name: {user['name']}<br>
            📱 Phone: {user['phone']}<br>
            🧾 Account: {user['account_number']}<br><br>

            🔐 Status:
            <b style="color:{status_color}">
                {user['status']}
            </b>

        </div>

        <div class="grid">

            <a href="/signals">📊 Signals</a>
            <a href="/content">📁 Content</a>
            <a href="/news">📰 News</a>
            <a href="/payments/status">💳 Payments</a>

        </div>

        <br>

        <a href="/logout" style="color:#ef4444">
            🚪 Logout
        </a>

    </div>

    """)


# =========================
# SIGNALS PAGE
# =========================
@user_bp.route("/signals")
def signals_page():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT status FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    if not user:
        conn.close()
        session.clear()
        return redirect("/login")

    if user["status"] != "active":
        conn.close()
        return layout("""

        <div class="card">

            <h2 style="color:#ef4444">
                🔒 SIGNALS LOCKED
            </h2>

            <p>
                You must activate your account to access signals.
            </p>

            <a href="/payments/status">
                💳 Check Payment Status
            </a>

        </div>

        """)

    signals = cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            📊 LIVE SIGNALS
        </h2>
    """

    for s in signals:

        status_class = s["status"].lower()

        html += f"""

        <div class="card">

            <h3>📌 {s['asset']}</h3>

            💰 Entry: <b>{s['entry']}</b><br>
            🎯 TP: <b>{s['tp']}</b><br>
            🛑 SL: <b>{s['sl']}</b><br><br>

            Status:

            <span class="badge {status_class}">
                {s['status']}
            </span>

        </div>

        """

    html += "</div>"

    return layout(html)


# =========================
# PAYMENT STATUS
# =========================
@user_bp.route("/payments/status")
def payment_status():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT phone FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    if not user:
        conn.close()
        session.clear()
        return redirect("/login")

    payments = cur.execute(
        "SELECT * FROM payments WHERE phone=?",
        (user["phone"],)
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            💳 PAYMENT STATUS
        </h2>
    """

    for p in payments:

        html += f"""

        <div class="card">

            📱 Phone: {p['phone']}<br>
            💰 Amount: {p['amount']}<br>
            🧾 M-Pesa Code: {p['mpesa_code']}<br>
            📦 Plan: {p['plan']}<br><br>

            🔐 Status:
            <b>{p['status']}</b>

        </div>

        """

    html += "</div>"

    return layout(html)


# =========================
# CONTENT PAGE
# =========================
@user_bp.route("/content")
def content():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    items = cur.execute(
        "SELECT * FROM content ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            📁 CONTENT GALLERY
        </h2>

        <div class="grid">
    """

    for i in items:

        html += f"""

        <div class="card">

            🏷 {i['type']}<br>
            📌 {i['title']}<br><br>

            <a href="{i['link']}" target="_blank">
                Open
            </a>

        </div>

        """

    html += "</div></div>"

    return layout(html)


# =========================
# NEWS PAGE
# =========================
@user_bp.route("/news")
def news():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    posts = cur.execute(
        """
        SELECT * FROM content
        WHERE type='news'
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            📰 NEWS
        </h2>
    """

    for p in posts:

        html += f"""

        <div class="card">

            📰 {p['title']}<br>
            🔗 {p['link']}

        </div>

        """

    html += "</div>"

    return layout(html)
