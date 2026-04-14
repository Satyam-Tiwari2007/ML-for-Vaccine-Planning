from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    location = data["location"]
    temp = data["temp"]
    holiday = data["holiday"]
    last_week_attendance = data["last_week_attendance"]
    doses_per_vial = data["doses_per_vial"]

    # Delhi historical subdistrict baseline
   location_map = {
    "Rohini": 82,
    "Dwarka": 75,
    "Shahdara": 68,
    "Laxmi Nagar": 72,
    "Saket": 77,
    "Karol Bagh": 70,
    "Najafgarh": 60,
    "Janakpuri": 74
}

    historical_base = location_map.get(location, 70)

    # smarter real-world logic
    weather_penalty = 5 if temp > 38 else 0
    holiday_penalty = 10 if holiday == 1 else 0

    expected_attendance = round(
        (historical_base + last_week_attendance) / 2
        - weather_penalty
        - holiday_penalty
    )

    recommended_doses = math.ceil(expected_attendance * 1.1)
    vials_to_open = math.ceil(recommended_doses / doses_per_vial)

    # simple risk logic
    if expected_attendance < 55:
        wastage_risk = "High"
    elif expected_attendance < 70:
        wastage_risk = "Medium"
    else:
        wastage_risk = "Low"

    return jsonify({
        "expected_attendance": expected_attendance,
        "recommended_doses": recommended_doses,
        "vials_to_open": vials_to_open,
        "wastage_risk": wastage_risk
    })


if __name__ == "__main__":
    app.run(debug=True)