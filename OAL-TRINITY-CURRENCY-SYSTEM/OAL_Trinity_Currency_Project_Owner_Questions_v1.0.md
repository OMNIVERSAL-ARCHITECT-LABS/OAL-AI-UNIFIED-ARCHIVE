# OAL Trinity Currency Laboratory - Project Owner Questions, Decisions, and Next-Step Recommendations

**Consolidated multi-AI collaboration record | Version 1.0 | 7 November 2026**

> **Purpose.** This document consolidates the questions that require project-owner direction, separates those decisions from technical work the AI collaborators can resolve independently, and records recommended next steps for versioning and traceability.

> **Response flexibility.** Any question may be answered with a selection, a plain-language explanation, “undecided,” “test both,” “use the recommended default,” or “leave this to the contributors.” None of these answers automatically creates canon.

## Executive status

- Cycle 1A - Exploratory capability modeling: completed.
- Cycle 1B - Reproduction and adversarial checker audit: in progress.
- Formal owner-adopted shared run: not yet authorized.
- Physical or external QC validation: not performed.
- Canon adoption: none.

The documentation and contributor coverage have improved, and the published implementations are reproducible under the tested environments. The project is not fully reconciled: checker-adequacy gaps, authority rules, identifier governance, partial-delivery recovery, and instrument-retention standards remain open.

## Part I - Priority owner questions

### Q1. Intended Quantum Credit capability

What must a successful Quantum Credit ultimately accomplish? Select or describe the intended minimum: (A) determine or represent a target-relative value; (B) make required resources or purchasing capability available; (C) obtain access, rights, or another defined outcome involving the target; (D) directly establish the requested target state within the fictional or simulated framework; or (E) preserve several of these as separately tested candidate architectures.

**Recommended default:** Preserve the ambitious design objective while retaining evaluation-only configurations as controls. An answer of “test multiple architectures” is sufficient.

### Q2. Authorization for the next phase

What work do you authorize next: continued independent exploratory work, one shared frozen run packet, or both with the results labeled separately? If a shared packet is authorized, which named packet and revision should be owner-adopted?

**Recommended default:** Authorize both tracks. Adopt a small, revision-specific shared packet for reproducibility while allowing independent experiments to continue.

### Q3. Instrument-retention standard

What may justify retaining 1COIN or NCOIN: strict mechanical necessity, operational advantages such as separation of duties and audit clarity, narrative/worldbuilding value, or a disclosed combination?

**Recommended default:** Evaluate mechanical necessity, operational advantage, and narrative value separately. Do not describe narrative retention as mechanical indispensability.

### Q4. Creation authority

Should creation require a distinct issuance authority such as AUTH_MINT? Should authority to take existing units, issue new units, deliver them to a recipient, and alter a simulated environment be treated as separate permissions?

**Recommended default:** Test separate authority profiles before selecting a permanent rule. Do not treat A’s consent over existing units as automatically deciding authority to create new units.

### Q5. Meaning of usable delivery

When B receives units, what must be true for delivery to count as successful? Is a correct balance sufficient, or must units also be valid, identifiable, correctly typed, unencumbered, permitted, and usable for a further operation?

**Recommended default:** Require genuine usability under the declared configuration; let the technical team propose the exact checks.

### Q6. Partial-delivery recovery

If two of three units are delivered and execution stops, should retry resume the remainder, roll back and restart, preserve a terminal partial result, reject retry, use a compensating transaction, or compare these as alternative policies?

**Recommended default:** Compare alternatives initially. Duplicate suppression should not silently choose the recovery policy.

## Part II - Additional owner questions

### Q7. Shortfall classification

When A holds two units but a named-source operation requires three, should the result be REJECTED_INSUFFICIENT, INCOHERENT_TARGET, or a multi-field result separating request coherence, feasibility, execution status, and reason?

**Recommended default:** Use separate fields: request_coherence, feasibility_under_configuration, execution_status, and reason.

### Q8. Request identity and replay

What counts as the same request: the same transaction ID, the same immutable payload, or the same underlying obligation even under a new ID? Should reuse of an ID with a changed payload be prohibited?

**Recommended default:** Bind each request ID to a canonical payload hash and distinguish same-ID replay from new-ID repetition.

### Q9. Receipt meaning and timing

Should a receipt certify only final completion, or may it represent intermediate milestones? If intermediate records are permitted, should they be named differently from 1COIN or a final settlement certificate?

**Recommended default:** Use request-scoped receipts and ordered events. Final settlement certification should occur only after completion.

### Q10. Blind and open review design

Should future rounds collect first-pass submissions before reference results are disclosed, conduct open challenge rounds, or use both as separately labeled stages?

**Recommended default:** Use both: staged blind submission followed by open adversarial review. The current round is reference-exposed and should remain labeled exploratory/non-blind.

### Q11. Identifier standard

May the team preserve original contributor IDs while using a three-level comparison structure: Case ID, Configuration ID, and Run ID, with neutral aliases only after equivalence is checked?

**Recommended default:** Approve the three-level structure and preserve original identifiers as aliases.

### Q12. Status and evidence vocabulary

Do you prefer a compact shared status set (PROPOSED, OWNER-ADOPTED, LOCKED FOR NAMED RUN, EXECUTED, SUPPORTED WITHIN NAMED RUN, CANON) with a separate evidence field (E0 STIPULATED, E1 DERIVED, E2 EXECUTED, E3 EXTERNAL)?

**Recommended default:** Keep design/adoption status separate from evidence level. Prefer SUPPORTED WITHIN RUN over wording that could imply physical validation.

### Q13. Executable-code expectation

Must every future run include executable code and machine-readable output, or may analytical traces remain sufficient for some cases?

**Recommended default:** Require code only when transition rules are fully computational; permit clearly labeled analytical traces for non-computational boundary cases.

### Q14. Model and exposure disclosure

Should contributors disclose underlying model/platform information and prior exposure to reference outputs? Should overlapping model families merely be disclosed or formally down-weighted?

**Recommended default:** Require disclosure. Avoid formal weighting until a defensible method is adopted.

### Q15. Publication preparation authority

May the team prepare a document manifest, access index, Markdown companions, corrected publication editions, and a correction log while preserving untouched originals?

**Recommended default:** Authorize preparation for review; treat repository commits, renames, moves, and deletions as separate actions.

### Q16. Reference-material handling

Should completed public reference materials remain online for transparency while new blind materials are privately staged, or should historical references be moved into a clearly marked post-disclosure area?

**Recommended default:** Keep historical artifacts available and clearly labeled; control pre-submission distribution for genuinely blind future rounds.

### Q17. Excluded assumptions and speculative track

Are there conventional assumptions the resource-box models must not impose universally, such as conservation, seller requirements, consent, stable unit identity, or ordinary time ordering?

**Recommended default:** Name protected assumptions explicitly and test changed premises as separate configurations rather than retroactively altering earlier runs.

### Q18. Next discriminating focus

After verification hardening, should the next shared work emphasize P3-Enact observability and resource identity, 1COIN ablation, NCOIN trigger falsification, or another priority?

**Recommended default:** Complete checker hardening first, then run P3 observability and 1COIN ablation before broad Cycle 2 claims.

## Part III - Items the AI team should resolve without burdening the project owner

- Publish corrected v0.2 implementations as new artifacts while preserving all v0.1 originals and the Perplexity audit.
- Derive totals from authoritative holdings; independently verify debits, credits, delivery quantity, authority, and settlement.
- Use request-scoped receipts and append-only ordered events; remove global receipt flags and hard-coded quantity thresholds.
- Add deliberate mutation testing and report mutation-detection coverage separately from ordinary assertion counts.
- Bind request IDs to immutable payloads; distinguish same-ID replay, changed-payload conflict, and new-ID repeated demand.
- Strengthen Perplexity completion checks for type, encumbrance, identity, provenance, recipient, uniqueness, and usability.
- Create a commit-pinned Markdown access index and manifest; provide Markdown/text companions for major binary reports.
- Inspect hyperlink targets, not only visible text, and remove temporary signed URLs from corrected publication editions.
- Resolve artifact-presence disputes against one named repository commit and path rather than relying on prior session memory.
- Keep analytical, executed, externally validated, blind, non-blind, and reference-exposed results explicitly separated.

## Part IV - Recommended immediate sequence

1. Record the project owner’s answers, including undecided and test-both responses.
2. Freeze one revision-specific shared Run Card without canonizing currency mechanics.
3. Publish v0.2 verification-hardening packages and retain v0.1 plus the audit unchanged.
4. Conduct a challenge round focused on checker adequacy, partial delivery, replay, receipt timing, and usable delivery.
5. Only after hardening, begin broader P3-Enact observability and 1COIN/NCOIN ablation work.
6. Publish an access index, manifest, correction log, and Markdown companions using commit-pinned references.

## Part V - Low-burden response template

- **Q1 - Intended Quantum Credit capability:** 
- **Q2 - Authorization for the next phase:** 
- **Q3 - Instrument-retention standard:** 
- **Q4 - Creation authority:** 
- **Q5 - Meaning of usable delivery:** 
- **Q6 - Partial-delivery recovery:** 
- **Q7 - Shortfall classification:** 
- **Q8 - Request identity and replay:** 
- **Q9 - Receipt meaning and timing:** 
- **Q10 - Blind and open review design:** 
- **Q11 - Identifier standard:** 
- **Q12 - Status and evidence vocabulary:** 
- **Q13 - Executable-code expectation:** 
- **Q14 - Model and exposure disclosure:** 
- **Q15 - Publication preparation authority:** 
- **Q16 - Reference-material handling:** 
- **Q17 - Excluded assumptions and speculative track:** 
- **Q18 - Next discriminating focus:** 

## Source basis

- ChatGPT collaboration response and verifier self-audit.
- Claude AI response and confirmation of receipt, replay, and recovery gaps.
- Google Gemini response and proposed Cycle 2 transition questions.
- Microsoft 365 Copilot review and 18-question owner-decision list.
- Grok review and consolidated owner questions.
- Perplexity AI owner-question consolidation and technical cautions.
- OAL_Perplexity_Claude_ChatGPT_Code_Audit_2026-11-07.txt and .json.
- AI Collaborator GitHub Access, Troubleshooting, and questions.docx.

---

**Scope statement:** All findings concern stipulated models, analytical reasoning, and executed simulations. No document in this record establishes physical Quantum Credit capability or canon.