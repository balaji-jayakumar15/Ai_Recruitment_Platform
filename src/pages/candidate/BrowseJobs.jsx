import React, { useState } from "react";
import "../../css/BrowseJobs.css";

function BrowseJobs() {
  const [search, setSearch] = useState("");
  const [role, setRole] = useState("");
  const [experience, setExperience] = useState("");
  const [location, setLocation] = useState("");

  const jobs = [
    {
      title: "Data Scientist",
      company: "IT Services",
      experience: "0–2 Years",
      location: "Chennai",
      skills: "Python, SQL, Pandas, ML",
    },
    {
      title: "Backend Developer",
      company: "Tech Solutions",
      experience: "1–3 Years",
      location: "Bangalore",
      skills: "Python, Django, SQL, REST API",
    },
    {
      title: "Frontend Developer",
      company: "Digital Solutions",
      experience: "0–2 Years",
      location: "Chennai",
      skills: "React, JavaScript, HTML, CSS",
    },
  ];

  const filteredJobs = jobs.filter((job) => {
    const matchesSearch =
      job.title.toLowerCase().includes(search.toLowerCase()) ||
      job.company.toLowerCase().includes(search.toLowerCase());

    const matchesRole =
      role === "" || job.title === role;

    const matchesExperience =
      experience === "" || job.experience === experience;

    const matchesLocation =
      location === "" || job.location === location;

    return (
      matchesSearch &&
      matchesRole &&
      matchesExperience &&
      matchesLocation
    );
  });

  return (
    <div className="browse-jobs-page">
      <div className="browse-header">
        <h1>Browse Jobs</h1>
        <p>Find jobs that match your skills and experience.</p>
      </div>

      <div className="job-filters">
        <input
          type="text"
          placeholder="Search jobs..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="">All Roles</option>
          <option value="Data Scientist">Data Scientist</option>
          <option value="Backend Developer">Backend Developer</option>
          <option value="Frontend Developer">Frontend Developer</option>
        </select>

        <select
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
        >
          <option value="">All Experience</option>
          <option value="0–2 Years">0–2 Years</option>
          <option value="1–3 Years">1–3 Years</option>
        </select>

        <select
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        >
          <option value="">All Locations</option>
          <option value="Chennai">Chennai</option>
          <option value="Bangalore">Bangalore</option>
        </select>
      </div>

      <div className="jobs-container">
        {filteredJobs.length > 0 ? (
          filteredJobs.map((job, index) => (
            <div className="browse-job-card" key={index}>
              <h2>{job.title}</h2>

              <p className="job-company">
                {job.company}
              </p>

              <p>
                <strong>Experience:</strong> {job.experience}
              </p>

              <p>
                <strong>Location:</strong> {job.location}
              </p>

              <p>
                <strong>Skills:</strong> {job.skills}
              </p>

              <button>View Details</button>
            </div>
          ))
        ) : (
          <p className="no-jobs">
            No jobs found.
          </p>
        )}
      </div>
    </div>
  );
}

export default BrowseJobs;