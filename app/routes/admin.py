def layout(content, title="Admin Panel"):

    return f"""
<!DOCTYPE html>
<html>
<head>

    <title>{title}</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>

        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b1220;
            color: white;
        }}

        .container {{
            display: flex;
            min-height: 100vh;
        }}

        /* SIDEBAR */
        .sidebar {{
            width: 250px;
            background: #0f172a;
            padding: 20px;
        }}

        .sidebar h2 {{
            color: #38bdf8;
            margin-bottom: 30px;
        }}

        .sidebar a {{
            display: block;
            padding: 12px;
            margin-bottom: 10px;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
        }}

        .sidebar a:hover {{
            background: #38bdf8;
        }}

        /* MAIN */
        .main {{
            flex: 1;
            padding: 25px;
        }}

        .card {{
            background: rgba(255,255,255,0.06);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
        }}

        .stat-card {{
            background: linear-gradient(135deg, #2563eb, #06b6d4);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }}

        .stat-card h2 {{
            margin: 0;
            font-size: 28px;
        }}

        .badge {{
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
        }}

        .running {{ background: #22c55e; }}
        .upcoming {{ background: #f59e0b; }}
        .expired {{ background: #ef4444; }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th, td {{
            padding: 10px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}

        button {{
            padding: 8px 12px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }}

        .approve {{
            background: #22c55e;
            color: white;
        }}

        .reject {{
            background: #ef4444;
            color: white;
        }}

        @media(max-width: 768px) {{
            .sidebar {{
                width: 100px;
            }}

            .sidebar a {{
                font-size: 12px;
                padding: 8px;
            }}
        }}

    </style>

</head>

<body>

<div class="container">

    <!-- SIDEBAR -->
    <div class="sidebar">

        <h2>⚙ Admin</h2>

        <a href="/admin/dashboard">📊 Dashboard</a>
        <a href="/admin/users">👥 Users</a>
        <a href="/admin/payments">💳 Payments</a>
        <a href="/admin/signals">📈 Signals</a>
        <a href="/admin/content">📁 Content</a>
        <a href="/logout" style="color:red;">🚪 Logout</a>

    </div>

    <!-- MAIN -->
    <div class="main">

        {content}

    </div>

</div>

</body>
</html>
"""
