import re
import json


SKILLS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "django",
    "flask",
    "fastapi",
    "spring boot",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "github",
    "rest api",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "pytorch"
]


def extract_required_skills(job_description):
    text = job_description.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))

if __name__ == "__main__":

    job_description = """
    We are looking for a Python Developer with
    Django, FastAPI, SQL and REST API experience.
    Knowledge of Git and GitHub is preferred.
    """

    required_skills = extract_required_skills(job_description)

    result = {"job_title": "Python Developer", "required_skills": required_skills}

    print(json.dumps(result,indent=2))