import React, { useState } from "react";
import "../../css/RecruiterRegister.css";

function RecruiterRegister() {
  const [formData, setFormData] = useState({
    recruiterName: "",
    companyName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (
      !formData.recruiterName ||
      !formData.companyName ||
      !formData.email ||
      !formData.password ||
      !formData.confirmPassword
    ) {
      alert("Please fill in all fields.");
      return;
    }

    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    alert("Recruiter account created successfully!");
  };

  return (
    <div className="recruiter-register-page">
      <div className="recruiter-register-card">
        <h1>Recruiter Registration</h1>

        <p>
          Create an account to manage your recruitment activities.
        </p>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="recruiterName">Recruiter Name</label>
            <input
              id="recruiterName"
              name="recruiterName"
              type="text"
              placeholder="Enter recruiter name"
              value={formData.recruiterName}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="companyName">Company Name</label>
            <input
              id="companyName"
              name="companyName"
              type="text"
              placeholder="Enter company name"
              value={formData.companyName}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              name="email"
              type="email"
              placeholder="Enter email"
              value={formData.email}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              placeholder="Enter password"
              value={formData.password}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="confirmPassword">
              Confirm Password
            </label>

            <input
              id="confirmPassword"
              name="confirmPassword"
              type="password"
              placeholder="Confirm password"
              value={formData.confirmPassword}
              onChange={handleChange}
            />
          </div>

          <button type="submit" className="create-account-button">
            Create Recruiter Account
          </button>
        </form>
      </div>
    </div>
  );
}

export default RecruiterRegister;