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
# ROOT
# =========================
@admin_bp.route("/")
def admin_root():
    return redirect("/admin/dashboard")


# =========================
# TEST ROUTE
# =========================
@admin_bp.route("/test")
def admin_test():
    return "ADMIN WORKS"


# =========================
# SESSION DEBUG ROUTE
# =========================
@admin_bp.route("/test-session")
def test_session():
    return str(dict(session))


# =========================
# DASHBOARD (SESSION DEBUG VERSION)
# =========================
@admin_bp.route("/dashboard")
def dashboard():
    return str(dict(session))


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
            📦 {p['plan']}<br>
            Status: <b>{p['status']}</b>
        </div>
        """

    return layout(f"<h2>💳 Payments</h2><div class='grid'>{rows}</div>")


# =========================
# SIGNALS
# =========================
@admin_bp.route("/signals")
@admin_required
def signals():

    conn = get_db()
    data = conn.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for s in data:
        rows += f"""
        <div class="card">
            📊 <b>{s['asset']}</b><br><br>
            Entry: {s['entry']}<br>
            TP: {s['tp']}<br>
            SL: {s['sl']}<br>
            Status: {s['status']}
        </div>
        """

    return layout(f"<h2>📊 Signals</h2><div class='grid'>{rows}</div>")


# =========================
# CONTENT
# =========================
@admin_bp.route("/content")
@admin_required
def content():

    conn = get_db()
    data = conn.execute("SELECT * FROM content ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for c in data:
        rows += f"""
        <div class="card">
            📁 {c['type']}<br>
            <b>{c['title']}</b><br><br>
            <a href="{c['link']}" target="_blank">Open</a>
        </div>
        """

    return layout(f"<h2>📁 Content</h2><div class='grid'>{rows}</div>")


# =========================
# ACCESS CODE GENERATOR
# =========================
@admin_bp.route("/generate-code/<int:user_id>")
@admin_required
def generate_code(user_id):

    conn = get_db()
    code = secrets.token_hex(8)

    conn.execute("""
        INSERT INTO access_codes
        (user_id, code, status, used, expires_at)
        VALUES (?, ?, ?, ?, datetime('now', '+7 days'))
    """, (user_id, code, "active", 0))

    conn.commit()
    conn.close()

    return layout(f"""
    <div class="card">
        <h2>🔐 Code Generated</h2>
        <p>User ID: {user_id}</p>

        <div style="background:#111;color:#0f0;padding:10px;">
            {code}
        </div>

        <p>⏳ Valid for 7 days</p>

        <a href="/admin/users">Back</a>
    </div>
    """)


# =========================
# ACCESS CODES
# =========================
@admin_bp.route("/codes")
@admin_required
def codes():

    conn = get_db()
    data = conn.execute("""
        SELECT id, user_id, code, status, used, expires_at, created_at
        FROM access_codes
        ORDER BY id DESC
    """).fetchall()
    conn.close()

    rows = ""

    for c in data:
        rows += f"""
        <div class="card">
            🔐 <b>{c['code']}</b><br>
            User: {c['user_id']}<br>
            Status: {c['status']}<br>
            Used: {c['used']}<br>
            Expires: {c['expires_at']}<br>
        </div>
        """

    return layout(f"<h2>🔐 Access Codes</h2><div class='grid'>{rows}</div>")
