from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CI/CD"

@app.route("/api/status")
def status():
    return jsonify({
        "project": "CI/CD Pipeline",
        "status": "Backend is running successfully 🚀"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
