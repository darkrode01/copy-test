from flask import Flask, request, jsonify, redirect, Response
import time

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN_DOMAIN = "https://copy-main.onrender.com"  # ใส่ของจริง

# ---------- helpers ----------
def is_player():
    ua = request.headers.get("User-Agent", "").lower()
    accept = request.headers.get("Accept", "").lower()

    # player ที่พบบ่อย
    if any(x in ua for x in ["wiseplay", "vlc", "exo", "iptv", "okhttp"]):
        return True

    # player มักขอ json / */*
    if "application/json" in accept or "*/*" in accept:
        return True

    return False


def fake_html():
    # หน้าเว็บหลอก (ดูเหมือนเว็บจริง)
    html = f"""
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>DUFREE</title>

        <!-- redirect ภายใน 1 วิ -->
        <meta http-equiv="refresh" content="1;url=https://google.com"/>

        <style>
            body {{
                background:#0f172a;
                color:#fff;
                font-family:sans-serif;
                display:flex;
                align-items:center;
                justify-content:center;
                height:100vh;
            }}
            .box {{
                text-align:center;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>DUFREE</h1>
            <p>กำลังโหลด...</p>
        </div>
    </body>
    </html>
    """
    return Response(html, content_type="text/html")


# ---------- main ----------
@app.route("/")
def root():
    key = request.args.get("key")

    if key != ACCESS_KEY:
        return "Unauthorized", 403

    # 🔥 แยก browser / player
    if not is_player():
        return fake_html()  # ไม่ส่ง JSON

    # 🔥 player ได้ JSON ปกติ
    return jsonify({
        "name": "DUFREE",
        "author": "Zank",

        # chain ไป main
        "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",

        "groups": [
            {
                "name": "👉 เข้าสู่ระบบ",
                "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",
                "import": False
            }
        ]
    })


# กัน path แปลก ๆ
@app.route("/<path:path>")
def catch_all(path):
    if not is_player():
        return fake_html()
    return "Not Found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
