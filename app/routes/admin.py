@admin_bp.route("/admin/dashboard")
@admin_required
def admin_dashboard():

    conn = sqlite3.connect(current_app.config["DATABASE"])
    cur = conn.cursor()

    users = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    payments = cur.execute("SELECT COUNT(*) FROM payments").fetchone()[0]
    signals = cur.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    content = cur.execute("SELECT COUNT(*) FROM content").fetchone()[0]

    conn.close()

    return layout(f"""

    <div style="padding:20px">

        <h1 style="color:#38bdf8">🛠 SaaS Admin Panel</h1>

        <div class="grid">

            <div class="stat-card">
                <h2>{users}</h2>
                <p>👤 Users</p>
            </div>

            <div class="stat-card">
                <h2>{payments}</h2>
                <p>💳 Payments</p>
            </div>

            <div class="stat-card">
                <h2>{signals}</h2>
                <p>📊 Signals</p>
            </div>

            <div class="stat-card">
                <h2>{content}</h2>
                <p>📁 Content</p>
            </div>

        </div>

        <br><br>

        <div class="card">
            <h3>⚡ Quick Actions</h3>

            <a href="/admin/users">👥 Manage Users</a><br><br>
            <a href="/admin/payments">💳 Payments</a><br><br>
            <a href="/admin/signals">📊 Trades</a><br><br>
            <a href="/admin/content">📁 Media</a><br><br>

            <a href="/logout" style="color:red">Logout</a>
        </div>

    </div>

    """)
