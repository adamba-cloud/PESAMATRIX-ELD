import sqlite3
import secrets
from flask import Blueprint, current_app
from app.utils.ui import layout
from app.middleware.auth import admin_required


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# =========================
# DASHBOARD
# =========================
@admin_bp.route("/dashboard")
@admin_required
def admin_dashboard():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    content = cur.execute("SELECT COUNT(*) FROM content").fetchone()[0]

    conn.close()

    return layout(f"""
    <div style="padding:20px">
        <h1>🛠 SaaS Admin Panel</h1>

        <div>
            <p>👤 Users: {users}</p>
            <p>💳 Payments: {payments}</p>
            <p>📊 Signals: {signals}</p>
            <p>📁 Content: {content}</p>
        </div>

        <hr>

        <a href="/admin/users">Users</a><br>
        <a href="/admin/payments">Payments</a><br>
        <a href="/admin/signals">Signals</a><br>
        <a href="/admin/content">Content</a><br>
        <a href="/admin/codes">Access Codes</a><br>

        <a href="/logout" style="color:red">Logout</a>
    </div>
    """)


# =========================
# USERS
# =========================
@admin_bp.route("/users")
@admin_required
def users():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    data = cur.execute("SELECT id,name,phone,email,role,status FROM users").fetchall()
    conn.close()

    rows = ""

    for u in data:
        rows += f"<tr><td>{u[0]}</td><td>{u[1]}</td><td>{u[2]}</td><td>{u[3]}</td><td>{u[4]}</td><td>{u[5]}</td></tr>"

    return layout(f"""
    <h2>👥 Users</h2>
    <table border="1" cellpadding="10">
        <tr><th>ID</th><th>Name</th><th>Phone</th><th>Email</th><th>Role</th><th>Status</th></tr>
        {rows}
    </table>
    """)


# =========================
# PAYMENTS
# =========================
@admin_bp.route("/payments")
@admin_required
def payments():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    data = cur.execute("SELECT * FROM payments ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for p in data:
        rows += f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td><td>{p[4]}</td><td>{p[5]}</td></tr>"

    return layout(f"""
    <h2>💳 Payments</h2>
    <table border="1" cellpadding="10">
        <tr><th>ID</th><th>Phone</th><th>Code</th><th>Amount</th><th>Plan</th><th>Status</th></tr>
        {rows}
    </table>
    """)


# =========================
# SIGNALS
# =========================
@admin_bp.route("/signals")
@admin_required
def signals():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    data = cur.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for s in data:
        rows += f"<tr><td>{s[0]}</td><td>{s[1]}</td><td>{s[2]}</td><td>{s[3]}</td><td>{s[4]}</td><td>{s[5]}</td></tr>"

    return layout(f"""
    <h2>📊 Signals</h2>
    <table border="1" cellpadding="10">
        <tr><th>ID</th><th>Asset</th><th>Entry</th><th>TP</th><th>SL</th><th>Status</th></tr>
        {rows}
    </table>
    """)


# =========================
# CONTENT
# =========================
@admin_bp.route("/content")
@admin_required
def content():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    data = cur.execute("SELECT * FROM content ORDER BY id DESC").fetchall()
    conn.close()

    rows = ""

    for c in data:
        rows += f"<tr><td>{c[0]}</td><td>{c[1]}</td><td>{c[2]}</td><td>{c[3]}</td><td>{c[4]}</td></tr>"

    return layout(f"""
    <h2>📁 Content</h2>
    <table border="1" cellpadding="10">
        <tr><th>ID</th><th>Type</th><th>Title</th><th>Link</th><th>Date</th></tr>
        {rows}
    </table>
    """)


# =========================
# CODE GENERATION SYSTEM
# =========================
@admin_bp.route("/generate-code/<int:user_id>")
@admin_required
def generate_code(user_id):

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    # 🔐 generate secure code
    code = secrets.token_hex(8)

    # expiry (7 days default)
    cur.execute("""
        INSERT INTO access_codes
        (user_id, code, status, used, expires_at)
        VALUES (?, ?, ?, ?, datetime('now', '+7 days'))
    """, (user_id, code, "active", 0))

    conn.commit()
    conn.close()

    return layout(f"""
    <div style="padding:20px">
        <h2>🔐 ACCESS CODE GENERATED</h2>

        <p>User ID: {user_id}</p>

        <div style="background:#111;color:#0f0;padding:10px">
            {code}
        </div>

        <p>⏳ Expires in 7 days</p>

        <a href="/admin/users">Back</a>
    </div>
    """)


# =========================
# VIEW CODES
# =========================
@admin_bp.route("/codes")
@admin_required
def codes():

    conn = sqlite3.connect(current_app.config["DATABASE"])
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
        <tr>
            <td>{c[0]}</td>
            <td>{c[1]}</td>
            <td>{c[2]}</td>
            <td>{c[3]}</td>
            <td>{c[4]}</td>
            <td>{c[5]}</td>
            <td>{c[6]}</td>
        </tr>
        """

    return layout(f"""
    <h2>🔐 Access Codes</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th><th>User</th><th>Code</th>
            <th>Status</th><th>Used</th><th>Expires</th><th>Date</th>
        </tr>
        {rows}
    </table>
    """)
