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
# Ranking Cards
if page == "Overview":
 st.title("Fraser Health Needs Index")
 st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")
 st.subheader("Municipality Ranking")
 ranking = final_df.sort_values("Rank")
 st.markdown(
    """
    <style>
    .ranking-card {
        background-color: #1E222B;
        border: 1px solid #3A3F4B;
        border-left: 8px solid #E74C3C;
        border-radius: 16px;
        padding: 22px 28px;
        margin-bottom: 16px;
    }

    .rank-number {
        font-size: 40px;
        font-weight: 800;
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
    """,
    unsafe_allow_html=True
)
for _, row in ranking.iterrows():

    card_html = f"""
<div class="ranking-card">
    <div class="rank-number">#{int(row['Rank'])}</div>
    <div class="municipality-name">{row['Municipality']}</div>
    <div class="need-score">
        Need Index: <strong>{row['Need Index']:.4f}</strong>
    </div>
</div>
"""

    st.markdown(card_html,unsafe_allow_html=True)

#Municipal information


# ============================================================
# 2. MUNICIPALITY BLURBS
# ============================================================
# Add/edit your own blurbs here.
# The key MUST exactly match the Municipality name in your dataframe.

municipality_blurbs = {municipality_blurbs = {
    "Surrey": """
    Surrey ranks highly across the index in almost all scenarios, this reflects a combination 
    of it being the highest populated municipality in the Fraser Health Area, along with large demand and access pressures, 
    while having some of the largest medical facilities in the region, including Surrey Memorial and Jim Pattison, 
    the supplies allocated to the municipality often fall short of the growing populations' needs, including but not limited to: 
    high wait times for specialized procedures, patient readmission rates, and higher than average rates of in-hospital sepsis""",
    "Abbotsford": """ Abbotsford consistently appears in the top 3 of the index in almost all situations, likely due to it's rising population
    and growing senior demographic. Although it's population is comparable to smaller municipalities such as Chilliwack, Mission, and Maple Ridge,
    Abbotsford has significantly higher demand pressure and capacity strain. This is likely caused by Abbotsford General Hospital, which serves not
    only the municipality, but the communities of Agassiz, Mission, and Chilliwack. The needs of this municipality include lowering its high
    surgical incompletion rate, along with more resources to combat emergency wait times, which are the highest in the region.""",
    "Burnaby": """ Although Burnaby is one of the largest cities in both the Fraser Valley and British Columbia, it ranks within the median. Burnaby
    has over 200,000 residents and a higher ratio of those being seniors or low-income, the demand and capacity strains appear to adequately supply the population
    with enough resources and programs to prevent bottlenecks in the system. This can likely be explained due to the existence of Burnaby General Hospital, 
    which is limited to Burnaby rather than overarching on multiple cities (see limitations). However, it is important to note that although being in the median, 
    Burnaby faces the largest 90th percentile procedure wait time in the region, meaning that patients are often left to wait for much longer for neccesary procedures.
    As the cities' population grows and ages, addressing the extreme cases of procedure waits will serve to create systems that stand the test of time.""",
    "New Westminster" : """ New Westminster consistently ranks below or near the average within the index, likely due to its lower senior and children demographics, 
    considerably lower emergency wait times, and less demand for procedures (such as biopsies, CT scans, etc). However, it is important to note 2 major factors that 
    wouldn't show up within this index, those being that 1. New Westminister has the highest population growth rate of all municipalities, it will need more resources
    in future years, including preventative care to avoid strain on emergency and acute systems, and 2. New West's Royal Columbian Hospital is the oldest hospital in BC,
    thus entailing that it's aging infrastructure and systems will need repair and renovation to accommodate new technologies over time."""
}
if "selected_municipality" not in st.session_state:
    st.session_state.selected_municipality = None
st.markdown("""
<style>
.municipality-card {
    border: 1px solid rgba(128,128,128,0.25);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    background-color: rgba(128,128,128,0.06);}
.rank-number {
    font-size: 14px;
    font-weight: 600;
    opacity: 0.65;}
.municipality-name {
    font-size: 23px;
    font-weight: 700;
    margin-top: 3px;}
.score-text {
    font-size: 15px;
    opacity: 0.75;}
.detail-panel {
    border: 1px solid rgba(128,128,128,0.3);
    border-radius: 18px;
    padding: 30px;
    margin-top: 25px;
    margin-bottom: 30px;
    background-color: rgba(128,128,128,0.04);}
.detail-title {
    font-size: 32px;
    font-weight: 750;
    margin-bottom: 4px;}
.detail-subtitle {
    font-size: 15px;
    opacity: 0.65;
    margin-bottom: 20px;}
.section-title {
    font-size: 20px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 10px;}
.blurb {
    font-size: 16px;
    line-height: 1.65;}
</style>
""", unsafe_allow_html=True)
st.title("Municipality Rankings")
st.write(
    "Select a municipality to explore the factors contributing "
    "to its position on the Fraser Health Needs Index."
)
ranking_display = ranking.copy()
if "Rank" not in ranking_display.columns:
    ranking_display = ranking_display.sort_values(
        "Final Score",
        ascending=False
    ).reset_index(drop=True)
    ranking_display["Rank"] = ranking_display.index + 1
st.markdown("## Municipality Ranking")
for _, row in ranking_display.iterrows():
    municipality = row["Municipality"]
    rank = int(row["Rank"])
    # Change this if your score column has a different name
    score = row["Need Index"]
    with st.container():
        st.markdown(
            f"""
            <div class="municipality-card">

                <div class="rank-number">
                    RANK #{rank}
                </div>

                <div class="municipality-name">
                    {municipality}
                </div>
                <div class="score-text">
                    Overall Need Score: {score:.3f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(
            f"View {municipality}",
            key=f"municipality_button_{municipality}",
            use_container_width=True
        ):
            st.session_state.selected_municipality = municipality
            st.rerun()

selected = st.session_state.selected_municipality


if selected is not None:
    selected_ranking = ranking_display[
        ranking_display["Municipality"] == selected
    ]

    if len(selected_ranking) == 0:
        st.error(
            f"Could not find {selected} in the ranking dataframe."
        )

    else:
        selected_ranking = selected_ranking.iloc[0]
        selected_data = index_data[
            index_data["Municipality"] == selected
        ]
        if len(selected_data) == 0:

            st.warning(
                f"No detailed data was found for {selected}."
            )
            selected_data = None
        else:
            selected_data = selected_data.iloc[0]
        st.markdown(
            '<div class="detail-panel">',
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="detail-title">
                {selected}
            </div>
            <div class="detail-subtitle">
                Municipality profile within the Fraser Health Needs Index
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button(
            "✕ Close",
            key="close_municipality"
        ):
            st.session_state.selected_municipality = None
            st.rerun()
        st.markdown(
            '<div class="section-title">Overall ranking</div>',
            unsafe_allow_html=True
        )
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Rank",
                f"#{int(selected_ranking['Rank'])}"
            )
        with col2:
            st.metric(
                "Overall Need Score",
                f"{selected_ranking['Final Score']:.3f}"
            )
        st.markdown(
            '<div class="section-title">What does this ranking mean?</div>',
            unsafe_allow_html=True
        )
        blurb = municipality_blurbs.get(
            selected,
            "A municipality-specific analysis has not yet been written."
        )
        st.markdown(
            f'<div class="blurb">{blurb}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="section-title">Pillar breakdown</div>',
            unsafe_allow_html=True
        )
        pillar_columns = [
            ("Demand", "Demand Score"),
            ("Capacity & Access", "Capacity Score"),
            ("Vulnerable Populations", "Vulnerability Score"),
            ("Outcomes", "Outcome Score")
        ]
        pillar_cols = st.columns(4)
        for column, (label, column_name) in zip(
            pillar_cols,
            pillar_columns
        ):
            with column:
                if column_name in selected_ranking.index:
                    value = selected_ranking[column_name]
                    st.metric(
                        label,
                        f"{value:.3f}"
                    )
                else:
                    st.metric(
                        label,
                        "N/A"
                    )

        if selected_data is not None:
            st.markdown(
                '<div class="section-title">Key indicators</div>',
                unsafe_allow_html=True
            )

            indicators = [

                (
                    "ED visit rate",
                    "ED_visit_rate",
                    "/ 1,000"
                ),

                (
                    "Acute hospital rate",
                    "acute_hospital_rate",
                    "/ 1,000"
                ),

                (
                    "ACSC hospitalization",
                    "ACSC_avg",
                    ""
                ),

                (
                    "Procedure demand rate",
                    "procedure_demand_rate",
                    ""
                ),

                (
                    "Procedure incompletion",
                    "incompletion_percent",
                    "%"
                ),

                (
                    "Procedure wait time",
                    "total_procedure_wait",
                    "days"
                )

            ]


            # Split into two rows of three
            for start in range(0, len(indicators), 3):

                current_indicators = indicators[
                    start:start + 3
                ]

                cols = st.columns(len(current_indicators))


                for col, (
                    label,
                    column_name,
                    suffix
                ) in zip(cols, current_indicators):

                    with col:

                        if column_name in selected_data.index:

                            value = selected_data[column_name]


                            # Handle missing values
                            if pd.isna(value):

                                display_value = "N/A"

                            else:

                                # Percentage
                                if suffix == "%":

                                    display_value = (
                                        f"{float(value):.1f}%"
                                    )

                                # Days
                                elif suffix == "days":

                                    display_value = (
                                        f"{float(value):.1f} days"
                                    )

                                # Other numeric variables
                                else:

                                    display_value = (
                                        f"{float(value):.1f} {suffix}"
                                    )


                            st.metric(
                                label,
                                display_value
                            )


        # ====================================================
        # INTERPRETATION
        # ====================================================

        st.markdown(
            '<div class="section-title">How to interpret this</div>',
            unsafe_allow_html=True
        )


        st.write(
            "A higher Needs Index score indicates greater relative "
            "healthcare need compared with the other municipalities "
            "included in the index. The score should therefore be "
            "interpreted comparatively rather than as an absolute "
            "measure of healthcare quality or service availability."
        )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

## STEP 2
components = pd.read_csv("data/pillar_components.csv")
