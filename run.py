from flask import Flask
from app.database import init_db
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "secret123")
app.config["DATABASE"] = os.path.join(os.getcwd(), "database.db")


# =========================
# REGISTER BLUEPRINTS (SAFE IMPORT)
# =========================
from app.routes.landing import landing_bp
app.register_blueprint(landing_bp)

from app.routes.auth import auth_bp   # <-- MUST WORK
app.register_blueprint(auth_bp)


print(app.url_map)


if __name__ == "__main__":
    print("🚀 Starting PESAMATRIX PRO SaaS...")

    with app.app_context():
        init_db()

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port, debug=False)
