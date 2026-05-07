from flask import Blueprint
from app.utils.ui import layout

landing_bp = Blueprint("landing", __name__)


@landing_bp.route("/")
def home():

    return layout("""

    <!-- NAVBAR -->
    <div style="
        background:#111a2e;
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
               style="color:white;margin-right:15px;text-decoration:none">
               Login
            </a>

            <a href="/register"
               style="color:#38bdf8;text-decoration:none">
               Register
            </a>
        </div>

    </div>


    <!-- HERO SECTION -->
    <div class="card" style="text-align:center;padding:60px 20px">

        <h1 style="font-size:40px;color:#38bdf8">
            PRO TRADING SIGNALS PLATFORM
        </h1>

        <p style="font-size:18px;color:#ccc">
            Get high accuracy forex & crypto signals in real-time
        </p>

        <br>

        <a href="/register"
           style="
                background:#38bdf8;
                color:black;
                padding:12px 25px;
                text-decoration:none;
                border-radius:5px;
                font-weight:bold;
           ">
           Get Started
        </a>

    </div>


    <!-- FEATURES -->
    <div style="
        display:flex;
        justify-content:center;
        gap:20px;
        padding:20px;
        flex-wrap:wrap;
    ">

        <div class="card" style="width:250px">
            <h3>📊 Daily Signals</h3>
            <p>High accuracy trading setups</p>
        </div>

        <div class="card" style="width:250px">
            <h3>🔒 Premium Access</h3>
            <p>Unlock after subscription</p>
        </div>

        <div class="card" style="width:250px">
            <h3>⚡ Fast Updates</h3>
            <p>Real-time market alerts</p>
        </div>

    </div>


    <!-- HOW IT WORKS -->
    <div class="card" style="text-align:center">

        <h2 style="color:#38bdf8">
            How It Works
        </h2>

        <p>1. Register an account</p>
        <p>2. Pay subscription (Paybill 322372)</p>
        <p>3. Wait for admin approval</p>
        <p>4. Access premium signals instantly</p>

    </div>


    <!-- PRICING -->
    <div class="card" style="text-align:center">

        <h2 style="color:#38bdf8">
            Subscription Plans
        </h2>

        <p>Daily Plan - Affordable access</p>
        <p>Weekly Plan - Best value</p>
        <p>Monthly Plan - Premium traders</p>

    </div>


    <!-- PAYMENT INFO -->
    <div class="card" style="text-align:center">

        <h2 style="color:#38bdf8">
            Payment Details
        </h2>

        <p>💰 Paybill: <b>322372</b></p>
        <p>📌 Account Number: Your registered account number</p>

    </div>


    <!-- CONTACT -->
    <div class="card" style="text-align:center">

        <h2 style="color:#38bdf8">
            Contact Us
        </h2>

        <p>
            📞
            <a href="tel:+254781585319" style="color:#38bdf8">
                +254781585319
            </a>
            |
            <a href="tel:+254717434943" style="color:#38bdf8">
                +254717434943
            </a>
        </p>

        <p>
            🎵
            <a href="https://tiktok.com/@smartgoldsignals"
               target="_blank"
               style="color:#38bdf8">
               tiktok.com/@smartgoldsignals
            </a>
        </p>

    </div>


    <!-- FOOTER -->
    <div style="
        text-align:center;
        padding:20px;
        color:#666;
    ">
        © 2026 PESAMATRIX PRO - All Rights Reserved
    </div>

    """)
