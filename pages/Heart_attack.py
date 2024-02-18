import streamlit as st

import os
import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Heart attack checker",
    page_icon="❤️️",
)

st.divider()
st.title("Program that predicts whether or not you are prone to a heart attack based on the input data")
st.text("Fill out the form below")

# Load model from file
HA_model = load(f"{os.getcwd()}/models/RF_model_heart_attack.joblib")

# Dictionary for chest pain type values
cp_dict = {
    "typical angina": 0,
    "atypical angina": 1,
    "non-anginal pain": 2,
    "asymptomatic": 3
}
# Dictionary for resting electrocardiographic results
restecg_dict = {
    "normal": 0,
    "having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)": 1,
    "showing probable or definite left ventricular hypertrophy by Estes' criteria": 2
}
# column names for dataframe
columns = ["age", "sex", "cp", "trtbps", "chol", "fbs", "restecg", "thalachh", "exng", "oldpeak", "slp", "caa", "thall"]

def heart_attack():

    # input all values
    age = int(st.number_input("Age:", key="age"))
    sex = st.selectbox("Sex:", ("Male", "Female"))
    cp = st.selectbox("Chest Pain type:", cp_dict.keys())
    trtbps = st.number_input("Resting blood pressure (in mm Hg):", key="trtbps")
    chol = st.number_input("Cholestoral in mg/dl fetched via BMI sensor:", key="chol")
    fbs = int(st.checkbox("(Fasting blood sugar) > 120 mg/dl:"))
    restecg = st.selectbox("Resting electrocardiographic results:", restecg_dict.keys())
    thalachh = st.number_input("Maximum heart rate achieved:", key="thalachh")
    exng = int(st.checkbox("Exercise induced angina:"))
    oldpeak = st.number_input("Previous peak:", key='exng')
    slp = st.number_input("Slope:", key="slp")
    caa = st.selectbox("Number of major vessels:", (0,1,2,3,4))
    thall = st.number_input("Thal rate:", key="thall")
    # convert to number some values
    sex = 1 if sex =="Male" else 0
    cp = cp_dict.get(cp)
    restecg = restecg_dict.get(restecg)

    data = [[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]
    row = pd.DataFrame(data, columns=columns)

    scaler = StandardScaler()
    row = scaler.fit_transform(row.values.reshape(-1, 1))
    del scaler
    row = row.T

    predict = HA_model.predict(row)
    result = "More" if predict[0]==1 else "Less"
    st.info(f"Patient's heart attack chance: {result}")

heart_attack()