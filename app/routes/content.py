from flask import Blueprint, request, session, redirect, current_app
from app.utils.ui import layout
import sqlite3
import os
import time
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
# ADMIN CHECK (SECURE)
# =========================
def is_admin():
    return session.get("role") == "admin" and session.get("user_id")


# =========================
# MEDIA LIBRARY (ADMIN DASHBOARD)
# =========================
@content_bp.route("/admin/content")
def media_library():

    if not is_admin():
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    media = cur.execute("""
        SELECT * FROM content
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    html = """
    <div class="card">

        <h1 style="color:#38bdf8">📁 MEDIA LIBRARY</h1>

        <a href="/admin/content/upload"
           style="color:#38bdf8">
           ⬆ Upload New Media
        </a>

        <br><br>
    """

    for m in media:

        preview = ""

        # =========================
        # IMAGE PREVIEW
        # =========================
        if m["type"] == "image":
            preview = f"""
            <img src="{m['link']}"
                 style="width:100%;max-width:300px;
                        border-radius:10px;margin-top:10px;">
            """

        # =========================
        # VIDEO PREVIEW
        # =========================
        elif m["type"] == "video":
            preview = f"""
            <video controls
                   style="width:100%;max-width:300px;
                          border-radius:10px;margin-top:10px;">
                <source src="{m['link']}">
            </video>
            """

        html += f"""

        <div class="card">

            <h3>{m['title']}</h3>

            📂 Type: <b>{m['type']}</b><br>

            🔗 Link:
            <a href="{m['link']}" target="_blank">
                Open
            </a>

            {preview}

            <br><br>

            🕒 ID: {m['id']}

        </div>

        """

    html += "</div>"

    return layout(html)


# =========================
# UPLOAD PAGE
# =========================
@content_bp.route("/admin/content/upload", methods=["GET", "POST"])
def upload_media():

    if not is_admin():
        return redirect("/login")

    message = ""

    if request.method == "POST":

        title = request.form.get("title")
        media_type = request.form.get("type")

        file = request.files.get("file")
        link = request.form.get("link")

        if not title or not media_type:
            return layout("""
            <div class="card" style="color:red">
                ❌ Title and Type required
            </div>
            """)

        saved_link = ""

        # =========================
        # FILE UPLOAD HANDLING
        # =========================
        if file and file.filename != "":

            upload_folder = current_app.config.get(
                "UPLOAD_FOLDER",
                "static/uploads"
            )

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(file.filename)

            unique_name = f"{int(time.time())}_{filename}"

            path = os.path.join(upload_folder, unique_name)

            file.save(path)

            saved_link = f"/static/uploads/{unique_name}"

            message = "✔ File uploaded successfully"

        # =========================
        # LINK HANDLING
        # =========================
        elif link:
            saved_link = link
            message = "✔ Link saved successfully"

        else:
            return layout("""
            <div class="card" style="color:red">
                ❌ Upload file or provide link
            </div>
            """)

        # =========================
        # SAVE TO DB
        # =========================
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO content(type, title, link)
            VALUES(?,?,?)
        """, (media_type, title, saved_link))

        conn.commit()
        conn.close()

        return redirect("/admin/content")

    # =========================
    # UPLOAD UI
    # =========================
    return layout("""

    <div class="card">

        <h2 style="color:#38bdf8">
            ⬆ UPLOAD MEDIA
        </h2>

        <form method="POST" enctype="multipart/form-data">

            📌 Title:<br>
            <input name="title" required><br><br>

            📂 Type:<br>
            <select name="type">

                <option value="image">Image</option>
                <option value="video">Video</option>
                <option value="news">News</option>
                <option value="link">External Link</option>

            </select><br><br>

            📤 Upload File:<br>
            <input type="file" name="file"><br><br>

            🔗 OR Link:<br>
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
                Upload to Library
            </button>

        </form>

        <br>

        <a href="/admin/content"
           style="color:#38bdf8">
           ⬅ Back to Media Library
        </a>

    </div>

    """)
