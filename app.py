from flask import Flask, request, render_template_string
import json
import os
from datetime import datetime

app = Flask(__name__)

DB = "database.json"

if not os.path.exists(DB):
    with open(DB, "w") as f:
        json.dump({}, f)

def load():
    with open(DB, "r") as f:
        return json.load(f)

HTML = """

<!DOCTYPE html>
<html>

<head>

<title>IOS SONU FF VIP PROXY</title>

<style>

body{
margin:0;
padding:0;
font-family:Arial;
background:black;
color:white;
background-image:url('https://i.postimg.cc/W1bJ8r9t/wp9764093.jpg');
background-size:cover;
background-position:center;
overflow:hidden;
}

.overlay{
background:rgba(0,0,0,0.85);
min-height:100vh;
padding:20px;
}

.box{
max-width:500px;
margin:auto;
margin-top:40px;
background:rgba(10,10,10,0.95);
border:2px solid gold;
border-radius:25px;
padding:25px;
box-shadow:0 0 40px gold;
animation: glow 2s infinite alternate;
}

@keyframes glow{
from{
box-shadow:0 0 20px gold;
}
to{
box-shadow:0 0 50px orange;
}
}

.logo{
width:230px;
display:block;
margin:auto;
margin-bottom:20px;
}

h1{
text-align:center;
color:gold;
font-size:34px;
}

p{
text-align:center;
color:#ccc;
}

.ip{
background:#111;
padding:14px;
border-radius:14px;
margin-top:15px;
text-align:center;
border:1px solid gold;
}

input{
width:100%;
padding:15px;
margin-top:20px;
border:none;
border-radius:12px;
background:#1c1c1c;
color:white;
font-size:16px;
}

button{
width:100%;
padding:15px;
margin-top:18px;
border:none;
border-radius:12px;
background:gold;
font-size:18px;
font-weight:bold;
cursor:pointer;
transition:0.3s;
}

button:hover{
background:white;
transform:scale(1.03);
}

.result{
margin-top:20px;
background:#111;
padding:20px;
border-radius:18px;
border:1px solid #333;
}

.ok{
color:#00ff66;
font-size:22px;
}

.bad{
color:red;
font-size:22px;
}

.btn{
display:block;
padding:15px;
margin-top:15px;
text-align:center;
border-radius:12px;
text-decoration:none;
font-weight:bold;
transition:0.3s;
}

.btn:hover{
transform:scale(1.03);
}

.tg{
background:#0088cc;
color:white;
}

.admin{
background:#ff004c;
color:white;
}

.footer{
margin-top:20px;
text-align:center;
color:gray;
font-size:14px;
}

</style>

</head>

<body>

<audio autoplay loop>
<source src="https://files.catbox.moe/8jv5gk.mp3" type="audio/mpeg">
</audio>

<script>

window.onload = function () {

let msg = new SpeechSynthesisUtterance(
"Welcome to IOS SONU FF Proxy"
);

msg.volume = 1;

msg.rate = 0.9;

msg.pitch = 1;

speechSynthesis.speak(msg);

}

</script>

<div class="overlay">

<div class="box">

<img class="logo" src="https://i.postimg.cc/3x3QzSGq/Picsart-25-05-09-23-10-34-434.png">

<h1>IOS SONU FF VIP PROXY</h1>

<p>PREMIUM KEY ACTIVATION SERVER</p>

<div class="ip">
YOUR IP: {{ip}}
</div>

<form method="POST">

<input type="text" name="key" placeholder="ENTER YOUR PREMIUM KEY" required>

<button type="submit">
VERIFY & ACTIVATE
</button>

</form>

{% if status %}

<div class="result">

<h2 class="{{cls}}">
{{status}}
</h2>

<p>{{msg}}</p>

</div>

{% endif %}

<a class="btn tg" href="https://t.me/+3kZ0sxFfDZAwODM1">
📢 JOIN TELEGRAM CHANNEL
</a>

<a class="btn admin" href="https://t.me/SONUSELLOR11">
👤 CONTACT ADMIN
</a>

<div class="footer">

ADMIN: @SONUSELLOR11

</div>

</div>

</div>

</body>

</html>

"""

@app.route("/", methods=["GET","POST"])
def home():

    ip = request.remote_addr

    status = ""
    msg = ""
    cls = ""

    if request.method == "POST":

        key = request.form.get("key")

        data = load()

        if key in data:

            info = data[key]

            if info["status"] == "deleted":

                status = "❌ KEY DELETED"
                msg = "THIS KEY HAS BEEN REMOVED"
                cls = "bad"

            else:

                exp = datetime.fromisoformat(info["expire"])

                now = datetime.now()

                if now > exp:

                    status = "⌛ KEY EXPIRED"
                    msg = "YOUR KEY TIME IS OVER"
                    cls = "bad"

                else:

                    remain = exp - now

                    status = "✅ KEY ACTIVE"

                    msg = f"""
Remaining Time:
{remain}

Expire Date:
{exp}
"""

                    cls = "ok"

        else:

            status = "❌ INVALID KEY"
            msg = "KEY NOT FOUND"
            cls = "bad"

    return render_template_string(
        HTML,
        ip=ip,
        status=status,
        msg=msg,
        cls=cls
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
