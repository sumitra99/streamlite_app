import streamlit as st
st.title("Form")

with st.form(key='form1'):
Name=st.text_input("Name")

submit_button=st.form_submit_button()


