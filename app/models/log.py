from app.services.auth_service import authenticate

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        phone = request.form.get("phone")
        password = request.form.get("password")

        user = authenticate(phone, password)

        if not user:
            return "Invalid login"

        # ONLY SESSION HERE
        session.clear()
        session["user_id"] = user["id"]
        session["role"] = user["role"]

        return redirect("/dashboard")

    return layout("login page here")
