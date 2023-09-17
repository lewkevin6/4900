import streamlit as st
import joblib
import pandas as pd


#Loads the desired model in for the app to use
def load_model():
    return joblib.load('model_for_app.pkl')

#Loads in the cleaned data
def load_data():
    return pd.read_csv('cleaned_data.csv')


data = load_data()



#Editing the side bar
with st.sidebar:
    st.write("Welcome to the stroke prediction app")
    st.radio('Menu:', ["Predict", "Data used"])



st.radio('Gender', ['Male', 'Female'])



st.write(data)

