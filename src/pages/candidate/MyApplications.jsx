import React from "react";
import "../../css/MyApplications.css";

function MyApplications() {
  const applications = [
    {
      id: "APP001",
      jobTitle: "Data Scientist",
      company: "ABC Technologies",
      appliedDate: "20 Aug 2026",
      status: "Under Review",
    },
    {
      id: "APP002",
      jobTitle: "Frontend Developer",
      company: "Tech Solutions",
      appliedDate: "18 Aug 2026",
      status: "Shortlisted",
    },
    {
      id: "APP003",
      jobTitle: "Backend Developer",
      company: "Digital Works",
      appliedDate: "15 Aug 2026",
      status: "Applied",
    },
  ];

  return (
    <div className="my-applications-page">
      <div className="applications-container">
        <div className="applications-header">
          <h1>My Applications</h1>
          <p>Track the status of your job applications.</p>
        </div>

        <div className="applications-list">
          {applications.map((application) => (
            <div
              className="application-card"
              key={application.id}
            >
              <div className="application-info">
                <h2>{application.jobTitle}</h2>

                <p>
                  <strong>Company:</strong>{" "}
                  {application.company}
                </p>

                <p>
                  <strong>Application ID:</strong>{" "}
                  {application.id}
                </p>

                <p>
                  <strong>Applied Date:</strong>{" "}
                  {application.appliedDate}
                </p>
              </div>

              <div className="application-status">
                <span>Status</span>
                <strong>{application.status}</strong>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default MyApplications;