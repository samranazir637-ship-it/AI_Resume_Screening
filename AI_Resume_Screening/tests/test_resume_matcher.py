from utils.resume_matcher import score_resume
from utils.skill_extractor import extract_skills


def test_extract_skills_finds_common_technologies():
    text = "I have worked with Python, SQL, and Docker for backend projects."
    skills = extract_skills(text)

    assert "Python" in skills
    assert "SQL" in skills
    assert "Docker" in skills


def test_score_resume_ranks_relevant_candidates():
    resume_text = "Experienced Python developer with SQL and Docker expertise."
    job_description = "Need a Python engineer with SQL and Docker experience."

    result = score_resume(resume_text, job_description)

    assert result["score"] >= 70
    assert result["matched_skills"] == ["Docker", "Python", "SQL"]
