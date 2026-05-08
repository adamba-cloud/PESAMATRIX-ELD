import sqlite3
import secrets
from flask import Blueprint, current_app
from app.utils.ui import layout
from app.middleware.auth import admin_required

admin_bp = Blueprint("admin", __name__)


# =========================
# ADMIN DASHBOARD
# =========================
@admin_bp.route("/admin/dashboard")
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

        <h1 style="color:#38bdf8">🛠 SaaS Admin Panel</h1>

        <div class="grid">

            <div class="stat-card">
                <h2>{users}</h2>
                <p>👤 Users</p>
            </div>

            <div class="stat-card">
                <h2>{payments}</h2>
                <p>💳 Payments</p>
            </div>

            <div class="stat-card">
                <h2>{signals}</h2>
                <p>📊 Signals</p>
            </div>

            <div class="stat-card">
                <h2>{content}</h2>
                <p>📁 Content</p>
            </div>

        </div>

        <br><br>

        <div class="card">
            <h3>⚡ Quick Actions</h3>

            <a href="/admin/users">👥 Manage Users</a><br><br>
            <a href="/admin/payments">💳 Payments</a><br><br>
            <a href="/admin/signals">📊 Trades</a><br><br>
            <a href="/admin/content">📁 Media</a><br><br>
            <a href="/admin/codes">🔐 Access Codes</a><br><br>

            <a href="/logout" style="color:red">Logout</a>
        </div>

    </div>

    """)


# =========================
# CODE GENERATION SYSTEM
# =========================
@admin_bp.route("/admin/generate-code/<int:user_id>")
@admin_required
def generate_code(user_id):

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    # generate secure secret code
    secret_code = secrets.token_hex(8)  # e.g. a1b2c3d4e5f6

    # store in database
    cur.execute("""
        INSERT INTO access_codes (user_id, code, status)
        VALUES (?, ?, ?)
    """, (user_id, secret_code, "active"))

    conn.commit()
    conn.close()

    return layout(f"""
        <div style="padding:20px">
            <h2>🔐 Access Code Generated</h2>

            <p>User ID: <b>{user_id}</b></p>

            <div style="background:#111;color:#0f0;padding:10px;border-radius:5px">
                {secret_code}
            </div>

            <br>
            <a href="/admin/dashboard">⬅ Back to Dashboard</a>
        </div>
    """)


# =========================
# VIEW ALL CODES
# =========================
@admin_bp.route("/admin/codes")
@admin_required
def view_codes():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    codes = cur.execute("""
        SELECT id, user_id, code, status, created_at
        FROM access_codes
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for c in codes:
        rows += f"""
        <tr>
            <td>{c[0]}</td>
            <td>{c[1]}</td>
            <td style="color:#38bdf8">{c[2]}</td>
            <td>{c[3]}</td>
            <td>{c[4]}</td>
        </tr>
        """

    return layout(f"""
    <div style="padding:20px">

        <h2>🔐 Generated Access Codes</h2>

        <table border="1" cellpadding="10" style="width:100%;color:white">
            <tr>
                <th>ID</th>
                <th>User</th>
                <th>Code</th>
                <th>Status</th>
                <th>Date</th>
            </tr>

            {rows}
        </table>

    </div>
    """)
