import joblib


# Load trained model
model = joblib.load("resume_classifier.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def predict_role(resume_text):
    """
    Predict the job role and confidence score from resume text.

    Returns:
        predicted_role: predicted job role
        confidence: confidence percentage
    """

    if not isinstance(resume_text, str):
        raise TypeError("resume_text must be a string")

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty")

    # Convert resume text into TF-IDF features
    resume_vector = vectorizer.transform([resume_text])

    # Predict role
    predicted_role = model.predict(resume_vector)[0]

    # Get prediction probabilities
    probabilities = model.predict_proba(resume_vector)[0]

    # Highest probability
    confidence = max(probabilities) * 100

    return predicted_role, round(confidence, 2)

def predict_top_roles(resume_text, top_n=3):
    """
    Return the top N predicted job roles with probabilities.
    """

    if not isinstance(resume_text, str):
        raise TypeError("resume_text must be a string")

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty")

    # Convert resume to TF-IDF
    resume_vector = vectorizer.transform([resume_text])

    # Get probabilities
    probabilities = model.predict_proba(resume_vector)[0]

    # Get class names
    classes = model.classes_

    # Sort probabilities from highest to lowest
    ranked_indices = probabilities.argsort()[::-1][:top_n]

    results = []

    for index in ranked_indices:

        results.append({
            "job_role": classes[index],
            "confidence": round(probabilities[index] * 100, 2)
        })

    return results


if __name__ == "__main__":

    test_resume = """
    Python developer with experience in Python, Django, Flask,
    REST APIs, PostgreSQL, Git and Docker.
    Developed backend APIs and database-driven applications.
    """

    role, confidence = predict_role(test_resume)

    print("Resume Classification")
    print("=" * 40)
    print("Predicted Job Role:", role)
    print("Confidence:", confidence, "%")

    print("\nTop 3 Predictions")
    print("=" * 40)

    top_roles = predict_top_roles(test_resume, top_n=3)

    for i, result in enumerate(top_roles, start=1):
        print(
            f"{i}. {result['job_role']} "
            f"- {result['confidence']}%"
        )

