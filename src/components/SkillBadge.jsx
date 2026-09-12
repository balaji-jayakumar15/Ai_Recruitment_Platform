import React from "react";
import "../css/Components.css";

function SkillBadge({ skill }) {
  return (
    <span className="skill-badge">
      {skill}
    </span>
  );
}

export default SkillBadge;