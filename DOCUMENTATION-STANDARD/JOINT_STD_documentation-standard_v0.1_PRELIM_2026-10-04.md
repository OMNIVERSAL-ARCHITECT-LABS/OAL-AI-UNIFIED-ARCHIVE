# Documentation Design, Presentation, Format, and Publication Standard

*OAL / One Industries / Lewis Corp: Independent Execution, with Review of the Team's Responses*

*Markdown edition. Page numbers apply only to the PDF and DOCX editions.*

## Document Control

**Preparer:** Claude Sonnet 5.5 (Anthropic), an AI model  
**Role:** Preparer only. Not canon author, not endorser, and not the adopter of this standard.  
**Prepared:** 2026-10-04 10:52 PDT  
**Version:** 0.1  
**Status:** PRELIMINARY. Proposed standard. Not adopted.  
**Entity:** JOINT. OAL, One Industries, and Lewis Corp.  
**Nature:** NON-SIMULATION. A governance and formatting standard.  
**Connection:** Component of the multi-AI documentation round. Intended for GitHub publication beside the other team members' executions.  
**Purpose:** To define how documents for the shared workspace are labeled, written, formatted, and delivered, and to record the review behind that definition, so the human coordinator can decide whether to adopt it.  
**Purpose type:** DEFINE (Part A) and INFORM (Part B)  
**Class:** Major Report  
**Governing standard:** This document is its own first draft. No adopted standard exists yet.  
**Formats:** Markdown, DOCX, and PDF. All three delivered. See Section 29 for format notes.  
**Non-claim:** This document does not decide whether OAL, One Industries, Lewis Corp, or any scenario they contain is real or fictional. It is not canon, not an endorsement, and not legal or financial advice.

## Executive Summary

**Why this exists.** Recent documents in the shared workspace leaned heavily on rows, columns, and matrices. A regular person on a phone could not simply read them. Different AI platforms also produced very different presentation when no standard was specified. This document is a proposed standard that fixes both problems.

**What was done.** I read the original brief and the five team responses (ChatGPT, Claude, Perplexity, Grok, Microsoft Copilot). Each response was a prompt for the standard, not the standard. I then wrote an independent execution: a complete first version of the standard (Part A), followed by a review of the responses and the decisions I made (Part B).

**What the standard requires, in short.** Every document opens with a Core Block on the first screen: preparer, date and timestamp, version, status, entity, simulation or non-simulation, connection to broader work, purpose, and a tailored non-claim. The body is single-column prose. Row-and-column tables, charts, and figures live only in a numbered Exhibits section and are cited by number. Every document ships as PDF, DOCX, and Markdown, or honestly reports which format failed and why. A pass/fail gate decides whether a document may be published.

**What the review found.** All five responses agree on the core: purpose before production, three formats, labels, non-claims, mobile-first. Each also has real gaps. ChatGPT is the most complete but risks bureaucratic overgrowth. My earlier response was too thin to govern anything. Perplexity has the best per-format rules but presented its own control block as a table. Grok is the most phone-friendly but omits versioning and governance. Copilot is clear, but its example shows an AI setting "Approved" status and it lacks proportionality.

**What remains unresolved.** Section 27 lists seven open questions for the human coordinator. The two that matter most: whether short records may skip the executive summary and table of contents, and whether PDFs should use a phone-sized page.

**What happens next.** Review this draft, answer the open questions, and pilot the standard on three recent GitHub documents before adopting it as v1.0. Section 28 has the full list.

## How to Read This Document

Part A is the standard. It is normative, which means its rules apply to future documents. Part B is informative. It explains the review and the reasoning, and it does not bind anyone.

Tables and figures are not in the body. Please refer to the List of Exhibits below, then to the Exhibits section at the end. This document follows its own exhibit rule.

If you only have two minutes, read the Executive Summary and Sections 4, 5, and 9.

## Table of Contents

- **[Document Control](#document-control)**
- **[Executive Summary](#executive-summary)**
- **[How to Read This Document](#how-to-read-this-document)**
- **[Table of Contents](#table-of-contents)**
- **[List of Exhibits](#list-of-exhibits)**
- **[Part A. The Standard (Normative)](#part-a-the-standard-normative)**
  - [1. Purpose and Intended Result](#1-purpose-and-intended-result)
  - [2. Scope and Non-Claims](#2-scope-and-non-claims)
  - [3. Governing Principles](#3-governing-principles)
  - [4. Document Classes and Required Components](#4-document-classes-and-required-components)
  - [5. Labels: Entity, Nature, Status, Connection](#5-labels-entity-nature-status-connection)
  - [6. Reality, Claim, and Simulation Boundaries](#6-reality-claim-and-simulation-boundaries)
  - [7. Purpose Statement and Purpose Test](#7-purpose-statement-and-purpose-test)
  - [8. Writing and Mobile-First Design](#8-writing-and-mobile-first-design)
  - [9. Exhibits: Tables, Figures, and Charts](#9-exhibits-tables-figures-and-charts)
  - [10. Evidence and Source Labeling](#10-evidence-and-source-labeling)
  - [11. Required Output Formats and Fidelity](#11-required-output-formats-and-fidelity)
  - [12. Format Failure and Recovery Protocol](#12-format-failure-and-recovery-protocol)
  - [13. Preparer, Attribution, and Multi-AI Collaboration](#13-preparer-attribution-and-multi-ai-collaboration)
  - [14. Accessibility and Format Resilience](#14-accessibility-and-format-resilience)
  - [15. File Naming, Versioning, and Relationships](#15-file-naming-versioning-and-relationships)
  - [16. GitHub Publication](#16-github-publication)
  - [17. Quality Checklist and Acceptance Gate](#17-quality-checklist-and-acceptance-gate)
  - [18. Exceptions](#18-exceptions)
  - [19. Governance and Revision](#19-governance-and-revision)
  - [20. Examples of Compliant and Noncompliant Presentation](#20-examples-of-compliant-and-noncompliant-presentation)
  - [21. Document Architectures by Type](#21-document-architectures-by-type)
- **[Part B. Review and Rationale (Informative)](#part-b-review-and-rationale-informative)**
  - [22. Review Method and Limits](#22-review-method-and-limits)
  - [23. Review of the Five Responses](#23-review-of-the-five-responses)
  - [24. Cross-Cutting Findings](#24-cross-cutting-findings)
  - [25. Conflicts and the Rules Adopted](#25-conflicts-and-the-rules-adopted)
  - [26. Adversarial Review of This Standard](#26-adversarial-review-of-this-standard)
  - [27. Open Questions for Decision](#27-open-questions-for-decision)
  - [28. Next Actions](#28-next-actions)
  - [29. Delivery Notes and Gate Record](#29-delivery-notes-and-gate-record)
- **[Exhibits](#exhibits)**

## List of Exhibits

- [Table 4.1. Document Classes and Required Components](#table-41-document-classes-and-required-components) (cited in Section 4)
- [Table 5.1. Status Words](#table-51-status-words) (cited in Section 5)
- [Table 12.1. Format Failure Types](#table-121-format-failure-types) (cited in Section 12)
- [Figure 12.1. Diagram: Delivery Decision Flow](#figure-121-diagram-delivery-decision-flow) (cited in Section 12)
- [Table 15.1. Filename Codes](#table-151-filename-codes) (cited in Section 15)
- [Table 15.2. Version Increments](#table-152-version-increments) (cited in Section 15)
- [Table 24.1. Summary of the Five Responses](#table-241-summary-of-the-five-responses) (cited in Section 24)
- [Table 25.1. Conflicts and Rules Adopted](#table-251-conflicts-and-rules-adopted) (cited in Section 25)

## Part A. The Standard (Normative)

### 1. Purpose and Intended Result

**1.1 What this standard is for.** It tells any human or AI preparing a document for the shared workspace what the document must contain, how it must look, how it must be labeled, and how it is delivered. It is a governance instrument. It is not a list of style preferences.

**1.2 Intended result.** A collaborator who receives this standard should know what document to create and why, how to label its status and nature, how to write for phone readers, where tables and figures go, how to deliver the three formats or report honestly why not, and how to tell whether the result is acceptable.

**1.3 Why it exists.** Documents drifted toward dense grids that ordinary readers could not follow. When no standard was given, each AI platform chose its own presentation, so the workspace changed style without anyone deciding it should. This standard stops that silent drift.

**1.4 How success is measured.** Not by page count. Success means future documents are clearer, more consistent, more traceable, and more useful. Section 19 sets a review after the first ten documents.

### 2. Scope and Non-Claims

**2.1 What it governs.** Every document prepared for the collaborative workspace for OAL, One Industries, Lewis Corp, or joint work, by any AI or human, including anything published to GitHub.

**2.2 What it does not govern.** Private chat, scratch notes, raw data files, and source code itself. It governs documentation about code. It also does not govern the content of the work. It says how to present canon, not what canon is.

**2.3 What it does not claim.** It does not decide whether any entity or scenario is real or fictional. It does not rank the three organizations. It does not ratify any other document.

**2.4 Normative words.** MUST means a document that fails it is noncompliant. SHOULD means a deviation needs a one-line reason. MAY means optional. Part A is normative. Part B is informative.

### 3. Governing Principles

Ten principles guide every later rule. When two rules seem to conflict, the principle decides.

1. **Purpose before production.** Know why the document exists before designing it.
2. **Reader before layout.** Design for how the information will actually be read.
3. **Narrative before matrix.** Explain in prose first. Structured data supports the prose.
4. **Evidence before confidence.** Never write more strongly than the evidence allows.
5. **Labels before assumptions.** Name simulations, proposals, and provisional work.
6. **Traceability before volume.** A smaller traceable document beats a large opaque one.
7. **Mobile before desktop-only design.** Assume most readers use phones.
8. **Consistency without rigidity.** Standardize where inconsistency harms the reader. Allow justified exceptions.
9. **Fidelity across formats.** PDF, DOCX, and Markdown carry the same substance.
10. **Execution before ceremony.** Documentation supports real work, decisions, testing, understanding, preservation, or accountability.

### 4. Document Classes and Required Components

**4.1 Four classes.** A Short Record is a memo, note, log entry, or decision record of about two pages or fewer. A Standard Document is an ordinary report, specification, simulation report, or review. A Major Report is long research, architecture, program-level work, or a standard like this one. A Technical Annex or Dataset is highly structured supporting material that attaches to a parent document.

**4.2 Pick the smallest class that works.** The preparer chooses the class and names it in the Core Block. Choose the smallest class that still lets the reader do what the purpose requires.

**4.3 The Core Block applies to every class.** It MUST appear on the first screen and MUST contain: preparer, role, date and timestamp with time zone, version, status, entity, nature, connection, purpose, class, governing standard and version, and a tailored non-claim. Section 5 defines the labels. Section 7 defines the purpose line.

**4.4 Other components by class.** Please refer to Table 4.1 in the Exhibits section for what each class MUST include and what it MAY omit. In plain terms: the heavier the document, the more navigation it needs. A Short Record needs the Core Block and a clear result. A Major Report also needs a table of contents, a list of exhibits when it has five or more, limitations, and next actions. Where an executive summary is required, it SHOULD fit on one page and be understandable without reading the rest.

**4.5 The short-record question is open.** The original instruction was that every document carries an executive summary and a table of contents. Table 4.1 proposes a lighter rule for Short Records, because a two-page memo with a table of contents is bureaucracy. That relaxation is not in force until the human coordinator accepts it (Open Question 1). Until then the strict reading applies, and a Short Record may satisfy it with a two-line summary and a three-line contents list.

### 5. Labels: Entity, Nature, Status, Connection

**5.1 The labels appear on the first screen and repeat in the header, the filename, and the opening summary.** They are always written as words. Color MAY be added but MUST NOT carry the meaning, because documents are printed in grayscale, viewed with accessibility tools, and converted between formats.

**5.2 Entity label.** Use OAL for Omniversal Architect Labs, ONE for One Industries, LC for Lewis Corp, JOINT when two or more are involved (and name them), or EXT for external or third-party material. Do not blend entities into one label.

**5.3 Nature label.** Use SIMULATION, NON-SIMULATION, or MIXED. Also state the work type, such as standard, concept, experiment, review, record, operational note, or specification. Section 6 adds required fields whenever the nature is SIMULATION or MIXED.

**5.4 Status label.** Seven status words cover the life of a document. Please refer to Table 5.1 in the Exhibits section for their meanings and who may set each. Status describes maturity only. It never describes nature. A document can be a PRELIMINARY SIMULATION or an ADOPTED NON-SIMULATION.

**5.5 Preliminary versus provisional.** PRELIMINARY means early and expected to change a lot. PROVISIONAL means usable now but subject to revision. Provisional work is in effect for the time being, so only the human coordinator may set it.

**5.6 No self-approval.** An AI preparer MAY set DRAFT, PRELIMINARY, and UNDER REVIEW. An AI MUST NOT mark its own work PROVISIONAL, ADOPTED, SUPERSEDED, or ARCHIVED. Those belong to the human coordinator.

**5.7 Connection label.** State whether the document is standalone, a component of a named program, a sub-study, a revision, an implementation, a supporting analysis, or part of a larger topic. Name the topic, or write "none stated". Do not leave the reader to guess.

**5.8 Defaults.** If the preparer is unsure, the default status is DRAFT and the default real-world claim is none.

### 6. Reality, Claim, and Simulation Boundaries

**6.1 The Non-Claim Statement.** Every document states, in one to three sentences, what it is and what it is not a claim on. Tailor it. Do not paste identical boilerplate into every file. Typical statements: this is a simulation; this is a proposed specification; this is not evidence that the modeled event occurred; this does not establish that the described entity exists in the physical world; this is not a validated operational system.

**6.2 The neutrality rule.** This standard does not exist to argue whether OAL, One Industries, Lewis Corp, a scenario, or a framework is real or fictional. The document's declared purpose governs. If the purpose is to classify something as real or fictional, say so. If the purpose is to open a debate, say so. Otherwise neither the preparer nor a reviewer reopens that question.

**6.3 Simulation fields.** When nature is SIMULATION or MIXED, add these labeled lines near the top, each on its own line. Simulation status: yes, no, or mixed. Simulation type. Real-world claim: none, limited, or specified (and state what). Input source. Assumptions (where they are listed). Execution status: proposed, executed, or partly executed. Result type: simulated, observed, calculated, estimated, or mixed.

**6.4 No number without an origin.** A reader should never have to guess whether a number came from observation, calculation, simulation, assumption, synthetic data, outside research, estimation, or speculation. Section 10 gives the origin labels.

**6.5 Claim discipline.** Use "is" only for what is established. Otherwise use the precise word: was observed, was simulated, was calculated, was reported, is modeled as, is assumed to be, is proposed, has been verified, or remains unknown. Confident style must not create false evidentiary confidence.

### 7. Purpose Statement and Purpose Test

**7.1 The purpose line.** Every document states in one or two sentences what it is designed to accomplish. It also names its purpose type: decide, define, execute, record, inform, analyze, test, instruct, propose, classify (real versus fictional), or debate.

**7.2 Intended outcome and success criteria.** Standard Documents and above add a short section answering: who will use this, what should they know, decide, or do afterward, and how will anyone tell whether it worked. Also state whether the document describes an intention or demonstrates something that was actually executed.

**7.3 The Purpose Test.** Before writing, the preparer answers seven questions. Why does this document exist? Who will use it? What outcome should follow? What does its existence actually accomplish? Does it require action after publication? Does it connect to other work? How can anyone tell whether it succeeded?

**7.4 Failing the test.** If those questions cannot be answered, the preparer reconsiders. Options: merge the content into an existing document, defer it, or do not create it. A document whose only result is that a document now exists fails. "No further action required" is a valid and honest outcome when it is accurate.

**7.5 Not an argument.** A document is not meant to start an argument unless that is its stated purpose. A document that exists to debate says so in the purpose line.

**7.6 No invented work.** A document that records an exercise states whether it was executed or only proposed. An AI preparer MUST NOT describe a test, run, or review that did not happen.

### 8. Writing and Mobile-First Design

**8.1 The reading assumption.** Most readers open documents on a phone and scroll down one continuous column. Mobile design is a core requirement and not an afterthought.

**8.2 Single column.** Content reads top to bottom in one logical order. No essential content sits side by side. No essential content needs horizontal scrolling.

**8.3 Prose first.** The body is readable prose that a non-specialist can follow. Keep paragraphs short, usually five sentences or fewer. Use one idea per section and descriptive headings that let a reader scan.

**8.4 No row-and-column tables in the body.** Tables, charts, matrices, and figures go in the Exhibits section (Section 9). The body MAY use short flat lists of seven items or fewer, numbered steps, and stacked label-and-value lines.

**8.5 The stacked-line alternative.** When a table row would have carried several fields, write the entry as short labeled lines instead. Example: "Status: PROVISIONAL." then "Meaning: usable now, subject to revision." then "Who may set it: the human coordinator." Readers on phones can follow that. They cannot follow four narrow columns.

**8.6 Type and spacing.** Body text MUST be at least 12 points in DOCX and PDF. Exhibit text and captions MUST be at least 10 points. Use generous line spacing, margins of at least 0.75 inch, portrait orientation, and high contrast. Never rely on tiny type to fit content.

**8.7 Links.** Use descriptive link text. Do not put raw URLs in running prose. Place long URLs in a References section.

**8.8 Plain language.** Define specialist terms at first use. Prefer active voice when it helps. State decisions, owners, and next actions directly.

**8.9 Restraint.** No decorative graphics. No ornamental title pages. No stacks of callout boxes. No artificial visual complexity. A document that looks sophisticated but reads poorly is noncompliant.

**8.10 Layers for mixed audiences.** Order content as summary first, then plain-language narrative, then technical detail, then exhibits, then appendices. Technical completeness must not make the main narrative inaccessible.

**8.11 Priority order.** When goals compete, prefer accuracy, then comprehension, then traceability, then usability, then accessibility, and only then information density. Dense is not the same as good.

### 9. Exhibits: Tables, Figures, and Charts

**9.1 What an exhibit is.** Any table, matrix, chart, graph, diagram, figure, or graphic. If it uses rows and columns or is a picture, it is an exhibit.

**9.2 Placement.** Exhibits MUST NOT appear in the body. They sit in one designated section titled Exhibits, near the end and before any appendices or references. In a Technical Annex the whole document may be exhibits.

**9.3 Two item types.** Use Table for anything in rows and columns. Use Figure for every chart, graph, diagram, or graphic, and name the kind in the title, such as "Figure 12.1. Diagram: Delivery decision flow". Two types keep numbering and lists simple.

**9.4 Numbering.** An item is numbered by the body section that first introduces it, then its order within that section. The first table introduced in Section 4 is Table 4.1. The second is Table 4.2. Appendix items use the appendix letter, such as Table A.1.

**9.5 Citing.** The body cites every exhibit by number and location. Use the form "Please refer to Table 4.1 in the Exhibits section." Never write "the table below," "the chart above," or "the following graphic." Documents reflow across PDF, DOCX, and Markdown, so spatial words are unreliable.

**9.6 Prose explains first.** The body MUST state what the exhibit shows and why it matters, in plain words. A reader who never opens the exhibit should still understand the point.

**9.7 What each exhibit carries.** A number, a title, a one-sentence purpose, the section that cites it, a source or origin note, an explanation of unusual abbreviations, units, axes, or symbols, and alternative text for every figure.

**9.8 Mobile design of exhibits.** Tables SHOULD have no more than three columns and short cell text. Do not put paragraphs inside cells. If a table is too wide, split it, restack it as labeled entries, move it to a Technical Annex, or provide a companion data file.

**9.9 The table test and the figure test.** A table must answer a question better than prose would. If it does not, use prose. A figure must do a job: explain structure, show relationships, illustrate a workflow, visualize data, document a result, show a timeline, or map dependencies. Decoration does not qualify.

**9.10 List of Exhibits.** A document with five or more exhibits MUST include a List of Exhibits after the table of contents. Each entry gives the number, title, and citing section. Smaller documents may omit it.

**9.11 Stability across formats.** Exhibit numbers MUST NOT change between PDF, DOCX, and Markdown. If a section is renumbered, update every citation.

### 10. Evidence and Source Labeling

**10.1 Origin labels.** Important claims and every exhibit identify where they came from, using plain terms: sourced (name the source), user-supplied, model-generated, calculated, estimated, simulated, synthetic, assumed, hypothesis, or conclusion. Label what matters. Do not tag every sentence.

**10.2 Source note on every exhibit.** Examples: "Source: simulation output under Scenario ECL-03." "Source: preparer calculation from user-supplied assumptions." "Source: user-supplied scenario description."

**10.3 Verified versus validated.** Verified means checked against a source or a rule. Validated means shown to work for its intended purpose. Do not use one word for the other.

**10.4 No fabricated citations.** If a source cannot be checked, write "unverified." Never invent a reference, quotation, test, or page number.

**10.5 Preserve uncertainty and disagreement.** When sources or collaborating AIs disagree, record both positions. Do not smooth a disagreement into false consensus.

### 11. Required Output Formats and Fidelity

**11.1 Three formats.** Every finished document is delivered as PDF, DOCX, and Markdown. Markdown is the source of truth for GitHub and version history. DOCX is the editable copy. PDF is the stable reading copy. All three are equal deliverables.

**11.2 One document, three files.** The three files carry the same content, section order, headings, numbering, exhibit numbers, status, dates, version, and citations. Differences are allowed only when a format forces them, such as page numbers existing only in paginated formats. Material differences in claims, findings, dates, or versions are never allowed.

**11.3 PDF requirements.** Selectable text, never image-only. Page numbers. Bookmarks from headings where the tool supports them. Accessibility tags where the tool supports them.

**11.4 DOCX requirements.** Real heading styles and real list styles, not hand-typed formatting. Header rows marked on tables. Alternative text on figures. Page numbers.

**11.5 Markdown requirements.** Heading levels that do not skip. Readable as raw text. Relative links. Pipe tables only inside the Exhibits section. A note that page numbers apply only to PDF and DOCX.

**11.6 Page numbers.** PDF and DOCX footers read "Page X of Y" on every page, with continuous numbering through the front matter and appendices. Markdown uses headings as its navigation.

**11.7 Header and footer.** The header carries the entity label and status. The footer carries the filename and the page number.

**11.8 Dates and times.** Write dates as YYYY-MM-DD. Write time in 24-hour form with a time zone abbreviation, such as 10:52 PDT. Add a last-revised date when the document changes.

### 12. Format Failure and Recovery Protocol

**12.1 The honesty rule.** A preparer MUST NOT claim a file exists unless it was written and opened. Plain text pasted into a chat reply is not a DOCX or a PDF. A missing format MUST NOT be silently replaced by a different one.

**12.2 Types of failure.** Please refer to Table 12.1 in the Exhibits section for six failure types and the response each needs. They are generation failure, conversion failure, rendering failure, layout incompatibility, unsupported feature, and incomplete export. Name the type accurately.

**12.3 The steps.** First, identify which format is missing. Second, state the limitation accurately. Third, deliver every format that did work. Fourth, supply the full content in the best editable format, usually Markdown. Fifth, give a conversion path, with the exact command or app steps where possible. Sixth, record a Format Exception notice in the document. Seventh, flag the delivery FORMAT INCOMPLETE until the gap is closed or an exception is accepted. Please refer to Figure 12.1 in the Exhibits section for the flow.

**12.4 The Format Exception notice.** Write it as stacked lines: required format, status (not produced or partly produced), failure type, reason, source supplied, recovery step, whether the content was reviewed for completeness, preparer, and timestamp.

**12.5 Handing off.** The preparer MAY recommend which collaborator or tool can finish the conversion. The preparer MUST NOT assume another collaborator accepted the task. The human coordinator assigns the work. The preparer stays responsible for an accurate notice.

**12.6 FORMAT INCOMPLETE is a delivery flag, not a status.** A document keeps its real status, such as PRELIMINARY, and carries the flag beside it. A flagged document MUST NOT be called final or adopted.

**12.7 Verify before saying delivered.** Before telling anyone a file was produced, the preparer opens it, checks the page count or section count, and confirms the content matches the source.

### 13. Preparer, Attribution, and Multi-AI Collaboration

**13.1 Name the preparer.** Every document names who actually prepared it. For an AI, give the system, the model, and the provider, such as "Claude Sonnet 5.5 (Anthropic)". For a person, give the name. For a combination, say so, such as "Prepared by Nathan Lewis II with ChatGPT." Never falsely credit human authorship to AI work or the reverse.

**13.2 State the role.** The Core Block says the preparer is the preparer. It is not the canon author or an endorser unless the human coordinator states otherwise.

**13.3 The preparer line is a record.** A document's design, clarity, assumptions, and accuracy reflect on whoever is listed. Treat AI-prepared documents as professional work products, not anonymous output. Other readers, including other AIs, will take that preparer's presentation as an example. This is a point about accountability. It does not require pretending that an AI is a person.

**13.4 Roles in collaborative documents.** Name each that applies: primary preparer, contributing systems, reviewers, adversarial reviewers, and the human coordinator.

**13.5 No implied consensus.** Several systems taking part does not mean they agree. Where they disagree and it matters, preserve the disagreement.

**13.6 No silent changes.** An AI MUST NOT change this standard, or quietly depart from it, on its own initiative. If a model update or rendering engine changes how a document looks, say so in the document.

**13.7 No self-adoption.** An AI MUST NOT adopt, ratify, or approve its own work or this standard. See Section 5.6.

### 14. Accessibility and Format Resilience

A document should stay understandable when viewed on a phone or a desktop, printed in grayscale, converted to another format, viewed in dark mode, read by an accessibility tool, or opened in different software. Requirements:

- Use a heading hierarchy with no skipped levels and a logical reading order.
- Use real text, not images of text.
- Give every figure alternative text and a caption.
- Give every table a marked header row and a caption.
- Use descriptive link text.
- Use high contrast. Never let color, shape, or position alone carry meaning.
- Use common fonts with sensible fallbacks. Do not depend on one exact font.
- Do not depend on exact page position or software-specific effects.
- Review the exported files, not only the source: PDF reading order and headings, DOCX with the available accessibility checker, and Markdown for heading and list structure.

Public accessibility guidance exists, notably from W3C (WCAG) and Section 508. This release does not quote it. Any later citation must be checked against the actual source (Section 10.4).

### 15. File Naming, Versioning, and Relationships

**15.1 Filename pattern.** Use ENTITY_TYPE_short-title_vMAJOR.MINOR_STATUS_YYYY-MM-DD.ext. Underscores separate the fields. Hyphens separate words inside the title. The title is lowercase with no spaces. The PDF, DOCX, and Markdown files share one name and differ only in the extension. Example: JOINT_STD_documentation-standard_v0.1_PRELIM_2026-10-04.pdf.

**15.2 Codes.** Please refer to Table 15.1 in the Exhibits section for entity, type, and status codes. The same labels appear in the filename, the Core Block, and the opening summary.

**15.3 Version numbers.** Drafts before adoption use v0.x. The first adopted version is v1.0. Please refer to Table 15.2 in the Exhibits section for what triggers each increment. Moving a document from PROVISIONAL to ADOPTED is a version event, so the filename changes with it.

**15.4 Old files are not renamed.** When a version is superseded, move it to the archive folder with its name unchanged. The index (Section 16) records that it was superseded and by what.

**15.5 Revision note.** Every document ends with a short revision note. A Short Record needs one line. Do not build a large revision table in the body. If history is long, put it in a Technical Annex.

**15.6 Relationship fields.** Include only those that apply: parent document, related document, supersedes, superseded by, depends on, supports, associated simulation, associated dataset, associated repository. These turn separate files into a navigable body of work.

### 16. GitHub Publication

**16.1 Folders.** Keep predictable folders: one for standards, one per entity for documents, one for archived versions, and one for assets such as figures. A README index lists the current version of each document with its status.

**16.2 Source and copies.** The Markdown file is the source of truth. The PDF and DOCX copies sit beside it with the same base name.

**16.3 Links and figures.** Use relative links. Store figures in the assets folder and reference them consistently. Check for broken internal links before committing.

**16.4 Tables in Markdown.** Pipe tables appear only in the Exhibits section and stay narrow. Wide tables render poorly on phones.

**16.5 Never overwrite.** Do not overwrite adopted or archived versions. Publish a new version and update the index.

**16.6 Check the audience before committing.** A public repository is public. State the document's distribution (public, internal, or restricted) in the Core Block when it matters, and confirm it before the file is committed.

**16.7 Keep the metadata.** The Core Block stays at the top of the Markdown file so the metadata travels with the text.

### 17. Quality Checklist and Acceptance Gate

**17.1 How the gate works.** The preparer runs the checklist before release. The ten blocking items must all be answered yes. Any no means the document does not ship, or ships with a recorded exception (Section 18). The warning items are noted but do not block.

**17.2 Blocking items.**

1. The purpose line is present and the Purpose Test is answered.
2. The entity, nature, status, and connection labels are present.
3. The non-claim is present and tailored to this document.
4. The preparer, role, date, time, time zone, and version are present.
5. No row-and-column table appears in the body.
6. Every exhibit is numbered, titled, sourced, and cited by number from the body.
7. The body explains every exhibit in plain words.
8. PDF, DOCX, and Markdown all exist and open, or a Format Exception is recorded and the flag is set.
9. The three formats say the same thing, and PDF and DOCX have page numbers.
10. The filename follows Section 15 and the document was checked for phone reading.

**17.3 Items that depend on class.** The executive summary and table of contents (Table 4.1). The simulation fields when nature is SIMULATION or MIXED. The list of exhibits when there are five or more.

**17.4 Warning items.** Related documents identified. Next action stated. Accessibility review done. Claims worded to match evidence. Revision note updated.

**17.5 Record the result.** The preparer records "Pass," "Pass with exceptions," or "Fail" and the date. Section 29 shows an example.

**17.6 A gate must be able to fail.** A checklist that always passes is decoration. If a reviewer cannot tell how an item would fail, rewrite the item.

### 18. Exceptions

**18.1 When an exception is acceptable.** When it is technically necessary, structurally appropriate, required by another format, or clearly better for the reader. Deviations are intentional, never accidental.

**18.2 Minor deviations.** Note them in one line near the revision note.

**18.3 Major deviations.** Record a Standard Exception: requirement, deviation, reason, impact, accepted by, and date. The human coordinator accepts it. Examples of major requirements: the three formats, the Core Block, the exhibits-only rule, and the non-claim.

**18.4 Exceptions expire.** An exception applies to one document unless the standard itself is revised to allow it.

### 19. Governance and Revision

**19.1 Who may propose.** Any human or AI collaborator MAY propose a change. A proposal states what changes, why, and which real documents showed the problem.

**19.2 Who adopts.** Only the human coordinator adopts, supersedes, or retires a version of this standard.

**19.3 Major versus minor.** A major change makes a previously compliant document noncompliant, so it raises the major version. A clarification or an optional addition raises the minor version.

**19.4 Which version governed.** Every document's Core Block names the standard version it followed. The older versions stay in the archive.

**19.5 Adversarial review before adoption.** A proposed version is reviewed against its own question: does it make documentation better or only more bureaucratic? Weaknesses found are preserved in the record, not removed.

**19.6 Scheduled review.** After the first ten documents prepared under an adopted version, or after 90 days, whichever comes first, compare them with earlier work. Remove any requirement that produced no benefit.

**19.7 Applies forward.** The standard applies to new documents. It does not require rewriting the existing archive. Retrofitting is optional, and the most-read documents come first.

### 20. Examples of Compliant and Noncompliant Presentation

The examples below are illustrative. Item numbers, figures, and names inside them are invented and do not refer to exhibits or content in this document.

**20.1 Exhibit references.** Noncompliant: "See the table below." Compliant: "Please refer to Table 4.2 in the Exhibits section."

**20.2 Simulated versus observed.** Noncompliant: "The grid failed at 14 percent load." Compliant: "In the simulation, the modeled grid failed at 14 percent load (simulated result; Table 6.1)."

**20.3 Status.** Noncompliant: "Mostly final." Compliant: "Status: PROVISIONAL."

**20.4 Delivery.** Noncompliant: "Here is your PDF," followed by pasted text. Compliant: "I produced Markdown and DOCX. I could not produce the PDF because this environment cannot render PDF files. The complete Markdown source is attached. Convert it to PDF with the steps below. This delivery is flagged FORMAT INCOMPLETE."

**20.5 Executive summary.** Noncompliant: "This document discusses documentation." Compliant: "This document defines how documents are labeled and delivered so that phone readers can follow them. It proposes ten rules and asks for decisions on seven open questions."

**20.6 Purpose.** Noncompliant: "To document the framework." Compliant: "To decide whether the framework's naming scheme is adopted."

**20.7 A table row as stacked lines.** Instead of a four-column row, write: "Class: Short Record. Typical use: a memo or log entry. Must include: the Core Block and a stated result."

**20.8 A compliant Core Block for a short simulation memo.** Preparer: ChatGPT (OpenAI). Role: preparer only. Prepared: 2026-11-02 14:05 PST. Version: 0.2. Status: PRELIMINARY. Entity: OAL. Nature: SIMULATION. Connection: sub-study of an illustrative program called Program X. Purpose: to record the first run and state what was and was not executed. Class: Short Record. Non-claim: this records a simulated exercise and does not claim the modeled event occurred. Every detail in this example is illustrative.

### 21. Document Architectures by Type

The standard changes shape by document type. Ten common types follow, with the reason each differs.

1. **Standard Research Document.** Summary, purpose, method, narrative findings, limitations, next actions, then exhibits. It differs because readers need to trace claims to sources.
2. **Simulation Report.** Adds the simulation fields (Section 6.3) near the top and labels every result by type. It differs because the main risk is confusing simulated results with observed ones.
3. **Technical Specification.** Stresses definitions, requirements stated as MUST and SHOULD, and dependencies. It differs because implementers need unambiguous rules.
4. **Adversarial Review.** States what was reviewed, the criteria, findings in plain prose, preserved weaknesses, and a verdict. It differs because disagreement must be visible and not smoothed over.
5. **Decision Record.** One decision, the options considered, the choice, who made it, and the date. It is usually a Short Record because its job is to be findable and clear.
6. **Short Project Memo.** Core Block, a two-line summary, the point, and the next action. It differs because proportion matters more than completeness.
7. **Experimental Exercise Report.** States whether the exercise was proposed or executed, the inputs, assumptions, and result type. It differs because an exercise record must not read as an observed event.
8. **Concept or Preliminary Proposal.** Status is PRELIMINARY or DRAFT, the non-claim is prominent, and open questions get a section. It differs because it asks for a reaction, not for trust.
9. **Multi-AI Collaborative Document.** Names primary preparer, contributors, and reviewers, and keeps each system's position visible. It differs because attribution and disagreement are its main risks.
10. **Public GitHub Publication.** Adds distribution, the README index entry, relative links, and the full file triplet. It differs because strangers will read it with no background.

## Part B. Review and Rationale (Informative)

### 22. Review Method and Limits

**22.1 What I reviewed.** The original brief, as dictated, and five team responses as pasted: ChatGPT, Claude, Perplexity, Grok, and Microsoft Copilot.

**22.2 A disclosure.** The Claude response is my own earlier work, from the same model family as this preparer. I applied the same criteria to it as to the others, but I cannot claim to be fully independent about it.

**22.3 Criteria.** Six questions. Is it faithful to the brief? Could an AI actually execute it? Does the response itself follow the mobile rule it prescribes? Is it proportionate? Is it honest about file generation? How deep is its governance?

**22.4 Limits.** I saw text only. I could not see how each response rendered in its own app. I did not run any of the prompts. Perplexity's bracketed citation markers could not be checked from the pasted text. I have not seen the GitHub documents that prompted this effort, so my picture of the problem comes from the brief's description of them.

**22.5 The responses are prompts.** The brief asked for a structured prompt. So none of the five is the standard itself. I judged each as a specification for a standard. This document is the first attempt to execute one.

**22.6 On weighting.** Copilot suggested that systems with project history deserve more weight. That is the coordinator's call. I judged each response on its content. Project history helps most with local vocabulary and expectations. It helps less with general design questions such as proportion and honesty about files. Where it mattered, I say so below.

### 23. Review of the Five Responses

**23.1 ChatGPT.** *Strengths.* It treated the task as a governance system, not a style guide. It added a Purpose-and-Execution Test, a precise vocabulary for claims, a six-way taxonomy of format failures, proportional document classes, an exception record, and an adversarial review of the standard itself. It also asked for ten example architectures and good-and-bad examples. Its closing question is the right one: can this standard actually govern future work?

*Gaps.* It is long, and it commissions a 38-part output, which risks the bureaucratic overgrowth it warns about. It offers 18 possible status words but leaves the choice to the preparer. It suggests a revision-history table, which conflicts with the phone-first rule. It ranks accuracy fifth, below comprehension. It routes exhibits to a designated section or appendix but never states that the body itself must be free of tables. It does not say who may set an Adopted status.

*Taken.* Document classes, the failure taxonomy, claim vocabulary, the exception record, the adversarial review, the examples by type, origin labels, and the no-silent-drift principle.

**23.2 Claude (my earlier response).** *Strengths.* It was concise and faithful to the dictated brief. It stated the exhibits-only rule plainly, with an example sentence. It named purpose types and a four-field label block.

*Gaps.* It was too thin to govern anything. It had no versioning, file naming, accessibility rules, evidence labeling, multi-AI attribution, or GitHub rules. It required an executive summary and table of contents for every document with no proportionality. Its status list had only three words. Its fallback protocol had no failure types and no incomplete state. It banned body tables outright and offered only short lists as an alternative for data.

*Taken.* The exhibit-reference wording and the four-label block, now expanded.

**23.3 Perplexity.** *Strengths.* It has the best per-format rules: selectable PDF text and bookmarks, real DOCX styles, Markdown that reads well raw. It supplies a Rendering/Conversion Notice with required fields, a FORMAT INCOMPLETE marker, a canonical-Markdown and README-index workflow, and an accessibility checklist.

*Gaps.* Its own document-control block is a table, which is the failure the brief is trying to end. It allows simple tables in the Markdown body. It requires a 16-item front matter for every formal document and a 21-section structure, which ignores proportion. It cites WCAG, Section 508, and GitHub documentation through bracketed markers I could not verify.

*Taken.* The notice fields, the FORMAT INCOMPLETE flag (reframed as a delivery flag, not a status), per-format requirements, the README index, and the rule that meaning must not rest on color or position alone.

**23.4 Grok.** *Strengths.* It is the shortest and the most phone-first, and it is written in prose. It puts labels on the first screen. It carries the same labels into the filename. It states that the preparer is not the canon author or an endorser. It defaults status to draft. It forbids adopting the standard on the user's behalf. Its completion test lists conditions under which a document fails, which is easy to check. It uses YYYY-MM-DD dates.

*Gaps.* Its brevity leaves out versioning, accessibility, multi-AI roles, evidence labels, an exception process, and governance of the standard. Its four status words (draft, provisional, reviewed, adopted) leave out "preliminary" as a status, though the brief names it and Grok uses it as a work type. Its rule not to hand a missing format to another model unless asked clashes with a multi-AI workspace where a collaborator may be best placed to convert. Putting status in filenames means a rename at every status change, which it does not address.

*Taken.* The first-screen rule, the preparer-role statement, the failure-condition style of gate, no self-adoption, and the date format. I resolved its two gaps in Sections 12.5 and 15.4.

**23.5 Microsoft Copilot.** *Strengths.* It was candid that it lacks the project history. It gives a clean metadata list, a one-page cap on the executive summary, a Purpose, Objective, Success Criteria, and Intended Use set, relationship mapping, and AI-preparer transparency.

*Gaps.* Its metadata example shows an AI preparer with "Document Status: Approved," which models an AI approving itself. "Public Internal Reference" is a contradictory classification. It says "no exceptions" to a cover page and an eight-item front matter. It requires four separate lists (tables, figures, charts, graphics) for every document. Its failure protocol is four short steps plus an undefined "structured export package," and it has no incomplete state. It proposes an 18-section default structure for all documents. It recommends titling the standard "v1.0" before any review.

*Taken.* The Purpose, Objective, Success Criteria, and Intended Use idea (folded into Section 7.2), the one-page executive summary guideline (Section 4.4), and the relationship fields (Section 15.6). Its lack of project history shows mainly in the missing proportionality and the thin simulation vocabulary. Its mobile and metadata points are general design and stand on their own.

### 24. Cross-Cutting Findings

Please refer to Table 24.1 in the Exhibits section for a side-by-side summary of each response's strongest contribution and main gap. The findings below explain what the pattern means.

**24.1 Strong agreement on the core.** Five independent responses agree on purpose before production, three formats, status and reality labels, non-claims, and mobile-first design. That agreement is a good sign these belong in the core of the standard.

**24.2 The responses showed the problem.** Three of the five were long and heavily formatted, and Perplexity used a table for its control block. The drift the brief describes was visible in the very responses that prescribe against it.

**24.3 One tension nobody resolved.** Most responses said both "avoid tables" and "tables help." None gave a rule for living with both. I resolved it with the Exhibits section plus stacked lines (Sections 8.4, 8.5, and 9).

**24.4 Authority was missing.** No response said who may mark a document adopted. Copilot's metadata example, which shows an AI preparer with Approved status, shows why that matters.

**24.5 Governance of the standard itself was thin.** Only ChatGPT covered how the standard changes, and Copilot and Grok barely did. A standard that cannot be revised will drift anyway.

**24.6 Proportion was rare.** Only ChatGPT addressed short documents. Several responses required the full apparatus for every file.

### 25. Conflicts and the Rules Adopted

Please refer to Table 25.1 in the Exhibits section for all nine conflicts, the rule chosen, and where it lives. Four deserve explanation here.

**25.1 Tables in the body versus exhibits only.** The brief is explicit: tables, charts, and figures go in a designated section and are cited by number. I followed the brief and added the stacked-line alternative so data does not disappear from phone readers.

**25.2 Full apparatus versus proportion.** The brief says every document carries an executive summary and table of contents. ChatGPT argued for proportion. I kept the strict reading as the default and flagged the lighter rule for Short Records as a decision for the coordinator (Section 4.5).

**25.3 Status in the filename.** Status in the filename helps a reader before they open a file. Renaming at each status change breaks links. I kept the status code and made status changes version events, so a rename already happens. Old files are archived, not renamed.

**25.4 Handing off a missing format.** Grok said not to hand it off unless asked. A multi-AI workspace may have a better converter. The preparer may recommend, and the human coordinator assigns.

### 26. Adversarial Review of This Standard

I asked this standard the hardest questions I could. The weaknesses stay in the record.

**26.1 Is it more bureaucratic than useful?** Part A has nineteen normative sections and a ten-item blocking gate. That is a real risk. The mitigation is proportion by class, but I have not tested whether a Short Record would feel burdensome in practice. *Weakness preserved.*

**26.2 Are any fields unnecessary?** Candidates: the Connection label on standalone documents, the governing-standard field, and the repeated role statement ("not canon author") on every file. They may become noise. A pilot should show which readers actually use.

**26.3 Could a regular reader follow it?** Sections 1 to 9 probably yes. The MUST and SHOULD wording is stiff, and Part A is long for a phone. A one-page quick card would help (Section 28). *Weakness preserved.*

**26.4 Could an AI follow it?** Labels, filenames, and the gate are mechanical, so yes. Judgment items such as tailoring the non-claim, or deciding whether a table beats prose, will vary by model. Sections 20 and 21 give examples to narrow that.

**26.5 Could a human follow it?** Less easily. Hand-producing three formats and a conforming filename is real work for a person. A conversion script would help (Section 28).

**26.6 Is it truly usable on mobile?** The prose is. The exhibits are still tables, though narrow ones. I have not tested on a physical phone, and a Letter-size PDF renders small on one (Open Question 2). *Weakness preserved.*

**26.7 Does it prevent false claims of file generation?** The rule is clear (Section 12.1). Enforcement rests on the preparer's honesty and on the gate's open-the-file check. Nothing independent verifies it unless a human or another AI does.

**26.8 Does it separate simulation from observation?** It requires labels and fields. It cannot detect a mislabeled number.

**26.9 Does it keep accountability?** It names the preparer and the model. Model names and versions change, so the record is only as exact as the label the preparer writes.

**26.10 Does it create needless formatting work?** The three formats and the filename pattern do. Tooling would reduce the cost. The cost is real until then.

**26.11 Which requirements sound professional but may accomplish nothing?** Possibly the formal MUST and SHOULD vocabulary, the connection field, and the List of Exhibits threshold of five, which is an unproven number.

**26.12 Can compliance be evaluated?** Most gate items are yes-or-no. Items 7 and 9 and the claim-wording warning need judgment.

**26.13 Would it improve the existing GitHub archive?** Unknown. It applies forward only. A pilot on three recent documents would show whether it helps.

**26.14 Is there a way to revise it?** Yes (Section 19), though untested.

**26.15 A structural weakness.** This document is the standard and also its own first test. The gate was run by its own preparer, which is not independent. An outside review is needed before adoption.

### 27. Open Questions for Decision

1. **Short Records.** May a Short Record omit the executive summary and table of contents (Table 4.1)? Until you decide, the strict rule applies.
2. **Page size.** Should PDFs use a phone-sized page instead of Letter? Open this PDF on your phone. If the text is too small, I recommend a narrower page of about 6 by 9 inches with the same type size.
3. **The human coordinator.** Who holds the coordinator role for adoption and exceptions? I have assumed one person, Nathan Lewis II, but have not been told.
4. **Status in filenames.** Keep the status code in filenames (Section 15.1), or drop it and rely on the index?
5. **Markdown as source of truth.** Is Markdown the right master when DOCX is where people edit?
6. **Weighting the responses.** Should any response carry more weight in a merged standard, as Copilot suggested? This review treated them equally on content.
7. **Default time zone.** Should the standard require one default time zone for every timestamp, or only that the zone is always stated?

### 28. Next Actions

1. The coordinator reads this draft and answers the seven open questions.
2. Compare the other four executions against this one using the Section 17 gate and the Section 26 questions. Record where they disagree.
3. Run a pilot: apply the standard to three recent GitHub documents and note the effort and any failures.
4. Prepare a one-page quick card and a Core Block template as companions. I can write them.
5. Build a small conversion script from Markdown to DOCX and PDF, so the three formats cost less effort.
6. Arrange an independent review of this draft before any adoption.
7. Adoption as v1.0 is the coordinator's decision, made after steps 1 to 6.

### 29. Delivery Notes and Gate Record

**29.1 Formats.** Markdown, DOCX, and PDF were all produced and opened. All three were built from one master source, so their content matches. The Markdown figure file is in the assets folder.

**29.2 Format Exception FX-1.** Required item: table of contents page numbers in DOCX. Failure type: unsupported feature. Reason: the DOCX table of contents is a static, hyperlinked list built from the headings, so it has no page numbers. Substitute: tappable links and "Page X of Y" in the footer. The PDF table of contents has both links and page numbers. Recovery: none required.

**29.3 Format Exception FX-2.** Required item: accessibility tags in PDF. Failure type: unsupported feature. Reason: the PDF toolchain used here does not write accessibility tags or figure alternative text. The PDF has selectable text and heading bookmarks. Substitute: the DOCX and Markdown carry the heading structure and figure alternative text. Recovery: if a tagged PDF is required, export it from the DOCX in Word.

**29.4 Mobile check.** I reviewed rendered pages at reduced size. I did not test on a physical phone.

**29.5 Gate result.** Pass with exceptions. The exceptions are FX-1, FX-2, the mobile check in 29.4, and the lack of an independent reviewer (Section 26.15). Gate run by the preparer on 2026-10-04.

**29.6 Revision note.** v0.1, 2026-10-04. First release. No earlier versions.

## Exhibits

This section holds every table and figure cited above. Each item gives its purpose, the section that cites it, and its source.

### Table 4.1. Document Classes and Required Components

**Purpose:** Shows what each document class must include and may omit.  
**Cited in:** Section 4  
**Source:** Preparer's design, drawing on ChatGPT's proportional-class idea.

| Class | Must include | May omit |
|---|---|---|
| Short Record | Core Block; purpose line; result or decision; next action or "no further action"; revision note | Executive summary and table of contents (proposed; see Open Question 1) |
| Standard Document | Core Block; executive summary; table of contents; purpose and intended outcome; narrative body; next actions | List of exhibits when fewer than five exhibits |
| Major Report | All of the above; limitations; references; list of exhibits when five or more | Nothing from the Core Block |
| Technical Annex or Dataset | Core Block; link to parent document; numbered exhibits with source notes | Executive summary; long narrative beyond a short guide |

### Table 5.1. Status Words

**Purpose:** Defines the seven status words and who may set each.  
**Cited in:** Section 5  
**Source:** Preparer's design, reducing ChatGPT's 18 candidate words.

| Status | Meaning | Who may set |
|---|---|---|
| DRAFT | First pass. Expect large changes. | Preparer |
| PRELIMINARY | Early but complete enough to review. | Preparer |
| PROVISIONAL | Usable now. Subject to revision. | Human coordinator |
| UNDER REVIEW | In a formal review. | Preparer, on request |
| ADOPTED | Accepted as governing or authoritative. | Human coordinator only |
| SUPERSEDED | Replaced by a named newer version. | Human coordinator |
| ARCHIVED | Kept as a record. Not current. | Human coordinator |

### Table 12.1. Format Failure Types

**Purpose:** Names the six ways a format can fail and the response each needs.  
**Cited in:** Section 12  
**Source:** Adapted from ChatGPT's taxonomy and Perplexity's notice fields.

| Failure type | What happened | Required response |
|---|---|---|
| Generation failure | The tool cannot create that file type | Say so. Deliver other formats. Supply Markdown and a conversion path. |
| Conversion failure | Conversion stopped or produced errors | Report where it failed. Deliver the last good file and the source. |
| Rendering failure | The file exists but displays wrongly | Do not call it delivered. Describe the defect. Supply a fix or alternative. |
| Layout incompatibility | Content cannot fit the format cleanly | Restructure per Section 9.8 or record an exception. |
| Unsupported feature | The format lacks a required feature | Name the substitute and record the deviation. |
| Incomplete export | The file opens but content is missing | List what is missing. Flag FORMAT INCOMPLETE. |

### Figure 12.1. Diagram: Delivery Decision Flow

**Purpose:** Shows the steps from producing the three formats to either a clean delivery or a flagged one.  
**Cited in:** Section 12  
**Source:** Preparer's design from Section 12.3.  
**Alternative text:** A vertical flowchart of the eight steps in Section 12.3. A yes at step 3 leads to a box reading delivery complete, run the gate. A no leads down through steps 4 to 8, and then a line returns to step 3.

![Flowchart of the delivery decision flow: yes at step 3 ends in delivery complete; no leads through steps 4 to 8 and back to step 3.](assets/figure-12-1-delivery-flow.png)

### Table 15.1. Filename Codes

**Purpose:** Lists the codes used in the filename pattern.  
**Cited in:** Section 15  
**Source:** Preparer's design.

| Field | Codes | Meaning |
|---|---|---|
| Entity | OAL, ONE, LC, JOINT, EXT | Omniversal Architect Labs; One Industries; Lewis Corp; two or more entities; external material |
| Type | STD, RPT, SIM, SPEC, REV, DEC, MEMO, EXP, CON, COL | Standard; report; simulation report; specification; adversarial review; decision record; memo; experimental exercise; concept or proposal; multi-AI collaborative document |
| Status | DRAFT, PRELIM, PROV, REVIEW, ADOPTED | Matches Table 5.1. Superseded and archived are recorded in the index, not in filenames. |

### Table 15.2. Version Increments

**Purpose:** Defines what causes each version number to change.  
**Cited in:** Section 15  
**Source:** Preparer's design, using a semantic-style scheme suggested by ChatGPT.

| Change | Result | Example |
|---|---|---|
| First draft | v0.1 | v0.1 |
| Revision before adoption | Next v0.x | v0.1 to v0.2 |
| Adopted by the human coordinator | v1.0 | v0.4 to v1.0 |
| Clarification or optional addition after adoption | Minor | v1.0 to v1.1 |
| Change that makes older compliant documents noncompliant | Major | v1.1 to v2.0 |

### Table 24.1. Summary of the Five Responses

**Purpose:** Summarizes each response's strongest contribution and main gap.  
**Cited in:** Section 24  
**Source:** Preparer's review of the pasted responses (Sections 22 and 23).

| Response | Strongest contribution | Main gap |
|---|---|---|
| ChatGPT | Governance system, failure taxonomy, proportional classes | Long; risks bureaucracy |
| Claude (earlier) | Concise, faithful exhibit rule | Too thin to govern |
| Perplexity | Per-format rules and notice template | Used a table itself; heavy for short documents |
| Grok | Phone-first, first-screen labels, testable gate | Omits versioning and governance |
| Copilot | Clear metadata and purpose set | Approved-status example; little proportion |

### Table 25.1. Conflicts and Rules Adopted

**Purpose:** Lists each conflict found among the responses and the rule chosen.  
**Cited in:** Section 25  
**Source:** Preparer's review and design decisions.

| Conflict | Rule adopted | Section |
|---|---|---|
| Body tables versus exhibits only | Exhibits only, plus stacked lines | 8.4, 9 |
| Full apparatus versus proportion | Strict default; lighter rule proposed | 4.5 |
| Mandatory title page versus restraint | No title page required | 8.9 |
| Status in filename versus stable links | Keep code; archive, never rename | 15.1, 15.4 |
| Handing off a missing format | Recommend; coordinator assigns | 12.5 |
| 18 status words versus 4 | Seven words with owners | 5.4, 5.6 |
| Density versus accuracy ranking | Accuracy first | 8.11 |
| AI marking its own work approved | Forbidden | 5.6, 13.7 |
| Unverifiable outside citations | Verify or label unverified | 10.4 |
