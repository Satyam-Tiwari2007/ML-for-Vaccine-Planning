import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
df = pd.read_csv("../dataset/vaccination_data.csv")

# Convert day_of_week into numbers
encoder = LabelEncoder()
df["day_of_week"] = encoder.fit_transform(df["day_of_week"])

# ==============================
# Attendance Prediction Model
# ==============================
X_attendance = df[["temp", "holiday", "last_week_attendance", "day_of_week"]]
y_attendance = df["expected_attendance"]

attendance_model = RandomForestRegressor(n_estimators=100, random_state=42)
attendance_model.fit(X_attendance, y_attendance)

# ==============================
# Wastage Risk Model
# ==============================
X_risk = df[["temp", "holiday", "last_week_attendance", "expected_attendance"]]
y_risk = df["wastage_risk"]

risk_encoder = LabelEncoder()
y_risk_encoded = risk_encoder.fit_transform(y_risk)

risk_model = LogisticRegression(max_iter=1000)
risk_model.fit(X_risk, y_risk_encoded)

# Save models
os.makedirs("models", exist_ok=True)

joblib.dump(attendance_model, "models/attendance_model.pkl")
joblib.dump(risk_model, "models/risk_model.pkl")
joblib.dump(encoder, "models/day_encoder.pkl")
joblib.dump(risk_encoder, "models/risk_encoder.pkl")

print("Models trained and saved successfully!")