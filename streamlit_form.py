import streamlit as st
st.title("Form")

st.form(key='form1')
name=st.text_input("Name")
submit_button=st.form_submit_button()


