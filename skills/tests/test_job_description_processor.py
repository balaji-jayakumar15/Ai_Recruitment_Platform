import sys
import os

# Add src folder to Python path
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from job_description_processor import process_job_description


# 22 Job Descriptions for testing
test_jobs = [

    {
        "title": "Python Developer",
        "description": "Required Python, Django and SQL. Git is preferred."
    },

    {
        "title": "Java Developer",
        "description": "Required Java, Spring Boot and MySQL."
    },

    {
        "title": "Frontend Developer",
        "description": "Required HTML, CSS and JavaScript. React is preferred."
    },

    {
        "title": "React Developer",
        "description": "Required JavaScript and React. TypeScript is preferred."
    },

    {
        "title": "Backend Developer",
        "description": "Required Python, FastAPI and REST API."
    },

    {
        "title": "Machine Learning Engineer",
        "description": "Required Python and Machine Learning. TensorFlow is preferred."
    },

    {
        "title": "AI Engineer",
        "description": "Required Python and Artificial Intelligence. PyTorch is preferred."
    },

    {
        "title": "Data Engineer",
        "description": "Required Python, SQL, PostgreSQL and Git."
    },

    {
        "title": "Web Developer",
        "description": "Required HTML, CSS and JavaScript."
    },

    {
        "title": "Full Stack Developer",
        "description": "Required JavaScript, React, Node.js and MongoDB."
    },

    {
        "title": "Django Developer",
        "description": "Required Python and Django. REST API is preferred."
    },

    {
        "title": "Database Developer",
        "description": "Required SQL, MySQL and PostgreSQL."
    },

    {
        "title": "Angular Developer",
        "description": "Required JavaScript and Angular. TypeScript is preferred."
    },

    {
        "title": "C++ Developer",
        "description": "Required C++ and SQL. Git is preferred."
    },

    {
        "title": "C# Developer",
        "description": "Required C# and SQL. GitHub is preferred."
    },

    {
        "title": "Flask Developer",
        "description": "Required Python and Flask. MongoDB is preferred."
    },

    {
        "title": "AI Developer",
        "description": "Required Python, Deep Learning and TensorFlow."
    },

    {
        "title": "Software Developer",
        "description": "Required Java, Git and SQL. Spring Boot is preferred."
    },

    {
        "title": "API Developer",
        "description": "Required Python and REST API. FastAPI is preferred."
    },

    {
        "title": "Data Science Developer",
        "description": "Required Python and Machine Learning. Deep Learning is preferred."
    },

    {
        "title": "Full Stack Engineer",
        "description": "Required React, Node.js, MongoDB and JavaScript."
    },

    {
        "title": "Python Backend Engineer",
        "description": "Required Python, FastAPI and PostgreSQL. GitHub is a plus."
    }
]


print("\n====================================")
print("JOB DESCRIPTION TESTING")
print("====================================")


passed = 0
failed = 0


for number, job in enumerate(test_jobs, start=1):

    result = process_job_description(
        job["title"],
        job["description"]
    )

    # Check whether required and preferred skills are available
    if (
        "required_skills" in result
        and "preferred_skills" in result
    ):
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(f"\nTest {number}: {job['title']}")
    print(f"Status: {status}")

    print(
        f"Required: {result['required_skills']}"
    )

    print(
        f"Preferred: {result['preferred_skills']}"
    )


print("\n====================================")
print("TEST SUMMARY")
print("====================================")

print(f"Total Tests : {len(test_jobs)}")
print(f"Passed      : {passed}")
print(f"Failed      : {failed}")


if failed == 0:
    print("\nAll Job Description tests passed successfully!")
else:
    print("\nSome tests failed. Please check the output.")