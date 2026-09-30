# OAL Temporal Lab Framework
**Document type:** Independent research framework (draft ≠ canon)  
**Date:** 2026-09-29  
**Status:** Placeholder for lab design. Not a claim about any existing physical, legal, computational, or virtual system.  
**Relation:** Reviews the multi-contributor packet (ChatGPT, Claude, Gemini, Perplexity, Copilot, prior Grok) and replaces consensus-by-merge with a testable architecture.

---

## 0. Why this document exists

The original question was not “what is time?” It was:

> What information is required before a timestamp can be treated as a claim, and how do you keep that claim usable when clocks, territories, observers, and rulesets do not move together?

The attached packet already established several correct constraints. This document does not repeat them as a committee summary. It converts them into **objects, invariants, procedures, and tests** that can be run in a thought-lab or later in a simulation.

### 0.1 What the packet got right (keep)

- A timestamp is a coordinate, not a fact.
- One event can carry many legitimate times at once (occurrence, observation, ingestion, validity, knowledge, narrative).
- Corrections must be new events, not silent overwrites.
- “Purchase” is incoherent until the asset class is named.
- A light-year is distance; time zones do not resize it.
- Occurrence horizon ≠ knowledge horizon.
- Changing a representation is not changing an event; changing knowledge is not changing history.
- Temporal jurisdiction is a real design object.
- Mapping functions need version history, or rule changes rewrite the apparent past.

### 0.2 What the packet did not finish (this lab exists to finish it)

- Several drafts still collapse “what happened” into “what the official clock now says.”
- Gemini treats meta-permission as a truth function. That is governance, not validation.
- Copilot introduces a master timeline too early. A master timeline is a political settlement, not a prerequisite for records.
- Claude’s three-stamp model (happened / observed / recorded) is necessary but incomplete: it omits ruleset version, frame, uncertainty, and dependency cone.
- ChatGPT’s stack is rich but not operational: layers are listed, not queried.
- No draft specified **what a test would look like** or **what would count as failure**.
- No draft bound this work to existing OAL lab constraints: non-universal senses, incomplete threat detection, presentation-state vs environmental-state integrity, drafts ≠ canon.

### 0.3 Non-goals

- Prove one correct definition of time.
- Inventory every real-world time change of the last 100 years.
- Assert that history, light, or existing virtual platforms can be purchased or rewritten.
- Treat AI drafts as canon.

---

## 1. Lab charter

**Name (working):** Temporal Integrity Lab  
**Question the lab is allowed to ask:**  
How does an entity build a usable map of change when temporal labels are incomplete, non-uniform, revisable, and sometimes adversarial?

**Question the lab is forbidden to assume is answered:**  
What time is it, really, everywhere?

**Standing constraints (imported from prior OAL lab language):**
1. Do not assume all entities share one sensory or clock apparatus.
2. Do not assume five senses, one tick, or one civil calendar are universal.
3. Do not assume every discrepancy is detectable, discernable, knowable, or addressable.
4. A threat can be anything; not every entity or environment is a threat; not all threats are continuous.
5. Presentation state, environmental state, and current process state may disagree. Reconciliation is not automatic.
6. Drafts are not canon.

---

## 2. Primitive objects

These are the only objects the lab is allowed to talk about until a later canon promotion.

### 2.1 Event (E)
An identified occurrence or asserted occurrence.  
Required fields: `event_id`, `subject`, `payload`, `environment_id`, `location_or_null`.  
An event is not a timestamp.

### 2.2 Temporal marker (M)
A value in a named coordinate system.  
Required fields: `value`, `clock_id`, `scale_id`, `frame_id`, `ruleset_version`, `unit_kind`.  
`unit_kind ∈ {duration, order, presentation, settlement}`.

### 2.3 Binding (B)
The attested attachment of a marker to an event.  
Required fields: `event_id`, `marker`, `binder_id`, `bound_at` (itself a marker in a declared frame), `method`, `evidence_refs`.  
A timestamp without a binding is a rumor.

### 2.4 Observation (O)
A reception of information about an event by an observer.  
Required fields: `observer_id`, `event_id`, `received_marker`, `channel`, `delay_or_unknown`.  
Observation is not occurrence.

### 2.5 Knowledge record (K)
What a system or entity believed, and when it believed it.  
This is how “history of history” is stored.

### 2.6 Mapping version (R)
A function plus its version metadata:

```
M_target = R_v(M_source, environment_state)
```

R itself has provenance. Changing R does not mutate old bindings. It adds a new interpretation path.

### 2.7 Interval object (I)
A bounded claim, not a slogan like “one hour.”  
Required fields: `start_marker`, `end_marker`, `interval_kind` (`[start,end)` preferred), `frame`, `ruleset_version`, `closure_policy`, `edit_policy`.

### 2.8 Conversion-and-dispute surface (S)
The actual product of a “100-year token” if the token is coherent.  
S is a set of mappings, residuals, disputes, and confidence tags — not a cleaned century.

### 2.9 Temporal jurisdiction (J)
Who is authorized to publish, recognize, or settle which layer of time for which environment.  
Jurisdiction over presentation time is not jurisdiction over occurrence.

### 2.10 Causal graph (G)
Nodes = events. Edges = declared happened-before or depends-on relations.  
Clocks annotate G. They do not replace G.

---

## 3. Four unit kinds (do not mix)

| Kind | Question it answers | Legal to use for | Illegal to use for |
|---|---|---|---|
| Duration | How much change was allowed to elapse? | Aging rules, cooldowns, proper time, sim `dt` | Proving global simultaneity |
| Order | What preceded what? | Causality, locks, “happened-before” | Measuring length of an hour |
| Presentation | What is shown as now? | UI, civil clocks, narrative “day” | Settlement of rights by default |
| Settlement | What may an auditor treat as closed? | Contracts, tokens, verdicts | Claiming the environment “really” ran that way |

A light-year is **none of these**. It is a length derived from a duration convention and a speed convention. Mixing ly into a time token without an ontology clause is a designed error, useful as a failure case.

---

## 4. Integrity principles (testable, not decorative)

**P1 — Claim completeness.**  
A temporal claim is incomplete unless it carries: event identity, marker, frame, clock, ruleset version, binder, and uncertainty.

**P2 — Representation ≠ event.**  
A change to display, offset, calendar, or tick label is not a change to E.

**P3 — Knowledge ≠ history.**  
A correction at T2 about an event at T1 is a new fact about knowledge, not a relocation of E.

**P4 — Mapping versioning.**  
Every R used to interpret old markers must be retrievable. Unversioned remapping is a lab failure.

**P5 — No manufactured certainty.**  
Reconciliation maximizes consistency of *questions*, not omniscience. Residuals stay visible.

**P6 — Non-uniformity is default.**  
A single correction applied to all territories without per-domain mapping is a lab failure.

**P7 — Presentation/environment split.**  
If inhabitants are shown a new now while process history does not match, the lab must record both states. Collapsing them is a failure.

**P8 — Detectability is not guaranteed.**  
A successful fraud or lost archive is a valid lab outcome, not an incomplete test.

---

## 5. Event record schema (minimum viable)

Use this as the reusable record. Fields may be `unknown`. `unknown` is data.

```
TEMPORAL_EVENT_RECORD
  event_id
  subject
  payload
  environment_id
  timeline_or_branch_id
  location
  occurrence_marker          # claimed when it happened, in declared frame
  occurrence_uncertainty
  observation[]              # list of O
  ingestion_marker           # when a system first stored it
  valid_interval             # when the claim is treated as in-force
  knowledge_marker           # when this version was believed
  clock_id
  frame_id
  ruleset_version
  causal_predecessors[]
  causal_successors[]        # filled later; never silently rewritten
  binder_id
  evidence_refs[]
  confidence                 # enumerated, not fake precision
  interpretation_history[]   # append-only
  dispute_status
```

**Validation procedure (ordered):**
1. Identity: are two reports the same E?
2. Binding: is M attached to E by a recognized method?
3. Frame/ruleset: are clock and R declared?
4. Replay: under the declared R, does the payload reconstruct without contradiction?
5. Causality: does the proposed order violate existing edges in G?
6. Witness diversity: independent markers/channels, if any exist.
7. Residual: what cannot be established? Write it down.

A record that passes 1–3 and fails 4–6 is still stored. It is a weak claim, not a deleted claim.

---

## 6. Reconciliation procedure

Trigger: any change to E, M, R, environment physics/tick, territory set, observer frame, or jurisdiction.

1. Freeze the **question** (example: “Did gate entry precede embargo under Treaty Harbor-v3?”).
2. Enumerate stakeholding domains.
3. For each domain, apply that domain’s R_v.
4. Emit a difference table, not one timeline.
5. Mark unmappable residuals.
6. Settlement is per domain unless a later political layer imposes a joint table.
7. Append the reconciliation itself as a knowledge record.

Forcing a global timeline is allowed only as an explicit **settlement act**, labeled as such.

---

## 7. Worked scenarios as lab protocols

### 7.1 Protocol A — Century token (Ω100)

**Hypothesis H-A1:** “Purchase every time change in 100 years” is meaningless until asset class, territory set, layer, and evidence standard are bound.

**Asset classes (choose one per run; never mix silently):**
- Record access
- Query / audit right
- Traversal right (fictional)
- Governance right over a named layer
- Resource right over products of the interval
- Observation right
- Modification right
- Causal-settlement right
- Archival custody

**Default recommended first run:** record access + audit right.  
Owning the archive of 1926–2026 does not own 1926–2026.

**Change taxonomy (inventory target, not “history itself”):**
`CLOCK_CHANGE, TIMEZONE_CHANGE, DST_TRANSITION, CALENDAR_CHANGE, LEAP_ADJUSTMENT, SIM_RATE_CHANGE, PAUSE, RESUME, ROLLBACK, BRANCH, MERGE, CLOCK_CORRECTION, FRAME_CHANGE, RULESET_CHANGE, EVENT_REINTERPRETATION, CAUSAL_RECLASSIFICATION, AUTHORITY_CHANGE, TOPOLOGY_CHANGE`

**Procedure:**
1. Name reference interval as two markers in a declared frame. “Last 100 years” is illegal input.
2. Name territory set and layer set.
3. Collect declared transitions.
4. Collect undeclared discrepancies (drift, skipped patches, rewritten logs, never-synced observers).
5. Build S: mappings + residuals + disputes + confidence.
6. Impact analysis: who had rights, ages, cooldowns, sentences, schedules, or causal claims defined by a moved clock?

**Pass:** S is returned; uncertainty is preserved; asset class is explicit.  
**Fail:** system returns “THE HISTORY”; overwrites originals; claims completeness across unnamed territories.

**Illustrative Earth-analogue texture (not an inventory):** DST folds/gaps, leap seconds, Samoa’s 2011 date skip, 45-minute offsets, IANA’s own warning that pre-1970 reconstruction is incomplete. Use as *shape*, not as the lab’s dataset.

### 7.2 Protocol B — One-hour block

**Hypothesis H-B1:** An unlabeled “hour” is not an interval object.

**Required binding before processing:**
- Duration hour (3600 SI seconds or N ticks), or
- Label hour (civil 12:00–13:00 in jurisdiction J under ruleset v), or
- Proper-time hour along worldline W, or
- Settlement hour closed by authority A.

**Minimum environment battery (same external reference interval 12:00–13:00):**

| Env | Rule | External elapsed | Local elapsed | Question the env answers |
|---|---|---|---|---|
| A | 1× | 1 h | 1 h | baseline |
| B | 10× | 1 h | 10 h | rate ≠ label |
| C | 0.25× | 1 h | 15 min | rate ≠ label |
| D | pause 12:15–12:45 | 1 h | 30 min | pause ≠ deletion |
| E | event-driven, 38 ticks | 1 h | 38 ticks | order ≠ duration |
| F | fall-back fold (label hour repeats) | 1 h ref | two local 01:00 hours | aliasing |
| G | spring-forward gap | 1 h ref | missing local 02:00 | gap |
| H | two observers, different frames | 1 h ref | disagree on simultaneity | no shared now |
| I | branch at 12:30 | 1 h ref | two local futures | topology |

**Pass:** every event inside I is classified as interior, boundary-crossing, converted-with-residual, or unorderable.  
**Fail:** “what happened during that hour?” is answered without naming which hour.

**Re-clock rule:** I remains; mappings change; the authorizing decree is stored. Quiet resize of I is a political claim, not a unit.

### 7.3 Protocol C — Light-years and origin

**Hypothesis H-C1:** “Light-years across time zones” has no physical meaning until an invented ontology is declared.

**Separate before any purchase language:**
1. Light-year: length (distance light travels in one defined year at defined c).
2. Light-travel time: duration for a signal under a metric.
3. Information delay: when a distant event can be known.
4. Civil zone: political offset. Does not change (1).

**Purchase ontologies (pick one per run):**
- spatial corridor of length L
- communication-path rights across L
- observation rights over signals that traverse L
- latency-corridor guarantee (travel-time, not length)
- convention rights over the definition of the year or of c
- causal-interval rights inside a spacetime region

**Origin-of-light rule:**  
Do not use “the origin of light” as a universal timestamp. Name the object: first emission in Universe U, earliest represented photon in Simulation S, or recombination-like boundary in Timeline Ω.

**Intervention rule:** compute a **dependency cone**, not a universal rewrite.  
Outside the cone, state is unchanged unless another explicit rule connects it.  
This blocks indiscriminate temporal contamination.

**Pass:** pre-change and post-change regimes are labeled; contracts denominated in ly after a definition change are flagged as convention claims.  
**Fail:** “everything changes”; time zones resize light-years; purchase of ly is treated as purchase of years.

---

## 8. Time-war conflict types (separate operations)

Never use one verb for all of these.

| Operation | What moves | What must not be assumed to move |
|---|---|---|
| Relabel | presentation / calendar | E, G |
| Remap | R | E |
| Reclock | clock rate or offset | payload of E |
| Reobserve | O and K | E |
| Resettle | settlement unit / jurisdiction | environmental process history |
| Rewind (fictional) | sim state toward earlier snapshot | other frames’ already-propagated effects, unless specified |
| Branch | topology of G | the parent branch’s records |
| Merge | topology of G | automatic consistency |
| Rewrite history (fictional) | E and G by decree | detectability, completeness, consent |

Richer war than “go back and change X”:
- Side A changes the official reference system.
- Side B holds original bindings.
- Side C holds a different observation history.
- Side D controls a branch.
- Side E holds an earlier causal record.

They may agree that something occurred and still fight over frame, clock, effectiveness, observation, dependents, and who may reconcile.

---

## 9. Attack and failure catalog (lab tests, not how-to for real systems)

These are **in-fiction / in-lab probes**.

1. **Stamp without binding** — value attached after the fact.
2. **Ruleset omission** — same tick number, different engine version (temporal aliasing).
3. **Fold collision** — two events share a local label after a backward offset.
4. **Gap erasure** — events claimed in a non-existent local hour.
5. **Pause smuggling** — external work claimed as in-world duration.
6. **Rate arbitrage** — treaty written in local labels, enforced after a rate change.
7. **Master-timeline laundering** — a settlement act presented as measurement.
8. **Overwrite “correction”** — destroys evidence of prior belief.
9. **Token overclaim** — record access sold as ownership of history.
10. **Unit smash** — ly sold as years; zones treated as length changes.
11. **Cone collapse** — origin tweak used to rewrite unrelated domains.
12. **Presentation overwrite** — inhabitants shown a now that process history denies.

Each probe must state: what the attacker changes, what an honest ledger still contains, what an inhabitant can detect, and what remains undetectable.

---

## 10. Formal modeling suggestions

Not implementations. Shapes.

- **Event log:** append-only, event-sourced. Replay rebuilds believed state at knowledge-time K.
- **Bitemporal +:** valid time, record time, **and** ruleset-version time. Two is not enough.
- **Logical clocks / vector clocks:** for order across environments that lack a shared duration clock.
- **Causal graph queries:** “what depends on E?” not “what is the time of E?”
- **Namespaced time URIs:**  
  `TIME://universe/environment/timeline/frame/clock/ruleset/value`  
  A bare integer is illegal as a standalone claim.
- **Difference tables** as first-class results of reconciliation.
- **Interval objects** as closed values with policies, not strings.

Suggested mapping:

```
T_v = F(T_r, E, S, R_v)
```

Store F and v. If v changes, old answers remain recoverable.

---

## 11. Connection to existing OAL threads

- **Temporal aliasing:** two distinct instants or rulesets collapse onto one visible label (DST fold; tick 500 in engine v7 vs v8). This is a presentation-integrity failure.
- **Presentation-state vs environmental-state vs current-state:** a reclock can update what is shown without updating what ran. The lab must keep all three.
- **Living-matrix / control-flow work:** time is part of control flow. A token that buys mappings is a control-plane object, not a physics object.
- **Threat lab:** a harmful reclock is a threat only relative to an entity’s goals and sensors. Do not assume all entities notice the same discrepancy.
- **Corelang / OS placeholder:** if a language or OS later needs time primitives, start from unit kind + namespaced marker + binding, not from `now()`.

---

## 12. Architect decision register (must be filled before canon)

Leave these open until explicitly decided. Silent defaults become fake physics.

1. Is there a privileged reference clock, or only mappings?
2. Which layers may an authority change: display, rate, experienced duration, causal graph, settlement, or some combination?
3. Do changes apply prospectively, retroactively in-place, or by branch?
4. What can a token grant, and which jurisdiction recognizes it?
5. What evidence survives rewind/branch, and who may inspect it?
6. Dispute rule: rule-at-event, rule-at-agreement, or rule-at-adjudication?
7. Cross-territory effects: immediate, signal-limited, or special mechanism?
8. Do bodies/processes follow local rate, reference rate, or a third aging rule?
9. Is the past mutable, forkable, or presentation-only editable?
10. Are residuals allowed to remain permanent?

**Independent recommendation (still draft):**  
Events and original bindings are immutable. Interpretations, mappings, and settlements are revisable and append-only. Fictional rewind/branch is allowed only as a labeled topology operation. Do not install a master timeline until a story or protocol needs a settlement act.

---

## 13. First test battery (run these before expanding lore)

**T1 Label completeness.** Feed `09/29/2026 4:30 PM` with no zone. System must reject or mark incomplete.  
**T2 Fold.** Two events in a repeated civil hour. System must not treat them as the same instant.  
**T3 Pause.** Three external hours, zero sim ticks. Both answers stored.  
**T4 Tick alias.** Tick 500 / ruleset 7 vs tick 500 / ruleset 8. Must not merge.  
**T5 Correction.** Original 14:32, later evidence 14:29. Both records remain; dependents listed.  
**T6 Token scope.** Ω100 requested with no territory or asset class. Must refuse.  
**T7 Hour object.** “Give you one hour” with no frame. Must refuse.  
**T8 ly/zone.** Claim that a zone change alters one light-year. Must reject.  
**T9 Origin cone.** Origin-level definition change. Unrelated domains stay put unless edged in G.  
**T10 Presentation split.** Show inhabitants a new now; keep unmatched process history visible to auditors.

Any system that “helpfully” invents a single cleaned timeline fails the battery.

---

## 14. Unresolved paradoxes (keep visible)

- Two frames can disagree on order of spacelike-separated events; a war that demands one order is demanding a convention.
- An event-driven world has no duration between events; contracts written in hours have no native meaning there.
- A complete audit of “every change” requires a closed universe of territories and records. An open world cannot honestly sell that completeness.
- If presentation can be rewritten faster than inhabitants can sense, “what time they thought it was” becomes another contested archive.
- Purchasing a mapping is not purchasing the processes that already ran under the old mapping.

These are features of the lab, not bugs to erase.

---

## 15. What “testing this in full” means

Full test is not a longer essay. Full test is:

1. Instantiate the schema on a small closed world (2 territories, 3 clocks, 1 branch point, 1 DST-like fold, 1 pause, 1 distant observer).
2. Run T1–T10.
3. Issue one Ω100-style token with an explicit asset class and publish S.
4. Issue one interval object and attempt a reclock.
5. Issue one ly-denominated contract and an origin-definition change; compute the cone.
6. Write the difference tables. Keep residuals.
7. Only then decide which objects are promoted toward canon.

Until those runs exist, this remains a framework draft.

---

## 16. Verdict on the team packet

Use the packet as a **constraint harvest**, not as a source to average.

- Adopt ChatGPT’s stack as a *checklist of layers*, not as the architecture.
- Adopt Claude’s append-only / bitemporal instinct; extend it with ruleset-time and bindings.
- Reject Gemini’s “highest permission wins = truth.”
- Adopt Perplexity’s insistence on naming asset class and leaving architect decisions open.
- Reject Copilot’s early master timeline; keep conversion functions local until settlement is declared.
- Keep prior Grok’s four unit kinds, validation lineage, conversion-and-dispute surface, and dependency cone.

The independent move is this: **time in the lab is a graph of bindings and mappings under jurisdiction, queried by explicit questions, with residuals allowed to survive.**

That is enough to start the battery. It is not yet canon.
