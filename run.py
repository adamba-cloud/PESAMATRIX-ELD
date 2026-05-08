from flask import Flask
import os
import sqlite3

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "secret123")

# =========================
# DATABASE
# =========================
from app.database import DATABASE, init_db

app.config["DATABASE"] = DATABASE

# =========================
# INIT DB
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
from app.routes.admin import admin_bp

# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(landing_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

# =========================
# TEMP ADMIN CREATOR
# DELETE AFTER USE
# =========================
@app.route("/make-admin")
def make_admin():

    conn = sqlite3.connect(app.config["DATABASE"])
    cur = conn.cursor()

    cur.execute("""
        UPDATE users
        SET role='admin'
        WHERE phone='254717434943'
    """)

    conn.commit()
    conn.close()

    return "✅ Admin updated successfully"

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
