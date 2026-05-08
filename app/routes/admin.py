from flask import Blueprint, current_app
import sqlite3
import secrets

from app.middleware.auth import admin_required
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
        <div class="card">

            <h1>🛠 ADMIN DASHBOARD</h1>

            <p>👤 Users: {users}</p>
            <p>💳 Payments: {payments}</p>
            <p>📊 Signals: {signals}</p>
            <p>📁 Content: {content}</p>

            <hr>

            <a href="/admin/users">👥 Users</a><br>
            <a href="/admin/payments">💳 Payments</a><br>
            <a href="/admin/signals">📊 Signals</a><br>
            <a href="/admin/content">📁 Content</a><br>
            <a href="/admin/codes">🔐 Access Codes</a><br><br>

            <a href="/logout" style="color:red">Logout</a>

        </div>
    """)


# =========================
# USERS
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
        rows += f"""
        <tr>
            <td>{u['id']}</td>
            <td>{u['name']}</td>
            <td>{u['phone']}</td>
            <td>{u['email']}</td>
            <td>{u['role']}</td>
            <td>{u['status']}</td>
        </tr>
        """

    return layout(f"""
        <div class="card">
            <h2>👥 USERS</h2>

            <table border="1" cellpadding="8">
                <tr>
                    <th>ID</th><th>Name</th><th>Phone</th>
                    <th>Email</th><th>Role</th><th>Status</th>
                </tr>
                {rows}
            </table>
        </div>
    """)


# =========================
# PAYMENTS
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
        <tr>
            <td>{p['id']}</td>
            <td>{p['phone']}</td>
            <td>{p['mpesa_code']}</td>
            <td>{p['amount']}</td>
            <td>{p['plan']}</td>
            <td>{p['status']}</td>
        </tr>
        """

    return layout(f"""
        <div class="card">
            <h2>💳 PAYMENTS</h2>

            <table border="1" cellpadding="8">
                <tr>
                    <th>ID</th><th>Phone</th><th>Code</th>
                    <th>Amount</th><th>Plan</th><th>Status</th>
                </tr>
                {rows}
            </table>
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
        <tr>
            <td>{s['id']}</td>
            <td>{s['asset']}</td>
            <td>{s['entry']}</td>
            <td>{s['tp']}</td>
            <td>{s['sl']}</td>
            <td>{s['status']}</td>
        </tr>
        """

    return layout(f"""
        <div class="card">
            <h2>📊 SIGNALS</h2>

            <table border="1" cellpadding="8">
                <tr>
                    <th>ID</th><th>Asset</th><th>Entry</th>
                    <th>TP</th><th>SL</th><th>Status</th>
                </tr>
                {rows}
            </table>
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
        <tr>
            <td>{c['id']}</td>
            <td>{c['type']}</td>
            <td>{c['title']}</td>
            <td>{c['link']}</td>
            <td>{c['created_at']}</td>
        </tr>
        """

    return layout(f"""
        <div class="card">
            <h2>📁 CONTENT</h2>

            <table border="1" cellpadding="8">
                <tr>
                    <th>ID</th><th>Type</th><th>Title</th>
                    <th>Link</th><th>Date</th>
                </tr>
                {rows}
            </table>
        </div>
    """)


# =========================
# ACCESS CODE GENERATION (FULL FIXED SYSTEM)
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

            <h2>🔐 CODE GENERATED</h2>

            <p>User ID: {user_id}</p>

            <div style="background:#111;color:#0f0;padding:10px">
                {code}
            </div>

            <p>⏳ Valid for 7 days</p>

            <a href="/admin/users">Back</a>

        </div>
    """)


# =========================
# ACCESS CODES LIST
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
        <tr>
            <td>{c['id']}</td>
            <td>{c['user_id']}</td>
            <td>{c['code']}</td>
            <td>{c['status']}</td>
            <td>{c['used']}</td>
            <td>{c['expires_at']}</td>
            <td>{c['created_at']}</td>
        </tr>
        """

    return layout(f"""
        <div class="card">
            <h2>🔐 ACCESS CODES</h2>

            <table border="1" cellpadding="8">
                <tr>
                    <th>ID</th><th>User</th><th>Code</th>
                    <th>Status</th><th>Used</th><th>Expiry</th><th>Date</th>
                </tr>
                {rows}
            </table>
        </div>
    """)
