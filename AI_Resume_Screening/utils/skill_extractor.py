import re
from typing import List

DEFAULT_SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "C++",
    "C#",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Flask",
    "Django",
    "Streamlit",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "Git",
    "Docker",
    "AWS",
    "Azure",
    "Linux",
    "Machine Learning",
    "Deep Learning",
    "Data Analysis",
    "API Development",
    "REST",
    "Microservices",
    "Pytest",
    "Jira",
    "Agile",
]


def extract_skills(text: str) -> List[str]:
    """Extract likely skills from resume text using a keyword-based approach."""
    if not text:
        return []

    normalized_text = text.lower()
    found_skills: List[str] = []

    for skill in DEFAULT_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, normalized_text):
            found_skills.append(skill)

    return found_skills


__all__ = ["DEFAULT_SKILLS", "extract_skills"]
