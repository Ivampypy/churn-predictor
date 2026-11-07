import sys

sys.path.append(".")

import streamlit as st
import requests
import json
from src.utils.config import cat_cl

st.header(" Main Page for Churn Prediction")
with st.form("Prediction form"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Numerical Parameters")
        num_param = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]

        response_senior = st.selectbox("Senior? (1 - yes, 0 - else): ", [0, 1])
        response_tenure = st.slider(label="Tenure:", max_value=100, min_value=0)
        response_mth_charges = st.slider(
            label="Monthly Charges: ",
            max_value=150.0,
            min_value=0.0,
            value=50.0,
            step=0.01,
            format="%f",
        )
        response_tot_charges = st.slider(
            label="Total Charges",
            max_value=10_000.0,
            min_value=0.0,
            value=1000.0,
            step=0.01,
            format="%f",
        )
    with col2:
        st.subheader("Categorical parameters")
        data = {}
        with open(cat_cl, "r") as f:
            cat_clas = json.load(f)

        for key, values in cat_clas.items():
            response_cat = st.selectbox(f"{key}:", values)
            data[key] = response_cat

    submit_buttn = st.form_submit_button(label="Click to predict")

if submit_buttn:
    data["SeniorCitizen"] = response_senior
    data["tenure"] = response_tenure
    data["MonthlyCharges"] = response_mth_charges
    data["TotalCharges"] = response_tot_charges

    try:
        response = requests.post("https://churn-predictor-0bss.onrender.com/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            probs = result["probability"]
            will_churn = result["will_churn"]

            st.session_state['client_data'] = data
            st.session_state['probability'] = probs
            
            st.divider()

            if will_churn:
                st.warning(f"Attention! High risk of leaving! Probability is {round(probs,2)}!")
            else:
                st.success(f"Everything is good, propability of leaving is too little: it stands at {round(probs,2)}")

        else:
            st.error("Warning! API Error")

    except requests.exceptions.ConnectionError:
        st.error("Connection is poor, reload the uvicorn!")
