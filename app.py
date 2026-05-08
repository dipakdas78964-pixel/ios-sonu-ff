from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)

DB_FILE = "database.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

HTML = """

<!DOCTYPE html>
<html>
<head>
<title>IOS SONU FF VIP PROXY</title>

<style>

body{
background:#0d0d0d;
font-family:Arial;
color:white;
text-align:center;
padding:20px;
}

.box{
background:#111;
padding:25px;
border-radius:20px;
box-shadow:0 0 25px gold;
max-width:420px;
margin:auto;
margin-top:40px;
}

.logo{
width:180px;
border-radius:20px;
margin-bottom:20px;
box-shadow:0 0 25px gold;
}

h1{
color:gold;
}

input{
width:90%;
padding:14px;
border:none;
border-radius:12px;
background:#222;
color:white;
font-size:17px;
margin-top:15px;
}

button{
width:95%;
padding:14px;
border:none;
border-radius:12px;
background:gold;
color:black;
font-size:18px;
font-weight:bold;
margin-top:15px;
cursor:pointer;
}

button:hover{
background:white;
}

.info{
margin-top:20px;
background:#1a1a1a;
padding:15px;
border-radius:15px;
}

a{
text-decoration:none;
}

.tgbtn{
display:block;
background:#229ED9;
padding:14px;
border-radius:12px;
margin-top:15px;
color:white;
font-weight:bold;
}

.adminbtn{
display:block;
background:#ff004c;
padding:14px;
border-radius:12px;
margin-top:15px;
color:white;
font-weight:bold;
}

.footer{
margin-top:20px;
color:gray;
font-size:14px;
}

</style>
</head>

<body>

<div class="box">

<img src="https://i.imgur.com/3l4KX5Y.png" class="logo">

<h1>IOS SONU FF VIP PROXY</h1>

<p>WELCOME TO PREMIUM KEY REGISTRATION SERVER</p>

<div class="info">
YOUR IP:
<b>{{ip}}</b>
</div>

<form method="POST">

<input type="text" name="key" placeholder="ENTER YOUR PREMIUM KEY" required>

<button type="submit">VERIFY & ACTIVATE</button>

</form>

{% if status %}

<div class="info">

<h2>{{status}}</h2>

<p>{{message}}</p>

</div>

{% endif %}

<a href="https://t.me/+3kZ0sxFfDZAwODM1">
<div class="tgbtn">
📢 JOIN TELEGRAM CHANNEL
</div>
</a>

<a href="https://t.me/SONUSELLOR11">
<div class="adminbtn">
👤 CONTACT ADMIN
</div>
</a>

<div class="footer">
ADMIN: @SONUSELLOR11
</div>

</div>

</body>
</html>

"""

@app.route("/", methods=["GET", "POST"])
def home():

    ip = request.remote_addr
    status = ""
    message = ""

    if request.method == "POST":

        key = request.form.get("key")

        data = load_db()

        if key in data:

            if data[key]["status"] == "deleted":

                status = "❌ KEY DELETED"
                message = "THIS KEY HAS BEEN REMOVED"

            else:

                status = "✅ KEY ACTIVE"

                message = f"""
KEY SUCCESSFULLY VERIFIED

DAYS: {data[key]['days']}

STATUS: ACTIVE
"""

        else:

            status = "❌ INVALID KEY"
            message = "KEY NOT FOUND"

    return render_template_string(
        HTML,
        ip=ip,
        status=status,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
