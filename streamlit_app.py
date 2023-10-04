import streamlit as st
import pandas as pd
st.title("APPLICATION")
df=pd.read_csv("data/names.dsv")
st.table(df)



