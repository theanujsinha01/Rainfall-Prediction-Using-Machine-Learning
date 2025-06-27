# Rainfall-Prediction-Using-Machine-Learning
This project predicts whether it will rain or not based on weather features like pressure, humidity, dew point, cloud cover, sunshine, wind direction, and wind speed.  We use a Random Forest Classifier, a popular ML algorithm, trained on historical weather data. The model learns patterns and helps us forecast rain chances.
This project is a **web-based application** that predicts whether it will rain today based on real-world weather input features like pressure, humidity, cloud cover, sunshine, etc. It uses a **Random Forest Classifier** trained on historical weather data and is deployed as an interactive **Streamlit app**.

---

## 📌 Problem Statement

Predicting rainfall is crucial in weather forecasting. It helps:
- Farmers plan irrigation and harvesting.
- People manage daily travel plans.
- Cities prepare for flood alerts or water conservation.

Traditional methods require large infrastructure, but machine learning can make accurate predictions from past weather patterns.

---

## 🎯 Objective

To build a machine learning model that:
- Takes weather features as input.
- Predicts whether it will rain or not.
- Provides results through a simple and user-friendly web app.

---

## 📊 Features of the App

✅ Predicts Rain or No Rain  
✅ Easy-to-use UI built with **Streamlit**  
✅ Takes 7 weather parameters as input  
✅ Displays prediction with icons: ☀️ / 🌧️  
✅ Trained using **Random Forest Classifier**  
✅ Model saved and loaded using **joblib**

---

## 🧪 Input Features Used for Prediction

| Feature         | Description                   |
|----------------|-------------------------------|
| `pressure`      | Atmospheric pressure (hPa)     |
| `dewpoint`      | Dew point temperature (°C)     |
| `humidity`      | Relative humidity (%)          |
| `cloud`         | Cloud cover (%)                |
| `sunshine`      | Sunshine duration (hours)      |
| `winddirection` | Wind direction in degrees (°)  |
| `windspeed`     | Wind speed in km/h             |

---

## 🧠 Machine Learning Model

- **Algorithm Used**: `RandomForestClassifier` (from Scikit-learn)
- **Model Training Steps**:
  - Data Preprocessing
  - Train-Test Split
  - Feature Selection
  - Model Tuning with GridSearchCV
- **Evaluation Metrics**:
  - Accuracy
  - Confusion Matrix
  - Classification Report
- **Model Deployment**:
  - Saved as `.pkl` file using `joblib`
  - Loaded into the Streamlit app for prediction

---

## 🛠️ Tech Stack

| Tool/Library    | Purpose                      |
|----------------|-------------------------------|
| Python          | Programming Language          |
| Pandas & NumPy  | Data handling and processing  |
| Scikit-learn    | Machine Learning model        |
| Matplotlib & Seaborn | Data Visualization       |
| Joblib          | Model saving/loading          |
| Streamlit       | Web App frontend              |

---


