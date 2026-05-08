from flask import Flask
from app.database import init_db
import os

# =========================
# CREATE FLASK APP
# =========================
app = Flask(__name__)

# SECRET KEY
app.secret_key = "secret123"

# DATABASE PATH
app.config["DATABASE"] = "database.db"


# =========================
# IMPORT ROUTES
# =========================
from app.routes.auth import auth_bp

app.register_blueprint(auth_bp)


# =========================
# START SERVER
# =========================
if __name__ == "__main__":

    print("🚀 Starting PESAMATRIX PRO SaaS...")

    # CREATE DATABASE TABLES
    init_db(app)

    print("✅ Database ready")
    print("🌐 Server starting...")

    # RENDER PORT
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
