from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker on AWS! Cloudnet calcutta dumdum Welcomes All 2026 WB"

app.run(host='0.0.0.0', port=5000)