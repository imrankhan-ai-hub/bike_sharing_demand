import streamlit as st
import pandas as pd
import joblib


# Load saved model and scaler


model = joblib.load("model/gradient_boosting_model.pkl")
scaler = joblib.load("model/scaler.pkl")


# Page

st.set_page_config(
    page_title="Bike Sharing Demand Prediction",
    page_icon="🚲"
)

st.title("🚲 Bike Sharing Demand Prediction")

st.write(
    "Enter the bike-sharing conditions below to predict the total number of rentals."
)


# User Inputs

season = st.selectbox(
    "Season",
    [1, 2, 3, 4]
)

holiday = st.selectbox(
    "Holiday",
    [0, 1]
)

workingday = st.selectbox(
    "Working Day",
    [0, 1]
)

weather = st.selectbox(
    "Weather",
    [1, 2, 3, 4]
)

temp = st.number_input(
    "Temperature",
    value=20.0
)

atemp = st.number_input(
    "Feels-like Temperature",
    value=20.0
)

humidity = st.number_input(
    "Humidity",
    value=60.0
)

windspeed = st.number_input(
    "Wind Speed",
    value=10.0
)

year = st.number_input(
    "Year",
    min_value=2011,
    max_value=2030,
    value=2012
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)



# Prediction

if st.button("Predict Bike Rentals"):

    
    input_data = pd.DataFrame([[
        season,
        holiday,
        workingday,
        weather,
        temp,
        atemp,
        humidity,
        windspeed,
        year,
        month,
        day,
        hour
    ]], columns=[
        "season",
        "holiday",
        "workingday",
        "weather",
        "temp",
        "atemp",
        "humidity",
        "windspeed",
        "year",
        "month",
        "day",
        "hour"
    ])


    # Apply the same scaler used during training
    input_scaled = scaler.transform(input_data)


    # Make prediction
    prediction = model.predict(input_scaled)[0]


    # Rental count cannot be negative
    prediction = max(0, prediction)


    # Display result
    st.success(
        f"Predicted Bike Rentals: {prediction:.0f}"
    )