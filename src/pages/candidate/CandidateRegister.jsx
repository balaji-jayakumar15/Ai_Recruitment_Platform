import "../css/CandidateRegister.css";

function CandidateRegister() {
  const handleSubmit = (event) => {
    event.preventDefault();

    console.log("Candidate registration submitted");
  };

  return (
    <div className="candidate-register-page">

      <div className="candidate-register-card">

        <div className="candidate-register-header">
          <h1>Create Candidate Account</h1>
          <p>Register to explore suitable job opportunities.</p>
        </div>

        <form
          className="candidate-register-form"
          onSubmit={handleSubmit}
        >

          <div className="candidate-register-field">
            <label htmlFor="candidate-name">
              Full Name
            </label>

            <input
              id="candidate-name"
              type="text"
              placeholder="Enter your full name"
              required
            />
          </div>

          <div className="candidate-register-field">
            <label htmlFor="register-email">
              Email
            </label>

            <input
              id="register-email"
              type="email"
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="candidate-register-field">
            <label htmlFor="register-password">
              Password
            </label>

            <input
              id="register-password"
              type="password"
              placeholder="Create a password"
              required
            />
          </div>

          <div className="candidate-register-field">
            <label htmlFor="confirm-password">
              Confirm Password
            </label>

            <input
              id="confirm-password"
              type="password"
              placeholder="Confirm your password"
              required
            />
          </div>

          <button
            type="submit"
            className="candidate-register-button"
          >
            Create Account
          </button>

        </form>

        <p className="candidate-register-login">
          Already have an account?
          <a href="/candidate/login">
            Login
          </a>
        </p>

      </div>

    </div>
  );
}

export default CandidateRegister;