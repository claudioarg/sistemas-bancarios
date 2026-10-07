import os
import json
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    # Try serving from static first, then from root if needed
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(path):
        return send_from_directory(".", path)
    return send_from_directory(app.static_folder, "index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "sistemas-bancarios"})

@app.route("/api/data")
def api_data():
    try:
        with open(os.path.join(app.static_folder, "static_data.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Iniciando servidor en http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
