import "../css/Home.css";

function Home() {
  return (
    <div className="home-page">

      <header className="home-header">
        <div className="home-logo">
          AI Recruitment  
        </div>

        <nav className="home-nav">
          <a href="#features">Features</a>
          <a href="/candidate/login">Candidate Login</a>
          <a href="/recruiter/login">Recruiter Login</a>
        </nav>
      </header>

      <main className="home-main">

        <section className="home-hero">
          <div className="home-hero-content">

            <p className="home-label">
              AI POWERED RECRUITMENT
            </p>

            <h1>
              Find the right opportunity with AI
            </h1>

            <p className="home-description">
              Our AI Recruitment Platform helps candidates
              find suitable jobs and helps recruiters identify
              the best candidates.
            </p>

            <div className="home-buttons">
              <a
                href="/candidate/jobs"
                className="home-btn home-btn-primary"
              >
                Find Jobs
              </a>

              <a
                href="/recruiter/login"
                className="home-btn home-btn-secondary"
              >
                Recruiter Login
              </a>
            </div>

          </div>
        </section>

        <section
          id="features"
          className="home-features"
        >
          <h2>Smart Recruitment Features</h2>

          <div className="home-feature-grid">

            <div className="home-feature-card">
              <h3>AI Resume Analysis</h3>
              <p>
                Analyze resumes and identify important
                candidate information.
              </p>
            </div>

            <div className="home-feature-card">
              <h3>Smart Job Matching</h3>
              <p>
                Match candidates with suitable job
                opportunities.
              </p>
            </div>

            <div className="home-feature-card">
              <h3>Skill Matching</h3>
              <p>
                Compare candidate skills with required
                job skills.
              </p>
            </div>

            <div className="home-feature-card">
              <h3>AI Candidate Ranking</h3>
              <p>
                Rank candidates based on their suitability
                for the job.
              </p>
            </div>

          </div>
        </section>

      </main>

      <footer className="home-footer">
        <p>AI Recruitment Platform</p>
      </footer>

    </div>
  );
}

export default Home;