import React from "react";
import "../../css/AIInsights.css";

function AIInsights() {
  const insights = [
    {
      title: "Top Matching Skills",
      value: "Python, SQL, Machine Learning",
    },
    {
      title: "Average Match Score",
      value: "84.4%",
    },
    {
      title: "Top Candidate",
      value: "C0653",
    },
    {
      title: "Recommended Candidates",
      value: "12",
    },
  ];

  return (
    <div className="ai-insights-page">
      <div className="ai-insights-container">
        <div className="insights-header">
          <h1>AI Recruitment Insights</h1>
          <p>
            AI-based insights to help recruiters understand
            candidate-job matching.
          </p>
        </div>

        <div className="insights-grid">
          {insights.map((insight, index) => (
            <div className="insight-card" key={index}>
              <h3>{insight.title}</h3>
              <p>{insight.value}</p>
            </div>
          ))}
        </div>

        <div className="recommendation-card">
          <h2>AI Recommendation</h2>

          <p>
            Candidates with strong skills in Python, SQL, and
            Machine Learning show the highest match for this
            job.
          </p>

          <p>
            Recruiters can review the top-ranked candidates
            before making the final selection.
          </p>
        </div>

        <div className="analysis-card">
          <h2>Skill Matching Summary</h2>

          <div className="skill-row">
            <span>Python</span>
            <strong>95%</strong>
          </div>

          <div className="skill-row">
            <span>SQL</span>
            <strong>90%</strong>
          </div>

          <div className="skill-row">
            <span>Machine Learning</span>
            <strong>85%</strong>
          </div>

          <div className="skill-row">
            <span>React</span>
            <strong>72%</strong>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AIInsights;