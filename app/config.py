import os

class Config:
    SECRET_KEY = "secret123"
    DATABASE = os.path.join(os.getcwd(), "app.db")
    UPLOAD_FOLDER = "app/static/uploads"
