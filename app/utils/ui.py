def layout(content):

    return f"""
    <html>
    <head>
        <style>

            body {{
                background:#0b1220;
                font-family:Arial;
                color:white;
                margin:0;
                padding:20px;
            }}

            .card {{
                background:#111a2e;
                padding:20px;
                margin:10px auto;
                border-radius:12px;
                max-width:500px;
                box-shadow:0 0 10px rgba(0,0,0,0.3);
            }}

            input {{
                width:100%;
                padding:10px;
                margin:5px 0;
                border-radius:6px;
                border:none;
            }}

            button {{
                cursor:pointer;
            }}

            a {{
                text-decoration:none;
            }}

        </style>
    </head>

    <body>
        {content}
    </body>
    </html>
    """
