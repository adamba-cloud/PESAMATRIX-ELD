from flask import Blueprint, session, redirect, current_app
from app.utils.ui import layout
import sqlite3

user_bp = Blueprint("user", __name__)


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

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    user = cur.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    status_color = "green" if user["status"] == "active" else "red"

    return layout(f"""
    <div class="card">

        <h1 style="color:#38bdf8">
            📱 USER DASHBOARD
        </h1>

        <div class="card">

            👤 Name: {user['name']}<br>
            📱 Phone: {user['phone']}<br>
            🧾 Account: {user['account_number']}<br>

            🔐 Status:
            <span style="color:{status_color}">
                {user['status']}
            </span>

        </div>

        <br>

        <a href="/signals" style="color:#38bdf8">
            📊 View Signals
        </a><br><br>

        <a href="/content" style="color:#38bdf8">
            📁 Content Gallery
        </a><br><br>

        <a href="/news" style="color:#38bdf8">
            📰 News
        </a><br><br>

        <a href="/payments/status" style="color:#38bdf8">
            💳 Payment Status
        </a><br><br>

        <a href="/logout" style="color:red">
            Logout
        </a>

    </div>
    """)


# =========================
# SIGNALS (LOCKED SYSTEM)
# =========================
@user_bp.route("/signals")
def signals():

    if not login_required():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    user = cur.execute(
        "SELECT status FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    # 🔒 LOCKED ACCESS
    if user["status"] != "active":

        conn.close()

        return layout("""
        <div class="card">

            <h2 style="color:#ff4d4d">
                🔒 SIGNALS LOCKED
            </h2>

            <p>
                You must subscribe to access trading signals.
            </p>

            <a href="/payments/status"
               style="color:#38bdf8">
               Check Payment Status
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

        html += f"""
        <div class="card">

            📌 Asset: {s['asset']}<br>
            💰 Entry: {s['entry']}<br>
            🎯 TP: {s['tp']}<br>
            🛑 SL: {s['sl']}<br>
            📡 Status: {s['status']}

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

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    user = cur.execute(
        "SELECT phone FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

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
            🧾 M-Pesa: {p['mpesa_code']}<br>
            📦 Plan: {p['plan']}<br>
            🔐 Status: {p['status']}

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# CONTENT GALLERY
# =========================
@user_bp.route("/content")
def content():

    if not login_required():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
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
    """

    for i in items:

        html += f"""
        <div class="card">

            🏷 Type: {i['type']}<br>
            📌 Title: {i['title']}<br><br>

            <a href="{i['link']}"
               target="_blank"
               style="color:#38bdf8">
               Open Content
            </a>

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# NEWS SYSTEM
# =========================
@user_bp.route("/news")
def news():

    if not login_required():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    posts = cur.execute(
        "SELECT * FROM content WHERE type='news' ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            📰 LATEST NEWS
        </h2>
    """

    for p in posts:

        html += f"""
        <div class="card">

            📰 Title: {p['title']}<br>
            📄 Content: {p['link']}

        </div>
        """

    html += "</div>"

    return layout(html)
