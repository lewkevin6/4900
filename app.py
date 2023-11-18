import streamlit as st
import joblib
import pandas as pd
import numpy as np

#Loads the desired model/pipeline in for the app to use
def load_pipeline():
    return joblib.load('version_4/app_probability_pipeline.pkl')


def predict(gender, age, hypertension, heart_disease, married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    
    pipeline = load_pipeline()

    flag = True

    if(age <= 0):
        st.error("Age is below 0, please enter a valid age")
        flag = False

    if(avg_glucose_level <= 0):
        st.error("Your average glucose level is below 0, please enter a valid average glucose level")
        flag = False

    if(bmi <= 0):
        st.error("Your bmi is below 0, please enter a valid bmi")
        flag = False
    
    if (hypertension == 'No'):
        hypertension = 0
    elif(hypertension == 'Yes'):
        hypertension = 1

    if (heart_disease == 'No'):
        heart_disease = 0
    elif(heart_disease == 'Yes'):
        heart_disease = 1

    if(work_type == "Government Job"):
        work_type = "Govt_job"

    if(smoking_status == "Formerly smoked"):
        smoking_status = "formerly smoked"

    if(smoking_status == "Never smoked"):
        smoking_status = "never smoked"

    if(smoking_status == "Smokes"):
        smoking_status = "smokes"

    if(work_type == "Self-Employed"):
        work_type = "Self-employed"

    if(work_type == "Never worked"):
        work_type = "Never_worked"


    user_input = {
        "gender": [gender],
        "age": [age],
        "hypertension": [hypertension],
        "heart_disease": [heart_disease],
        "ever_married": [married],
        "work_type": [work_type],
        "Residence_type": [residence_type],
        "avg_glucose_level": [avg_glucose_level],
        "bmi": [bmi],
        "smoking_status": [smoking_status],
    }

    user_input = pd.DataFrame(user_input)

    prediction = pipeline.predict_proba(user_input).any()

    if(flag is True):
        if(prediction >= 0.7): #
            st.success("No Stroke")
        elif(prediction < 0.7):
            st.warning("Stroke")


#Use this in terminal after running: python -m streamlit run c:/Users/lewke/Desktop/4900/app.py
st.title("Stroke Predictor")
gender = st.radio('Gender', ['Male', 'Female'])
age = st.number_input("Enter your age:")
hypertension = st.radio('Hypertension (high blood pressure)', ['Yes', 'No'])
heart_disease = st.radio('History of heart disease?', ['Yes', 'No'])
married = st.radio('Married?', ['Yes', 'No'])
work_type = st.radio('Work type', ['Private', 'Self-Employed', 'Government Job', 'Never worked'])
residence_type = st.radio('Residence type', ['Urban', 'Rural'])
avg_glucose_level = st.number_input("Enter your average glucose level:")
bmi = st.number_input("Enter your BMI: ")
smoking_status = st.radio('Smoking status', ['Never smoked', 'Unknown', 'Formerly smoked', 'Smokes'])

features = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', "bmi", "smoking_status"]


#Submit button
if st.button('Submit'):
    st.write(predict(gender,age,hypertension,heart_disease,married,work_type,residence_type,avg_glucose_level, bmi, smoking_status))
