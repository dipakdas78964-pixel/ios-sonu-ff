from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

VALID_KEYS = {
    "IOS-SONU-FF-X7A92K": 7
}

@app.route("/", methods=["GET", "POST"])
def home():

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    status = None

    if request.method == "POST":

        key = request.form.get("key")

        if key in VALID_KEYS:

            now = datetime.now()
            exp = now + timedelta(days=7)

            status = {
                "active": True,
                "key": key,
                "activated": now.strftime("%d %b %Y %I:%M %p"),
                "expires": exp.strftime("%d %b %Y %I:%M %p"),
                "remaining": "7 DAYS"
            }

        else:

            status = {
                "active": False
            }

    return render_template(
        "index.html",
        ip=ip,
        status=status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
