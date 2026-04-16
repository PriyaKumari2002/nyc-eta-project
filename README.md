# 🚕 NYC Ride Demand Predictor

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

## 🌐 Live Demo
👉 **[Click here to view the live app](https://nyc-eta-project-aak5cugjhxqpg2vzmpegm5.streamlit.app/)**

---

## 📌 Project Overview

This end-to-end Data Science project predicts **NYC Uber ride demand** for any given hour, day, and month using real-world Uber trip data (1.5 million+ rides). The project covers the full data science lifecycle — from raw data ingestion and exploratory analysis to model training, REST API development, and cloud deployment.

> **Use case:** Transportation companies like Uber, Lyft, and NYC Taxi & Limousine Commission can use demand forecasting to optimize driver allocation, reduce wait times, and improve customer satisfaction.

---

## 🎯 Key Features

- 📊 **Exploratory Data Analysis** — visualizes ride patterns by hour, weekday, and location
- 🤖 **Machine Learning Model** — Random Forest Regressor with 95% R² accuracy
- 🗺️ **Interactive NYC Map** — plots 10,000+ real Uber pickup locations
- 🔮 **Real-time Predictions** — predicts ride demand for any time input
- 🌐 **REST API** — Flask-based API for programmatic access
- ☁️ **Cloud Deployed** — live on Streamlit Cloud, accessible to anyone

---

## 📂 Project Structure

```
nyc_eta_project/
├── data/                   # Raw dataset (downloaded at runtime)
├── notebooks/              # Jupyter notebooks for EDA
├── src/
│   ├── train.py            # Model training script
│   └── predict.py          # Prediction script
├── models/
│   └── model.pkl           # Saved Random Forest model
├── streamlit_app.py        # Interactive Streamlit dashboard
├── app.py                  # Flask REST API
└── requirements.txt        # Project dependencies
```

---

## 🧠 Machine Learning Details

| Item | Details |
|---|---|
| **Dataset** | Uber NYC Rides (1.5M+ records) |
| **Features** | Month, Day, Weekday, Hour |
| **Target** | Hourly ride demand count |
| **Algorithm** | Random Forest Regressor |
| **MAE** | ~68 rides |
| **R² Score** | 0.95 (95% accuracy) |
| **Train/Test Split** | 80% / 20% |

---

## 📊 Key Insights from EDA

- 🌅 **Morning rush (8-9 AM)** and **evening rush (6-8 PM)** show highest demand
- 🎉 **Friday and Saturday nights** have significantly more rides than weekdays
- 🗽 **Manhattan** has the highest pickup density in all of NYC
- 📉 **4-5 AM** is the lowest demand period across all days

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/jageshwar252/nyc-eta-project.git
cd nyc-eta-project
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit app
```bash
streamlit run streamlit_app.py
```

### 5. Run Flask API
```bash
python app.py
```

---

## 🔌 API Usage

### Get prediction via REST API

```bash
curl "http://127.0.0.1:5000/predict?month=4&day=15&weekday=0&hour=8"
```

### Sample Response

```json
{
  "month": 4,
  "day": 15,
  "weekday": 0,
  "hour": 8,
  "predicted_rides": 782
}
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.12 |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Web Framework** | Flask, Streamlit |
| **Deployment** | Streamlit Cloud |
| **Version Control** | Git, GitHub |

---

## 📈 Results

```
Training size  : 1,747 samples
Testing size   : 437 samples
MAE            : 68.25 rides
R² Score       : 0.95
```

The model achieves **95% accuracy** in predicting hourly ride demand,
making it production-ready for real-world transportation use cases.

---

## 🔮 Future Improvements

- [ ] Add weather data as a feature (rain = more rides)
- [ ] Include NYC events calendar for better predictions
- [ ] Add borough-level demand breakdown
- [ ] Implement XGBoost / LightGBM for better accuracy
- [ ] Add real-time data pipeline with NYC Open Data API
- [ ] Dockerize the application for easier deployment

---

## 👨‍💻 Author

**Priya*
- GitHub: [PriyaKumari2002](https://github.com/PriyaKumari2002)
- Project: [NYC Ride Demand Predictor](https://nyc-eta-project-aak5cugjhxqpg2vzmpegm5.streamlit.app/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project useful, please give it a star!** ⭐