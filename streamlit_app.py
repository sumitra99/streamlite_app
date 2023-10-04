import streamlit as st
import pandas as pd
st.title("APPLICATION")
df=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.write(df)

st.sidebar.header("options")
options_form = st.sidebar.form("options_form")
user_name=options_form.text_input("Name")
user_age=options_form.text_input("Age")
add_data=options_form.form_submit_button()
if add_data:
  st.write(user_name,user_age)
  new_data={"name":user_name, "age":int(user_age)}
  st.write(new_data)
  df=df.append(new_data,ignore_index=true)
  st.write(df)
