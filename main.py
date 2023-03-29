import streamlit as st
import pickle 
pickle_in=open('HeartDisease.pkl','rb')
model=pickle.load(pickle_in)

age=st.number_input('enter age')
trestbps=st.number_input('enter trestbps')
chol=st.number_input('enter chol')

if st.button('Predict'):
  disease1=model.predict([[trestbps]])
  disease2=model.predict([[chol]])
  disease=model.predict([[age]])
  st.success(f'Disease predicted is {disease1}')
  st.success(f'Disease predicted is {disease2}')
  st.success(f'Disease predicted is {disease}')
