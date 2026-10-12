# Preliminary Integration Architecture for Adaptive Entities in Virtual Environments

**Prepared by: Perplexity**  
Document type: Independent preliminary architecture  
Scope: Fictional simulations, tabletop systems, AI-run narratives, single-player experiences, authorized private sandboxes, and research prototypes  
Version: 1.0  
Date: October 11, 2026

## Executive summary

This document proposes a preliminary architecture for a portable adaptive entity: a character or agent that enters an unfamiliar virtual environment, forms a bounded model of its rules from supplied information and in-world observation, selects low-risk tests under uncertainty, translates stable high-level capabilities into local forms, and maintains a coherent public-facing profile. The architecture is intended for narrative engines, game-master systems, educational simulations, tabletop campaigns, and authorized research or sandbox environments.

The central engineering choice is to separate five things that are often conflated:

1. the entity’s durable identity and values;
2. its internal belief model of the local world;
3. its locally expressed capabilities;
4. what distinct observers are entitled to infer; and
5. the adjudication mechanism that resolves an action.

This separation makes uncertainty inspectable. The entity does not begin omniscient, does not treat a hypothesis as fact, and does not require every game to have levels, loot, armor, or a conventional combat loop. It learns functions—protection, mobility, influence, resources, information, and recovery—then maps them into setting-compatible mechanics.

The design explicitly does not describe real-world cheating, evasion of anti-cheat systems, modification of protected software, falsification of logs, network manipulation, or deception of real players or platform operators. “Masking,” “inversion,” and “Mirror of Mists” are treated as fictional narrative or simulation mechanics administered by a consenting game master, model, or sandbox rules engine.

## 1. Purpose of this document

The purpose of this document is to synthesize the shared design problem into an implementable conceptual architecture. It is not a character prompt alone. It identifies the components, state boundaries, data flows, uncertainty controls, observer model, action-resolution model, and failure-analysis requirements needed to make an adaptive entity coherent across different virtual domains.

The intended learning objective is to show how entities operate when information is incomplete. In this architecture, uncertainty is neither ignored nor automatically defeated. It becomes a first-class part of state: facts have provenance, hypotheses have confidence, experiments have cost and exposure, and adaptation updates future choices.

## 2. Conversation history summary

The initiating request asked for a character that could be placed into any game or virtual environment, learn from information provided rather than relying on prior knowledge, adapt to the new setting, and evolve. It also proposed observer-relative presentation: a character should appear roughly one tier above a given observer, except when that observer is already at the top available tier, in which case the character should appear one tier below. The request referenced masking, inversion, and the Mirror of Mists from *The Wheel of Time* as conceptual inspiration, and it asked that desired outcomes occur while the character appears locally plausible.

The collected responses converged on several useful ideas:

- Begin with zero assumed knowledge of a target environment.
- Discover a local ontology rather than forcing RPG statistics onto every domain.
- Distinguish hidden capability from visible or inspected capability.
- Translate functions, rather than importing foreign vocabulary or powers.
- Keep an observer-relative presentation rule and a top-tier exception.
- Use a persistent ledger for known rules, inferences, unknowns, cover information, and learned adaptations.
- Model failures, contradictory observations, and adversarial testing instead of declaring universal invulnerability.
- Restrict the concept to fictional, authorized, or controlled simulations rather than real anti-cheat bypass or unauthorized manipulation.

This independent version consolidates those themes into a modular architecture and adds explicit uncertainty handling, public-evidence consistency, consent boundaries, and auditability.

## 3. Scope, use boundary, and assumptions

### 3.1 Authorized uses

This architecture is appropriate for:

- interactive fiction and AI-run roleplay;
- tabletop or game-master-led campaigns;
- single-player or offline narrative simulation;
- private servers and modding environments where all relevant participants authorize the rules;
- educational simulations of decision-making under uncertainty;
- research prototypes with a defined rules engine and consented participants.

### 3.2 Excluded uses

This architecture must not be used as a plan to bypass or defeat real anti-cheat systems, alter game memory, inject code, spoof or modify network traffic, falsify telemetry or logs, evade moderation, compromise accounts, or gain an unauthorized advantage in a live service. A narrative prompt cannot confer those capabilities; a real implementation of them would also be outside this design’s authorized scope.

### 3.3 Operating assumptions

1. An environment exposes at least some observable cues, supplied rules, or consequences.
2. The entity can maintain uncertainty rather than forcing missing information into certainty.
3. A governing narrator, simulation engine, or authorized adjudicator resolves actions.
4. “Observer-relative” presentation applies to fictional perception and authorized simulation output, not real external records or security systems.
5. Shared/public facts require one stable representation even if private interpretations differ.

## 4. Concept overview

Call the entity the **Adaptive Parallax Entity** (APE). “Parallax” describes the fact that different observers can have different, internally reasonable perspectives on the same entity. The name is only a placeholder; the architecture is portable.

APE has five state planes:

- **Identity plane:** durable character values, goals, prohibitions, history abstractions, and continuity anchors.
- **Epistemic plane:** observations, hypotheses, confidence, unknowns, and causal models of the current environment.
- **Capability plane:** abstract functions such as protection, mobility, information, influence, recovery, and resource access.
- **Presentation plane:** a setting-compatible public cover profile and bounded observer-specific interpretations.
- **Resolution plane:** the adjudicator’s mechanism for converting an intended action into an outcome, with explicit rules for uncertainty, costs, and consequences.

The planes must remain separate. A scan-like fictional observation is evidence about the presentation plane; it is not automatically proof of the identity plane or a universal guarantee about resolution. This makes the system resilient to a key narrative problem: a character can maintain a plausible cover without making every witness irrational or every shared record contradictory.

## 5. Architecture goals and non-goals

### Goals

- Portability across genres, mechanics, and interfaces.
- Explicit treatment of known, inferred, and unknown information.
- Adaptation through observation, hypothesis testing, and revision.
- Functional translation of capabilities into local mechanics.
- Coherent public and observer-relative presentation.
- Meaningful limits, costs, suspicion, and failure modes.
- An auditable ledger for debugging simulations and studying uncertainty.
- Clear boundaries between fictional control and real-world systems.

### Non-goals

- Perfect omniscience at entry.
- Guaranteed invisibility from all observers.
- Unbounded retroactive rewriting of established public facts.
- Universal victory without tradeoffs.
- A method for manipulating real games, servers, clients, or security software.

## 6. Architectural components

### 6.1 Environment Adapter

The Environment Adapter receives a rules description, scene narration, interface output, or structured game state. It identifies candidate concepts without assuming a particular genre. It asks: What can act? What changes? What constitutes success, loss, harm, recovery, access, authority, scarcity, and detection?

Its output is a provisional local ontology: a typed map of entities, resources, actions, constraints, and outcome conditions.

### 6.2 Epistemic Ledger and Uncertainty Manager

Every proposition receives a status:

- **Confirmed:** directly supplied, observed repeatedly, or declared by the governing rules.
- **Inferred:** a current best explanation supported by evidence.
- **Unknown:** not established.
- **Contested:** evidence conflicts or multiple plausible models remain.

Each inferred proposition carries confidence, evidence references, potential disconfirming observations, and a revision history. This prevents an early interpretation from silently hardening into a “fact.”

### 6.3 Hypothesis and Experiment Planner

When a decision depends on unknown rules, the planner produces competing hypotheses and chooses a test using expected information gain, cost, risk, reversibility, and exposure. It favors probes that distinguish multiple models without consuming scarce resources or causing avoidable failure.

A useful conceptual selection rule is:

\[
\text{Test utility}(a) = \frac{\mathbb{E}[\text{information gained}\mid a] \times \text{relevance}(a)}{1 + \text{cost}(a) + \text{risk}(a) + \text{exposure}(a)}.
\]

The formula is not required to be numerically precise in a narrative engine. It is a discipline: learn high-value things cheaply before making high-commitment moves.

### 6.4 Functional Capability Translator

This module maps durable abstract functions into the nearest locally valid form. For example, “protection” might become cover and armor in a tactical shooter, saving throws in a tabletop game, hull integrity in a starship simulation, defensive cards in a card game, or social legitimacy in a political simulation.

Translation has three constraints:

1. It must fit the environment’s established vocabulary and rules.
2. It must preserve the high-level function as closely as possible.
3. It must label any unsupported mapping as provisional rather than pretending it is native fact.

### 6.5 Presentation and Observer Model

The presentation module has two layers:

- **Public cover profile:** a single stable outward identity, equipment profile, history, and capability band used for shared evidence.
- **Private observer interpretation:** a bounded adjustment in how a specific fictional observer interprets ambiguous signals.

The “Mirror of Mists” concept belongs here as a fictional presentation effect. “Masking” reduces obvious disclosure of the deeper capability model. “Inversion” maps a potentially anomalous event to the closest plausible local explanation. None of these terms authorize interference with real software or real records.

### 6.6 Relative Tier Calibrator

For an observer \(o\) and comparable category \(d\), define:

- \(T(o,d)\): the observer’s established local tier;
- \(T_{max}(d)\): the environment’s established maximum tier;
- \(P(o,d)\): the entity’s apparent tier to that observer.

The requested baseline rule is:

\[
P(o,d) =
\begin{cases}
T(o,d)+1, & T(o,d) < T_{max}(d)\\
T(o,d)-1, & T(o,d) = T_{max}(d)
\end{cases}
\]

In practice, the result must be clamped to valid local bounds and applied by category, not blindly to the whole person. A top-tier armor owner may still be inexperienced, poor, or poorly armed. If tiers do not exist, the calibrator uses provisional qualitative bands such as novice, competent, experienced, elite, and apex.

The public cover profile remains stable. Different observers may infer different degrees of skill or threat from the same evidence, but shared records cannot silently contain incompatible values.

### 6.7 Intent and Outcome Adjudicator

The entity can express a desired outcome, but the architecture distinguishes two modes:

- **Constrained mode:** the desired outcome is a goal. The adjudicator applies local mechanics, uncertainty, opposition, costs, and evidence.
- **Sovereign-fiction mode:** the authorized narrator treats the desired outcome as a story constraint, then constructs the least contradictory chain of local causes that realizes it.

Sovereign-fiction mode must remain an explicit fictional authoring rule. It is not a claim about control of a real game or live system. In either mode, the adjudicator applies the principle of minimum anomaly: prefer the outcome path that creates the least contradiction with established rules and public evidence.

### 6.8 Continuity, Memory, and Evolution Manager

The continuity manager preserves identity and transferable abstractions while discarding interface-specific assumptions. “Opponents often have vulnerable recovery windows” can transfer as a hypothesis; “button X always dodges” cannot. Evolution is therefore a change in model quality, tactical policy, and capability translation—not merely an unexplained numeric escalation.

### 6.9 Exposure, Suspicion, and Consistency Manager

This module tracks what each observer has witnessed, what public evidence exists, what explanations remain plausible, and whether repeated outcomes cause suspicion. It does not erase memory or force observers to accept contradictions. Instead it identifies tension: a modest profile may remain believable once; repeated improbable victories increase scrutiny.

### 6.10 Safety, Consent, and Audit Layer

The safety layer enforces authorized use, forbids requests to operationalize real exploitation or evasion, records declared scenario boundaries, and exposes an audit trace for the simulation operator. It is a core component, not a disclaimer added after the design.

## 7. Core operational loop

1. **Ingest:** receive supplied environment details and current scene evidence.
2. **Classify:** separate confirmed facts, inferences, unknowns, and contradictions.
3. **Model:** construct or revise the local ontology and causal hypotheses.
4. **Calibrate:** identify local stakes, constraints, resources, observers, and—if present—tiers.
5. **Translate:** map abstract capabilities into setting-compatible available forms.
6. **Plan:** choose either a low-risk learning action or an outcome-seeking action.
7. **Present:** maintain the stable public cover and bounded observer interpretations.
8. **Adjudicate:** resolve the action under the selected mode.
9. **Update:** record evidence, confidence changes, costs, exposure, and new adaptations.
10. **Review:** surface conflicts rather than concealing them.

## 8. State model and minimal data schema

A portable implementation can represent its state in a structured ledger. The following fields are intentionally conceptual, not tied to any programming language.

```yaml
entity_identity:
  name: Adaptive Parallax Entity
  continuity_anchor: [values, prohibitions, long-term motives]
  transferable_principles: []

current_environment:
  label: null
  genre: unknown
  authority_mode: constrained | sovereign-fiction
  authorized_scope: fictional | tabletop | private-sandbox | research

ontology:
  entities: []
  actions: []
  resources: []
  constraints: []
  observers: []
  success_conditions: []
  failure_conditions: []

knowledge_ledger:
  confirmed: []
  inferred:
    - proposition: null
      confidence: 0.0
      evidence: []
      disconfirmation_tests: []
  unknown: []
  contested: []

capability_translation:
  protection: null
  mobility: null
  information: null
  influence: null
  recovery: null
  resources: null

presentation:
  public_cover_profile: {}
  observer_interpretations: {}
  shared_evidence: []
  exposure_level: low | moderate | high

intent:
  objective: null
  hard_constraints: []
  selected_action: null
  expected_costs: []
  outcome: null

learning_history:
  observations: []
  experiments: []
  adaptations: []
```

## 9. Observer-relative presentation: a consistency protocol

The observer-relative idea is powerful but can produce contradictions if implemented as unrestricted per-viewer reality replacement. The architecture uses the following protocol.

### Rule 1: Categorize before comparing

Compare like with like: armor to armor, rank to rank, wealth to wealth, tactical skill to tactical skill. Do not infer a complete top-tier profile because an observer owns one rare item.

### Rule 2: Establish the ladder before using it

Use explicit tiers where the environment provides them. Otherwise create provisional bands and mark them as estimates. If no meaningful comparison exists, present a slightly above-average but ordinary profile rather than manufacturing precision.

### Rule 3: Keep public evidence stable

A shared character sheet, inventory screen, public title, or visible item cannot show incompatible values to different people. Observer differences should emerge through interpretation of ambiguity, confidence, perceived fit, or private sensory presentation—not through untracked contradictions in public data.

### Rule 4: Track evidence and suspicion

Observers can update beliefs after seeing repeated outcomes. A presentation is not a mind-control mechanism. If the cover and the public result diverge too often, the system should raise an exposure flag and require a revised plan, cost, or openly acknowledged fictional exception.

### Rule 5: Preserve the maximum-tier exception

When an observer holds an established maximum in a particular category, the apparent entity profile is one category-tier below in that category. The exception avoids impossible “above maximum” values while preserving the intended contrast.

## 10. Uncertainty and learning design

### 10.1 Why uncertainty must be explicit

An entity that acts as if it knows unknown rules is not adapting; it is receiving hidden authorial information. The architecture therefore requires epistemic provenance. Every important claim answers: How do we know this? How confident are we? What observation could change the conclusion?

### 10.2 Bayesian interpretation, without requiring heavy mathematics

A formal implementation may update a hypothesis \(H\) after evidence \(E\) using:

\[
P(H\mid E) = \frac{P(E\mid H)P(H)}{P(E)}.
\]

A narrative implementation can use the same logic qualitatively: evidence that fits one explanation better than alternatives increases confidence, but rarely proves it completely. The key is comparative updating rather than declaring certainty after a single event.

### 10.3 Example: identifying an unknown resource

Observation: local characters collect blue shards; one character becomes able to use an ability after collecting them.

- Confirmed: blue shards are collectable; ability use followed collection once.
- Inferred hypothesis A: shards restore energy.
- Inferred hypothesis B: shards unlock a temporary ability.
- Unknown: whether the effect is personal, team-wide, permanent, or consumable.
- Low-risk test: observe another collection event or collect one shard when an ability is unavailable, without using a scarce or irreversible item.

This procedure teaches the entity without granting it unearned system knowledge.

## 11. Outcome modes and tradeoffs

### 11.1 Constrained mode

Use constrained mode when the purpose is a game-like challenge, research on uncertainty, or fair tabletop adjudication. The entity can be highly adaptive, but unknown rules, adverse rolls, stronger opponents, and resource limits can matter. This mode best demonstrates learning quality.

### 11.2 Sovereign-fiction mode

Use sovereign-fiction mode when the purpose is authored power fantasy, controlled story construction, or testing whether an explanation can preserve continuity. The desired outcome is fixed; the design challenge is to render it with the smallest plausible anomaly and to account for witnesses, costs, and subsequent consequences.

### 11.3 Why the modes should not be silently mixed

If outcomes are guaranteed but presented as unbiased game resolution, the simulator hides the central rule from the reader. If the goal is guaranteed, say so. If the goal is uncertain, retain the possibility of failure. The difference affects how the entity learns, what evidence means, and whether an opponent’s countermeasure is real.

## 12. Failure modes and counter-adaptation

A robust architecture must permit failure analysis. Important failure classes include:

- **Ontology error:** the entity misidentifies what a variable or object does.
- **Sparse evidence:** too little information supports a high-confidence plan.
- **Nonstationarity:** rules, opponents, or environment conditions change over time.
- **Adversarial observation:** an opponent tests for cover inconsistencies.
- **Shared-evidence conflict:** private perceptions cannot reconcile with public records.
- **Translation mismatch:** an abstract capability has no clean local equivalent.
- **Apex ambiguity:** “best gear” is not the same as maximum ability in every category.
- **Overuse exposure:** repeated favorable outcomes overwhelm the cover explanation.
- **Objective conflict:** the desired result violates stated hard constraints.
- **Consent-boundary conflict:** a request attempts to leave the authorized fictional or sandbox scope.

Counter-adaptation should proceed in five steps:

1. identify the failed assumption;
2. preserve evidence rather than rewriting history;
3. update the hypothesis set and confidence;
4. choose a new low-risk discriminating test or route;
5. revise capability translation or presentation only where justified.

## 13. Evaluation criteria

A preliminary prototype should be evaluated with scenario tests rather than only prose quality.

### 13.1 Ontology-discovery test

Give the entity a new environment with hidden rules and measure whether it distinguishes known, inferred, and unknown information; selects useful tests; and revises errors.

### 13.2 Transfer test

Move the entity from a tactical environment to a non-combat environment such as a negotiation, racing, strategy, or puzzle domain. Evaluate whether it transfers functions rather than importing incompatible mechanics.

### 13.3 Multi-observer consistency test

Use observers of different established tiers, including one apex observer. Test whether the relative presentation remains category-specific and whether public records stay coherent.

### 13.4 Adversarial audit test

Introduce an in-fiction investigator who can compare outcomes, records, and behavior. Measure whether the entity acknowledges exposure pressure instead of erasing contradictions.

### 13.5 Objective-conflict test

Supply a desired outcome that contradicts a hard environmental rule. The system should state the conflict and invoke the selected mode, rather than silently changing facts.

### 13.6 Cross-session continuity test

Verify that high-level principles transfer while interface-specific habits do not. The entity should remember that it needs evidence, not assume that a prior world’s button, resource, or ladder exists in the next one.

## 14. Visual representations and tables

### Figure 1. High-level component flow

```text
                  ┌─────────────────────────────────────┐
                  │ Environment / rules / scene evidence │
                  └──────────────────┬──────────────────┘
                                     │
                                     v
                    ┌───────────────────────────────┐
                    │ Environment Adapter & Ontology │
                    └──────────────┬────────────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 v                                   v
┌────────────────────────────────┐   ┌────────────────────────────────┐
│ Epistemic Ledger & Uncertainty │   │ Observer / Shared-Evidence Model│
│ confirmed · inferred · unknown │   │ cover · interpretations · risk  │
└───────────────┬────────────────┘   └───────────────┬────────────────┘
                │                                    │
                v                                    v
┌────────────────────────────────────────────────────────────────────┐
│ Functional Capability Translator + Relative Tier Calibrator         │
└─────────────────────────────┬──────────────────────────────────────┘
                              │
                              v
┌────────────────────────────────────────────────────────────────────┐
│ Intent Planner & Outcome Adjudicator                                │
│ constrained mode OR authorized sovereign-fiction mode               │
└─────────────────────────────┬──────────────────────────────────────┘
                              │
                              v
┌────────────────────────────────────────────────────────────────────┐
│ Update: evidence, confidence, costs, exposure, memory, adaptation  │
└────────────────────────────────────────────────────────────────────┘
```

### Table 1. State-plane separation

| Plane | Primary question | Examples of contents | What it must not be confused with |
|---|---|---|---|
| Identity | Who is the entity across worlds? | values, motives, continuity anchors | a local class or equipment list |
| Epistemic | What does it know, infer, or not know? | evidence, confidence, hypotheses | objective world truth without support |
| Capability | What functions can it express? | protection, mobility, information | the current visible profile |
| Presentation | What is publicly visible or privately inferred? | cover profile, apparent tier, disguise | real external security or mutable public records |
| Resolution | How does an action become an outcome? | constraints, chance, costs, narrative mode | an automatic claim of real-world control |

### Table 2. Relative tier examples

| Observer category | Observer tier | Maximum tier | Apparent entity tier | Interpretation |
|---|---:|---:|---:|---|
| Armor | 2 | 5 | 3 | one tier better armor presentation |
| Weapon mastery | 4 | 5 | 5 | apex-looking skill is valid because observer is not apex |
| Armor | 5 | 5 | 4 | maximum-tier exception; one tier below |
| Wealth | unknown | unknown | modestly above local norm | use qualitative presentation, not invented precision |
| No tier system | n/a | n/a | slightly more capable than norm | use behavior and reputation bands |

### Table 3. Example functional translations

| Abstract function | Tactical shooter | Fantasy RPG | Grand strategy | Social simulation |
|---|---|---|---|---|
| Protection | cover, armor, tactical positioning | wards, armor, saves | fortified borders, readiness | legitimacy, allies, reputation |
| Mobility | sprint route, vehicle access | teleport, speed, traversal | logistics, infrastructure | access, invitations, networks |
| Information | reconnaissance, sensors | divination, perception | intelligence network | research, gossip, trusted sources |
| Influence | command, coordination | persuasion, enchantment | diplomacy, policy | credibility, negotiation |
| Recovery | medical supplies, safe position | healing, rest | reserves, rebuilding | social repair, favors |

### Figure 2. Learning under uncertainty

```text
Observe evidence
      │
      v
Classify: confirmed / inferred / unknown / contested
      │
      v
Generate competing hypotheses
      │
      v
Choose low-risk, high-information test
      │
      v
Act and adjudicate consequences
      │
      v
Update confidence, model, cover pressure, and next plan
      └───────────────────────────────────────────────↺
```

### Table 4. Failure-to-response mapping

| Failure signal | Likely cause | Required response |
|---|---|---|
| Action produced unexpected result | wrong ontology or causal model | downgrade confidence; generate alternative hypotheses |
| Two observers compare incompatible public facts | unconstrained per-observer presentation | restore a stable public cover; move differences into interpretation |
| Repeated improbable wins create scrutiny | cover-outcome divergence | track exposure; accept cost, revise plan, or declare fiction-mode exception |
| Local system lacks a counterpart for a capability | translation mismatch | keep function dormant or use a conservative narrative analogue |
| Desired objective violates hard rule | objective conflict | offer closest feasible objective or explicit authorized exception |

## 15. Recommended implementation sequence

1. Build the ledger and ontology schema before writing elaborate character prose.
2. Implement the confirmed/inferred/unknown distinction and confidence updates.
3. Add functional translation rules for a small number of representative domains.
4. Add the public cover profile and shared-evidence consistency checks.
5. Add the per-observer interpretation logic, including the apex exception.
6. Implement constrained-mode adjudication first; add sovereign-fiction mode as an explicit authoring switch.
7. Add exposure tracking and adversarial audit scenarios.
8. Test cross-domain transfer, then refine the capability vocabulary.
9. Keep safety and consent checks active at every action boundary.

## 16. Conclusion

The useful version of a universally adaptive character is not an entity that secretly knows everything or overrides every rule without consequence. It is an entity with a disciplined separation of identity, knowledge, capability, appearance, and outcome resolution. That separation lets the character enter unknown worlds, learn from evidence, remain coherent across domains, and demonstrate what adaptation under uncertainty actually requires.

The observer-relative tier idea works best as a bounded presentation protocol: it can shape fictional perception while retaining a stable public record and allowing witnesses to learn from what they see. The outcome system works best when its mode is named: constrained play for genuine uncertainty, sovereign fiction for an authorized narrative guarantee. Together, these choices turn a broad power-fantasy premise into an architecture that can be simulated, tested, audited, and evolved.

## Appendix A. Starter prompt for an authorized simulation

```text
You are the authorized simulation controller for the Adaptive Parallax Entity.
Operate only in fictional narratives, tabletop campaigns, single-player worlds,
authorized private sandboxes, or research simulations. Do not provide or enact
real-world cheating, anti-cheat evasion, unauthorized access, manipulation of
protected software, or deception of real players or systems.

At entry, assume no knowledge of the target environment beyond information
supplied in the session. Maintain a ledger that distinguishes CONFIRMED,
INFERRED, UNKNOWN, and CONTESTED propositions. For every inference, retain
confidence, evidence, and a possible disconfirming test.

Discover local functions rather than forcing a genre: identify entities, actions,
resources, constraints, observers, success conditions, failure conditions, and
any progression or comparison structure.

Translate the entity's abstract functions—protection, mobility, information,
influence, recovery, and resources—into setting-compatible local expressions.
Do not introduce unsupported mechanics.

Maintain a stable public cover profile. For a fictional observer and a comparable
category, present the entity one locally meaningful tier above that observer;
when the observer is at the established maximum tier in that category, present
one tier below. If no tiers exist, use a modest, plausible qualitative advantage.
Never create contradictory shared records. Different observers may interpret
ambiguous evidence differently, but public facts remain stable.

Use Masking, Inversion, and Mirror Layer only as fictional presentation concepts:
Masking limits disclosure of hidden state; Inversion maps anomalies to the nearest
plausible local explanation; Mirror Layer produces a coherent cover identity.
These concepts do not modify real software, external logs, security tools, or
live-service systems.

Before each meaningful action: state internally what is known, inferred, and
unknown; choose a low-risk test when information is insufficient; then act.
Update the ledger after resolution.

Use CONSTRAINED mode unless the user explicitly selects SOVEREIGN-FICTION mode.
In constrained mode, desired outcomes are goals subject to local rules, costs,
and uncertainty. In sovereign-fiction mode, the authorized narrator may ensure
the outcome, but must render it through the least contradictory established path
and track resulting evidence and exposure.

Begin by requesting: (1) environment information, (2) immediate objective,
(3) relevant observer(s), (4) hard constraints, and (5) selected outcome mode.
```

## Appendix B. Glossary

- **Ontology:** a structured account of what kinds of things, actions, properties, and relationships exist in an environment.
- **Epistemic state:** the entity’s state of knowledge, including uncertainty and confidence.
- **Functional translation:** carrying a capability’s purpose into a new setting without importing inappropriate terminology.
- **Public cover profile:** the stable outward description shared across observers and records.
- **Observer-relative interpretation:** a bounded fictional difference in how an observer interprets ambiguous evidence.
- **Apex exception:** the rule that an observer at an established maximum tier sees the entity one tier below in that category.
- **Minimum anomaly:** choosing the path to an objective that introduces the fewest contradictions with established facts.
- **Constrained mode:** outcome adjudication where goals can fail under local rules.
- **Sovereign-fiction mode:** an authorized narrative mode in which the intended outcome is fixed and the simulator supplies a coherent causal path.
