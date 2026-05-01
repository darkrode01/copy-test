from flask import Flask, request, jsonify

app = Flask(__name__)

ACCESS_KEY = "abc123"

# 🔥 ใส่ลิงก์ MAIN ของคุณ
MAIN_DOMAIN = "https://dufree-main.onrender.com"

@app.route("/")
def root():
    key = request.args.get("key")
    if key != ACCESS_KEY:
        return "Unauthorized", 403

    return jsonify({
        "name": "DUFREE",
        "author": "Zank",

        # 🔥 ให้ Wiseplay กระโดดไป MAIN
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
