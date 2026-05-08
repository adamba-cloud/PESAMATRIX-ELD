from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "secret123")

# =========================
# USE SAME DATABASE EVERYWHERE
# =========================
from app.database import DATABASE, init_db

app.config["DATABASE"] = DATABASE

# =========================
# INIT DATABASE
# =========================
with app.app_context():

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

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
