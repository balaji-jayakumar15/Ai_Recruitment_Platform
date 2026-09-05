# M4 - Job Description Processing

## 1. Module Overview

The Job Description Processing module is responsible for analyzing job descriptions and identifying the skills required for a particular job role.

## 2. Objective

The main objective of this module is to extract technical skills from job descriptions and organize them into required and preferred skills.

## 3. Input

The system accepts:

- Job Title
- Job Description

Example:

Python Developer with Django, FastAPI and SQL experience.
Git and GitHub are preferred.

## 4. Processing Steps

1. Accept the job description.
2. Convert the text into lowercase.
3. Split the job description into sentences.
4. Match the text with the predefined skills list.
5. Identify required skills.
6. Identify preferred skills using preferred keywords.
7. Remove duplicate skills.
8. Generate structured JSON output.

## 5. Required Skills

Required skills are the skills that are directly mentioned as necessary for the job.

Example:

- Python
- Django
- FastAPI
- SQL
- REST API

## 6. Preferred Skills

Preferred skills are optional or additional skills mentioned using terms such as:

- Preferred
- Nice to have
- Good to have
- Optional
- Plus
- Bonus

Example:

- Git
- GitHub

## 7. Output Format

The final output is generated in JSON format.

Example:

{
  "job_title": "Python Developer",
  "required_skills": [
    "django",
    "fastapi",
    "python",
    "rest api",
    "sql"
  ],
  "preferred_skills": [
    "git",
    "github"
  ]
}

## 8. Testing

The Job Description Processor was tested using 22 different job descriptions covering multiple technical roles.

Test categories included:

- Python Developer
- Java Developer
- Frontend Developer
- React Developer
- Backend Developer
- Machine Learning Engineer
- AI Engineer
- Data Engineer
- Web Developer
- Full Stack Developer
- Django Developer
- Database Developer
- Angular Developer
- C++ Developer
- C# Developer
- Flask Developer
- AI Developer
- Software Developer
- API Developer
- Data Science Developer
- Full Stack Engineer
- Python Backend Engineer

## 9. Test Result

Total Tests: 22

Expected Result:

All valid job description inputs should generate both required_skills and preferred_skills fields.

## 10. Module Output

The final structured output can be used by other modules in the AI Recruitment Platform for job matching and candidate ranking.

## 11. Conclusion

The M4 Job Description Processing module extracts relevant skills from job descriptions and organizes them into a structured JSON format. The module supports required and preferred skill classification and has been tested with multiple job descriptions.