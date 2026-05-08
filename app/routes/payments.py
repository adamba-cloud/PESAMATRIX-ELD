from flask import Blueprint, request, session, redirect, current_app
from app.utils.ui import layout
import sqlite3

payments_bp = Blueprint("payments", __name__)


# =========================
# DB CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# LOGIN CHECK
# =========================
def login_required():
    return session.get("user_id") is not None


# =========================
# USER PAYMENT PAGE
# =========================
@payments_bp.route("/pay", methods=["GET", "POST"])
def pay():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    # get user (IMPORTANT: use account_number system)
    user = cur.execute(
        "SELECT phone, account_number FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    if request.method == "POST":

        cur.execute("""
            INSERT INTO payments(
                phone,
                mpesa_code,
                amount,
                plan,
                status,
                account_number
            )
            VALUES(?,?,?,?,?,?)
        """, (
            user["phone"],
            request.form["mpesa"],
            request.form["amount"],
            request.form["plan"],
            "pending",
            user["account_number"]
        ))

        conn.commit()
        conn.close()

        return layout("""
        <div class="card" style="text-align:center">

            <h2 style="color:#22c55e">
                ✔ Payment Submitted
            </h2>

            <p>
                Waiting for admin approval
            </p>

            <a href="/dashboard" style="color:#38bdf8">
                Go to Dashboard
            </a>

        </div>
        """)

    conn.close()

    return layout(f"""
    <div class="card">

        <h2 style="color:#38bdf8">
            💳 Subscription Payment
        </h2>

        <p>
            Paybill: <b>322372</b><br>
            Account: <b>{session.get("user_id")}</b>
        </p>

        <form method="POST">

            M-Pesa Code:<br>
            <input name="mpesa" required><br><br>

            Amount:<br>
            <input name="amount" required><br><br>

            Plan:<br>
            <select name="plan">
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
            </select><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                width:100%;
                border:none;
                border-radius:8px;
            ">
                Submit Payment
            </button>

        </form>

    </div>
    """)


# =========================
# USER PAYMENT STATUS
# =========================
@payments_bp.route("/payments")
def my_payments():

    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    user = cur.execute(
        "SELECT phone FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    payments = cur.execute(
        """
        SELECT * FROM payments
        WHERE phone=?
        ORDER BY id DESC
        """,
        (user["phone"],)
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            💳 My Payments
        </h2>
    """

    for p in payments:

        status_color = "#22c55e" if p["status"] == "approved" else "#f59e0b"

        html += f"""
        <div class="card">

            📱 {p['phone']}<br>
            💰 {p['amount']}<br>
            🧾 {p['mpesa_code']}<br>
            📦 {p['plan']}<br><br>

            Status:
            <b style="color:{status_color}">
                {p['status']}
            </b>

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# ADMIN VIEW PAYMENTS
# =========================
@payments_bp.route("/admin/payments")
def admin_payments():

    if session.get("role") != "admin":
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    payments = cur.execute(
        """
        SELECT * FROM payments
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h2 style="color:#38bdf8">
            💳 Admin Payments
        </h2>
    """

    for p in payments:

        html += f"""
        <div class="card">

            Phone: {p['phone']}<br>
            Amount: {p['amount']}<br>
            Mpesa: {p['mpesa_code']}<br>
            Plan: {p['plan']}<br>
            Account: {p.get('account_number','-')}<br>
            Status: <b>{p['status']}</b><br><br>

            <form method="POST"
                  action="/admin/approve-payment">

                <input type="hidden"
                       name="payment_id"
                       value="{p['id']}">

                <input type="hidden"
                       name="account_number"
                       value="{p.get('account_number','')}">

                <button style="
                    background:#22c55e;
                    color:black;
                    padding:8px;
                    border:none;
                    border-radius:6px;
                ">
                    Approve
                </button>

            </form>

        </div>
        """

    html += "</div>"

    return layout(html)


# =========================
# ADMIN APPROVE PAYMENT (SAFE VERSION)
# =========================
@payments_bp.route("/admin/approve-payment", methods=["POST"])
def approve_payment():

    if session.get("role") != "admin":
        return redirect("/login")

    payment_id = request.form["payment_id"]
    account_number = request.form["account_number"]

    conn = get_db()
    cur = conn.cursor()

    # approve payment
    cur.execute(
        """
        UPDATE payments
        SET status='approved'
        WHERE id=?
        """,
        (payment_id,)
    )

    # activate user using account number (SAFE WAY)
    cur.execute(
        """
        UPDATE users
        SET status='active'
        WHERE account_number=?
        """,
        (account_number,)
    )

    conn.commit()
    conn.close()

    return redirect("/admin/payments")
