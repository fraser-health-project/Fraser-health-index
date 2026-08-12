import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap
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
   ranking = final_df.sort_values("Rank")

    cluster_colors = {
    "High-Pressure System (High Demand + Strained Capacity)": "#E74C3C",
    "High Demand + Adequate Capacity": "#F1C40F",
    "Low Demand + Strained Capacity": "#3498DB",
    "Low-Need System": "#2ECC71"
}
st.markdown("""
<style>

.ranking-card {
    border-radius: 18px;
    padding: 24px 28px;
    margin-bottom: 18px;

    background-color: #1E222B;

    border-top: 1px solid #3A3F4B;
    border-right: 1px solid #3A3F4B;
    border-bottom: 1px solid #3A3F4B;

    min-height: 145px;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

.rank-number {
    font-size: 42px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 8px;
}

.municipality-name {
    font-size: 27px;
    font-weight: 700;
    margin-bottom: 8px;
}

.need-score {
    font-size: 17px;
    opacity: 0.85;
}

.cluster-label {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    margin-top: 12px;
}

</style>
""", unsafe_allow_html=True)

ranking = final_df.sort_values("Rank")

for _, row in ranking.iterrows():

    cluster = row["Cluster_Label"]

    # Match the actual cluster name to a color
    cluster_color = cluster_colors.get(cluster, "#808080")

    card = f"""
<div class="ranking-card" style="border-left: 8px solid {cluster_color};">

    <div class="rank-number">
        #{int(row['Rank'])}
    </div>

    <div class="municipality-name">
        {row['Municipality']}
    </div>

    <div class="need-score">
        Need Index: <strong>{row['Need Index']:.4f}</strong>
    </div>

    <div class="cluster-label"
         style="background-color: {cluster_color}; color: white;">
        {cluster}
    </div>

</div>
"""

    st.markdown(
        textwrap.dedent(card),
        unsafe_allow_html=True
    )
   fig = px.bar(
        final_df.sort_values('Need Index', ascending=False),
        x='Need Index', y='Municipality', color='Cluster_Label',
        title="Need Index by Municipality"
    )
    st.plotly_chart(fig, use_container_width=True)
