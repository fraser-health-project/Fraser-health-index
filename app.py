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
#Cards
if page == "Overview":

    st.title("Fraser Health Needs Index")

    st.markdown(
        "An interactive tool ranking and grouping hospital "
        "systems' need across the Fraser Health Region."
    )

    st.subheader("Municipality Ranking")

    # Sort municipalities from highest need to lowest need
    ranking = final_df.sort_values("Rank")


    # ========================================================
    # CARD STYLING
    # ========================================================

    st.markdown("""
<style>

.ranking-card {
    background-color: #1E222B;
    border: 1px solid #3A3F4B;
    border-left: 8px solid #E74C3C;
    border-radius: 16px;

    padding: 22px 28px;
    margin-bottom: 16px;

    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
}

.rank-number {
    font-size: 40px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 8px;
}

.municipality-name {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 8px;
}

.need-score {
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True

    for _, row in ranking.iterrows():

        st.markdown(
            f"""<div class="ranking-card">
<div class="rank-number">#{int(row['Rank'])}</div>
<div class="municipality-name">{row['Municipality']}</div>
<div class="need-score">Need Index: <strong>{row['Need Index']:.4f}</strong></div>
</div>""",
            unsafe_allow_html=True
        )
