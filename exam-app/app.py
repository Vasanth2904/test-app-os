from flask import Flask, jsonify
import os
from config import get_config

app = Flask(__name__)
config = get_config()

@app.route('/')
def home():
    return jsonify({
        "message": "Exam App",
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

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        return "NOT_FOUND"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)