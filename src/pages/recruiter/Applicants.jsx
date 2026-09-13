import React from "react";
import "../../css/Applicants.css";

function Applicants() {
  const applicants = [
    {
      id: "C0653",
      role: "Data Scientist",
      matchScore: "89.17%",
    },
    {
      id: "C0709",
      role: "Data Scientist",
      matchScore: "84.17%",
    },
    {
      id: "C0625",
      role: "Data Scientist",
      matchScore: "83.83%",
    },
    {
      id: "C0712",
      role: "Data Scientist",
      matchScore: "80.45%",
    },
  ];

  return (
    <div className="applicants-page">
      <div className="applicants-container">
        <div className="applicants-header">
          <h1>Data Scientist</h1>
          <p>227 Applicants</p>
        </div>

        <div className="applicants-table-wrapper">
          <table className="applicants-table">
            <thead>
              <tr>
                <th>Candidate ID</th>
                <th>Role</th>
                <th>Match Score</th>
                <th>Action</th>
              </tr>
            </thead>

            <tbody>
              {applicants.map((applicant) => (
                <tr key={applicant.id}>
                  <td>{applicant.id}</td>
                  <td>{applicant.role}</td>
                  <td>
                    <span className="match-score">
                      {applicant.matchScore}
                    </span>
                  </td>
                  <td>
                    <button className="view-candidate-button">
                      View Candidate
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <button className="rank-button">
          Rank Candidates
        </button>
      </div>
    </div>
  );
}

export default Applicants;