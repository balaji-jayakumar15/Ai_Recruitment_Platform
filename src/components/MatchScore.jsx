import React from "react";
import "../css/Components.css";

function MatchScore({ score }) {
  return (
    <div className="match-score">
      <span className="match-score-label">
        AI Match Score
      </span>

      <span className="match-score-value">
        {score}%
      </span>
    </div>
  );
}

export default MatchScore;