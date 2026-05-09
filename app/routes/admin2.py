from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    session
)

import sqlite3
import secrets

from functools import wraps

from app.utils.ui import layout


# ====================================================
# BLUEPRINT
# ====================================================
admin2_bp = Blueprint(
    "admin2",
    __name__,
    url_prefix="/superadmin"
)


# ====================================================
# DB HELPER
# ====================================================
def get_db():

    conn = sqlite3.connect(
        current_app.config["DATABASE"]
    )

    conn.row_factory = sqlite3.Row

    return conn


# ====================================================
# SUPER ADMIN DECORATOR
# ====================================================
def super_admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("SESSION =", dict(session))

        # BLOCK NON ADMINS
        if session.get("role") != "admin":
            return redirect("/login")

        return func(*args, **kwargs)

    return wrapper


# ====================================================
# ROOT
# ====================================================
@admin2_bp.route("/")
def home():

    return redirect("/superadmin/dashboard")


# ====================================================
# TEST ROUTE
# ====================================================
@admin2_bp.route("/test")
def test():

    return """
    <h1 style='color:#22c55e'>
        ✅ SUPER ADMIN WORKING
    </h1>
    """


# ====================================================
# SESSION DEBUG
# ====================================================
@admin2_bp.route("/test-session")
def test_session():

    return str(dict(session))


# ====================================================
# DASHBOARD
# ====================================================
@admin2_bp.route("/dashboard")
@super_admin_required
def dashboard():

    conn = get_db()

    users = conn.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    payments = conn.execute(
        "SELECT COUNT(*) FROM payments"
    ).fetchone()[0]

    signals = conn.execute(
        "SELECT COUNT(*) FROM signals"
    ).fetchone()[0]

    content = conn.execute(
        "SELECT COUNT(*) FROM content"
    ).fetchone()[0]

    conn.close()

    return layout(f"""

    <div style="padding:20px">

        <h1 style="
            color:#38bdf8;
            font-size:32px;
        ">
            🛠 SUPER ADMIN DASHBOARD
        </h1>

        <hr><br>

        <div class="grid">

            <div class="card">
                <h2>👤 {users}</h2>
                <p>Users</p>
            </div>

            <div class="card">
                <h2>💳 {payments}</h2>
                <p>Payments</p>
            </div>

            <div class="card">
                <h2>📊 {signals}</h2>
                <p>Signals</p>
            </div>

            <div class="card">
                <h2>📁 {content}</h2>
                <p>Content</p>
            </div>

        </div>

        <br><br>

        <div class="card">

            <h3>⚡ Super Admin Controls</h3>

            <a href="/superadmin/users">
                👥 Manage Users
            </a>

            <br><br>

            <a href="/superadmin/payments">
                💳 Manage Payments
            </a>

            <br><br>

            <a href="/superadmin/signals">
                📊 Manage Signals
            </a>

            <br><br>

            <a href="/superadmin/content">
                📁 Manage Content
            </a>

            <br><br>

            <a href="/superadmin/codes">
                🔐 Access Codes
            </a>

            <br><br>

            <a href="/superadmin/logs">
                📡 System Logs
            </a>

            <br><br>

            <a href="/logout" style="color:red">
                Logout
            </a>

        </div>

    </div>

    """)


# ====================================================
# USERS
# ====================================================
@admin2_bp.route("/users")
@super_admin_required
def users():

    conn = get_db()

    data = conn.execute("""
        SELECT *
        FROM users
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for u in data:

        color = (
            "#22c55e"
            if u["status"] == "active"
            else "#ef4444"
        )

        rows += f"""

        <div class="card">

            <b>👤 {u['name']}</b><br><br>

            📱 {u['phone']}<br>

            📧 {u['email']}<br>

            🎭 Role: {u['role']}<br>

            Status:
            <b style="color:{color}">
                {u['status']}
            </b>

            <br><br>

            <a href="/superadmin/generate-code/{u['id']}">
                🔐 Generate Access Code
            </a>

        </div>

        """

    return layout(f"""

    <h2>👥 USERS MANAGEMENT</h2>

    <div class="grid">

        {rows}

    </div>

    """)


# ====================================================
# PAYMENTS
# ====================================================
@admin2_bp.route("/payments")
@super_admin_required
def payments():

    conn = get_db()

    data = conn.execute("""
        SELECT *
        FROM payments
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for p in data:

        rows += f"""

        <div class="card">

            📱 {p['phone']}<br><br>

            💳 {p['mpesa_code']}<br>

            💰 {p['amount']}<br>

            📦 {p['plan']}<br>

            Status:
            <b>{p['status']}</b>

        </div>

        """

    return layout(f"""

    <h2>💳 PAYMENTS</h2>

    <div class="grid">

        {rows}

    </div>

    """)


# ====================================================
# SIGNALS
# ====================================================
@admin2_bp.route("/signals")
@super_admin_required
def signals():

    conn = get_db()

    data = conn.execute("""
        SELECT *
        FROM signals
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for s in data:

        rows += f"""

        <div class="card">

            📊 <b>{s['asset']}</b><br><br>

            Entry: {s['entry']}<br>

            TP: {s['tp']}<br>

            SL: {s['sl']}<br>

            Status: {s['status']}

        </div>

        """

    return layout(f"""

    <h2>📊 SIGNALS</h2>

    <div class="grid">

        {rows}

    </div>

    """)


# ====================================================
# CONTENT
# ====================================================
@admin2_bp.route("/content")
@super_admin_required
def content():

    conn = get_db()

    data = conn.execute("""
        SELECT *
        FROM content
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for c in data:

        rows += f"""

        <div class="card">

            📁 {c['type']}<br><br>

            <b>{c['title']}</b><br><br>

            <a href="{c['link']}" target="_blank">
                Open Content
            </a>

        </div>

        """

    return layout(f"""

    <h2>📁 CONTENT LIBRARY</h2>

    <div class="grid">

        {rows}

    </div>

    """)


# ====================================================
# GENERATE ACCESS CODE
# ====================================================
@admin2_bp.route("/generate-code/<int:user_id>")
@super_admin_required
def generate_code(user_id):

    conn = get_db()

    code = secrets.token_hex(8)

    conn.execute("""

        INSERT INTO access_codes
        (
            user_id,
            code,
            status,
            used,
            expires_at
        )

        VALUES
        (
            ?, ?, ?, ?,
            datetime('now', '+7 days')
        )

    """, (
        user_id,
        code,
        "active",
        0
    ))

    conn.commit()
    conn.close()

    return layout(f"""

    <div class="card">

        <h2>🔐 ACCESS CODE GENERATED</h2>

        <br>

        <p>User ID: {user_id}</p>

        <div style="
            background:#111;
            color:#0f0;
            padding:15px;
            font-size:20px;
            border-radius:10px;
        ">

            {code}

        </div>

        <br>

        <p>⏳ Valid for 7 days</p>

        <a href="/superadmin/users">
            ← Back to Users
        </a>

    </div>

    """)


# ====================================================
# ACCESS CODES
# ====================================================
@admin2_bp.route("/codes")
@super_admin_required
def codes():

    conn = get_db()

    data = conn.execute("""
        SELECT *
        FROM access_codes
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    rows = ""

    for c in data:

        rows += f"""

        <div class="card">

            🔐 <b>{c['code']}</b><br><br>

            User: {c['user_id']}<br>

            Status: {c['status']}<br>

            Used: {c['used']}<br>

            Expires: {c['expires_at']}<br>

        </div>

        """

    return layout(f"""

    <h2>🔐 ACCESS CODES</h2>

    <div class="grid">

        {rows}

    </div>

    """)


# ====================================================
# LOGS
# ====================================================
@admin2_bp.route("/logs")
@super_admin_required
def logs():

    conn = get_db()

    logs = conn.execute("""
        SELECT *
        FROM request_logs
        ORDER BY timestamp DESC
        LIMIT 200
    """).fetchall()

    conn.close()

    rows = ""

    for log in logs:

        rows += f"""

        <div class="card">

            🌐 Path: {log['path']}<br><br>

            📡 Method: {log['method']}<br>

            🕒 Time: {log['timestamp']}<br>

            👤 IP: {log['ip_address']}

        </div>

        """

    return layout(f"""

    <h2>📡 SYSTEM LOGS</h2>

    <div class="grid">

        {rows}

    </div>

    """)
