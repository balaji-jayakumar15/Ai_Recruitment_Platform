# ============================================================
# MODEL 3 - CANDIDATE RANKING
# ============================================================

def generate_recommendation(score):

    if score >= 85:
        return "Strongly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Consider"

    else:
        return "Not Recommended"


# ============================================================
# RECOMMENDATION REASON
# ============================================================

def generate_recommendation_reason(candidate):

    score = candidate["job_match_score"]

    matched = candidate.get("matched_skills", [])
    missing = candidate.get("missing_skills", [])

    # Convert strings to lists
    if isinstance(matched, str):
        matched = [
            skill.strip()
            for skill in matched.split(",")
            if skill.strip()
        ]

    if isinstance(missing, str):
        missing = [
            skill.strip()
            for skill in missing.split(",")
            if skill.strip()
        ]

    # Generate recommendation
    recommendation = generate_recommendation(score)

    # Matched skills text
    if matched:
        matched_text = ", ".join(matched)
    else:
        matched_text = "limited required skills"

    # Missing skills text
    if missing:

        missing_text = ", ".join(missing)

        reason = (
            f"{recommendation}: Strong match with "
            f"{matched_text}. "
            f"Missing skills include {missing_text}."
        )

    else:

        reason = (
            f"{recommendation}: Strong match with "
            f"{matched_text}. "
            f"The candidate has no major missing required skills."
        )

    return recommendation, reason


# ============================================================
# RANK APPLICANTS
# ============================================================

def rank_applicants(candidates, top_n=3):

    if not candidates:
        return []

    # Sort by job match score
    ranked = sorted(
        candidates,
        key=lambda x: x["job_match_score"],
        reverse=True
    )

    # Add rank, recommendation and reason
    for rank, candidate in enumerate(ranked, start=1):

        candidate["rank"] = rank

        recommendation, reason = generate_recommendation_reason(
            candidate
        )

        candidate["recommendation"] = recommendation
        candidate["recommendation_reason"] = reason

    return ranked[:top_n]


# ============================================================
# TEST MODEL 3
# ============================================================

if __name__ == "__main__":

    candidates = [

        {
            "candidate_id": "C0653",
            "job_role": "Data Scientist",
            "job_match_score": 89.17,
            "matched_skills": [
                "jupyter",
                "machine learning",
                "matplotlib",
                "numpy",
                "scikit-learn",
                "sql"
            ],
            "missing_skills": []
        },

        {
            "candidate_id": "C0709",
            "job_role": "Data Scientist",
            "job_match_score": 84.17,
            "matched_skills": [
                "jupyter",
                "machine learning",
                "matplotlib",
                "pandas",
                "python",
                "scikit-learn"
            ],
            "missing_skills": []
        },

        {
            "candidate_id": "C0625",
            "job_role": "Data Scientist",
            "job_match_score": 83.83,
            "matched_skills": [
                "matplotlib",
                "numpy",
                "python",
                "seaborn",
                "sql",
                "statistics"
            ],
            "missing_skills": []
        },

        {
            "candidate_id": "C0005",
            "job_role": "Data Scientist",
            "job_match_score": 45.00,
            "matched_skills": [
                "python"
            ],
            "missing_skills": [
                "sql",
                "pandas",
                "machine learning"
            ]
        }
    ]

    # Rank candidates
    top3 = rank_applicants(
        candidates,
        top_n=3
    )

    print("=" * 60)
    print("MODEL 3 - CANDIDATE RANKING")
    print("=" * 60)

    print("\nTOP 3 CANDIDATES")
    print("=" * 60)

    for candidate in top3:

        print("Rank:", candidate["rank"])
        print("Candidate:", candidate["candidate_id"])
        print("Job Role:", candidate["job_role"])
        print("Match Score:",
              candidate["job_match_score"], "%")
        print("Matched Skills:",
              ", ".join(candidate["matched_skills"]))

        print(
            "Missing Skills:",
            ", ".join(candidate["missing_skills"])
            if candidate["missing_skills"]
            else "None"
        )

        print(
            "Recommendation:",
            candidate["recommendation"]
        )

        print(
            "Reason:",
            candidate["recommendation_reason"]
        )

        print("-" * 60)