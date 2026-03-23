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
        data["failed_logins"],
        data["login_frequency"],
        data["ip_risk_score"],
        data["geo_distance"],
        data["time_anomaly"]
    ]).reshape(1, -1)

    pred = model.predict(features)[0]

    return jsonify({
        "result": "ANOMALY" if pred == -1 else "NORMAL"
    })

if __name__ == "__main__":
    app.run()