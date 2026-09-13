import React from "react";
import "../../css/CandidateRanking.css";

function CandidateRanking() {
  const candidates = [
    {
      id: "C0653",
      score: "89.17%",
      skills: "Python, SQL, Machine Learning",
      status: "Top Match",
    },
    {
      id: "C0709",
      score: "84.17%",
      skills: "Python, React, SQL",
      status: "Strong Match",
    },
    {
      id: "C0625",
      score: "83.83%",
      skills: "Python, Data Science, SQL",
      status: "Strong Match",
    },
    {
      id: "C0712",
      score: "80.45%",
      skills: "Python, SQL, AWS",
      status: "Good Match",
    },
  ];

  return (
    <div className="candidate-ranking-page">
      <div className="ranking-container">
        <div className="ranking-header">
          <h1>Candidate Ranking</h1>
          <p>
            Candidates ranked based on job requirements and
            matching skills.
          </p>
        </div>

        <div className="ranking-list">
          {candidates.map((candidate, index) => (
            <div className="ranking-card" key={candidate.id}>
              <div className="rank-number">
                #{index + 1}
              </div>

              <div className="candidate-info">
                <h2>{candidate.id}</h2>
                <p>
                  <strong>Skills:</strong> {candidate.skills}
                </p>
                <span className="candidate-status">
                  {candidate.status}
                </span>
              </div>

              <div className="score-section">
                <span>Match Score</span>
                <strong>{candidate.score}</strong>
              </div>

              <button className="view-details-button">
                View Details
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default CandidateRanking;