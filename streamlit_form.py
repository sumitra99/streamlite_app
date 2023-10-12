import streamlit as st
st.title("Form")
sepal_l = st.slider('Sepal length (cm)', 1.0, 8.0, 0.5)
sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)

st.form(key='form1')
name=st.text_input("Name")
#submit_button=st.form_submit_button(label='signup')
    
def click_button():
    st.session_state.button = not st.session_state.button
st.button('Click me', on_click=click_button)
#submit_button=st.form_submit_button

