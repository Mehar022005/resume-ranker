# app/main.py
import streamlit as st
import os
from utils.parser import parse_resume
from utils.scorer import rank_resumes
from utils.visuals import plot_scores, show_heatmap

st.set_page_config(page_title="AI Resume Ranker", layout="wide")

# Header Section
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🤖 AI-Powered Resume Ranker</h1>
    <p style='text-align: center; font-size: 18px;'>Upload resumes and compare them against your job description using smart AI scoring</p>
""", unsafe_allow_html=True)

# Input Section
with st.container():
    st.markdown("### 📝 Job Description")
    job_text = st.text_area("Paste the Job Description below", height=200)

    st.markdown("### 📄 Upload Resumes")
    resume_files = st.file_uploader("Upload one or more resumes (PDF format)", type=["pdf"], accept_multiple_files=True)

# Process Section
if job_text and resume_files:
    with st.spinner("⚙️ Processing resumes and ranking..."):
        resumes = []
        names = []
        for file in resume_files:
            text = parse_resume(file)
            resumes.append(text)
            names.append(file.name)

        results_df, skill_matrix = rank_resumes(resumes, job_text, names)

    st.success("✅ Ranking Complete!")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📊 Resume Ranking Scores")
        st.dataframe(results_df)
        st.pyplot(plot_scores(results_df))

    with col2:
        show_heatmap(skill_matrix, names)

    st.download_button("📥 Download CSV Report", results_df.to_csv(index=False), "ranked_resumes.csv")

else:
    st.info("⬆️ Please enter a job description and upload at least one resume to begin.")
