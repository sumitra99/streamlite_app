import streamlit as st
import pandas as pd
st.title("APPLICATION")
df=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.write(df)
