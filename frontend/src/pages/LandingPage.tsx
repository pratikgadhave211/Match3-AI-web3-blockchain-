import { useMemo } from "react";
import { useNavigate } from "react-router-dom";

const HERO_STATS = [
  { value: "500+", label: "Active Users" },
  { value: "10K+", label: "Connections Made" },
  { value: "95%", label: "Match Success" }
];

const ORBIT_NODES = [
  { angle: 0, delay: 0.5, accent: "primary" as const },
  { angle: 90, delay: 1, accent: "secondary" as const },
  { angle: 180, delay: 1.5, accent: "primary" as const },
  { angle: 270, delay: 2, accent: "secondary" as const }
];

const FEATURES = [
  {
    icon: "psychology",
    title: "AI-Powered Matching",
    description:
      "Our proprietary algorithm analyzes skills, goals, and values to find your highest-synergy collaboration opportunities in seconds."
  },
  {
    icon: "tune",
    title: "Smart Filtering",
    description:
      "Refine your network with adaptive filters across domain expertise, startup intent, and role alignment for relevant conversations."
  },
  {
    icon: "mail",
    title: "Instant Introductions",
    description:
      "Generate context-aware AI intros that break the ice instantly and convert mutual interest into meaningful interaction."
  },
  {
    icon: "people",
    title: "Build Your Network",
    description:
      "Track and nurture high-value connections with a premium relationship flow built for founders, builders, and operators."
  }
];

export default function LandingPage() {
  const navigate = useNavigate();
  const connectionLines = useMemo(() => {
    const centerX = 300;
    const centerY = 300;
    const distance = 150;

    return ORBIT_NODES.map((node) => {
      const radians = (node.angle * Math.PI) / 180;
      return {
        angle: node.angle,
        x: centerX + distance * Math.cos(radians),
        y: centerY + distance * Math.sin(radians)
      };
    });
  }, []);

  const navigateToRegister = () => navigate("/register");

  const scrollToFeatures = () => {
    document.getElementById("features")?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <main className="landing-page">
      <nav className="landing-fixed-nav" id="landing-nav">
        <div className="landing-nav-backdrop">
          <div className="landing-shell landing-nav-inner">
            <div className="landing-brand" onClick={() => navigate("/")}>MATCH3</div>
            <button onClick={navigateToRegister} className="landing-button landing-button--primary">
              Get Started
            </button>
          </div>
        </div>
      </nav>

      <section className="landing-hero-section">
        <div className="landing-video-background">
          <video autoPlay muted loop playsInline className="landing-video">
            <source src="https://cdn.dribbble.com/userupload/47426469/file/0ff6816e42475292f5cc195fd862e978.mp4" type="video/mp4" />
          </video>
          <div className="landing-video-dim" />
        </div>

        <div className="landing-orb landing-orb--one" />
        <div className="landing-orb landing-orb--two" />

        <div className="landing-shell landing-hero-grid">
          <div className="landing-hero-copy">
            <h1 className="landing-title">Find Your Perfect Match</h1>
            <p className="landing-subtitle">AI-Powered Networking for Web3 Builders</p>
            <p className="landing-description">
              Discover meaningful connections in seconds using cutting-edge AI. MATCH3 analyzes
              skills, goals, and values to connect you with the right people in the startup ecosystem.
            </p>

            <div className="landing-actions">
              <button onClick={navigateToRegister} className="landing-button landing-button--primary landing-button--large">
                Get Started
              </button>
              <button onClick={scrollToFeatures} className="landing-button landing-button--ghost landing-button--large">
                Learn More
              </button>
            </div>

            <div className="landing-stats">
              {HERO_STATS.map((stat, index) => (
                <div key={stat.label} className="landing-stat-block">
                  <div className="landing-stat-value">{stat.value}</div>
                  <p className="landing-stat-label">{stat.label}</p>
                  {index < HERO_STATS.length - 1 ? <div className="landing-stat-divider" /> : null}
                </div>
              ))}
            </div>
          </div>

          <div className="landing-visual" id="3d-container">
            <div className="landing-orbit-stage">
              <div className="landing-center-node">
                <span className="material-symbols-outlined">hub</span>
              </div>

              {ORBIT_NODES.map((node) => (
                <div
                  key={node.angle}
                  className="landing-orbit-node"
                  style={
                    {
                      "--angle": `${node.angle}deg`,
                      "--distance": "150px",
                      "--delay": `${node.delay}s`
                    } as React.CSSProperties
                  }
                >
                  <div className={`landing-mini-card landing-mini-card--${node.accent}`}>
                    <div className="landing-mini-avatar" />
                    <div className="landing-mini-line landing-mini-line--wide" />
                    <div className="landing-mini-line" />
                  </div>
                </div>
              ))}

              <svg className="landing-lines" viewBox="0 0 600 600" aria-hidden="true">
                {connectionLines.map((line) => (
                  <line
                    key={line.angle}
                    x1="300"
                    y1="300"
                    x2={line.x}
                    y2={line.y}
                    stroke="rgba(176, 127, 241, 0.28)"
                    strokeWidth="2"
                  />
                ))}
              </svg>
            </div>
          </div>
        </div>
      </section>

      <section id="features" className="landing-features-section">
        <div className="landing-shell">
          <div className="landing-section-header">
            <h2>How MATCH3 Works</h2>
            <p>
              Powered by advanced AI models to connect you with the right people, at the right time,
              for the right reasons.
            </p>
          </div>

          <div className="landing-features-grid">
            {FEATURES.map((feature, index) => (
              <article
                key={feature.title}
                className="landing-feature-card"
                style={{ animationDelay: `${index * 0.12}s` }}
              >
                <div className="landing-feature-icon">
                  <span className="material-symbols-outlined">{feature.icon}</span>
                </div>
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="landing-cta-section">
        <div className="landing-shell landing-cta-inner">
          <h2>Ready to Find Your Match?</h2>
          <p>
            Join innovators, builders, and founders already finding meaningful connections on MATCH3.
          </p>
          <button onClick={navigateToRegister} className="landing-button landing-button--primary landing-button--large">
            Get Started for Free
          </button>
        </div>
      </section>

      <footer className="landing-footer">
        <div className="landing-shell landing-footer-inner">
          <div className="landing-brand">MATCH3</div>
          <p>AI-Powered Networking for Web3 Builders</p>
          <small>© 2026 MATCH3. All rights reserved.</small>
        </div>
      </footer>
    </main>
  );
}
