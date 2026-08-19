import streamlit as st
from utils.pdf_reader import extract_document_text
from utils.resume_matcher import rank_candidates, score_resume
from utils.skill_extractor import extract_skills

st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.title("📄 Intelligent Resume Screening System")
st.caption("Week 1 AI-powered resume screening workflow")

col1, col2 = st.columns([1, 1])
with col1:
    uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
with col2:
    job_description = st.text_area(
        "Job Description",
        value="Looking for a Python developer with SQL, Docker, and API development experience.",
        height=180,
    )

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    resume_text = extract_document_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=250)

    skills = extract_skills(resume_text)
    st.subheader("Detected Skills")
    if skills:
        st.write("• " + "\n• ".join(skills))
    else:
        st.warning("No skills found.")

    if job_description.strip():
        match_result = score_resume(resume_text, job_description)
        st.subheader("Match Summary")
        st.metric("Compatibility Score", f"{match_result['score']}%")
        st.progress(int(match_result["score"]) / 100)
        st.write("Matched Skills:", match_result["matched_skills"])
        st.write("Missing Skills:", match_result["missing_skills"])

        st.download_button(
            label="Export Result as TXT",
            data=(
                f"Candidate Score: {match_result['score']}%\n"
                f"Matched Skills: {', '.join(match_result['matched_skills']) or 'None'}\n"
                f"Missing Skills: {', '.join(match_result['missing_skills']) or 'None'}"
            ),
            file_name="resume_match_result.txt",
            mime="text/plain",
        )
else:
    st.info("Upload a PDF resume to begin screening.")

st.markdown("---")
st.subheader("Candidate Ranking Demo")
example_resumes = [
    {"name": "Alice Johnson", "text": "Python developer with SQL and Docker experience."},
    {"name": "Bob Chen", "text": "Java engineer with REST APIs and AWS experience."},
    {"name": "Carlos Rivera", "text": "Data scientist using Python, Pandas, and Machine Learning."},
]
ranked = rank_candidates(example_resumes, job_description)
for item in ranked:
    st.write(f"{item['candidate_name']} — {item['score']}%")
    st.caption(f"Matched: {', '.join(item['matched_skills']) or 'None'}")
    st.progress(min(1.0, item['score'] / 100))