import streamlit as st
import pandas as pd
import joblib

# diabetes_app.py


# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS for light styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f9;
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #2c3e50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("🧠 Diabetes Prediction App")
st.markdown("This is a **machine learning app** that predicts diabetes risk based on your health details.")

# Load ML model
model = joblib.load("diabetes_model.pkl")

# 👤 User Info Section
with st.expander("🧑 Personal Info", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        user_name = st.text_input("👤 Your Name")
    with col2:
        user_age = st.slider("🎂 Your Age", 10, 100, 25)

    if user_name:
        st.success(f"👋 Hello, {user_name}!")

# 📁 Upload CSV File
with st.expander("📂 Upload a CSV File"):
    file = st.file_uploader("Upload your data (CSV only)", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.write("✅ File Contents:")
        st.dataframe(df)

# 🖼️ Image & 🎵 Audio
with st.expander("🎵 Media Section"):
    st.image("cat.jpg", caption="Here's a cat to brighten your day 😺", use_container_width=True)
    st.audio("abc.mp3", format="audio/mp3")

# 🔍 Prediction Input Section
st.markdown("---")
st.header("🩺 Enter Health Info for Prediction")

col1, col2 = st.columns(2)
with col1:
    age = st.slider("📅 Age", 10, 100, 30)
    bmi = st.slider("⚖️ BMI (Body Mass Index)", 10.0, 45.0, 22.5)
    glucose = st.slider("🩸 Glucose Level", 70, 200, 100)
with col2:
    bp = st.slider("💓 Blood Pressure", 50, 180, 90)
    insulin = st.slider("💉 Insulin Level", 15, 276, 80)
    skin_thickness = st.slider("📏 Skin Thickness", 7, 99, 20)

# 🧠 Prediction
if st.button("🚀 Predict"):
    input_data = [[age, bmi, glucose, bp, insulin, skin_thickness]]
    prediction = model.predict(input_data)
    result = "🔴 Positive (Diabetic)" if prediction[0] == 1 else "🟢 Negative (Not Diabetic)"
    st.success(f"Prediction Result: **{result}**")

    with st.expander("ℹ️ How to Interpret"):
        st.markdown("""
        - **High Glucose & BMI** can increase diabetes risk.
        - **Older Age** and **low insulin sensitivity** also contribute.
        - This model is based on simulated data and should not replace professional medical advice.
        """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and Machine Learning")
