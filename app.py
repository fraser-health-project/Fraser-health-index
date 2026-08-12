import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Fraser Health Needs Index")
df = pd.read_csv("data/final_df.csv")
st.dataframe(df)

st.set_page_config(page_title="Fraser Health Needs Index", layout="wide")

st.sidebar.title("Fraser Health Needs Index")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "View By Map", "View By Group", "Data and Limitations", "Methodology"]
)

st.title("Fraser Health Needs Index")
st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")

if page == "Overview":
    st.subheader("Municipality Ranking")
    st.dataframe(
        final_df[['Rank', 'Municipality', 'Need Index', 'Cluster_Label']].sort_values('Rank'),
        use_container_width=True
    )

    fig = px.bar(
        final_df.sort_values('Need Index', ascending=False),
        x='Municipality', y='Need Index', color='Cluster_Label',
        title="Need Index by Municipality"
    )
    st.plotly_chart(fig, use_container_width=True)
