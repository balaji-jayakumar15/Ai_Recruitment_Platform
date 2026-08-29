import json
from pathlib import Path


# ============================================================
# PATH
# ============================================================

CURRENT_FILE = Path(__file__).resolve()

SKILLS_FOLDER = CURRENT_FILE.parent.parent

PROFILE_FILE = (
    SKILLS_FOLDER
    / "output"
    / "candidate_profiles.json"
)


# ============================================================
# LOAD PROFILES
# ============================================================

with open(
    PROFILE_FILE,
    "r",
    encoding="utf-8"
) as file:

    profiles = json.load(file)


# ============================================================
# REQUIRED FIELDS
# ============================================================

required_fields = [
    "personal_details",
    "education",
    "skills",
    "experience",
    "projects",
    "certifications",
    "internships",
    "achievements",
    "languages",
    "total_experience_years"
]


# ============================================================
# QUALITY CHECK
# ============================================================

print("=" * 60)
print("MEMBER 3 - EXTRACTION QUALITY CHECK")
print("=" * 60)

print(
    f"\nTotal resumes checked: {len(profiles)}"
)


for index, profile in enumerate(
    profiles,
    start=1
):

    print("\n" + "-" * 60)

    print(
        f"Resume {index}: "
        f"{profile.get('source_file', 'Unknown')}"
    )

    print("-" * 60)

    # Check fields
    missing = []

    for field in required_fields:

        if field not in profile:

            missing.append(field)

    if missing:

        print(
            "✗ Missing fields:",
            missing
        )

    else:

        print(
            "✓ All required fields present"
        )


    # Personal details
    personal = profile.get(
        "personal_details",
        {}
    )

    print(
        "Name     :",
        personal.get("name")
    )

    print(
        "Email    :",
        personal.get("email")
    )

    print(
        "Phone    :",
        personal.get("phone")
    )

    print(
        "Location :",
        personal.get("location")
    )


    # Skills
    skills = profile.get(
        "skills",
        {}
    )

    skill_count = 0

    for category, skill_list in skills.items():

        if isinstance(skill_list, list):

            skill_count += len(skill_list)

    print(
        "Skills   :",
        skill_count
    )


    # Other details
    print(
        "Education      :",
        len(profile.get("education", []))
    )

    print(
        "Experience     :",
        len(profile.get("experience", []))
    )

    print(
        "Projects       :",
        len(profile.get("projects", []))
    )

    print(
        "Certifications :",
        len(profile.get("certifications", []))
    )

    print(
        "Internships    :",
        len(profile.get("internships", []))
    )

    print(
        "Achievements   :",
        len(profile.get("achievements", []))
    )

    print(
        "Languages      :",
        len(profile.get("languages", []))
    )


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 60)
print("EXTRACTION QUALITY CHECK COMPLETED")
print("=" * 60)

print(
    f"✓ Checked {len(profiles)} resume profiles"
)

print(
    "✓ Ready for larger resume dataset from M2"
)

print("=" * 60)