from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN_DOMAIN = "https://copy-main.onrender.com"

def redirect_browser():
    ua = request.headers.get("User-Agent", "").lower()
    accept = request.headers.get("Accept", "").lower()

    # ✅ อนุญาต player
    if any(x in ua for x in ["wiseplay", "vlc", "exo", "iptv"]):
        return None

    # 🔥 ถ้าเป็น browser → เด้ง
    if "text/html" in accept or "mozilla" in ua:
        return redirect("https://i.pinimg.com/originals/04/98/67/049867e9ccd2b0ad0deae212fa9f2240.jpg")  # 👈 เปลี่ยนเว็บได้

    return None


@app.route("/")
def root():
    key = request.args.get("key")

    if key != ACCESS_KEY:
        return "Unauthorized", 403

    # 🔥 ใส่ตรงนี้
    r = redirect_browser()
    if r:
        return r

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
