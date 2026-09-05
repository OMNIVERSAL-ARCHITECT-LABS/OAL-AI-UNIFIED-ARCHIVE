# Open Window Doctrine
## Implementation Memorandum for Decision Record & Architecture Update v0.3

**Document status:** Working implementation memorandum for review  
**Date:** 2026-08-14  
**Authority model:** Originator plus defined review group  
**Purpose:** Implement the edits and revisions recommended after review of the v0.3 Decision Record & Architecture Update, reconcile the document with the currently locked baseline, and define the remaining items that should be resolved before MVP execution. [file:38][file:39]

This memorandum treats the v0.3 Decision Record as the active working baseline because it explicitly locks the three previously disputed decisions on MVP timing, interface architecture, and manifestation handling, and states that those decisions supersede conflicting language in Draft Pass 0.2 and earlier materials. [file:38][file:39] It also preserves the stronger methodological gains from Draft Pass 0.2, including simulation-only safety, credibility-oriented thinking, and gate-based progression, while clarifying where v0.3 changes the governing definitions. [file:33][file:38][web:40][page:1]

## Executive summary

The v0.3 Decision Record is strong enough to serve as the governing baseline for immediate MVP scenario-card development. [file:38][file:39] Its best improvements are the explicit closure of the three architectural disputes, the broadened definition of interface vectors beyond screens and engineered objects, the demotion of Interface Airlock from a default architectural assumption to an optional containment control, and the replacement of “infection” as the top-level technical term with **Cross-Environment Transfer Event (CETE)**. [file:38][file:39]

Before MVP execution begins, however, four additional governance and control items should be locked: the exact ONESTAMP trigger, the composition and authority of the review group, the handling protocol for a Candidate Interface Event discovered during MVP, and a mandatory scenario-card schema that operationalizes the v0.3 baseline in a consistent way. [file:38][file:39] These additions are justified by established modeling-and-simulation credibility guidance, which requires defined acceptance criteria and disciplined product use, and by systems-security engineering guidance that treats trustworthiness and resilience as engineered properties requiring explicit decision structures and recovery rules. [web:40][web:41][web:42][web:50]

## Governing baseline

The following v0.3 decisions are already locked and should be treated as non-negotiable unless directly amended by a later originator decision record. [file:38][file:39]

| Locked area | Governing v0.3 rule | Implementation consequence |
|---|---|---|
| MVP timing | Flexible, exit-criteria-driven; 8–16 active hours is only a planning estimate [file:38] | No scenario may be called successful because time expired; advancement depends on gates and review. |
| Interface architecture | Window, aperture, and interface are provisional functional terms for any potential crossing vector [file:38] | MVP definitions must not assume screens are the only relevant vector class. |
| Airlock | Interface Airlock is optional and inserted deliberately; not a default property of every interface [file:38] | Scenario cards must state whether airlock is absent, present, or varied as a condition. |
| Manifestation handling | No single manifestation class is privileged; multiple classes and Unknown/Unclassified are allowed [file:38] | Every scenario must declare proxy class, while retaining MU and MX for unexpected results. |
| CETE terminology | CETE is the higher-level concept; infection is one possible subtype [file:38] | Protocol language should use CETE as the default term except where a specifically unwanted propagative subtype is intended. |

Draft Pass 0.2 remains a valuable engineering source, especially for its credibility framing, gate structure, telemetry logic, BTEC decomposition, and replay/recurrence discipline. [file:33] NASA’s current modeling-and-simulation standard is a good fit for keeping those strengths, because it emphasizes defined acceptance criteria, lifecycle discipline, and credibility assessment for model products and their use. [web:40][web:42] NIST’s cyber-resiliency guidance also supports retaining explicit trust boundaries, recovery logic, and resilience-oriented containment thinking rather than relying on intuitive or ad hoc interpretations. [web:41][web:50]

## Implemented revisions

### 1. Make the review group explicit

The project now has a defined authority model: **originator plus defined review group**. This should be written into the baseline rather than left implicit in conversation history, because v0.3 currently names the originator and ONESTAMP status but does not define the review body that participates in MVP advancement decisions. [file:38][file:39]

**Recommended implementation language:**  
The Open Window MVP operates under a dual authority model. Nathan Lewis II remains originator and final ratification authority. A defined review group conducts structured review of scenario cards, pilot findings, gate completion, exception handling, and readiness for ONESTAMP recommendation. The review group may recommend approval, revision, rescheduling, hold, or escalation; final ONESTAMP authority remains with the originator unless separately delegated. [file:38][file:39]

This edit is important because NASA-STD-7009B requires that acceptance criteria be defined and approved by the appropriate technical authority, which means the project should state who reviews evidence and who can accept or reject a model product for its intended use. [web:40] It also aligns with NIST’s view that trustworthiness depends on explicit governance and engineered decision structures, not informal assumptions about who is “probably” approving the work. [web:41][web:50]

### 2. Define the ONESTAMP trigger

v0.3 correctly says that ONESTAMP is still required for full ratification, but it does not specify when that threshold is reached. [file:38][file:39] Without that, the project still lacks a final acceptance rule.

**Recommended implementation language:**  
ONESTAMP recommendation becomes eligible only after: (1) all required MVP scenario cards are approved by the review group, (2) pilot gates are completed or explicitly classified as not met, (3) the after-action review is completed, (4) unresolved exception items are dispositioned, and (5) the review group submits a written recommendation to the originator. ONESTAMP is applied only by the originator after review of that recommendation. [file:38][file:39][web:40]

This preserves your authority while giving the review group a formal function. It also prevents premature ratification of a baseline that has never survived actual pilot execution or after-action review. [file:38][file:39]

### 3. Add an MVP exception-handling rule

The strongest unresolved operational gap in v0.3 is what to do if an apparent undeclared vector appears during the MVP, given that Candidate Interface Event discovery is reserved for later campaigns. [file:38][file:39] The current baseline defines the concept well, but it does not tell operators how to behave when one appears.

**Recommended implementation language:**  
If an apparent undeclared interface/vector, unexplained correlation, or anomalous crossing appears during MVP execution, the event is initially classified as a **Candidate Interface Event** and assigned a unique event ID. The run does not automatically promote the event to a verified interface, CETE, or doctrine-level finding. Operators must preserve raw telemetry, record timing and lineage context, and apply the scenario’s stop-condition rule if thresholds are met. The event is dispositioned after the run as one of four statuses: instrumentation anomaly, unresolved candidate, candidate requiring replay, or candidate cleared for later campaign investigation. Promotion requires the v0.3 conditions of independent observation, replay, independent recurrence, and, where possible, intervention testing. [file:38][file:39]

This implementation is consistent with the existing v0.3 definition and also with Draft Pass 0.2’s insistence that one-off anomalies should not be promoted to doctrine-level findings without replay and independent recurrence. [file:33][file:38]

### 4. Standardize proxy-class declaration

v0.3 requires each controlled test to declare the proxy class it uses, but it does not yet give a standard mapping rule. [file:38][file:39] Without a mapping convention, different contributors may label the same proxy inconsistently.

**Recommended implementation language:**  
Each MVP scenario card shall declare one or more engineered proxy classes before execution. The declared class identifies the intended observable mode, not the assumed metaphysical truth of the phenomenon. Suggested MVP mapping guidance is as follows:

| Proxy example | Default class code | Notes |
|---|---|---|
| Checksum drift, injected metadata token, message-state discrepancy | M1 Informational or M2 System/state [file:38] | Use M1 when content/information is primary; M2 when system state is primary. |
| Harmless color change, bounded temperature variable, synthetic ambient shift | M3 Environmental [file:38] | Use only within safe engineered limits. |
| Scripted attention shift, behavioral flag, movement response | M4 Behavioral/agent-mediated [file:38] | Must be explicitly scripted or safely induced in simulation only. |
| Process token, daemon-like simulated persistence, controlled service handoff | M5 Entity/process-mediated [file:38] | Use for process persistence or nonhuman simulated mediation. |
| Deliberate cross-carrier transition across classes | MX Mixed/carrier-changing [file:38] | Especially useful in later campaigns. |
| Unexpected outcome outside declared model | MU Unknown/unclassified [file:38] | Apply post-observation only; do not predeclare as a routine MVP proxy class unless testing anomaly handling itself. |

This mapping rule preserves v0.3’s descriptive intent while creating practical consistency for the review group. [file:38][file:39]

### 5. Require a single scenario-card schema

v0.3 says each card must include setup, declared proxy classes, null hypothesis, controls, metrics, stop conditions, and replications. [file:38][file:39] That is good, but a fuller schema would reduce ambiguity during cross-platform review.

**Recommended mandatory MVP scenario-card fields:**
- Scenario ID and revision
- Scenario title
- Purpose / decision supported
- Declared Interface Object(s)
- Declared proxy class(es)
- Airlock condition: absent, present, or varied
- Exact setup and initial-state requirements
- Null hypothesis / falsification condition
- Positive control
- Negative control
- Primary metrics
- Secondary observations
- Stop conditions
- Required replications
- Replay requirement
- Independent recurrence requirement
- Data products to preserve
- Review-group disposition authority
- Post-run classification options: supported, inconclusive, falsified, blocked, deferred

This is consistent with both v0.3’s immediate next-step requirements and NASA’s emphasis on acceptance criteria, product traceability, and disciplined use of simulation outputs. [file:38][web:40][web:42]

## Recommended insertions into the architecture update

### Authority and review section

Add a short section after Status / Authority:

> **Review authority model**  
> The Open Window MVP is reviewed under an originator-plus-review-group model. The originator retains final ratification authority. The review group evaluates scenario-card completeness, gate completion, pilot findings, exception handling, and readiness for ONESTAMP recommendation. Review-group approval does not itself ONESTAMP the baseline; it produces a written recommendation to the originator.

### ONESTAMP section

Add a short section before Immediate Next Steps:

> **ONESTAMP recommendation threshold**  
> A recommendation for ONESTAMP may be made only after approved MVP scenario cards exist, pilot gates are dispositioned, after-action review is complete, unresolved exception items are logged and classified, and the review group has issued a written recommendation. Final ONESTAMP remains the originator’s decision.

### MVP exception handling section

Add a section under Implications for the MVP Pilot:

> **Candidate Interface Event handling during MVP**  
> If an undeclared or unexplained vector is suspected during MVP, the event is logged as a Candidate Interface Event, assigned a unique identifier, and preserved with raw telemetry. It is not promoted to a verified interface, CETE, or doctrine-level claim during the same run without the required promotion tests. The run proceeds, pauses, or terminates according to the scenario’s stop conditions and the review group’s exception-handling rule.

## Additional recommendations before moving forward

### Keep CETE as the default technical term

The shift from “infection” to **CETE** is one of the most important conceptual improvements in v0.3 because it prevents the framework from assuming that all crossings are harmful, propagative, or biologically framed. [file:38][file:39] This broader term supports observation, synchronization, disclosure, manipulation, and other subtypes without losing the option to classify a subset as infection when appropriate. [file:38][file:39]

### Preserve candidate discovery for later campaigns

v0.3 is correct to defer Candidate Interface Event discovery methodology until after baseline instrumentation is proven. [file:38][file:39] INACSL guidance on prebriefing and debriefing is useful here not as a physical-lab blueprint, but because it reinforces the value of clearly preparing participants, defining ground rules, and conducting a structured debrief before trying more ambiguous scenario types. [web:10][web:45][web:48][web:51]

### Do not weaken the replay and recurrence standard

Draft Pass 0.2’s replay and independent recurrence discipline should be preserved in the protocol documents even where v0.3 is the governing baseline. [file:33][file:38] NASA’s modeling-and-simulation guidance strongly supports traceability, explicit criteria, and disciplined use of simulation outputs, which makes replay and recurrence especially important when the doctrine allows candidate vectors that may sit outside the declared ontology. [web:40][web:42]

## Questions still worth resolving

The v0.3 document is strong, but these questions should be answered before MVP execution:

1. Who specifically sits on the defined review group, and what constitutes quorum for approving a scenario card or recommending ONESTAMP?  
2. Can the review group pause a pilot run on its own authority, or only recommend pause/escalation to the originator?  
3. What exact stop-condition threshold converts a Candidate Interface Event from “log and preserve” to “pause or terminate run”?  
4. Will MU be allowed only as a post-observation label, or can any dedicated anomaly-handling scenario deliberately exercise MU classification logic during MVP?  
5. What artifact becomes the single authoritative home for the executable scenario cards: a protocol document, a scenario packet, or a controlled annex to v0.3?  

## Immediate next-step recommendations

1. Issue a short v0.3.1 or implementation memo adopting the review-group model, ONESTAMP threshold, candidate-event handling rule, and mandatory scenario-card schema. [file:38][file:39]
2. Update Draft Pass 0.2-derived protocol language so it conforms to CETE terminology, optional airlock logic, and manifestation coding from v0.3. [file:33][file:38]
3. Draft the executable MVP scenario cards using the mandatory schema above. [file:38][file:39]
4. Conduct a structured review-group pass on those cards before pilot authorization. [file:38][web:10][web:45]
5. Only after that review, authorize MVP execution under the gate-driven timing rule and preserve full telemetry, replay, and recurrence discipline. [file:33][file:38][web:40][web:41]

## Proposed closing language

The Open Window Decision Record & Architecture Update v0.3 is sufficiently mature to function as the active working baseline for MVP preparation. [file:38][file:39] The project should now shift from definitional debate to controlled implementation by formalizing review authority, ONESTAMP thresholds, exception handling, and scenario-card structure, then moving directly into executable MVP card development under CETE-centered terminology and the locked architectural decisions. [file:33][file:38][web:40][web:41]
