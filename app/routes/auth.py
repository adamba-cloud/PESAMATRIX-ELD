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
