from flask import Blueprint
from app.utils.ui import layout

landing_bp = Blueprint("landing", __name__)


# =========================
# HOME PAGE
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
               style="color:white;margin-right:15px;text-decoration:none">
                Login
            </a>

            <a href="/register"
               style="color:#38bdf8;text-decoration:none">
                Register
            </a>
        </div>

    </div>


    <!-- HERO -->
    <div class="card" style="text-align:center;padding:60px 20px">

        <h1 style="font-size:42px;color:#38bdf8;margin-bottom:10px">
            PRO TRADING SIGNALS PLATFORM
        </h1>

        <p style="font-size:18px;color:#cbd5e1">
            Get high accuracy Forex & Crypto signals in real-time
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
            <h3>📊 Daily Signals</h3>
            <p>High accuracy trading setups delivered daily</p>
        </div>

        <div class="card">
            <h3>🔒 Premium Access</h3>
            <p>Unlock full signals after subscription</p>
        </div>

        <div class="card">
            <h3>⚡ Fast Updates</h3>
            <p>Real-time market alerts and entries</p>
        </div>

    </div>


    <!-- HOW IT WORKS -->
    <div class="card">

        <h2 style="color:#38bdf8;text-align:center">
            How It Works
        </h2>

        <div style="line-height:2;text-align:center">

            1. Register an account<br>
            2. Pay subscription via Paybill <b>322372</b><br>
            3. Use your account number as reference<br>
            4. Wait for admin approval<br>
            5. Access premium signals instantly

        </div>

    </div>


    <!-- PRICING -->
    <div class="card">

        <h2 style="color:#38bdf8;text-align:center">
            Subscription Plans
        </h2>

        <div style="text-align:center;line-height:2">

            <b>Daily Plan</b> - Affordable access<br>
            <b>Weekly Plan</b> - Best value<br>
            <b>Monthly Plan</b> - Professional traders

        </div>

    </div>


    <!-- ABOUT US (NEW SECTION) -->
    <div class="card">

        <h2 style="color:#38bdf8;text-align:center">
            About Us
        </h2>

        <p style="text-align:center;color:#cbd5e1;line-height:1.8">

            PESAMATRIX PRO is a professional trading signals platform
            designed to help traders make smarter and faster decisions in
            Forex and Crypto markets.<br><br>

            Our team focuses on market analysis, price action strategies,
            and high-probability setups to deliver accurate signals in real time.<br><br>

            We aim to empower traders in Kenya and globally with
            consistent, transparent, and data-driven trading insights.

        </p>

    </div>


    <!-- PAYMENT INFO -->
    <div class="card" style="text-align:center">

        <h2 style="color:#38bdf8">
            Payment Details
        </h2>

        <p>💰 Paybill: <b>322372</b></p>
        <p>📌 Account Number: Your registration account number</p>

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
               TikTok Profile
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
        © 2026 PESAMATRIX PRO — All Rights Reserved
    </div>

    """)
