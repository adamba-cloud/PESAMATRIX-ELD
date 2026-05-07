from flask import Blueprint, request, session, redirect, current_app
from app.utils.ui import layout
import sqlite3

payments_bp = Blueprint("payments", __name__)


# =========================
# LOGIN CHECK
# =========================
def login_required():
    return session.get("user_id") is not None


# =========================
# DATABASE CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# USER: MAKE PAYMENT PAGE
# =========================
@payments_bp.route("/subscribe", methods=["GET", "POST"])
def subscribe():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":

        cur.execute("""
        INSERT INTO payments(phone, mpesa_code, amount, plan, status)
        VALUES(?,?,?,?,?)
        """, (
            request.form["phone"],
            request.form["mpesa_code"],
            request.form["amount"],
            request.form["plan"],
            "pending"
        ))

        conn.commit()
        conn.close()

        return layout("""
        <div class="card">

            <h2 style="color:green">
                ✅ Payment Submitted
            </h2>

            <p>Waiting for admin approval.</p>

            <a href="/dashboard" style="color:#38bdf8">
                Go to Dashboard
            </a>

        </div>
        """)

    conn.close()

    return layout("""
    <div class="card">

        <h1 style="color:#38bdf8">
            💳 SUBSCRIBE
        </h1>

        <form method="POST">

            Phone:<br>
            <input name="phone" required><br><br>

            M-Pesa Code:<br>
            <input name="mpesa_code" required><br><br>

            Amount:<br>
            <input name="amount" required><br><br>

            Plan:<br>
            <select name="plan">
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
            </select><br><br>

            <button>Submit Payment</button>

        </form>

        <br>

        <p>Paybill: <b>322372</b></p>
        <p>Account: <b>Your Account Number</b></p>

    </div>
    """)


# =========================
# USER: PAYMENT STATUS
# =========================
@payments_bp.route("/payments/status")
def payment_status():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT phone FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    payments = cur.execute(
        "SELECT * FROM payments WHERE phone=? ORDER BY id DESC",
        (user["phone"],)
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h1 style="color:#38bdf8">
            💳 PAYMENT STATUS
        </h1>
    """

    for p in payments:

        html += f"""
        <div class="card">

            📱 {p['phone']}<br>
            💰 {p['amount']}<br>
            🧾 {p['mpesa_code']}<br>
            📦 {p['plan']}<br>
            🔐 {p['status']}

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# ADMIN: VIEW PAYMENTS
# =========================
@payments_bp.route("/admin/payments")
def admin_payments():

    if session.get("role") != "admin":
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    payments = cur.execute(
        "SELECT * FROM payments ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h1 style="color:#38bdf8">
            💳 PAYMENT APPROVAL
        </h1>
    """

    for p in payments:

        html += f"""
        <div class="card">

            Phone: {p['phone']}<br>
            Amount: {p['amount']}<br>
            Mpesa: {p['mpesa_code']}<br>
            Plan: {p['plan']}<br>
            Status: {p['status']}<br><br>

            <form method="POST" action="/admin/approve-payment">

                <input
                    type="hidden"
                    name="phone"
                    value="{p['phone']}"
                >

                <button>
                    Approve
                </button>

            </form>

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# ADMIN: APPROVE PAYMENT
# =========================
@payments_bp.route("/admin/approve-payment", methods=["POST"])
def approve_payment():

    if session.get("role") != "admin":
        return redirect("/login")

    phone = request.form["phone"]

    conn = get_db()
    cur = conn.cursor()

    # approve payment
    cur.execute(
        "UPDATE payments SET status='approved' WHERE phone=?",
        (phone,)
    )

    # activate user
