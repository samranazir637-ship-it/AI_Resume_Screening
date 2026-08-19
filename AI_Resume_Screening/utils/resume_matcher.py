import re
from typing import Dict, List

from utils.skill_extractor import DEFAULT_SKILLS, extract_skills


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def score_resume(resume_text: str, job_description: str) -> Dict[str, object]:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = [skill for skill in job_skills if skill in resume_skills]
    matched_skills = sorted(matched_skills, key=lambda item: item.lower())
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]
    missing_skills = sorted(missing_skills, key=lambda item: item.lower())

    if not job_skills:
        score = 0
    else:
        score = round((len(matched_skills) / len(job_skills)) * 100)

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
    }


def rank_candidates(resumes: List[Dict[str, str]], job_description: str) -> List[Dict[str, object]]:
    ranked = []
    for resume in resumes:
        result = score_resume(resume["text"], job_description)
        ranked.append(
            {
                "candidate_name": resume.get("name", "Unknown Candidate"),
                "score": result["score"],
                "matched_skills": result["matched_skills"],
                "missing_skills": result["missing_skills"],
            }
        )

    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked
