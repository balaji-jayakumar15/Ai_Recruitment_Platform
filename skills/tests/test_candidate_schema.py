import json
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

CURRENT_FILE = Path(__file__).resolve()

SKILLS_FOLDER = CURRENT_FILE.parent.parent

SCHEMA_FILE = SKILLS_FOLDER / "candidate_schema.json"

PROFILE_FILE = (
    SKILLS_FOLDER
    / "output"
    / "candidate_profiles.json"
)


# ============================================================
# LOAD JSON FILE
# ============================================================

def load_json(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# VALIDATE PROFILE
# ============================================================

def validate_profile(profile, schema):

    missing_fields = []

    for field in schema:

        if field not in profile:

            missing_fields.append(field)

    return missing_fields


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("MEMBER 3 - CANDIDATE PROFILE VALIDATION")
    print("=" * 60)

    schema = load_json(
        SCHEMA_FILE
    )

    profiles = load_json(
        PROFILE_FILE
    )

    print(
        f"\nTotal profiles found: {len(profiles)}"
    )

    valid_count = 0

    for index, profile in enumerate(
        profiles,
        start=1
    ):

        missing = validate_profile(
            profile,
            schema
        )

        if not missing:

            print(
                f"✓ Profile {index}: VALID"
            )

            valid_count += 1

        else:

            print(
                f"✗ Profile {index}: "
                f"Missing {missing}"
            )

    print("\n" + "=" * 60)

    print(
        f"Valid profiles: "
        f"{valid_count}/{len(profiles)}"
    )

    print("=" * 60)

    if valid_count == len(profiles):

        print(
            "\n✓ ALL CANDIDATE PROFILES ARE VALID"
        )

    else:

        print(
            "\n⚠ SOME PROFILES NEED FIXING"
        )