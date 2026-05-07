from flask import Blueprint, session, redirect, render_template_string, current_app
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

    return render_template_string(f"""
    <div style="background:#0b1220;color:white;font-family:Arial;padding:20px">

        <h1 style="color:#38bdf8">📱 USER DASHBOARD</h1>

        <div style="background:#111a2e;padding:10px;margin:10px;border-radius:8px">
            👤 Name: {user['name']}<br>
            📱 Phone: {user['phone']}<br>
            🧾 Account: {user['account_number']}<br>
            🔐 Status:
            <span style="color:{status_color}">{user['status']}</span>
        </div>

        <br>

        <a href="/signals" style="color:#38bdf8">📊 View Signals</a><br>
        <a href="/content" style="color:#38bdf8">📁 Content Gallery</a><br>
        <a href="/news" style="color:#38bdf8">📰 News</a><br>
        <a href="/payments/status" style="color:#38bdf8">💳 Payment Status</a><br>
        <a href="/logout" style="color:red">Logout</a>

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
        return render_template_string("""
        <div style="background:#0b1220;color:white;padding:20px;font-family:Arial">
            <h2>🔒 SIGNALS LOCKED</h2>
            <p>You must subscribe to access trading signals.</p>
            <a href="/payments/status" style="color:#38bdf8">Check Payment Status</a>
        </div>
        """)

    signals = cur.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()
    conn.close()

    html = "<h2 style='color:#38bdf8'>📊 LIVE SIGNALS</h2>"

    for s in signals:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">
            📌 Asset: {s['asset']}<br>
            💰 Entry: {s['entry']}<br>
            🎯 TP: {s['tp']}<br>
            🛑 SL: {s['sl']}<br>
            📡 Status: {s['status']}
        </div>
        """

    return html


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

    html = "<h2 style='color:#38bdf8'>💳 PAYMENT STATUS</h2>"

    for p in payments:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">
            📱 Phone: {p['phone']}<br>
            💰 Amount: {p['amount']}<br>
            🧾 M-Pesa: {p['mpesa_code']}<br>
            📦 Plan: {p['plan']}<br>
            🔐 Status: {p['status']}
        </div>
        """

    return html


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

    html = "<h2 style='color:#38bdf8'>📁 CONTENT GALLERY</h2>"

    for i in items:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">

            🏷 Type: {i['type']}<br>
            📌 Title: {i['title']}<br>

            <a href="{i['link']}" target="_blank" style="color:#38bdf8">
                Open Content
            </a>

        </div>
        """

    return html


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

    html = "<h2 style='color:#38bdf8'>📰 LATEST NEWS</h2>"

    for p in posts:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">
            📰 Title: {p['title']}<br>
            📄 Content: {p['link']}
        </div>
        """

    return html
