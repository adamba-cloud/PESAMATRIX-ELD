from flask import (
    Blueprint,
    redirect,
    current_app,
    url_for,
    request
)

from app.utils.ui import layout
from app.utils.decorators import admin_required

import sqlite3
import os
from werkzeug.utils import secure_filename


admin_bp = Blueprint("admin", __name__)

UPLOAD_FOLDER = "static/uploads"


# =========================
# ADMIN ROOT
# =========================
@admin_bp.route("/admin")
@admin_required
def admin_root():
    return redirect(url_for("admin.admin_dashboard"))


# =========================
# ADMIN DASHBOARD
# =========================
@admin_bp.route("/admin/dashboard")
@admin_required
def admin_dashboard():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    users = cur.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    payments = cur.execute(
        "SELECT COUNT(*) FROM payments"
    ).fetchone()[0]

    signals = cur.execute(
        "SELECT COUNT(*) FROM signals"
    ).fetchone()[0]

    content = cur.execute(
        "SELECT COUNT(*) FROM content"
    ).fetchone()[0]

    conn.close()

    return layout(f"""

    <div class="card">

        <h1 style="color:#38bdf8">
            🛠 ADMIN DASHBOARD
        </h1>

        <div class="grid">

            <div class="stat-card">
                <h2>{users}</h2>
                <p>👤 Users</p>
            </div>

            <div class="stat-card">
                <h2>{payments}</h2>
                <p>💳 Payments</p>
            </div>

            <div class="stat-card">
                <h2>{signals}</h2>
                <p>📊 Signals</p>
            </div>

            <div class="stat-card">
                <h2>{content}</h2>
                <p>📁 Content</p>
            </div>

        </div>

        <br>

        <a href="/admin/users">
            👥 Manage Users
        </a><br><br>

        <a href="/admin/payments">
            💳 Approve Payments
        </a><br><br>

        <a href="/admin/signals">
            📊 Trade Management
        </a><br><br>

        <a href="/admin/content">
            📁 Upload Content
        </a><br><br>

        <a href="/logout"
           style="
           background:#ef4444;
           color:white;
           ">
            Logout
        </a>

    </div>

    """)


# =========================
# TRADE MANAGEMENT
# =========================
@admin_bp.route("/admin/signals")
@admin_required
def manage_signals():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    signals = cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    ).fetchall()

    conn.close()

    html = """

    <div class="card">

        <h2 style="color:#38bdf8">
            📊 TRADE MANAGEMENT
        </h2>

    """

    for s in signals:

        status_class = s["status"].lower()

        html += f"""

        <div class="card">

            <h3 style="color:#38bdf8">
                📌 {s['asset']}
            </h3>

            💰 Entry:
            <b>{s['entry']}</b><br><br>

            🎯 Take Profit:
            <b>{s['tp']}</b><br><br>

            🛑 Stop Loss:
            <b>{s['sl']}</b><br><br>

            Current Status:

            <span class="badge {status_class}">
                {s['status']}
            </span>

            <br><br>

            <a href="/admin/signal/{s['id']}/Upcoming">
                Upcoming
            </a>

            |

            <a href="/admin/signal/{s['id']}/Running">
                Running
            </a>

            |

            <a href="/admin/signal/{s['id']}/Expired">
                Expired
            </a>

        </div>

        """

    html += "</div>"

    return layout(html)


# =========================
# UPDATE SIGNAL STATUS
# =========================
@admin_bp.route("/admin/signal/<int:id>/<status>")
@admin_required
def update_signal_status(id, status):

    allowed = [
        "Upcoming",
        "Running",
        "Expired"
    ]

    if status not in allowed:
        return redirect("/admin/signals")

    conn = sqlite3.connect(
        current_app.config["DATABASE"]
    )

    cur = conn.cursor()

    cur.execute(
        "UPDATE signals SET status=? WHERE id=?",
        (status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/admin/signals")


# =========================
# CONTENT MANAGEMENT
# =========================
@admin_bp.route(
    "/admin/content",
    methods=["GET", "POST"]
)
@admin_required
def content_upload():

    message = ""

    if request.method == "POST":

        title = request.form.get("title")
        content_type = request.form.get("type")
        link = request.form.get("link")

        file = request.files.get("file")

        uploaded_path = ""

        if file and file.filename != "":

            os.makedirs(
                UPLOAD_FOLDER,
                exist_ok=True
            )

            filename = secure_filename(
                file.filename
            )

            uploaded_path = (
                f"{UPLOAD_FOLDER}/{filename}"
            )

            file.save(uploaded_path)

            message = """

            <div class="success">
                ✅ Upload Successful
            </div>

            """

        elif link:

            uploaded_path = link

            message = """

            <div class="success">
                ✅ Link Saved Successfully
            </div>

            """

        conn = sqlite3.connect(
            current_app.config["DATABASE"]
        )

        cur = conn.cursor()

        cur.execute(
            """

            INSERT INTO content
            (title, type, link)

            VALUES (?, ?, ?)

            """,
            (
                title,
                content_type,
                uploaded_path
            )
        )

        conn.commit()
        conn.close()

    return layout(f"""

    <div class="card">

        <h2 style="color:#38bdf8">
            📁 CONTENT MANAGEMENT
        </h2>

        {message}

        <form method="POST"
              enctype="multipart/form-data">

            <input
                type="text"
                name="title"
                placeholder="Content Title"
                required
            >

            <select name="type">

                <option value="image">
                    🖼 Image
                </option>

                <option value="video">
                    🎥 Video
                </option>

                <option value="news">
                    📰 News
                </option>

                <option value="link">
                    🔗 External Link
                </option>

            </select>

            <input
                type="file"
                name="file"
            >

            <input
                type="text"
                name="link"
                placeholder="External Link (optional)"
            >

            <button type="submit">

                ⬆ Upload Content

            </button>

        </form>

    </div>

    """)
