import React, { useState } from "react";
import "../../css/CreateJob.css";

function CreateJob() {
  const [formData, setFormData] = useState({
    jobTitle: "",
    company: "",
    location: "",
    experience: "",
    education: "",
    description: "",
    requiredSkills: "",
    preferredSkills: "",
    deadline: "",
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

    const isEmpty = Object.values(formData).some(
      (value) => value.trim() === ""
    );

    if (isEmpty) {
      alert("Please fill in all fields.");
      return;
    }

    alert("Job created successfully!");
  };

  return (
    <div className="create-job-page">
      <div className="create-job-container">
        <h1>Create Job</h1>
        <p className="create-job-subtitle">
          Add the details of the job opportunity.
        </p>

        <form onSubmit={handleSubmit} className="job-form">
          <div className="form-group">
            <label htmlFor="jobTitle">Job Title</label>
            <input
              id="jobTitle"
              name="jobTitle"
              type="text"
              placeholder="Enter job title"
              value={formData.jobTitle}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="company">Company</label>
            <input
              id="company"
              name="company"
              type="text"
              placeholder="Enter company name"
              value={formData.company}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="location">Location</label>
            <input
              id="location"
              name="location"
              type="text"
              placeholder="Enter job location"
              value={formData.location}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="experience">Experience Required</label>
            <input
              id="experience"
              name="experience"
              type="text"
              placeholder="Example: 0–2 Years"
              value={formData.experience}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="education">Education</label>
            <input
              id="education"
              name="education"
              type="text"
              placeholder="Example: B.Tech / B.E"
              value={formData.education}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="description">Job Description</label>
            <textarea
              id="description"
              name="description"
              rows="5"
              placeholder="Enter job description"
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="requiredSkills">
              Required Skills
            </label>
            <textarea
              id="requiredSkills"
              name="requiredSkills"
              rows="3"
              placeholder="Example: Python, SQL, Machine Learning"
              value={formData.requiredSkills}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="preferredSkills">
              Preferred Skills
            </label>
            <textarea
              id="preferredSkills"
              name="preferredSkills"
              rows="3"
              placeholder="Example: AWS, TensorFlow"
              value={formData.preferredSkills}
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="deadline">
              Application Deadline
            </label>
            <input
              id="deadline"
              name="deadline"
              type="date"
              value={formData.deadline}
              onChange={handleChange}
            />
          </div>

          <button type="submit" className="create-job-button">
            Create Job
          </button>
        </form>
      </div>
    </div>
  );
}

export default CreateJob;