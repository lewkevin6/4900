import streamlit as st
import joblib

#streamlit run /workspaces/4900/app.py 
st.title("Make a prediction")

#Loads the desired model in for the app to use
def load_model():
    return joblib.load('model_for_app.pkl')


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
    
    model = load_model()
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

    if(gender == "Male"):
        converted_gender = 1
    elif(gender == "Female"):
        converted_gender = 0

    if(hypertension == "Yes"):
        converted_hypertension = 1
    elif(hypertension == "No"):
        converted_hypertension = 0

    if(heart_disease == "Yes"):
        converted_heart_disease = 1
    elif(heart_disease == "No"):
        converted_heart_disease = 0

    if(married == "Yes"):
        converted_married = 1
    elif(married == "No"):
        converted_married = 0

    if(work_type == "Private"):
        converted_work_type = 0
    elif(work_type == "Self-Employed"):
        converted_work_type = 1
    elif(work_type == "Children"):
        converted_work_type = 2
    elif(work_type == "Government Job"):
        converted_work_type = 3
    elif(work_type == "Never worked"):
        converted_work_type = 4

    if(residence_type == "Rural"):
        converted_residence_type = 0
    elif(residence_type == "Urban"):
         converted_residence_type = 1

    if(smoking_status == "Never smoked"):
        converted_smoking_status = 0
    elif(smoking_status == "Unknown"):
         converted_smoking_status = 1
    elif(smoking_status == "Formerly smoked"):
         converted_smoking_status = 2
    elif(smoking_status == "Smokes"):
         converted_smoking_status = 3

    prediction = model.predict([[converted_gender,age,converted_hypertension,converted_heart_disease,converted_married,converted_work_type,converted_residence_type,avg_glucose_level, bmi, converted_smoking_status]])
    
    if(flag == True):
        if(prediction == 0):
            st.success("No Stroke")
        elif(prediction == 1):
            st.warning("Stroke")

#Submit button
if st.button('Submit'):
    st.write(predict(gender,age,hypertension,heart_disease,married,work_type,residence_type,avg_glucose_level, bmi, smoking_status))
