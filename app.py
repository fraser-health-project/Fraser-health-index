import streamlit as st
import pandas as pd

st.title("Fraser Health Needs Index")
df = pd.read_csv("data/final_df.csv")
st.dataframe(df)

st.set_page_config(page_title="Fraser Health Needs Index", layout="wide")

st.sidebar.title("Fraser Health Needs Index")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "View By Map", "", "Clusters", "Methodology"]
)

st.title("Fraser Health Needs Index")
st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")
