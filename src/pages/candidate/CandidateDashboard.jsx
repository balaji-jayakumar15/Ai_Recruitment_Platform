import React from "react";
import "../../css/CandidateDashboard.css";

function CandidateDashboard() {
  const jobs = [
    {
      title: "Data Scientist",
      company: "ABC Technologies",
      skills: "Python, SQL, Pandas, Machine Learning",
    },
    {
      title: "Backend Developer",
      company: "XYZ Solutions",
      skills: "Python, Django, SQL, REST API",
    },
  ];

  return (
    <div className="candidate-dashboard">
      <header className="dashboard-header">
        <h1>Welcome, Candidate</h1>
        <p>Find the right opportunity with AI.</p>
      </header>

      <section className="application-summary">
        <div className="summary-card">
          <h3>Applications</h3>
          <p>5</p>
        </div>

        <div className="summary-card">
          <h3>Pending</h3>
          <p>2</p>
        </div>

        <div className="summary-card">
          <h3>Shortlisted</h3>
          <p>1</p>
        </div>

        <div className="summary-card">
          <h3>Rejected</h3>
          <p>2</p>
        </div>
      </section>

      <section className="recommended-section">
        <h2>Recommended Jobs</h2>

        <div className="job-list">
          {jobs.map((job, index) => (
            <div className="job-card" key={index}>
              <h3>{job.title}</h3>
              <p className="company-name">{job.company}</p>

              <p>
                <strong>Required Skills:</strong>
              </p>

              <p className="skills">{job.skills}</p>

              <button className="view-job-button">
                View Job
              </button>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default CandidateDashboard;