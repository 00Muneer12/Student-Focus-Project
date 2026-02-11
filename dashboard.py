import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Focus Analyzer",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e6e6e6;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.metric-box {
    background: white;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #e6e6e6;
    text-align: center;
    transition: 0.3s;
}

.metric-box:hover {
    border-color: #4CAF50;
    transform: scale(1.03);
}

.title-text {
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title-text">🎯 Student Focus Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze mood, phone usage and study duration impact on focus</div>', unsafe_allow_html=True)

st.write("")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("student_focus_data.csv")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Filter Data")

phone_filter = st.sidebar.selectbox(
    "Phone Usage",
    ["All", "No Phone", "Phone Used"]
)

if phone_filter == "No Phone":
    df = df[df["phone_used"] == 0]
elif phone_filter == "Phone Used":
    df = df[df["phone_used"] == 1]

# ---------------- SMART METRIC BOXES ----------------
col1, col2, col3 = st.columns(3)

avg_focus = round(df["focus_level"].mean(), 2)
avg_mood = round(df["mood"].mean(), 2)
avg_duration = round(df["duration_min"].mean(), 2)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <h3>Average Focus</h3>
        <h1>{avg_focus}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <h3>Average Mood</h3>
        <h1>{avg_mood}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <h3>Avg Study Duration</h3>
        <h1>{avg_duration} min</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- DATA PREVIEW CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Dataset Preview")
st.dataframe(df)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Focus Level Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["focus_level"], bins=5, ax=ax1)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Mood vs Focus")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="mood", y="focus_level", data=df, ax=ax2)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📱 Phone Usage vs Focus")
fig3, ax3 = plt.subplots()
sns.boxplot(x="phone_used", y="focus_level", data=df, ax=ax3)
st.pyplot(fig3)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.success("✅ Dashboard running successfully!")
