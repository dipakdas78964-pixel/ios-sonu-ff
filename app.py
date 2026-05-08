from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🔥 IOS SONU FF PROXY 🔥</h1>
    <h3>Premium Key Registration Server</h3>
    <p>Server Status: ONLINE</p>
    """
