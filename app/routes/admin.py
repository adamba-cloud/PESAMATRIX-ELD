return layout(f"""
<div class="card">

    <h1 style="color:#38bdf8">🧑‍💼 ADMIN DASHBOARD</h1>

    <div class="card">👤 Users: {users}</div>
    <div class="card">💳 Payments: {payments}</div>
    <div class="card">📊 Signals: {signals}</div>

    <a href="/admin/users">Manage Users</a><br>
    <a href="/admin/payments">Approve Payments</a><br>
    <a href="/admin/signals">Create Signals</a><br>
    <a href="/logout" style="color:red">Logout</a>

</div>
""")
