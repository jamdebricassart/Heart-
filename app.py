import streamlit as st
import pickle

st.header('Расчет риска развития ССЗ с помощью машинного обучения')
st.subheader('Пожалуйста, заполните данные для рассчета риска сердечно-сосудистых заболеваний')

def load ():
    with open ('best_model.pcl', 'rb') as fid:
        return pickle.load(fid)

age = st.slider('Укажите ваш возраст', 15, 80, key = 'age')
gender = st.slider('Укажите ваш пол', 1, 2, key = 'gender')
st.write('1 – мужчина, 2 – женщина')
height = st.slider('Укажите ваш рост', 50, 250, key = 'height')
weight = st.slider('Укажите вес', 30, 300, key = 'weight')
ap_hi = st.slider('Давление сист', 30, 300, key = 'ap_hi')
ap_lo = st.slider('Давление дисист', 30, 300, key = 'ap_lo')
cholesterol = st.selectbox('Холестерин', [1, 2, 3], key = 'cholesterol')
gluc = st.selectbox('Глюкоза', [1, 2, 3], key = 'gluc')
smoke = st.checkbox('Курите ли вы?', key = 'smoke')
alco = st.checkbox('Выпиваете ли вы?', key = 'alco')
active = st.checkbox('Ведете активный образ жизни?', key = 'active')

age = age*365

model = load()

pred = model.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]]) [:,1]
st.subheader('Вероятность развития сердечно-сосудистых заболеваний составляет:')
st.write(pred)