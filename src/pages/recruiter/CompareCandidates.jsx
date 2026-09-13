import React from "react";
import "../../css/CompareCandidates.css";

function CompareCandidates() {
  const candidates = [
    {
      id: "C0653",
      score: "89.17%",
      experience: "2 Years",
      education: "B.Tech CSE",
      skills: "Python, SQL, ML",
    },
    {
      id: "C0709",
      score: "84.17%",
      experience: "3 Years",
      education: "B.E CSE",
      skills: "Python, React, SQL",
    },
    {
      id: "C0625",
      score: "83.83%",
      experience: "2 Years",
      education: "B.Tech IT",
      skills: "Python, Data Science, SQL",
    },
  ];

  return (
    <div className="compare-candidates-page">
      <div className="compare-container">
        <div className="compare-header">
          <h1>Compare Candidates</h1>
          <p>
            Compare candidate profiles and matching scores
            before making a recruitment decision.
          </p>
        </div>

        <div className="comparison-wrapper">
          <table className="comparison-table">
            <thead>
              <tr>
                <th>Details</th>

                {candidates.map((candidate) => (
                  <th key={candidate.id}>
                    {candidate.id}
                  </th>
                ))}
              </tr>
            </thead>

            <tbody>
              <tr>
                <td>Match Score</td>

                {candidates.map((candidate) => (
                  <td key={candidate.id}>
                    <strong>{candidate.score}</strong>
                  </td>
                ))}
              </tr>

              <tr>
                <td>Experience</td>

                {candidates.map((candidate) => (
                  <td key={candidate.id}>
                    {candidate.experience}
                  </td>
                ))}
              </tr>

              <tr>
                <td>Education</td>

                {candidates.map((candidate) => (
                  <td key={candidate.id}>
                    {candidate.education}
                  </td>
                ))}
              </tr>

              <tr>
                <td>Skills</td>

                {candidates.map((candidate) => (
                  <td key={candidate.id}>
                    {candidate.skills}
                  </td>
                ))}
              </tr>

              <tr>
                <td>Action</td>

                {candidates.map((candidate) => (
                  <td key={candidate.id}>
                    <button className="select-button">
                      Select
                    </button>
                  </td>
                ))}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default CompareCandidates;