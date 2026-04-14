from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>ImageStream Demo 🚀</h1>
    <p>Version: {os.environ.get('APP_VERSION', '1.0')}</p>
    """

@app.route('/health')
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)