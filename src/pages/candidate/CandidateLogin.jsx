import "../css/CandidateLogin.css";

function CandidateLogin() {
  const handleSubmit = (event) => {
    event.preventDefault();

    console.log("Candidate login submitted");
  };

  return (
    <div className="candidate-login-page">

      <div className="candidate-login-card">

        <div className="candidate-login-header">
          <h1>Candidate Login</h1>
          <p>Login to find suitable job opportunities.</p>
        </div>

        <form
          className="candidate-login-form"
          onSubmit={handleSubmit}
        >

          <div className="candidate-login-field">
            <label htmlFor="candidate-email">
              Email
            </label>

            <input
              id="candidate-email"
              type="email"
              placeholder="Enter your email"
              required
            />
          </div>

          <div className="candidate-login-field">
            <label htmlFor="candidate-password">
              Password
            </label>

            <input
              id="candidate-password"
              type="password"
              placeholder="Enter your password"
              required
            />
          </div>

          <button
            type="submit"
            className="candidate-login-button"
          >
            Login
          </button>

        </form>

        <p className="candidate-login-register">
          Don't have an account?
          <a href="/candidate/register">
            Create Account
          </a>
        </p>

      </div>

    </div>
  );
}

export default CandidateLogin;