import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.utils import resample
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib 
import streamlit as st


# Title
st.title("🌦️ Rainfall Prediction App")
st.write("Enter weather details to predict rain.")

# Load model using joblib
model = joblib.load("rainfall_prediction_model.pkl")

# User Inputs
pressure = st.number_input("Pressure (hPa)", value=1010.0)
dewpoint = st.number_input("Dew Point (°C)", value=14.0)
humidity = st.number_input("Humidity (%)", value=70)
cloud = st.number_input("Cloud Cover (%)", value=50)
sunshine = st.number_input("Sunshine (hours)", value=5.0)
winddirection = st.number_input("Wind Direction (°)", value=180.0)
windspeed = st.number_input("Wind Speed (km/h)", value=10.0)

# Make dataframe
input_df = pd.DataFrame([{
    "pressure": pressure,
    "dewpoint": dewpoint,
    "humidity": humidity,
    "cloud": cloud,
    "sunshine": sunshine,
    "winddirection": winddirection,
    "windspeed": windspeed
}])

# Predict button
if st.button("Predict ☁️"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("🌧️ Rain is expected today.")
    else:
        st.success("☀️ No rain expected today.")
