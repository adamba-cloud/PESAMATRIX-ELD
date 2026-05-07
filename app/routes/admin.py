from flask import Blueprint, request, session, redirect, render_template_string, current_app
import sqlite3

admin_bp = Blueprint("admin", __name__)


# =========================
# ADMIN CHECK
# =========================
def is_admin():
    return session.get("role") == "admin"


# =========================
# ADMIN DASHBOARD
# =========================
@admin_bp.route("/admin")
def admin_home():
    if not is_admin():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]

    conn.close()

    return render_template_string(f"""
    <div style="background:#0b1220;color:white;padding:20px;font-family:Arial">

        <h1 style="color:#38bdf8">🧑‍💼 ADMIN DASHBOARD</h1>

        <div style="background:#111a2e;padding:10px;margin:10px">
            👤 Users: {users}
        </div>

        <div style="background:#111a2e;padding:10px;margin:10px">
            💳 Payments: {payments}
        </div>

        <div style="background:#111a2e;padding:10px;margin:10px">
            📊 Signals: {signals}
        </div>

        <br>

        <a href="/admin/users" style="color:#38bdf8">Manage Users</a><br>
        <a href="/admin/payments" style="color:#38bdf8">Approve Payments</a><br>
        <a href="/admin/signals" style="color:#38bdf8">Create Signals</a><br>
        <a href="/logout" style="color:red">Logout</a>

    </div>
    """)
