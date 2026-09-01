import json
import re
from pathlib import Path

from skill_normalizer import normalize_skills


# ============================================================
# PATH CONFIGURATION
# ============================================================

CURRENT_FILE = Path(__file__).resolve()

SRC_FOLDER = CURRENT_FILE.parent
SKILLS_FOLDER = SRC_FOLDER.parent

SKILLS_JSON_FILE = SKILLS_FOLDER / "skills.json"
RESUME_FOLDER = SKILLS_FOLDER / "resumes"
OUTPUT_FOLDER = SKILLS_FOLDER / "output"

OUTPUT_FILE = OUTPUT_FOLDER / "candidate_profiles.json"


# ============================================================
# LOAD SKILL DICTIONARY
# ============================================================

def load_skill_dictionary():

    try:

        with open(
            SKILLS_JSON_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            skill_data = json.load(file)

    except FileNotFoundError:

        print(
            f"ERROR: skills.json not found:\n"
            f"{SKILLS_JSON_FILE}"
        )

        return {}, []

    except json.JSONDecodeError:

        print("ERROR: Invalid skills.json")

        return {}, []


    all_skills = []

    for category, skills in skill_data.items():

        if isinstance(skills, list):

            for skill in skills:

                if skill not in all_skills:

                    all_skills.append(skill)


    return skill_data, all_skills


SKILL_DATA, ALL_SKILLS = load_skill_dictionary()


# ============================================================
# CLEAN RESUME TEXT
# ============================================================

def clean_resume_text(text):

    if not isinstance(text, str):

        return ""

    text = text.replace("\x00", " ")

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = text.replace("\t", " ")

    text = re.sub(
        r"[ ]{2,}",
        " ",
        text
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


# ============================================================
# GET CLEAN LINES
# ============================================================

def get_resume_lines(text):

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:

            lines.append(line)

    return lines


# ============================================================
# EXTRACT NAME
# ============================================================

def extract_name(text):

    lines = get_resume_lines(text)

    ignored_headings = {
        "resume",
        "curriculum vitae",
        "cv",
        "profile",
        "resume 1",
        "resume 2",
        "resume 3",
        "resume 4",
        "resume 5"
    }

    for line in lines[:10]:

        cleaned = line.strip()

        if cleaned.lower() in ignored_headings:

            continue

        if "@" in cleaned:

            continue

        if re.search(r"\d{7,}", cleaned):

            continue

        if cleaned.lower() in {
            "skills",
            "education",
            "experience",
            "projects",
            "certifications",
            "internships",
            "objective",
            "summary",
            "profile summary"
        }:

            continue

        words = cleaned.split()

        if 1 <= len(words) <= 5:

            if not re.search(r"\d", cleaned):

                return cleaned

    return None


# ============================================================
# EXTRACT EMAIL
# ============================================================

def extract_email(text):

    pattern = (
        r"[A-Za-z0-9._%+-]+"
        r"@"
        r"[A-Za-z0-9.-]+"
        r"\."
        r"[A-Za-z]{2,}"
    )

    match = re.search(
        pattern,
        text
    )

    if match:

        return match.group(0)

    return None


# ============================================================
# EXTRACT PHONE
# ============================================================

def extract_phone(text):

    patterns = [

        r"(?:\+91[\s-]?)?[6-9]\d{9}",

        r"(?:\+91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            return match.group(0)

    return None


# ============================================================
# EXTRACT LOCATION
# ============================================================

def extract_location(text):

    pattern = (
        r"(?:Location|Address|City)"
        r"\s*:\s*([^\n]+)"
    )

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:

        return match.group(1).strip()

    return None

# --------------------------------------------------
# Extract social and portfolio links
# --------------------------------------------------

def extract_social_profiles(text):

    profiles = {
        "github": None,
        "linkedin": None,
        "naukri": None,
        "portfolio": None
    }

    # Find URLs
    url_pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'

    urls = re.findall(
        url_pattern,
        text,
        re.IGNORECASE
    )

    # Remove punctuation at the end of URLs
    urls = [
        url.rstrip(".,;:)]}")
        for url in urls
    ]

    for url in urls:

        url_lower = url.lower()

        if "github.com" in url_lower:
            profiles["github"] = url

        elif "linkedin.com" in url_lower:
            profiles["linkedin"] = url

        elif "naukri.com" in url_lower:
            profiles["naukri"] = url

        elif (
            "portfolio" in url_lower
            or "personal" in url_lower
        ):
            profiles["portfolio"] = url

    return profiles

# ============================================================
# EXTRACT SKILLS
# ============================================================

def extract_skills(resume_text):

    found_skills = []

    text_lower = resume_text.lower()

    for skill in ALL_SKILLS:

        skill_lower = skill.lower()

        pattern = (
            r"(?<!\w)"
            + re.escape(skill_lower)
            + r"(?!\w)"
        )

        if re.search(
            pattern,
            text_lower
        ):

            found_skills.append(skill)

    found_skills = normalize_skills(
        found_skills
    )

    unique_skills = []

    for skill in found_skills:

        if skill.lower() not in [
            existing.lower()
            for existing in unique_skills
        ]:

            unique_skills.append(skill)

    return sorted(
        unique_skills,
        key=str.lower
    )

# ============================================================
# CATEGORIZE SKILLS
# ============================================================

def categorize_skills(skills):

    categorized = {
        "programming_languages": [],
        "web_development": [],
        "databases": [],
        "machine_learning": [],
        "data_analytics": [],
        "backend": [],
        "cloud_and_devops": [],
        "tools": []
    }

    category_mapping = {
        "programming_languages": "programming_languages",
        "web_development": "web_development",
        "databases": "databases",
        "machine_learning_ai": "machine_learning",
        "machine_learning": "machine_learning",
        "data_analytics": "data_analytics",
        "backend": "backend",
        "cloud_devops": "cloud_and_devops",
        "cloud_and_devops": "cloud_and_devops",
        "tools": "tools"
    }

    for category, dictionary_skills in SKILL_DATA.items():

        output_category = category_mapping.get(category)

        if not output_category:
            continue

        if not isinstance(dictionary_skills, list):
            continue

        for extracted_skill in skills:

            for dictionary_skill in dictionary_skills:

                if (
                    extracted_skill.lower()
                    == dictionary_skill.lower()
                ):

                    if extracted_skill not in categorized[
                        output_category
                    ]:

                        categorized[
                            output_category
                        ].append(
                            extracted_skill
                        )

    return categorized


# ============================================================
# EXTRACT EDUCATION
# ============================================================

def extract_education(text):

    education = []

    lines = get_resume_lines(text)

    education_keywords = [
        "b.sc",
        "b.sc.",
        "b.e",
        "b.e.",
        "b.tech",
        "b.tech.",
        "bca",
        "mca",
        "m.sc",
        "m.sc.",
        "m.e",
        "m.e.",
        "m.tech",
        "mba",
        "bachelor",
        "master"
    ]

    inside_education = False

    for line in lines:

        lower_line = line.lower()

        if "education" in lower_line:

            inside_education = True

            continue

        if inside_education:

            if any(
                section in lower_line
                for section in [
                    "skills",
                    "experience",
                    "projects",
                    "certification",
                    "internship",
                    "achievements",
                    "languages"
                ]
            ):

                break

            if any(
                keyword in lower_line
                for keyword in education_keywords
            ):

                education.append(line)

        else:

            if any(
                keyword in lower_line
                for keyword in education_keywords
            ):

                education.append(line)

    result = []

    for item in education:

        if item not in result:

            result.append(item)

    return result


# ============================================================
# EXTRACT PROJECTS
# ============================================================

def extract_projects(text):

    projects = []

    lines = get_resume_lines(text)

    inside_project_section = False

    for line in lines:

        lower_line = line.lower()

        if "project" in lower_line:

            inside_project_section = True

            continue

        if inside_project_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "certification",
                    "internship",
                    "achievement",
                    "language"
                ]
            ):

                break

            projects.append(
                line.lstrip("-• ")
            )

    return projects


# ============================================================
# EXTRACT CERTIFICATIONS
# ============================================================

def extract_certifications(text):

    certifications = []

    lines = get_resume_lines(text)

    inside_section = False

    for line in lines:

        lower_line = line.lower()

        if (
            "certification" in lower_line
            or "certificate" in lower_line
        ):

            inside_section = True

            continue

        if inside_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "project",
                    "internship",
                    "achievement",
                    "language"
                ]
            ):

                break

            certifications.append(
                line.lstrip("-• ")
            )

    return certifications


# ============================================================
# EXTRACT INTERNSHIPS
# ============================================================

def extract_internships(text):

    internships = []

    lines = get_resume_lines(text)

    inside_section = False

    for line in lines:

        lower_line = line.lower()

        if "internship" in lower_line:

            inside_section = True

            continue

        if inside_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "project",
                    "certification",
                    "achievement",
                    "language"
                ]
            ):

                break

            internships.append(
                line.lstrip("-• ")
            )

    return internships


# ============================================================
# EXTRACT ACHIEVEMENTS
# ============================================================

def extract_achievements(text):

    achievements = []

    lines = get_resume_lines(text)

    inside_section = False

    for line in lines:

        lower_line = line.lower()

        if (
            "achievement" in lower_line
            or "accomplishment" in lower_line
        ):

            inside_section = True

            continue

        if inside_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "project",
                    "certification",
                    "internship",
                    "language"
                ]
            ):

                break

            achievements.append(
                line.lstrip("-• ")
            )

    return achievements


# ============================================================
# EXTRACT LANGUAGES
# ============================================================

def extract_languages(text):

    languages = []

    lines = get_resume_lines(text)

    inside_section = False

    common_languages = [
        "english",
        "tamil",
        "hindi",
        "telugu",
        "malayalam",
        "kannada",
        "marathi",
        "french",
        "german",
        "spanish"
    ]

    for line in lines:

        lower_line = line.lower()

        if (
            lower_line == "languages"
            or lower_line.startswith("languages:")
        ):

            inside_section = True

            if ":" in line:

                values = line.split(
                    ":",
                    1
                )[1]

                for value in values.split(","):

                    value = value.strip()

                    if value:

                        languages.append(value)

            continue

        if inside_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "experience",
                    "project",
                    "certification",
                    "internship",
                    "achievement"
                ]
            ):

                break

            for language in common_languages:

                if language in lower_line:

                    languages.append(
                        language.title()
                    )

    result = []

    for language in languages:

        if language not in result:

            result.append(language)

    return result


# ============================================================
# EXTRACT EXPERIENCE
# ============================================================

def extract_experience(text):

    experience = []

    lines = get_resume_lines(text)

    inside_section = False

    for line in lines:

        lower_line = line.lower()

        if (
            lower_line == "experience"
            or "work experience" in lower_line
            or "professional experience" in lower_line
        ):

            inside_section = True

            continue

        if inside_section:

            if any(
                section in lower_line
                for section in [
                    "education",
                    "skills",
                    "project",
                    "certification",
                    "internship",
                    "achievement",
                    "language"
                ]
            ):

                break

            experience.append(
                line.lstrip("-• ")
            )

    return experience


# ============================================================
# EXTRACT TOTAL EXPERIENCE YEARS
# ============================================================

def extract_experience_years(text):

    patterns = [
        r"(\d+(?:\.\d+)?)\+?\s*years?\s+(?:of\s+)?experience",
        r"experience\s*:\s*(\d+(?:\.\d+)?)\+?\s*years?"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            try:

                return float(
                    match.group(1)
                )

            except ValueError:

                pass

    return 0

# ============================================================
# COMPLETE CANDIDATE PROFILE
# ============================================================

def extract_candidate_profile(resume_text):

    clean_text = clean_resume_text(
        resume_text
    )

    extracted_skills = extract_skills(
        clean_text
    )

    categorized_skills = categorize_skills(
        extracted_skills
    )

    profile = {

        "personal_details": {

            "name": extract_name(
                clean_text
            ),

            "email": extract_email(
                clean_text
            ),

            "phone": extract_phone(
                clean_text
            ),

            "location": extract_location(
                clean_text
            )
        },

        "social_profiles": extract_social_profiles(
            clean_text
        ),
        

        "education": extract_education(
            clean_text
        ),

        "skills": categorized_skills,

        "experience": extract_experience(
            clean_text
        ),

        "projects": extract_projects(
            clean_text
        ),

        "certifications": extract_certifications(
            clean_text
        ),

        "internships": extract_internships(
            clean_text
        ),

        "achievements": extract_achievements(
            clean_text
        ),

        "languages": extract_languages(
            clean_text
        ),

        "total_experience_years":
            extract_experience_years(
                clean_text
            )
    }

    return profile


# ============================================================
# PROCESS ONE RESUME
# ============================================================

def process_resume_file(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            resume_text = file.read()

        profile = extract_candidate_profile(
            resume_text
        )

        return profile, None

    except UnicodeDecodeError:

        return None, "Encoding error"

    except Exception as error:

        return None, str(error)


# ============================================================
# PROCESS ALL RESUMES
# ============================================================

def process_all_resumes():

    if not RESUME_FOLDER.exists():

        print(
            f"ERROR: Resume folder not found:\n"
            f"{RESUME_FOLDER}"
        )

        return []

    resume_files = sorted(
        [
            file
            for file in RESUME_FOLDER.iterdir()
            if file.is_file()
            and file.suffix.lower() == ".txt"
        ]
    )

    if not resume_files:

        print(
            "No .txt resume files found."
        )

        return []

    print("=" * 60)

    print(
        f"Found {len(resume_files)} resume(s)"
    )

    print("=" * 60)

    all_profiles = []

    for index, resume_file in enumerate(
        resume_files,
        start=1
    ):

        print("\n")

        print("=" * 60)

        print(
            f"[{index}/{len(resume_files)}] "
            f"Processing: {resume_file.name}"
        )

        print("=" * 60)

        profile, error = process_resume_file(
            resume_file
        )

        if error:

            print(
                f"✗ Error: {error}"
            )

            continue

        # Keep track of which resume produced
        # each candidate profile
        profile["source_file"] = (
            resume_file.name
        )

        all_profiles.append(
            profile
        )

        print(
            json.dumps(
                profile,
                indent=4,
                ensure_ascii=False
            )
        )

        print(
            f"\n✓ {resume_file.name} "
            f"processed successfully"
        )

    return all_profiles


# ============================================================
# SAVE ALL PROFILES TO JSON
# ============================================================

def save_profiles(profiles):

    try:

        OUTPUT_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                profiles,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\n")

        print("=" * 60)

        print(
            "ALL RESUMES PROCESSED"
        )

        print("=" * 60)

        print(
            f"\n✓ Total profiles saved: "
            f"{len(profiles)}"
        )

        print(
            f"✓ Output file:\n"
            f"{OUTPUT_FILE}"
        )

        return True

    except Exception as error:

        print(
            f"\n✗ Failed to save JSON: "
            f"{error}"
        )

        return False


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\n")

    print("=" * 60)

    print(
        "MEMBER 3 - RESUME PROCESSOR"
    )

    print("=" * 60)

    print(
        f"\nSkill dictionary:"
        f"\n{SKILLS_JSON_FILE}"
    )

    print(
        f"\nResume folder:"
        f"\n{RESUME_FOLDER}"
    )

    print(
        f"\nOutput file:"
        f"\n{OUTPUT_FILE}"
    )

    print("\n")

    # Check whether skills were loaded
    if not ALL_SKILLS:

        print(
            "WARNING: No skills loaded "
            "from skills.json."
        )

    # Process every resume
    profiles = process_all_resumes()

    # Save extracted profiles
    if profiles:

        save_profiles(
            profiles
        )

    else:

        print(
            "\nNo profiles were created."
        )
        