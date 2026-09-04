# AI Recruitment Platform - ML Models

## Model 1 - Resume Classification
Predicts the job role from resume text using TF-IDF and the trained classifier.

## Model 2 - Job Matching
Calculates:
- Required skill match
- Preferred skill match
- Experience score
- Project match
- Education score
- Final job match score

## Model 3 - Candidate Ranking
Ranks applicants according to job match score and returns the Top 3 candidates.

## Files

- resume_classifier.py - Resume classification
- resume_classifier.pkl - Trained classification model
- tfidf_vectorizer.pkl - TF-IDF vectorizer
- job_matching.py - Job matching
- candidate_ranking.py - Applicant ranking