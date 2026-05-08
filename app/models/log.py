from flask import Blueprint, request, session, redirect, url_for, render_template
from app.services.auth_service import authenticate

# =========================
# BLUEPRINT
# =========================
auth_bp = Blueprint("auth", __name__)


# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # Show login page
    if request.method == "GET":
        return render_template("login.html")

    # Get form data
    phone = request.form.get("phone")
    password = request.form.get("password")

    # Authenticate user
    user = authenticate(phone, password)

    # Invalid login
    if not user:
        return render_template(
            "login.html",
            error="Invalid phone or password"
        )

    # =========================
    # SAVE SESSION
    # =========================
    session["user_id"] = user["id"]
    session["role"] = user["role"]
    session["account"] = user["account_number"]

    # =========================
    # REDIRECT
    # =========================
    if user["role"] == "admin":
        return redirect(url_for("admin.dashboard"))

    return redirect(url_for("user.dashboard"))


# =========================
# LOGOUT
# =========================
@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))
