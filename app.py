
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("food_waste_model.pkl")

st.title("Food Waste Prediction")
st.write("Enter the details to estimate food waste.")

meals_served = st.number_input("Meals served", min_value=0, value=150)
kitchen_staff = st.number_input("Kitchen staff", min_value=0, value=10)
temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.number_input("Humidity (%)", value=60.0)
day_of_week = st.selectbox("Day of week (Monday=0)", list(range(7)))
special_event = st.selectbox("Special event", [0, 1])
past_waste = st.number_input("Past food waste (kg)", min_value=0.0, value=40.0)
experience = st.selectbox(
    "Staff experience", ["Unknown", "Beginner", "Experienced"]
)
category = st.selectbox(
    "Waste category", ["vegetables", "fruits", "meat", "other"]
)

year = st.number_input("Year", min_value=2000, max_value=2100, value=2026)
month = st.number_input("Month", min_value=1, max_value=12, value=10)
day = st.number_input("Day", min_value=1, max_value=31, value=27)

if st.button("Predict food waste"):
    new_data = pd.DataFrame([{
        "meals_served": meals_served,
        "kitchen_staff": kitchen_staff,
        "temperature_C": temperature,
        "humidity_percent": humidity,
        "day_of_week": day_of_week,
        "special_event": special_event,
        "past_waste_kg": past_waste,
        "staff_experience": experience,
        "waste_category": category,
        "year": year,
        "month": month,
        "day": day
    }])

    try:
        prediction = model.predict(new_data)[0]
        st.success(f"Predicted food waste: {prediction:.2f} kg")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
