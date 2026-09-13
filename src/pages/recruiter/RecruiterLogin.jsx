import React, { useState } from "react";
import "../../css/RecruiterLogin.css";

function RecruiterLogin() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!email || !password) {
      alert("Please enter email and password.");
      return;
    }

    alert("Login successful!");
  };

  return (
    <div className="recruiter-login-page">
      <div className="recruiter-login-card">
        <h1>Recruiter Login</h1>
        <p>Login to manage your recruitment activities.</p>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
          </div>

          <button type="submit" className="login-button">
            Login
          </button>
        </form>

        <p className="register-text">
          Don't have an account?{" "}
          <button type="button" className="register-link">
            Recruiter Registration
          </button>
        </p>
      </div>
    </div>
  );
}

export default RecruiterLogin;