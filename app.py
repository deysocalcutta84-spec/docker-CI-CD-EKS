from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker on AWS! Cloudnet calcutta dumdum Welcome All 2026 West Bengal"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)