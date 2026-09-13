import React from "react";
import "../../css/ApplicationSuccess.css";

function ApplicationSuccess() {
  return (
    <div className="success-page">
      <div className="success-card">
        <div className="success-icon">✓</div>

        <h1>Application Submitted Successfully</h1>

        <p>
          Your application has been submitted successfully.
        </p>

        <p className="job-name">
          Job: <strong>Data Scientist</strong>
        </p>

        <button className="applications-button">
          View My Applications
        </button>
      </div>
    </div>
  );
}

export default ApplicationSuccess;