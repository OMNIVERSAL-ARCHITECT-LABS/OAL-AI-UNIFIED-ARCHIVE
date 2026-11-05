# Network Defense Intelligence Exercise
## Independent Research Prompt v1.1 (Perplexity)
Document ID: NDIE-RESEARCH-PROMPT-PERPLEXITY-001
Version: 1.1 | Supersedes: v1.0 (retained unchanged) | Date: November 4, 2026
Prepared by: Perplexity | Requested by: Nathan Lewis
Status: Draft for cross-AI review. Research not executed. No canon ratification, ONESTAMP, deployment, testing, purchase, or repository write is implied.

## 0. Change log from v1.0 to v1.1
Basis: review of the Claude, Gemini, Copilot, and two unattributed directive prompts (OAL-RESEARCH-PROMPT-NDIE-001 and OAL-RESEARCH-NDIE-001) supplied by Nathan. Authorship of the two unattributed files was not verifiable.
ADDED
- Shared A-E evidence grades and a claim ledger (Section 5), adapted from Claude's proposal, so reports are comparable.
- R / C / N tags (real-world feasibility / canon realism / narrative design) on every finding (Section 5).
- A capability decomposition matrix with a fixed status vocabulary (Section 6), adapted from Copilot.
- Hypotheses and disproof conditions written before searching, plus a pre-mortem (Section 5).
- Adversary-generation progression, defender-adaptation risk, a failure laboratory, a safety case, and a recurring "missing threat" question (Sections 7, 8, 10, 13).
- Decision gates G0-G4 and minimum floors for precedents, negative studies, failure modes, and experiments (Sections 9, 10, 15), adapted from the unattributed directive.
- Common cost tiers for all AIs (Section 11) and a coverage map from Nathan's ten questions to report sections (Section 16).
- A canon-translation track so findings also support Story Bible development without contaminating the engineering evidence (Section 14).
- Named verification leads for national exercises, incidents, and frameworks (Section 8). These are leads, not findings.
- Report-format rules for phone-readable single-column reading (Section 17).
CHANGED
- Cost and funding tiers are standardized; the national-scale tier is always flagged separately.
- Bypass analysis now includes an explicit ranked top-five and a statement of which bypasses make "real infrastructure fully secured" untenable.
- Priority tiers added so bypass, evolution, precedent, and cost work receive full depth first.
REJECTED (with reasons)
- Seeded cost figures, capture percentages, or performance-degradation numbers from any peer prompt: unverified, and they would anchor independent estimates.
- Fixed bandwidth quotas for disconfirming evidence (for example 40 percent) and mandates to prove the design "would fail": these replace one bias with another. Symmetric searching with null results reported is retained.
- Role-play personas (for example principal architect or red-team lead): a persona can steer findings.
- Presenting peer-proposed fixes (split-plane migration, a sacrificial ingress window, a tethered black-box transfer) as required amendments. They are hypotheses to test, not decisions.
- Operationally specific bypass detail (numeric probing scenarios, malware self-checks). All bypass work stays at the threat-model level.
UNCHANGED
- Canon/engineering separation, document audit, falsifiable central question, observable definition of capture, three seconds as a test variable, verified funding status, governance boundaries, and the staged execution sequence.

## 1. Assignment and decision to support
Conduct an independent, evidence-led investigation of the Network Defense Intelligence Exercise in OAL-DOSSIER-CANON-002 v1.0.0 (PDF and DOCX). Determine whether a bounded real-world defensive research program is worthwhile, under what conditions, at what cost, with what safeguards, and what must change in the design and canon first. Do not assume the national scale, three-second cycle, silent migration, or universal capture is achievable or desirable.
Central research question: Can authorized, selectively deployed deception and adaptive isolation measurably reduce the probability or impact of compromise of real assets, relative to credible alternatives, against adversaries who may avoid the deception altogether?
Produce a decision-ready assessment, not an endorsement, scene, marketing proposal, or implementation tutorial. Findings of insufficient evidence, narrowing, redesign, or cancellation are acceptable. Distinguish the value of investigating a question from the value of building or deploying a system.

## 2. Priority tiers
Tier 1 (full depth first): bypass of the whole process; evolution over time; precedents and what worked or failed; cost and funding; changes required before proceeding.
Tier 2: purpose and counterfactual; feasibility decomposition; experimental design; governance and safety.
Tier 3 (concise): canon translation; repository organization.
If effort is limited, state what was cut. Do not cut disconfirming evidence from Tier 1.

## 3. Source dossier and scope discipline
Read both documents. Test, rather than assume, that they are equivalent exports; do not count them as independent corroboration. Cite section and page.
Treat narrative canon as a creative constraint inside the fiction only. In the real-world track every technical assertion is contestable. Separate: demonstrated capability; plausible but unvalidated research; speculative fiction. Keep Time Wars, First Memory, purpose-reading, and temporal containment outside the engineering evidence unless in the canon-translation track.
Do not revise canon or apply ONESTAMP. Propose changes through a change-request register. The dossier's reported agreement among five AIs is a reported synthesis, not experimental validation. If underlying submissions are unavailable, say their independence cannot be verified.

## 4. Document audit (do before external research)
Classify each major assertion as source claim, narrative requirement, engineering hypothesis, measurable requirement, assumption, contradiction, or unsupported conclusion. Investigate, do not smooth over:
- The approval notice says nothing is ratified until ONESTAMP, while later sections call elements locked.
- Five AIs reviewed, a wider distribution list includes Claude, and roles are proposed for six; separate reviewers, recipients, and participants.
- The asset taxonomy is called five-tier but examples use Tier 0 and Tier 5, and critical assets are labeled both Tier 0 and Tier 1.
- Section 4.4 points to Q17 for the transfer package, though Q14 covers transfer and Q17 covers failure modes.
- The roadmap cites five goes-wrong scenarios; Section 9.4 labels four (A-D), distinct from five failure modes in 9.3.
- Consensus on timeline placement is overstated relative to the placement table.
- A disappearing line, session termination, workload containment, endpoint identification, and apprehension of a person are different things.
- The sequence neutralizes access to real assets before building and migrating into the honeypot. Establish what the deception adds if protection already succeeded, and what exposure exists during the handoff.
- The Architect holds sole visibility and decision authority while collaborators have partial views; the data flow is undefined.
For each: severity, research consequence, proposed correction, decision owner, whether it blocks work.

## 5. Evidence method, grading, and bias controls
Before searching, write your hypotheses and what would disprove each. Search symmetrically for support, contradiction, null, failed, abandoned, and inconclusive results. Use queries such as limitations, detection or fingerprinting of the technique, escape, overhead, deployment failure, postmortem, criticism, and cost-effectiveness. Steelman the opposing view before each major conclusion. Run a pre-mortem: assume the program failed badly in three years and list the most likely reasons.
Source priority: government and standards documents, national-laboratory and peer-reviewed work, official evaluations and postmortems, and primary program records. Vendor claims are claims needing corroboration. Record preprint versus peer-reviewed status.
Shared evidence grades (use exactly):
- A: primary and verifiable source.
- B: credible secondary source or several independent sources agree.
- C: single source, vendor claim, or commentary.
- D: researcher inference, labeled and derived from A-C evidence.
- E: speculation, used only to frame questions.
Every finding carries a tag: R (real-world feasibility), C (canon realism), N (narrative design), plus a grade and a confidence level (high, moderate, low).
Claim ledger fields: claim ID; claim; tag; grade; source ID; exact location; limitation; independence from other sources; counterevidence ID.
Source ledger fields: source ID; title; publisher or author; date; URL or persistent identifier; access date; source type; study setting; sample size; funding or conflicts disclosed; data or code availability.
Never invent quotations, identifiers, studies, award amounts, or results. Report null searches with what was searched. State "insufficient evidence to establish this capability at the proposed scale" when appropriate. Record search terms, databases, cutoff, exclusions, access limits, and gaps. If search tools are unavailable, mark the task unexecuted rather than supply remembered findings as verified.
Independence: complete the first-pass analysis before reading peer outputs; log which peer materials were visible. Agreement among AIs reflects shared training and sources, not replication. No AI speaks for another.

## 6. Feasibility decomposition
Evaluate the chain separately: observe; classify; map reachable attack paths; prevent access to real assets; select response; instantiate decoys; redirect eligible sessions; monitor; isolate; recover; transfer a deployable artifact.
Capability decomposition matrix: for each step record required privileges, ownership, instrumentation, latency, scale, trust assumptions, failure behavior, and validation evidence, and classify as: Demonstrated; Demonstrated at smaller scale; Partially demonstrated; Research-stage; Speculative; Unsupported. State whether the complete combination has ever been demonstrated or is an aggregate of separately demonstrated parts.
Assess stateful session redirection, authenticated and encrypted protocols, pre-existing compromise, identity continuity, and external dependencies. Distinguish routing a new connection from transparently moving an established authenticated session. Do not assume national visibility or authority to redirect third-party traffic.
Compare full duplication, selective emulation, pre-provisioned decoys, procedural generation, digital twins, and replay. Examine limits of synthetic fidelity: what independent ground truth an adversary can reach (time sources, certificates, counterparties, physical processes), and whether excessive realism itself creates risk.
Three seconds is a candidate parameter, not a proven optimum. Define what rotates (address, route, identity, key, service state, decoy content, presentation), what cannot safely rotate that fast, session and synchronization costs, observability and forensic effects, and whether the periodicity becomes a detectable signature. Compare fixed, randomized, event-driven, slower, and no-rotation policies, and look for regimes where rotation worsens outcomes.
Evaluate whether AI is necessary versus deterministic orchestration, statistical detection, or human authorization. Examine false positives, injection through attacker-controlled telemetry, poisoning, drift, and compromise of orchestration. Test the "quantum-inspired" analysis claim: does it add anything concrete?
Define capture as separate measurable states: activity diverted; session contained; behavior recorded; infrastructure identified; campaign characterized; real assets isolated. Connection captured is not attacker identified, attributed, or eliminated. Replace visual disappearance with auditable states: suspected; observed; diverted; isolation verified; visibility lost; resolved; unknown.
Name the smallest realistic version (enclave, sector, or region) and the largest defensible claim.

## 7. Bypass analysis: reaching real assets without engaging the process
Assume an attacker values the real asset, not winning inside the decoy. Build defensive attack trees for confidentiality, integrity, availability, and physical safety, with actors including patient states, insiders, supply-chain adversaries, opportunists, automated or AI agents, and multiple concurrent campaigns.
Cover at least:
- Unmonitored ingress, unmanaged devices, forgotten services, alternate connectivity, third-party and managed-service access, and assets outside the administrative boundary.
- Abuse of valid accounts, sessions, delegated access, trusted administrators, identity providers, and control planes.
- Compromise present before activation; update channels and upstream software, including this system's own transfer and update path; firmware and management infrastructure; backup and recovery.
- Direct access to real data through legitimate workflows, SaaS integrations, contractors, or compromised human processes.
- Physical, wireless, maintenance, and operational-technology paths that never cross the deception layer; air-gapped, legacy, foreign-hosted, and enclave systems.
- Attacks on the defender: sensors, policy engine, virtualization, orchestration, logging, the human operator, forced disclosure.
- Resource exhaustion, distraction, concurrent attacks, misleading telemetry, and damage before useful engagement.
- Patience and dormancy beyond any rotation interval; avoidance of instrumented assets; abandoning one session and re-entering by another path; learning without touching the same surface twice.
- Non-network strategies: influence, legal, financial, physical, and personnel pressure; seams between jurisdictions, agencies, and private owners.
- Exploiting the defender's own capture logs, attribution outputs, and transfer package.
- Misclassification of innocent users and attackers blending into legitimate activity.
For each: violated assumption, assets at risk, broad feasibility conditions, observable warnings, defensive control, safe laboratory test, residual risk, and grade. Rank by likelihood, impact, and detectability with reasoning; name the top five; state which bypasses make "real infrastructure fully secured" untenable. Distinguish bypass from decoy recognition, containment escape, and ordinary detector failure.
Guardrail: threat-model level only. No exploit chains, payloads, evasion recipes, real-target reconnaissance, credential abuse instructions, or unauthorized testing. Use abstract scenarios, synthetic identities, owned infrastructure, and written rules of engagement. The guardrail must not soften the assessment of architectural weaknesses.

## 8. Evolution over time and comparable work
Adversary generations: G0 unaware of the system; G1 knows deception is used; G2 understands broad characteristics; G3 tests whether the environment is genuine; G4 tries to cause defender misclassification; G5 assumes any observed environment may be deceptive. Model four horizons: hours to days; weeks to months; one to three years; five to ten years. Label best, expected, and worst trajectories as scenario analysis, not forecasts, with drivers and signposts.
Test whether value declines after disclosure or recognition; displacement to weaker assets; silent non-engagement; defender decay (upkeep, staleness, alert fatigue, staff turnover, doctrine leakage, proliferation of the package); and the cost-exchange ratio between attacker and defender. Defender adaptation can itself be a vulnerability: poisoned training data, false attribution, automation bias, feedback loops, overfitting to past attackers, and model homogenization. Captured behavior must not automatically alter trusted production policy without review. Define leading indicators, re-evaluation frequency, and triggers for redesign, reduced scope, or shutdown. State what remains beneficial if the attacker knows deception exists.
Comparable work to investigate: honeypots and honeynets, honeytokens, moving-target defense and address hopping, SDN-based deception, cyber ranges and digital twins, OT/ICS deception, adversary engagement and automated response. Verification leads (not findings): MITRE Engage, ATT&CK and D3FEND; NIST SP 800-160 Vol. 2, SP 800-53 and SP 800-207; DARPA cyber-defense and moving-target programs; Cyber Storm, GridEx, Locked Shields, Cyber Flag, Eligible Receiver 97; DARPA Cyber Grand Challenge; SolarWinds, Volt Typhoon, Salt Typhoon, Ukraine grid attacks, Stuxnet, Colonial Pipeline; early deception accounts such as The Cuckoo's Egg and Berferd; honeyfarm and honeypot-detection research; game-theoretic deception surveys; and non-cyber military deception.
For each selected precedent report objective, scale, environment, attacker model, design (tabletop, simulation, emulation, human study, competition, prototype, field deployment, incident), baseline, results, negative results, cost, limits, and what transfers or does not. Minimum floors: 8 relevant precedents and 3 contrary, negative, or inconclusive ones; do not pad. Distinguish announcements from demonstrated outcomes. Answer plainly: has this exact architecture been modeled or deployed, which components have, and which combination is unvalidated? If no exact precedent is found, state search scope and uncertainty.

## 9. Purpose, counterfactual, and decision gates
State the operational problem, protected mission, users, assets, and harm avoided. Distinguish detection, delay, observation, attribution support, containment, recovery, and deterrence. Clarify which goals conflict (speed versus depth of capture; secrecy versus transfer; deterrence versus concealment). Compare "exercise," live operation, demonstration, and proof of concept, and recommend a label. Explain why this should be done, why now, and why a simpler study would not answer the question.
Mandatory baseline comparison at equal budget: segmentation, zero trust, identity security, patching, endpoint monitoring, backups and recovery, conventional honeypots, static decoys, and improved incident response. State what happens if nothing is funded. Define a minimum useful research outcome and a minimum deployable capability.
Independent argument sequence before any funding case: (1) the strongest case that this should not be funded; (2) the strongest case that the problem is worth studying but this architecture is the wrong way; (3) only then the evidence-based case for a limited study, if supported.
Decision gates: G0 concept clarity (asset boundary, owner, purpose, threat model, metrics); G1 research justification (comparable evidence, incremental value, known bypasses; continue, narrow, or abandon); G2 safe prototype (approved sandbox, oversight, budget, test plan); G3 controlled pilot (replicated measured advantage, manageable collateral risk, rollback); G4 scale decision (independent review, legal authority, cost-benefit, sustained reliability). Production is never an automatic final step.

## 10. Experimental design and failure laboratory
Stages: evidence review; tabletop and threat model; isolated proof of concept; controlled cyber range; human red/blue experiment; adaptive-adversary experiment; limited opt-in pilot; independent scale review. Start with one bounded asset class under explicit control.
Floor of six experiments, each with null hypothesis, abstract topology, variables, controls, outputs, repetitions or power analysis, data stewardship, stopping conditions, bias risks, failure signatures, and acceptance and rejection criteria: (1) deception versus baseline controls; (2) bypass coverage for threats that never touch the decoy; (3) three-second rotation versus randomized, event-driven, slower, and static; (4) repeated-episode attacker learning with separated training and test cohorts; (5) false-positive and collateral capture and ordinary-user performance; (6) control-plane outage, telemetry failure, corrupted updates, rollback, and reconstruction. Optional: coordinated adversaries, model drift, simulation-to-reality limits.
Compare standard controls, static deception, adaptive deception without rapid cycling, and adaptive cycling. Use matched workloads, unseen scenarios, randomization where feasible, blinded adjudication where feasible, and independent ground truth. Report failed and inconclusive runs.
Primary outcomes: real-asset compromise and mission impact. Secondary: time to detection and isolation, engagement coverage, visibility gaps, false diversion of benign traffic, verified isolation failures, decoy-recognition rate, latency, availability, analyst workload, forensic usefulness, compute cost, cost per useful outcome. State denominators and windows. Identify metrics that could create false confidence; zero observed compromises is not zero residual risk.
Failure laboratory: deliberately construct failure conditions: incomplete visibility, stale telemetry, degraded sensors, resource exhaustion, adversarial deception, false positives, compromised trusted systems, internal misuse, benign actor mistaken for adversary, synthetic-environment detection, conflicting automation, defender-model poisoning, simultaneous unrelated incidents. List at least 12 failure modes with likelihood, consequence, detectability, evidence grade, and mitigation confidence, plus at least five stop-or-redesign triggers.
Safety case before any operational test: effects on real assets; prevention of test escape and accidental production routing; durable marking of synthetic data for authorized evaluators; egress controls; emergency termination and termination authority; evidence retention; audit responsibility; independent observer and safety authority able to halt the test.

## 11. Cost model (common tiers for all AIs)
Estimate only after scoping, bottom-up, dated, in stated-year USD. Common tiers: T1 desk study and tabletop (3-6 months); T2 isolated prototype or cyber-range proof of concept (6-12 months); T3 bounded organizational or sector pilot (12-24 months); T4 multi-organization research demonstration; T5 national-scale operation, always separate and marked speculative or non-estimable if inputs are missing (list the inputs).
For each tier: duration, roles and person-months, loaded rates and what they include, compute, storage and logging, network and egress, licenses, facilities and range access, OT hardware if used, integration, independent evaluation, legal and privacy review, training, contingency, indirect costs, recurring annual cost, and three-to-five-year total where meaningful. Show low, base, and high with arithmetic, assumption sources, exclusions, uncertainty, and sensitivity to fidelity, retention, staffing, asset count, concurrency, and rotation frequency. Distinguish planning estimates from quotes or awards. Estimate cost of the simpler baseline alternatives and break-even assumptions; do not treat avoided losses as guaranteed savings. Tie later-stage funds to evidence gates. Name the five largest cost drivers.

## 12. Funding pathways
Match pathways to maturity: university and national-laboratory partnerships; small-business programs; federal and state cybersecurity research; sector-specific critical-infrastructure research; industry sponsorship; philanthropy; in-kind range or cloud support; international programs. Named agencies and programs are leads, not presumed active.
For each verify at research time: sponsor and program, official source, current status (open call, recurring without open call, closed example, procurement, grant, cooperative agreement, informal partnership), applicant eligibility, entity and registration requirements, scope fit, published award range, period, deadlines, cost share, eligible costs, security and data conditions, IP and publication terms, conflicts of interest, and burden. Do not call historical funding available now. State whether an individual concept owner needs a university, company, or nonprofit lead. Recommend a staged first-dollar sequence tied to evidence gates and a neutral concept-note outline. Flag dual-use, export-control, and agenda-capture risks. In-universe funding (ONE Industries) is a separate canon question.

## 13. Governance, legal, safety, and human factors
Flag jurisdiction-specific issues for qualified counsel: written authorization, monitoring scope, interception and privacy, notice and consent, data minimization and retention, evidence handling, cross-border data, procurement, liability, intellectual property, export, critical-infrastructure obligations, entrapment questions, and attribution norms. Distinguish binding law, guidance, and project policy; separate passive observation, containment under authorized control, active interference, and retaliation. Exclude hack-back and changes to third-party systems absent separate lawful authority. Apply this to Q11. Assess dual-use risk of the technology as an unaccountable surveillance or control system, including misuse of the transfer artifact; define transfer, signing, keys, inspection, approval, revocation, and receiving-operator acceptance tests.
Assess the single-Architect dependency (control-plane compromise, coercion, fatigue, continuity), least privilege, separation of duties, emergency access, and independent oversight. Consider the tension between secrecy and deterrence. Include false accusation, alert fatigue, unequal impacts, and a path to report unexpected harm. Treat "Could you do this to an entire civilization?" as a real ethics question as well as a hook.
Missing-threat exercise: at the end ask what class of threat the team never modeled, from the perspectives of defenders, operators, legal and privacy reviewers, infrastructure owners, red teams, funders, and executives. Repeat it each research cycle.

## 14. Required changes, issues register, and canon translation
Produce a ranked change register: original wording and section, issue, evidence, proposed real-world replacement, canon impact, owner, dependency, disposition (keep, modify, drop, add). Evaluate, as hypotheses not decisions: bounded measured outcomes instead of universal capture; observable indicators instead of purpose-reading; scoped selective deception instead of complete national replication; a tested schedule instead of a fixed three-second rule; verified states instead of visual disappearance; and a signed, inspected, versioned, rollback-capable transfer with acceptance tests instead of an automatic reboot hand-off. Explain which are design corrections and which depend on later test results.
Issues register: new questions beyond Q1-Q20, refinements, objections, and assumptions, each with ID, statement, why it matters, severity, who answers, evidence. Red-team the dossier's own red-team section: what did the five AIs miss? Separate blockers of safe testing from refinements of cost or scope. Do not block desk research on narrative decisions; use labeled scenario assumptions.
Canon-translation track (separate, tagged C and N): which failure modes, goes-wrong scenarios, and Q1-Q20 priorities should change; what a credible, costly failure would reveal about the Architect; where the escalation from networks to organizations to timelines breaks (typically where an adversary has independent access to ground truth). Present all canon changes as change requests awaiting ONESTAMP.

## 15. Next actions and recommendations
Provide Now / Next / Later actions with owner role, effort, dependencies, evidence required, and completion criteria, and a conditional 30/60/90-day plan that is not a commitment. Include the strongest argument against funding, the strongest argument for a limited study, the most consequential unknown, the cheapest discriminating experiment, what would change the recommendation, and a readiness assessment for dossier v1.1.

## 16. Coverage map and final report structure
Map to Nathan's ten questions: goal and why it matters (Sections 9, 1); cost (11); funding pathways (12); what must be addressed, questions and concerns (4, 14); adversarial analysis and bypass (7); next steps (15); evolution over time (8); real-world occurrence and modeling (6, 8); what worked and what failed (8); what must change (14).
Final report order: (1) executive summary answering all ten questions; (2) method, search log summary, and limits; (3) document audit; (4) findings by section with tags, grades, and confidence; (5) bypass matrix and top five; (6) comparables table; (7) evolution analysis; (8) experiments and metrics; (9) cost workbook; (10) funding matrix; (11) governance and safety case; (12) issues register and change register; (13) dissent, uncertainty, and what would change conclusions; (14) next actions and gates; (15) appendices: claim ledger, source ledger, search log with disconfirming searches.

## 17. Deliverables, format, and repository
Deliver PDF and editable DOCX with matching substantive content, document ID, version, date, status, headings, page numbers, citations, and change history; verify both open. Provide a Markdown source and CSV exports of the claim ledger, cost workbook, and issues register where feasible. Label all estimates.
Format: single-column body readable on a phone; short paragraphs; tables, charts, and figures in appendices at the end; no raw markup showing.
Proposed (not created) folder network-defense-intelligence-exercise: README.md; 00-source-dossier; 01-research-prompts (iteration-1, iteration-2); 02-research-reports; 03-peer-reviews; 04-synthesis; 05-evidence (claims, sources); 06-threat-model; 07-experiments; 08-costs; 09-funding; 10-governance; 11-decisions; changelog. Preserve each AI's original prompt and first-pass report; store syntheses separately; keep fictional canon apart from empirical research. Use stable IDs for claims, risks, questions, experiments, sources, decisions, and changes. Do not publish credentials, real topology, personal data, confidential telemetry, or harmful operational artifacts. Define public/private split, license review, and release checks.

## 18. Execution sequence
Stage A: share this v1.1 and the other prompts. Do not execute research.
Stage B: peer prompt review with ADD / CHANGE / REMOVE decisions and reasons.
Stage C: Nathan decides which shared conventions the team standardizes (evidence grades, tags, cost tiers, format) and whether a common v2.0 core is used.
Stage D: execute only on Nathan's explicit instruction, independently, disclosing tools and limits.
Stage E: compare completed reports without majority-vote truth claims; resolve disputes by source verification or testable observation; preserve dissent.
End each stage with three questions for the Architect and three objections to the premise.

## Source basis
OAL-DOSSIER-CANON-002 v1.0.0 (PDF and DOCX); Nathan Lewis's request of November 4, 2026; and the peer research prompts supplied that day. No external research was executed in preparing this prompt, and none of the peer-proposed figures were adopted.
