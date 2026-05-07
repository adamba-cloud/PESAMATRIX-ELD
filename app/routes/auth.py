from flask import Blueprint, request, session, redirect, current_app
from app.services.auth_service import create_user, authenticate
from app.utils.ui import layout

auth_bp = Blueprint("auth", __name__)

# =========================
# REGISTER
# =========================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        account = create_user(
            current_app.config["DATABASE"],
            request.form["name"],
            request.form["phone"],
            request.form["email"],
            request.form["password"]
        )

        return layout(f"""
        <div class="card">

            <h2 style="color:green">Account Created ✔</h2>
            <p>Your Account Number: <b>{account}</b></p>

            <a href="/login" style="color:#38bdf8">Go to Login</a>

        </div>
        """)

    return layout("""
    <div class="card">

        <h2 style="color:#38bdf8">Register</h2>

        <form method="POST">
            Name:<br><input name="name"><br><br>
            Phone:<br><input name="phone"><br><br>
            Email:<br><input name="email"><br><br>
            Password:<br><input type="password" name="password"><br><br>

            <button>Register</button>
        </form>

    </div>
    """)


# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = authenticate(
            current_app.config["DATABASE"],
            request.form["phone"],
            request.form["password"]
        )

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]
            session["account"] = user["account_number"]
            session["phone"] = user["phone"]

            return redirect("/dashboard")

        return layout("""
        <div class="card" style="color:red">
            <h3>Invalid login</h3>
            <a href="/login" style="color:#38bdf8">Try again</a>
        </div>
        """)

    return layout("""
    <div class="card">

        <h2 style="color:#38bdf8">Login</h2>

        <form method="POST">
            Phone:<br><input name="phone"><br><br>
            Password:<br><input type="password" name="password"><br><br>

            <button>Login</button>
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
