import React from "react";
import "../../css/JobDetails.css";

function JobDetails() {
  const job = {
    title: "Data Scientist",
    company: "IT Services",
    location: "Chennai",
    experience: "0–2 Years",
    description:
      "We are looking for a Data Scientist to analyze data and build machine learning solutions.",
    requiredSkills: [
      "Python",
      "SQL",
      "Machine Learning",
      "Pandas",
    ],
    preferredSkills: [
      "TensorFlow",
      "AWS",
    ],
  };

  return (
    <div className="job-details-page">
      <div className="job-details-card">
        <h1>{job.title}</h1>

        <p className="company">{job.company}</p>

        <div className="job-info">
          <p>
            <strong>Location:</strong> {job.location}
          </p>

          <p>
            <strong>Experience:</strong> {job.experience}
          </p>
        </div>

        <section>
          <h2>Job Description</h2>
          <p>{job.description}</p>
        </section>

        <section>
          <h2>Required Skills</h2>

          <ul>
            {job.requiredSkills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </section>

        <section>
          <h2>Preferred Skills</h2>

          <ul>
            {job.preferredSkills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </section>

        <button className="apply-button">
          Apply Now
        </button>
      </div>
    </div>
  );
}

export default JobDetails;