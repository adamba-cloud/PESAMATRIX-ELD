from flask import Blueprint, request, session, redirect, render_template_string, current_app
import sqlite3

signals_bp = Blueprint("signals", __name__)


# =========================
# LOGIN CHECK
# =========================
def login_required():
    return session.get("user_id") is not None


# =========================
# DATABASE HELPER
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# USER SIGNALS PAGE (LOCKED SYSTEM)
# =========================
@signals_bp.route("/signals")
def view_signals():
    if not login_required():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    # check user status
    user = cur.execute(
        "SELECT status FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    # =========================
    # 🔒 LOCKED ACCESS
    # =========================
    if user["status"] != "active":
        conn.close()
        return render_template_string("""
        <div style="background:#0b1220;color:white;padding:30px;font-family:Arial;text-align:center">

            <h1 style="color:#ff4d4d">🔒 SIGNALS LOCKED</h1>

            <p>You must subscribe and get approval to access trading signals.</p>

            <br>

            <a href="/payments/status"
               style="background:#38bdf8;color:black;padding:10px 20px;text-decoration:none;border-radius:5px">
               💳 Check Payment Status
            </a>

        </div>
        """)

    # =========================
    # UNLOCKED SIGNALS
    # =========================
    signals = cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """
    <div style="background:#0b1220;color:white;font-family:Arial;padding:20px">

        <h1 style="color:#38bdf8">📊 LIVE SIGNALS</h1>
    """

    for s in signals:
        html += f"""
        <div style="background:#111a2e;padding:10px;margin:10px;border-radius:8px">
            📌 Asset: {s['asset']}<br>
            💰 Entry: {s['entry']}<br>
            🎯 TP: {s['tp']}<br>
            🛑 SL: {s['sl']}<br>
            📡 Status: {s['status']}
        </div>
        """

    html += "</div>"
    return html


# =========================
# ADMIN CREATE SIGNALS
# =========================
@signals_bp.route("/admin/signals", methods=["GET", "POST"])
def create_signal():
    if session.get("role") != "admin":
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        cur.execute("""
        INSERT INTO signals(asset, entry, tp, sl, status)
        VALUES(?,?,?,?,?)
        """, (
            request.form["asset"],
            request.form["entry"],
            request.form["tp"],
            request.form["sl"],
            "ACTIVE"
        ))

        conn.commit()
        conn.close()
        return redirect("/admin/signals")

    conn.close()

    return render_template_string("""
    <div style="background:#0b1220;color:white;font-family:Arial;padding:20px">

        <h1 style="color:#38bdf8">📊 CREATE SIGNAL</h1>

        <form method="POST">
            Asset:<br><input name="asset"><br><br>
            Entry:<br><input name="entry"><br><br>
            TP:<br><input name="tp"><br><br>
            SL:<br><input name="sl"><br><br>
            <button type="submit">Create Signal</button>
        </form>

        <br>
        <a href="/admin" style="color:#38bdf8">⬅ Back to Admin</a>

    </div>
    """)
