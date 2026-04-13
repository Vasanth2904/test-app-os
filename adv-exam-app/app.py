from flask import Flask, jsonify, request
import os
from config import get_config
from db import get_data, add_data

app = Flask(__name__)
config = get_config()

@app.route('/')
def home():
    return jsonify({
        "app": "Advanced Exam App 🚀",
        "env": config["ENV"],
        "version": config["VERSION"]
    })

@app.route('/health')
def health():
    return "OK", 200

@app.route('/config')
def config_data():
    return jsonify({
        "env_config": os.environ.get("APP_CONFIG"),
        "file_config": read_file("/etc/config/app.conf")
    })

@app.route('/secret')
def secret_data():
    return jsonify({
        "env_secret": os.environ.get("APP_SECRET"),
        "file_secret": read_file("/etc/secret/secret.txt")
    })

@app.route('/data', methods=["GET"])
def data():
    return jsonify(get_data())

@app.route('/data', methods=["POST"])
def add():
    payload = request.json
    add_data(payload)
    return jsonify({"status": "added", "data": payload})

@app.route('/compute/<int:x>')
def compute(x):
    return jsonify({
        "input": x,
        "square": x * x,
        "cube": x * x * x,
        "env_multiplier": x * int(os.environ.get("MULTIPLIER", 2))
    })

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        return "NOT_FOUND"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)