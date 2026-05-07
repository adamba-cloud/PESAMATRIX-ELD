def layout(content):
    return f"""
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                font-family: Arial;
                background: #0b1220;
                color: white;
            }}
            .card {{
                background: #111a2e;
                padding: 20px;
                margin: 20px;
                border-radius: 12px;
            }}
        </style>
    </head>
    <body>

        <div class="nav">
            <!-- navbar -->
        </div>

        <div class="content">
            {content}
        </div>

    </body>
    </html>
    """
