from flask import Blueprint, current_app, redirect, url_for
from app.utils.ui import layout
from app.utils.decorators import admin_required
import sqlite3

admin_bp = Blueprint("admin", __name__)


# =========================
# DASHBOARD
# =========================
@admin_bp.route("/admin/dashboard")
@admin_required
def dashboard():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    content = cur.execute("SELECT COUNT(*) FROM content").fetchone()[0]

    conn.close()

    return layout(f"""

    <div class="card">
        <h1>🛠 Admin Dashboard</h1>

        <div class="grid">

            <div class="stat-card">
                <h2>{users}</h2>
                <p>Users</p>
            </div>

            <div class="stat-card">
                <h2>{payments}</h2>
                <p>Payments</p>
            </div>

            <div class="stat-card">
                <h2>{signals}</h2>
                <p>Signals</p>
            </div>

            <div class="stat-card">
                <h2>{content}</h2>
                <p>Content</p>
            </div>

        </div>

    </div>

    """)


# =========================
# USERS
# =========================
@admin_bp.route("/admin/users")
@admin_required
def users():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    users = cur.execute("SELECT * FROM users ORDER BY id DESC").fetchall()

    conn.close()

    html = """
    <div class="card">
        <h2>👥 Users</h2>

        <table>
            <tr>
                <th>ID</th>
                <th>Phone</th>
                <th>Status</th>
                <th>Role</th>
            </tr>
    """

    for u in users:
        html += f"""
        <tr>
            <td>{u['id']}</td>
            <td>{u['phone']}</td>
            <td>{u['status']}</td>
            <td>{u['role']}</td>
        </tr>
        """

    html += "</table></div>"

    return layout(html)


# =========================
# PAYMENTS
# =========================
@admin_bp.route("/admin/payments")
@admin_required
def payments():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    payments = cur.execute("SELECT * FROM payments ORDER BY id DESC").fetchall()

    conn.close()

    html = """
    <div class="card">
        <h2>💳 Payments</h2>

        <table>
            <tr>
                <th>Phone</th>
                <th>Amount</th>
                <th>Code</th>
                <th>Status</th>
            </tr>
    """

    for p in payments:
        html += f"""
        <tr>
            <td>{p['phone']}</td>
            <td>{p['amount']}</td>
            <td>{p['mpesa_code']}</td>
            <td>{p['status']}</td>
        </tr>
        """

    html += "</table></div>"

    return layout(html)


# =========================
# SIGNALS
# =========================
@admin_bp.route("/admin/signals")
@admin_required
def signals():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    signals = cur.execute("SELECT * FROM signals ORDER BY id DESC").fetchall()

    conn.close()

    html = """
    <div class="card">
        <h2>📈 Trade Management</h2>
    """

    for s in signals:

        status_class = s["status"].lower()

        html += f"""
        <div class="card">

            <b>{s['asset']}</b><br>
            Entry: {s['entry']}<br>
            TP: {s['tp']}<br>
            SL: {s['sl']}<br><br>

            <span class="badge {status_class}">
                {s['status']}
            </span>

            <br><br>

            <a class="button" href="/admin/signal/{s['id']}/Upcoming">Upcoming</a>
            <a class="button" href="/admin/signal/{s['id']}/Running">Running</a>
            <a class="button" href="/admin/signal/{s['id']}/Expired">Expired</a>

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# UPDATE SIGNAL STATUS
# =========================
@admin_bp.route("/admin/signal/<int:id>/<status>")
@admin_required
def update_signal(id, status):

    allowed = ["Upcoming", "Running", "Expired"]

    if status not in allowed:
        return redirect("/admin/signals")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    cur.execute(
        "UPDATE signals SET status=? WHERE id=?",
        (status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/admin/signals")


# =========================
# CONTENT
# =========================
@admin_bp.route("/admin/content")
@admin_required
def content():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    items = cur.execute("SELECT * FROM content ORDER BY id DESC").fetchall()

    conn.close()

    html = """
    <div class="card">
        <h2>📁 Content</h2>

        <div class="grid">
    """

    for i in items:
        html += f"""
        <div class="card">
            <b>{i['title']}</b><br>
            {i['type']}<br><br>
            <a href="{i['link']}" target="_blank">Open</a>
        </div>
        """

    html += "</div></div>"

    return layout(html)
