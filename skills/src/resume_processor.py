import json
import re

from skill_normalizer import normalize_skills


# --------------------------------------------------
# Load skill dictionary
# --------------------------------------------------

with open("skills/skills.json", "r", encoding="utf-8") as file:
    skill_data = json.load(file)


# Convert dictionary into one skill list
ALL_SKILLS = []

for category, skills in skill_data.items():
    ALL_SKILLS.extend(skills)


# --------------------------------------------------
# Clean resume text
# --------------------------------------------------

def clean_resume_text(text):
    """
    Clean unnecessary spaces and characters from resume text.
    """

    text = text.replace("\x00", " ")

    # Replace multiple spaces/newlines
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# --------------------------------------------------
# Extract name
# --------------------------------------------------

def extract_name(text):
    """
    Basic name extraction.
    Assumes the first meaningful line is the candidate name.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        first_line = lines[0]

        # Avoid treating headings as names
        if len(first_line.split()) <= 5:
            return first_line

    return None


# --------------------------------------------------
# Extract email
# --------------------------------------------------

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


# --------------------------------------------------
# Extract phone
# --------------------------------------------------

def extract_phone(text):

    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


# --------------------------------------------------
# Extract location
# --------------------------------------------------

def extract_location(text):

    location_pattern = r"(?:Location|Address|City)\s*:\s*([^\n]+)"

    match = re.search(
        location_pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


# --------------------------------------------------
# Extract skills
# --------------------------------------------------

def extract_skills(resume_text):

    found_skills = []

    text_lower = resume_text.lower()

    for skill in ALL_SKILLS:

        skill_lower = skill.lower()

        # Word boundary matching
        pattern = r"(?<!\w)" + re.escape(skill_lower) + r"(?!\w)"

        if re.search(pattern, text_lower):

            found_skills.append(skill)

    # Normalize
    found_skills = normalize_skills(found_skills)

    return sorted(found_skills)


# --------------------------------------------------
# Extract education
# --------------------------------------------------

def extract_education(text):

    education = []

    education_keywords = [
        "b.sc",
        "b.e",
        "b.tech",
        "bca",
        "mca",
        "m.sc",
        "m.e",
        "m.tech",
        "mba",
        "bachelor",
        "master"
    ]

    lines = text.splitlines()

    for line in lines:

        line_clean = line.strip()

        for keyword in education_keywords:

            if keyword.lower() in line_clean.lower():

                education.append(line_clean)
                break

    return education


# --------------------------------------------------
# Extract projects
# --------------------------------------------------

def extract_projects(text):

    projects = []

    lines = text.splitlines()

    inside_project_section = False

    for line in lines:

        line_clean = line.strip()

        if not line_clean:
            continue

        if "project" in line_clean.lower():
            inside_project_section = True
            continue

        if inside_project_section:

            if any(
                section in line_clean.lower()
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "certification"
                ]
            ):
                break

            projects.append(line_clean)

    return projects


# --------------------------------------------------
# Extract certifications
# --------------------------------------------------

def extract_certifications(text):

    certifications = []

    lines = text.splitlines()

    inside_section = False

    for line in lines:

        line_clean = line.strip()

        if "certification" in line_clean.lower():
            inside_section = True
            continue

        if inside_section:

            if any(
                section in line_clean.lower()
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "project"
                ]
            ):
                break

            if line_clean:
                certifications.append(line_clean)

    return certifications


# --------------------------------------------------
# Complete candidate profile
# --------------------------------------------------

def extract_candidate_profile(resume_text):

    clean_text = clean_resume_text(resume_text)

    profile = {

        "candidate_name": extract_name(clean_text),

        "email": extract_email(clean_text),

        "phone": extract_phone(clean_text),

        "location": extract_location(clean_text),

        "skills": extract_skills(clean_text),

        "education": extract_education(clean_text),

        "experience": [],

        "experience_years": None,

        "certifications": extract_certifications(clean_text),

        "projects": extract_projects(clean_text)
    }

    return profile


# --------------------------------------------------
# Test directly
# --------------------------------------------------

if __name__ == "__main__":

    with open(
        "skills/resumes/resume1.txt",
        "r",
        encoding="utf-8"
    ) as file:

        resume_text = file.read()

    profile = extract_candidate_profile(resume_text)

    print(json.dumps(
        profile,
        indent=4,
        ensure_ascii=False
    ))