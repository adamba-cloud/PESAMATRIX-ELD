import sqlite3
import random

from flask import (
    Blueprint,
    request,
    session,
    redirect,
    current_app
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.utils.ui import layout
from app.utils.decorators import login_required

# ====================================================
# BLUEPRINT
# ====================================================
auth_bp = Blueprint("auth", __name__)


# ====================================================
# REGISTER
# ====================================================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name or not phone or not email or not password:
            return layout("<div class='card' style='color:red'>❌ All fields are required</div>")

        conn = sqlite3.connect(current_app.config["DATABASE"])
        cur = conn.cursor()

        try:
            account_number = "ACC" + str(random.randint(100000, 999999))

            cur.execute("""
                INSERT INTO users (
                    name, phone, email, password,
                    account_number, role, status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                phone,
                email,
                generate_password_hash(password),
                account_number,
                "user",
                "inactive"
            ))

            conn.commit()

        except Exception as e:
            conn.close()
            return layout(f"<div class='card' style='color:red'>❌ {str(e)}</div>")

        conn.close()

        return layout(f"""
            <div class="card" style="text-align:center">
                <h2 style="color:#22c55e">Account Created ✔</h2>
                <p>Your Account Number:</p>
                <h3 style="color:#38bdf8">{account_number}</h3>
                <a href="/login">Go to Login</a>
            </div>
        """)

    return layout("""
        <div class="card">
            <h2>Register</h2>
            <form method="POST">
                <input name="name" placeholder="Full Name"><br><br>
                <input name="phone" placeholder="Phone"><br><br>
                <input name="email" placeholder="Email"><br><br>
                <input type="password" name="password" placeholder="Password"><br><br>
                <button style="background:#38bdf8;width:100%;padding:10px">
                    Register
                </button>
            </form>
        </div>
    """)


# ====================================================
# LOGIN
# ====================================================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "").strip()

        if not phone or not password:
            return layout("<div class='card' style='color:red'>❌ Phone & password required</div>")

        conn = sqlite3.connect(current_app.config["DATABASE"])
        cur = conn.cursor()

        user = cur.execute("""
            SELECT id, name, password, role, status, account_number
            FROM users
            WHERE phone=?
        """, (phone,)).fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):

            session.clear()

            session["user_id"] = user[0]
            session["name"] = user[1]
            session["role"] = user[3]
            session["status"] = user[4]
            session["account"] = user[5]

            if user[3] == "admin":
                return redirect("/admin/dashboard")

            return redirect("/dashboard")

        return layout("<div class='card' style='color:red'>❌ Invalid login</div>")

    return layout("""
        <div class="card">
            <h2>Login</h2>
            <form method="POST">
                <input name="phone" placeholder="Phone"><br><br>
                <input type="password" name="password" placeholder="Password"><br><br>
                <button style="background:#38bdf8;width:100%;padding:10px">
                    Login
                </button>
            </form>
        </div>
    """)


# ====================================================
# LOGOUT
# ====================================================
@auth_bp.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")


# ====================================================
# FORCE SESSION (DEBUG ONLY - REMOVE IN PRODUCTION)
# ====================================================
@auth_bp.route("/force-session")
def force_session():

    session["user_id"] = 1
    session["role"] = "admin"

    return str(dict(session))
