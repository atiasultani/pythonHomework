# BMI Calculation (Body Mass index)
import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height=st.slider("Enter Your Height in cm : ",100,250,175)
weight=st.slider("Enter Your weight in kg : ",20,270,50)
bmi=weight/((height/100)**2)
st.write(f"Your BMI is : {bmi:.2f}")
st.write("BMI Categories")
st.write("- Underweight : BMI Less than 18.5 ")
st.write("- Normal : BMI between 18.5 to 24.9 ")
st.write("- Overweight : BMI between 25 to 29.9 ")
st.write("- Obesity :  BMI 30 or greater ")



