import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))



st.title("Medical Cost Prediction")

# User inputs
age = st.number_input("Age", 0, 100, 30)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
bp = st.number_input("Blood Pressure", 60, 200, 120)
chol = st.number_input("Cholesterol", 100, 300, 180)
visits = st.number_input("Hospital Visits", 0, 20, 1)
meds = st.number_input("Medications", 0, 20, 1)

sex = st.selectbox("Sex", ["Male", "Female"])
smoking = st.selectbox("Smoking Status", ["Yes", "No"])
alcohol = st.selectbox("Alcohol Use", ["Yes", "No"])
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
heart = st.selectbox("Heart Disease", ["Yes", "No"])
activity = st.selectbox(
    "Physical Activity Level",
    ["Low", "Medium", "High"]
)

# CREATE RAW INPUT DATAFRAME (NO ENCODING)
input_df = pd.DataFrame([{
    "age": age,
    "bmi": bmi,
    "blood_pressure": bp,
    "cholesterol": chol,
    "hospital_visits": visits,
    "medications": meds,
    "sex": sex,
    "smoking_status": smoking,
    "alcohol_use": alcohol,
    "diabetes": diabetes,
    "heart_disease": heart,
    "physical_activity_level": activity
}])

if st.button("Predict Medical Cost"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Medical Cost: ₹ {prediction:,.2f}")


