from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model_iforest.pkl")

@app.route("/")
def home():
    return "SOC Monitoring API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([
    0,  # protocol (default tcp)
    data.get("duration", 0),
    data.get("src_bytes", 0),
    data.get("dst_bytes", 0),
    data.get("pkts", 0),
    data.get("conn_rate", 0),
    data.get("failed_logins", 0)
]).reshape(1, -1)

    pred = model.predict(features)[0]

    return jsonify({
        "result": "ANOMALY" if pred == -1 else "NORMAL"
    })

if __name__ == "__main__":
    app.run()
