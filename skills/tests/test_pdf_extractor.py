import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)



from resume_processor import extract_candidate_profile


def test_resume(resume_path):

    print("\n===================================")
    print("Testing:", resume_path)
    print("===================================")

    with open(
        resume_path,
        "r",
        encoding="utf-8"
    ) as file:

        resume_text = file.read()

    result = extract_candidate_profile(resume_text)

    print(json.dumps(
        result,
        indent=4,
        ensure_ascii=False
    ))

    return result


if __name__ == "__main__":

    resume_files = [
        "skills/resumes/resume1.txt",
        "skills/resumes/resume2.txt",
        "skills/resumes/resume3.txt"
    ]

    for resume in resume_files:

        try:
            test_resume(resume)

        except FileNotFoundError:

            print(
                f"\nFile not found: {resume}"
            )