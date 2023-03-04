import streamlit as st
import pickle

st.write('Это моя попытка освоить Srteamlit')

def load ():
    with open ('best_model.pcl', 'rb') as fid:
        return pickle.load(fid)

age = st.slider('Укажите ваш возраст в днях', 15, 80, key = 'age')
gender = st.slider('Укажите ваш пол', 1, 2, key = 'gender')
height = st.slider('Укажите ваш рост', 50, 250, key = 'height')
weight = st.slider('Укажите вес', 30, 300, key = 'weight')
ap_hi = st.slider('Давление сист', 30, 300, key = 'ap_hi')
ap_lo = st.slider('Давление дисист', 30, 300, key = 'ap_lo')
cholesterol = st.selectbox('Холестерин', [1, 2, 3], key = 'cholesterol')
gluc = st.selectbox('Глюкоза', [1, 2, 3], key = 'gluc')
smoke = st.checkbox('Курит', key = 'smoke')
alco = st.checkbox('Выпивает', key = 'alco')
active = st.checkbox('Ведет активный образ жизни', key = 'active')

model = load()

pred = model.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])