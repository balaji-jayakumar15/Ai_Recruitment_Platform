import joblib
import pandas as pd
import os


# ============================================================
# MODEL 5 - SALARY PREDICTION
# ============================================================

# Model path
MODEL_PATH = "salary_prediction.pkl"


# Load trained model
salary_model = joblib.load(MODEL_PATH)


# ============================================================
# SALARY PREDICTION FUNCTION
# ============================================================

def predict_salary(
    job_role,
    location,
    experience_level,
    experience_years,
    education,
    technical_skills,
    skill_match_percent,
    preferred_skill_match_percent,
    experience_score,
    project_match_percent,
    education_score,
    ats_score
):
    """
    Predict candidate salary using the trained Model 5.

    Returns:
        Dictionary containing predicted salary in LPA and INR.
    """

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "Job_Role": job_role,
        "Location": location,
        "Experience_Level": experience_level,
        "Experience_Years": experience_years,
        "Education": education,
        "Technical_Skills": technical_skills,
        "Skill_Match_Percent": skill_match_percent,
        "Preferred_Skill_Match_Percent": preferred_skill_match_percent,
        "Experience_Score": experience_score,
        "Project_Match_Percent": project_match_percent,
        "Education_Score": education_score,
        "ATS_Score": ats_score
    }])

    # Predict salary
    predicted_salary_lpa = salary_model.predict(input_data)[0]

    # Prevent negative prediction
    predicted_salary_lpa = max(0, predicted_salary_lpa)

    # Convert LPA to INR
    predicted_salary_inr = predicted_salary_lpa * 100000

    return {
        "job_role": job_role,
        "location": location,
        "predicted_salary_lpa": round(predicted_salary_lpa, 2),
        "predicted_salary_inr": round(predicted_salary_inr, 0)
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    result = predict_salary(
        job_role="Data Scientist",
        location="Chennai, Tamil Nadu, India",
        experience_level="Mid-level",
        experience_years=4,
        education="B.Tech Computer Science",
        technical_skills="Python, SQL, Machine Learning, Pandas, Scikit-learn",
        skill_match_percent=83.33,
        preferred_skill_match_percent=80.00,
        experience_score=100,
        project_match_percent=85.00,
        education_score=100,
        ats_score=86.50
    )

    print("=" * 50)
    print("MODEL-5 SALARY PREDICTION")
    print("=" * 50)

    print("Job Role:", result["job_role"])
    print("Location:", result["location"])

    print(
        "Predicted Salary:",
        result["predicted_salary_lpa"],
        "LPA"
    )

    print(
        "Predicted Salary: ₹{:,.0f}".format(
            result["predicted_salary_inr"]
        )
    )