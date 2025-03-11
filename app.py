import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
with open('linear_regression_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

# Title of the app
st.title("Student Performance Prediction")

# Description
st.write("This application predicts the student's final grade based on various factors such as gender, attendance rate, study hours, and more.")

# Input fields for the user to enter the data
name = st.text_input("Student's Name", "Prasad")
gender = st.selectbox('Gender', ['Male', 'Female'])
attendance_rate = st.slider('Attendance Rate', min_value=0, max_value=100, value=85)
study_hours = st.slider('Study Hours per Week', min_value=0, max_value=40, value=15)
previous_grade = st.slider('Previous Grade', min_value=0, max_value=100, value=78)
extracurricular_activities = st.selectbox('Extracurricular Activities', ['Low', 'Medium', 'High'])
parental_support = st.selectbox('Parental Support', ['Low', 'Medium', 'High'])

# Mapping categorical variables to numerical values
gender_value = 1 if gender == 'Male' else 0
extracurricular_map = {'Low': 0, 'Medium': 1, 'High': 2}
extracurricular_value = extracurricular_map[extracurricular_activities]
parental_support_map = {'Low': 0, 'Medium': 1, 'High': 2}
parental_support_value = parental_support_map[parental_support]

# Prepare the input data as a DataFrame
data = pd.DataFrame({
    'Gender': [gender_value],
    'AttendanceRate': [attendance_rate],
    'StudyHoursPerWeek': [study_hours],
    'PreviousGrade': [previous_grade],
    'ExtracurricularActivities': [extracurricular_value],
    'ParentalSupport': [parental_support_value]
})

# Scale the data using the loaded scaler
data_scaled = loaded_scaler.transform(data)

# Perform prediction using the loaded model
if st.button('Predict'):
    # Predict the final grade (model output is already in the 0-100 range)
    prediction = loaded_model.predict(data_scaled)

    # Display the result rounded to two decimal places
    st.write(f"Predicted Final Grade for {name}: {prediction[0]:.2f}")
