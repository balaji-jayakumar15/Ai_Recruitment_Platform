import React from "react";
import "../css/Components.css";

function Navbar() {
  return (
    <header className="common-navbar">
      <div className="navbar-logo">
        AI Recruit
      </div>

      <nav className="navbar-links">
        <a href="/">Home</a>
        <a href="/candidate/login">Candidate</a>
        <a href="/recruiter/login">Recruiter</a>
      </nav>

      <div className="navbar-profile">
        <span>Welcome</span>
        <div className="navbar-profile-icon">👤</div>
      </div>
    </header>
  );
}

export default Navbar;