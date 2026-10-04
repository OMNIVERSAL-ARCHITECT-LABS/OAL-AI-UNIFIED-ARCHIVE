# OAL / One Industries / Lewis Corp
# Documentation Governance, Design, Presentation, Format, and Publication Standard

**Document ID:** OAL-ONE-LC-DOC-STD-001  
**Version:** 0.1  
**Status:** PROVISIONAL DRAFT — NOT RATIFIED  
**Prepared by:** Perplexity AI — independent preparer  
**Preparation date:** 2026-10-04  
**Preparation timestamp:** 10:48 PDT (UTC−07:00)  
**Entity scope:** Omniversal Architect Labs (OAL), One Industries, and Lewis Corp; each remains separately identifiable  
**Document type:** Documentation governance and publication standard  
**Work type:** Governance standard; non-simulation  
**Distribution:** Collaborative workspace / GitHub publication candidate  
**Approval status:** Pending authorized human review and ratification  
**Canonical source:** This Markdown file after ratification; matching DOCX and PDF are publication derivatives  
**Required formats:** Markdown, DOCX, and PDF  
**Format status at preparation:** All three formats generated; validation status recorded in Section 19  
**Related broader topic:** Collaborative multi-AI documentation governance  

> **What this document is:** An independent, executable first draft of a standard for producing future documentation.
>
> **What this document is not:** It is not canon, ratification, legal advice, a legal instrument, a claim that any named organization or scenario has a particular real-world status, or evidence that any described project, entity, event, test, simulation, or outcome exists or occurred. It does not adopt itself on the user's behalf.

---

## Executive Summary

This standard establishes how documents for OAL, One Industries, Lewis Corp, and joint projects are commissioned, written, classified, designed, reviewed, exported, and published. Its governing rule is **purpose before production**: a document must support a defined decision, action, understanding, record, test, specification, review, or archival need. A file whose only result is that another file exists does not pass the publication gate.

The standard responds directly to a recurring presentation failure: documents composed primarily of large matrices, dense tables, and row-and-column layouts that are difficult for an ordinary reader to understand, especially on a phone. Future documents must use readable prose as the primary communication layer. Tables and figures support the narrative; they do not replace it. Significant exhibits receive stable item numbers, captions, sources, plain-language interpretations, and explicit references from the body.

Every substantive document must make its identity and boundaries visible near the beginning. The reader must be able to determine the responsible entity, preparer, purpose, audience, maturity, simulation status, evidence status, relationship to broader work, and what the document does not claim. OAL, One Industries, and Lewis Corp must not be blended into a single identity merely because a document mentions more than one of them.

The required publication package consists of substantively equivalent Markdown, DOCX, and PDF files. Markdown is the version-controlled canonical source unless a project expressly designates another accessible source. DOCX is the editable office derivative. PDF is the fixed-layout publication derivative. A preparer must never claim to have created a file that does not exist. Missing, failed, or unvalidated formats trigger the Format Failure and Recovery Protocol in Section 14.

The standard is proportional. A short decision record does not need the same volume of front matter as a major report. However, no substantive document may omit its purpose, entity identity, status, preparer, timestamp, boundaries, intended result, or format status. Section 2 establishes four document classes and their minimum obligations.

This draft synthesizes the strongest provisions in the collaboration transcript while correcting several overbroad proposals. In particular, it rejects a universal ban on body tables, rejects mandatory cover pages and executive summaries for every short record, separates lifecycle status from evidence status, and makes adoption a human governance decision rather than an AI declaration. The result is intended to be enforceable without becoming ceremonial bureaucracy.

---

## Table of Contents

- [1. Purpose and Authority](#1-purpose-and-authority)
- [2. Scope and Proportionality](#2-scope-and-proportionality)
- [3. Governing Principles](#3-governing-principles)
- [4. Purpose and Execution Test](#4-purpose-and-execution-test)
- [5. Identity, Classification, and Status](#5-identity-classification-and-status)
- [6. Reality, Simulation, and Claim Boundaries](#6-reality-simulation-and-claim-boundaries)
- [7. Required Document Architecture](#7-required-document-architecture)
- [8. Writing and Readability](#8-writing-and-readability)
- [9. Mobile-First Design](#9-mobile-first-design)
- [10. Tables, Figures, and Exhibits](#10-tables-figures-and-exhibits)
- [11. Accessibility and Resilience](#11-accessibility-and-resilience)
- [12. Sources, Evidence, and Provenance](#12-sources-evidence-and-provenance)
- [13. File Formats and Fidelity](#13-file-formats-and-fidelity)
- [14. Format Failure and Recovery](#14-format-failure-and-recovery)
- [15. Naming, Versioning, and Publication](#15-naming-versioning-and-publication)
- [16. AI Attribution and Collaboration](#16-ai-attribution-and-collaboration)
- [17. Quality Assurance and Acceptance](#17-quality-assurance-and-acceptance)
- [18. Exceptions and Governance](#18-exceptions-and-governance)
- [19. Independent Execution Validation](#19-independent-execution-validation)
- [20. Implementation Guide](#20-implementation-guide)
- [21. Collaboration Review](#21-collaboration-review)
- [22. Adoption and Next Actions](#22-adoption-and-next-actions)
- [Appendix A. Required Templates](#appendix-a-required-templates)
- [Appendix B. Compliance Checklists](#appendix-b-compliance-checklists)
- [Appendix C. Format Failure Notice](#appendix-c-format-failure-notice)
- [Appendix D. Document Architectures](#appendix-d-document-architectures)
- [Appendix E. Exhibits](#appendix-e-exhibits)
- [Appendix F. Style Specification](#appendix-f-style-specification)

---

## List of Exhibits

- **Table E.1 — Document Class Requirements.** Cited in Sections 2 and 7.
- **Table E.2 — Status and Classification Taxonomy.** Cited in Sections 5 and 6.
- **Table E.3 — Required Format Roles and Validation.** Cited in Sections 13 and 17.
- **Table E.4 — Publication Acceptance Gate.** Cited in Section 17.
- **Table E.5 — Council Response Assessment.** Cited in Section 21.
- **Figure E.1 — Document Lifecycle and Recovery Flow.** Cited in Sections 4, 14, and 20.

No chart is included because this standard contains no quantitative dataset for which a chart would improve comprehension. Decorative graphics are intentionally omitted.

---

## 1. Purpose and Authority

### 1.1 Purpose

This standard governs the creation, structure, presentation, classification, review, file delivery, maintenance, and publication of documents prepared for OAL, One Industries, Lewis Corp, and explicitly joint initiatives. It is designed to make future documentation clear, useful, traceable, accessible, and consistent across human and AI preparers.

The standard exists to change production behavior. It is not merely a visual style guide. It defines the minimum conditions under which a document may be represented as complete, reviewed, approved, or published.

### 1.2 Intended result

A preparer applying this standard should be able to determine:

- Whether a proposed document should exist.
- What the document is intended to accomplish.
- Which entity or entities it concerns.
- What status and evidentiary boundaries apply.
- Which sections and metadata are mandatory.
- How prose, data, tables, and figures should be presented.
- How the document should behave on mobile devices.
- Which files must be delivered.
- What to do when rendering or conversion fails.
- How to test whether the result is acceptable.

### 1.3 Authority

This version is a provisional independent draft. It has no binding force until accepted through the governance process in Section 18. No AI preparer may declare the standard ratified, canon, legally operative, or organizationally binding without explicit authorization from the designated human authority.

After ratification, the approved version governs prospectively. Previously approved documents are not automatically invalidated; they may be remediated according to risk, use, and maintenance priority.

### 1.4 Audience

Primary audiences include project collaborators, document preparers, AI systems, reviewers, repository maintainers, executive readers, technical readers, and general readers encountering the workspace for the first time.

### 1.5 Success criteria

This standard succeeds when future documents become easier to read, easier to classify, harder to misinterpret, simpler to validate across formats, and more useful for decisions or action. Success is not measured by page count, table count, visual complexity, or repository volume.

---

## 2. Scope and Proportionality

### 2.1 In scope

The standard applies to substantive reports, policies, specifications, research documents, simulation reports, charters, adversarial reviews, decision records, project memos, public GitHub publications, and multi-AI collaborative work products.

It also applies to material revisions of those documents and to publication packages derived from them.

### 2.2 Out of scope

Transient chat messages, informal brainstorming, commit messages, raw datasets, source code, issue comments, and private notes are not automatically full documents. When any of these is elevated into an official record or published work product, the applicable document class must be assigned and the corresponding requirements begin to apply.

### 2.3 Document classes

The standard uses four classes:

- **Class A — Short Record:** A concise memo, decision record, notice, or note, ordinarily one to three pages.
- **Class B — Standard Document:** A normal report, proposal, protocol, or specification.
- **Class C — Major Report:** A high-impact research, architecture, validation, policy, or governance document.
- **Class D — Technical Annex or Dataset Companion:** Highly structured support material that depends on a narrative parent document.

The specific obligations for each class are listed in **Table E.1, Document Class Requirements, in Appendix E**. The class system prevents the standard from turning a two-page record into a ceremonial major report.

### 2.4 Universal minimum

Regardless of class, every official document must include:

- A descriptive title.
- Entity scope.
- Document type and status.
- Purpose and intended result.
- Intended audience.
- Preparer identity.
- Date, time, and time zone.
- Reality, simulation, and non-claim boundaries where relevant.
- Version or stable revision identifier.
- Format status.
- A clear outcome, decision, next action, or statement that no further action is required.

---

## 3. Governing Principles

### 3.1 Purpose before production

Know why the document exists before designing it. If no meaningful outcome, record, decision, instruction, analysis, test, or preservation need can be named, the proposed document must be reconsidered.

### 3.2 Reader before layout

Design for the people who must use the information. A layout that looks sophisticated on a large monitor but fails on a phone is not successful.

### 3.3 Narrative before matrix

Explain the subject in ordinary prose before requiring the reader to decode structured data. Tables and figures may compress or support information; they must not become a substitute for communication.

### 3.4 Evidence before confidence

Language strength must not exceed the strength of the supporting evidence. “Observed,” “reported,” “calculated,” “simulated,” “estimated,” “assumed,” “proposed,” and “unknown” are not interchangeable.

### 3.5 Labels before assumptions

Entity identity, lifecycle status, simulation status, evidence status, and scope boundaries must be explicit. The reader must not be forced to infer whether a document is preliminary, approved, fictional, simulated, operational, or mixed.

### 3.6 Traceability before volume

A smaller document with clear sources, decisions, and relationships is often more useful than a large opaque document. Volume is not proof of rigor.

### 3.7 Accessibility by construction

Accessibility must be built into the source document, not deferred as cosmetic remediation. Section508.gov warns that remediation is rework and waste, and provides separate creation guidance for Word and PDF documents.[cite:4][cite:13]

### 3.8 Consistency without rigidity

Standardize what improves comprehension, attribution, fidelity, and archival continuity. Permit justified variation where the document type or audience requires it.

### 3.9 Fidelity across formats

Markdown, DOCX, and PDF versions must preserve the same substantive meaning, status, numbering, and decisions even when layout differs.

### 3.10 Execution before ceremony

The standard must help people perform work. Requirements that cannot be tested, do not serve readers, or create effort without value should be revised or removed.

---

## 4. Purpose and Execution Test

### 4.1 Required questions

Before drafting, the preparer must answer:

1. Why should this document exist?
2. What problem, question, decision, activity, record, experiment, requirement, or preservation need does it address?
3. Who must use or understand it?
4. What should the reader know, decide, perform, evaluate, reproduce, or verify?
5. What does the document actually accomplish upon publication?
6. What is outside its scope?
7. What does it not establish or claim?
8. Does it require a next action?
9. How will success be recognized?
10. Is a new document necessary, or should an existing document be revised?

### 4.2 Purpose types

The preparer must identify one or more purpose types:

- **Decisional:** Records or supports a choice.
- **Prescriptive:** Establishes a rule, requirement, or procedure.
- **Instructional:** Enables a task to be performed.
- **Analytical:** Evaluates evidence, alternatives, or implications.
- **Evidentiary:** Preserves observations, records, or validation results.
- **Experimental:** Defines or reports a test or simulation.
- **Exploratory:** Frames an unresolved question without implying closure.
- **Archival:** Preserves continuity or provenance.
- **Communicative:** Briefs a defined audience on relevant information.
- **Debate-initiating:** Deliberately opens a specified dispute or inquiry.
- **Classification:** Determines whether specified material is real-world, fictional, simulated, hypothetical, or otherwise bounded.

If debate or reality classification is not an explicit purpose, the document must not drift into arguing whether named organizations, scenarios, or constructs are “real.”

### 4.3 Execution status

Every project document must distinguish among:

- **Proposed:** Work has not begun.
- **In progress:** Work has begun but is incomplete.
- **Partially executed:** Some planned actions occurred.
- **Executed:** The defined activity occurred.
- **Verified:** Specified evidence was checked against stated criteria.
- **Validated:** The result was shown fit for a stated use under stated conditions.
- **Not applicable:** The document does not describe execution.

A plan must not be presented as execution. A simulation must not be presented as observation. A generated description must not be presented as a completed test.

### 4.4 Rejection rule

A document fails commissioning when it has no identifiable audience, no intended result, duplicates an existing controlled document without reason, or cannot state what changes because it exists. The proper response may be to revise an existing file, create a short record, add a repository issue, or take no documentation action.

### 4.5 Lifecycle

The lifecycle is shown in **Figure E.1, Document Lifecycle and Recovery Flow, in Appendix E**. A document moves from commission to classification, drafting, review, format generation, validation, acceptance, publication, maintenance, and eventual supersession or retirement. Format failure creates a recovery branch; it does not authorize a false completion claim.

---

## 5. Identity, Classification, and Status

### 5.1 Entity identity

Every document must identify one of the following entity scopes:

- Omniversal Architect Labs (OAL).
- One Industries.
- Lewis Corp.
- Joint or cross-organizational, with each participating entity named.
- External or comparative material.
- Unaffiliated conceptual material.

A joint label indicates shared relevance, not merger of identity, authority, or doctrine. Entity-specific rules must remain separately visible.

### 5.2 Separation of classification dimensions

Classification must not collapse unrelated concepts into one “status” field. At minimum, the metadata distinguishes:

- **Lifecycle status:** Draft, under review, approved, superseded, retired.
- **Maturity:** Concept, preliminary, provisional, developed, validated.
- **Work nature:** Operational, research, simulation, fictional, hypothetical, mixed.
- **Evidence status:** Observed, reported, calculated, simulated, estimated, assumed, synthetic, unknown.
- **Distribution:** Public, collaborative internal, restricted, archival.
- **Execution status:** Proposed, in progress, executed, verified, not applicable.

The controlled vocabulary and permitted combinations appear in **Table E.2, Status and Classification Taxonomy, in Appendix E**.

### 5.3 Visible label block

Class B and C documents must display the classification block on the first page or first mobile screen. Class A documents may use a compact version immediately under the title. Classification information must not appear only in a footer because assistive technologies and format conversion may not expose footer content reliably.

### 5.4 Controlled status words

Use status terms consistently:

- **DRAFT:** In preparation; not ready for decision.
- **UNDER REVIEW:** Submitted for structured review; not approved.
- **PROVISIONAL:** Usable within stated limits while material conditions remain unresolved.
- **APPROVED:** Accepted by the designated authority for the declared scope.
- **RATIFIED:** Formally adopted under an established governance mechanism.
- **SUPERSEDED:** Replaced by a named later version.
- **RETIRED:** No longer active and not replaced.
- **ARCHIVAL:** Preserved for historical reference.
- **FORMAT INCOMPLETE:** One or more required deliverables are missing or failed validation.

“Final” should be avoided as a lifecycle label unless the governance scheme defines it, because an approved document may still be revised or superseded.

### 5.5 Relationship metadata

Where applicable, identify:

- Parent document.
- Related documents.
- Supersedes.
- Superseded by.
- Depends on.
- Supports.
- Associated simulation.
- Associated dataset.
- Repository location.
- Broader topic or program.

---

## 6. Reality, Simulation, and Claim Boundaries

### 6.1 Required boundary statement

Every substantive document must include concise statements titled or labeled:

- **What this document is.**
- **What this document is not.**

These statements must be tailored to the actual document. Boilerplate that lists every possible disclaimer without relevance should be removed.

### 6.2 Simulation identification

Documents involving simulations, models, hypothetical scenarios, synthetic data, fictional constructs, computational exercises, or mixed reality status must declare:

- Simulation status: yes, no, or mixed.
- Simulation type and purpose.
- Input sources.
- Material assumptions.
- Execution status.
- Result type.
- Relationship to observed or real-world information.
- Limits on inference or application.

### 6.3 Result labeling

Each significant finding or number must remain identifiable as one or more of:

- Observed.
- User-provided.
- Externally sourced.
- Calculated.
- Simulated.
- Estimated.
- Assumed.
- Synthetic.
- Model-generated interpretation.
- Hypothesis.
- Unknown or contested.

Transforming or summarizing information must not erase its uncertainty or provenance.

### 6.4 Non-claim rule

A document must state what it does not claim when confusion is reasonably foreseeable. Depending on context, it may clarify that it is not legal, medical, financial, scientific, historical, organizational, or operational authority; not proof of existence or occurrence; not an endorsement; and not validation of a proposed system.

### 6.5 Neutrality rule

Boundary statements are mechanisms for clarity, not invitations to derail the document. Unless the declared purpose is to investigate reality status, the text must neither litigate nor presume the real-world or fictional status of OAL, One Industries, Lewis Corp, or any associated scenario.

---

## 7. Required Document Architecture

### 7.1 Core sequence

A Class B or C document should ordinarily use this sequence:

1. Title and document-control block.
2. What this document is and is not.
3. Executive summary.
4. Table of contents.
5. List of exhibits when the threshold in Section 10.8 is met.
6. Purpose and intended outcome.
7. Scope and audience.
8. Definitions when needed.
9. Main narrative.
10. Findings, decisions, requirements, or results as appropriate.
11. Limitations, risks, or open questions as appropriate.
12. Next actions or statement that no action is required.
13. Revision history.
14. Appendices and exhibits.

The architecture varies by document class and purpose. Refer to **Table E.1 in Appendix E** and the examples in Appendix D.

### 7.2 Executive summary

Class B and C documents require an executive summary. It must explain why the document exists, what was done or established, the most important result, unresolved matters, and what happens next. It must be understandable without reading the full document.

Class A documents use a one-paragraph summary or purpose/result statement rather than a separate executive summary. Class D material relies on the executive summary of its parent document and includes a short annex purpose statement.

### 7.3 Table of contents

Class B and C documents require a table of contents. DOCX must use true heading styles so the table can be generated or updated. PDF should include bookmarks when technically supported. GitHub renders a heading outline for Markdown files with multiple headings, but the source must still use a logical hierarchy.[cite:3][cite:8]

Class A documents do not require a table of contents unless navigation would materially improve use.

### 7.4 Heading hierarchy

Use a single document title, followed by major sections and subsections in logical order. Avoid skipping levels. Heading depth should ordinarily stop at the third body level; deeper nesting requires a clear reason.

### 7.5 Required closing

Every active project document must close with one or more of the following:

- Decision recorded.
- Requirements established.
- Recommendations.
- Next actions with ownership or routing.
- Validation requirements.
- Open questions.
- No further action required.

A generic “Conclusion” that merely repeats the introduction is not required.

---

## 8. Writing and Readability

### 8.1 Plain-language standard

Write for an informed general reader unless the document declares a specialized audience. Define necessary technical terms at first use. Prefer specific verbs and concrete statements over abstract corporate language.

### 8.2 Paragraph and sentence design

Use short to moderate paragraphs, usually one idea each. Vary sentence length, but split sentences that carry multiple independent requirements. Lists should clarify parallel items; they should not fragment a connected argument into dozens of isolated bullets.

### 8.3 Human-readable narrative

The main body must explain the topic as prose. A reader should be able to understand the purpose, reasoning, principal findings, and next action without reconstructing them from a table.

### 8.4 Claim discipline

Use terms accurately:

- “Is” for established conditions within the document's defined frame.
- “Was observed” for direct observation.
- “Was reported” for attributed external statements.
- “Was calculated” for derived values.
- “Was simulated” for model output.
- “Is assumed” for an input assumption.
- “May” for possibility.
- “Is proposed” for an unapproved design.
- “Remains unknown” when evidence does not support resolution.

### 8.5 Tone

Use direct, professional, non-adversarial language. Adversarial analysis may be rigorous without becoming mocking or combative. If the document's purpose is debate, identify the disputed proposition and rules of engagement.

### 8.6 Acronyms

Spell out an acronym at first use unless it is universally understood by the declared audience. Provide a glossary when numerous specialized terms are unavoidable.

### 8.7 Duplication

Do not repeat the same narrative in the executive summary, introduction, table, and conclusion. Each layer should serve a distinct function: orientation, explanation, structured lookup, or action.

---

## 9. Mobile-First Design

### 9.1 Primary reading environment

Assume many readers will open documents on a phone in portrait orientation and scroll vertically. Mobile suitability is a publication requirement, not an optional enhancement.

### 9.2 Layout

Use one primary text column. Essential content must not depend on side-by-side panels, floating text boxes, landscape-only pages, or exact spatial placement. Avoid multi-column page layouts in the main narrative.

### 9.3 Reflow principle

For web and Markdown presentation, the practical target is that content remain available without two-dimensional scrolling at a width equivalent to 320 CSS pixels, except for elements such as data tables or diagrams whose meaning genuinely requires two dimensions.[cite:19][cite:30] Even when an exhibit qualifies for the exception, the narrative must provide its essential meaning in linear text.

### 9.4 Typography

Use readable body text, adequate line spacing, visible heading contrast, and sufficient white space. Do not shrink text to force a wide table onto a page. The PDF and DOCX baseline in Appendix F uses at least 11-point body text and a clear sans-serif typeface.

### 9.5 Links and navigation

Use descriptive link text. Avoid “click here” and exposed long URLs in primary prose. GitHub-compatible relative links should connect related repository files so links remain valid across branches and repository locations.[cite:6][cite:8]

### 9.6 Mobile acceptance test

A document fails mobile review if essential information requires repeated horizontal scrolling, excessive zoom, decoding tiny labels, or consulting a desktop-only layout. Testing should include:

- A typical phone-width Markdown or web view.
- PDF viewing at fit-to-width.
- DOCX mobile or narrow-window view.
- Navigation by headings.
- Inspection of tables, captions, links, and lists.

---

## 10. Tables, Figures, and Exhibits

### 10.1 Governing rule

Tables are for structured data and concise comparison, not for page layout or ordinary prose. Federal accessible-document guidance similarly states that a table should contain only data and that table titles or captions belong outside the table.[cite:5]

### 10.2 Body placement

Short, essential, mobile-readable data tables may appear near the narrative that explains them. Large, complex, supplementary, or lookup-oriented tables and all nonessential visuals belong in a designated Exhibits section or appendix.

This rule intentionally improves on the collaboration proposal that every table must be removed from the body. A universal ban would force readers to jump away from the explanation even when a small two-column table is the clearest accessible form. The controlling test is reader benefit, not mechanical placement.

### 10.3 Narrative requirement

Every significant exhibit must be introduced or discussed in prose. The narrative must state why the exhibit exists and the takeaway a reader should understand. Do not make the reader derive the document's conclusion solely from rows, columns, axes, color, or spatial position.

### 10.4 Numbering

Use section-based item numbers:

- Table 3.1, Table 3.2.
- Figure 4.1, Figure 4.2.
- Chart 5.1.
- Diagram 6.1.
- Appendix A, Appendix B.

Appendix exhibits may use appendix-based numbering such as Table E.1. Item numbers must remain stable across Markdown, DOCX, and PDF. Pagination may differ.

### 10.5 Cross-references

Reference significant items by number and title, and include the section or appendix when useful. Acceptable language includes:

- “Refer to Table E.3, Required Format Roles and Validation, in Appendix E.”
- “The recovery branch is shown in Figure E.1 in Appendix E.”

Do not rely solely on “the table below,” “the chart above,” or “the following figure,” because content may reflow or move during conversion.

### 10.6 Captions and descriptions

Every substantive exhibit must have:

- A unique item number.
- A descriptive title.
- A one-sentence purpose or interpretive caption.
- A source or derivation note when applicable.
- Definitions of unusual abbreviations, units, symbols, or axes.
- Alternative text or a nearby text equivalent for meaningful visuals.

W3C guidance explains that captions help users locate and understand tables and that headers must identify relationships between header and data cells.[cite:22][cite:24]

### 10.7 Table construction

Use simple structures with clear row or column headers. Avoid merged cells, blank header cells, paragraph-length cell content, nested tables, and decorative shading that carries meaning by itself. Repeat header rows across pages in DOCX and PDF where supported. Complex tables may require redesign or an accessible HTML/dataset companion rather than forced inclusion in Word.[cite:12][cite:15]

### 10.8 Lists of exhibits

A Class B or C document requires a List of Exhibits when it contains three or more significant tables or figures, or when any exhibit is placed in an appendix separate from its first narrative reference. The list includes item number, title, and location.

### 10.9 Charts and graphics

Charts must visualize real, sourced data or clearly labeled simulation output. Decorative charts, pseudo-quantitative graphics, and unscaled diagrams that imply measurement are prohibited. Every chart must include a plain-language interpretation and enough source information to reproduce or verify it where feasible.

### 10.10 Machine-readable companions

Large datasets should be delivered in an appropriate machine-readable format in addition to a human-readable summary. The main document should explain what the dataset contains, how it was produced, and how it should be interpreted.

---

## 11. Accessibility and Resilience

### 11.1 Structural accessibility

Use semantic headings, real lists, real tables, captions, descriptive links, and meaningful alternative text. Do not simulate structure with font size, bolding, tabs, spaces, or manually typed symbols.

### 11.2 Heading order

DOCX must use built-in heading styles in hierarchical order. Accessible Word guidance emphasizes descriptive headings, correct hierarchy, and no skipped levels because assistive technologies use these indicators for navigation.[cite:5][cite:14]

### 11.3 Images and non-text content

Meaningful images, charts, diagrams, and shapes require alternative text or a nearby full description. Images of text should be avoided. Decorative images must be marked decorative when the format supports it.

### 11.4 Color and contrast

Information must not be communicated by color alone. Use adequate foreground-background contrast and preserve meaning in grayscale. Status labels should include text, not merely red, amber, or green styling.

### 11.5 PDF requirements

PDF must contain searchable, selectable text; semantic tags when the production tool supports them; logical reading order; document language; bookmarks for long documents; descriptive metadata; accessible links; and tagged headings, lists, tables, and figures. Tagged PDF provides semantic structure and predictable reading order for assistive technology and reflow.[cite:18][cite:21][cite:28]

A visually accurate PDF is not automatically accessible. The exported file must be inspected after conversion because source-document structure can be lost or misinterpreted.

### 11.6 DOCX requirements

DOCX must use real styles, real list structures, accessible tables, inline images where practical, alt text, meaningful link text, document language, and a logical reading order. The file must remain editable and must not contain unresolved tracked changes or comments in an approved release.

### 11.7 Markdown requirements

Markdown must use a single H1 title, logical H2/H3 hierarchy, native lists, fenced code blocks when needed, descriptive links, meaningful alt text, and simple tables only when suitable. It must remain understandable in raw text and in GitHub's rendered view.

### 11.8 Resilience

Documents must remain understandable when viewed on mobile, desktop, in print, in grayscale, without custom fonts, through assistive technology, or after reasonable format conversion. Essential information must not depend on proprietary effects, floating objects, watermarks, or exact page position.

---

## 12. Sources, Evidence, and Provenance

### 12.1 Traceability

Important factual claims, numbers, quotations, and external standards must be traceable to a source. Cite primary and authoritative material when available. A citation should support the exact claim to which it is attached.

### 12.2 Derivation labels

Tables and figures must include a source note that distinguishes:

- External source.
- User-supplied information.
- Author calculation.
- Model-generated synthesis.
- Simulation output.
- Synthetic data.
- Assumption.
- Mixed derivation.

### 12.3 AI-generated content

AI generation is provenance, not evidence. An AI may summarize or reason from sources, but its generated statement does not become verified merely because it is fluent, repeated, or included in a formal document.

### 12.4 Quotations and copyright

Quote only what is necessary, attribute it, and prefer original summary where extensive reproduction is not authorized. Do not reconstruct copyrighted works or copy long passages merely to make a document appear comprehensive.

### 12.5 Conflicting evidence

When credible sources disagree, state the disagreement, identify the basis for the selected interpretation, and preserve material uncertainty. Do not erase dissent to create artificial consensus.

### 12.6 Source durability

For repository publication, prefer stable URLs, document identifiers, version dates, and archived or official sources. Relative links should be used for internal repository materials where appropriate.

---

## 13. File Formats and Fidelity

### 13.1 Required package

Unless an approved exception applies, each approved substantive document must be delivered as:

1. Markdown (.md).
2. Microsoft Word Open XML (.docx).
3. Portable Document Format (.pdf).

The role and validation criteria for each are listed in **Table E.3, Required Format Roles and Validation, in Appendix E**.

### 13.2 Canonical source

Markdown is the default canonical source for repository-managed documents because it is editable, diffable, and GitHub-compatible. A project may designate DOCX or another accessible structured source as canonical when the content depends on features Markdown cannot preserve. The canonical choice must be declared.

### 13.3 Substantive fidelity

All formats must preserve:

- Title, document ID, version, and status.
- Entity and classification labels.
- Purpose, scope, and boundaries.
- Heading order and section numbering.
- Requirements, findings, decisions, and next actions.
- Exhibit numbers, captions, and references.
- Citations and source notes.
- Revision history.

Layout, pagination, line breaks, and automatic navigation may differ. No decision, warning, limitation, or substantive claim may exist in only one format.

### 13.4 PDF role

PDF is the fixed-layout publication and archival presentation derivative. It must include page numbers and, for Class B and C, a consistent header or footer and bookmarks when supported.

### 13.5 DOCX role

DOCX is the editable office derivative. It must use styles rather than manual formatting, contain page numbers, and preserve editability, captions, heading navigation, and accessible document structure.

### 13.6 Markdown role

Markdown is the plain-text, version-controlled derivative or source. Page numbers do not apply. Navigation is provided by headings, anchors, and links.

### 13.7 Synchronization

Files in one publication package must share the same base filename, version, status, and substantive content. A package is not complete merely because three files with similar titles exist.

### 13.8 Validation

At minimum, verify that each file opens, contains the complete section sequence, displays the correct version and status, and preserves exhibit references. PDF text must be searchable. DOCX must pass a structural inspection. Markdown links and headings must render correctly.

---

## 14. Format Failure and Recovery

### 14.1 Trigger

The protocol applies when a required format cannot be generated, converted, opened, validated, or delivered; when rendering materially damages content; or when an unsupported feature prevents substantive fidelity.

### 14.2 Prohibited conduct

A preparer must not:

- Claim a file was generated when it was not.
- Represent pasted plain text as an actual DOCX or PDF.
- Silently substitute another format.
- Mark a package complete when a required format is missing or corrupted.
- Hide a conversion error in a generic limitation statement.

### 14.3 Required response

The preparer must:

1. Identify every affected format.
2. Classify the failure as generation, conversion, rendering, validation, delivery, unsupported-feature, or corruption failure.
3. State the technical reason as precisely as available.
4. Deliver every valid format that can be produced.
5. Deliver the highest-fidelity editable source.
6. Protect the source from substantive alteration during recovery.
7. Provide a reproducible conversion or remediation path.
8. Complete the Format Failure Notice in Appendix C.
9. Mark the package **FORMAT INCOMPLETE**.
10. Revalidate the recovered format before removing that status.

### 14.4 Recovery priority

Recovery should proceed in this order:

- Preserve content and metadata.
- Preserve status, warnings, and non-claim boundaries.
- Preserve headings, lists, captions, and references.
- Restore accessibility structure.
- Restore layout and visual styling.

Cosmetic fidelity must never take priority over substantive or accessibility fidelity.

### 14.5 Conversion pathways

Approved pathways may include:

- Markdown to DOCX using a controlled converter and reference template.
- DOCX to PDF using an accessible export function rather than print-to-PDF.
- Manual remediation of tags, reading order, tables, and alternative text.
- Replacement of unsupported complex tables with an accessible companion dataset and narrative summary.

Accessible Word-to-PDF guidance recommends retaining DOCX accessibility features and using an export path configured for tagged, reflowable PDF rather than printing to PDF.[cite:5]

### 14.6 Closure

The failure is closed only when the missing format is generated, opens correctly, matches the canonical source, passes the applicable validation checks, and the publication record is updated. The lifecycle and recovery branch appear in **Figure E.1 in Appendix E**.

---

## 15. Naming, Versioning, and Publication

### 15.1 Filename pattern

Use:

`ENTITY-PROJECT-DOCUMENTTYPE-SHORTTITLE-vMAJOR.MINOR-STATUS-YYYY-MM-DD.ext`

Example:

`OAL-DOCS-STANDARD-Publication-v0.1-DRAFT-2026-10-04.md`

Use hyphens, ASCII letters and numbers, and consistent entity abbreviations. Avoid spaces, unexplained acronyms, “final-final,” and filenames that differ only by capitalization.

### 15.2 Version rules

- **v0.x:** Draft development before adoption.
- **v1.0:** First approved or ratified release.
- **v1.1:** Backward-compatible clarification or minor requirement change.
- **v2.0:** Material change to obligations, taxonomy, workflow, or acceptance criteria.

Changing only file format or correcting a typographical error does not necessarily require a substantive version increment, but the publication record must remain traceable.

### 15.3 Revision history

Class B and C documents must record version, date, preparer, change summary, and status. Class A documents may use a compact revision note. Do not allow the change log to overwhelm the document.

### 15.4 Repository structure

Recommended structure:

- `/docs/standards/` — approved standards.
- `/docs/drafts/` — active drafts.
- `/docs/templates/` — controlled templates.
- `/docs/reports/` — project documents.
- `/docs/archive/` — superseded and retired releases.
- `/assets/` — figures and supporting media.
- `/data/` — machine-readable datasets.

### 15.5 Publication index

A README or index must identify the current approved version, canonical source, PDF and DOCX derivatives, status, and superseded versions. GitHub headings and relative links should be used to create reliable internal navigation.[cite:3][cite:6]

### 15.6 Supersession

Approved files must not be overwritten without preserving revision history. A superseded file remains available with a visible notice naming the replacement. Internal links should be updated without destroying historical traceability.

### 15.7 Release package

A release package includes:

- Canonical source.
- DOCX derivative.
- PDF derivative.
- Required assets.
- Optional machine-readable data.
- Validation record or checklist.
- Format Failure Notice if applicable.

---

## 16. AI Attribution and Collaboration

### 16.1 Preparer identity

An AI that materially drafts or structures a document must identify itself by product or system name and role. It must not falsely attribute authorship to a human or conceal material AI contribution.

Examples:

- Prepared by: Perplexity AI — primary preparer.
- Prepared by: [Human name], with drafting assistance from [AI system].
- Primary preparer: [AI system]; human coordinator: [name].

### 16.2 Role boundaries

Preparer identity does not imply endorsement, ownership, canon authority, ratification authority, or factual verification. These roles must be separately identified when relevant.

### 16.3 AI conduct

An AI preparer must:

- Distinguish analysis from execution.
- Distinguish simulation from observation.
- Preserve uncertainty and source provenance.
- State technical limitations.
- Avoid inventing tests, approvals, citations, or files.
- Apply the controlled status taxonomy.
- Preserve entity separation.
- Follow format fidelity and recovery rules.
- Avoid silently changing the documentation standard.

### 16.4 Multi-AI attribution

Where several systems contribute, identify:

- Primary preparer.
- Contributing systems.
- Reviewers.
- Adversarial reviewers.
- Human coordinator.
- Decision or ratification authority.

Participation does not equal consensus. Material disagreement must be preserved in a review note or decision record.

### 16.5 Model changes

A model or application update does not authorize a new presentation standard. The current approved standard governs until formally revised. A system unable to comply must invoke the exception or failure protocol rather than silently substituting its preferred style.

---

## 17. Quality Assurance and Acceptance

### 17.1 Review layers

Each Class B or C publication should receive four reviews:

1. **Substantive review:** Accuracy, reasoning, evidence, and completeness.
2. **Boundary review:** Entity, status, simulation, claim, and non-claim clarity.
3. **Presentation review:** Readability, mobile use, exhibit discipline, and navigation.
4. **Format review:** Cross-format fidelity, file integrity, accessibility, and metadata.

A Class A record may combine these reviews but must still satisfy the universal minimum.

### 17.2 Acceptance gate

A document may be published as approved only when every mandatory gate is either passed or covered by an approved exception. The gates are defined in **Table E.4, Publication Acceptance Gate, in Appendix E**.

### 17.3 Severity

- **Blocking defect:** Missing purpose, ambiguous entity, false completion claim, absent preparer, unmarked simulation, unsupported material claim, missing required format without protocol, corrupted file, or material cross-format inconsistency.
- **Major defect:** Unreadable mobile layout, inaccessible critical content, unreferenced significant exhibit, missing source for a material claim, or incomplete next action.
- **Minor defect:** Nonmaterial style inconsistency, isolated typo, or cosmetic spacing issue.

Blocking defects prevent approval. Major defects require correction or an explicit exception. Minor defects may be corrected in maintenance.

### 17.4 Validation evidence

The release record should note:

- Files opened successfully.
- Page numbers present in PDF and DOCX.
- Headings and navigation inspected.
- PDF text selectable.
- Tables and figures numbered and cited.
- Mobile-width review completed.
- Accessibility checker or manual checks completed.
- Cross-format spot comparison completed.
- Status and version synchronized.

### 17.5 Adversarial review

Major standards, policies, and high-impact reports must include an adversarial review that asks whether requirements are useful, testable, proportional, understandable, and capable of creating unintended burdens. Identified weaknesses must be recorded rather than edited out for appearance.

---

## 18. Exceptions and Governance

### 18.1 Exception principle

The standard is mandatory after adoption, but not mechanically absolute. A justified exception is preferable to hidden noncompliance. Exceptions must improve reader use, meet a technical necessity, or satisfy a higher controlling requirement.

### 18.2 Exception record

A significant exception must state:

- Requirement.
- Deviation.
- Reason.
- Reader or operational benefit.
- Accessibility and fidelity impact.
- Compensating control.
- Approver.
- Date and expiration or review condition.

### 18.3 Non-waivable elements

Without explicit ratification-level approval, an exception may not waive:

- Accurate preparer attribution.
- Purpose and entity identification.
- Honest format status.
- Simulation and evidence boundaries.
- Protection against fabricated execution, sources, approvals, or files.
- Preservation of material warnings and limitations across formats.

### 18.4 Governance

The adopted standard must identify:

- Standard owner.
- Ratification authority.
- Maintainer.
- Review interval.
- Revision proposal method.
- Approval method.
- Archive and supersession method.

This draft leaves those roles unassigned rather than inventing authority.

### 18.5 Change control

Any collaborator may propose a revision. The proposal must identify the problem, affected requirement, expected benefit, compatibility impact, migration need, and adversarial concerns. Major changes require a major version increment and explicit ratification.

### 18.6 Review cycle

Review the standard after its first three substantive uses and at least annually thereafter, or sooner when format tooling, accessibility requirements, repository workflows, or project governance materially change.

### 18.7 Prospective application

Adopted revisions apply prospectively unless the decision record explicitly requires remediation. High-risk legacy documents should be prioritized by readership, decision impact, accessibility barriers, and continuing use.

---

## 19. Independent Execution Validation

### 19.1 Delivered files

This independent execution is prepared as synchronized Markdown, DOCX, and PDF files. The Markdown file is the canonical source for this draft. The DOCX and PDF are generated derivatives.

### 19.2 Self-assessment

The draft includes:

- Executive summary.
- Table of contents.
- Preparer name, date, timestamp, and time zone.
- Entity, status, simulation, and non-claim labels.
- Clear numbered sections.
- Mobile-first single-column narrative.
- Page-number requirements for paginated formats.
- Numbered and cited exhibits in a designated appendix.
- Format fidelity and recovery protocol.
- AI attribution and multi-AI collaboration rules.
- Proportional document classes.
- Acceptance gates, exceptions, and governance.
- Collaboration response analysis.

### 19.3 Known limitations

Automated generation can produce structurally sound files without establishing full legal or standards conformance. This draft does not claim WCAG, Section 508, PDF/UA, or organizational compliance certification. Final adoption should include manual accessibility inspection in the target tools, review of PDF tags and reading order, mobile-device testing, and human governance approval.

### 19.4 Validation status

At generation, the files are intended to be checked for opening, complete text, page numbering, and basic structural consistency. A human reviewer must still verify typography, bookmarks or table-of-contents behavior, accessible reading order, links, and mobile rendering in the final publication environment.

### 19.5 Acceptance status

This document remains **PROVISIONAL DRAFT — NOT RATIFIED**. The generation of all required files does not convert the draft into an approved standard.

---

## 20. Implementation Guide

### 20.1 Commission

Start with a short commission record that names the entity, audience, purpose type, intended result, document class, preparer, due state, and required formats. Apply the Purpose and Execution Test before drafting.

### 20.2 Classify

Assign the lifecycle, maturity, work nature, evidence, distribution, and execution statuses. Write the “is” and “is not” boundary statements before the main narrative so scope drift becomes visible early.

### 20.3 Draft the narrative

Write the plain-language explanation first. Add headings that match the reader's questions. Introduce structured data only after the narrative identifies what the reader needs to compare or verify.

### 20.4 Add exhibits

Number each significant table or figure, add a concise caption and source note, provide alt text or a text equivalent, and cite it from the body. Move complex lookup material to Appendix E or a separate annex. The placement test is stated in Section 10.

### 20.5 Review on mobile

Inspect the document at phone width or fit-to-width. Rewrite wide tables as smaller tables, labeled fields, prose, or companion data. Do not solve width problems by shrinking text.

### 20.6 Generate formats

Generate DOCX and PDF from the controlled source or update all three through a controlled workflow. Preserve section order, numbering, warnings, and version metadata.

### 20.7 Validate

Apply Appendix B and the acceptance gates in Table E.4. Compare representative passages, labels, exhibits, and closing actions across all three files.

### 20.8 Recover or publish

If a format fails, follow Section 14 and Figure E.1. If all blocking gates pass, route the package for the appropriate review or approval. Do not allow a preparer to approve its own high-impact policy merely because it generated the files.

---

## 21. Collaboration Review

### 21.1 Overall finding

The collaboration responses strongly agreed on purpose-driven documentation, multi-format delivery, mobile-first readability, explicit preparer attribution, entity and simulation labeling, numbered exhibits, and a truthful format-failure protocol. The strongest combined contribution was the shift from a style guide to a governance system with acceptance criteria.

A comparative assessment appears in **Table E.5, Council Response Assessment, in Appendix E**. The assessment is qualitative; it does not create a numerical ranking or claim consensus beyond the supplied text.

### 21.2 ChatGPT contribution

The ChatGPT response was the most comprehensive governance commission. It added proportional document classes, lifecycle and evidence distinctions, cross-document relationships, claim discipline, AI-specific rules, multi-AI attribution, adversarial review, and governance of the standard itself. Its main risk was scope: forty-five commissioned areas could produce an extremely long and bureaucratic standard if adopted without consolidation.

This independent version preserves its high-value governance mechanisms while combining overlapping requirements and converting aspirational language into acceptance rules.

### 21.3 Claude contribution

The Claude response was concise and highly executable. It captured the user's central concern about phone reading and made prose, exhibits, labels, non-claims, and purpose testing easy for another model to follow. Its strict rule that no tables may appear in the body was too absolute, and “every document” having full front matter and three formats would burden short records.

This version keeps Claude's directness but permits small essential data tables near the narrative and applies proportional classes.

### 21.4 Perplexity contribution

The prior Perplexity response provided a strong operational prompt, explicit output roles, a detailed failure notice, accessibility provisions, GitHub workflow, and practical templates. It was especially useful in separating Markdown, DOCX, and PDF responsibilities and requiring substantive fidelity.

Its main weakness was length and some duplication between the prompt and explanatory material. This execution integrates those requirements directly into one governing standard.

### 21.5 Grok contribution

The Grok response was the strongest compact model-facing instruction. It emphasized visible first-screen labels, vertical mobile reading, “do not claim a file exists,” and “do not adopt the standard on the user's behalf.” Those are important safeguards.

Its preference for all tables in exhibits is retained as a default for complex material, not a universal ban. Its concise completion test influenced the blocking defects in Section 17.

### 21.6 Microsoft Copilot contribution

The Copilot response openly disclosed its lack of historical context and correctly suggested weighting context-rich contributions more heavily. It contributed a usable metadata set, mobile-first principles, quality criteria, and a documentation philosophy.

Several provisions were too rigid or risky: “No exceptions” for full front matter conflicts with proportionality, automatic “Approved” metadata is inappropriate without authority, and the fallback statement that absent rendering “shall never prevent documentation creation” could understate a genuine publication blocker. This version replaces those with class-based obligations, human approval, and FORMAT INCOMPLETE status.

### 21.7 Resolved conflicts

The independent standard resolves key conflicts as follows:

- **All tables in exhibits vs. useful body tables:** Small essential tables may remain near the narrative; complex or supplementary items go to Exhibits.
- **Mandatory full structure vs. proportionality:** Class A short records use a compact structure; Classes B and C use full front matter.
- **Markdown always canonical vs. feature needs:** Markdown is the default, but a project may designate another accessible structured source.
- **“Final” status vs. maintainability:** Approved and ratified are controlled terms; “final” is discouraged.
- **AI as preparer vs. authority:** AI contribution is disclosed, but preparation does not confer approval, endorsement, or canon authority.
- **Universal PDF requirement vs. accessibility:** PDF remains required for the package, but the accessible source remains available and PDF must be validated rather than presumed accessible.

### 21.8 Adversarial review of this standard

Potential weaknesses remain:

- Three-format delivery creates maintenance cost and can produce drift.
- Section-based exhibit numbers can change during major reorganization.
- The classification system may feel heavy for small records.
- Mobile-friendly PDF remains constrained by fixed-page design.
- Automated DOCX-to-PDF conversion may not create fully accessible tags.
- Repository naming rules may conflict with established project conventions.
- Ratification and ownership roles remain intentionally unresolved.

Mitigations include document classes, canonical-source designation, stable release validation, exception records, post-adoption review after three uses, and retention of Markdown or another accessible source alongside PDF.

---

## 22. Adoption and Next Actions

### 22.1 Decision required

The authorized human reviewer should decide whether to:

- Adopt this draft as v1.0.
- Revise and adopt it.
- Run a limited pilot on three document types.
- Return it for further multi-AI review.
- Reject it with recorded reasons.

### 22.2 Recommended pilot

Before ratification, apply the draft to:

1. A short decision record.
2. A standard simulation or research report.
3. A major governance or architecture document.

The pilot should record drafting time, mobile readability, cross-format drift, accessibility defects, and reviewer comprehension. Findings should inform v1.0.

### 22.3 Required governance assignments

Before adoption, assign:

- Standard owner.
- Ratification authority.
- Maintainer.
- Repository location.
- Review interval.
- Approved conversion tools or workflow.
- Accessibility validation responsibility.

### 22.4 Immediate next action

Review Appendix B, run the three-document pilot, resolve the governance assignments, and record the adoption decision. Until that occurs, this version remains a provisional publication candidate.

---

## Appendix A. Required Templates

### A.1 Compact document-control block

```text
DOCUMENT TITLE:
DOCUMENT ID:
VERSION:
LIFECYCLE STATUS:
MATURITY:
ENTITY SCOPE:
DOCUMENT TYPE:
WORK NATURE:
SIMULATION STATUS:
EVIDENCE STATUS:
EXECUTION STATUS:
DISTRIBUTION:
PREPARED BY:
CONTRIBUTORS:
REVIEWED BY:
PREPARATION DATE/TIME/TIME ZONE:
LAST REVISED:
INTENDED AUDIENCE:
PURPOSE:
INTENDED RESULT:
BROADER TOPIC OR PARENT WORK:
WHAT THIS DOCUMENT IS:
WHAT THIS DOCUMENT IS NOT:
CANONICAL SOURCE:
FORMAT STATUS — MD / DOCX / PDF:
REPOSITORY LOCATION:
```

### A.2 Purpose and intended outcome

```text
Purpose type:
Why this document exists:
Problem, decision, activity, or record addressed:
Intended audience:
What the reader should know, decide, perform, evaluate, or verify:
What publication accomplishes:
Outside scope:
What the document does not establish:
Success criteria:
Next action or “No further action required”:
```

### A.3 Exhibit caption

```text
[Item type and number] — [Descriptive title]
Purpose: [Why this exhibit is included.]
Interpretation: [Plain-language takeaway.]
Source/derivation: [External source, user input, calculation, simulation, assumption, or mixed.]
Accessibility description: [Alt text or location of full text equivalent.]
Cited from: [Section number and title.]
```

### A.4 Revision note

```text
Version:
Date:
Preparer:
Status:
Change summary:
Affected sections:
Compatibility or migration impact:
```

### A.5 Exception record

```text
DOCUMENTATION STANDARD EXCEPTION
Document:
Requirement:
Deviation:
Reason:
Reader or operational benefit:
Accessibility impact:
Fidelity impact:
Compensating control:
Approved by:
Approval date:
Expiration or review condition:
```

### A.6 Multi-AI attribution

```text
Primary preparer:
Contributing systems:
Human coordinator:
Substantive reviewer(s):
Adversarial reviewer(s):
Decision or ratification authority:
Material disagreements preserved in:
```

---

## Appendix B. Compliance Checklists

### B.1 Commission checklist

- [ ] A new document is necessary rather than a revision, issue, or short record.
- [ ] Entity scope is identified.
- [ ] Document class is assigned.
- [ ] Purpose type and intended result are stated.
- [ ] Intended audience is identified.
- [ ] Success criteria are testable.
- [ ] Canonical source and required formats are identified.

### B.2 Content checklist

- [ ] Purpose and intended outcome are clear.
- [ ] Scope and exclusions are clear.
- [ ] What the document is and is not are stated.
- [ ] Simulation and evidence statuses are explicit where relevant.
- [ ] Proposal, execution, verification, and validation are not conflated.
- [ ] Material claims are qualified and sourced.
- [ ] Ordinary readers can understand the main narrative.
- [ ] Conclusions, decisions, or next actions are explicit.

### B.3 Design checklist

- [ ] Single-column primary narrative.
- [ ] Logical heading hierarchy.
- [ ] Readable text and spacing.
- [ ] No essential content depends on color or position.
- [ ] No dense table replaces the narrative.
- [ ] Complex exhibits are in the designated section or annex.
- [ ] Every significant exhibit is numbered, titled, described, sourced, and cited.
- [ ] Mobile-width inspection is complete.

### B.4 Accessibility checklist

- [ ] Built-in heading and list structures are used.
- [ ] Heading levels are not skipped.
- [ ] Links are descriptive.
- [ ] Meaningful images have alt text or a text equivalent.
- [ ] Tables have clear headers and simple structures.
- [ ] PDF text is searchable and reading order has been inspected.
- [ ] DOCX accessibility checker or equivalent review is complete.
- [ ] Markdown is understandable in raw and rendered form.
- [ ] Status and warnings appear in the body, not only headers or footers.

### B.5 Format checklist

- [ ] Markdown exists and opens.
- [ ] DOCX exists and opens.
- [ ] PDF exists and opens.
- [ ] Filenames share the same identity and version.
- [ ] Titles, statuses, sections, and exhibit numbers match.
- [ ] PDF and DOCX have page numbers.
- [ ] PDF has selectable text.
- [ ] Required navigation is present.
- [ ] No substantive warning, claim, or decision exists in only one format.
- [ ] Any failure invokes Appendix C and FORMAT INCOMPLETE status.

### B.6 Publication gate

- [ ] No blocking defects remain.
- [ ] Major defects are corrected or covered by approved exceptions.
- [ ] Revision history is current.
- [ ] Related and superseded documents are linked.
- [ ] Approval was granted by the proper authority.
- [ ] Repository index points to the approved version.
- [ ] The document fulfills its stated purpose.

---

## Appendix C. Format Failure Notice

```text
REQUIRED FORMAT FAILURE AND RECOVERY NOTICE

Document title:
Document ID:
Version:
Status: FORMAT INCOMPLETE
Prepared by:
Notice date/time/time zone:

Affected format(s):
Failure class: generation / conversion / rendering / validation / delivery / unsupported feature / corruption
Observed problem:
Technical reason, if known:
Formats successfully delivered:
Canonical editable source supplied:
Completeness review performed:
Substantive fidelity risk:
Accessibility risk:

Recovery procedure:
1.
2.
3.

Required validation after recovery:
Responsible party or routing destination:
Target review condition:
Closure record:
```

---

## Appendix D. Document Architectures

### D.1 Standard research document

Use a full Class B or C structure: executive summary, research question, scope, methodology, evidence review, analysis, limitations, findings, and next actions. Tables and charts summarize sourced evidence; they do not replace analysis.

### D.2 Simulation report

Add simulation purpose, model boundary, inputs, assumptions, execution environment, scenario identifiers, result labeling, sensitivity, limitations, and prohibition on treating simulated output as observation.

### D.3 Technical specification

Lead with purpose, system boundary, normative language, requirements, interfaces, constraints, acceptance criteria, verification method, dependencies, and change control. Put large schemas and field dictionaries in annexes.

### D.4 Adversarial review

State the proposition or artifact under review, review criteria, strongest supporting case, strongest countercase, failure modes, unresolved disagreements, severity, and recommended disposition. Do not use adversarial tone as a substitute for evidence.

### D.5 Decision record

Use Class A: context, decision, alternatives considered, rationale, consequences, owner, effective date, and review trigger. A separate executive summary and table of contents are ordinarily unnecessary.

### D.6 Short project memo

Use Class A: title block, purpose, current state, needed action, constraints, and next step. Avoid a cover page, decorative design, and large tables.

### D.7 Experimental exercise report

Identify whether the exercise was actually executed, the protocol, participants or systems, inputs, observations, deviations, results, evidence status, repeatability, and next experiment.

### D.8 Concept or preliminary proposal

Prominently label it concept, preliminary, or provisional. Separate desired future state from current capability. State assumptions, unresolved decisions, dependencies, and what evidence is needed before approval.

### D.9 Multi-AI collaborative document

Identify each system's role, the common commission, independent contributions, synthesis method, disagreements, human coordinator, and approval authority. Do not imply consensus merely from participation.

### D.10 Public GitHub publication

Use clean Markdown headings, relative links, stable assets, descriptive filenames, visible status, version links, and companion DOCX/PDF release files. Avoid repository-specific context that an external reader cannot understand.

---

## Appendix E. Exhibits

### Table E.1 — Document Class Requirements

**Purpose:** Defines proportionate obligations by document class.  
**Interpretation:** All classes retain the universal identity and purpose minimum; front matter expands with complexity and impact.  
**Source/derivation:** Independent synthesis of the collaboration responses.  
**Cited from:** Sections 2 and 7.

| Requirement | Class A: Short Record | Class B: Standard | Class C: Major Report | Class D: Annex/Data Companion |
|---|---|---|---|---|
| Purpose and intended result | Required | Required | Required | Required |
| Entity, status, preparer, timestamp | Required | Required | Required | Required |
| “Is / Is Not” boundary | Compact | Required | Required | Required |
| Executive summary | One-paragraph summary | Required | Required | Parent summary plus annex purpose |
| Table of contents | If useful | Required | Required | If multi-section |
| List of exhibits | If threshold met | At threshold | At threshold | At threshold |
| Full accessibility review | Proportionate | Required | Required plus adversarial review | Required for delivered format |
| MD / DOCX / PDF | Required if official release; exception allowed | Required | Required | Required with parent package or approved exception |
| Revision history | Compact note | Required | Required | Required |
| Approval gate | Combined review | Full gate | Full gate plus independent review | Parent or annex gate |

### Table E.2 — Status and Classification Taxonomy

**Purpose:** Prevents unrelated status concepts from being collapsed into one ambiguous label.  
**Interpretation:** A document may be “UNDER REVIEW,” “PROVISIONAL,” “SIMULATION,” “SIMULATED EVIDENCE,” and “PARTIALLY EXECUTED” at the same time because those labels describe different dimensions.  
**Source/derivation:** Independent synthesis of the collaboration responses.  
**Cited from:** Sections 5 and 6.

| Dimension | Controlled examples | Governing question |
|---|---|---|
| Lifecycle | Draft; Under Review; Approved; Ratified; Superseded; Retired; Archival | Where is the document in governance? |
| Maturity | Concept; Preliminary; Provisional; Developed; Validated | How mature is the work? |
| Work nature | Operational; Research; Simulation; Fictional; Hypothetical; Mixed | What kind of content is this? |
| Evidence | Observed; Reported; Calculated; Simulated; Estimated; Assumed; Synthetic; Unknown | How was the claim or value produced? |
| Execution | Proposed; In Progress; Partially Executed; Executed; Verified; Validated; Not Applicable | What has actually occurred? |
| Distribution | Public; Collaborative Internal; Restricted; Archival | Who may receive it? |
| Format | Complete; Format Incomplete; Conversion Pending; Validation Pending | Are all required files valid? |

### Table E.3 — Required Format Roles and Validation

**Purpose:** Assigns a distinct operational role and minimum validation to each required format.  
**Interpretation:** Three filenames are not sufficient; each format must be usable and substantively synchronized.  
**Source/derivation:** Independent standard design informed by official GitHub, Section 508, W3C, and PDF accessibility guidance.[cite:4][cite:8][cite:21]  
**Cited from:** Sections 13 and 17.

| Format | Primary role | Minimum structure | Minimum validation |
|---|---|---|---|
| Markdown | Canonical version-controlled source by default | Logical headings, lists, links, captions, readable raw text | Render check, link check, heading and content comparison |
| DOCX | Editable office and collaboration derivative | True styles, page numbers, accessible tables, alt text, navigation | Open check, style/navigation inspection, accessibility review |
| PDF | Fixed-layout publication and archival derivative | Page numbers, selectable text, tags/bookmarks where supported, logical reading order | Open check, text extraction, visual review, reading-order/tag inspection |

### Table E.4 — Publication Acceptance Gate

**Purpose:** Converts this standard into a testable release decision.  
**Interpretation:** A mandatory “No” blocks approval unless the standard explicitly allows and records an exception.  
**Source/derivation:** Independent execution.  
**Cited from:** Section 17.

| Gate | Acceptance question | Blocking? |
|---|---|---|
| Purpose | Does the document state and fulfill a meaningful purpose? | Yes |
| Identity | Are entity, status, preparer, version, and timestamp explicit? | Yes |
| Boundaries | Are simulation, evidence, scope, and non-claims clear? | Yes |
| Readability | Can a general reader understand the main narrative? | Yes |
| Mobile | Is essential content usable at phone width or fit-to-width? | Yes |
| Exhibits | Are significant exhibits numbered, cited, described, and sourced? | Yes |
| Evidence | Are material claims traceable and appropriately qualified? | Yes |
| Formats | Do valid MD, DOCX, and PDF files exist, or is the failure protocol active? | Yes |
| Fidelity | Do all formats preserve substantive content and status? | Yes |
| Accessibility | Have required structural and manual checks been completed? | Major/Yes for critical content |
| Action | Is the decision, outcome, or next action explicit? | Yes |
| Approval | Has the proper authority approved the release? | Yes for approved status |

### Table E.5 — Council Response Assessment

**Purpose:** Records the qualitative review of the supplied collaboration responses.  
**Interpretation:** Each response added value; the independent standard combines their strengths while correcting rigidity, context gaps, or scope inflation.  
**Source/derivation:** User-supplied collaboration transcript.  
**Cited from:** Section 21.

| Response | Strongest contribution | Principal risk | Treatment in this standard |
|---|---|---|---|
| ChatGPT | Comprehensive governance, proportionality, adversarial review, AI rules | Excessive scope and possible bureaucracy | Consolidated into testable sections and classes |
| Claude | Concise, mobile-first, strongly executable | Absolute ban on body tables and universal full structure | Retained as default direction with proportional exceptions |
| Perplexity | Format roles, recovery protocol, accessibility, GitHub workflow | Length and duplication | Integrated directly into governing requirements |
| Grok | Visible labels, honest file claims, no self-adoption | Overly strict exhibit placement | Used in blocking defects and boundary rules |
| Microsoft Copilot | Context disclosure, metadata, quality principles | “No exceptions,” approval overreach, generic fallback | Replaced by class rules, human approval, and recovery status |

### Figure E.1 — Document Lifecycle and Recovery Flow

**Purpose:** Shows the controlled path from commission to publication and the branch taken when a required format fails.  
**Interpretation:** A document cannot move from failed format generation directly to approved publication; it must be remediated, regenerated, and revalidated.  
**Source/derivation:** Independent execution.  
**Accessibility description:** Linear flow with one recovery loop: commission, purpose test, classification, drafting, review, format generation, validation, acceptance, publication, maintenance, and supersession. A format failure moves to notice, source preservation, recovery, regeneration, and validation before returning to acceptance.  
**Cited from:** Sections 4, 14, and 20.

```text
COMMISSION
    ↓
PURPOSE & EXECUTION TEST ── fail ──→ REVISE / CONSOLIDATE / DO NOT CREATE
    ↓ pass
CLASSIFY & DEFINE BOUNDARIES
    ↓
DRAFT NARRATIVE → ADD & CITE EXHIBITS
    ↓
SUBSTANTIVE / BOUNDARY / MOBILE / ACCESSIBILITY REVIEW
    ↓
GENERATE MD + DOCX + PDF
    ↓
VALIDATE FILES & CROSS-FORMAT FIDELITY
    ├── failure → FORMAT INCOMPLETE NOTICE → PRESERVE SOURCE
    │                                      ↓
    │                              RECOVER / REGENERATE
    │                                      ↓
    └────────────────────────────── REVALIDATE
    ↓ pass
ACCEPTANCE & AUTHORIZED APPROVAL
    ↓
PUBLISH & INDEX
    ↓
MAINTAIN → SUPERSEDE / RETIRE / ARCHIVE
```

---

## Appendix F. Style Specification

### F.1 General

Use a restrained, professional design. Content hierarchy must remain clear in grayscale and without custom fonts. Avoid decorative title pages, oversized logos, ornamental dividers, background images, and dense callout-box layouts.

### F.2 PDF and DOCX baseline

- Page size: Letter by default; A4 by project exception.
- Orientation: Portrait for narrative; landscape only for justified exhibits.
- Margins: Approximately 0.65 to 0.8 inches.
- Body font: Aptos, Arial, Calibri, Source Sans, or another accessible sans-serif; 11 to 12 points.
- Heading 1: 18 to 22 points.
- Heading 2: 15 to 17 points.
- Heading 3: 12 to 14 points.
- Line spacing: Approximately 1.15 to 1.3.
- Paragraph spacing: Visible space after paragraphs; do not create spacing with blank paragraphs.
- Header: Short title and status.
- Footer: Document ID, version, and `Page X of Y` where supported.
- Color: Dark text on a light background; restrained accent color; no color-only meaning.
- Tables: Simple, narrow, repeating header row, no paragraph-dense cells.
- Captions: Keep with the referenced exhibit when feasible.

### F.3 Markdown baseline

- One H1 title.
- H2 for major sections; H3 for subsections.
- No manual table of contents that conflicts with actual headings.
- Blank line between blocks.
- Native lists and fenced code blocks.
- Relative internal links where appropriate.
- No HTML layout tables.
- No essential styling that disappears in raw text.

### F.4 Page numbering

PDF and DOCX use Arabic numerals in the footer. The preferred display is `Page X of Y`. Front matter may use the same continuous sequence for simplicity; separate Roman numbering requires an approved template and a clear benefit.

### F.5 Headers and footers

Headers and footers support navigation but must not be the only location of vital status, confidentiality, deadline, or warning information. Such information must also appear near the beginning of the body.

### F.6 Final file inspection

Inspect widows, orphaned headings, split captions, clipped tables, broken links, missing glyphs, blank pages, and footer collisions. Fixing these issues must not change the substantive content of only one format.

---

**End of Document**  
**Status:** PROVISIONAL DRAFT — NOT RATIFIED  
**Prepared by:** Perplexity AI  
**Version:** 0.1  
**Timestamp:** 2026-10-04 10:48 PDT (UTC−07:00)
