from flask import Flask
import os

from app.database import DATABASE, init_db

# =========================
# APP CONFIG
# =========================
app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change_this_in_production"
)

app.config["DATABASE"] = DATABASE


# =========================
# INIT DATABASE SAFELY
# =========================
with app.app_context():
    try:
        print("📦 Using DB:", DATABASE)
        init_db()
        print("✅ Database initialized successfully")

    except Exception as e:
        print("❌ Database init failed:", str(e))


# =========================
# IMPORT BLUEPRINTS
# =========================
from app.routes.landing import landing_bp
from app.routes.auth import auth_bp
from app.routes.user import user_bp
from app.routes.admin import admin_bp


# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(landing_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


# =========================
# HEALTH CHECK (SAFE)
# =========================
@app.route("/health")
def health():

    return {
        "status": "running",
        "database": "connected"
    }


# =========================
# START SERVER
# =========================
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    print("🚀 Starting server on port", port)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
