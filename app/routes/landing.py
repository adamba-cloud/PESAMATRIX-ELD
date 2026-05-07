from flask import Blueprint, render_template_string

landing_bp = Blueprint("landing", __name__)


@landing_bp.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>PESAMATRIX PRO - SaaS Trading Signals</title>
</head>

<body style="margin:0;font-family:Arial;background:#0b1220;color:white">

<!-- NAVBAR -->
<div style="background:#111a2e;padding:15px;display:flex;justify-content:space-between;align-items:center">
    <h2 style="color:#38bdf8">📊 PESAMATRIX PRO</h2>

    <div>
        <a href="/login" style="color:white;margin-right:15px">Login</a>
        <a href="/register" style="color:#38bdf8">Register</a>
    </div>
</div>

<!-- HERO SECTION -->
<div style="text-align:center;padding:60px 20px">
    <h1 style="font-size:40px;color:#38bdf8">PRO TRADING SIGNALS PLATFORM</h1>
    <p style="font-size:18px;color:#ccc">
        Get high accuracy forex & crypto signals in real-time
    </p>

    <br>

    <a href="/register" style="background:#38bdf8;color:black;padding:12px 25px;text-decoration:none;border-radius:5px">
        Get Started
    </a>
</div>

<!-- FEATURES -->
<div style="display:flex;justify-content:center;gap:20px;padding:20px;flex-wrap:wrap">

    <div style="background:#111a2e;padding:20px;width:250px;border-radius:10px">
        📊 Daily Signals<br>
        High accuracy trading setups
    </div>

    <div style="background:#111a2e;padding:20px;width:250px;border-radius:10px">
        🔒 Premium Access<br>
        Unlock after subscription
    </div>

    <div style="background:#111a2e;padding:20px;width:250px;border-radius:10px">
        ⚡ Fast Updates<br>
        Real-time market alerts
    </div>

</div>

<!-- HOW IT WORKS -->
<div style="padding:40px;text-align:center">
    <h2 style="color:#38bdf8">How It Works</h2>

    <p>1. Register an account</p>
    <p>2. Pay subscription (Paybill 322372)</p>
    <p>3. Wait for admin approval</p>
    <p>4. Access premium signals instantly</p>
</div>

<!-- PRICING -->
<div style="text-align:center;padding:40px;background:#111a2e">
    <h2 style="color:#38bdf8">Subscription Plans</h2>

    <p>Daily Plan - Affordable access</p>
    <p>Weekly Plan - Best value</p>
    <p>Monthly Plan - Premium traders</p>
</div>

<!-- PAYMENT INFO -->
<div style="text-align:center;padding:40px">
    <h2 style="color:#38bdf8">Payment Details</h2>

    <p>💰 Paybill: <b>322372</b></p>
    <p>📌 Account Number: Your registered account number</p>
</div>

<!-- CONTACT -->
<div style="text-align:center;padding:40px;background:#111a2e">

    <h2>Contact Us</h2>

    <p>
        📞 <a href="tel:+254781585319" style="color:#38bdf8">+254781585319</a> |
        <a href="tel:+254717434943" style="color:#38bdf8">+254717434943</a>
    </p>

    <p>
        🎵 <a href="https://tiktok.com/@smartgoldsignals" target="_blank" style="color:#38bdf8">
        tiktok.com/@smartgoldsignals
        </a>
    </p>

</div>

<!-- FOOTER -->
<div style="text-align:center;padding:20px;color:#666">
    © 2026 PESAMATRIX PRO - All Rights Reserved
</div>

</body>
</html>
""")
