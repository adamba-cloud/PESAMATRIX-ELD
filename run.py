from flask import Flask
from app.database import init_db
import os

# =========================
# CREATE FLASK APP
# =========================
app = Flask(__name__)

# =========================
# SECURITY
# =========================
app.secret_key = os.environ.get("SECRET_KEY", "secret123")

# =========================
# DATABASE PATH (RENDER SAFE)
# =========================
app.config["DATABASE"] = os.path.join(os.getcwd(), "database.db")

# =========================
# IMPORT ROUTES
# =========================
from app.routes.auth import auth_bp
from app.routes.landing import landing_bp   # ✅ ADDED (important for /)
app.register_blueprint(auth_bp)
app.register_blueprint(landing_bp)

# =========================
# DEBUG ROUTES (IMPORTANT)
# =========================
print(app.url_map)

# =========================
# START SERVER
# =========================
if __name__ == "__main__":

    print("🚀 Starting PESAMATRIX PRO SaaS...")

    # CREATE DATABASE TABLES
    init_db()

    print("✅ Database ready")
    print("🌐 Server starting...")

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
