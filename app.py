import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("salary_predictor.pkl")

# Title
st.title("💼 Employee Salary Predictor")

st.markdown("""
Enter employee details below to predict their estimated salary using ensemble ML models.
""")

# Input fields
job_title = st.selectbox("Job Title", ['Data Scientist', 'Software Engineer', 'Manager', 'Analyst'])
education = st.selectbox("Education", ['Bachelor', 'Master', 'PhD'])
location = st.selectbox("Location", ['New York', 'San Francisco', 'Remote', 'Other'])
experience = st.slider("Years of Experience", 0, 40, 3)

# Map to encoded values (match with training encoding)
job_map = {'Data Scientist': 0, 'Software Engineer': 1, 'Manager': 2, 'Analyst': 3}
edu_map = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
loc_map = {'New York': 0, 'San Francisco': 1, 'Remote': 2, 'Other': 3}

# Prepare input
features = pd.DataFrame([[
    job_map[job_title],
    edu_map[education],
    loc_map[location],
    experience
]], columns=['job_title', 'education', 'location', 'experience'])

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(features)[0]
    st.success(f"💰 Estimated Salary: ${prediction:,.2f}")