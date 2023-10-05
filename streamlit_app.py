import streamlit as st
import pandas as pd
st.title("EXCEL DATA")
#df=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#st.write(df)


st.sidebar.header("APPLICATION ")
options_form = st.sidebar.form("options_form")
user_fruit=options_form.text_input("Fruit")
user_serving_size=options_form.text_input("Serving_size")
add_data=options_form.form_submit_button()
if add_data:
  st.write(user_fruit,user_serving_size)
  new_data={"fruit":user_fruit, "serving_size":int(user_serving_size)}
  #st.write(new_data)
  #df=df.append(new_data,ignore_index=True)
  #st.write(df)
