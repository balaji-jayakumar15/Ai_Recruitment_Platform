import re


SKILL_ALIASES = {
    "js": "JavaScript",
    "javascript": "JavaScript",

    "ts": "TypeScript",
    "typescript": "TypeScript",

    "py": "Python",
    "python": "Python",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    "mysql": "MySQL",

    "mongo": "MongoDB",
    "mongodb": "MongoDB",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "dl": "Deep Learning",
    "deep learning": "Deep Learning",

    "reactjs": "React",
    "react.js": "React",
    "react": "React",

    "nodejs": "Node.js",
    "node.js": "Node.js",

    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",

    "git": "Git",
    "github": "GitHub",

    "powerbi": "Power BI",
    "power bi": "Power BI"
}


def normalize_skill(skill):
    """
    Convert different names/aliases into one standard skill name.
    """

    skill = skill.strip().lower()

    # Remove unnecessary spaces
    skill = re.sub(r"\s+", " ", skill)

    return SKILL_ALIASES.get(skill, skill.title())


def normalize_skills(skills):
    """
    Normalize skills and remove duplicates.
    """

    normalized = []

    for skill in skills:
        standard_skill = normalize_skill(skill)

        if standard_skill not in normalized:
            normalized.append(standard_skill)

    return normalized