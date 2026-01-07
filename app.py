import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical Cost Prediction",
    layout="centered"
)

# ---------------- LOAD MODEL (NO CACHE - REQUIRED FIX) ----------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# ---------------- HEADER ----------------
st.title("💊 Medical Cost Prediction")
st.caption("Predict estimated medical cost based on health and lifestyle indicators")

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("🧍 Personal & Health Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 0, 100, 30)
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    bp = st.number_input("Blood Pressure", 60, 200, 120)
    chol = st.number_input("Cholesterol", 100, 300, 180)

with col2:
    visits = st.number_input("Hospital Visits", 0, 20, 1)
    meds = st.number_input("Medications", 0, 20, 1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    activity = st.selectbox(
        "Physical Activity Level",
        ["Low", "Medium", "High"]
    )

st.markdown("---")

# ---------------- LIFESTYLE SECTION ----------------
st.subheader("🚬 Lifestyle & Medical Conditions")

col3, col4 = st.columns(2)

with col3:
    smoking = st.selectbox("Smoking Status", ["Yes", "No"])
    alcohol = st.selectbox("Alcohol Use", ["Yes", "No"])

with col4:
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    heart = st.selectbox("Heart Disease", ["Yes", "No"])

st.markdown("---")

# ---------------- INPUT DATAFRAME ----------------
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

# ---------------- INPUT NORMALIZATION ----------------
def normalize_input(df):
    df = df.copy()
    for col in [
        "sex",
        "smoking_status",
        "alcohol_use",
        "diabetes",
        "heart_disease",
        "physical_activity_level"
    ]:
        df[col] = df[col].str.lower()
    return df

# ---------------- PREDICTION BUTTON ----------------
if st.button("🔮 Predict Medical Cost"):
    input_df = normalize_input(input_df)
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Medical Cost: ₹ {prediction:,.2f}")

# ---------------- FOOTER ----------------
st.markdown(
    "<hr style='border:1px solid #333'>"
    "<center><small>Built with Streamlit & Machine Learning</small></center>",
    unsafe_allow_html=True
)
