def layout(content, title="PESAMATRIX"):

    return f"""

    <!DOCTYPE html>
    <html>

    <head>

        <title>{title}</title>

        <meta name="viewport"
              content="width=device-width, initial-scale=1">

        <style>

            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }}

            body {{

                background:
                linear-gradient(
                    135deg,
                    #0f172a,
                    #111827,
                    #1e293b
                );

                color: white;

                padding: 20px;

                min-height: 100vh;
            }}

            .container {{
                max-width: 900px;
                margin: auto;
            }}

            .card {{

                background:
                rgba(255,255,255,0.06);

                border:
                1px solid rgba(255,255,255,0.1);

                backdrop-filter: blur(10px);

                border-radius: 18px;

                padding: 20px;

                margin-bottom: 20px;

                box-shadow:
                0 8px 30px rgba(0,0,0,0.3);

                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-3px);
            }}

            h1, h2, h3 {{
                margin-bottom: 15px;
            }}

            a {{

                display: inline-block;

                padding: 10px 18px;

                border-radius: 10px;

                text-decoration: none;

                background: #38bdf8;

                color: white;

                font-weight: bold;

                transition: 0.3s;
            }}

            a:hover {{
                background: #0ea5e9;
                transform: scale(1.03);
            }}

            input,
            select,
            textarea {{

                width: 100%;

                padding: 14px;

                margin-top: 10px;
                margin-bottom: 15px;

                border: none;

                border-radius: 12px;

                background: rgba(255,255,255,0.08);

                color: white;

                outline: none;

                font-size: 15px;
            }}

            input::placeholder,
            textarea::placeholder {{
                color: #cbd5e1;
            }}

            button {{

                width: 100%;

                padding: 14px;

                border: none;

                border-radius: 12px;

                background:
                linear-gradient(
                    90deg,
                    #06b6d4,
                    #3b82f6
                );

                color: white;

                font-size: 16px;

                font-weight: bold;

                cursor: pointer;

                transition: 0.3s;
            }}

            button:hover {{

                opacity: 0.9;

                transform: scale(1.02);
            }}

            .success {{

                background:
                rgba(34,197,94,0.2);

                border:
                1px solid #22c55e;

                color: #86efac;

                padding: 12px;

                border-radius: 10px;

                margin-bottom: 20px;
            }}

            .danger {{

                background:
                rgba(239,68,68,0.2);

                border:
                1px solid #ef4444;

                color: #fca5a5;

                padding: 12px;

                border-radius: 10px;

                margin-bottom: 20px;
            }}

            .warning {{

                background:
                rgba(245,158,11,0.2);

                border:
                1px solid #f59e0b;

                color: #fcd34d;

                padding: 12px;

                border-radius: 10px;

                margin-bottom: 20px;
            }}

            .grid {{

                display: grid;

                grid-template-columns:
                repeat(auto-fit, minmax(220px,1fr));

                gap: 20px;
            }}

            .stat-card {{

                background:
                linear-gradient(
                    135deg,
                    #1d4ed8,
                    #06b6d4
                );

                padding: 25px;

                border-radius: 18px;

                text-align: center;

                box-shadow:
                0 8px 25px rgba(0,0,0,0.25);
            }}

            .stat-card h2 {{
                font-size: 35px;
                margin-bottom: 10px;
            }}

            .badge {{

                display: inline-block;

                padding: 6px 12px;

                border-radius: 999px;

                font-size: 13px;

                font-weight: bold;
            }}

            .running {{
                background: #22c55e;
                color: white;
            }}

            .upcoming {{
                background: #f59e0b;
                color: white;
            }}

            .expired {{
                background: #ef4444;
                color: white;
            }}

            img, video {{

                width: 100%;

                border-radius: 14px;

                margin-top: 10px;
            }}

            @media(max-width:600px) {{

                body {{
                    padding: 12px;
                }}

                .card {{
                    padding: 16px;
                }}

            }}

        </style>

    </head>

    <body>

        <div class="container">

            {content}

        </div>

    </body>

    </html>

    """
