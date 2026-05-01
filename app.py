from flask import Flask, request, jsonify, redirect, make_response

app = Flask(__name__)

ACCESS_KEY = "abc123"
MAIN = "https://copy-main.onrender.com"


def is_browser():
    accept = request.headers.get("Accept", "").lower()

    # browser จะมี text/html
    return "text/html" in accept


@app.route("/")
def root():
    key = request.args.get("key")
    if key != ACCESS_KEY:
        return "403", 403

    # 👉 browser → เด้ง
    if is_browser():
        return redirect("https://google.com")

    # 👉 wiseplay → ส่ง JSON
    base_json = {
        "name": "DUFREE",
        "author": "Zank",
        "image": "https://cdn.dufreeapi.uk/dufreedd.png",

        # ❌ เอา url ออก
        "groups": [
            {
                "name": "👉 เข้าสู่ระบบ",
                "url": f"{MAIN}/home?key={ACCESS_KEY}",
                "import": False
            }
        ],

        "stations": [
            {
                "name": "OK",
                "import": False
            }
        ]
    }

    # 🔥 บังคับ header
    res = make_response(jsonify(base_json))
    res.headers["Content-Type"] = "application/json"
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
