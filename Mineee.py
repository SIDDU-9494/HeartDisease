import pickle
import streamlit as st
pickle_in=open('Predicts.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('')
if st.button('Health'):
  rs=model.predict([[e]]).squeeze()
  st.success(f'Health is {rs}')
