from flask import Blueprint, session, redirect, current_app
from functools import wraps
import sqlite3
from app.utils.ui import layout

user_bp = Blueprint("user", __name__)


# =========================
# DB HELPER
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# FIXED LOGIN GUARD (UPDATED)
# =========================
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if not session.get("user_id"):
            return redirect("/login")

        return f(*args, **kwargs)

    return wrapper


# =========================
# DASHBOARD
# =========================
@user_bp.route("/dashboard")
@login_required
def dashboard():

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

            <h1>👤 USER DASHBOARD</h1>

            <p>Name: {user['name']}</p>
            <p>Phone: {user['phone']}</p>
            <p>Account: {user['account_number']}</p>

            <p>
                Status:
                <b style="color:{status_color}">
                    {user['status']}
                </b>
            </p>

            <hr>

            <a href="/signals">📊 Signals</a><br>
            <a href="/content">📁 Content</a><br>
            <a href="/news">📰 News</a><br>
            <a href="/payments/status">💳 Payments</a><br><br>

            <a href="/logout" style="color:red">Logout</a>

        </div>
    """)


# =========================
# SIGNALS (LOCK SYSTEM FIXED)
# =========================
@user_bp.route("/signals")
@login_required
def signals():

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

    # LOCK SYSTEM
    if user["status"] != "active":
        conn.close()
        return layout("""
            <div class="card">

                <h2>🔒 SIGNALS LOCKED</h2>

                <p>Activate account to access signals.</p>

                <a href="/payments/status">Check Payment</a>

            </div>
        """)

    signals = cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = "<div class='card'><h2>📊 LIVE SIGNALS</h2>"

    for s in signals:
        html += f"""
        <div class="card">
            <h3>{s['asset']}</h3>
            Entry: {s['entry']}<br>
            TP: {s['tp']}<br>
            SL: {s['sl']}<br>
            Status: {s['status']}
        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# PAYMENT STATUS
# =========================
@user_bp.route("/payments/status")
@login_required
def payments():

    conn = get_db()
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

    html = "<div class='card'><h2>💳 PAYMENT STATUS</h2>"

    for p in payments:
        html += f"""
        <div class="card">
            Phone: {p['phone']}<br>
            Amount: {p['amount']}<br>
            Code: {p['mpesa_code']}<br>
            Plan: {p['plan']}<br>
            Status: {p['status']}
        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# CONTENT
# =========================
@user_bp.route("/content")
@login_required
def content():

    conn = get_db()
    cur = conn.cursor()

    items = cur.execute(
        "SELECT * FROM content ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = "<div class='card'><h2>📁 CONTENT</h2>"

    for i in items:
        html += f"""
        <div class="card">
            {i['type']}<br>
            {i['title']}<br>
            <a href="{i['link']}" target="_blank">Open</a>
        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# NEWS
# =========================
@user_bp.route("/news")
@login_required
def news():

    conn = get_db()
    cur = conn.cursor()

    posts = cur.execute(
        "SELECT * FROM content WHERE type='news'"
    ).fetchall()

    conn.close()

    html = "<div class='card'><h2>📰 NEWS</h2>"

    for p in posts:
        html += f"""
        <div class="card">
            {p['title']}<br>
            {p['link']}
        </div>
        """

    html += "</div>"

    return layout(html)
