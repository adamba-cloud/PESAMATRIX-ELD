from flask import Flask
from flask_cors import CORS

# =========================
# ROUTES
# =========================
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.user import user_bp
from routes.users import users_bp
from routes.payments import payments_bp
from routes.signals import signals_bp
from routes.content import content_bp
from routes.licenses import licenses_bp
from routes.audit import audit_bp

# =========================
# DB CLEANUP
# =========================
from utils.db import close_db


# =========================
# APP INITIALIZATION
# =========================
app = Flask(__name__)

# IMPORTANT: move to env in production later
app.config["SECRET_KEY"] = "change-this-in-production"
app.config["DATABASE"] = "database.db"

# enable frontend communication (React)
CORS(app, supports_credentials=True)


# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(payments_bp, url_prefix="/api/payments")
app.register_blueprint(signals_bp, url_prefix="/api/signals")
app.register_blueprint(content_bp, url_prefix="/api/content")
app.register_blueprint(licenses_bp, url_prefix="/api/licenses")
app.register_blueprint(audit_bp, url_prefix="/api/audit")


# =========================
# CLEAN DB HANDLER (IMPORTANT)
# =========================
app.teardown_appcontext(close_db)


# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return {
        "status": "Hybrid SaaS API running",
        "version": "1.0",
        "mode": "production-ready"
    }
