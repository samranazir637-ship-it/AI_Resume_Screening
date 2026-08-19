import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask",
    "machine learning",
    "deep learning",
    "data analysis",
    "pandas",
    "numpy",
    "git",
    "docker",
    "aws"
]

def extract_skills(text):
    doc = nlp(text.lower())

    found_skills = []

    for skill in skills_list:
        if skill in doc.text:
            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))