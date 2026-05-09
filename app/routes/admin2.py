from flask import Blueprint

admin2_bp = Blueprint(
    "admin2",
    __name__,
    url_prefix="/superadmin"
)


# =========================
# SUPER ADMIN HOME
# =========================
@admin2_bp.route("/")
def home():

    return """
    <h1 style='color:#38bdf8'>
        ✅ SUPER ADMIN WORKING
    </h1>

    <br>

    <a href='/superadmin/dashboard'>
        Open Dashboard
    </a>
    """


# =========================
# DASHBOARD
# =========================
@admin2_bp.route("/dashboard")
def dashboard():

    return """
    <div style='padding:30px;font-family:Arial'>

        <h1 style='color:#38bdf8'>
            🛠 SUPER ADMIN DASHBOARD
        </h1>

        <hr><br>

        <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:20px'>

            <div style='background:#111;padding:20px;border-radius:10px'>
                <h2>👤 120</h2>
                <p>Users</p>
            </div>

            <div style='background:#111;padding:20px;border-radius:10px'>
                <h2>💳 43</h2>
                <p>Payments</p>
            </div>

            <div style='background:#111;padding:20px;border-radius:10px'>
                <h2>📊 17</h2>
                <p>Signals</p>
            </div>

            <div style='background:#111;padding:20px;border-radius:10px'>
                <h2>📁 9</h2>
                <p>Content</p>
            </div>

        </div>

        <br><br>

        <a href='/superadmin/users'>
            👥 Manage Users
        </a>

        <br><br>

        <a href='/superadmin/payments'>
            💳 Payments
        </a>

    </div>
    """


# =========================
# USERS
# =========================
@admin2_bp.route("/users")
def users():

    return """
    <h1>👥 USERS PAGE WORKING</h1>
    """


# =========================
# PAYMENTS
# =========================
@admin2_bp.route("/payments")
def payments():

    return """
    <h1>💳 PAYMENTS PAGE WORKING</h1>
    """
