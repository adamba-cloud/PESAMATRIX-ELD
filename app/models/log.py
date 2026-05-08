from flask import request, session, redirect, render_template, current_app
import sqlite3
from datetime import datetime

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")

        # =========================
        # DEBUG START
        # =========================
        print("LOGIN START")
        print("PHONE:", phone)
        print("PASSWORD:", password)

        if not phone or not password:
            return "Missing fields"

        user = authenticate(phone, password)

        # =========================
        # DEBUG RESULT
        # =========================
        print("USER:", user)
        print("LOGIN END")

        if user:
            # ✅ SESSION FIX (THIS WAS MISSING ROLE BEFORE)
            session["user_id"] = user["id"]
            session["role"] = user["role"]   # 🔥 REQUIRED FOR ADMIN

            # =========================
            # LOG SUCCESS
            # =========================
            conn = sqlite3.connect(current_app.config["DATABASE"])
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO logs (action, user, time) VALUES (?, ?, ?)",
                ("login_success", phone, datetime.now().isoformat())
            )
            conn.commit()
            conn.close()

            return redirect("/dashboard")

        # =========================
        # LOG FAILURE
        # =========================
        conn = sqlite3.connect(current_app.config["DATABASE"])
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO logs (action, user, time) VALUES (?, ?, ?)",
            ("login_failed", phone, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()

        return "Invalid credentials"

    return render_template("login.html")
