import json
import re
import os

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

    # Replace multiple spaces/tabs
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

        # Avoid treating very long headings as names
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
        pattern = (
            r"(?<!\w)"
            + re.escape(skill_lower)
            + r"(?!\w)"
        )

        if re.search(pattern, text_lower):

            found_skills.append(skill)

    # Normalize skills
    found_skills = normalize_skills(found_skills)

    # Remove duplicates
    found_skills = list(set(found_skills))

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
                    "certification",
                    "internship"
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
                    "project",
                    "internship"
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
# Process ALL resume text files
# --------------------------------------------------

if __name__ == "__main__":

    resume_folder = "skills/resumes"

    # Check whether folder exists
    if not os.path.exists(resume_folder):

        print(f"Resume folder not found: {resume_folder}")

        exit()

    # Get all .txt files
    resume_files = [
        file
        for file in os.listdir(resume_folder)
        if file.lower().endswith(".txt")
    ]

    # Sort files
    resume_files.sort()

    # Check if resumes exist
    if not resume_files:

        print("No .txt resume files found.")

        exit()

    print("=" * 60)
    print(f"Found {len(resume_files)} resume(s)")
    print("=" * 60)

    # Process every resume
    for resume_file in resume_files:

        file_path = os.path.join(
            resume_folder,
            resume_file
        )

        print("\n")
        print("=" * 60)
        print(f"Processing: {resume_file}")
        print("=" * 60)

        try:

            # Read resume
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                resume_text = file.read()

            # Extract candidate profile
            profile = extract_candidate_profile(
                resume_text
            )

            # Display result
            print(
                json.dumps(
                    profile,
                    indent=4,
                    ensure_ascii=False
                )
            )

            print(f"\n✓ {resume_file} processed successfully")

        except Exception as error:

            print(
                f"\n✗ Error processing {resume_file}: {error}"
            )

    print("\n")
    print("=" * 60)
    print("ALL RESUMES PROCESSED")
    print("=" * 60)