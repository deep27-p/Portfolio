import streamlit as st

# Page Configuration
st.set_page_config(page_title="Deepak Baskar - Portfolio", page_icon="📊", layout="wide")

# Sidebar Contact Info
with st.sidebar:
    st.title("Deepak Baskar N")
    st.write("📍 Anamalai, Tamil Nadu, India")
    st.write("📧 baskardeepak27@gmail.com")
    st.write("📞 9965463281")
    st.markdown("[🔗 LinkedIn](https://linkedin.com) | [🔗 GitHub](https://github.com)")
    st.write("---")
    st.caption("Built entirely with Python & Streamlit")

# Main Header
st.title("🚀 ERPNext Consultant & Data Science Professional")
st.write(
    "Dynamic and analytical professional with a unique blend of experience as an **ERPNext Trainee/Support Specialist** "
    "and a trained **Data Science Professional (GUVI-IIT Madras)**."
)

st.write("---")

# Skills Section
st.header("🛠️ Technical Skill Set")
col1, col2 = st.columns(2)

with col1:
    st.subheader("ERP & Databases")
    st.write("- **ERPNext** (Functional Support, Workflow, Module Configuration)")
    st.write("- **Databases:** SQL, MySQL")
    st.write("- **Core:** Python, Excel")

with col2:
    st.subheader("Data Science & Deployment")
    st.write("- **AI/ML:** Scikit-learn, TensorFlow, PyTorch, NLP (BERT, RoBERTa)")
    st.write("- **Analytics:** Pandas, NumPy, Matplotlib, Seaborn, Power BI")
    st.write("- **DevOps/Tools:** Streamlit, AWS, VS Code, GitHub")

st.write("---")

# Experience Section
st.header("💼 Professional Experience")

st.subheader("Junior Full Stack Developer (ERPNext Functional Support)")
st.caption("Makto Technology | Coimbatore | 01/2026 – 02/2026")
st.write("- Gathered complex client requirements and configured tailored workflows for ERPNext Yarn and Fabric modules.")
st.write("- Managed system setup and provided robust backend support, including data management and critical issue troubleshooting.")

st.subheader("Medical Billing Specialist")
st.caption("RND Softech Pvt. Ltd | Coimbatore | 05/2024 – 06/2025")
st.write("- Served as a Quality Checker, maintaining exceptionally high process accuracy through diligent, detail-oriented checks.")

st.write("---")

# Projects Section
st.header("💻 Technical Projects")

with st.expander("📊 Content Monetization Modeler"):
    st.write("**Tech Stack:** Python, Scikit-learn, Regression Models, EDA, Streamlit")
    st.write("- Built a regression-based machine learning system to estimate video revenue using engagement metrics.")
    st.write("- Developed an interactive Streamlit application allowing users to view real-time revenue predictions.")

with st.expander("🔍 Hyperlocal News Anomaly Detection & Source Attribution"):
    st.write("**Tech Stack:** BERT, RoBERTa, NLP, Isolation Forest, Streamlit, AWS")
    st.write("- Developed an NLP-driven solution to detect abnormal news patterns and identify source credibility.")
    st.write("- Deployed the solution on AWS and monitored system logs to ensure stability.")