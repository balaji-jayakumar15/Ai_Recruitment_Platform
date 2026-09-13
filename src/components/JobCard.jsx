import React from "react";
import "../css/Components.css";

function JobCard({ job }) {
  return (
    <div className="common-job-card">
      <h3>{job.title}</h3>

      <p className="job-card-company">
        {job.company}
      </p>

      <p>
        <strong>Experience:</strong>{" "}
        {job.experience || "Not specified"}
      </p>

      <p>
        <strong>Location:</strong>{" "}
        {job.location || "Not specified"}
      </p>

      <p>
        <strong>Skills:</strong>
      </p>

      <p className="job-card-skills">
        {job.skills}
      </p>

      <button className="common-primary-button">
        View Details
      </button>
    </div>
  );
}

export default JobCard;