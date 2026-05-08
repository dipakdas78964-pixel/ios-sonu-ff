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
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IOS SONU FF VIP PROXY</title>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Orbitron',sans-serif;
}

body{
background:url('https://images.unsplash.com/photo-1542751110-97427bbecf20?q=80&w=1200&auto=format&fit=crop') no-repeat center center fixed;
background-size:cover;
min-height:100vh;
overflow:hidden;
color:white;
}

.bg{
position:fixed;
width:100%;
height:100%;
background:rgba(0,0,0,0.72);
backdrop-filter:blur(4px);
}

.particles{
position:absolute;
width:100%;
height:100%;
overflow:hidden;
}

.particles span{
position:absolute;
display:block;
width:4px;
height:4px;
background:#ffd700;
border-radius:50%;
animation:animate 15s linear infinite;
}

@keyframes animate{
0%{
transform:translateY(100vh) scale(0);
opacity:0;
}
50%{
opacity:1;
}
100%{
transform:translateY(-10vh) scale(1);
opacity:0;
}
}

.container{
position:relative;
z-index:10;
display:flex;
justify-content:center;
align-items:center;
min-height:100vh;
padding:20px;
}

.card{
width:100%;
max-width:430px;
background:rgba(0,0,0,0.55);
border:2px solid rgba(255,215,0,0.4);
border-radius:30px;
padding:30px;
backdrop-filter:blur(15px);
box-shadow:0 0 50px rgba(255,215,0,0.4);
animation:glow 2s infinite alternate;
}

@keyframes glow{
from{
box-shadow:0 0 20px rgba(255,215,0,0.3);
}

to{
box-shadow:0 0 60px rgba(255,215,0,0.8);
}
}

.logo{
width:140px;
display:block;
margin:auto;
margin-bottom:15px;
filter:drop-shadow(0 0 15px gold);
}

.title{
text-align:center;
font-size:32px;
color:#ffd700;
margin-bottom:10px;
text-shadow:0 0 15px gold;
}

.sub{
text-align:center;
color:#ccc;
font-size:13px;
margin-bottom:20px;
}

.live{
text-align:center;
padding:12px;
border-radius:15px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,215,0,0.3);
margin-bottom:15px;
}

.clock{
text-align:center;
margin-bottom:15px;
color:#00ffcc;
font-size:14px;
}

input{
width:100%;
padding:16px;
border:none;
border-radius:15px;
background:rgba(255,255,255,0.08);
margin-top:15px;
color:white;
font-size:15px;
outline:none;
border:1px solid rgba(255,255,255,0.08);
}

button{
width:100%;
padding:16px;
border:none;
border-radius:15px;
margin-top:18px;
background:linear-gradient(45deg,#ffd700,#ff9900);
font-size:17px;
font-weight:bold;
color:black;
cursor:pointer;
transition:0.3s;
}

button:hover{
transform:scale(1.03);
box-shadow:0 0 20px gold;
}

.result{
margin-top:20px;
padding:18px;
border-radius:18px;
background:rgba(255,255,255,0.05);
text-align:center;
}

.ok{
color:#00ff66;
font-size:22px;
}

.bad{
color:#ff3b3b;
font-size:22px;
}

.btn{
display:block;
text-decoration:none;
text-align:center;
padding:14px;
border-radius:14px;
margin-top:14px;
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
background:#ff0055;
color:white;
}

.footer{
margin-top:18px;
text-align:center;
font-size:12px;
color:#aaa;
}

</style>
</head>
<body>

<div class="bg"></div>

<div class="particles">
<span style="left:10%;animation-delay:0s"></span>
<span style="left:20%;animation-delay:2s"></span>
<span style="left:30%;animation-delay:4s"></span>
<span style="left:40%;animation-delay:6s"></span>
<span style="left:50%;animation-delay:8s"></span>
<span style="left:60%;animation-delay:10s"></span>
<span style="left:70%;animation-delay:12s"></span>
<span style="left:80%;animation-delay:14s"></span>
<span style="left:90%;animation-delay:16s"></span>
</div>

<audio autoplay loop>
<source src="https://files.catbox.moe/8jv5gk.mp3" type="audio/mpeg">
</audio>

<script>
window.onload=function(){
let msg=new SpeechSynthesisUtterance('Welcome to IOS SONU FF Proxy');
msg.volume=1;
msg.rate=0.9;
msg.pitch=1;
speechSynthesis.speak(msg);
}

function updateClock(){
const now=new Date();
document.getElementById('clock').innerHTML=now.toLocaleString();
}

setInterval(updateClock,1000);
</script>

<div class="container">
<div class="card">

<img class="logo" src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png">

<div class="title">IOS SONU FF</div>
<div class="sub">ULTIMATE VIP KEY ACTIVATION PROXY</div>

<div class="clock" id="clock"></div>

<div class="live">
🌐 YOUR NETWORK IP: {{ip}}
</div>

<form method="POST">
<input type="text" name="key" placeholder="ENTER PREMIUM KEY" required>
<button type="submit">VERIFY & ACTIVATE</button>
</form>

{% if status %}
<div class="result">
<h2 class="{{cls}}">{{status}}</h2>
<p>{{msg}}</p>
</div>
{% endif %}

<a class="btn tg" href="https://t.me/+3kZ0sxFfDZAwODM1">📢 JOIN TELEGRAM CHANNEL</a>

<a class="btn admin" href="https://t.me/SONUSELLOR11">👤 CONTACT ADMIN</a>

<div class="footer">
OWNER: SONU SELLOR | IOS SONU FF VIP SYSTEM
</div>

</div>
</div>

</body>
</html>

"""

@app.route('/', methods=['GET','POST'])
def home():

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    status = ''
    msg = ''
    cls = ''

    if request.method == 'POST':

        key = request.form.get('key')

        data = load()

        if key in data:

            info = data[key]

            if info['status'] == 'deleted':

                status = '❌ KEY DELETED'
                msg = 'THIS KEY HAS BEEN REMOVED'
                cls = 'bad'

            else:

                exp = datetime.fromisoformat(info['expire'])
                now = datetime.now()

                if now > exp:

                    status = '⌛ KEY EXPIRED'
                    msg = 'YOUR KEY TIME IS OVER'
                    cls = 'bad'

                else:

                    remain = exp - now

                    status = '✅ KEY ACTIVE'
                    msg = f'REMAINING TIME: {remain}'
                    cls = 'ok'

        else:

            status = '❌ INVALID KEY'
            msg = 'KEY NOT FOUND'
            cls = 'bad'

    return render_template_string(
        HTML,
        ip=ip,
        status=status,
        msg=msg,
        cls=cls
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
