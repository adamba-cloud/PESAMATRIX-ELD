from flask import Flask
from flask_cors import CORS

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.user import user_bp
from routes.users import users_bp
from routes.payments import payments_bp
from routes.signals import signals_bp
from routes.content import content_bp
from routes.licenses import licenses_bp
from routes.audit import audit_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "change-this-in-production"
app.config["DATABASE"] = "database.db"

CORS(app, supports_credentials=True)

# API ROUTES
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(payments_bp, url_prefix="/api/payments")
app.register_blueprint(signals_bp, url_prefix="/api/signals")
app.register_blueprint(content_bp, url_prefix="/api/content")
app.register_blueprint(licenses_bp, url_prefix="/api/licenses")
app.register_blueprint(audit_bp, url_prefix="/api/audit")


@app.route("/")
def home():
    return {"status": "Hybrid SaaS API running"}
