import os


class Config:

    # =========================
    # SECURITY
    # =========================
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret123")

    # =========================
    # BASE DIRECTORY (SAFE PATHING)
    # =========================
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # =========================
    # DATABASE (ABSOLUTE PATH)
    # =========================
    DATABASE = os.path.join(BASE_DIR, "app.db")

    # =========================
    # UPLOADS (MEDIA STORAGE)
    # =========================
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit (safe default)

    # =========================
    # SECURITY SETTINGS (SAAS READY)
    # =========================
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


# =========================
# ENSURE FOLDERS EXIST
# =========================
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
