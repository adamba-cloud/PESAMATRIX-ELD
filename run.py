from app import create_app
from app.db import init_db
import os

app = create_app()


# =========================
# START SERVER
# =========================
if __name__ == "__main__":

    print("🚀 Starting PESAMATRIX PRO SaaS...")

    # CREATE DATABASE TABLES
    init_db()

    print("✅ Database ready")
    print("🌐 Server starting...")

    # RENDER + LOCAL SUPPORT
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
