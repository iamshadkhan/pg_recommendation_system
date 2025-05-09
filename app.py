import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('pg_model.pkl')

st.title("PG Recommendation System")

# UI Inputs
location = st.selectbox("Select Location", ["Gurgaon", "Delhi", "Noida"])
gender = st.selectbox("Gender Preference", ["Men-only", "Women-only", "Unisex"])
wifi = st.radio("WiFi Available?", ["Yes", "No"])
food = st.radio("Food Provided?", ["Yes", "No"])

# Mapping inputs to encoded format (you must match this with your training preprocessing)
location_map = {"Gurgaon": 0, "Delhi": 1, "Noida": 2}
gender_map = {"Men-only": 0, "Women-only": 1, "Unisex": 2}
binary_map = {"Yes": 1, "No": 0}

if st.button("Recommend"):
    try:
        input_data = [[
            location_map[location],
            gender_map[gender],
            binary_map[wifi],
            binary_map[food]
        ]]
        prediction = model.predict(input_data)
        st.success(f"Recommended PG Price: ₹{prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
