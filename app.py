import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Fraser Health Needs Index", layout="wide")
final_df = pd.read_csv("data/final_df.csv")

st.sidebar.title("In this index...")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "View By Map", "View By Group", "Data and Limitations", "Methodology"]
)

st.title("Fraser Health Needs Index")
st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")

if page == "Overview":
    st.subheader("Municipality Ranking")
    cluster_colors = {
    0: "#3498DB",
    1: "#F1C40F",
    2: "#E74C3C",
    3: "#2ECC71"
}
    st.dataframe(
        final_df[['Rank', 'Municipality', 'Need Index']].sort_values('Rank'),
        use_container_width=True
    )

    fig = px.bar(
        final_df.sort_values('Need Index', ascending=False),
        x='Need Index', y='Municipality', color='Cluster_Label',
        title="Need Index by Municipality"
    )
    st.plotly_chart(fig, use_container_width=True)
