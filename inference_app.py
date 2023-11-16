# inference_app.py

import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained XGBoost model
# Replace 'your_model_filename.joblib' with the actual filename of your saved model
model = joblib.load("https://github.com/himanshu1698/Rate_My_Resume/model.joblib")

# Streamlit app
st.title("Salary Prediction App")

df = pd.read_csv("https://github.com/himanshu1698/Rate_My_Resume/data.csv")


df1 = pd.read_csv("https://github.com/himanshu1698/Rate_My_Resume/1.csv")

# Sidebar with input features
st.sidebar.header("Enter Job Details:")
job_title = st.sidebar.selectbox("Job Title", df['job_simp'].unique())
location = st.sidebar.selectbox("Location", df['job_state'].unique())
seniority = st.sidebar.selectbox("Seniority", df['Seniority'].unique())

input_data = pd.DataFrame({
    'job_simp': [job_title],
    'job_state': [location],
    'Seniority': [seniority]
})

# One-hot encode categorical columns
input_data = pd.get_dummies(input_data, columns=['job_state','job_simp','Seniority'], prefix=['job_state','job_simp','seniority'])
input_data_encoded = input_data.reindex(columns=df1.columns, fill_value=0)


# Make prediction
prediction = model.predict(input_data_encoded)



# Display the prediction
st.subheader("Predicted Salary:")
st.write(f"Estimated Salary Range: " + "$" + str(prediction[0]-10) + "K- $" +str(prediction[0]+10)+ "K")
