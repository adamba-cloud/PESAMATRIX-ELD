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

        <div style="background:#111a2e;padding:10px;margin:10px;border-radius:8px">
            👤 Users: {users}
        </div>

        <div style="background:#111a2e;padding:10px;margin:10px;border-radius:8px">
            💳 Payments: {payments}
        </div>

        <div style="background:#111a2e;padding:10px;margin:10px;border-radius:8px">
            📊 Signals: {signals}
        </div>

        <br>

        <a href="/admin/users" style="color:#38bdf8">Manage Users</a><br>
        <a href="/admin/payments" style="color:#38bdf8">Approve Payments</a><br>
        <a href="/admin/signals" style="color:#38bdf8">Create Signals</a><br>
        <a href="/logout" style="color:red">Logout</a>

    </div>
    """)


# =========================
# USERS MANAGEMENT
# =========================
@admin_bp.route("/admin/users")
def users():
    if not is_admin():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    users = cur.execute("SELECT * FROM users").fetchall()
    conn.close()

    html = "<h2>👤 USERS</h2>"

    for u in users:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">
            Name: {u['name']}<br>
            Phone: {u['phone']}<br>
            Role: {u['role']}<br>
            Status: {u['status']}<br>
            Account: {u['account_number']}
        </div>
        """

    return html


# =========================
# PAYMENTS LIST
# =========================
@admin_bp.route("/admin/payments")
def payments():
    if not is_admin():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    payments = cur.execute("SELECT * FROM payments").fetchall()
    conn.close()

    html = "<h2>💳 PAYMENT APPROVAL</h2>"

    for p in payments:
        html += f"""
        <div style="background:#111a2e;color:white;padding:10px;margin:10px;border-radius:8px">

            Phone: {p['phone']}<br>
            Amount: {p['amount']}<br>
            Mpesa Code: {p['mpesa_code']}<br>
            Plan: {p['plan']}<br>
            Status: {p['status']}<br>

            <form method="POST" action="/admin/approve_payment">
                <input type="hidden" name="phone" value="{p['phone']}">
                <button style="background:#22c55e;color:black;padding:5px;margin-top:5px">
                    Approve Payment
                </button>
            </form>

        </div>
        """

    return html


# =========================
# APPROVE PAYMENT (AUTO ACTIVATE USER)
# =========================
@admin_bp.route("/admin/approve_payment", methods=["POST"])
def approve_payment():
    if not is_admin():
        return redirect("/login")

    phone = request.form["phone"]

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    # approve payment
    cur.execute("UPDATE payments SET status='approved' WHERE phone=?", (phone,))

    # activate user (ENTERPRISE LOGIC)
    cur.execute("UPDATE users SET status='active' WHERE phone=?", (phone,))

    conn.commit()
    conn.close()

    return redirect("/admin/payments")


# =========================
# CREATE SIGNALS
# =========================
@admin_bp.route("/admin/signals", methods=["GET", "POST"])
def signals():
    if not is_admin():
        return redirect("/login")

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    if request.method == "POST":
        cur.execute("""
            INSERT INTO signals(asset, entry, tp, sl, status)
            VALUES(?,?,?,?,?)
        """, (
            request.form["asset"],
            request.form["entry"],
            request.form["tp"],
            request.form["sl"],
            "ACTIVE"
        ))

        conn.commit()

    conn.close()

    return render_template_string("""
    <div style="background:#0b1220;color:white;padding:20px;font-family:Arial">

        <h2 style="color:#38bdf8">📊 CREATE SIGNAL</h2>

        <form method="POST">
            Asset:<br><input name="asset"><br><br>
            Entry:<br><input name="entry"><br><br>
            TP:<br><input name="tp"><br><br>
            SL:<br><input name="sl"><br><br>

            <button style="background:#38bdf8;padding:8px">Create Signal</button>
        </form>

    </div>
    """)
