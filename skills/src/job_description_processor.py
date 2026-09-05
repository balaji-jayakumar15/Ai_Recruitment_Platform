import re
import json


# Skills that our system can identify
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


# Words that indicate a preferred / optional skill
PREFERRED_KEYWORDS = [
    "preferred",
    "nice to have",
    "good to have",
    "optional",
    "plus",
    "bonus"
]


def skill_found(skill, text):
    """
    Check whether a skill exists in the given text.
    """

    skill = skill.lower()

    # Special handling for skills containing symbols
    if skill in ["c++", "c#"]:
        return re.search(re.escape(skill), text) is not None

    if skill == "node.js":
        return re.search(r"\bnode\.js\b", text) is not None

    if skill == "rest api":
        return re.search(r"\brest\s+api\b", text) is not None

    # Normal skills
    pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

    return re.search(pattern, text) is not None


def extract_skills_from_sentence(sentence):
    """
    Extract skills from one sentence.
    """

    found_skills = []

    sentence = sentence.lower()

    for skill in SKILLS:
        if skill_found(skill, sentence):
            found_skills.append(skill)

    return found_skills


def extract_job_requirements(job_description):
    """
    Extract required and preferred skills from a job description.
    """

    text = job_description.lower()

    required_skills = []
    preferred_skills = []

    # Split job description into sentences/lines
    sentences = re.split(r"[.!?\n]+", text)

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        skills_in_sentence = extract_skills_from_sentence(sentence)

        # Check whether the sentence indicates preferred skills
        is_preferred = any(
            keyword in sentence
            for keyword in PREFERRED_KEYWORDS
        )

        if is_preferred:
            preferred_skills.extend(skills_in_sentence)
        else:
            required_skills.extend(skills_in_sentence)

    # Remove duplicates and sort
    required_skills = sorted(set(required_skills))
    preferred_skills = sorted(set(preferred_skills))

    # If a skill exists in both lists, keep it as required
    preferred_skills = [
        skill
        for skill in preferred_skills
        if skill not in required_skills
    ]

    return required_skills, preferred_skills


def process_job_description(job_title, job_description):
    """
    Create final structured Job Description output.
    """

    required_skills, preferred_skills = extract_job_requirements(
        job_description
    )

    result = {
        "job_title": job_title,
        "required_skills": required_skills,
        "preferred_skills": preferred_skills
    }

    return result


if __name__ == "__main__":

    job_title = "Python Developer"

    job_description = """
    We are looking for a Python Developer with
    Django, FastAPI, SQL and REST API experience.
    Knowledge of Git and GitHub is preferred.
    """

    result = process_job_description(
        job_title,
        job_description
    )

    print("\nJob Description Processing Result:")
    print(json.dumps(result, indent=2))