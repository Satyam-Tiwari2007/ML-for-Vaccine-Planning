# 💉 Delhi Vaccine Intelligence Dashboard

**AI-powered district-wise vaccine demand forecasting and wastage risk optimization system for Delhi public healthcare centers.**

Developed as a **Data Science + GovTech healthcare intelligence project** using:

* **Random Forest Regressor** for attendance prediction
* **Logistic Regression** for wastage risk classification
* **Delhi HMIS real government dataset** for historical public-health signals
* **Live weather API integration** for real-time temperature-aware forecasting
* **Dynamic district heatmap** for risk intelligence visualization

---

## 📌 Problem Statement

Vaccine sessions in public healthcare centers often face **dose wastage due to incorrect vial opening decisions**.

In Delhi, attendance varies by:

* district
* weather conditions
* holiday schedules
* previous turnout trends
* local healthcare demand

This project helps health officers **predict attendance before the session starts**, estimate the required number of doses, and classify wastage risk.

---

## 🎯 Objectives

* Forecast district-level vaccine attendance
* Reduce vial wastage using optimized dose recommendations
* Use real HMIS historical trends for better district priors
* Integrate live weather for contextual prediction
* Visualize high-risk districts using a live heatmap
* Provide a government-dashboard style decision support system

---

## 🧠 Machine Learning Algorithms Used

### 🌲 1) Random Forest Regressor

Used for **Expected Attendance Prediction**.

### Input Features

* Live temperature
* Holiday flag
* Last week attendance
* Day of week

### Output

* Expected attendance

---

### 📉 2) Logistic Regression

Used for **Wastage Risk Classification**.

### Classes

* Low
* Medium
* High

### Input Features

* Temperature
* Holiday
* Last week attendance
* Predicted attendance

---

## 📂 Dataset Used

### ✅ Real Delhi Government Dataset

* **Delhi HMIS Sub-District Healthcare Data**
* cleaned and transformed into ML-ready format
* district trend proxies extracted from historical indicators

### Additional Features

* Delhi district dropdown priors
* live weather API using Open-Meteo
* manual field override support

---

## 🏗️ Project Architecture

```text
DATA SCIENCE/
│
├── backend/
│   ├── app.py
│   ├── model_train.py
│   ├── clean_delhi_data.py
│   └── models/
│       ├── attendance_model.pkl
│       ├── risk_model.pkl
│       ├── day_encoder.pkl
│       └── risk_encoder.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   ├── vaccination_data.csv
│   ├── delhi_real_vaccine_data.csv
│   └── delhi_cleaned_vaccine_data.csv
│
└── requirements.txt
```

---

## 🌐 Key Features

* 📍 **Delhi district-wise prediction**
* 🌡️ **Live temperature auto-fill by selected district**
* ✍️ **Manual temperature override**
* 📊 **Prediction analytics cards**
* 🗺️ **Dynamic live district risk heatmap**
* 💉 **Dose and vial recommendation engine**
* 🏥 **Government healthcare dashboard UI**
* ⚡ **Portable GitHub-ready project structure**

---

## 🚀 How to Run

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Run backend

```bash
cd backend
python app.py
```

### 3) Open frontend

Open:

```text
frontend/index.html
```

in Chrome.

---

## 📈 Workflow

1. User selects Delhi district
2. Live temperature auto-fills
3. User enters attendance history
4. Backend loads trained ML models
5. Random Forest predicts attendance
6. Logistic Regression predicts wastage risk
7. Dashboard shows doses + vial recommendations
8. Heatmap updates selected district risk color

---

## 🏆 Real-World Use Cases

* Delhi PHCs
* district immunization officers
* vaccine camp planning
* Mission Indradhanush rounds
* school immunization drives
* heatwave-sensitive attendance forecasting
* public health logistics optimization

---

## 🔮 Future Scope

* district trend graphs
* monthly cost savings analytics
* vaccine-type specific forecasting
* geo-spatial GIS Delhi maps
* streamlit / cloud deployment
* integration with CoWIN / HMIS APIs
* anomaly alerts for sudden demand spikes

---

## 👨‍💻 Author

**Satyam Tiwari**
Data Science • Healthcare AI • GovTech Innovation

---

## 🌟 Project Vision

To transform vaccine planning from **manual estimations to AI-driven district intelligence**, helping Delhi public healthcare centers reduce wastage and improve vaccination coverage.
