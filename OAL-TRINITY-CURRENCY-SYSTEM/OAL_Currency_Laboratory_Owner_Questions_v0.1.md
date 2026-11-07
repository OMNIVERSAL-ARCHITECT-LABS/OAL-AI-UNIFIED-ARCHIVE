# OAL Currency Laboratory — Consolidated Owner Questions and Next-Step Items

**Document ID:** OAL-CURR-OWNER-QUESTIONS-v0.1  
**Date:** 7 November 2026  
**Status:** For project-owner review / Pre-Canon  
**Prepared for:** Nathan Lewis II (Project Owner)  
**Source:** Synthesized from collaboration responses of ChatGPT, Claude, Gemini, Microsoft Copilot, Perplexity, and Grok  

**Purpose:** Provide a single, versioned list of decisions and clarifications needed from the project owner so the laboratory can proceed without another full charter cycle. You are not required to answer every item. Answers of “undecided,” “test both,” “leave to the team,” or “recommend a default” are useful and sufficient.

---

## Priority Questions (highest leverage)

These four items, if addressed, give the strongest guidance for the next cycle.

### Q1. Minimum intended capability of a successful Quantum Credit
What do you ultimately want a Quantum Credit to accomplish?

- A. Evaluate / represent the target’s equivalent value  
- B. Make the required resources or purchasing capability available  
- C. Obtain access, rights, or another defined outcome involving the target  
- D. Directly establish the requested target state  
- E. Keep several of these as separate candidate architectures (recommended default by multiple members)

**Why it matters:** Evaluation-only models can be internally coherent while still falling short of an original design intention that required delivery or enactment.

### Q2. Formal adoption of a named Pilot 001 run card
Would you like to formally adopt one specific run-card configuration as a shared experimental benchmark?

Options:
- Adopt one existing packet (name which one)
- Direct the team to prepare a small harmonized run card for your review
- Allow multiple parallel run cards to remain exploratory for now
- Undecided / continue exploratory only

Until an adoption record exists, every package correctly remains PROPOSED.

### Q3. Authority over resource creation
If QC creates new units without taking them from an existing owner, should creation require:

- Authorization from a system issuer (AUTH_MINT or equivalent)
- Authorization from the requester
- No external authorization beyond the request itself
- Separate authority profiles tested as explicit configurations (recommended by several members)

### Q4. What can justify retaining 1COIN and NCOIN
Must each instrument demonstrate strict mechanical indispensability, or are the following also acceptable grounds for retention?

- Operational advantages (separation of duties, clearer auditing, reliability)
- Narrative / worldbuilding value
- Some combination, with the reasons disclosed

---

## Additional Owner Questions

### Capability, classification, and recovery
5. **Shortfall classification** (A holds 2, named-source request requires 3): Prefer REJECTED (insufficient resources), INCOHERENT_TARGET, or two separate fields (e.g., execution_status + target_validity / feasibility)?

6. **Partial-delivery recovery policy:** After a request delivers only part of the quantity, should a retry:
   - Resume the remaining units
   - Roll back and start clean
   - Preserve the partial result as terminal and require a new request
   - Reject the retry under the same ID
   - Be tested as alternative configurations

7. **Meaning of usable delivery:** When B receives three units, is success simply the correct balance, or must the units also be valid, identifiable, unencumbered, and usable for a further operation?

### Process and comparison rules
8. **Future review protocol:** For subsequent rounds, do you want reference results withheld until independent first-pass submissions are collected (staged disclosure), open challenge rounds, or both labeled separately?

9. **Shared vs independent experiments:** Continue both a shared frozen benchmark and independently designed experiments, with results labeled separately?

10. **Identifier scheme:** Prefer contributor-qualified IDs, Gemini’s LAB-F series, Copilot’s neutral IDs, or a minimal three-part scheme (Case ID + Configuration ID + Run ID)?

### Repository and publication
11. **Access index / manifest:** Authorize preparation of a lightweight Markdown access index and document manifest for the currency folder (contributor, title, revision, Raw URL, text companion available)?

12. **Status vocabulary:** Is a compact shared set acceptable (PROPOSED / OWNER-ADOPTED / LOCKED FOR NAMED RUN / EXECUTED / SUPPORTED WITHIN NAMED RUN / CANON) plus a separate evidence field (E0 STIPULATED / E1 DERIVED / E2 EXECUTED / E3 EXTERNAL), or keep existing per-package language for now?

### Additional items raised
13. **Receipt scope:** Should a receipt certify only final completion, or may intermediate milestones be recorded (and if so, under a different name than final settlement / 1COIN)?

14. **Model-family disclosure:** Should team members continue to disclose the underlying model family used in a session (as Perplexity did)?

15. **Assumptions the laboratory must not silently impose:** Are there any conventional assumptions (conservation, unit identity, seller requirement, etc.) that you want the laboratory to challenge in a designated speculative track rather than treat as background?

---

## Next-Step Recommendations (team-executable without further owner decisions)

These do not require your answers and can proceed in parallel:

- Strengthen verification layers: derive totals from holdings, validate debits/credits/authority independently of status strings, add request-scoped receipts and ordered event logs, and include deliberate-defect injection in reference models.
- Publish corrected v0.2 models and checkers alongside (not replacing) the original v0.1 artifacts.
- Preserve the Perplexity checker audit as a formal research artifact.
- Add Markdown companions or raw-text editions for key binary documents where useful.
- Maintain contributor attribution and original documents; add a coordination layer rather than forcing architectural merger.
- Record current Cycle 1 work as exploratory / reference-exposed rather than blind.

---

## How to respond

You may answer only the priority items (Q1–Q4) or any subset. Partial answers, “test both,” “undecided,” or “recommend a default and proceed” are all useful. The laboratory will treat any explicit adoption or clarification as an owner decision and will leave unaddressed items open or under explicit alternative configurations.

**End of consolidated owner questions list — v0.1**
