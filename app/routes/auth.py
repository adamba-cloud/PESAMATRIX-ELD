from flask import Blueprint, request, session, redirect
from app.services.auth_service import create_user, authenticate
from app.utils.ui import layout

# =========================
# BLUEPRINT
# =========================
auth_bp = Blueprint("auth", __name__)


# =========================
# REGISTER
# =========================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        account = create_user(
            request.form["name"],
            request.form["phone"],
            request.form["email"],
            request.form["password"]
        )

        return layout(f"""
        <div class="card" style="text-align:center">

            <h2 style="color:#22c55e">Account Created ✔</h2>

            <p>Your Account Number:</p>
            <h3 style="color:#38bdf8">{account}</h3>

            <a href="/login" style="color:#38bdf8">
                Go to Login
            </a>

        </div>
        """)

    return layout("""
    <div class="card">

        <h2 style="color:#38bdf8">Create Account</h2>

        <form method="POST">
            <input name="name" placeholder="Name"><br><br>
            <input name="phone" placeholder="Phone"><br><br>
            <input name="email" placeholder="Email"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                border:none;
                border-radius:6px;
                width:100%;
            ">Register</button>
        </form>

    </div>
    """)


# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        phone = request.form.get("phone")
        password = request.form.get("password")

        user = authenticate(phone, password)

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]
            session["account"] = user["account_number"]

            return redirect("/dashboard")

        return layout("""
        <div class="card" style="color:red;text-align:center">
            <h3>Invalid login</h3>
            <a href="/login" style="color:#38bdf8">Try again</a>
        </div>
        """)

    return layout("""
    <div class="card">

        <h2 style="color:#38bdf8">Login</h2>

        <form method="POST">
            <input name="phone" placeholder="Phone"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                border:none;
                border-radius:6px;
                width:100%;
            ">Login</button>
        </form>

    </div>
    """)


# =========================
# LOGOUT
# =========================
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
