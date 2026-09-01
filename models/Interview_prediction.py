import joblib
import pandas as pd
import os


# Load trained Model 4
MODEL_PATH = "interview_prediction.pkl"

model4 = joblib.load(MODEL_PATH)


def predict_interview(
    skill_match_percent,
    preferred_skill_match_percent,
    experience_score,
    project_match_percent,
    education_score,
    ats_score,
    experience_years,
    job_role
):
    """
    Predict whether a candidate is likely to be shortlisted
    for an interview and return the probability.
    """

    # Create candidate input
    candidate = pd.DataFrame({
        "Skill_Match_Percent": [skill_match_percent],
        "Preferred_Skill_Match_Percent": [preferred_skill_match_percent],
        "Experience_Score": [experience_score],
        "Project_Match_Percent": [project_match_percent],
        "Education_Score": [education_score],
        "ATS_Score": [ats_score],
        "Experience_Years": [experience_years],
        "Job_Role": [job_role]
    })

    # Prediction
    prediction = model4.predict(candidate)[0]

    # Probability
    probabilities = model4.predict_proba(candidate)[0]

    # Find index of Likely class
    classes = model4.named_steps["classifier"].classes_

    likely_index = list(classes).index("Likely")

    probability = probabilities[likely_index] * 100

    return {
        "interview_prediction": prediction,
        "interview_probability": round(probability, 2)
    }


# Test the model
if __name__ == "__main__":

    result = predict_interview(
        skill_match_percent=89.17,
        preferred_skill_match_percent=100,
        experience_score=100,
        project_match_percent=90,
        education_score=100,
        ats_score=88,
        experience_years=4,
        job_role="Data Scientist"
    )

    print("=" * 50)
    print("INTERVIEW PREDICTION")
    print("=" * 50)

    print("Prediction:",
          result["interview_prediction"])

    print("Interview Probability:",
          result["interview_probability"], "%")