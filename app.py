import streamlit as st
import pandas as pd
import joblib
st.title("Simple ML App")
st.write("hhhhhhhhhiiiiiiiiieeeeeeeeeeeeee")
st.write(1234)
if st.button("Click here"):
    st.write("Button clicked!")
age = st.slider("Your age", 0 ,100)
name = st.text_input("Enter your name")
print(name)
file = st.file_uploader("Upload a CSV file")
st.image("cat.jpg")
st.audio("abc.mp3")

#df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
#st.line_chart(df)
#st.bar_chart(df)
#st.area_chart(df)

model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction")
age2 = st.slider("Age", 10, 100)
bmi = st.slider("BMI", 10.0, 40.0)

if st.button("Predict"):
    result = model.predict([[age2, bmi]])
    st.write("Prediction:", result)