import streamlit as st
import joblib
import pandas as pd

st.title("Make a prediction")

#Loads the desired model in for the app to use
def load_model():
    return joblib.load('model_for_app.pkl')

def predict(gender, age, hypertension, heart_diease, married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    if(age < 0):
    st.error("Age is below 0, please enter a valid age")

    if(avg_glucose_level < 0):
    st.error("Your average glucose level is below 0, please enter a valid average glucose level")

    if(bmi < 0):
    st.error("Your bmi is below 0, please enter a valid bmi")


gender = st.radio('Gender', ['Male', 'Female'])
age = st.number_input("Enter your age:")
hypertension = st.radio('Hypertension (high blood pressure)', ['Yes', 'No'])
heart_disease = st.radio('History of heart disease?', ['Yes', 'No'])
married = st.radio('Married?', ['Yes', 'No'])
work_type = st.radio('Work type', ['Private', 'Self-Employed', 'Children', 'Government Job', 'Taking care of children'])
residence_type = st.radio('Residence type', ['Urban', 'Rural'])
avg_glucose_level = st.number_input("Enter your average glucose level:")
bmi = st.number_input("Enter your BMI: ")
smoking_status = st.radio('Smoking status', ['Never smoked', 'Unknown', 'Formerly smoked', 'Smokes'])


st.button("Submit", on_press = predict(gender, age, hypertension, heart_diease, married, work_type, residence_type, avg_glucose_level, bmi, smoking_status))

