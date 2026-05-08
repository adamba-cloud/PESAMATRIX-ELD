from flask import Flask
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
# DATABASE PATH
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.config["DATABASE"] = os.path.join(
    BASE_DIR,
    "database.db"
)

# =========================
# INIT DATABASE
# =========================
with app.app_context():

    from app.database import init_db, DATABASE

    print("USING DB:", DATABASE)

    init_db()

    print("✅ Database initialized successfully")

# =========================
# IMPORT BLUEPRINTS
# =========================
from app.routes.landing import landing_bp
from app.routes.auth import auth_bp
from app.routes.user import user_bp

# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(landing_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

# =========================
# DEBUG ROUTES
# =========================
print(app.url_map)

# =========================
# START SERVER
# =========================
if __name__ == "__main__":

    print("🚀 Starting PESAMATRIX PRO SaaS...")

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
