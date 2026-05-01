from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN_DOMAIN = "https://copy-main.onrender.com"

def is_player():
    ua = request.headers.get("User-Agent", "").lower()

    # 🔥 whitelist player (สำคัญมาก)
    players = ["wiseplay", "vlc", "exo", "iptv"]

    return any(p in ua for p in players)


@app.route("/")
def root():
    key = request.args.get("key")
    if key != ACCESS_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    # 🔥 ถ้าไม่ใช่ player → เด้ง
    if not is_player():
        return redirect("https://google.com")

    # 🔥 ถ้าเป็น Wiseplay → ให้ JSON ปกติ
    return jsonify({
        "name": "DUFREE",
        "author": "Zank",
        "image": "https://cdn.dufreeapi.uk/dufreedd.png",

        "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",

        "groups": [
            {
                "name": "👉 เข้าสู่ระบบ",
                "url": f"{MAIN_DOMAIN}/home?key={ACCESS_KEY}",
                "import": False
            }
        ],

        # 🔥 กัน Wiseplay งอแง
        "stations": [
            {
                "name": "✔ Ready",
                "import": False
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
