import re


# ============================================================
# SKILL NORMALIZATION
# ============================================================

def normalize_skill(skill):
    """
    Normalize an individual skill.
    """

    skill = str(skill).strip().lower()

    replacements = {
        "node": "node.js",
        "node js": "node.js",
        "nodejs": "node.js",

        "reactjs": "react",
        "react.js": "react",

        "vuejs": "vue",
        "vue.js": "vue",

        "angularjs": "angular",
        "angular.js": "angular",

        "postgres": "postgresql",

        "scikit learn": "scikit-learn",
        "sklearn": "scikit-learn",

        "powerbi": "power bi",

        "ms sql": "sql server",
        "mssql": "sql server",

        "amazon web services": "aws",
        "microsoft azure": "azure",
        "google cloud platform": "gcp"
    }

    if skill in replacements:
        skill = replacements[skill]

    return skill


# ============================================================
# SKILL PARSING
# ============================================================

def parse_skills(skill_string):
    """
    Convert comma-separated skills into a normalized set.
    """

    if skill_string is None:
        return set()

    skills = str(skill_string).split(",")

    normalized = set()

    for skill in skills:

        skill = normalize_skill(skill)

        if skill:
            normalized.add(skill)

    return normalized


# ============================================================
# REQUIRED SKILL MATCHING
# ============================================================

def calculate_skill_match(candidate_skills, required_skills):

    candidate = parse_skills(candidate_skills)
    required = parse_skills(required_skills)

    matched = candidate.intersection(required)
    missing = required.difference(candidate)

    if len(required) == 0:
        match_percentage = 0.0
    else:
        match_percentage = (len(matched) / len(required)) * 100

    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "skill_match_percentage": round(match_percentage, 2)
    }


# ============================================================
# PREFERRED SKILL MATCHING
# ============================================================

def calculate_preferred_skill_match(candidate_skills, preferred_skills):

    candidate = parse_skills(candidate_skills)
    preferred = parse_skills(preferred_skills)

    if len(preferred) == 0:
        return {
            "matched_preferred_skills": [],
            "preferred_match_percentage": 0.0
        }

    matched = candidate.intersection(preferred)

    percentage = (len(matched) / len(preferred)) * 100

    return {
        "matched_preferred_skills": sorted(matched),
        "preferred_match_percentage": round(percentage, 2)
    }


# ============================================================
# EXPERIENCE SCORE
# ============================================================

def calculate_experience_score(experience_level, experience_years):

    experience_years = float(experience_years)

    if experience_level == "Fresher":

        if experience_years <= 1:
            return 100
        else:
            return 90

    elif experience_level == "Junior":

        if experience_years >= 1:
            return 100
        elif experience_years >= 0.5:
            return 80
        else:
            return 60

    elif experience_level == "Mid-level":

        if experience_years >= 3:
            return 100
        elif experience_years >= 2:
            return 80
        elif experience_years >= 1:
            return 60
        else:
            return 40

    elif experience_level == "Senior":

        if experience_years >= 6:
            return 100
        elif experience_years >= 4:
            return 80
        elif experience_years >= 2:
            return 60
        else:
            return 40

    return 50


# ============================================================
# EDUCATION SCORE
# ============================================================

IT_EDUCATION_KEYWORDS = [
    "computer science",
    "information technology",
    "computer applications",
    "software engineering",
    "data science",
    "artificial intelligence",
    "information systems"
]


def calculate_education_score(education):

    education = str(education).lower()

    for keyword in IT_EDUCATION_KEYWORDS:

        if keyword in education:
            return 100

    return 60


# ============================================================
# PROJECT MATCH
# ============================================================

def calculate_project_match(projects, required_skills):

    project_text = str(projects).lower()

    required = parse_skills(required_skills)

    if len(required) == 0:
        return 0.0

    matched = []

    for skill in required:

        if skill in project_text:
            matched.append(skill)

    score = (len(matched) / len(required)) * 100

    return round(score, 2)


# ============================================================
# FINAL JOB MATCH SCORE
# ============================================================

def calculate_job_match_score(
    skill_match,
    experience_match,
    project_match,
    preferred_match,
    education_match
):

    score = (
        skill_match * 0.50 +
        experience_match * 0.20 +
        project_match * 0.15 +
        preferred_match * 0.10 +
        education_match * 0.05
    )

    # Required-skill gates
    if skill_match < 20:
        score = min(score, 35)

    elif skill_match < 40:
        score = min(score, 50)

    elif skill_match < 60:
        score = min(score, 70)

    return round(score, 2)


# ============================================================
# MAIN MODEL 2 FUNCTION
# ============================================================

def calculate_job_match(
    candidate_skills,
    required_skills,
    preferred_skills,
    experience_level,
    experience_years,
    education,
    projects
):
    """
    Calculate complete job matching results for one candidate.
    """

    # Required skills
    skill_result = calculate_skill_match(
        candidate_skills,
        required_skills
    )

    # Preferred skills
    preferred_result = calculate_preferred_skill_match(
        candidate_skills,
        preferred_skills
    )

    # Experience
    experience_score = calculate_experience_score(
        experience_level,
        experience_years
    )

    # Education
    education_score = calculate_education_score(
        education
    )

    # Projects
    project_score = calculate_project_match(
        projects,
        required_skills
    )

    # Final score
    final_score = calculate_job_match_score(
        skill_result["skill_match_percentage"],
        experience_score,
        project_score,
        preferred_result["preferred_match_percentage"],
        education_score
    )

    return {
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"],
        "skill_match_percentage": skill_result["skill_match_percentage"],

        "preferred_matched_skills":
            preferred_result["matched_preferred_skills"],

        "preferred_match_percentage":
            preferred_result["preferred_match_percentage"],

        "experience_score": experience_score,
        "project_match": project_score,
        "education_score": education_score,
        "job_match_score": final_score
    }


# ============================================================
# TEST MODEL 2
# ============================================================

if __name__ == "__main__":

    candidate_skills = (
        "REST APIs, Express, Docker, Java, PostgreSQL, Git"
    )

    required_skills = (
        "MongoDB, Python, Docker, Redis, Java, PostgreSQL"
    )

    preferred_skills = (
        "Git, Express, REST APIs"
    )

    experience_level = "Fresher"
    experience_years = 0

    education = "B.Tech Information Technology"

    projects = (
        "Prediction project for Backend Developer using "
        "REST APIs, Express, Docker"
    )

    result = calculate_job_match(
        candidate_skills,
        required_skills,
        preferred_skills,
        experience_level,
        experience_years,
        education,
        projects
    )

    print("=" * 60)
    print("MODEL 2 - JOB MATCHING TEST")
    print("=" * 60)

    print("Matched Skills:",
          result["matched_skills"])

    print("Missing Skills:",
          result["missing_skills"])

    print("Skill Match:",
          result["skill_match_percentage"], "%")

    print("Preferred Matched Skills:",
          result["preferred_matched_skills"])

    print("Preferred Match:",
          result["preferred_match_percentage"], "%")

    print("Experience Score:",
          result["experience_score"])

    print("Project Match:",
          result["project_match"], "%")

    print("Education Score:",
          result["education_score"])

    print("FINAL JOB MATCH SCORE:",
          result["job_match_score"], "%")

    print("=" * 60)