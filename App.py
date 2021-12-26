# pip install streamlit
import streamlit as st
from model import predict
import numpy as np

st.set_page_config(page_title="Survival Prediction App",
                   page_icon="🔫", layout="wide")

feats = ['Age', 'BMI', '3J', 'Ventialted', 'Hearrate', 'Resprate', 'SP02',
       'Temperature', 'Hos_mor', 'ICU_mor']

with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    age = st.slider("Age: ", 20, 100, value=20)
    bmi = st.slider("BMI: ", 20, 100, value=20, format="%d")
    j_3 = st.number_input("apache_3j_diagnosis: ")
    ventilated = st.number_input("Whether the patient was invasively ventilated ?: (0 or 1)")
    
    
    heartrate = st.number_input("Heart_rate: ")
    resprate = st.number_input("Res_rate: ")
    spO2 = st.number_input("SP O2: ")
    Temp = st.number_input("Temp: ")
    
    hos_mor = st.number_input("apache_4a_hospital_death_prob(0 to 1): ")
    icu_mor = st.number_input("apache_4a_hospital_icu_prob(0 to 1): ")
    
    
    
    

    submit_val = st.form_submit_button("Survial Prediction ")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([age, bmi, j_3, ventilated, 
                          heartrate, resprate, spO2, Temp,
                          hos_mor, icu_mor]).reshape(1,-1)


    
    print("attrubutes valid")
    

    value = predict(attributes= attribute)


    st.header("Here are the results:")
    
    if value ==0:
        st.success("Patient will survive")
        
    else:
        st.success("Patient may not survive")
        