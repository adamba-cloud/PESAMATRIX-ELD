from flask import Blueprint, request, session, redirect, render_template_string, current_app
import sqlite3, os

content_bp = Blueprint("content", __name__)


# =========================
# ADMIN CHECK
# =========================
def is_admin():
    return session.get("role") == "admin"


# =========================
# UPLOAD CONTENT (ADMIN)
# =========================
@content_bp.route("/admin/content", methods=["GET", "POST"])
def upload_content():
    if not is_admin():
        return redirect("/login")

    if request.method == "POST":

        conn = sqlite3.connect(current_app.config["DATABASE"])
        cur = conn.cursor()

        content_type = request.form["type"]
        title = request.form["title"]

        file = request.files.get("file")
        link = request.form.get("link")

        saved_link = ""

        # =========================
        # FILE UPLOAD
        # =========================
        if file and file.filename != "":
            path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                file.filename
            )
            file.save(path)

            saved_link = "/static/uploads/" + file.filename

        # =========================
        # LINK CONTENT
        # =========================
        elif link:
            saved_link = link

        cur.execute("""
            INSERT INTO content(type, title, link)
            VALUES(?,?,?)
        """, (content_type, title, saved_link))

        conn.commit()
        conn.close()

        return redirect("/admin/content")

    return render_template_string("""
    <div style="background:#0b1220;color:white;padding:20px;font-family:Arial">

        <h2 style="color:#38bdf8">📁 ADMIN CONTENT UPLOAD</h2>

        <form method="POST" enctype="multipart/form-data">

            📌 Title:<br>
            <input name="title"><br><br>

            📂 Type:<br>
            <select name="type">
                <option value="image">Image</option>
                <option value="video">Video</option>
                <option value="news">News</option>
                <option value="link">Link</option>
            </select><br><br>

            📤 Upload File:<br>
            <input type="file" name="file"><br><br>

            🔗 OR External Link:<br>
            <input name="link"><br><br>

            <button>Upload Content</button>
        </form>

        <br>
        <a href="/admin" style="color:#38bdf8">⬅ Back to Admin</a>

    </div>
    """)
