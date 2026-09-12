import React from "react";
import "../css/Components.css";

function Sidebar() {
  return (
    <aside className="common-sidebar">
      <div className="sidebar-title">
        AI Recruit
      </div>

      <nav className="sidebar-menu">
        <a href="/">Dashboard</a>
        <a href="/candidate/browse-jobs">Browse Jobs</a>
        <a href="/candidate/applications">My Applications</a>
        <a href="/candidate/profile">Profile</a>
        <a href="/logout">Logout</a>
      </nav>
    </aside>
  );
}

export default Sidebar;