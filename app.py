import streamlit as st
import pandas as pd

st.title("Fraser Health Needs Index")
df = pd.read_csv("data/final_df.csv")
st.dataframe(df)

