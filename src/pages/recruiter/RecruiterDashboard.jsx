import React from "react";
import "../../css/RecruiterDashboard.css";

function RecruiterDashboard() {
  const stats = [
    { title: "Active Jobs", value: "5" },
    { title: "Applications", value: "227" },
    { title: "Closed Jobs", value: "3" },
    { title: "Shortlisted", value: "12" },
  ];

  const recentJobs = [
    {
      title: "Data Scientist",
      applicants: 227,
      deadline: "30 Aug 2026",
    },
    {
      title: "Backend Developer",
      applicants: 104,
      deadline: "2 Sep 2026",
    },
  ];

  return (
    <div className="recruiter-dashboard-page">
      <div className="dashboard-container">
        <header className="dashboard-header">
          <h1>Welcome, Recruiter</h1>
          <p>
            Manage your jobs and track candidate applications.
          </p>
        </header>

        <section className="stats-grid">
          {stats.map((stat, index) => (
            <div className="stat-card" key={index}>
              <h3>{stat.title}</h3>
              <p>{stat.value}</p>
            </div>
          ))}
        </section>

        <section className="recent-jobs-section">
          <h2>Recent Jobs</h2>

          <div className="recent-jobs-list">
            {recentJobs.map((job, index) => (
              <div className="recent-job-card" key={index}>
                <div>
                  <h3>{job.title}</h3>
                  <p>
                    {job.applicants} Applicants
                  </p>
                  <p>
                    Deadline: {job.deadline}
                  </p>
                </div>

                <button className="view-applicants-button">
                  View Applicants
                </button>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}

export default RecruiterDashboard;