from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN = "https://copy-main.onrender.com"


def is_browser():
    ua = request.headers.get("User-Agent", "").lower()
    accept = request.headers.get("Accept", "").lower()

    # 🔥 ถ้าเป็น browser จริง
    if "text/html" in accept:
        return True

    # 🔥 fallback (กันบางเคส)
    if any(x in ua for x in ["chrome", "safari", "firefox", "mozilla"]):
        return True

    return False


@app.route("/")
def root():
    key = request.args.get("key")
    if key != ACCESS_KEY:
        return "403", 403

    # 🔥 ถ้าเป็น browser → เด้ง
    if is_browser():
        return redirect("https://google.com")

    # 🔥 ถ้าเป็น Wiseplay / Player → ผ่าน
    return jsonify({
        "name": "DUFREE",
        "author": "Zank",
        "image": "https://cdn.dufreeapi.uk/dufreedd.png",

        "url": f"{MAIN}/home?key={ACCESS_KEY}",

        "groups": [
            {
                "name": "👉 เข้าสู่ระบบ",
                "url": f"{MAIN}/home?key={ACCESS_KEY}",
                "import": False
            }
        ],

        # 🔥 สำคัญมาก ต้องมี ไม่งั้น Wiseplay บางเครื่องจะไม่โหลด
        "stations": [
            {
                "name": "OK",
                "import": False
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
