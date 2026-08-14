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
##Setup
components = pd.read_csv("data/pillar_components.csv")
numeric_cols = components.columns.drop("Municipality")
components[numeric_cols] = components[numeric_cols].fillna(0)

profiles = pd.DataFrame({
 "Municipality": [ "Surrey", "Abbotsford", "Delta", "Langley", "White Rock", "Burnaby", 
                  "New Westminster", "Coquitlam", "Port Coquitlam", "Port Moody", "Pitt Meadows",
                  "Maple Ridge", "Chilliwack", "Mission", "Hope", "Kent"],
    "Blurb": [

        (
            "Surrey ranks highly across the index in almost all scenarios. "
            "This reflects a combination of being the highest populated "
            "municipality in the Fraser Health Area, along with large demand "
            "and access pressures. While Surrey has some of the largest "
            "medical facilities in the region, including Surrey Memorial "
            "and Jim Pattison, the supplies allocated to the municipality "
            "often fall short of the growing population's needs. This "
            "includes high wait times for specialized procedures, patient "
            "readmission rates, and higher than average rates of "
            "in-hospital sepsis."
        ),

        (
            "Abbotsford consistently appears in the top 3 of the index in "
            "almost all situations, likely due to its rising population "
            "and growing senior demographic. Although its population is "
            "comparable to smaller municipalities such as Chilliwack, "
            "Mission, and Maple Ridge, Abbotsford has significantly higher "
            "demand pressure and capacity strain. This is likely caused by "
            "Abbotsford General Hospital, which serves not only the "
            "municipality, but the communities of Agassiz, Mission, and "
            "Chilliwack. The needs of this municipality include lowering "
            "its high surgical incompletion rate, along with more resources "
            "to combat emergency wait times, which are the highest in "
            "the region."
        ),

        (
            "Delta, although having a comparable population to municipalities "
            "like Abbotsford and Langley, finds itself amongst the lower "
            "average of need. This is likely explained by its demand "
            "pressure being the lowest in the index, including the lowest "
            "procedure demand and incompletion rates, along with the lowest "
            "emergency visit rate of only 37 people out of every 1,000. "
            "However, Delta presents a mismatch between demand and outcomes: "
            "despite having the lowest demand pressure in the region, it "
            "ranks highly in Unmet Need and Outcomes, behind only Surrey "
            "and Maple Ridge. This points to a system that may be "
            "underperforming on quality and continuity of care for the "
            "patients it does serve, rather than one strained by sheer volume."
        ),

        (
            "Langley, one of the fastest growing cities in the Fraser Valley, "
            "finds itself in the top half of the index. With one of the "
            "highest emergency initial wait times in the region, Langley "
            "Memorial Hospital faces immense capacity pressure. Over 50% "
            "of emergency patients at Langley Memorial are admitted to "
            "acute care, pointing to a gap between residents needing acute "
            "care and not being able to access it in a timely manner, likely "
            "caused by a low acute bed to resident ratio and a lack of "
            "physicians to conduct initial assessments. Another important "
            "note is the fact that residents from Surrey border "
            "neighbourhoods, such as Clayton and Cloverdale, make up 20% "
            "of patients at the hospital, meaning that calculated demand "
            "of services is an understatement of the real need of the area."
        ),

        (
            "White Rock is home to Peace Arch Hospital, a smaller regional "
            "hospital that serves both White Rock and South Surrey, bringing "
            "a lot more capacity stress to the region. Additionally, White "
            "Rock has both a large aging population and a high population "
            "growth rate, creating a unique combination of overall increased "
            "demand and a large minority needing frequent and more "
            "specialized care. This means a proportionate growth in scale, "
            "complexity, and continuum of care is especially important for "
            "the municipality."
        ),

        (
            "Although Burnaby is one of the largest cities in both the "
            "Fraser Valley and British Columbia, it ranks within the median. "
            "Burnaby has over 200,000 residents and a higher ratio of seniors "
            "or low-income residents, but the demand and capacity strains "
            "appear to adequately supply the population with enough "
            "resources and programs to prevent bottlenecks in the system. "
            "This can likely be explained by the existence of Burnaby "
            "General Hospital, which is limited to Burnaby rather than "
            "overarching on multiple cities. However, it is important to "
            "note that although being in the median, cities like Burnaby "
            "still need policies that help combat growing strains, such as "
            "its high procedural wait time. Maintaining this balance will "
            "become increasingly important as the city's population grows "
            "and ages."
        ),

        (
            "New Westminster consistently ranks below or near the average "
            "within the index, likely due to its lower senior and children "
            "demographics, considerably lower emergency wait times, and "
            "less demand for procedures such as biopsies and CT scans. "
            "However, it is important to note two major factors that would "
            "not show up within the index. First, New Westminster has the "
            "highest population growth rate of all municipalities, meaning "
            "it will need more resources in future years, including "
            "preventative care to avoid strain on emergency and acute "
            "systems. Second, New West's Royal Columbian Hospital is the "
            "oldest hospital in BC, meaning its aging infrastructure and "
            "systems will need repair and renovation to accommodate new "
            "technologies over time."
        ),

        (
            "Coquitlam is one of the larger municipalities within this "
            "index, with a population of approximately 150,000, and "
            "uniquely presents need within long-term care and patient "
            "outcomes. Strains on long-term residential facilities and the "
            "quality of procedures within hospitals likely explain high "
            "metrics for worsening physical and mental conditions within "
            "these types of care facilities. However, other types of strain "
            "including initial appointments, wait times, and large amounts "
            "of surgery demand may also be the cause. Until more "
            "comprehensive data can be utilized, municipalities with less "
            "public data, such as Coquitlam, remain somewhat inaccurate "
            "within the index."
        ),

        (
            "Port Coquitlam ranks among the lower-need municipalities in "
            "the region, driven largely by consistently strong outcomes "
            "and a comparatively low-vulnerability population. With most "
            "residents utilizing local facilities for non-life threatening "
            "procedures and using neighbouring cities' hospitals for "
            "specialized care, the municipality demonstrates relatively "
            "effective access to healthcare. Notably, the municipality's "
            "Unmet Need and Outcomes score is the second-best in Fraser "
            "Health, trailing only Port Moody, indicating physicians are "
            "able to deliver quality care. This care holds despite a "
            "modest strain on capacity, suggesting the system serving "
            "Port Coquitlam is handling its current patient load effectively "
            "rather than showing signs of being overwhelmed."
        ),

        (
            "Port Moody consistently ranks at the bottom of the Needs "
            "Index, despite being home to Eagle Ridge Hospital, which "
            "provides emergency and acute services to the Tri-Cities, "
            "Anmore, and Belcarra. Ranking the lowest amongst Vulnerable "
            "Populations and Unmet Need and Outcomes, while being around "
            "the median for Demand Pressure, the municipality demonstrates "
            "that it is able to take in patients and provide care with "
            "minimal backlog in the system. It is important to note that "
            "Port Moody has a considerably high surgical incompletion rate, "
            "indicating that non-emergency procedures such as hip and knee "
            "replacements are still heavily demanded across the region, "
            "no matter how little 'need' a municipality demonstrates."
        ),

        (
            "With a population of roughly 20,000, Pitt Meadows does not "
            "have a general healthcare facility, and thus most residents "
            "go to Ridge Meadows Hospital in Maple Ridge for emergency "
            "and acute services. However, this does not create an inherent "
            "backlog as Pitt Meadows ranks near the bottom under most "
            "pillars, indicating that residents are able to receive "
            "quality and timely care. However, it is important to note "
            "that due to a combination of not having a municipal healthcare "
            "facility, nor much regional data, we cannot know the true "
            "need of a town like Pitt Meadows, and it remains fairly "
            "ambiguous."
        ),

        (
            "Maple Ridge places itself almost exactly at the median or "
            "average point within the index, which points to adequate "
            "supply and quality of care for its residents. However, it is "
            "important to note that Maple Ridge has one of the highest "
            "rates of general and specialized patient re-admission in "
            "the region. This can likely be explained by staffing shortages "
            "and rising emergency department volumes, as these types of "
            "strain on physicians and specialists often lead to a lower "
            "quality of care and persistent backlog. Creating systems "
            "across Fraser Health to alleviate strain on staff will help "
            "lower the average into creating more accessible healthcare."
        ),

        (
            "Being home to Chilliwack General Hospital, the municipality "
            "covers much more than its 113,000 residents, including Cultus "
            "Lake, Agassiz, Harrison, and multiple First Nations communities "
            "in the East Fraser Valley. This coverage presents a very high "
            "rank in Demand Pressure, third only to Surrey and Abbotsford. "
            "However, it consistently ranks average or below average within "
            "other columns, indicating that care is able to meet the "
            "complexity and quality needed by patients. This combination "
            "points to moderate need: a system that may face strain due "
            "to scale, but is able to rise and match the needs of the "
            "communities it covers."
        ),

        (
            "While the municipality has lower than 50,000 residents, "
            "Mission consistently ranks within the top half of the index "
            "and faces significant capacity and access pressure, notably "
            "in emergency departments and patient discharge, where slow "
            "procedures and administration can easily create bottlenecks. "
            "In particular, patients often occupy hospital beds not because "
            "they need acute care, but are waiting for discharge to "
            "long-term care, rehabilitation, and other forms of community "
            "support. For municipalities like Mission, providing "
            "streamlined paths for patient discharge will alleviate the "
            "idle use of much-needed supplies like beds for Mission's "
            "large hospitalized senior population."
        ),

        (
            "Hope is the second smallest municipality in the Fraser Valley, "
            "but rather than scale, its need is demonstrated in the "
            "complexity of care needed by its population. Hope has a "
            "significantly higher percentage of seniors as compared to "
            "larger municipalities like Burnaby and Surrey, demonstrating "
            "that its smaller population requires different forms of care "
            "rather than just a scaled-down version of other municipalities. "
            "An important thing to note is that Hope is fairly rural, "
            "meaning patients often have to travel to larger hubs like "
            "Abbotsford and Chilliwack in order to access general and "
            "specialized care. Potential solutions could include stronger "
            "telemedicine systems along with accessible facilities for "
            "seniors to meet with primary healthcare providers."
        ),

        (
            "Kent is the smallest municipality in the Fraser Health region, "
            "having only the Agassiz Community Health Centre for primary "
            "health services. Many residents of Kent rely on Chilliwack "
            "General Hospital for emergency and acute care services. "
            "Throughout the index, Kent tends to fall in the average to "
            "below average rank, indicating adequate capacity and quality "
            "of care for the municipality's residents. Nonetheless, Kent "
            "demonstrates above-average need based on facility demand, "
            "by having some of the highest avoidable hospitalizations "
            "in the region. Providing general hospitals like Chilliwack, "
            "which serve smaller rural regions such as Kent, with adequate "
            "outpatient support and ambulatory systems will help alleviate "
            "patient needs as care becomes complex." ) ]})

pillar_columns = {
    "Demand": ['ED_visit_rate', 'acute_hospital_rate', 'ACSC_avg',
       'procedure_demand_rate', 'incompletion_percent'],
    "Capacity": [ 'Acute bed shortage', 'Resource Use Intensity','Facilities', 'Wait before initial assesment (ED)',
       '90th percentile ED wait time', 'Days in alternate levels of care',
       'Procedure and surgical wait', 'Patients admitted through ED'],
    "Vulnerable Populations": ['Seniors (65+)', 'Over 85', 'Under 5', 'Frailty',
       'Low income (By LICO)', 'Visible Minority', 'Population', 'Unemployed',
       'Population growth', 'High hospital bed users'],
    "Unmet Need and Outcomes": ['Deaths following major surgery',
       'All patient readmissions', 'Specialized readmission',
       'In Hospital Sepsis', 'LTC fall rate', 'Pressure Ulcers',
       'Depressive Moods', 'Antipsychotic use (Potentially Innapropriate)']}
highlight_columns = [ 'ED_visit_rate', 'incompletion_percent', 'Wait before initial assesment (ED)', 'Acute bed shortage', 'Procedure and surgical wait',
                     'Seniors (65+)', 'Population', 'Population growth', 'All patient readmissions', 'Specialized readmission']
def get_top_rankings(municipality,df,columns,top_n_threshold=3):
    highlights = []
    for col in columns:
        ranked = df[["Municipality", col]].copy()
        ranked["_rank"] = ranked[col].rank(
            ascending=False,
            method="min")
        muni_rank = ranked.loc[
            ranked["Municipality"] == municipality,
            "_rank"
        ].values
        if len(muni_rank) == 0 or pd.isna(muni_rank[0]):
            continue
        muni_rank = int(muni_rank[0])
        if muni_rank <= top_n_threshold:
            suffix = { 1: "st", 2: "nd", 3: "rd"}.get(muni_rank, "th")
            highlights.append(f"{muni_rank}{suffix} highest in {col}")
    return highlights
    
## OVerview Page
if page == "Overview":
    st.title("Fraser Health Needs Index")
    st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")
    if "expanded_muni" not in st.session_state:
        st.session_state.expanded_muni = None
    main_col, control_col = st.columns([3.5, 1],gap="large")

    dem = st.slider( "Demand", 0, 100, 25, key="pillar_demand")
    cap = st.slider(
    "Capacity",
    0, 100, 25,
    key="pillar_capacity")

    vul = st.slider(
    "Vulnerable Populations",
    0, 100, 25,
    key="pillar_vulnerable")

    unmet = st.slider(
    "Unmet Need",
    0, 100, 25,
    key="pillar_unmet")

    pillar_total = dem + cap + vul + unmet

    if pillar_total == 0:

        pillar_weights_normalized = {
        "Demand": 0.25,
        "Capacity": 0.25,
        "Vulnerable Populations": 0.25,
        "Unmet Need and Outcomes": 0.25
    }

    else:

        pillar_weights_normalized = {
        "Demand": dem / pillar_total,
        "Capacity": cap / pillar_total,
        "Vulnerable Populations": vul / pillar_total,
        "Unmet Need and Outcomes": unmet / pillar_total
    }
DEFAULT_VARIABLE_WEIGHTS = { "Demand": { "ED_visit_rate": 20,"acute_hospital_rate": 25,"ACSC_avg": 5,"procedure_demand_rate": 20,"incompletion_percent": 30},
        "Capacity": {"Acute bed shortage": 12.5, "Resource Use Intensity": 12.5 , "Facilities": 10, "Wait before initial assesment (ED)": 12.5, 
                     "90th percentile ED wait time": 15, "Days in alternate levels of care": 12.5,"Procedure and surgical wait": 15,"Patients admitted through ED": 10},
        "Vulnerable Populations": { "Seniors (65+)": 17, "Over 85": 5, "Under 5": 6, "Frailty": 10, "Low income (By LICO)": 17, "Visible Minority": 1,
        "Population": 25,"Unemployed": 12.5,"Population growth": 12.5,"High hospital bed users": 10},
        "Unmet Need and Outcomes": {"Deaths following major surgery": 15,"All patient readmissions": 15,"Specialized readmission": 10,"In Hospital Sepsis": 12.5,
        "LTC fall rate": 12.5,"Pressure Ulcers": 10,"Depressive Moods": 12.5,"Antipsychotic use (Potentially Innapropriate)": 12.5}}

with st.popover("Advanced Settings"):
    st.markdown("Adjust the weight of each individual variable within its pillar.")
    variable_weights = {}
    for pillar_name, cols in pillar_columns.items():
        st.markdown(f"**{pillar_name}**")
        even_split = round(100 / len(cols))
        pillar_var_weights = {}
        for col in cols:
            default_value = DEFAULT_VARIABLE_WEIGHTS[pillar_name][col]
            pillar_var_weights[col] = st.slider(col,0,100,even_split,key=f"adv_{col}")
        var_total = sum(pillar_var_weights.values())
        if var_total == 0:
            variable_weights[pillar_name] = {
                col: 1 / len(cols)
                for col in cols}
        else:
            variable_weights[pillar_name] = {
                col: pillar_var_weights[col] / var_total
                for col in cols}
   with main_col:
    live_pillars = pd.DataFrame({"Municipality": components["Municipality"]})
    pillar_scores = {}
    for pillar_name, cols in pillar_columns.items():
        weighted_components = []
        for col in cols:
            if col not in components.columns:
                continue
            z = zscore(components[col])
            weight = variable_weights[pillar_name][col]
            weighted_components.append(z * weight)
        if weighted_components:
            pillar_scores[pillar_name] = sum(weighted_components)
        else:
            pillar_scores[pillar_name] = pd.Series(0,index=components.index)
    live_pillars["Live Need Index"] = (
        pillar_scores["Demand"]
        * pillar_weights_normalized["Demand"]
        + pillar_scores["Capacity"]
        * pillar_weights_normalized["Capacity"]
        + pillar_scores["Vulnerable Populations"]
        * pillar_weights_normalized["Vulnerable Populations"]
        + pillar_scores["Unmet Need and Outcomes"]
        * pillar_weights_normalized["Unmet Need and Outcomes"])
        ranking = live_pillars[["Municipality", "Live Need Index"]].merge(
            final_df[["Municipality", "Cluster_Label"]], on="Municipality"
        ).sort_values("Live Need Index", ascending=False).reset_index(drop=True)
        ranking["Rank"] = range(1, len(ranking) + 1)

        st.subheader("Municipality Ranking")

        st.markdown(
            """
            <style>
            .ranking-card {
                background-color: #1E222B;
                border: 1px solid #3A3F4B;
                border-left: 8px solid #E74C3C;
                border-radius: 16px;
                padding: 22px 28px;
                margin-bottom: 4px;
            }
            .rank-number { font-size: 40px; font-weight: 800; margin-bottom: 8px; }
            .municipality-name { font-size: 28px; font-weight: 700; margin-bottom: 8px; }
            </style>
            """,
            unsafe_allow_html=True
        )

        stats_source = components.merge(final_df[["Municipality"]], on="Municipality")
for _, row in ranking.iterrows():
    muni = row["Municipality"]
    card_html = f"""
<div class="ranking-card">
    <div class="rank-number">#{int(row['Rank'])}</div>
    <div class="municipality-name">{muni}</div>
    </div>
</div>
"""
    st.markdown(card_html, unsafe_allow_html=True)

    if st.button(f"View {muni} details", key=f"btn_{muni}"):
        st.session_state.expanded_muni = None if st.session_state.expanded_muni == muni else muni
    if st.session_state.expanded_muni == muni:
        st.markdown(f"### {muni} — Need Index")
        st.metric("Live Need Index",f"{row['Live Need Index']:.4f}")
        profile_row = profiles[profiles["Municipality"] == muni]
        if not profile_row.empty:
            profile_row = profile_row.iloc[0]
            st.markdown(profile_row["Blurb"])
        else:
            st.markdown("_Profile not yet written for this municipality._")

        st.markdown("**Notable Stats**")
        highlights = get_top_rankings(muni, stats_source, highlight_columns)
        if highlights:
            for h in highlights:
                st.markdown(f"- {h}")
        else:
            st.markdown("_No top-3 rankings in the highlighted categories._")

        st.caption(f"Cluster: {row['Cluster_Label']}")








