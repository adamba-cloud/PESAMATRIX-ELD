from flask import request, session, redirect, render_template
import sqlite3
from datetime import datetime

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        phone = request.form.get("phone")
        password = request.form.get("password")

        # =========================
        # DEBUG PRINTS (ADDED)
        # =========================
        print("PHONE:", phone)
        print("PASSWORD:", password)

        if not phone or not password:
            return "Missing fields"

        user = authenticate(phone, password)

        # =========================
        # DEBUG PRINT (ADDED)
        # =========================
        print("USER:", user)

        if user:
            session["user_id"] = user["id"]

            # ✅ LOG LOGIN SUCCESS
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO logs (action, user, time) VALUES (?, ?, ?)",
                ("login_success", phone, datetime.now().isoformat())
            )
            conn.commit()
            conn.close()

            return redirect("/dashboard")

        # ❌ LOG LOGIN FAILURE
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO logs (action, user, time) VALUES (?, ?, ?)",
            ("login_failed", phone, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()

        return "Invalid credentials"

    return render_template("login.html")
