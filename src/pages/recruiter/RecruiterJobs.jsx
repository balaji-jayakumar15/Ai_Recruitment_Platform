import React from "react";
import "../../css/RecruiterJobs.css";

function RecruiterJobs() {
  const jobs = [
    {
      title: "Data Scientist",
      applicants: 227,
      deadline: "Aug 30, 2026",
      status: "Active",
    },
    {
      title: "Backend Developer",
      applicants: 104,
      deadline: "Sep 2, 2026",
      status: "Active",
    },
    {
      title: "Frontend Developer",
      applicants: 86,
      deadline: "Sep 5, 2026",
      status: "Active",
    },
  ];

  const handleAction = (action, jobTitle) => {
    alert(`${action} selected for ${jobTitle}`);
  };

  return (
    <div className="recruiter-jobs-page">
      <div className="recruiter-jobs-container">
        <div className="jobs-header">
          <div>
            <h1>My Jobs</h1>
            <p>Manage your job postings and applications.</p>
          </div>

          <button
            className="create-job-button"
            onClick={() => handleAction("Create Job", "")}
          >
            Create Job
          </button>
        </div>

        <div className="jobs-list">
          {jobs.map((job, index) => (
            <div className="recruiter-job-card" key={index}>
              <div className="job-details">
                <h2>{job.title}</h2>

                <p>
                  <strong>{job.applicants}</strong> Applicants
                </p>

                <p>Deadline: {job.deadline}</p>

                <span className="job-status">
                  {job.status}
                </span>
              </div>

              <div className="job-actions">
                <button
                  onClick={() =>
                    handleAction("View", job.title)
                  }
                >
                  View
                </button>

                <button
                  onClick={() =>
                    handleAction("Edit", job.title)
                  }
                >
                  Edit
                </button>

                <button
                  className="close-button"
                  onClick={() =>
                    handleAction("Close", job.title)
                  }
                >
                  Close
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default RecruiterJobs;