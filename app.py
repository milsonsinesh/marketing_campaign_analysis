import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ---------------- CONFIGURATION ----------------
st.set_page_config(
    page_title="Marketing Campaign Analytics",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    path = "data/marketing_final.csv"
    if not os.path.exists(path):
        st.error("❌ marketing_final.csv not found. Run data_cleaning.py and segmentation.py first.")
        st.stop()
    return pd.read_csv(path)

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Filters")

country = st.sidebar.multiselect(
    "Country",
    options=sorted(df['Country'].dropna().unique())
)

education = st.sidebar.multiselect(
    "Education",
    options=sorted(df['Education'].dropna().unique())
)

marital = st.sidebar.multiselect(
    "Marital Status",
    options=sorted(df['Marital_Status'].dropna().unique())
)

if country:
    df = df[df['Country'].isin(country)]
if education:
    df = df[df['Education'].isin(education)]
if marital:
    df = df[df['Marital_Status'].isin(marital)]

st.sidebar.markdown("---")
st.sidebar.info("Use filters to explore customer behavior")

# ---------------- TITLE ----------------
st.title("📊 Marketing Campaign Analytics Dashboard")
st.caption("Customer Segmentation & Campaign Performance Analysis")

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Customers", f"{len(df):,}")
col2.metric("✅ Response Rate", f"{df['Response'].mean()*100:.2f}%")
col3.metric("💰 Avg Spend", f"₹{df['Total_Spend'].mean():,.0f}")
col4.metric("🌐 Avg Web Visits", f"{df['NumWebVisitsMonth'].mean():.1f}")

st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📈 Overview", "🧩 Segments", "🛒 Channels"])

# ============ TAB 1: OVERVIEW ============
with tab1:
    st.subheader("Customer Spending vs Age")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Age",
        y="Total_Spend",
        hue="Response",
        palette="Set2",
        ax=ax
    )
    ax.set_xlabel("Age")
    ax.set_ylabel("Total Spend")
    st.pyplot(fig)

    st.info("📌 Customers who respond to campaigns generally spend more.")

# ============ TAB 2: SEGMENTS ============
with tab2:
    st.subheader("Segment-wise Average Spend")

    segment_data = df.groupby("High_Spender")["Total_Spend"].mean().reset_index()
    segment_data["High_Spender"] = segment_data["High_Spender"].map({0: "Others", 1: "High Spenders"})

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=segment_data,
        x="High_Spender",
        y="Total_Spend",
        palette="Blues",
        ax=ax
    )
    ax.set_xlabel("Segment")
    ax.set_ylabel("Average Spend")
    st.pyplot(fig)

    st.success("🎯 High spenders contribute significantly more revenue.")

# ============ TAB 3: CHANNELS ============
with tab3:
    st.subheader("Web Visits vs Campaign Response")

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(
        data=df,
        x="Response",
        y="NumWebVisitsMonth",
        palette="Set3",
        ax=ax
    )
    ax.set_xlabel("Campaign Response (0 = No, 1 = Yes)")
    ax.set_ylabel("Web Visits per Month")
    st.pyplot(fig)

    st.warning("⚠️ Some customers visit the website often but do not respond — conversion opportunity.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption(
    "📘 Built using Python, Pandas & Streamlit | Marketing Campaign Analytics Project"
)

