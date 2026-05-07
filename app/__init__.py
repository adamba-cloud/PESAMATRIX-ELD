from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # create folders
    import os
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # register routes
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.user import user_bp
    from app.routes.signals import signals_bp
    from app.routes.payments import payments_bp
    from app.routes.content import content_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(signals_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(content_bp)

    @app.route("/")
    def home():
        return "<h1 style='text-align:center'>PESAMATRIX PRO SaaS Running 🚀</h1>"

    return app
