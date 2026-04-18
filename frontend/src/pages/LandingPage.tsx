import { useRef } from "react";
import { useNavigate } from "react-router-dom";

const FEATURES = [
  {
    title: "AI-powered matchmaking",
    description:
      "Intelligent matching uses interests, goals, and event context to surface high-synergy connections quickly."
  },
  {
    title: "On-chain profile registration",
    description:
      "Participants register profiles directly to the smart contract for transparent and tamper-resistant event identity."
  },
  {
    title: "Verifiable event networking",
    description:
      "Every registration is linked to a wallet address for auditable attendee credibility and trust-first collaboration."
  }
];

export default function LandingPage() {
  const navigate = useNavigate();
  const featureSectionRef = useRef<HTMLElement | null>(null);

  const handleGetStarted = () => {
    navigate("/register");
  };

  const handleLearnMore = () => {
    featureSectionRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  return (
    <main className="relative min-h-screen overflow-hidden">
      <div className="gradient-orb gradient-orb--one" />
      <div className="gradient-orb gradient-orb--two" />
      <div className="landing-grid-overlay" />

      <section className="relative z-10 mx-auto flex max-w-7xl flex-col px-6 pb-24 pt-16 md:px-10 lg:px-14 lg:pt-24">
        <div className="grid gap-10 lg:grid-cols-[1.05fr_0.95fr] lg:items-center">
          <div className="animate-rise">
            <span className="inline-flex items-center rounded-full border border-primary/40 bg-primary/15 px-4 py-1.5 text-xs font-semibold uppercase tracking-widest text-primary">
              AI + Web3 Event Matchmaker
            </span>
            <h1 className="mt-6 text-5xl font-headline font-black leading-[1.05] text-white md:text-6xl xl:text-7xl">
              Match High-Value Builders
              <span className="block bg-gradient-to-r from-secondary via-white to-primary bg-clip-text text-transparent">
                In Real Time
              </span>
            </h1>
            <p className="mt-6 max-w-2xl text-base text-white/75 md:text-lg">
              Launch a premium networking experience where event attendees connect by verified
              wallet identity, shared interests, and startup goals.
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              <button
                type="button"
                onClick={handleGetStarted}
                className="rounded-xl border border-primary/40 bg-primary px-6 py-3 text-sm font-semibold text-on-primary transition hover:-translate-y-0.5 hover:shadow-[0_12px_32px_rgba(176,127,241,0.55)] md:text-base"
              >
                Get Started
              </button>
              <button
                type="button"
                onClick={handleLearnMore}
                className="rounded-xl border border-white/30 bg-white/10 px-6 py-3 text-sm font-semibold text-white transition hover:-translate-y-0.5 hover:bg-white/20 md:text-base"
              >
                Learn More
              </button>
            </div>
          </div>

          <div className="relative hidden min-h-[460px] lg:block">
            <article className="floating-card glass-panel absolute left-0 top-8 w-72 rounded-2xl border border-white/15 p-5">
              <p className="text-xs uppercase tracking-widest text-secondary">Live Matching</p>
              <h3 className="mt-2 text-lg font-bold text-white">AI-powered matchmaking</h3>
              <p className="mt-2 text-sm text-white/70">Builder profiles ranked by collaboration potential.</p>
            </article>

            <article className="floating-card floating-card--delay glass-panel absolute right-0 top-36 w-72 rounded-2xl border border-white/15 p-5">
              <p className="text-xs uppercase tracking-widest text-secondary">Smart Contract</p>
              <h3 className="mt-2 text-lg font-bold text-white">On-chain profile registration</h3>
              <p className="mt-2 text-sm text-white/70">Every attendee registers through wallet-signed transactions.</p>
            </article>

            <article className="floating-card floating-card--delay-2 glass-panel absolute left-14 top-[19.5rem] w-72 rounded-2xl border border-white/15 p-5">
              <p className="text-xs uppercase tracking-widest text-secondary">Event Trust Layer</p>
              <h3 className="mt-2 text-lg font-bold text-white">Verifiable networking</h3>
              <p className="mt-2 text-sm text-white/70">Create transparent and credibility-first event interactions.</p>
            </article>
          </div>
        </div>
      </section>

      <section ref={featureSectionRef} className="relative z-10 mx-auto max-w-7xl px-6 pb-24 md:px-10 lg:px-14">
        <div className="grid gap-5 md:grid-cols-3">
          {FEATURES.map((feature, index) => (
            <article
              key={feature.title}
              className="glass-panel rounded-2xl border border-white/15 p-6 animate-rise"
              style={{ animationDelay: `${index * 120}ms` }}
            >
              <p className="text-xs uppercase tracking-widest text-primary">Feature 0{index + 1}</p>
              <h2 className="mt-3 text-2xl font-headline font-bold text-white">{feature.title}</h2>
              <p className="mt-3 text-white/70">{feature.description}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
