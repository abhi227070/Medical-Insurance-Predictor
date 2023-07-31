import numpy as np
import pandas as pd
import streamlit as st
import pickle


model = pickle.load(open("medical_insurance_model.pkl",'rb'))
df = pd.read_csv("insurance.csv")

st.title("Medical Insurance Price Predictor")

st.write("Please Fill the following details: ")

age = st.selectbox("Age",list(range(0,101)))
sex = st.selectbox("Sex",df['sex'].unique())
if sex == 'female':
    sex =1
if sex == "male":
    sex = 0
bmi = st.number_input("BMI")
children = st.selectbox("How many children do you have?",list(range(0,16)))
smoker = st.selectbox("Are you a smoker",df['smoker'].unique())
if smoker == "yes":
    smoker = 0
if smoker == 'no':
    smoker = 1
region = st.selectbox("You are from which region",df['region'].unique())
if region == "southeast":
    region = 0
if region == 'southwest':
    region = 1
if region == 'northeast':
    region = 2
if region == 'northwest':
    region = 3
    
if st.button("Predict"):
    
    output = model.predict([[age,sex,bmi,children,smoker,region]])
    
    st.success("Your Medical Insurance will be "+str(np.round(output[0],2))+" rupees.")


