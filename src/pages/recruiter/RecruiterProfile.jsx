import React, { useState } from "react";
import "../../css/RecruiterProfile.css";

function RecruiterProfile() {
  const [profile, setProfile] = useState({
    name: "Recruiter Name",
    email: "recruiter@example.com",
    company: "ABC Technologies",
    role: "HR Recruiter",
    phone: "",
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
    <div className="recruiter-profile-page">
      <div className="recruiter-profile-container">
        <h1>Recruiter Profile</h1>

        <p className="profile-subtitle">
          Manage your recruiter and company information.
        </p>

        <form onSubmit={handleSubmit} className="recruiter-profile-form">
          <div className="form-group">
            <label htmlFor="name">Recruiter Name</label>

            <input
              id="name"
              name="name"
              type="text"
              value={profile.name}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="email">Email</label>

            <input
              id="email"
              name="email"
              type="email"
              value={profile.email}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="company">Company Name</label>

            <input
              id="company"
              name="company"
              type="text"
              value={profile.company}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="role">Role</label>

            <input
              id="role"
              name="role"
              type="text"
              value={profile.role}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="phone">Phone Number</label>

            <input
              id="phone"
              name="phone"
              type="tel"
              placeholder="Enter phone number"
              value={profile.phone}
              onChange={handleChange}
            />
          </div>

          <button type="submit" className="update-profile-button">
            Update Profile
          </button>
        </form>
      </div>
    </div>
  );
}

export default RecruiterProfile;