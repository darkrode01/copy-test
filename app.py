from flask import Flask, request, jsonify, Response

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN_DOMAIN = "https://copy-main.onrender.com"  # 🔥 เปลี่ยนเป็น main ของนาย

# ================= ตรวจว่าเป็น player =================
def is_player():
    ua = request.headers.get("User-Agent", "").lower()

    # ✅ อนุญาตเฉพาะ player จริง
    return any(x in ua for x in ["wiseplay", "vlc", "exo", "iptv", "okhttp"])


# ================= หน้าเว็บหลอก =================
def fake_page():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Loading...</title>

        <!-- 🔥 เปลี่ยนเว็บปลายทาง -->
        <meta http-equiv="refresh" content="1;url=https://facebook.com">

        <style>
            body {
                background:#0f172a;
                color:#fff;
                display:flex;
                align-items:center;
                justify-content:center;
                height:100vh;
                font-family:sans-serif;
            }
        </style>
    </head>
    <body>
        <h2>Loading...</h2>
    </body>
    </html>
    """
    return Response(html, content_type="text/html")


# ================= ROOT =================
@app.route("/")
def root():
    key = request.args.get("key")

    if key != ACCESS_KEY:
        return "Unauthorized", 403

    # 🔥 ถ้าไม่ใช่ player → หลอก
    if not is_player():
        return fake_page()

    # 🔥 Wiseplay → JSON
    return jsonify({
        "name": "DUFREE",
        "author": "Zank",

        "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",

        "groups": [
            {
                "name": "👉 เข้าสู่ระบบ",
                "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",
                "import": False
            }
        ]
    })


# ================= กัน path แปลก =================
@app.route("/<path:path>")
def catch_all(path):
    if not is_player():
        return fake_page()
    return "Not Found", 404


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
