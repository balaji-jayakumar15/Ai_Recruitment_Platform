import json

# --------------------------------------------------
# MEMBER 3 - SKILL EXTRACTION VALIDATION
# --------------------------------------------------

OUTPUT_FILE = "skills/output/candidate_profiles.json"

with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
    profiles = json.load(file)


print("=" * 60)
print("MEMBER 3 - SKILL EXTRACTION VALIDATION")
print("=" * 60)

total_profiles = len(profiles)
valid_profiles = 0


for profile in profiles:

    source_file = profile.get("source_file", "Unknown")
    skills_data = profile.get("skills", {})

    all_skills = []

    for category, skills in skills_data.items():

        if isinstance(skills, list):
            all_skills.extend(skills)

    # Check for duplicate skills
    skill_names = [skill.lower() for skill in all_skills]

    duplicates = []

    for skill in set(skill_names):
        if skill_names.count(skill) > 1:
            duplicates.append(skill)

    # Check that every skill is a non-empty string
    invalid_skills = [
        skill for skill in all_skills
        if not isinstance(skill, str) or not skill.strip()
    ]

    print("\n" + "-" * 60)
    print(f"Resume: {source_file}")
    print(f"Total skills: {len(all_skills)}")

    if duplicates:
        print(f"✗ Duplicate skills: {duplicates}")
    else:
        print("✓ No duplicate skills")

    if invalid_skills:
        print(f"✗ Invalid skills: {invalid_skills}")
    else:
        print("✓ All skills are valid")

    if not duplicates and not invalid_skills:
        print("✓ Skill extraction VALID")
        valid_profiles += 1
    else:
        print("✗ Skill extraction NEEDS REVIEW")


print("\n" + "=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)

print(f"Total profiles: {total_profiles}")
print(f"Valid profiles: {valid_profiles}/{total_profiles}")

if valid_profiles == total_profiles:
    print("\n✓ ALL SKILL EXTRACTIONS ARE VALID")
else:
    print("\n⚠ SOME SKILLS NEED REVIEW")