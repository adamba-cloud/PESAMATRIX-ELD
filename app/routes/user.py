from flask import Blueprint, session, redirect, render_template_string, current_app
import sqlite3

user_bp = Blueprint("user", __name__)


# =========================
# CHECK LOGIN
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

        <div style="background:#111a2e;padding:10px;margin:10px">
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
