import streamlit as st
st.title("Form")

with st.form(key='form1'):
Name=st.text_input("Name")
#slider_val=st.slider("form slider")
submit_button=st.form_submit_button()


