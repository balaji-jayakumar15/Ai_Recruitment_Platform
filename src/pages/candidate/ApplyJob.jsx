import React, { useState } from "react";
import "../../css/ApplyJob.css";

function ApplyJob() {
  const [resume, setResume] = useState(null);

  const handleFileChange = (event) => {
    setResume(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!resume) {
      alert("Please upload your resume.");
      return;
    }

    alert("Application submitted successfully!");
  };

  return (
    <div className="apply-job-page">
      <div className="apply-job-card">
        <h1>Apply for Data Scientist</h1>

        <p className="apply-description">
          Upload your resume to apply for this job.
        </p>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="resume">Upload Resume</label>

            <input
              id="resume"
              type="file"
              accept=".pdf,.doc,.docx"
              onChange={handleFileChange}
            />
          </div>

          {resume && (
            <div className="resume-preview">
              <h3>Resume Preview</h3>
              <p>{resume.name}</p>
            </div>
          )}

          <button type="submit" className="submit-button">
            Submit Application
          </button>
        </form>
      </div>
    </div>
  );
}

export default ApplyJob;