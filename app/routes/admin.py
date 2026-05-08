from flask import Blueprint, session, redirect, current_app
from app.utils.ui import layout
from app.utils.security import admin_required
import sqlite3

# =========================
# BLUEPRINT
# =========================
admin_bp = Blueprint("admin", __name__)


# =========================
# ROOT ADMIN ROUTE (FIX)
# =========================
@admin_bp.route("/admin")
def admin_root():
    return redirect("/admin/dashboard")


# =========================
# ADMIN DASHBOARD
# =========================
@admin_bp.route("/admin/dashboard")
def admin_dashboard():

    if not admin_required():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]

    conn.close()

    return layout(f"""
    <div class="card">

        <h1 style="color:#38bdf8">
            🛠 Admin Dashboard
        </h1>

        <div class="card">
            👤 Users: <b>{users}</b>
        </div>

        <div class="card">
            💳 Payments: <b>{payments}</b>
        </div>

        <div class="card">
            📊 Signals: <b>{signals}</b>
        </div>

        <br>

        <div class="card">

            <a href="/admin/users" style="color:#38bdf8">
                👤 Manage Users
            </a><br><br>

            <a href="/admin/payments" style="color:#38bdf8">
                💳 Approve Payments
            </a><br><br>

            <a href="/admin/signals" style="color:#38bdf8">
                📊 Create Signals
            </a><br><br>

            <a href="/admin/content" style="color:#38bdf8">
                📁 Upload Content
            </a><br><br>

            <a href="/logout" style="color:red">
                🚪 Logout
            </a>

        </div>

    </div>
    """)
