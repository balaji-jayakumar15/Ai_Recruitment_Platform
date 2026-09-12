import json
from collections import Counter

# --------------------------------------------------
# MEMBER 3 - MULTIPLE RESUME SKILL TEST
# --------------------------------------------------

OUTPUT_FILE = "skills/output/candidate_profiles.json"


# Load candidate profiles
with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
    profiles = json.load(file)


print("=" * 60)
print("MEMBER 3 - MULTIPLE RESUME SKILL ANALYSIS")
print("=" * 60)

print(f"\nTotal resumes processed: {len(profiles)}")


# Store all skills
all_skills = []


# --------------------------------------------------
# Display skills for each resume
# --------------------------------------------------

for profile in profiles:

    source_file = profile.get("source_file", "Unknown")

    skills_data = profile.get("skills", {})

    resume_skills = []

    for category, skills in skills_data.items():

        if isinstance(skills, list):
            resume_skills.extend(skills)

    all_skills.extend(resume_skills)

    print("\n" + "-" * 60)
    print(f"Resume: {source_file}")
    print(f"Total skills: {len(resume_skills)}")
    print("Skills:", ", ".join(resume_skills))


# --------------------------------------------------
# Skill frequency across all resumes
# --------------------------------------------------

skill_counter = Counter(all_skills)

print("\n" + "=" * 60)
print("MOST COMMON SKILLS")
print("=" * 60)

for skill, count in skill_counter.most_common():

    print(f"{skill}: {count}")


# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"Total resumes: {len(profiles)}")
print(f"Total skill occurrences: {len(all_skills)}")
print(f"Unique skills: {len(skill_counter)}")

print("\n✓ Multiple resume skill processing completed")