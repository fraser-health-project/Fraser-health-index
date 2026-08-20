##Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap

st.set_page_config(page_title="Fraser Health Needs Index", layout="wide")
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        width: 220px;}
</style>
""", unsafe_allow_html=True)
final_df = pd.read_csv("data/final_df(part4).csv")
meta = pd.read_csv("data/KPI_metadata(part2).csv")

st.sidebar.title("In this index...")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Data and Limitations", "Methodology"])
##Setup
components = pd.read_csv("data/pillar_components(part2).csv")
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
            "patient demand pressure and hospital strain. This is likely caused by "
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
            "ranks highly in Outcomes, behind only Surrey "
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
            "or low-income residents, but the demand and hospital strains "
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
            "Outcomes score is the second-best in Fraser "
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
            "Populations and Outcomes, while being around "
            "the median for Patient Demand Pressure, the municipality demonstrates "
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
            "rank in Patient Demand, third only to Surrey and Abbotsford. "
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
            "and faces significant hospital strain, notably "
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

# Temporary, drop later
pillar_columns = {
    "Patient Demand": ['ED visits per 1,000', 'Acute Hospital Stays', 'ACSC (Avoidable) Hospitalizations',
       'Procedure Demand Rate'],
    "Hospital Strain": [ 'Acute bed shortage', 'Resource Use Intensity','Facilities', 'Wait before initial assesment (ED)',
       '90th percentile ED wait time', 'Days in alternate levels of care',
       'Procedure and surgical wait', 'Patients admitted through ED','Procedure Incompletion Rate'],
    "Vulnerable Populations": ['Seniors (65+)', 'Over 85', 'Under 5', 'Frailty','Population', 'Unemployed','Population growth', 'High hospital bed users'],
    "Outcomes": ['Deaths following major surgery',
       'All patient readmissions', 'Specialized readmission',
       'In Hospital Sepsis', 'LTC fall rate', 'Pressure Ulcers',
       'Depressive Moods', 'Antipsychotic use (Potentially Innapropriate)']}
## Define
def zscore(series):
    series = pd.to_numeric(series, errors="coerce")
    mean = series.mean()
    std = series.std()
    if pd.isna(std) or std == 0:
        return pd.Series(0, index=series.index)
    return (series.fillna(mean) - mean) / std
population_kpis = ["Population", "Under 5", "Seniors (65+)", "Over 85", "Population growth"]
hospital_strain_kpis = ['Acute bed shortage', 'Resource Use Intensity', 'Facilities', 'Wait before initial assesment (ED)', '90th percentile ED wait time',
    'Days in alternate levels of care']
patient_demand_kpis = ['ED visits per 1,000', 'Acute Hospital Stays', 'ACSC (Avoidable) Hospitalizations', 'Procedure Demand Rate'    ]
outcomes_kpis = [ "All patient readmissions", "Deaths following major surgery", "In Hospital Sepsis", "Pressure Ulcers", "Antipsychotic use (Potentially Innapropriate)"]
kpi_units = {
    "Population growth": "%",
    "Seniors (65+)": "%",
    "Over 85": "%",
    "Under 5": "%",
    "Frailty": "%",
    "Facilities" : " per 1,000",
    "ACSC (Avoidable) Hospitalizations" : " per 1,000",
    "Procedure Demand Rate" : " per 1,000",
    "90th percentile ED wait time" : " weeks",
    "Wait before initial assesment (ED)" : " hours",
    "Day in alternate levels of care" : " Days",
    "All patient readmissions": "%",
    "Deaths following major surgery" : "%",
    "In Hospital Sepsis" : "%",
    "Acute Hospital Stays" : " per 1,000",
    "ED visits per 1,000": " per 1,000"}
def build_horizontal_kpi_chart(muni, kpi_list, title):
    rows = []
    for kpi in kpi_list:
        if kpi not in components.columns:
            continue
        raw_series = pd.to_numeric(components[kpi], errors="coerce")
        pct_series = raw_series.rank(pct=True) * 100
        muni_mask = components["Municipality"] == muni
        if not muni_mask.any():
            continue
        muni_pct = pct_series[muni_mask].iloc[0]
        meta_mask = meta["Municipality"] == muni
        if meta_mask.any() and kpi in meta.columns:
            actual_value = round(meta.loc[meta_mask, kpi].iloc[0], 4)
        else:
            actual_value = None
        rows.append({
            "KPI": kpi,
            "Percentile": muni_pct,
            "Actual Value": actual_value,
            "Unit": kpi_units.get(kpi,"")})
    chart_df = pd.DataFrame(rows)
    if chart_df.empty:
        return None
    chart_df = chart_df.sort_values("Percentile")
    fig = px.bar(
        chart_df,
        x="Percentile",
        y="KPI",
        orientation="h",
        text=chart_df["Percentile"].round(0).astype(int).astype(str) + "th",
        custom_data=["Actual Value","Unit"],
        title=title,
        color="Percentile",
        color_continuous_scale="Reds",
        range_x=[0, 105],)
    fig.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Actual Value: %{customdata[0]}%{customdata[1]}<br>"
            "Percentile: %{x:.0f}th"
            "<extra></extra>"))
    fig.update_layout(
        bargap=0.5,
        height=400,
        showlegend=False,
        coloraxis_showscale=False,
        xaxis_title="Percentile Rank",
        yaxis_title="",)
    return fig
def build_population_chart(muni):
    return build_horizontal_kpi_chart(muni, population_kpis, "Population & Demographic Context")
def build_hospital_strain_chart(muni):
    return build_horizontal_kpi_chart(muni, hospital_strain_kpis, "Facility Strain")
def build_demand_chart(muni):
    return build_horizontal_kpi_chart(muni, patient_demand_kpis, "Patient Demand")
def build_outcomes_chart(muni):
    return build_horizontal_kpi_chart(muni, outcomes_kpis, "Outcomes")
def render_analytics_page(muni):
    st.title(f"{muni} — Analytics")
    if st.button("← Back", key="analytics_back"):
        st.session_state.view = "detail"
        st.rerun()
    charts = [
        build_population_chart(muni),
        build_hospital_strain_chart(muni),
        build_demand_chart(muni),
        build_outcomes_chart(muni)]
    cols = st.columns(2)
    for i, fig in enumerate(charts):
        if fig is not None:
            with cols[i % 2]:
                st.plotly_chart(fig, width="stretch")
def build_pillar_compare_chart(muni_a, muni_b):
    pillar_cols = [c for c in live_pillars.columns if c.endswith(" Z (live)")]
    compare_df = live_pillars[live_pillars["Municipality"].isin([muni_a, muni_b])][["Municipality"] + pillar_cols]
    compare_long = compare_df.melt(id_vars="Municipality", var_name="Pillar", value_name="Z-score")
    compare_long["Pillar"] = compare_long["Pillar"].str.replace(" Z (live)", "", regex=False)

    fig = px.bar(
        compare_long, x="Z-score", y="Pillar", color="Municipality",
        orientation="h", barmode="group",
        color_discrete_sequence=["#E74C3C", "#3B82C4"],
        title="Pillar Comparison (relative to regional average)")
    fig.add_vline(x=0, line_dash="dash", annotation_text="Regional average")
    fig.update_layout(bargap=0.3, height=350)
    return fig
def build_compare_kpi_chart(muni_a, muni_b, kpi_list, title):
    rows = []
    for kpi in kpi_list:
        if kpi not in components.columns:
            continue
        val_a = pd.to_numeric(components.loc[components["Municipality"] == muni_a, kpi], errors="coerce").values[0]
        val_b = pd.to_numeric(components.loc[components["Municipality"] == muni_b, kpi], errors="coerce").values[0]
        rows.append({"KPI": kpi, "Municipality": muni_a, "Value": val_a})
        rows.append({"KPI": kpi, "Municipality": muni_b, "Value": val_b})
    chart_df = pd.DataFrame(rows)
    if chart_df.empty:
        return None
    fig = px.bar(
        chart_df, x="Value", y="KPI", color="Municipality",
        orientation="h", barmode="group",
        color_discrete_sequence=["#E74C3C", "#3B82C4"],
        title=title
    )
    fig.update_layout(bargap=0.3, height=max(280, 70 * len(kpi_list)))
    return fig


## OVerview Page
if page == "Overview":
    #elif st.session_state.view == "detail":
        #render_detail_page(st.session_state.selected_muni)  # see D2
    with st.sidebar:
        st.markdown("---")
        st.markdown("#### Pillar Weights")
        dem = st.slider("Patient Demand", 0, 100, 25, key="pillar_demand")
        cap = st.slider("Hospital Strain", 0, 100, 25, key="pillar_capacity")
        vul = st.slider("Vulnerable Populations", 0, 100, 25, key="pillar_vulnerable")
        unmet = st.slider("Outcomes", 0, 100, 25, key="pillar_unmet")

        pillar_total = dem + cap + vul + unmet
        if pillar_total == 0:
            pillar_weights_normalized = {
                "Patient Demand": 0.25, "Hospital Strain": 0.25,
                "Vulnerable Populations": 0.25, "Outcomes": 0.25
            }
        else:
            pillar_weights_normalized = {
                "Patient Demand": dem / pillar_total,
                "Hospital Strain": cap / pillar_total,
                "Vulnerable Populations": vul / pillar_total,
                "Outcomes": unmet / pillar_total
            }
        DEFAULT_VARIABLE_WEIGHTS = {
            "Patient Demand": {"ED visits Per 1,000": 35, "Acute Hospital Stays": 25, "ACSC (Avoidable) Hospitalizations": 5,
                       "Procedure Demand Rate": 35},
            "Hospital Strain": {"Acute bed shortage": 12.5, "Resource Use Intensity": 10, "Facilities": 10,
                         "Wait before initial assesment (ED)": 10, "90th percentile ED wait time": 10,
                         "Days in alternate levels of care": 10, "Procedure and surgical wait": 15,
                         "Patients admitted through ED": 10, "Procedure Incompletion Rate": 12.5},
            "Vulnerable Populations": {"Seniors (65+)": 15, "Over 85": 7.5, "Under 5": 15, "Frailty": 12.5, "Population": 15,
                                        "Unemployed": 12.5, "Population growth": 12.5, "High hospital bed users": 10},
            "Outcomes": {"Deaths following major surgery": 15, "All patient readmissions": 15,
                                         "Specialized readmission": 10, "In Hospital Sepsis": 12.5,
                                         "LTC fall rate": 12.5, "Pressure Ulcers": 10, "Depressive Moods": 12.5,
                                         "Antipsychotic use (Potentially Innapropriate)": 12.5}}

        policy_recommendations = {
        "Surrey": [
            "An expansion of specialized procedure and surgical capacity, so Surrey can act as a hub for neighbouring municipalities with complex care needs",
            "Expand care for complication prevention, this includes more follow up appointments, discharge planning, and social services for patients with high risk of frailty or readmission",
            "Use population growth projections during capacity planning to tie beds, specialists, and other resources to Surrey's rapidly growing city"],
        "Abbotsford": [
            "Allocate resources to Abbotsford General Hospital based on it's regional catchment area (i.e include Chilliwack, Mission, Kent), including a greater ambulatory fleet to support rural communities",
            "Establish regional referal mechanisms across the area so non-emergency patients can recieve timely care at another Fraser facility at times when Abbotsford General's ED is oversatured",
            "Provide patients with options for same-day diagnostic clinics, so patients who do not need hospital admission can recieve consultation and testing without increasing emergency occupancy"],
        "Delta": [
            "PASTE DELTA POLICY RECOMMENDATION 1 HERE",
            "PASTE DELTA POLICY RECOMMENDATION 2 HERE",
            "PASTE DELTA POLICY RECOMMENDATION 3 HERE" ],
        "Langley": [
            "PASTE LANGLEY POLICY RECOMMENDATION 1 HERE",
            "PASTE LANGLEY POLICY RECOMMENDATION 2 HERE",
            "PASTE LANGLEY POLICY RECOMMENDATION 3 HERE"],
        "White Rock": [
            "PASTE WHITE ROCK POLICY RECOMMENDATION 1 HERE",
            "PASTE WHITE ROCK POLICY RECOMMENDATION 2 HERE",
            "PASTE WHITE ROCK POLICY RECOMMENDATION 3 HERE" ],
        "Burnaby": [
            "PASTE BURNABY POLICY RECOMMENDATION 1 HERE",
            "PASTE BURNABY POLICY RECOMMENDATION 2 HERE",
            "PASTE BURNABY POLICY RECOMMENDATION 3 HERE"],
        "New Westminster": [
            "PASTE NEW WESTMINSTER POLICY RECOMMENDATION 1 HERE",
            "PASTE NEW WESTMINSTER POLICY RECOMMENDATION 2 HERE",
            "PASTE NEW WESTMINSTER POLICY RECOMMENDATION 3 HERE"],
        "Coquitlam": [
            "PASTE COQUITLAM POLICY RECOMMENDATION 1 HERE",
            "PASTE COQUITLAM POLICY RECOMMENDATION 2 HERE",
            "PASTE COQUITLAM POLICY RECOMMENDATION 3 HERE" ],
        "Port Coquitlam": [
            "PASTE PORT COQUITLAM POLICY RECOMMENDATION 1 HERE",
            "PASTE PORT COQUITLAM POLICY RECOMMENDATION 2 HERE",
            "PASTE PORT COQUITLAM POLICY RECOMMENDATION 3 HERE"],
        "Port Moody": [
            "PASTE PORT MOODY POLICY RECOMMENDATION 1 HERE",
            "PASTE PORT MOODY POLICY RECOMMENDATION 2 HERE",
            "PASTE PORT MOODY POLICY RECOMMENDATION 3 HERE" ],
        "Pitt Meadows": [
            "PASTE PITT MEADOWS POLICY RECOMMENDATION 1 HERE",
            "PASTE PITT MEADOWS POLICY RECOMMENDATION 2 HERE",
            "PASTE PITT MEADOWS POLICY RECOMMENDATION 3 HERE" ],
        "Maple Ridge": [
            "PASTE MAPLE RIDGE POLICY RECOMMENDATION 1 HERE",
            "PASTE MAPLE RIDGE POLICY RECOMMENDATION 2 HERE",
            "PASTE MAPLE RIDGE POLICY RECOMMENDATION 3 HERE"],
        "Chilliwack": [
            "PASTE CHILLIWACK POLICY RECOMMENDATION 1 HERE",
            "PASTE CHILLIWACK POLICY RECOMMENDATION 2 HERE",
            "PASTE CHILLIWACK POLICY RECOMMENDATION 3 HERE"],
        "Mission": [
            "PASTE MISSION POLICY RECOMMENDATION 1 HERE",
            "PASTE MISSION POLICY RECOMMENDATION 2 HERE",
            "PASTE MISSION POLICY RECOMMENDATION 3 HERE" ],
        "Hope": [
            "PASTE HOPE POLICY RECOMMENDATION 1 HERE",
            "PASTE HOPE POLICY RECOMMENDATION 2 HERE",
            "PASTE HOPE POLICY RECOMMENDATION 3 HERE"],
        "Kent": [
            "PASTE KENT POLICY RECOMMENDATION 1 HERE",
            "PASTE KENT POLICY RECOMMENDATION 2 HERE",
            "PASTE KENT POLICY RECOMMENDATION 3 HERE"]}

        with st.popover("Advanced Settings"):
            st.markdown("Adjust the weight of each individual variable within its pillar.")
            variable_weights = {}
            for pillar_name, cols in pillar_columns.items():
                st.markdown(f"**{pillar_name}**")
                pillar_var_weights = {}
                for i, col in enumerate(cols):
                    default_value = DEFAULT_VARIABLE_WEIGHTS.get(pillar_name, {}).get(col, round(100 / len(cols), 1))
                    widget_key = f"adv_{pillar_name}_{i}"
                    pillar_var_weights[col] = st.slider(col, 0.0, 100.0, float(default_value), step=0.5, key=widget_key)

                var_total = sum(pillar_var_weights.values())
                if var_total == 0:
                    variable_weights[pillar_name] = {c: 1 / len(cols) for c in cols}
                else:
                    variable_weights[pillar_name] = {
                        c: pillar_var_weights.get(c, 0) / var_total
                        for c in cols}

    live_pillars = pd.DataFrame({"Municipality": components["Municipality"]})
    pillar_scores = {}
    for pillar_name, cols in pillar_columns.items():
        weighted_components = []
        for col in cols:
            if col not in components.columns:
                continue
            z = zscore(components[col])
            weight = variable_weights.get(pillar_name, {}).get(col, 1)
            weighted_components.append(z * weight)
        if weighted_components:
            pillar_scores[pillar_name] = sum(weighted_components)

    for pillar_name, score in pillar_scores.items():
        live_pillars[pillar_name + " Z (live)"] = score
    live_pillars["Live Need Index"] = sum(
        live_pillars[p + " Z (live)"] * w for p, w in pillar_weights_normalized.items()
        if (p + " Z (live)") in live_pillars.columns)
    live_pillars["Live Need Index"] = (live_pillars["Live Need Index"]- live_pillars["Live Need Index"].min())
    ranking = live_pillars[["Municipality", "Live Need Index"]].merge(
    final_df[["Municipality", "Cluster_Label"]],
    on="Municipality"
).sort_values("Live Need Index", ascending=False).reset_index(drop=True)
    if "view" not in st.session_state:
        st.session_state.view = "ranking"  # "ranking" or "detail"
    if "selected_muni" not in st.session_state:
        st.session_state.selected_muni = None
    group_descriptions = {
    "Vulnerable Population, Adequate Capacity":
        "Census data can tell us that these municipalities have large populations, or certain demographics that are especially in need of care",
    "High-Pressure System (High Demand + Strained Capacity)": "These municipalities likely serve a large population and often face strains in both acute care and emergency departments",
    "Baseline, Moderate Need": "These municipalities adequately supply their resident's needs, however, this does not mean these municipalities do not need new policies to better allieviate need"
    }
    ranking["Group_Description"] = ranking["Cluster_Label"].map(
    group_descriptions)
    ranking["Group_Wrapped"] = ranking["Group_Description"].apply(
    lambda x: "<br>".join(textwrap.wrap(str(x), width=45)))
    if st.session_state.view == "ranking":
        st.title("Fraser Health Needs Index")
        st.markdown("An interactive tool ranking and grouping hospital systems' need across the Fraser Health Region.")
        cluster_colors = { "Vulnerable Population, Adequate Capacity": "#E94F58","High-Pressure System (High Demand + Strained Capacity)": "#800020","Baseline, Moderate Need": "#F5D2D2"}
        fig_bar = px.bar(
            ranking,x="Live Need Index",
            y="Municipality",
            orientation="h",
            color="Cluster_Label",
            color_discrete_map=cluster_colors,
            title="Municipality Ranking by Need",
            custom_data=["Municipality", "Cluster_Label", "Group_Wrapped"])
        st.markdown("Tap on a municipality for details")
        if st.button("⚖️ Compare Two Municipalities"):
            st.session_state.view = "compare"
            st.rerun()
        fig_bar.update_layout(height = 600, yaxis={"categoryorder": "total ascending"},legend_title_text="Group") 
        fig_bar.update_traces(hovertemplate=(
            "<b>%{y}</b><br>"
            "Need Index: %{x:.2f}<br>"
            "<b>Group:</b> %{customdata[1]}<br>"
            "<br>"
            "<b>What this group means:</b><br>"
            "%{customdata[2]}"
            "<extra></extra>"))
        event = st.plotly_chart(fig_bar, use_container_width=True, on_select="rerun", key="ranking_chart")
        if event and event.get("selection", {}).get("points"):
            clicked_point = event["selection"]["points"][0]
            clicked_muni = clicked_point["customdata"][0]
            st.session_state.selected_muni = clicked_muni
            st.session_state.view = "detail"
            st.rerun()
        legend_title_text="Group"
    elif st.session_state.view == "detail":
        selected_muni = st.session_state.selected_muni
        municipality_profile = profiles[profiles["Municipality"] == selected_muni]
        if not municipality_profile.empty:
            insight = municipality_profile.iloc[0]["Blurb"]
        else:
            insight = "No insight available for this municipality."
        recommendations = policy_recommendations.get(
            selected_muni,
            [])
        if st.button("← Back to Rankings"):
            st.session_state.view = "ranking"
            st.session_state.selected_muni = None
            st.rerun()
        st.title(selected_muni)
        st.subheader("Insight")
        st.write(insight)
        st.subheader("Policy Recommendations")
        if recommendations:
            for i, recommendation in enumerate(
                recommendations,
                start=1):
                st.markdown(
                    f"**{i}.** {recommendation}")
        else:
            st.write("No policy recommendations have been added yet.")
        st.divider()
        if st.button("View Analytics →"):
            st.session_state.view = "analytics"
            st.rerun()
    elif st.session_state.view == "analytics":
        render_analytics_page(st.session_state.selected_muni)
    elif st.session_state.view == "compare":
        st.title("Compare Municipalities")
        if st.button("← Back to Ranking"):
            st.session_state.view = "ranking"
            st.rerun()
        muni_list = ranking["Municipality"].tolist()
        col1, col2 = st.columns(2)
        with col1:
            muni_a = st.selectbox("Municipality A", muni_list, index=0, key="compare_a")
        with col2:
            muni_b = st.selectbox("Municipality B", muni_list, index=1, key="compare_b")
        if muni_a == muni_b:
            st.warning("Choose two different municipalities to compare.")
        else:
            st.plotly_chart(build_pillar_compare_chart(muni_a, muni_b), width='stretch')

            st.markdown("#### Compare a Specific Category")
            category_map = {
                "Population & Demographics": population_kpis,
                "Facility Strain": facility_strain_kpis,
                "Healthcare Access": access_kpis,
                "Demand & Outcomes": demand_outcomes_kpis,}
            chosen_category = st.selectbox("Category", list(category_map.keys()))
            kpi_fig = build_compare_kpi_chart(muni_a, muni_b, category_map[chosen_category], chosen_category)
            if kpi_fig is not None:
                st.plotly_chart(kpi_fig, width='stretch')
            else:
                st.write("No data available for this category.")
