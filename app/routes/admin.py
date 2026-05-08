from flask import Blueprint, current_app, session, redirect
import sqlite3
import secrets
from functools import wraps

from app.utils.ui import layout

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# =========================
# DB HELPER
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# ADMIN AUTH GUARD
# =========================
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if not session.get("admin_logged_in"):
            return redirect("/admin/login")

        return f(*args, **kwargs)

    return wrapper


# =========================
# ROOT
# =========================
@admin_bp.route("/")
def admin_root():
    return redirect("/admin/dashboard")


# =========================
# MODERN DASHBOARD (SAAS STYLE)
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

        <!-- STATS CARDS -->
        <div class="grid">

            <div class="card">
                <h2>👤 {users}</h2>
                <p>Users</p>
            </div>

            <div class="card">
                <h2>💳 {payments}</h2>
                <p>Payments</p>
            </div>

            <div class="card">
                <h2>📊 {signals}</h2>
                <p>Signals</p>
            </div>

            <div class="card">
                <h2>📁 {content}</h2>
                <p>Content</p>
            </div>

        </div>

        <br>

        <!-- QUICK ACTIONS -->
        <div class="card">

            <h3>⚡ Quick Actions</h3>

            <a href="/admin/users">👥 Manage Users</a><br><br>
            <a href="/admin/payments">💳 View Payments</a><br><br>
            <a href="/admin/signals">📊 Trade Signals</a><br><br>
            <a href="/admin/content">📁 Content Library</a><br><br>
            <a href="/admin/codes">🔐 Access Codes</a><br><br>

            <a href="/logout" style="color:red">Logout</a>

        </div>

    </div>

    """)


# =========================
# USERS (MODERN LIST)
# =========================
@admin_bp.route("/users")
@admin_required
def users():

    conn = get_db()
    cur = conn.cursor()

    data = cur.execute(
        "SELECT id,name,phone,email,role,status FROM users"
    ).fetchall()

    conn.close()

    rows = ""

    for u in data:
        status_color = "#22c55e" if u["status"] == "active" else "#ef4444"

        rows += f"""
        <div class="card">

            <b>👤 {u['name']}</b><br>
            📱 {u['phone']}<br>
            📧 {u['email']}<br>
            🎭 Role: {u['role']}<br>

            Status:
            <b style="color:{status_color}">
                {u['status']}
            </b>

        </div>
        """

    return layout(f"""
        <h2>👥 Users</h2>
        <div class="grid">
            {rows}
        </div>
    """)


# =========================
# PAYMENTS (MODERN CARDS)
# =========================
@admin_bp.route("/payments")
@admin_required
def payments():

    conn = get_db()
    cur = conn.cursor()

    data = cur.execute(
        "SELECT * FROM payments ORDER BY id DESC"
    ).fetchall()

    conn.close()

    rows = ""

    for p in data:

        rows += f"""
        <div class="card">

            📱 Phone: {p['phone']}<br>
            💳 Code: {p['mpesa_code']}<br>
            💰 Amount: {p['amount']}<br>
            📦 Plan: {p['plan']}<br>

            Status:
            <b>{p['status']}</b>

        </div>
        """

    return layout(f"""
        <h2>💳 Payments</h2>
        <div class="grid">
            {rows}
        </div>
    """)


# =========================
# SIGNALS
# =========================
@admin_bp.route("/signals")
@admin_required
def signals():

    conn = get_db()
    cur = conn.cursor()

    data = cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

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

    return layout(f"""
        <h2>📊 Signals</h2>
        <div class="grid">
            {rows}
        </div>
    """)


# =========================
# CONTENT
# =========================
@admin_bp.route("/content")
@admin_required
def content():

    conn = get_db()
    cur = conn.cursor()

    data = cur.execute(
        "SELECT * FROM content ORDER BY id DESC"
    ).fetchall()

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

    return layout(f"""
        <h2>📁 Content</h2>
        <div class="grid">
            {rows}
        </div>
    """)


# =========================
# ACCESS CODE GENERATION
# =========================
@admin_bp.route("/generate-code/<int:user_id>")
@admin_required
def generate_code(user_id):

    conn = get_db()
    cur = conn.cursor()

    code = secrets.token_hex(8)

    cur.execute("""
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

            <div style="background:#111;color:#0f0;padding:10px">
                {code}
            </div>

            <p>⏳ Valid for 7 days</p>

            <a href="/admin/users">Back</a>

        </div>
    """)


# =========================
# CODES LIST
# =========================
@admin_bp.route("/codes")
@admin_required
def codes():

    conn = get_db()
    cur = conn.cursor()

    data = cur.execute("""
        SELECT id,user_id,code,status,used,expires_at,created_at
        FROM access_codes
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for c in data:

        rows += f"""
        <div class="card">

            🔐 Code: <b>{c['code']}</b><br>
            User: {c['user_id']}<br>
            Status: {c['status']}<br>
            Used: {c['used']}<br>
            Expires: {c['expires_at']}<br>

        </div>
        """

    return layout(f"""
        <h2>🔐 Access Codes</h2>
        <div class="grid">
            {rows}
        </div>
    """)
