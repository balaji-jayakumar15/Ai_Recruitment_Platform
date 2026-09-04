import json
import re
from pathlib import Path


# ---------------------------------------------------------
# 1. SKILL ALIASES
# Different names → One standard skill name
# ---------------------------------------------------------

SKILL_ALIASES = {

    # ---------------- PROGRAMMING LANGUAGES ----------------
    "py": "Python",
    "python3": "Python",
    "python 3": "Python",

    "js": "JavaScript",
    "javascript": "JavaScript",
    "java script": "JavaScript",

    "ts": "TypeScript",
    "type script": "TypeScript",

    "cpp": "C++",
    "c plus plus": "C++",

    "csharp": "C#",
    "c sharp": "C#",

    # ---------------- WEB DEVELOPMENT ----------------
    "html5": "HTML",
    "html 5": "HTML",

    "css3": "CSS",
    "css 3": "CSS",

    "reactjs": "React",
    "react js": "React",
    "react.js": "React",

    "angularjs": "Angular",
    "angular js": "Angular",

    "vuejs": "Vue.js",
    "vue js": "Vue.js",
    "vue": "Vue.js",

    "nodejs": "Node.js",
    "node js": "Node.js",
    "node.js": "Node.js",

    "expressjs": "Express.js",
    "express js": "Express.js",
    "express.js": "Express.js",

    "bootstrap css": "Bootstrap",

    "tailwindcss": "Tailwind CSS",
    "tailwind": "Tailwind CSS",

    # ---------------- DATABASES ----------------
    "sql": "SQL",

    "mysql": "MySQL",
    "my sql": "MySQL",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "postgre sql": "PostgreSQL",

    "mongo": "MongoDB",
    "mongodb": "MongoDB",

    "sqlite3": "SQLite",
    "sqlite": "SQLite",

    "oracle db": "Oracle",
    "oracle database": "Oracle",

    # ---------------- MACHINE LEARNING / AI ----------------
    "ml": "Machine Learning",
    "machine-learning": "Machine Learning",
    "machinelearning": "Machine Learning",

    "dl": "Deep Learning",
    "deep-learning": "Deep Learning",
    "deeplearning": "Deep Learning",

    "nlp": "Natural Language Processing",
    "natural-language-processing": "Natural Language Processing",

    "cv": "Computer Vision",
    "computer-vision": "Computer Vision",

    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",
    "scikit-learn": "Scikit-learn",

    "tensorflow": "TensorFlow",
    "tensor flow": "TensorFlow",

    "pytorch": "PyTorch",
    "py torch": "PyTorch",

    "keras": "Keras",

    # ---------------- DATA ANALYTICS ----------------
    "powerbi": "Power BI",
    "power bi": "Power BI",

    "ms excel": "Excel",
    "microsoft excel": "Excel",

    "tableau desktop": "Tableau",

    "pandas": "Pandas",

    "numpy": "NumPy",
    "num py": "NumPy",

    "matplotlib": "Matplotlib",

    "seaborn": "Seaborn",

    # ---------------- BACKEND ----------------
    "fast api": "FastAPI",
    "fastapi": "FastAPI",

    "flask": "Flask",

    "django": "Django",

    "springboot": "Spring Boot",
    "spring boot": "Spring Boot",

    # ---------------- CLOUD / DEVOPS ----------------
    "amazon web services": "AWS",
    "amazon aws": "AWS",
    "aws": "AWS",

    "microsoft azure": "Azure",
    "azure cloud": "Azure",
    "azure": "Azure",

    "google cloud platform": "Google Cloud",
    "google cloud": "Google Cloud",
    "gcp": "Google Cloud",

    "docker": "Docker",

    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",

    # ---------------- TOOLS ----------------
    "git hub": "GitHub",
    "github": "GitHub",

    "git": "Git",

    "visual studio code": "VS Code",
    "vs code": "VS Code",
    "vscode": "VS Code",

    "jupyter": "Jupyter Notebook",
    "jupyter notebook": "Jupyter Notebook"
}


# ---------------------------------------------------------
# 2. CLEAN SKILL TEXT
# ---------------------------------------------------------

def clean_skill(skill):
    """
    Clean a skill before normalization.

    Example:
        '  Python3  ' → 'python3'
        'React   JS' → 'react js'
    """

    if not isinstance(skill, str):
        return ""

    # Remove leading/trailing spaces
    skill = skill.strip()

    # Convert multiple spaces into one
    skill = re.sub(r"\s+", " ", skill)

    # Convert to lowercase
    skill = skill.lower()

    return skill


# ---------------------------------------------------------
# 3. NORMALIZE ONE SKILL
# ---------------------------------------------------------

def normalize_skill(skill):
    """
    Convert a skill variation into its standard name.

    Example:
        Python3 → Python
        JS → JavaScript
        ReactJS → React
        ML → Machine Learning
    """

    cleaned_skill = clean_skill(skill)

    if not cleaned_skill:
        return ""

    # Check alias dictionary
    if cleaned_skill in SKILL_ALIASES:
        return SKILL_ALIASES[cleaned_skill]

    # If no alias exists, return original skill
    # with first letter capitalization
    return skill.strip()


# ---------------------------------------------------------
# 4. NORMALIZE MULTIPLE SKILLS
# ---------------------------------------------------------

def normalize_skills(skills):
    """
    Normalize a list of skills and remove duplicates.

    Example:

        ["Python3", "Python", "JS", "JavaScript"]

    becomes:

        ["Python", "JavaScript"]
    """

    if not isinstance(skills, list):
        return []

    normalized_skills = []

    for skill in skills:

        if not isinstance(skill, str) or not skill.strip():
            continue

        standard_skill = normalize_skill(skill)

        if not standard_skill:
            continue

        # Case-insensitive duplicate checking
        already_exists = any(
            existing.lower() == standard_skill.lower()
            for existing in normalized_skills
        )

        if not already_exists:
            normalized_skills.append(standard_skill)

    return normalized_skills


# ---------------------------------------------------------
# 5. LOAD SKILL DICTIONARY FROM skills.json
# ---------------------------------------------------------

def load_skill_dictionary():
    """
    Load all standard skills from skills.json.
    """

    current_folder = Path(__file__).parent

    skills_file = current_folder.parent  /  "skills.json"

    try:

        with open(skills_file, "r", encoding="utf-8") as file:
            skill_data = json.load(file)

        all_skills = []

        for category, skills in skill_data.items():

            if isinstance(skills, list):

                for skill in skills:

                    if skill not in all_skills:
                        all_skills.append(skill)

        return all_skills

    except FileNotFoundError:

        print("Error: skills.json not found.")
        return []

    except json.JSONDecodeError:

        print("Error: skills.json contains invalid JSON.")
        return []


# ---------------------------------------------------------
# 6. CHECK WHETHER A SKILL EXISTS IN OUR DICTIONARY
# ---------------------------------------------------------

def is_known_skill(skill):
    """
    Check whether a skill belongs to our skill dictionary.
    """

    standard_skill = normalize_skill(skill)

    all_skills = load_skill_dictionary()

    return any(
        known_skill.lower() == standard_skill.lower()
        for known_skill in all_skills
    )


# ---------------------------------------------------------
# 7. NORMALIZE AND VALIDATE SKILLS
# ---------------------------------------------------------

def normalize_and_validate_skills(skills):
    """
    Normalize skills and check them against skills.json.
    """

    normalized = normalize_skills(skills)

    valid_skills = []
    unknown_skills = []

    all_skills = load_skill_dictionary()

    for skill in normalized:

        matched_skill = None

        for known_skill in all_skills:

            if known_skill.lower() == skill.lower():
                matched_skill = known_skill
                break

        if matched_skill:
            valid_skills.append(matched_skill)

        else:
            unknown_skills.append(skill)

    return {
        "valid_skills": valid_skills,
        "unknown_skills": unknown_skills
    }


# ---------------------------------------------------------
# 8. TEST FUNCTION
# ---------------------------------------------------------

def test_normalizer():

    print("=" * 60)
    print("MEMBER 3 - SKILL NORMALIZATION TEST")
    print("=" * 60)

    test_skills = [
        "Python3",
        "python",
        "PY",
        "JS",
        "javascript",
        "Java Script",
        "ReactJS",
        "React.js",
        "react js",
        "ML",
        "machine-learning",
        "NLP",
        "PowerBI",
        "My SQL",
        "Postgre SQL",
        "cpp",
        "C Plus Plus",
        "NodeJS",
        "Git Hub",
        "VSCode"
    ]

    print("\nOriginal Skills:")
    print(test_skills)

    print("\nNormalized Skills:")

    normalized = normalize_skills(test_skills)

    for skill in normalized:
        print("→", skill)

    print("\nTotal Original Skills:", len(test_skills))
    print("Total Unique Skills:", len(normalized))

    print("\nValidation Result:")

    result = normalize_and_validate_skills(normalized)

    print("\nValid Skills:")
    for skill in result["valid_skills"]:
        print("✓", skill)

    print("\nUnknown Skills:")
    for skill in result["unknown_skills"]:
        print("?", skill)

    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)


# ---------------------------------------------------------
# 9. PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    test_normalizer()