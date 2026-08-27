import sys
import os

# Get the project paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "src"))
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

# Add src folder to Python path
sys.path.insert(0, SRC_DIR)

# Move to project folder so skills/skills.json can be found
os.chdir(PROJECT_DIR)

from resume_processor import extract_candidate_profile


# --------------------------------------------------
# Test resume1.txt
# --------------------------------------------------

resume_path = os.path.join(
    PROJECT_DIR,
    "skills",
    "resumes",
    "resume1.txt"
)


with open(
    resume_path,
    "r",
    encoding="utf-8"
) as file:

    resume_text = file.read()


# Extract candidate profile
profile = extract_candidate_profile(resume_text)


# Display result
print("\n===== EXTRACTED CANDIDATE PROFILE =====")

for key, value in profile.items():
    print(f"{key}: {value}")

print("========================================\n")