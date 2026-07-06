import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Deepak Baskar N | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1F2937;
        border-bottom: 2px solid #3B82F6;
        padding-bottom: 0.3rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .job-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2563EB;
    }
    .company-info {
        font-size: 1rem;
        font-style: italic;
        color: #6B7280;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation & Contact
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Deepak Baskar N") # Replace with your actual image URL or local path
    st.markdown("### 📬 Contact Info")
    st.markdown("- **Email:** baskardeepak27@gmail.com")[cite: 1]
    st.markdown("- **Phone:** +91 9965463281")[cite: 1]
    st.markdown("- **Location:** Anaimalai, Tamil Nadu, India")[cite: 1]
    st.markdown("---")
    st.markdown("[🔗 LinkedIn](https://linkedin.com) | [💻 GitHub](https://github.com)")[cite: 1]
    
    st.markdown("---")
    navigation = st.radio(
        "Go to Section:",
        ["About Me", "Technical Skills", "Experience", "Projects", "Education & Certifications"]
    )

# 4. Content Logic Based on Navigation
if navigation == "About Me":
    st.markdown('<div class="main-title">Deepak Baskar N</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Driven Cloud & Data Solutions Engineer</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">🚀 Profile Summary</div>', unsafe_allow_html=True)
    st.write(
        "Technology professional with experience in Salesforce CRM Cloud, API testing, and application support. "[cite: 1]
        "Skilled in Postman, Salesforce Health Cloud, and Lightning Web Components (LWC). "[cite: 1]
        "Possess basic knowledge of ERPNext Inventory, Sales, and HR modules. "[cite: 1]
        "Certified in Data Science (GUVI-IIT Madras) with proficiency in Python, SQL, and Power BI. "[cite: 1]
        "Passionate about Software Testing, Technical Support, DSPy, Prompt Engineering, and AI-driven solutions."[cite: 1]
    )

elif navigation == "Technical Skills":
    st.markdown('<div class="section-header">🛠️ Technical Toolkit</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### **Cloud & Business Applications**")
        st.markdown("- **CRM:** Salesforce CRM Cloud, Salesforce Health Cloud")[cite: 1]
        st.markdown("- **Frontend:** Lightning Web Components (LWC)")[cite: 1]
        st.markdown("- **ERP:** ERPNext (Functional Support, Workflow Configuration, Module Support)")[cite: 1]
        st.markdown("- **API Testing:** Postman")[cite: 1]
        
        st.markdown("### **Programming & Databases**")
        st.markdown("- **Languages:** Python")[cite: 1]
        st.markdown("- **Databases:** SQL, MySQL")[cite: 1]

    with col2:
        st.markdown("### **AI / ML & Deep Learning**")
        st.markdown("- **Frameworks:** Scikit-learn, TensorFlow, PyTorch")[cite: 1]
        st.markdown("- **Domains:** NLP, Computer Vision")[cite: 1]
        st.markdown("- **Advanced AI:** DSPy, Prompt Engineering")[cite: 1]
        
        st.markdown("### **Data Analysis & Deployment**")
        st.markdown("- **Analysis:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Power BI, Excel")[cite: 1]
        st.markdown("- **Deployment/Tools:** Streamlit, AWS, VS Code, GitHub")[cite: 1]

elif navigation == "Experience":
    st.markdown('<div class="section-header">💼 Professional Experience</div>', unsafe_allow_html=True)
    
    # Job 1
    st.markdown('<div class="job-title">Developer Internship</div>', unsafe_allow_html=True)
    st.markdown('<div class="company-info">Conuxt | 05/2026 - Present | Pollachi</div>', unsafe_allow_html=True)
    st.markdown(
        "- Worked with Salesforce CRM Cloud, gaining experience in CRM workflows, cloud solutions, and business processes.\n"[cite: 1]
        "- Performed API testing and validation using Postman, ensuring successful system integrations and data flow.\n"[cite: 1]
        "- Explored Salesforce Health Cloud and healthcare CRM functionalities, including patient-centric workflows.\n"[cite: 1]
        "- Developed technical skills in Lightning Web Components (LWC), DSPy, and Prompt Engineering for AI-powered application development."[cite: 1]
    )
    st.markdown(" ")

    # Job 2
    st.markdown('<div class="job-title">Junior Full Stack Developer (ERPNext Functional Support)</div>', unsafe_allow_html=True)
    st.markdown('<div class="company-info">Makto Technology | 01/2026 - 02/2026 | Coimbatore</div>', unsafe_allow_html=True)
    st.markdown(
        "- Gathered client requirements and configured workflows for ERPNext Yarn and Fabric modules.\n"[cite: 1]
        "- Supported system setup and provided backend support including data management and issue troubleshooting.\n"[cite: 1]
        "- Coordinated with stakeholders to resolve issues and ensure smooth implementation."[cite: 1]
    )
    st.markdown(" ")

    # Job 3
    st.markdown('<div class="job-title">Medical Billing Specialist</div>', unsafe_allow_html=True)
    st.markdown('<div class="company-info">RND Softech Pvt. Ltd | 05/2024 - 06/2025 | Coimbatore</div>', unsafe_allow_html=True)
    st.markdown(
        "- Verified eligibility and processed DME machine and supply resupply requests.\n"[cite: 1]
        "- Checked resupply quantities, monthly supply limits, and patient notes for any changes.\n"[cite: 1]
        "- Worked as a quality checker, maintaining high process accuracy through diligent checks."[cite: 1]
    )

elif navigation == "Projects":
    st.markdown('<div class="section-header">🔬 Engineering Projects</div>', unsafe_allow_html=True)
    
    # Project 1
    with st.expander("🤖 Hyperlocal News Anomaly Detection & Source Attribution (AWS)", expanded=True):
        st.markdown("**Technologies:** BERT, RoBERTa, NLP, Isolation Forest, Autoencoder, Streamlit, AWS")[cite: 1]
        st.markdown(
            "- Troubleshot AWS deployment issues including service configuration, application access errors, and runtime failures.\n"[cite: 1]
            "- Monitored application logs and resolved data processing and connectivity issues to maintain system stability.\n"[cite: 1]
            "- Developed an NLP-driven solution to detect abnormal news patterns and identify source credibility.\n"[cite: 1]
            "- Implemented a real-time dashboard for monitoring anomalies and regional content behavior using machine learning models."[cite: 1]
        )
        
    # Project 2
    with st.expander("📊 Content Monetization Modeler", expanded=True):
        st.markdown("**Technologies:** Scikit-learn, Regression Models, EDA, Feature Engineering, Data Visualization, Streamlit")[cite: 1]
        st.markdown(
            "- Resolved environment and dependency issues during Python library installation and Streamlit deployment.\n"[cite: 1]
            "- Diagnosed data loading and application runtime errors, ensuring smooth execution of the prediction interface.\n"[cite: 1]
            "- Built a regression-based system to estimate video revenue using engagement and performance metrics.\n"[cite: 1]
            "- Developed an interactive Streamlit application allowing users to input parameters and view revenue predictions."[cite: 1]
        )

elif navigation == "Education & Certifications":
    st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
    
    st.markdown("**Advanced Programming Professional & Master Data Science**")[cite: 1]
    st.caption("GUVI - IIT Madras | 06/2025 - 10/2025 | Chennai")[cite: 1]
    st.markdown(" ")
    st.markdown("**Bachelor of Computer Applications (BCA)**")[cite: 1]
    st.caption("Nallamuthu Gounder Mahalingam College | 07/2021 - 05/2024 | Pollachi")[cite: 1]
    
    st.markdown('<div class="section-header">📜 Certifications</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🐍 **Python**\n\nIssued by GUVI")[cite: 1]
    with col2:
        st.info("🛢️ **MySQL**\n\nIssued by GUVI")[cite: 1]
    with col3:
        st.info("📊 **Power BI**\n\nIssued by Simplilearn")[cite: 1]
