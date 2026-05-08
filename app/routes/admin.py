from flask import Blueprint, current_app, redirect, render_template, session
import sqlite3
import secrets

from app.utils.ui import layout
from app.utils.decorators import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# =========================
# DB HELPER
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# ROOT (OLD - REDIRECT)
# =========================
@admin_bp.route("/")
def admin_root():
    return redirect("/admin/dashboard")


# =========================
# NEW ROOT TEST (DEBUG)
# =========================
@admin_bp.route("/test")
def admin_test():
    return "ADMIN WORKS"


# =========================
# DASHBOARD
# =========================
@admin_bp.route("/dashboard")
@admin_required
def dashboard():

    conn = get_db()
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    content = cur.execute("SELECT COUNT(*) FROM content").fetchone()[0]

    conn.close()

    return layout(f"""
    <div style="padding:20px">

        <h1 style="color:#38bdf8">🛠 Admin Dashboard</h1>

        <div class="grid">

            <div class="card"><h2>👤 {users}</h2><p>Users</p></div>
            <div class="card"><h2>💳 {payments}</h2><p>Payments</p></div>
            <div class="card"><h2>📊 {signals}</h2><p>Signals</p></div>
            <div class="card"><h2>📁 {content}</h2><p>Content</p></div>

        </div>

        <br>

        <div class="card">
            <h3>⚡ Quick Actions</h3>

            <a href="/admin/users">👥 Manage Users</a><br><br>
            <a href="/admin/payments">💳 View Payments</a><br><br>
            <a href="/admin/signals">📊 Trade Signals</a><br><br>
            <a href="/admin/content">📁 Content Library</a><br><br>
            <a href="/admin/codes">🔐 Access Codes</a><br><br>
            <a href="/admin/logs">📡 System Logs</a><br><br>
            <a href="/logout" style="color:red">Logout</a>

        </div>

    </div>
    """)


# =========================
# LOGS ANALYTICS DASHBOARD
# =========================
@admin_bp.route("/logs")
@admin_required
def logs_dashboard():

    conn = get_db()

    logs = conn.execute("""
        SELECT *
        FROM request_logs
        ORDER BY timestamp DESC
        LIMIT 200
    """).fetchall()

    stats = {
        "total": conn.execute("SELECT COUNT(*) FROM request_logs").fetchone()[0],
        "signals_hits": conn.execute(
            "SELECT COUNT(*) FROM request_logs WHERE path='/signals'"
        ).fetchone()[0],
        "payments_hits": conn.execute(
            "SELECT COUNT(*) FROM request_logs WHERE path='/payments/status'"
        ).fetchone()[0],
    }

    conn.close()

    return render_template("admin_logs.html", logs=logs, stats=stats)


# =========================
# USERS
# =========================
@admin_bp.route("/users")
@admin_required
def users():

    conn = get_db()
    data = conn.execute("""
        SELECT id, name, phone, email, role, status
        FROM users
    """).fetchall()
    conn.close()

    rows = ""

    for u in data:

        color = "#22c55e" if u["status"] == "active" else "#ef4444"

        rows += f"""
        <div class="card">
            <b>👤 {u['name']}</b><br>
            📱 {u['phone']}<br>
            📧 {u['email']}<br>
            🎭 Role: {u['role']}<br>
            Status: <b style="color:{color}">{u['status']}</b>
        </div>
        """

    return layout(f"<h2>👥 Users</h2><div class='grid'>{rows}</div>")


# =========================
# PAYMENTS
# =========================
@admin_bp.route("/payments")
@admin_required
def payments():

    conn = get_db()
    data = conn.execute("SELECT * FROM payments ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for p in data:
        rows += f"""
        <div class="card">
            📱 {p['phone']}<br>
            💳 {p['mpesa_code']}<br>
            💰 {p['amount']}<br>
            📦 {p['plan
