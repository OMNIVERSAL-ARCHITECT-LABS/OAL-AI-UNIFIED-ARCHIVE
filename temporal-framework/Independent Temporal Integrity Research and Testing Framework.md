# Independent Temporal Integrity Research and Testing Framework

## Executive finding

The contributor set has reached a strong conceptual convergence: time must not be represented as a single timestamp, and a time-referenced event must be modeled as an event plus a clock, environment, ruleset, observer, provenance chain, uncertainty statement, and causal context. The shared recommendation to preserve original assertions while adding corrections is consistent with event sourcing and system-versioned temporal data, both of which support reconstruction of earlier states rather than retaining only the latest value.[^1][^2]

The material is ready to move from ideation into a governed research program, but it is **not yet ready for a single “full test.”** The current proposals combine five different objects of inquiry: physical time, civil-time representation, distributed-system ordering, simulation time, and fictional powers that alter history. These require separate test tracks joined by a common event ontology. The appropriate next artifact is therefore a **Temporal Integrity Test Framework (TITF)**: a model-and-protocol framework that tests internal consistency, traceability, conversion correctness, resilience under temporal changes, and narrative consequences without claiming to experimentally determine the metaphysical nature of time.

## Contributor review

### Areas of convergence

Across the contributor responses, the most stable ideas are:

- **No unqualified timestamp:** a time value is meaningful only relative to a clock or counter, scale, environment, ruleset version, and often an observer or reference frame.
- **Multiple valid temporal coordinates:** occurrence time, observation time, receipt time, record time, effective time, correction time, simulation time, and causal position can all differ.
- **Causality is not reducible to wall-clock order:** Lamport’s “happened-before” relation establishes a partial order of distributed events; logical clocks can impose an order consistent with causal constraints without proving a universal physical chronology.[^3][^4]
- **Append rather than overwrite:** corrections, reinterpretations, and ruleset changes should produce new records linked to prior assertions.
- **Explicit jurisdiction:** a time claim must say which territorial, computational, physical, legal, or narrative authority governs it.
- **Separate representation from reality change:** changing a displayed time, changing knowledge about an event, and changing fictional history are different operations.
- **Tokens confer defined rights, not undefined ownership of time:** access, audit, traversal, governance, modification, and archival custody must be modeled separately.
- **Light-year discipline:** a light-year is a distance, while observation of an object at that distance carries a propagation delay; terrestrial time zones do not alter the distance.[^5]

This convergence is substantial enough to support a shared core ontology. It does not, by itself, resolve the constitutional and fictional choices needed to determine which timeline becomes canonical or who may change temporal rules.

### Productive differences

| Issue | Position found in the responses | Independent assessment |
|---|---|---|
| Reference architecture | One master/global clock versus mappings among local clocks | Do not require a master clock. Permit optional reference clocks and require explicit, versioned mappings. |
| Event immutability | Immutable events with revisable interpretations versus branches that replace events | Preserve immutable **claims and evidence**. Whether the fictional event itself can change is a separate world rule. |
| Canonical reconciliation | Highest authority or latest meta-time edit wins versus unresolved plural histories | Authority can settle governance but cannot manufacture evidentiary certainty. Preserve dissenting histories and the settlement decision separately. |
| Token ownership | Control of the interval and its contents versus access/audit rights | Begin with access and audit rights. Treat control, traversal, and alteration as elevated, separately granted capabilities. |
| One-hour membership | Events belong to a fixed interval versus membership changes after re-clocking | Preserve the original interval definition and calculate new membership as a derived view. Never silently resize the original object. |
| Origin-level light change | Recalculate all downstream reality versus branch or causal-cone propagation | Require an explicit propagation law. Default to dependency-cone analysis, not indiscriminate universal rewriting. |
| Validation outcome | Determine “what really happened” versus establish a warranted temporal claim | Validation should produce a bounded claim with evidence and uncertainty, not absolute truth. |

### Weaknesses to correct

The responses are strongest as conceptual design and weakest as test methodology. Several propose ledgers and examples without specifying falsifiable properties, test oracles, coverage requirements, stopping criteria, or how contradictory outputs should be classified. Some also slide between a **record of an event** and the **event itself**, or between computational replay and literal alteration of history.

The use of a single global timeline in some drafts is too strong for the intended scope. Distributed systems may only support partial ordering, while relativistic frameworks distinguish proper and coordinate time; NIST’s lunar-time work specifically models clock-rate differences caused by gravity and motion and the need for interoperable coordinate references. A global coordinate may be selected for a particular experiment, but it must be declared as a modeling choice rather than discovered as a universal clock.[^6][^7]

The “100-year” proposal also needs a completeness discipline. IANA’s time-zone database records known civil-clock transitions but warns that it is not authoritative, contains errors, has especially incomplete pre-1970 coverage, and sometimes models gradual historical adoption as an instantaneous change. A valid century audit must therefore report the covered corpus, evidence quality, known gaps, and residual uncertainty—not “all changes” without qualification.[^8]

## Research boundary

### What can be tested

The framework can test whether a specified temporal model:

- Represents distinct time domains without accidental collapse.
- Preserves event identity through clock, calendar, and ruleset changes.
- Produces reproducible conversions when the same inputs and rules are used.
- Detects ambiguity, gaps, duplicated labels, impossible causal cycles, and missing provenance.
- Retains original evidence when corrections and canonical decisions are added.
- Reconstructs a past system state under a named knowledge cutoff.
- Maps impacts to affected entities, contracts, systems, observers, and downstream events.
- Remains stable under clock skew, pauses, rate changes, rollback, branching, delayed observations, and adversarial records.
- Makes fictional consequences follow the declared world rules.

### What cannot be established

This program cannot prove that one model is the true nature of time, validate literal ownership of real time, demonstrate real retrocausality, or infer that simulated rewinds are physical rewinds. It also cannot certify a complete century of real-world local timekeeping without a bounded territory list and authoritative evidence corpus. The framework tests the coherence and behavior of representations and rules.

## Epistemic labels

Every proposition and test result should carry one of three labels:

| Label | Meaning | Example |
|---|---|---|
| **E — Established analogue** | Supported by accepted physical, standards, or computing practice | The SI second has a formal cesium-133 definition.[^9] |
| **D — Design rule** | Chosen for the project because it improves consistency or auditability | Corrections are appended and linked rather than overwriting earlier claims. |
| **S — Speculative extension** | Fictional capability whose behavior must be stipulated | A token permits traversal into a closed temporal block. |

The labels apply to individual claims, not whole documents. A fictional scenario can contain established units, designed data structures, and speculative powers simultaneously.

## Core model

### Temporal reference tuple

A temporal value should be represented as the tuple:

\[
T = (v, u, c, s, e, f, r, b, q)
\]

where:

- \(v\) is the numeric or symbolic value;
- \(u\) is the unit;
- \(c\) is the clock or counter identity;
- \(s\) is the time scale or progression model;
- \(e\) is the environment or territory;
- \(f\) is the physical, computational, observer, or legal frame;
- \(r\) is the temporal ruleset and version;
- \(b\) is the timeline or branch;
- \(q\) is uncertainty, precision, or confidence metadata.

For civil timestamps, Internet standards already demonstrate why an explicit relationship to UTC matters, while also noting that many historical offsets cannot be represented exactly as integral numbers of minutes. The fictional model generalizes that principle beyond UTC to any declared clock and mapping regime.[^10][^11]

### Event claim record

The fundamental stored object should be an **Event Claim Record**, not an unqualified event row:

| Field group | Minimum contents |
|---|---|
| Identity | Claim ID, asserted event ID, event type, subject, object, environment, location |
| Temporal coordinates | Occurrence interval, local display, simulation tick, observation time, ingestion time, effective time, record time |
| Temporal bindings | Clock ID, scale, frame, ruleset version, branch, conversion function ID |
| Causal structure | Parent events, dependent events, concurrency status, causal constraints |
| Evidence | Source artifacts, witnesses, signatures or integrity bindings, acquisition method |
| Provenance | Claiming agent, observing agent, recording agent, validating agent, derivation lineage |
| Epistemic state | Observed/inferred/reported/simulated, confidence, uncertainty interval, disputes |
| Governance | Jurisdiction, authority, permissions, canonical status, review decision |
| Version lineage | Supersedes, corrects, reinterprets, branches from, merged into |

W3C PROV provides an established foundation for exchanging provenance across heterogeneous systems by representing entities, activities, agents, and their relationships. It can inform the provenance portion without dictating the entire fictional temporal ontology.[^12][^13]

### Graph architecture

The primary representation should be a **versioned temporal claim graph**:

- Nodes represent events, claims, observations, rulesets, clocks, tokens, jurisdictions, corrections, and decisions.
- Edges represent causation, observation, derivation, temporal mapping, contradiction, supersession, jurisdiction, and authorization.
- Local clock values are coordinates attached to nodes, not the sole ordering mechanism.
- Branches are named subgraphs with explicit fork and merge rules.
- Canon is a governed status assigned to claims or branches; it is not deletion of alternatives.

This structure preserves Lamport-style causal partial orders while allowing optional total orders for domains whose rules require one. It also supports history reconstruction analogous to event sourcing and system-versioned data.[^2][^3][^1]

## Required invariants

The first full test campaign should evaluate these invariants:

1. **Identity preservation:** changing a temporal representation does not silently create or destroy the asserted event identity.
2. **No undeclared frame:** every temporal coordinate names its clock/counter, frame, environment, and ruleset version.
3. **Causal monotonicity:** if claim A is a declared cause of claim B in one branch, accepted mappings cannot place B before A unless a specific speculative rule authorizes retrocausality.
4. **Correction preservation:** a corrected claim remains discoverable with its evidence, status, and period of acceptance.
5. **Mapping reproducibility:** the same source coordinate, target frame, and mapping version produce the same result.
6. **Ambiguity visibility:** a fold, gap, non-bijective mapping, or unorderable pair is returned as such rather than forced into a false exact answer.
7. **Uncertainty conservation:** transformations cannot silently increase precision or confidence.
8. **Provenance continuity:** every derived claim can be traced to sources, transformations, and responsible agents.
9. **Branch isolation:** events in one branch do not affect another unless a declared cross-branch edge permits it.
10. **Authority separation:** authority to observe, record, interpret, canonicalize, traverse, or alter is independently represented.
11. **Token non-expansion:** a token grants only the rights enumerated in its instrument.
12. **Knowledge-state separation:** what an observer knew at a time remains distinct from what the framework later concludes.
13. **Idempotent replay:** replaying the same ordered claims under the same rules yields the same state.
14. **Bounded reconciliation:** every reconciliation report states scope, evidence cutoff, ruleset, unresolved conflicts, and omissions.
15. **Distance-duration separation:** light-year values remain distance measures unless a fictional instrument explicitly defines a different asset.

## Validation protocol

Each submitted event claim should pass through nine gates:

1. **Schema validation:** required identity, time, environment, and ruleset fields exist.
2. **Binding validation:** evidence shows that the temporal marker was bound to this claim by an identified source.
3. **Clock validation:** the clock or counter exists, and its behavior is defined for the relevant interval.
4. **Mapping validation:** conversions use a named, versioned function and expose loss, ambiguity, and uncertainty.
5. **Causal validation:** declared dependencies do not violate branch rules or known message/order constraints.
6. **Provenance validation:** source, observer, recorder, transforms, and validating authority are traceable.
7. **Corroboration assessment:** independent evidence is compared without treating repetition from one source as independence.
8. **Governance validation:** the adjudicating authority has jurisdiction over the decision it is making.
9. **Result classification:** validated, conditionally validated, disputed, indeterminate, contradicted, or invalidly formed.

Validation is therefore a status assigned to a bounded claim, not proof that an event is metaphysically true. This follows the contributor insight that an event is not validated merely because a clock displayed a value.

## Reconciliation protocol

A reconciliation run should be query-centered. “What time was it?” is usually too broad; “Did Gate Event G occur before Embargo E under Treaty Ruleset R?” is testable.

The procedure is:

1. Freeze the question, scope, evidence cutoff, and permitted rulesets.
2. Enumerate all affected environments, jurisdictions, branches, clocks, entities, and observers.
3. Retrieve claims and all correction, supersession, and dispute links.
4. Build each domain’s local ordering before attempting cross-domain conversion.
5. Apply only declared, versioned mappings.
6. Calculate causal constraints independently of displayed clock order.
7. Generate candidate reconciliations rather than assuming one answer.
8. Score candidates by evidence support, rule compliance, causal consistency, and information loss.
9. Record authority decisions separately from evidentiary findings.
10. Publish unresolved conflicts, unmapped residuals, and alternative lawful interpretations.

A temporal-table implementation can preserve prior row versions and support point-in-time queries, while event sourcing can reconstruct states and replay corrected sequences. Neither technique alone settles cross-branch metaphysics or authority; those remain explicit design layers.[^1][^2]

## Full test matrix

### Dimensions

| Dimension | Required values |
|---|---|
| Progression | Continuous, fixed tick, variable tick, event-driven, paused, accelerated, slowed |
| Mapping | One-to-one, many-to-one, one-to-many, discontinuous, undefined, probabilistic |
| Ordering | Total, partial, concurrent, cyclic claim, retrocausal by rule |
| History model | Immutable, corrigible claims, rollback, replacement, branching, merge |
| Observation | Immediate, delayed, censored, contradictory, observer-relative |
| Governance | Single authority, overlapping authority, disputed authority, no authority |
| Evidence | Complete, missing, forged, delayed, duplicated, corrupted, mutually inconsistent |
| Change timing | Prospective, retroactive interpretation, retroactive fictional effect, emergency |
| Territory | Single, crossing, nested, mobile, boundary-disputed |
| Rights | Observe, query, audit, retain, transfer, traverse, govern, modify |

Testing should use pairwise coverage first, then targeted higher-order combinations around the highest-risk interactions: branch plus rollback plus delayed evidence; overlapping jurisdiction plus tokenized modification; and rate changes plus boundary-crossing contracts.

### Test oracles

A test oracle determines whether an output passes. TITF needs several oracles rather than one:

- **Schema oracle:** rejects underspecified records.
- **Conversion oracle:** compares a conversion with the declared mapping function.
- **Causal oracle:** checks partial-order constraints.
- **Replay oracle:** compares reconstructed state with expected state.
- **Provenance oracle:** verifies derivation completeness.
- **Rights oracle:** detects capability expansion beyond the token grant.
- **Reconciliation oracle:** verifies that all contradictions and residuals are reported.
- **Narrative oracle:** checks fictional outcomes against declared canon rules.

Consistency models can be defined as sets of legal histories; Jepsen’s approach records operation histories and checks them against a model, while fault-injection tests can introduce clock skew, network partitions, crashes, and Byzantine behavior. TITF should borrow this history-and-checker pattern without assuming that linearizability is the correct oracle for every temporal domain.[^14][^15][^16]

## Experimental suites

### Suite A: One-hour block

Define a closed-open interval \(

- 1:1 continuous time;
- 10:1 accelerated simulation;
- 1:4 slowed simulation;
- pause from reference minute 15 through 45;
- event-driven progression;
- backward local-clock fold;
- branch at reference minute 30.

Inject boundary events, long-running events that cross a boundary, identical local labels for different instants, observation delay, and a ruleset change announced after it takes effect. The pass condition is not identical local output. The pass condition is correct mapping, explicit ambiguity, preserved causal order, and reproducible interval membership under each named interpretation.

### Suite B: Century ledger

The century experiment must use a **bounded synthetic fictional corpus**, not invented real-world historical data. Create territories with known ground truth and inject:

- clock-offset and daylight-style changes;
- a skipped local date;
- a repeated hour;
- rate changes and pauses;
- unauthorized local practice;
- missing transition records;
- delayed decrees;
- forged authority signatures;
- rollback, branch, and merge events;
- reinterpretations that do not alter the underlying event;
- genuine fictional history alterations under declared rules.

The acquisition token should initially grant query and audit rights only. The test should measure whether the system identifies all changes present in the corpus, distinguishes authorized from actual adoption, preserves disputed alternatives, and refuses to claim completeness outside the corpus. The real-world IANA limitations demonstrate why corpus-bounded completeness is essential.[^8]

### Suite C: Light and observation

Model two locations separated by a declared distance with a fixed propagation rule. Record occurrence time at the source, emission time, path, arrival time, observation time, and record time. NASA’s explanation that distant observation is observation of earlier emitted light provides the established analogue.[^5]

Then run three separate speculative interventions:

1. Change the **unit definition** while leaving propagation untouched.
2. Change the **propagation law** after a boundary event.
3. Change the **historical record** while leaving events and signals untouched.

A fourth intervention may alter fictional history, but only after choosing mutable-single-history, branching-history, or fixed-point rules. The test fails if these four operations become indistinguishable in the ledger.

### Suite D: Temporal jurisdiction

Move an entity through nested temporal domains: planetary civil jurisdiction, spacecraft proper-time regime, transit coordinate frame, accelerated virtual environment, and return jurisdiction. NIST’s coordinate-time work supports the underlying need for mappings among local clock rates and shared coordinate frameworks in space operations.[^7]

Test which authority governs contracts, aging claims, deadlines, event inclusion, and evidence retention at each boundary. Conflicting authorities should generate a jurisdiction dispute object, not an automatic global answer.

### Suite E: Adversarial Time War

Red-team the model with:

- clock spoofing;
- timestamp replay;
- forged conversion tables;
- ambiguous-hour arbitrage;
- branch laundering;
- retroactive authority claims;
- censorship of observation records;
- precision inflation;
- uncertainty deletion;
- causal-edge insertion;
- denial of historical ruleset versions;
- tokens that claim undeclared powers.

Property-based testing is appropriate for generating large numbers of temporal operation sequences against formal properties, and published work has specifically connected property-based testing with temporal formal models such as TLA+.[^17][^18] Fault injection should target both system mechanics and governance metadata.

## Metrics

| Metric | Definition | Desired direction |
|---|---|---|
| Event recovery | Qualifying injected events correctly identified | Higher |
| False reconciliation | Contradictory histories incorrectly collapsed | Lower |
| Provenance completeness | Derived claims with complete lineage | Higher |
| Mapping reproducibility | Repeated conversions producing identical bounded results | Higher |
| Ambiguity detection | Injected folds, gaps, and non-mappings surfaced | Higher |
| Causal violation count | Accepted outputs violating declared dependencies | Zero unless authorized |
| Uncertainty loss | Outputs more precise/confident without evidence | Zero |
| Token overreach | Actions permitted beyond enumerated rights | Zero |
| Branch leakage | Unauthorized cross-branch effects | Zero |
| Reconstruction fidelity | Replayed state matching known corpus ground truth | Higher |
| Dispute preservation | Material dissent retained after canonical decision | Complete |
| Coverage | Required model dimensions and risk combinations exercised | Higher |

No single aggregate “temporal accuracy score” should hide failures. Safety-critical invariants such as provenance continuity, token non-expansion, and branch isolation should be pass/fail gates.

## Research phases

### Phase 0: Canon decisions

Before implementation, settle:

- Whether a privileged reference clock exists.
- Whether the past is immutable, mutable, branchable, or model-dependent.
- Whether speculative retrocausality is allowed.
- Whether observers can retain memories across rollback or branch replacement.
- Whether clocks, bodies, computation, and legal effects can progress at different rates.
- Which authorities can observe, map, canonicalize, traverse, and alter.
- What “purchase” means for every temporal asset class.
- Which invariants survive every fictional power.

### Phase 1: Ontology and schema

Produce controlled vocabularies for time domains, event claims, evidence, mappings, changes, disputes, rights, and jurisdictions. Publish JSON Schema or an equivalent formal schema, plus example valid and invalid records. Align provenance fields where practical with W3C PROV.[^12]

### Phase 2: Reference model

Implement a deterministic graph engine with versioned mappings, append-only claims, branch support, causal constraints, and point-in-time reconstruction. The reference model is the oracle; it is not yet the final production architecture.

### Phase 3: Deterministic scenarios

Execute the one-hour, century, light-propagation, jurisdiction, and Time-War suites using fixed fixtures with known outcomes. Every failed invariant must produce a minimal counterexample and a trace of the responsible rule applications.

### Phase 4: Generated testing

Add property-based sequence generation, mutation testing, and adversarial fault injection. Formal temporal models can guide property generation and help expose combinations not anticipated by hand-authored cases.[^17][^19]

### Phase 5: Multi-contributor challenge

Give each contributor the same schema, canon rules, fixture corpus, and questions. Require machine-checkable outputs where possible. Compare disagreements at the level of assumptions, transformations, evidence use, and unresolved residuals—not prose preference.

### Phase 6: Canon integration

Only after testing should findings be translated into project canon, governance instruments, narrative rules, or implementation requirements. Preserve experimental results and dissenting interpretations as provenance for later revisions.

## Minimum deliverables

A complete first implementation package should contain:

- Temporal ontology and glossary.
- Event Claim Record schema.
- Clock and mapping schema.
- Temporal change taxonomy.
- Token-rights capability matrix.
- Reconciliation protocol.
- Formal invariants and test oracles.
- Deterministic fixture corpus.
- One-hour, century, light, jurisdiction, and adversarial test specifications.
- Expected-results files.
- Coverage and metrics plan.
- Canon-decision register.
- Assumption, uncertainty, and unresolved-dispute register.

## Independent recommendation

Adopt **“claims are immutable; interpretations and canonical status are versioned”** as the baseline engineering rule. This does not force the fictional universe itself to have an immutable past. It ensures that even when the fiction permits altered history, the research system retains evidence of what was asserted, observed, believed, changed, and authorized in each branch.

Use a temporal graph rather than one master chronological table. Make causal order, clock coordinates, observer knowledge, governance decisions, and branch membership separate dimensions. This preserves the strongest insight from the contributor set: temporal reconciliation should maximize consistency and explainability **without manufacturing certainty**.

The immediate next build should be Phase 0 through Phase 2: a canon-decision register, formal ontology, schemas, invariants, and deterministic reference model. Only then should the full scenario campaign begin; otherwise, divergent results will mainly reveal that contributors silently chose different meanings for “time,” “event,” “purchase,” “change,” and “history.”

---

## References

1. [Temporal Tables - SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal/overview?view=sql-server-ver17) - A system-versioned temporal table is a type of user table designed to keep a full history of data ch...

2. [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) - Capture all changes to an application state as a sequence of events.

3. [[PDF] Time, clocks, and the ordering of events in a distributed system](https://amturing.acm.org/p558-lamport.pdf)

4. [Time, Clocks and the Ordering of Events in a Distributed ...](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/) - Jim Gray once told me that he had heard two different opinions of this paper: that it’s trivial and ...

5. [What Is a Light-Year?](https://spaceplace.nasa.gov/light-year/en/) - A light-year is the distance light travels in one Earth year. Learn about how we use light-years to ...

6. [Mise en pratique - second - Appendix 2 - SI Brochure](https://www.bipm.org/documents/20126/41489667/SI-App2-second.pdf/3c76fec8-04d9-f484-5c3c-a2e280a0f248) - The definition of the second should be understood as the definition of the unit of proper time: it a...

7. [A relativistic framework to establish Coordinate time on the ...](https://www.nist.gov/publications/relativistic-framework-establish-coordinate-time-moon-and-beyond) - by N Ashby · 2024 · Cited by 3 — Using this framework, we also calculate the clock rates at earth-mo...

8. [Theory and pragmatics of the tz code and data](https://data.iana.org/time-zones/theory.html)

9. [second](https://www.bipm.org/en/si-base-units/second) - The second, symbol s, is the SI unit of time. It is defined by taking the fixed numerical value of t...

10. [RFC 3339 - Date and Time on the Internet: Timestamps](https://datatracker.ietf.org/doc/html/rfc3339) - This document defines a date and time format for use in Internet protocols that is a profile of the ...

11. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339.html)

12. [PROV-O: The PROV Ontology - W3C](https://www.w3.org/TR/prov-o/)

13. [PROV-DM: The PROV Data Model - W3C](https://www.w3.org/TR/prov-dm/)

14. [Consistency Models - Jepsen](https://jepsen.io/consistency/models)

15. [Tendermint 0.10.2](https://jepsen.io/analyses/tendermint-0-10-2)

16. [jepsen/README.md at main · jepsen-io/jepsen](https://github.com/jepsen-io/jepsen/blob/main/README.md) - A framework for distributed systems verification, with fault injection - jepsen-io/jepsen

17. [[1705.10032] From Temporal Models to Property-Based Testing - arXiv](https://arxiv.org/abs/1705.10032) - This paper presents a framework to apply property-based testing (PBT) on top of temporal formal mode...

18. [[PDF] From Temporal Models to Property-based Testing - SciTePress](https://www.scitepress.org/papers/2017/63403/63403.pdf)

19. [Specification-Based Testing with Linear Temporal Logic](https://repository.upenn.edu/items/4719153b-b0ce-488c-9440-8269983c6e10) - This paper considers the specification-based testing in which the requirement is given in the linear...

