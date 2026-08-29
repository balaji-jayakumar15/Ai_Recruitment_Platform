import json
from pathlib import Path


# ============================================================
# FILE PATH
# ============================================================

CURRENT_FILE = Path(__file__).resolve()

SKILLS_FOLDER = CURRENT_FILE.parent.parent

PROFILE_FILE = (
    SKILLS_FOLDER
    / "output"
    / "candidate_profiles.json"
)


# ============================================================
# LOAD CANDIDATE PROFILES
# ============================================================

with open(
    PROFILE_FILE,
    "r",
    encoding="utf-8"
) as file:

    profiles = json.load(file)


# ============================================================
# TEST SKILLS
# ============================================================

print("=" * 60)
print("MEMBER 3 - SKILL EXTRACTION TEST")
print("=" * 60)

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

    skills = profile.get(
        "skills",
        {}
    )

    total_skills = 0

    for category, skill_list in skills.items():

        if skill_list:

            print(
                f"\n{category}:"
            )

            for skill in skill_list:

                print(
                    f"  ✓ {skill}"
                )

                total_skills += 1

    print(
        f"\nTotal skills: {total_skills}"
    )


# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 60)
print("SKILL EXTRACTION TEST COMPLETED")
print("=" * 60)

print(
    f"Total resumes tested: {len(profiles)}"
)

print(
    "✓ Skill extraction output generated successfully"
)