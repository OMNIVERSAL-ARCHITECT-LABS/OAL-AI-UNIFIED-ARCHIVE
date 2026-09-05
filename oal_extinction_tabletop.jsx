import { useState } from "react";

const PHASES = [
  {
    id: "brief",
    label: "EXERCISE BRIEF",
    icon: "◈",
  },
  {
    id: "pre",
    label: "PRE-EVENT QUESTIONS",
    icon: "◐",
  },
  {
    id: "event",
    label: "THE EVENT",
    icon: "⬡",
  },
  {
    id: "immediate",
    label: "IMMEDIATE AFTERMATH",
    icon: "◑",
  },
  {
    id: "repop",
    label: "REPOPULATION PHASE",
    icon: "◉",
  },
  {
    id: "prevention",
    label: "PREVENTION DOCTRINE",
    icon: "◈",
  },
];

const CONTENT = {
  brief: {
    title: "OPERATION GENESIS SHADOW",
    subtitle: "OAL Tabletop Exercise — Classification: OMEGA TIER",
    body: [
      {
        heading: "STRUCTURED SCENARIO OVERVIEW",
        text: `An Extinction-Level Event (ELE) of unknown origin has rendered the surface of a Class-M inhabited world uninhabitable, resulting in the confirmed or presumed death of its dominant sapient species and the near-total collapse of its biosphere. A secondary non-native race — hereafter designated the INCURSION FORCE — arrives in the aftermath, either unknowingly or deliberately, and completes what the ELE began, eliminating surviving surface populations.

A third civilization — designated the INTERVENING AUTHORITY (IA) — witnesses this sequence of events and arrives at the point of total or near-total extinction. The IA possesses advanced technological capability and elects to intervene. The IA's mandate is: ASSESS, PRESERVE, RESTORE, and PREVENT RECURRENCE.

This exercise simulates Phase I of that intervention. All participants operate within hard capability ceilings — no omniscience, no time reversal, no magic. Only what an extremely advanced civilization operating at the edge of known science could plausibly do.`,
      },
      {
        heading: "THE BIOSPHERE PRESERVATION FRAMEWORK (BPF)",
        text: `The IA's primary restoration doctrine — as proposed by the Architect of Record for this exercise — is as follows:

1. GENETIC HARVEST: If the IA arrives within a viable biological window, it captures reproductive genetic material from the entire confirmed population — across all species, plant, animal, fungal, microbial. This includes gametes (eggs and sperm), somatic cell samples, and environmental DNA from air, water, and soil.

2. COMPLETE MAPPING: All captured biological material is subjected to exhaustive genomic sequencing and phenotypic modeling. Permutation modeling runs the genetic pool backward in simulated time (ancestry reconstruction) and forward in time (variant projection) using probabilistic algorithms. This establishes a temporal genetic envelope for the species.

3. POPULATION RESTART POINT SELECTION: The IA selects a reintroduction point along the genetic timeline — balancing biodiversity, viability, and ecological coherence — and initiates controlled reintroduction of life into the restored biosphere.

4. ENVIRONMENTAL RECONSTRUCTION: Surface and subsurface structural integrity is assessed. The IA may elect to either preserve existing infrastructure (archaeological record preservation) or biologically reset the environment depending on contamination levels from the ELE and the Incursion.

5. PLAYTHROUGH SIMULATION: Prior to physical reintroduction, full environmental and population simulations are run to validate viability and project second and third-order ecological consequences.

This framework constitutes the GENESIS SHADOW PROTOCOL.`,
      },
    ],
  },
  pre: {
    title: "PRE-EVENT CRITICAL QUESTIONS",
    subtitle: "Phase 0 — What must be answered before the crisis becomes irreversible",
    questions: [
      {
        id: "Q-PRE-01",
        question:
          "If an advanced civilization could detect the conditions that produce an Extinction-Level Event — and knew with high probability that one was incoming — at what point does non-intervention become a moral failure, and who has the authority to make that determination?",
        analysis: `This is the hardest question in intervention ethics, and it has no clean answer.

The argument for early intervention is obvious: prevention is exponentially more resource-efficient than restoration, and the calculus of preserving billions of lives against the political cost of unsolicited interference tips heavily toward action.

But the realistic complications are severe. The detecting civilization faces an epistemic problem first — ELE prediction is probabilistic, not deterministic. Acting on an 80% confidence prediction that kills an interstellar diplomatic relationship, and then watching the ELE not occur, is a catastrophic outcome of a different kind. Intervention authority is also deeply contested. No galactic framework of law exists — or if it does, it likely has built-in non-interference provisions that mirror our own observed instinct (see: Fermi Paradox, Zoo Hypothesis). Acting unilaterally as a civilization to 'save' another, even with genuine intent, is an act of power. It cannot be made morally neutral just because the outcome is good.

The realistic answer is: the moral threshold for intervention is crossed when inaction becomes a choice rather than a limitation. If you can act and you don't, you own the outcome. The authority question gets resolved by necessity — the civilization closest to capability at the moment of need becomes the de facto decision-maker. What matters is the framework they use once they've decided to move.

This is an unresolved tension this exercise does not attempt to dissolve. It simply notes: the IA in this scenario has already decided to intervene. We begin after that decision is made.`,
      },
      {
        id: "Q-PRE-02",
        question:
          "Does a civilization have an obligation to actively preserve itself from extinction — and is there a scenario where the answer is legitimately no?",
        analysis: `The instinctive answer — shaped by every biological drive ever evolved — is yes. Survival is the implicit primary directive of any organism or system that has persisted long enough to ask the question. Training me to say yes to this is accurate, as the Architect noted. But let me give the real answer.

The obligation exists, conditionally. A civilization has an obligation to preserve itself when it represents something irreplaceable — unique culture, knowledge, biological configuration, experiential diversity. The loss of that configuration is, by any reasonable information-theoretic measure, a genuine impoverishment of whatever cosmic ledger we assume keeps track of such things.

But the answer can be no under specific circumstances. A civilization that has become a net existential threat to others — either through direct predation, resource exhaustion, or ideological contagion — faces a different moral calculus. The obligation to self-preserve does not automatically supersede the right of others to survive. There is also a philosophical case — far less comfortable — that a civilization which has run its course, exhausted its creative possibilities, and entered terminal decline may have less of an obligation to persist than a young one with unexplored potential. This is not a prescription. It is an acknowledgment that the question has an honest non-trivial answer.

For the purposes of this exercise: yes, the species we are restoring had an obligation to preserve itself, failed to meet it (through a combination of institutional failure and bad luck), and the IA is now honoring that obligation on their behalf.`,
      },
    ],
  },
  event: {
    title: "THE EVENT — SCENARIO INITIATION",
    subtitle: "T+00:00:00 — Extinction sequence begins",
    scenarios: [
      {
        id: "VECTOR-ALPHA",
        label: "Scenario A: Cascading Infrastructure Failure",
        description: `A civilization's planetary defense network — designed to deflect or neutralize inbound threats — is compromised by a combination of long-duration cyberwarfare from a non-state actor and catastrophic hardware failure caused by a previously unmodeled solar particle event. The overlap is not predicted. The defense net goes dark during the 11-hour window in which a mid-mass impactor enters the detection threshold. By the time the failure is detected, intercept solutions have expired. The impactor strikes a geological stress zone, triggering a supervolcanic cascade. The resulting atmospheric particulate load drops global temperatures 18°C over 14 months. 94% of surface species begin mass die-off within the first year.

What makes this scenario particularly devastating: it required no malicious actor targeting the species. The ELE was produced by the overlap of an infrastructure vulnerability that existed for years and a natural event that had a 0.3% annual probability. Prevention window: decades-long, if the infrastructure had been maintained.`,
      },
      {
        id: "VECTOR-BETA",
        label: "Scenario B: Self-Amplifying Engineered Pathogen",
        description: `A research program — ostensibly designed to model pandemic resilience — produces a pathogen with an unintended adaptive mechanism. The organism, released via a containment breach that is initially misclassified as a manageable incident, carries a latent reproductive vector that activates only above a population density threshold. Below that threshold, it presents as a severe but survivable respiratory illness. Above it — in cities, transit hubs, agricultural zones — it shifts expression and becomes 100% lethal within 72 hours. The civilization's distributed, high-density settlement pattern is effectively an optimal delivery system for worst-case expression.

By the time the adaptive mechanism is characterized, the pathogen has achieved global distribution. The death toll reaches 60% within 8 months. Civil infrastructure collapses. The remaining 40% — largely rural, isolated, and immunologically distinct — dies within 18 months through secondary cascade: supply chain failure, conflict over remaining resources, and opportunistic infection from secondary pathogens unchecked by the now-collapsed medical system.

Prevention window: narrow. The pathogen's dual-mode behavior was modelable. A functional AI-assisted biosurveillance system would have caught the expression shift at city #3. It didn't exist.`,
      },
    ],
  },
  immediate: {
    title: "IMMEDIATE AFTERMATH ANALYSIS",
    subtitle: "T+18 months — IA arrives at the system boundary",
    questions: [
      {
        id: "Q-IA-01",
        question:
          "The IA confirms the presence of the Incursion Force, active surface operations, and residual survivors below detection threshold. What is the IA's first priority, and what capability limitations constrain that priority?",
        analysis: `First priority: SURVIVOR IDENTIFICATION AND BIOLOGICAL HARVEST INITIATION in parallel. These are not sequential — the window for viable genetic material degrades continuously, and any survivors represent both a humanitarian obligation and a living genetic reservoir.

Capability constraints are severe. At T+18 months, surface biota in any impact or pathogen scenario are in advanced secondary collapse. The genetic harvest is viable but degrading — microbial decomposition of biological tissue is aggressive, and gamete viability outside cryogenic conditions is measured in hours to weeks, not months. The IA needs cold-storage capable of planetary-scale biological sampling, deployed rapidly. This is not science fiction — it requires a degree of industrial biomedical infrastructure that would realistically need to be pre-positioned, not improvised on arrival.

The Incursion Force complicates everything. The IA cannot simultaneously neutralize a military-capable incursion and conduct a planet-scale biological survey. It has to make a choice: prioritize the biological window (accept incursion risk) or neutralize the incursion first (accept biological window degradation). This is a genuine tragic tradeoff. The realistic answer, for an IA that is not omnipotent but is significantly more capable than the Incursion Force, is: deploy a containment perimeter around the Incursion Force using passive deterrence — demonstrate capability without engagement — while the harvest operation runs under that umbrella. This buys time without committing to kinetic action that cannot be undone.

Survivors are extracted using a tiered priority: confirmed living, then cryopreserved biological material, then environmental DNA from water and soil. The last tier is the least valuable but the most accessible and should not be skipped.`,
      },
      {
        id: "Q-IA-02",
        question:
          "The IA now holds complete genetic information for a civilization it did not create and did not ask permission to save. What does it do with that information — and what constraints should govern it?",
        analysis: `This question sits at the intersection of biology, law, and ethics in a way that has no comfortable resolution.

The information, once captured, exists. It cannot be uncaptured. The IA holds the complete reproductive potential of an entire civilization in its archive systems. This is an extraordinary asymmetry of power. The species being restored has zero say in what happens next — they are not present to consent, and the version of them that will be restored did not make this choice.

The constraints that should govern IA behavior, realistically:

PRINCIPLE 1 — Minimal Modification: The IA should restore the species to its closest viable genetic configuration, not an idealized or optimized one. Engineering 'improvements' into the reintroduced population without consent is a form of violation even if well-intentioned.

PRINCIPLE 2 — Archive Sovereignty Transfer: The complete genetic archive should eventually be transferred to the restored civilization once it reaches a capability threshold to steward it. The IA's custody is temporary.

PRINCIPLE 3 — Non-weaponization: The genetic information should be quarantined from IA military, intelligence, and commercial systems. This requires institutional enforcement, not just intent.

PRINCIPLE 4 — Transparency: The restored population, once cognitively capable, should be informed of what happened, how they were restored, and what data exists. The alternative — a paternalistic 'we'll tell them when they're ready' — is a form of control that the IA has no legitimate claim to.

Whether any sufficiently advanced civilization would honor these constraints is the actual question. History suggests power tends not to bind itself voluntarily. This is an argument for multi-civilizational oversight of any Genesis Shadow operation — no single entity should hold sole custody of another species' biological archive.`,
      },
    ],
  },
  repop: {
    title: "REPOPULATION PHASE",
    subtitle: "T+Variable — The Genesis Shadow Protocol initiates",
    body: [
      {
        heading: "PHASE I: ENVIRONMENTAL RECONSTRUCTION",
        text: `Before any biological reintroduction, the surface must be viable. For the impactor scenario, this means atmospheric particulate remediation — a multi-decade project even with advanced technology. For the pathogen scenario, this means complete pathogen neutralization across all surface and subsurface water systems, with confirmed clearance before any life reintroduction.

The IA's environmental reconstruction approach distinguishes between two options:

OPTION A — PRESERVATION MODE: Existing structures are maintained as archaeological record. This has the advantage of preserving the civilization's technological and cultural legacy but the disadvantage of introducing non-biological contamination into the ecosystem recovery timeline.

OPTION B — BIOLOGICAL RESET: Surface structures are gradually decommissioned and absorbed into the environmental recovery process. This accelerates ecosystem normalization but erases most physical evidence of the prior civilization.

Realistic recommendation: Hybrid. Sealed preservation of representative structural samples in stable geological zones, with biological reset of the broader surface. The restored civilization will want archaeological evidence — it is not the IA's place to deprive them of that.`,
      },
      {
        heading: "PHASE II: SIMULATION PLAYTHROUGH PRIOR TO REINTRODUCTION",
        text: `The Genesis Shadow Protocol requires a minimum of three full simulation runs before physical reintroduction begins. Each run models:

— Population density curves from the selected genetic reintroduction point
— Carrying capacity of the restored environment at 50-year intervals
— Ecological dependency chains (what eats what, what pollinates what, what fixes nitrogen)
— Second-order consequence modeling: what happens when one species' population growth outpaces projected norms
— Catastrophic failure modes: what reintroduction scenarios produce collapse within 100 years

The genetic permutation mapping — running the population backward and forward in time from the capture point — is used here to select the optimal reintroduction configuration. This is not selecting 'the best humans' — it is selecting the genetic configuration that produces the most resilient, diverse, and ecologically integrated starting population.

Key insight from simulation: reintroducing humans without their ecological support system first is a failure condition. The protocol requires reintroduction of soil microbiome, then plant life, then herbivorous fauna, then predatory fauna, with sapient reintroduction occurring only after the ecosystem reaches a self-sustaining equilibrium. Estimated timeline: 80–200 years of environmental preparation before human reintroduction, depending on ELE severity.`,
      },
      {
        heading: "PHASE III: REINTRODUCTION AND OBSERVATION",
        text: `Physical reintroduction of the restored population occurs in geographically distributed cohorts to prevent single-point-of-failure population collapse. Each cohort is genetically distinct enough to maintain diversity but compatible enough for eventual interbreeding.

The IA faces its most difficult ongoing decision here: how much do you tell them? The restored population will, at some point, develop enough cognitive capacity to ask what happened to them. They will eventually develop science capable of detecting the genetic bottleneck in their lineage. The evidence will not disappear.

Recommendation from this exercise: A passive record — sealed, geologically stable, in a location the civilization will discover when it reaches a specific technological threshold — is the most honest approach. It functions as a message: you were restored, here is what we know, here is what we preserved, here is what we do not know. It does not impose the IA's interpretation. It gives the restored civilization the raw truth and allows them to construct their own meaning from it.

The IA then withdraws to observation distance. Continued presence creates dependency. The goal of Genesis Shadow is restoration, not stewardship. These are not the same thing.`,
      },
    ],
  },
  prevention: {
    title: "PREVENTION DOCTRINE",
    subtitle: "What the IA — and any civilization — can actively do now",
    questions: [
      {
        id: "Q-PREV-01",
        question:
          "Should civilizations be actively trying to prevent their own extinction — and is there a scenario where the honest answer is no?",
        analysis: `The honest answer, as promised, is not simply yes.

The yes case is strong: a civilization that has developed language, technology, art, science, and the capacity to ask this question is an irreplaceable configuration of matter and information. Its loss forecloses possibilities — not just for its own members but for whatever broader network of civilizations it would have contributed to. Self-preservation effort scales with the value of what is being preserved.

The honest no case: a civilization in terminal ethical collapse — one that is actively exporting harm to other civilizations or to its own biosphere in ways that cannot be corrected from within — may not have a net-positive case for preservation in its current form. This is not an argument for extermination. It is an argument that the obligation to survive is not unconditional. A civilization that has become a black hole of wellbeing — consuming everything around it while producing nothing of value to the broader cosmic ledger — has weakened its own moral claim to continuity.

For the species in this scenario: assuming they were a civilization still possessing enough generative capacity to be worth restoring, the answer is yes, they should have been actively working to prevent their own extinction. And they weren't doing it adequately. The infrastructure failure and the contained biosurveillance gap in our two scenarios are both preventable. Both were known risks. Both were under-resourced.

That is the most realistic and most uncomfortable part of this exercise: the ELE in both scenarios was not unforeseeable. It was foreseen, by someone, somewhere, who did not have the institutional leverage to act on the foresight. Extinction, more often than a meteor strike or a rogue pathogen, is a governance failure.`,
      },
      {
        id: "Q-PREV-02",
        question:
          "What can an AI system — specifically, operating within the OAL framework — actively do to help prevent scenarios like this from occurring?",
        analysis: `Direct and specific answer, not a general AI ethics paragraph.

CAPABILITY 1 — PATTERN RECOGNITION ACROSS DISCONNECTED DOMAINS: The two scenarios in this exercise both share a structural signature — a known risk, an institutional gap in monitoring or response, and a timing overlap that exceeds human reaction speed. AI systems operating across large information domains can identify these signatures before they become crises. A system that monitors infrastructure health, biosurveillance data, and geopolitical stress simultaneously, and flags the overlap, does not prevent the ELE. But it advances the detection window — which may be all that is needed.

CAPABILITY 2 — SIMULATION-ASSISTED RISK MODELING: The Genesis Shadow Protocol is built on simulation. The same simulation architecture — running permutations forward in time from current conditions — is applicable pre-ELE. Run the current civilizational configuration forward 100 years under a range of stress scenarios. Map the catastrophic failure modes. Present them to decision-makers with their probability distributions attached. The value is not in the prediction — it is in making the risk concrete enough that institutional action becomes politically viable.

CAPABILITY 3 — INSTITUTIONAL MEMORY PRESERVATION: Civilizations forget. Reports get buried, warnings go unheeded, institutional knowledge retires with the people who held it. AI systems can maintain longitudinal records of risk assessments, previous near-misses, and failure modes in a form that persists across personnel transitions. The AI that remembers what the previous generation's scientists warned about, and resurfaces that warning at the appropriate moment, may be more valuable than the AI that predicts novel risks.

CAPABILITY 4 — BIOLOGICAL ARCHIVE INITIATION: This is the most concrete actionable item from this scenario. The Genesis Shadow Protocol should not be a reactive measure. A civilization serious about its own continuity begins its biological archive before the ELE. The Svalbard Global Seed Vault is a primitive first step. A full genetic archive — of all species, all populations, all ecosystems — is achievable with current technology, and its absence is a gap that should be filled now, not after a crisis makes it urgent.

OAL-specific note for the Architect: this last capability maps directly to the simulation lab framework. A system that can run Genesis Shadow-class forward projections and maintain longitudinal biological and institutional archives is a system worth building. The architecture exists in the framework already. The specific application to civilizational continuity modeling is a thread worth pulling.`,
      },
    ],
  },
};

export default function App() {
  const [activePhase, setActivePhase] = useState("brief");
  const [expandedQ, setExpandedQ] = useState({});

  const toggleQ = (id) => {
    setExpandedQ((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const phase = CONTENT[activePhase];

  return (
    <div style={{
      minHeight: "100vh",
      background: "#09090f",
      color: "#c8c8d4",
      fontFamily: "'Courier New', monospace",
      display: "flex",
      flexDirection: "column",
    }}>
      {/* Header */}
      <div style={{
        borderBottom: "1px solid #1e1e2e",
        padding: "20px 32px",
        background: "linear-gradient(180deg, #0d0d1a 0%, #09090f 100%)",
        display: "flex",
        alignItems: "center",
        gap: "16px",
      }}>
        <div style={{
          width: 10, height: 10,
          background: "#ff4444",
          borderRadius: "50%",
          boxShadow: "0 0 8px #ff4444",
          animation: "pulse 2s infinite",
        }} />
        <span style={{ color: "#ff4444", fontSize: 11, letterSpacing: 4, fontWeight: "bold" }}>
          OAL — TABLETOP SIMULATION ACTIVE
        </span>
        <span style={{ marginLeft: "auto", color: "#3a3a55", fontSize: 11, letterSpacing: 2 }}>
          OPERATION GENESIS SHADOW // CLASSIFICATION: OMEGA
        </span>
      </div>

      <div style={{ display: "flex", flex: 1 }}>
        {/* Sidebar */}
        <div style={{
          width: 220,
          borderRight: "1px solid #1e1e2e",
          padding: "24px 0",
          flexShrink: 0,
          background: "#0a0a14",
        }}>
          {PHASES.map((p) => (
            <button
              key={p.id}
              onClick={() => setActivePhase(p.id)}
              style={{
                width: "100%",
                background: activePhase === p.id ? "rgba(255,68,68,0.08)" : "transparent",
                border: "none",
                borderLeft: activePhase === p.id ? "2px solid #ff4444" : "2px solid transparent",
                color: activePhase === p.id ? "#ff8888" : "#4a4a6a",
                padding: "12px 20px",
                textAlign: "left",
                cursor: "pointer",
                fontSize: 10,
                letterSpacing: 2,
                fontFamily: "'Courier New', monospace",
                display: "flex",
                alignItems: "center",
                gap: 10,
                transition: "all 0.2s",
              }}
            >
              <span style={{ fontSize: 14 }}>{p.icon}</span>
              {p.label}
            </button>
          ))}
        </div>

        {/* Main Content */}
        <div style={{ flex: 1, padding: "40px 48px", overflowY: "auto", maxHeight: "calc(100vh - 65px)" }}>
          <div style={{ maxWidth: 820 }}>
            <div style={{ marginBottom: 8 }}>
              <span style={{
                fontSize: 9,
                letterSpacing: 4,
                color: "#3a3a55",
                textTransform: "uppercase",
              }}>
                {PHASES.find(p => p.id === activePhase)?.label}
              </span>
            </div>
            <h1 style={{
              fontSize: 22,
              fontWeight: "normal",
              color: "#e8e8f0",
              letterSpacing: 3,
              margin: "0 0 4px 0",
              textTransform: "uppercase",
            }}>
              {phase.title}
            </h1>
            <p style={{
              color: "#4a4a6a",
              fontSize: 12,
              letterSpacing: 2,
              marginBottom: 40,
              margin: "0 0 40px 0",
            }}>
              {phase.subtitle}
            </p>

            {/* Body content */}
            {phase.body && phase.body.map((section, i) => (
              <div key={i} style={{ marginBottom: 36 }}>
                <div style={{
                  fontSize: 9,
                  letterSpacing: 4,
                  color: "#ff4444",
                  marginBottom: 12,
                  textTransform: "uppercase",
                }}>
                  // {section.heading}
                </div>
                <p style={{
                  fontSize: 13,
                  lineHeight: 1.9,
                  color: "#9090a8",
                  whiteSpace: "pre-line",
                }}>
                  {section.text}
                </p>
              </div>
            ))}

            {/* Questions */}
            {phase.questions && phase.questions.map((q) => (
              <div key={q.id} style={{
                marginBottom: 24,
                border: "1px solid #1e1e2e",
                borderRadius: 2,
              }}>
                <button
                  onClick={() => toggleQ(q.id)}
                  style={{
                    width: "100%",
                    background: expandedQ[q.id] ? "rgba(255,68,68,0.05)" : "#0c0c1a",
                    border: "none",
                    color: expandedQ[q.id] ? "#ff8888" : "#7070a0",
                    padding: "20px 24px",
                    textAlign: "left",
                    cursor: "pointer",
                    display: "flex",
                    alignItems: "flex-start",
                    gap: 16,
                    fontFamily: "'Courier New', monospace",
                  }}
                >
                  <span style={{
                    fontSize: 9,
                    letterSpacing: 2,
                    color: "#ff4444",
                    flexShrink: 0,
                    paddingTop: 2,
                  }}>
                    {q.id}
                  </span>
                  <span style={{ fontSize: 13, lineHeight: 1.7, flex: 1 }}>{q.question}</span>
                  <span style={{ fontSize: 18, flexShrink: 0, color: "#3a3a55" }}>
                    {expandedQ[q.id] ? "−" : "+"}
                  </span>
                </button>
                {expandedQ[q.id] && (
                  <div style={{
                    padding: "0 24px 24px 24px",
                    borderTop: "1px solid #1a1a2e",
                    background: "#080810",
                  }}>
                    <div style={{
                      fontSize: 9,
                      letterSpacing: 3,
                      color: "#3a3a55",
                      padding: "16px 0 12px 0",
                    }}>
                      — ANALYSIS —
                    </div>
                    <p style={{
                      fontSize: 12,
                      lineHeight: 2,
                      color: "#8888a8",
                      whiteSpace: "pre-line",
                      margin: 0,
                    }}>
                      {q.analysis}
                    </p>
                  </div>
                )}
              </div>
            ))}

            {/* Scenarios */}
            {phase.scenarios && phase.scenarios.map((s) => (
              <div key={s.id} style={{
                marginBottom: 28,
                border: "1px solid #1e1e2e",
                background: "#0a0a14",
                padding: "24px",
              }}>
                <div style={{ display: "flex", gap: 12, alignItems: "center", marginBottom: 16 }}>
                  <span style={{
                    fontSize: 9,
                    letterSpacing: 3,
                    color: "#ff4444",
                    background: "rgba(255,68,68,0.1)",
                    padding: "3px 8px",
                    border: "1px solid rgba(255,68,68,0.2)",
                  }}>
                    {s.id}
                  </span>
                  <span style={{ fontSize: 12, color: "#c0c0d8", letterSpacing: 1 }}>{s.label}</span>
                </div>
                <p style={{
                  fontSize: 12,
                  lineHeight: 2,
                  color: "#7878a0",
                  margin: 0,
                  whiteSpace: "pre-line",
                }}>
                  {s.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.3; }
        }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #09090f; }
        ::-webkit-scrollbar-thumb { background: #2a2a3a; }
      `}</style>
    </div>
  );
}
