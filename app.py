from flask import Flask, request, jsonify

app = Flask(__name__)

ACCESS_KEY = "abc123"

MAIN_DOMAIN = "https://copy-main.onrender.com"  # 👈 ของนาย

@app.route("/")
def root():
    key = request.args.get("key")
    if key != ACCESS_KEY:
        return "403", 403

    return jsonify({
        "name": "DUFREE",
        "author": "Zank",

        # 🔥 ตัวนี้สำคัญ
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
