from flask import Blueprint, request, session, redirect, current_app
from app.utils.ui import layout
import sqlite3
import os
from werkzeug.utils import secure_filename

content_bp = Blueprint("content", __name__)


# =========================
# DB CONNECTION
# =========================
def get_db():
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# ADMIN CHECK (SAFE)
# =========================
def is_admin():
    return session.get("role") == "admin" and session.get("user_id") is not None


# =========================
# ADMIN CONTENT UPLOAD
# =========================
@content_bp.route("/admin/content", methods=["GET", "POST"])
def upload_content():

    if not is_admin():
        return redirect("/login")

    message = ""

    if request.method == "POST":

        content_type = request.form.get("type")
        title = request.form.get("title")

        file = request.files.get("file")
        link = request.form.get("link")

        saved_link = ""

        # =========================
        # VALIDATION
        # =========================
        if not title or not content_type:
            return layout("""
            <div class="card" style="color:red">
                ❌ Title and Type are required
            </div>
            """)

        # =========================
        # FILE UPLOAD (SAFE)
        # =========================
        if file and file.filename != "":

            upload_folder = current_app.config.get(
                "UPLOAD_FOLDER",
                "static/uploads"
            )

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(file.filename)

            # prevent overwrite collisions
            unique_filename = f"{int(__import__('time').time())}_{filename}"

            path = os.path.join(upload_folder, unique_filename)

            file.save(path)

            saved_link = f"/static/uploads/{unique_filename}"

            message = "✔ File uploaded successfully"

        # =========================
        # EXTERNAL LINK
        # =========================
        elif link:
            saved_link = link
            message = "✔ Link saved successfully"

        else:
            return layout("""
            <div class="card" style="color:red">
                ❌ Please upload a file or provide a link
            </div>
            """)

        # =========================
        # SAVE TO DATABASE
        # =========================
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO content(type, title, link)
            VALUES(?,?,?)
        """, (content_type, title, saved_link))

        conn.commit()
        conn.close()

        return redirect("/admin/content")


    # =========================
    # UPLOAD FORM UI
    # =========================
    return layout("""

    <div class="card">

        <h2 style="color:#38bdf8">
            📁 ADMIN CONTENT UPLOAD
        </h2>

        <form method="POST" enctype="multipart/form-data">

            📌 Title:<br>
            <input name="title" required><br><br>

            📂 Type:<br>
            <select name="type" required>

                <option value="image">Image</option>
                <option value="video">Video</option>
                <option value="news">News</option>
                <option value="link">Link</option>

            </select><br><br>

            📤 Upload File:<br>
            <input type="file" name="file"><br><br>

            🔗 OR External Link:<br>
            <input name="link"><br><br>

            <button style="
                background:#38bdf8;
                color:black;
                padding:10px;
                border:none;
                border-radius:6px;
                width:100%;
                font-weight:bold;
            ">
                ⬆ Upload Content
            </button>

        </form>

        <br>

        <a href="/admin" style="color:#38bdf8">
            ⬅ Back to Admin
        </a>

    </div>

    """)
