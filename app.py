from flask import Flask, request, jsonify, Response

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN_DOMAIN = "https://copy-main.onrender.com"

# ================= ตรวจ browser =================
def is_browser():
    ua = request.headers.get("User-Agent", "").lower()
    accept = request.headers.get("Accept", "").lower()

    # 🔥 browser แน่นอน
    if "mozilla" in ua:
        return True

    if "text/html" in accept:
        return True

    return False


# ================= fake page =================
def fake_page():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Loading...</title>
        <meta http-equiv="refresh" content="1;url=https://img1.pic.in.th/images/522674995_4152170111697004_2505366505724440296_n.jpg">
    </head>
    <body style="background:#111;color:#fff;display:flex;align-items:center;justify-content:center;height:100vh;">
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

    # 🔥 ถ้าเป็น browser → หลอก
    if is_browser():
        return fake_page()

    # 🔥 ที่เหลือทั้งหมด = Wiseplay / VLC
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


# ================= fallback =================
@app.route("/<path:path>")
def catch_all(path):
    if is_browser():
        return fake_page()
    return "Not Found", 404


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
