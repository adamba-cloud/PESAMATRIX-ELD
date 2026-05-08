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
# DATABASE PATH (RENDER SAFE)
# =========================
app.config["DATABASE"] = os.path.join(
    os.path.dirname(__file__),
    "database.db"
)

# =========================
# INITIALIZE DATABASE (SAFE CONTEXT)
# =========================
with app.app_context():
    from app.database import init_db
    init_db()

# =========================
# IMPORT BLUEPRINTS
# =========================
from app.routes.landing import landing_bp
from app.routes.auth import auth_bp

# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(landing_bp)
app.register_blueprint(auth_bp)

# =========================
# DEBUG ROUTES (OPTIONAL)
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
