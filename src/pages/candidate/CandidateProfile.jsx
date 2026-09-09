import React, { useState } from "react";
import "../../css/CandidateProfile.css";

function CandidateProfile() {
  const [profile, setProfile] = useState({
    name: "Candidate Name",
    email: "candidate@example.com",
    education: "B.Tech Computer Science",
    experience: "2 Years",
    skills: "Python, SQL, React, Machine Learning",
    certifications: "AWS Cloud Practitioner",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;

    setProfile({
      ...profile,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert("Profile updated successfully!");
  };

  return (
    <div className="candidate-profile-page">
      <div className="profile-container">
        <h1>Candidate Profile</h1>
        <p className="profile-subtitle">
          Manage your personal and professional information.
        </p>

        <form onSubmit={handleSubmit} className="profile-form">
          <div className="form-group">
            <label>Full Name</label>
            <input
              type="text"
              name="name"
              value={profile.name}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={profile.email}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Education</label>
            <input
              type="text"
              name="education"
              value={profile.education}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Experience</label>
            <input
              type="text"
              name="experience"
              value={profile.experience}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Skills</label>
            <textarea
              name="skills"
              value={profile.skills}
              onChange={handleChange}
              rows="3"
            />
          </div>

          <div className="form-group">
            <label>Certifications</label>
            <textarea
              name="certifications"
              value={profile.certifications}
              onChange={handleChange}
              rows="3"
            />
          </div>

          <div className="form-group">
            <label>Resume</label>
            <input
              type="file"
              accept=".pdf,.doc,.docx"
            />
          </div>

          <button type="submit" className="update-button">
            Update Profile
          </button>
        </form>
      </div>
    </div>
  );
}

export default CandidateProfile;