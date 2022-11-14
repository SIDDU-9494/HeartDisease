import pickle
import streamlit as st
pickle_in=open('Predicts.pkl','rb')
model=pickle.load(pickle_in)
ef=st.number_input('Enter heartbeat')
if st.button('Health'):
  rs=model.predict([[ef]]).squeeze()
  st.success(f'Health is {rs}')
