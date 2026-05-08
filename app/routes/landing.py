from flask import Blueprint
from app.utils.ui import layout

landing_bp = Blueprint("landing", __name__)


# =========================
# HOME PAGE (PUBLIC)
# =========================
@landing_bp.route("/")
def home():

    return layout("""

    <!-- NAVBAR -->
    <div style="
        background:#0f172a;
        padding:15px 25px;
        display:flex;
        justify-content:space-between;
        align-items:center;
        border-radius:12px;
        margin-bottom:20px;
    ">

        <h2 style="color:#38bdf8;margin:0">
            📊 PESAMATRIX PRO
        </h2>

        <div>

            <a href="/login"
               style="
                    color:white;
                    margin-right:15px;
                    text-decoration:none
               ">

                Login

            </a>

            <a href="/register"
               style="
                    color:#38bdf8;
                    text-decoration:none
               ">

                Register

            </a>

        </div>

    </div>


    <!-- HERO -->
    <div class="card"
        style="text-align:center;padding:50px 20px">

        <h1 style="
            font-size:38px;
            color:#38bdf8;
            margin-bottom:10px
        ">

            Smart Trading & Copy System

        </h1>

        <p style="color:#cbd5e1;font-size:16px">

            Forex & Crypto signals platform built
            for consistent traders

        </p>

        <br>

        <a href="/register"
           style="
                background:#38bdf8;
                color:black;
                padding:12px 25px;
                text-decoration:none;
                border-radius:8px;
                font-weight:bold;
           ">

            🚀 Get Started

        </a>

    </div>


    <!-- FEATURES -->
    <div class="grid">

        <div class="card">
            <h3>📊 Signals</h3>
            <p>Daily high-quality trading setups</p>
        </div>

        <div class="card">
            <h3>⚡ Fast Alerts</h3>
            <p>Real-time market updates</p>
        </div>

        <div class="card">
            <h3>🔒 Premium Access</h3>
            <p>Unlock after subscription approval</p>
        </div>

    </div>


    <!-- HOW IT WORKS -->
    <div class="card">

        <h2 style="color:#38bdf8;text-align:center">
            How It Works
        </h2>

        <div style="
            text-align:center;
            line-height:2;
            color:#cbd5e1
        ">

            1. Create an account<br>
            2. Pay via Paybill <b>322372</b><br>
            3. Use account number as reference<br>
            4. Wait for activation<br>
            5. Access signals instantly

        </div>

    </div>


    <!-- PRICING -->
    <div class="card">

        <h2 style="color:#38bdf8;text-align:center">
            Subscription Plans
        </h2>

        <div style="
            text-align:center;
            line-height:2;
            color:#cbd5e1
        ">

            Daily Plan – Affordable access<br>
            Weekly Plan – Best value<br>
            Monthly Plan – Professional traders

        </div>

    </div>


    <!-- PAYMENT -->
    <div class="card"
        style="text-align:center">

        <h2 style="color:#38bdf8">
            Payment Details
        </h2>

        <p>💰 Paybill: <b>322372</b></p>
        <p>📌 Account: Your registration number</p>

    </div>


    <!-- CONTACT -->
    <div class="card"
        style="text-align:center">

        <h2 style="color:#38bdf8">
            Contact
        </h2>

        <p>

            📞
            <a href="tel:+254781585319"
               style="color:#38bdf8">

                +254781585319

            </a>

            |

            <a href="tel:+254717434943"
               style="color:#38bdf8">

                +254717434943

            </a>

        </p>

    </div>


    <!-- FOOTER -->
    <div style="
        text-align:center;
        padding:20px;
        color:#64748b;
        font-size:13px;
    ">

        © 2026 PESAMATRIX PRO

    </div>

    """)
