import streamlit as st
from functions import AppFunctions


DATA_URL = './assets/data.csv'
core = AppFunctions(DATA_URL)
st.title('Приложение')
p_by_age = st.slider('Год регистрации', 1950, 2023, value=(1950, 2023))
p_name = st.text_input('Бренд:')
filtered_data = core.find_auto(p_name, p_by_age[0], p_by_age[1])
st.dataframe(filtered_data)

