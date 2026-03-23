import requests

url = "https://your-app.onrender.com/predict"

data = {
    "failed_logins": 5,
    "login_frequency": 8,
    "ip_risk_score": 0.9,
    "geo_distance": 3000,
    "time_anomaly": 0.8
}

response = requests.post(url, json=data)
print(response.json())