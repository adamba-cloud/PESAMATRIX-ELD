import os

class Config:
    # 🔐 Security key (change later in production)
    SECRET_KEY = "secret123"

    # 🗄️ Database path (always absolute for stability)
    DATABASE = os.path.join(os.getcwd(), "app.db")

    # 📁 Upload folder for images/videos
    UPLOAD_FOLDER = os.path.join("app", "static", "uploads")
