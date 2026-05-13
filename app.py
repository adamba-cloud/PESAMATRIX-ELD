import os
import sqlite3
from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "super-secret-key")

DB = "tradepro.db"
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")


# ================= DATABASE =================
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        plan TEXT DEFAULT 'Free',
        total_profit REAL DEFAULT 4250,
        win_rate INTEGER DEFAULT 82,
        total_signals INTEGER DEFAULT 128
    )
    """)

    # Create default admin
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users (username, password, plan) VALUES (?, ?, ?)",
            ("admin", ADMIN_PASSWORD, "VIP"),
        )

    conn.commit()
    conn.close()


# ================= AUTH =================
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


@app.context_processor
def inject_user():
    if "user_id" in session:
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE id=?", (session["user_id"],)
        ).fetchone()
        conn.close()
        return {"current_user": user}
    return {"current_user": None}


# ================= ROUTES =================
@app.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            flash("All fields are required.")
            return redirect(url_for("register"))

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            conn.commit()
            flash("Account created successfully.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
        finally:
            conn.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password),
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/signals")
@login_required
def signals():
    sample_signals = [
        {"pair": "EUR/USD", "type": "BUY", "entry": "1.08245", "pips": "+45"},
        {"pair": "XAUUSD", "type": "BUY", "entry": "2356.75", "pips": "+120"},
        {"pair": "GBP/USD", "type": "SELL", "entry": "1.26340", "pips": "-25"},
        {"pair": "BTCUSDT", "type": "BUY", "entry": "67892.11", "pips": "+230"},
    ]
    return render_template("signals.html", signals=sample_signals)


@app.route("/payments")
@login_required
def payments():
    return render_template("payments.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/upgrade")
@login_required
def upgrade():
    conn = get_db()
    conn.execute(
        "UPDATE users SET plan='VIP' WHERE id=?", (session["user_id"],)
    )
    conn.commit()
    conn.close()
    flash("Your account has been upgraded to VIP.")
    return redirect(url_for("dashboard"))


@app.route("/admin")
@login_required
def admin():
    if current_user()["username"] != "admin":
        flash("Access denied.")
        return redirect(url_for("dashboard"))

    conn = get_db()
    users = conn.execute("SELECT * FROM users ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("admin.html", users=users)


# Helper to fetch current user in routes

def current_user():
    if "user_id" not in session:
        return None
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE id=?", (session["user_id"],)
    ).fetchone()
    conn.close()
    return user


# ================= STARTUP =================
init_db()


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
