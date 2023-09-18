import streamlit as st
import pandas as pd
st.title("Data used")


def load_data():
    return pd.read_csv('cleaned_data.csv')

data = load_data()
st.write(data)