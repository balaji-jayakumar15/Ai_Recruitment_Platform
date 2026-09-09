import React from "react";
import "../../css/CandidateDetails.css";

function CandidateDetails() {
  const candidate = {
    id: "C0653",
    name: "Candidate Name",
    email: "candidate@example.com",
    education: "B.Tech Computer Science",
    experience: "2 Years",
    skills: ["Python", "SQL", "React", "Machine Learning"],
    matchScore: "89.17%",
  };

  return (
    <div className="candidate-details-page">
      <div className="candidate-details-container">
        <div className="details-header">
          <div>
            <h1>{candidate.name}</h1>
            <p>Candidate ID: {candidate.id}</p>
          </div>

          <div className="match-score-box">
            <span>Match Score</span>
            <strong>{candidate.matchScore}</strong>
          </div>
        </div>

        <div className="details-card">
          <h2>Personal Information</h2>

          <div className="info-grid">
            <div>
              <span>Email</span>
              <p>{candidate.email}</p>
            </div>

            <div>
              <span>Education</span>
              <p>{candidate.education}</p>
            </div>

            <div>
              <span>Experience</span>
              <p>{candidate.experience}</p>
            </div>
          </div>
        </div>

        <div className="details-card">
          <h2>Skills</h2>

          <div className="skills-list">
            {candidate.skills.map((skill) => (
              <span className="skill-badge" key={skill}>
                {skill}
              </span>
            ))}
          </div>
        </div>

        <div className="details-card">
          <h2>Resume</h2>

          <p>
            Candidate resume is available for recruiter review.
          </p>

          <button className="resume-button">
            View Resume
          </button>
        </div>

        <div className="candidate-actions">
          <button className="shortlist-button">
            Shortlist Candidate
          </button>

          <button className="reject-button">
            Reject Candidate
          </button>
        </div>
      </div>
    </div>
  );
}

export default CandidateDetails;