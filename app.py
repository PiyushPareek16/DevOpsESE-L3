from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def health() -> tuple:
    return jsonify({"status": "ok", "app": "weather-monitor"}), 200


@app.get("/weather")
def get_weather() -> tuple:
    # Static placeholder payload; replace with real API integration as needed
    payload = {
        "location": "San Francisco, CA",
        "temperature_c": 20.5,
        "condition": "Clear",
    }
    return jsonify(payload), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


