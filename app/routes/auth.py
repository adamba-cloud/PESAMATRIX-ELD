from flask import Blueprint, request, session, redirect
from app.services.auth_service import create_user, authenticate
from app.utils.ui import layout

auth_bp = Blueprint("auth", __name__)


# =========================
# REGISTER
# =========================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    # =========================
    # POST REGISTER
    # =========================
    if request.method == "POST":

        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # =========================
        # VALIDATION
        # =========================
        if not name or not phone or not email or not password:
            return layout("""
            <div class="card" style="color:red;text-align:center">
                ❌ All fields are required
            </div>
            """)

        try:
            account = create_user(name, phone, email, password)

        except Exception as e:
            return layout(f"""
            <div class="card" style="color:red;text-align:center">

                ❌ Registration failed<br><br>
                {str(e)}

                <br><br>

                <a href="/register" style="color:#38bdf8">
                    Try again
                </a>

            </div>
            """)

        return layout(f"""

        <div class="card" style="text-align:center">

            <h2 style="color:#22c55e">
                Account Created ✔
            </h2>

            <p>Your Account Number:</p>

            <h3 style="color:#38bdf8">
                {account}
            </h3>

            <p style="color:#cbd5e1">
                Use this account number as your Paybill reference (322372)
            </p>

            <a href="/login" style="color:#38bdf8">
                Go to Login
            </a>

        </div>

        """)

    # =========================
    # REGISTER PAGE
    # =========================
    return layout("""

    <div class="card">

        <h2 style="color:#38bdf8">Create Account</h2>

        <form method="POST">

            <input name="name" placeholder="Full Name" required><br><br>

            <input name="phone" placeholder="Phone Number" required><br><br>

            <input name="email" placeholder="Email Address" required><br><br>

            <input type="password" name="password" placeholder="Password" required><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                border:none;
                border-radius:6px;
                width:100%;
                font-weight:bold;
            ">
                Register
            </button>

        </form>

    </div>

    """)


# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # =========================
    # POST LOGIN
    # =========================
    if request.method == "POST":

        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "").strip()

        if not phone or not password:
            return layout("""
            <div class="card" style="color:red;text-align:center">
                ❌ Phone and password required
            </div>
            """)

        user = authenticate(phone, password)

        if not user:
            return layout("""
            <div class="card" style="color:red;text-align:center">

                <h3>Invalid login ❌</h3>

                <a href="/login" style="color:#38bdf8">
                    Try again
                </a>

            </div>
            """)

        # =========================
        # SESSION SETUP
        # =========================
        session["user_id"] = user["id"]
        session["role"] = user["role"]
        session["account"] = user["account_number"]

        # =========================
        # ROLE ROUTING
        # =========================
        if user["role"] == "admin":
            return redirect("/admin/dashboard")

        return redirect("/dashboard")

    # =========================
    # LOGIN PAGE
    # =========================
    return layout("""

    <div class="card">

        <h2 style="color:#38bdf8">Login</h2>

        <form method="POST">

            <input name="phone" placeholder="Phone Number" required><br><br>

            <input type="password" name="password" placeholder="Password" required><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                border:none;
                border-radius:6px;
                width:100%;
                font-weight:bold;
            ">
                Login
            </button>

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
