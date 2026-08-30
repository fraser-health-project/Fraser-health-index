##Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap
import plotly.graph_objects as go

st.set_page_config(page_title="Fraser Health Needs Index", layout="wide")
# Custom fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap');

/* Main page titles */
h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 600 !important;
}

/* Methodology and Limitations pages */
.cormorant-page {
    font-family: 'Cormorant Garamond', serif;
}

.cormorant-page h2,
.cormorant-page h3,
.cormorant-page p,
.cormorant-page li {
    font-family: 'Cormorant Garamond', serif;
}

.cormorant-page p,
.cormorant-page li {
    font-size: 18px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

final_df = pd.read_csv("data/final_df(part4).csv")
meta = pd.read_csv("data/KPI_metadata.csv")
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

    max_abs = compare_long["Z-score"].abs().max()
    axis_limit = (max_abs * 1.2) if max_abs > 0 else 1
    axis_min = -axis_limit

    colors = {muni_a: "#E74C3C", muni_b: "#3B82C4"}
    fig = go.Figure()
    for muni in [muni_a, muni_b]:
        sub = compare_long[compare_long["Municipality"] == muni]
        fig.add_trace(go.Bar(
            y=sub["Pillar"],
            x=sub["Z-score"] - axis_min,   
            base=axis_min,                  
            orientation="h",
            name=muni,
            marker_color=colors[muni],
            text=sub["Z-score"].round(2),
            textposition="outside",
            customdata=sub["Z-score"],
            hovertemplate="%{y}: %{customdata:.2f}<extra></extra>",))
    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    fig.update_layout(
        barmode="group",
        title="Pillar Comparison (relative to regional average)",
        xaxis=dict(range=[axis_min, axis_limit], tickmode="linear", dtick=0.5,
                   title="Z-score (relative to regional average)"),
        height=350,
        bargap=0.3,)
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
    max_abs = chart_df["Value"].abs().max()
    axis_limit = (max_abs * 1.2) if max_abs > 0 else 1
    axis_min = -axis_limit
    colors = {muni_a: "#E74C3C", muni_b: "#3B82C4"}
    fig = go.Figure()
    for muni in [muni_a, muni_b]:
        sub = chart_df[chart_df["Municipality"] == muni]
        fig.add_trace(go.Bar(
            y=sub["KPI"],
            x=sub["Value"] - axis_min,
            base=axis_min,
            orientation="h",
            name=muni,
            marker_color=colors[muni],
            text=sub["Value"].round(1),
            textposition="outside",
            customdata=sub["Value"],
            hovertemplate="%{y}: %{customdata:.1f}<extra></extra>",))
    fig.add_vline(x=0, line_dash="dash", line_color="gray")
    fig.update_layout(
        barmode="group",
        title=title,
        xaxis=dict(range=[axis_min, axis_limit], title="Value"),
        height=max(280, 70 * len(kpi_list)),
        bargap=0.3,)
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
            "Conduct patient surveys and audits to determine whether worsened healthcare outcomes are due to a lack of continuity, quality, or access in day-to-day health management and education",
            "Create centralized information and referral tracking for patients so less people become stuck in the limbo between primary care, specialists, and long term care",
            "Introduced 5-10 day follow-up standards for high-risk discharged patients in order to prevent complications and/or deterioration down the line" ],
        "Langley": [
            "Account for multi-city demand, this includes Clayton, Cloverdale, and other bordering neighbourhoods when furthering capacity and specialist availability",
            "Expand physician and emergency beds available to patients to combat high ED wait times",
            "Create reference programs between Langley, Abbotsford, Surrey, and White Rock which include updating diagnostics to divert patients during particular surge times"],
        "White Rock": [
            "Shift into a senior-focused lense, including chronic continous monitering and the expansion of staffing availability for long term care facilities ",
            "Develop a joint Surrey-White Rock demand model for Peace Arch Hospital rather than simply accounting for the health region or just White Rock's population",
            "Increase logistical and technical pathways in geriatric care between Peace Arch Hospital, long term care facilities, and specialized clinics to streamline the healthcare experience for an aging population" ],
        "Burnaby": [
            "Create dedicated programs to moniter the wait time of highly-demanded procedures in comparison to targeted benchmarks",
            "Publicize and market local chronic disease management clinics to avoid preventable ED and Primary care visits",
            "Establish bi-annual to annual capacity reviews associated with senior population growth, and determine staffing of specialists, LTC nurses, and paramedics as such"],
        "New Westminster": [
            "Develop a 10-year framework for Royal Columbian Hospital which identifies the capacity of aging infrastructure, and prioritizing upgrades that cannot be addressed by the new section",
            "Use population and senior growth projections, rather than population when planning annual service and funds",
            "Prioritize Royal Columbian as being able to serve specialty procedures where demand exceeds current capacity, rather than treating it as covering only New Westminister"],
        "Coquitlam": [
            "Expand resources on residential facilities to address the pressure on LTC facilities",
            "Target worsening physical and mental conditions through increased follow up monitering, hiring specialized physicians to ensure quality of care, and addressing nurse burnout",
            "Expansion of preventative care systems, such as bi-annual general exams, and regular screening for high-risk or chronic patients" ],
        "Port Coquitlam": [
            "Maintain current care quality through adequate re-imbursement for nurses and physicians to optimize productivity and success",
            "Preserve the fairly low vulnerable population and unmet need values by expanding preventative care systems through family physicians and health education initiatives",
            "Establish indicators that are continously monitered so potential capacity bottlenecks are addressed before they fester into a larger issue"],
        "Port Moody": [
            "Decrease turnaround time for operating rooms and increase surgical staffing to alleviate burdens on the high waits for procedures",
            "Monitor capacity planning for Eagle Ridge Hospital by taking into account regions like Anmore and Belcarra, including consideration of larger ambulatory services to make up for the vast distance",
            "Improve scheduling and referral systems for specialized consultation and care while maintaining the low demand in ED facilities" ],
        "Pitt Meadows": [
            "Collect further data on the needs, capacity, and complexity of the region in order to find true unique needs",
            "Ensure residents are able to access Ridge Meadows hospital, this includes the strengthening of services such as shuttles and ambulances",
            "Expand local clinic and consultation sites to reduce dependance on traveling out of municipality for care or assesment" ],
        "Maple Ridge": [
            "Reduce the high numbers of patient re-admission by creating stronger diagnostics to assess a patient's quality of care prior to discharge",
            "Create Fraser Health wide staff surge policies, this could look like temporary transfers in order to address certain emergencies or crisis in particular areas",
            "Improve coordination and sharing of health reports between EDs, Primary, LTCs, and residential facilities"],
        "Chilliwack": [
            "Identify common hospital services that could be safely conducted in outpatient settings/clinics and move them out of inpatient settings to alleviate acute space occupancy",
            "Track the utilization of services based on the residence of patients to determine which smaller municipalities require more outpatient supplies",
            "Calculate the minimum resource and staffing requirements based on the statistics not only within Chilliwack, but also Cultus Lake, Harrison, Agassiz etc etc"],
        "Mission": [
            "Assign dedicated 'discharge coordinators' to complex patients as soon as they arrive to minimize idle use of acute spaces",
            "Prioritize home-support and/or rehabilitation for seniors who are medically stable but would likely remain in hospital",
            "Ensure home-care, rehabilitation, and discharge coordination is available 7 days a week so patients don't have to remain in hospitals over weekends" ],
        "Hope": [
            "Expand telehealth services in rural areas with specialists in Abbotsford and Chilliwack so residents can access timely assesment rather than long travel times",
            "Establish telehealth help services in local community centers and clinics so seniors can recieve adequate access",
            "Assign local coordinators to different communities to help organize resident's follow-up appointments, rehabilitation, and managing in-home management and care"],
        "Kent": [
            "Identify the key characteristics of avoidable hospitalization in Chilliwack General and create targeted prevention campaigns to address them",
            "Standardize the process for referrals between the community health centre in Agassiz and Chilliwack to better aid patients whose conditions become more complex",
            "Expand Agassiz health centre to accomodate regular chronic disease management and outpatient patient support"]}

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
        fig_bar.update_layout(xaxis={'categoryorder': 'total descending'})
        fig_bar.update_layout(
            xaxis=dict(
            tickmode='array',
            tickvals=ranking['Municipality'],
            ticktext=ranking['Municipality'],
            tickangle=-45,),margin=dict(b=120),)
        event = st.plotly_chart(fig_bar, use_container_width=True, on_select="rerun", key="ranking_chart")
        st.markdown("Tap on a municipality for details")
        if st.button("Compare Municipalities"):
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
            st.info("The dotted line (0) represents the regional average, a positive value is higher need, a negative value is lower need")
            st.markdown("#### Compare a Specific Category")
            category_map = {
                "Population & Demographics": population_kpis,
                "Hospital Strain": hospital_strain_kpis,
                "Patient Demand": patient_demand_kpis,
                "Outcomes": outcomes_kpis,}
            chosen_category = st.selectbox("Category", list(category_map.keys()))
            kpi_fig = build_compare_kpi_chart(muni_a, muni_b, category_map[chosen_category], chosen_category)
            if kpi_fig is not None:
                st.plotly_chart(kpi_fig, width='stretch')
            else:
                st.write("No data available for this category.")

elif page == "Data and Limitations":

    st.title("Limitations")

    st.markdown("""
    <div class="cormorant-page">
    No analysis that utilizes publicly available data at a fairly amateur independent level is without flaw. The limitations page below outlines some of the major limitations and opportunities for further growth, accuracy, and recommendations for those wishing to create something similar for their own communities. It covers geographic aggregation, data quality, temporal coverage, and index construction.

    ## 1. Geographic Aggregation

    **1.1 Coarse geographic data**

    Several CIHI and surgical wait time indicators were only available at a coarser geographic level (such as HSDA or even the broader Fraser Valley). In these cases, a single uniform value was placed on every municipality, while in reality these values will likely vary. As a result, these forms of variables were weighted much lower in the interest of granularity. However, even despite this mitigation, municipalities within similar HSDA areas are bound to show very similar need indexes and variable values due to the census area overlap, while in reality there are bound to be underlying differences that would make for a far more accurate index.

    **1.2 Healthcare facility catchment areas**

    Population as a per-capita denominator was replaced with census-subdivisions across all municipalities. While this helped differentiate municipalities within the same HSDA, it fails to account for the catchment area of healthcare facilities (such as Peace Arch Hospital in White Rock, which covers a large portion of Surrey, but only accounts for White Rock in the index). As a result, the geographic accuracy of various municipalities' need scores is heavily dependent on the catchment area of its facilities. This likely explains how municipalities like Burnaby tend to score below average despite having a large population, since Burnaby General additionally covers portions of Vancouver, which don't fall under Fraser Health and are therefore ignored when selecting data.

    **1.3 Municipality consolidation**

    Smaller municipalities such as Township of Langley, Agassiz, and Harrison were consolidated into broader groups of Langley and Kent in order to maintain a consistent 16 municipalities that had ample data to calculate the index. However, by doing so, the index risks losing out on key differences from community to community and obscuring unique changes.


    ## 2. Data Quality

    **2.1 Hospital-scale bias**

    Indicators such as CIHI's Total Resource Use Intensity are heavily reliant on the scale and patient volume of a given hospital, even if smaller facilities utilize far more per patient. Since this variable was used raw rather than converted to a per-capita rate, there is still further conversation to be had as to whether bias towards larger municipalities is prevalent within the index due to the data used.

    **2.2 Suppressed or omitted data**

    Certain data from CIHI and surgical wait data is suppressed and/or omitted in accordance with data reliability and privacy policy. This results in incomplete coverage on indicators and a tendency towards lower scoring for smaller municipalities, examples of these being Port Coquitlam, Hope, and Pitt Meadows.

    **2.3 Unattributed surgical wait times**

    Some surgical wait times data was listed under all facilities and therefore could not be linked towards a particular municipality or hospital. These were excluded from the analysis in order to preserve the core function of creating a comparative index. As a result, this index may exclude or result in the incompleteness of certain procedures.


    ## 3. Temporal Coverage

    **3.1 Different reference periods**

    Data used for this index spans different reference periods based on what was readily available. For example, Stats Can's Census could only provide data from the 2021 census, while CIHI indicators reflect the most recent time-period (2024-25). As a result, the need index reflects a composite estimate of the most recent available year per source, and is not accurate to the modern day (i.e. the second half of 2026).

    **3.2 Data collection date**

    Because data was collected across the span of mid to late July and has not been updated since, this index does not reflect recent developments in certain indicators or any new facilities a municipality may have received.


    ## 4. Index Construction

    **4.1 Subjective weighting and variable selection**

    The weighting, selection, and calculation of individual variables as key performance indicators (KPIs) were determined by relative contrast and subjective judgement rather than peer-reviewed or externally validated choices. Recommendations from LLMs such as Claude and ChatGPT were also taken into account before choosing. As a result, the index is not definitive; allocating different weights would likely produce different results.

    **4.2 User-adjustable weighting**

    To address this subjectivity, an option has been added for users to change weights if they so choose and observe the changes it makes to a municipality's score in real time. The next step of this project would likely be to observe what indicators are the best at demonstrating struggle or bottlenecks in not only healthcare, but social systems as a whole. Being able to research this at a higher level with access to larger sets of data would not only help the accuracy of this index, but also its ability to spark meaningful discussion and change.
    /div>""", unsafe_allow_html=True)
    st.title("Sources")
    st.markdown("""
    <div class="cormorant-page">
    
    *Note: All data was accessed between July 14th 2026 and July 31st 2026.*

    Canadian Institute for Health Information. (2025). *Number of Acute Care Beds* [Data set]. CIHI.  
    [https://www.cihi.ca/en/indicators/number-of-acute-care-beds](https://www.cihi.ca/en/indicators/number-of-acute-care-beds)

    Canadian Institute for Health Information. (2025). *All Available Indicators* [Data set]. CIHI.  
    [https://www.cihi.ca/en/access-data-and-reports/indicator-library/download-indicator-data](https://www.cihi.ca/en/access-data-and-reports/indicator-library/download-indicator-data)

    Statistics Canada. (2022). *Census Profile of Population, 2021 Census of Fraser East Health Service Delivery Area* [Data set]. Statistics Canada Catalogue no. 98-316-X2021001.  
    [https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075921&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075921&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0)

    Statistics Canada. (2022). *Census Profile of Population, 2021 Census of Fraser South Health Service Delivery Area* [Data set]. Statistics Canada Catalogue no. 98-316-X2021001.  
    [https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075923&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075923&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0)

    Statistics Canada. (2022). *Census Profile of Population, 2021 Census of Fraser North Health Service Delivery Area* [Data set]. Statistics Canada Catalogue no. 98-316-X2021001.  
    [https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075922&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?Lang=E&SearchText=Fraser%20&DGUIDlist=2022A00075922&GENDERlist=1,2,3&STATISTIClist=1,4&HEADERlist=0)

    Open Government. (2026). *Surgical wait times* [Data set]. Government of Canada.  
    [https://open.canada.ca/data/en/dataset/7c1bf2a8-96bb-4ad5-888d-a90672eb306e](https://open.canada.ca/data/en/dataset/7c1bf2a8-96bb-4ad5-888d-a90672eb306e)

    Statistics Canada. (2025). *Open database of healthcare facilities* [Data set]. Statistics Canada.  
    [https://www.statcan.gc.ca/en/lode/databases/odhf](https://www.statcan.gc.ca/en/lode/databases/odhf)

    Statistics Canada. (2022). *Census Profile of Population, 2021 Census Profiles* [Data set sorted by geography]. Statistics Canada Catalogue no. 98-316-X2021001.  
    [https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/search-recherche/lst/results-resultats.cfm?Lang=E&GEOCODE=59](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/search-recherche/lst/results-resultats.cfm?Lang=E&GEOCODE=59)
    </div>""", unsafe_allow_html=True)
    
elif page == "Methodology":

    st.title("Methodology")

    st.markdown("""
    <div class="cormorant-page">
    This project combines publicly available hospital indicators, population demographic, and facility data into a composite need index, spanning 16 municipalities across the Fraser Valley Health Service Delivery Area (HSDA). This index is supported by an interactive tool that allows users to explore and compare results between municipalities.

    The methodology below is a guide covering resources used, data collection, data merging and integration, index building, further analysis, and designing the interactive tool.

    ## 1. Resources Used

    **1.1 OneNote or another note-taking software**

    Used to keep track of what datasets have been used, what they tell us, and when they were accessed.

    **1.2 Microsoft Excel**

    Used primarily for smaller datasets and as a preliminary way to review datasets before processing them with Python or integrating them into the index.

    **1.3 Python**

    Python was used for data processing and analysis, primarily through Pandas, NumPy, Plotly, and Text Wrap. The analysis can be conducted natively on a desktop setup or through Jupyter Notebooks via Anaconda.

    **1.4 GitHub and Streamlit**

    A GitHub repository was used to store the project code, while Streamlit was used to create the interactive web interface.


    ## 2. Data Collection

    **2.1 Datasets used**

    This project involved five different datasets:

    **2.1.1 CIHI Number of Acute Care Beds**

    Primarily used to calculate the number of acute care beds per 1,000 residents as an indicator of hospital strain.

    **2.1.2 CIHI Indicator Library**

    Provided facility-level performance data spanning 2010–2025.

    **2.1.3 Statistics Canada Census Profile of Population**

    Extracted at the HSDA level for population and at the municipal level for percentages and growth rates. This provided data on population, population growth, seniors, and children under five.

    **2.1.4 BC Surgical Waiting Times**

    Provided data on whether procedures were completed within a given timeframe, as well as median and 90th-percentile wait times.

    **2.1.5 Statistics Canada Open Database of Healthcare Facilities**

    Provided data on healthcare services available within each municipality, including ambulances, residential and long-term-care facilities, and hospital spaces.

    **2.2 Geographic scope**

    This project covers 16 municipalities within the Fraser Health region. A single region was selected rather than multiple regions in order to understand individual municipal needs in comparison with one another.

    Fraser Health was selected due to its composition of some of British Columbia's largest cities, as well as the project's connection to the region. The region was further subdivided into 16 municipalities to match individual census data and available records. Creating smaller municipalities would result in substantially more missing data and many regions that do not possess their own medical facilities.

    **2.3 Data reference periods**

    Each data source covers a different time period:

    **2.3.1 CIHI Number of Acute Care Beds:** 2024–25

    **2.3.2 CIHI Indicator Library:** 2010–2025

    **2.3.3 Statistics Canada Census of Population:** 2021, with population growth measured from 2016–2021

    **2.3.4 BC Surgical Waiting Times:** 2009–2026

    **2.3.5 Statistics Canada Open Database of Healthcare Facilities:** 2025


    ## 3. Merging and Integration

    Because each dataset used its own method of defining indicators—including hospital name, region, HSDA, or municipality name—it was necessary to standardize each dataset into the 16 municipalities before building the index.

    **3.1 Establishing a canonical municipality list**

    A canonical list of all 16 municipalities was defined as the standard unit for the project. Every dataset was mapped to follow this list prior to merging.

    **3.2 Mapping facility-level indicators**

    Facility-level indicators, such as those in CIHI's Indicator Library, were manually mapped by assigning each facility to the municipality where it was located using a lookup dictionary.

    Several smaller communities and neighbourhoods were consolidated into nearby municipalities in order to maintain consistency and avoid having more than 16 values when calling unique municipalities. For example, although the Township of Langley and Langley City are separate municipalities, they were merged into a broader "Langley" municipality.

    **3.3 Applying HSDA-level data**

    Some data, including Statistics Canada's Census data, was only available at broader HSDA levels. In these cases, a uniform value was applied to all municipalities within the respective HSDA.

    Population was an exception because it could be applied as a unique denominator for each municipality when calculating per-capita rates. Population, including seniors and children under five, was therefore extracted from census subdivisions rather than HSDA reporting.

    **3.4 Creating the master dataset**

    Once all datasets had been cleaned and standardized using municipality as the common key, they were merged into a single master table containing one row per municipality and one column per indicator.


    ## 4. Index Building

    **4.1 Z-score normalization**

    Before combining the data into a final need score, all variables were normalized using z-score normalization. This was necessary because the variables were expressed in different units, such as weeks, rates per 1,000, and percentages. Adding these values directly would allow variables with numerically larger units to disproportionately influence the index.

    **4.2 Choosing a normalization method**

    Two normalization methods were considered: min-max normalization and z-score normalization.

    Min-max normalization expresses the largest value as 100, the smallest as 0, and all other values somewhere between them. Z-score normalization instead expresses values relative to the mean, with zero representing the mean and one representing one standard deviation.

    Z-score normalization was selected because it was considered less vulnerable to the influence of outliers than min-max normalization.

    **4.3 Four conceptual pillars**

    Rather than combining every variable into one conglomerate score immediately, the variables were divided into four conceptual pillars:

    - **Patient Demand**
    - **Hospital Strain**
    - **Vulnerable Populations**
    - **Outcomes**

    Patient Demand reflects how much residents are utilizing facilities through measures such as emergency-room visits, acute care, and specialized procedures.

    Hospital Strain measures how well hospitals are managing this demand and helps identify potential bottlenecks.

    Vulnerable Populations provides context for the expected complexity and scale of care required.

    Outcomes focuses on post-hospital results and long-term care, helping assess the quality of care provided by healthcare facilities.

    Together, these pillars assess entry, process, and longer-term indicators of the Fraser Health system.

    **4.4 Weighting**

    To produce a single index score for each municipality, the four pillars must be combined. Each pillar is therefore weighted equally by default at 25% of the total score.

    Within each pillar, individual variables are assigned weights, typically between 5% and 25%, based on their granularity and subjective assessment of importance.

    Users can modify both pillar weights and individual variable weights through the interactive tool.


    ## 5. Further Analysis

    **5.1 K-means clustering**

    Beyond the need-score index, the municipalities were analyzed using clustering. This helps demonstrate that healthcare need can take different forms—for example, vulnerable populations may require different resources from municipalities experiencing worsening outcomes.

    **5.2 Four-dimensional clustering**

    K-means clustering was used to group municipalities according to their four pillar scores. Each municipality can be thought of as a point in a four-dimensional space, with each dimension representing one pillar.

    K-means groups municipalities that are close together in this four-dimensional space, meaning municipalities with similar combinations of pillar scores are grouped together.

    This differs from the index because the clustering algorithm identifies groups based on profile similarity rather than a subjective definition of what constitutes need. However, the scores used by the algorithm are still influenced by the subjective weighting decisions used in the index.

    **5.3 Selecting the number of clusters**

    The number of clusters was determined using two complementary methods: the elbow method and silhouette scoring.

    The elbow method identifies the point at which adding additional clusters produces diminishing improvements in cluster similarity. Silhouette scoring measures how well-separated the resulting clusters are.

    Both methods indicated that five or more clusters would provide little additional benefit. Given the relatively small dataset of 16 municipalities, three clusters were ultimately selected.

    **5.4 Naming the clusters**

    Once the final clusters were defined, the average pillar values within each cluster were compared. Each cluster was then given a plain-language name summarizing its characteristics:

    - **High Pressure Systems**
    - **Vulnerable Populations + Adequate Capacity**
    - **Baseline, Moderate Need**


    ## 6. Designing the Interactive Tool

    **6.1 Purpose of the interactive tool**

    The culmination of the index was an interactive web application that allows users to visualize and explore different variables and pillars, read municipality-specific insights and recommendations, and compare analytics between municipalities.

    An interactive tool was selected instead of a static report to maintain a degree of customization and encourage exploration.

    **6.2 Core features**

    The application includes:

    **6.2.1 Municipality ranking**

    A graph ranking the final need score of each municipality.

    **6.2.2 Live reweighting**

    Users can modify pillar weights and, through advanced settings, individual variable weights.

    **6.2.3 Municipality comparison**

    A comparative page allows users to compare the values of two municipalities.

    **6.2.4 Municipality detail pages**

    Each municipality has a detail page containing an insight/blurb and policy recommendations based on notable statistics.

    **6.2.5 Analytics page**

    A separate analytics page shows how each municipality's statistics compare with other municipalities using percentile rankings.

    **6.3 Intended users**

    The web application was designed to work alongside policymakers, analysts, and grassroots organizations working with data to support resource-allocation decisions and arguments for changes to existing policy.

    As a result, features such as municipality-specific insights, policy recommendations, and accessible bar graphs were selected to prioritize aesthetic and functional simplicity.
    </div>
    """, unsafe_allow_html=True)
