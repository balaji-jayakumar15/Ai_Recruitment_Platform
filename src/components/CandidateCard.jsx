import React from "react";
import "../css/Components.css";

function CandidateCard({ candidate }) {
  return (
    <div className="common-candidate-card">
      <div className="candidate-card-header">
        <div className="candidate-avatar">
          👤
        </div>

        <div>
          <h3>{candidate.name}</h3>
          <p>{candidate.email}</p>
        </div>
      </div>

      <div className="candidate-card-info">
        <p>
          <strong>Experience:</strong>{" "}
          {candidate.experience || "Not specified"}
        </p>

        <p>
          <strong>Skills:</strong>{" "}
          {candidate.skills || "Not specified"}
        </p>
      </div>

      <button className="common-primary-button">
        View Candidate
      </button>
    </div>
  );
}

export default CandidateCard;