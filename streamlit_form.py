import streamlit as st
st.title("Form")

with st.form(key='form1'):
name=st.text_input("Name")
#slider_val=st.slider("form slider")
submitted=st.form_submit_button()


