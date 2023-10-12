import streamlit as st
import joblib

#streamlit run /workspaces/4900/app.py 
st.title("Stroke Predictor")

#Loads the desired model in for the app to use
def load_model():
    return joblib.load('/workspaces/4900/pipeline_for_app_3.pkl')

gender = st.radio('Gender', ['Male', 'Female'])
age = st.number_input("Enter your age:")
hypertension = st.radio('Hypertension (high blood pressure)', ['Yes', 'No'])
heart_disease = st.radio('History of heart disease?', ['Yes', 'No'])
married = st.radio('Married?', ['Yes', 'No'])
work_type = st.radio('Work type', ['Private', 'Self-Employed', 'Children', 'Government Job', 'Never worked'])
residence_type = st.radio('Residence type', ['Urban', 'Rural'])
avg_glucose_level = st.number_input("Enter your average glucose level:")
bmi = st.number_input("Enter your BMI: ")
smoking_status = st.radio('Smoking status', ['Never smoked', 'Unknown', 'Formerly smoked', 'Smokes'])

#features = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', "bmi", "smoking_status"]
def predict(gender, age, hypertension, heart_disease, married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):
    
    pipeline = load_model()

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

    prediction = pipeline.predict([[gender, age, hypertension, heart_disease, married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])
    
    if(flag is True):
        if(prediction == 0):
            st.success("No Stroke")
        elif(prediction == 1):
            st.warning("Stroke")

#Submit button
if st.button('Submit'):
    st.write(predict(gender,age,hypertension,heart_disease,married,work_type,residence_type,avg_glucose_level, bmi, smoking_status))
