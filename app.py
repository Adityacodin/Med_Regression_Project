import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("insurance_premium_model.pkl")

st.title("💰 Insurance Premium Predictor")
st.write("Enter the customer details below to predict the insurance premium:")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])

# Convert inputs to numerical form
sex_num = 1 if sex == "male" else 0
smoker_num = 1 if smoker == "yes" else 0

# Prepare input data
X_new = np.array([[age, sex_num, bmi, children, smoker_num]])

if st.button("Predict"):
    prediction = model.predict(X_new)[0]
    st.success(f"Predicted Insurance Premium: ₹{prediction:,.2f}")
