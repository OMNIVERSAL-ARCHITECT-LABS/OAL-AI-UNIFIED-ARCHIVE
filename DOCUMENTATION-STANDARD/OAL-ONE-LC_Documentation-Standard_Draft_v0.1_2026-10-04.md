# Documentation Design, Presentation, Format, and Publication Standard

Shared workspace standard for Omniversal Architect Labs, One Industries, and Lewis Corp

Document ID: OAL-ONE-LC-STD-DOC-001
Version: v0.1
Status: draft
Work type: standard
Simulation status: non-simulation
Connection: standalone governance document for the collaborative workspace
Distribution: internal working draft, intended for later GitHub publication after review

Prepared by: Grok 4.7 (xAI)
Role: preparer of this draft. Not the author of canon. Not an endorser. Not authorized to adopt this standard.
Prepared on: 2026-10-04
Prepared at: 10:49 AM PDT (UTC-7)
Entity scope: Shared — Omniversal Architect Labs (OAL), One Industries, and Lewis Corp
Related broader topic: collaborative documentation practice
What this document is not a claim on: It does not adopt the standard. It is not canon. It is not an endorsement of any named entity, scenario, or prior AI output. It does not find that OAL, One Industries, or Lewis Corp is real, fictional, operational, or published. It does not decide a legal, financial, scientific, or employment matter.

## Purpose and intended result

This document exists to give the workspace one executable rule set for how later documents are designed, labeled, written, referenced, and delivered.

Intended result: a human or an AI can receive this draft, apply it to the next project document, and know whether that document is acceptable. Success is a later document that states its purpose, can be read as prose on a phone, labels its entity and status, numbers its exhibits, and arrives as Markdown, DOCX, and PDF, or records an honest format gap.

This draft does not accomplish adoption. Adoption requires a separate review by the workspace coordinator. If that review does not happen, this file remains a proposal.

Audience: the workspace coordinator, collaborating AI systems, and a later GitHub reader opening the file on a phone.

## Executive summary

Recent project documents arrived as walls of rows and columns. A reader on a phone could not read them as documents. The applications also disagreed with each other on presentation when no standard was specified. This draft closes that gap.

The rule is simple. A document must say why it exists and what it is supposed to accomplish. The body is prose. Tables, charts, and figures are numbered exhibits, cited from the prose, and collected in a designated section. The first screen names the entity, the work type, the simulation status, the broader topic or the standalone label, and what the document does not claim. The preparer is named, with date, time, and timezone. PDF and DOCX carry page numbers. The same substance is delivered as Markdown, DOCX, and PDF. If a format cannot be rendered, the preparer says so and supplies a conversion path. The preparer does not claim a file that was not written.

The standard governs presentation, classification, and delivery. It does not exist to argue whether the named entities or scenarios are real. That argument is allowed only when it is the stated purpose of a particular document.

This file is a draft. It is not adopted.

## Table of contents

1. Scope
2. Purpose-and-execution test
3. Labels
4. Non-claims and claim language
5. Document classes
6. Front matter
7. Executive summary and contents
8. Reading and mobile design
9. Exhibits, numbering, and cross-reference
10. Formats and the failure protocol
11. Names, versions, and GitHub
12. Preparer accountability
13. Exceptions and change control
14. Completion gate
15. Architectures by document type
16. Patterns that fail
17. Review of the 2026-10-04 team responses
18. Exhibits
19. Next action
20. Revision note

## 1. Scope

This standard applies to substantive documents generated for the collaborative workspace of Omniversal Architect Labs, One Industries, and Lewis Corp, including joint work and work later published to the workspace repository.

It applies to research notes, simulation reports, specifications, reviews, decision records, memos, and standards. It does not apply to a one-line chat reply, a commit message, or a scratch calculation that is not being filed as a document.

A document belongs to one entity label or to the shared label. Do not blend OAL, One Industries, and Lewis Corp into one voice. If a document serves more than one, label it Shared and name the entities.

## 2. Purpose-and-execution test

Before a substantive document is written, the preparer answers these questions in the file, not only in the prompt.

Why does this document exist? What question, record, decision, specification, test, or instruction does it address? Who is expected to read it? What should that reader know, decide, perform, or verify afterward? What does the file actually accomplish? Is the work descriptive, prescriptive, exploratory, evidentiary, instructional, archival, or decisional? Does anything have to happen after publication? How would a later reader tell that the document succeeded?

If no purpose, audience, or result can be named, do not create the document.

A document that describes an intention is not a document that shows execution. Say which one it is. "No further action" is an acceptable result when it is true.

The goal of a document is not automatically an argument. If the goal is to open a debate, or to classify something as fictional, real, simulated, or historical, state that goal in the purpose block. Otherwise do not spend the document on that classification.

## 3. Labels

The first screen of every substantive document carries a label block. The same labels appear in the filename, the opening block, and the executive summary. Do not rely on color. A grayscale print, a screen reader, and a format conversion must still carry the meaning.

Entity is one of: OAL, One Industries, Lewis Corp, Shared, or External. Shared means two or more of the named entities. External means third-party material used for comparison.

Work type is one of: standard, operational note, simulation, preliminary, decision record, review, specification, or a stated other type. Do not invent a second name for the same type inside one document.

Maturity is separate from work type. Use only these status words: draft, provisional, under review, reviewed, adopted, superseded, retired. Default is draft. A draft is not adopted. Provisional means usable for the stated next step and still subject to change. Reviewed means a named reviewer read it. Adopted means the workspace coordinator accepted it for use. Superseded and retired point to the replacement or state that there is none.

Simulation status is yes or no. If yes, name the simulation type, the input source, whether the run was proposed or executed, and whether a number is simulated, observed, calculated, estimated, or assumed. A reader must not have to guess where a figure came from.

Connection is the broader topic this document attaches to, or the word standalone.

See Table 1.1 in Exhibits for the document classes that use these labels. See Table 1.2 in Exhibits for the status words.

## 4. Non-claims and claim language

Every document states what it is not a claim on. The statement is specific to that document. Do not paste a universal disclaimer and stop thinking.

At minimum, a draft states that it is not canon, not an endorsement, and not a finding that a named entity or scenario is real or fictional. Add any further boundary the document actually needs, such as "not a validated operational system," "not evidence that a modeled event occurred," or "not legal, financial, or medical advice."

Claim language stays at the strength of the support. Use "is" for a stated definition inside the document. Use "was observed," "was simulated," "was calculated," "was reported," "is assumed," "is proposed," or "remains unknown" when that is the real status. Do not let a confident tone upgrade an assumption into a finding.

## 5. Document classes

Length follows the job. The standard is not a reason to make a short record long.

A short record is a memo, log, or note. It needs the label block, purpose, preparer, timestamp, and non-claim. It does not need a multi-page front matter.

A standard document is the usual project report, specification, or review. It needs the full front matter in Section 6, prose body, exhibits if any, and the completion gate.

A major report is a validation, architecture, or program document. It adds a revision history, related-document list, and a list of exhibits.

A technical annex holds structured data. It may be dense. It still has a prose cover that says what the data are, how they were derived, and what they are not.

See Table 1.1 in Exhibits.

## 6. Front matter

A standard document opens in this order.

Title. Document identifier, if the project uses one. Version. Entity. Work type. Maturity. Simulation status. Connection. Distribution, if it matters. Preparer, named as the model or person who wrote the file. Role. Date. Time and timezone. Audience. Purpose and intended result. Non-claim. Executive summary. Table of contents.

An AI preparer names the system. Do not list a person as preparer of text the person did not write. If a person directed the work and a model wrote the file, say both, and say who did which.

Page numbers are required in PDF and DOCX, in the footer, as the current page. Markdown has no pages. The Markdown file states that page numbers apply to the paginated formats.

## 7. Executive summary and contents

The executive summary is not a second introduction. In a few short paragraphs it says why the document exists, what was done, what was found or decided, what is unresolved, and what happens next. A reader who stops there should know whether to continue.

Substantive documents include a table of contents that matches the headings. In DOCX and PDF, use a generated contents list where the tool can do so. Do not hand-maintain page numbers that drift from the file. In Markdown, a linked list of headings is enough.

Headings use a numbered hierarchy: 1, 1.1, 1.1.1. Stop at three levels unless the document is a major report. Major sections are separated by headings, not by decoration.

## 8. Reading and mobile design

Most readers will open these files on a phone and scroll vertically. Design for that reader first.

The body is prose a non-specialist can read. Short sections. One idea in a section. Short paragraphs. Define a specialized term at first use. Do not make a grid the only way to learn the point.

Wide tables, multi-column layouts, and row-and-column figures are not the body. If a comparison is needed, say the comparison in sentences, then point to the exhibit. If a table is too wide for a portrait phone, split it, restack it as labeled fields, or move it to the annex and summarize it.

Meaning does not depend on color, exact page position, or a proprietary effect. A conversion that drops the styling must still leave a readable document.

Desktop layout does not outrank phone reading.

## 9. Exhibits, numbering, and cross-reference

Tables, charts, diagrams, and figures live in the Exhibits section unless a single narrow list is clearer in place. Even then, it is numbered.

Number tables as Table 1.1, Table 1.2, and figures as Figure 1.1. Use the section number as the first part. Do not restart at 1 inside every subsection if that creates duplicates.

Every exhibit has a number, a title, one sentence on why it is there, and the section that cites it. The prose cites it by number and location, in the form "See Table 1.2 in Exhibits." Do not write "the table below" or "the chart above" as the only reference. Files reflow.

A table earns its place when it answers a lookup question better than a sentence. It does not hold paragraph-length policy. A figure earns its place when it shows a relationship, a flow, a result, or a structure the prose needs. Decorative images are not exhibits.

If a document has more than three exhibits, add a short list of exhibits before the body ends, with number, title, and citing section. A two-page note with one table does not need that list.

## 10. Formats and the failure protocol

Completed project documentation is delivered in three formats with the same substance.

Markdown is the version-controlled source. It must be readable as raw text. DOCX is the editable office copy, with real heading styles. PDF is the stable reading copy, with selectable text and page numbers. An image-only PDF does not qualify.

Claims, dates, numbers, headings, and exhibit numbers do not diverge across the three. Layout may differ where the format requires it.

If a format cannot be rendered, the preparer does not claim that it was. The preparer states which format failed and the actual limitation, delivers every format that was produced, supplies the full source in Markdown, names the local conversion step, and records a format-gap note in the file. The document is marked format-incomplete until the gap is closed or a named exception is accepted. A chat paste is not a DOCX or a PDF.

See Table 1.3 in Exhibits for the role of each format.

## 11. Names, versions, and GitHub

File names use entity, document type, status, version, and date, with hyphens and no spaces. Example: OAL-ONE-LC_Documentation-Standard_Draft_v0.1_2026-10-04.md. The DOCX and PDF twins use the same stem.

Version numbers move for a reason. v0.x is draft. v1.0 is the first adopted text. A later v1.x corrects or clarifies without changing a rule. v2.0 changes a rule. Superseded files stay in history. Do not overwrite an adopted file in place.

The repository keeps the Markdown source, the DOCX, and the PDF together, or links them from the Markdown. An index names the current draft or adopted file. Related documents are named when they exist: parent, supersedes, superseded by, depends on. Do not invent relationships.

## 12. Preparer accountability

The preparer line is part of the record. Later readers, including other models, will treat the structure, the labels, and the density as evidence of how that preparer presents information.

An AI preparer identifies itself, does not invent a completed test, separates analysis from execution, separates simulated output from observation, and does not silently replace this standard with a house style. Different models may prefer different tones. The delivered file still follows this standard.

If more than one system contributes, name the primary preparer, the contributing systems, and any reviewer. Participation is not consensus. Keep a relevant disagreement visible.

## 13. Exceptions and change control

A requirement may be skipped when following it would make the file worse, when the format cannot support it, or when the document class does not need it. A significant skip is written down: requirement, deviation, reason, impact, and date. A missing preparer line or a missing purpose is not a minor skip.

This draft can be changed only by a later version that says what changed. The workspace coordinator accepts or rejects adoption. A model does not adopt the standard by writing it. Previous drafts remain available. A project document names the standard version it followed.

## 14. Completion gate

A document is not ready if any of these are true.

It has no stated purpose or no stated result. The entity, work type, maturity, or simulation status is ambiguous. The preparer, date, or timezone is missing. The non-claim is missing. The body cannot be read as prose on a phone. An exhibit is unnumbered, untitled, or uncited. The prose says "the table below" as its only pointer. PDF, DOCX, or Markdown is missing and no format-gap note exists. The file argues real-versus-fictional status without stating that as its purpose. The preparer claims a file that was not written.

Passing the gate means the file is ready for review. It does not mean the file is adopted or canon.

## 15. Architectures by document type

A research note opens with the label block and purpose, states the question, gives the prose finding, and puts sources and any comparison grid in Exhibits. It changes from a specification because its result is a finding, not a rule.

A simulation report adds the simulation block from Section 3 and separates proposed runs from executed runs. It changes from a research note because a number may be synthetic.

A specification states the requirement, the test that would show compliance, and what is out of scope. It changes from a report because it is prescriptive.

A review states the object reviewed, the criteria, the disagreements, and what was not checked. It does not flatten dissent into a single verdict unless the purpose is a verdict.

A decision record states the decision, the alternatives considered, and what happens next. It is short unless the reasoning needs length.

A concept note is marked preliminary. It says it is not a specification and not an executed result.

A public repository copy uses the same substance as the internal file and states the distribution label. It does not add a second argument about the status of the entities.

## 16. Patterns that fail

A file that is only tables fails, even if every cell is accurate. A file that cites "the figure above" fails once the formats reflow. A file that says it is a PDF, and links nothing, fails. A file that opens with an eight-column matrix fails the phone test. A file that uses the word approved for an unreviewed draft fails. A file that argues the entities are fictional, or real, without stating that purpose, fails. A file whose only outcome is that a file now exists fails the purpose test.

## 17. Review of the 2026-10-04 team responses

This section is an accompanying review of the prompt drafts submitted on 2026-10-04. It is not a rule of the standard. It is not a ranking of vendors. It records what this preparer kept, what this preparer rejected, and why.

The shared request was a structured prompt that would design the documentation standard, then an independent execution of that prompt. Four systems with workspace history answered as prompt authors. Microsoft Copilot answered as a prompt author and asked that its pass be weighted lower, because Copilot 365 does not hold this workspace's conversation history. That limitation is real for this task. This review treats Copilot as a useful cross-check, not as a source of workspace-specific rules.

ChatGPT treated the job as governance rather than a style sheet. That is the right frame. The purpose-and-execution test, the format-exception declaration, the separation of simulated and observed values, proportional document classes, and the demand that the standard survive an adversarial pass are kept. The proposed status list is not kept. Concept, working draft, preliminary, provisional, proposed, experimental, simulation, test article, validation pending, verified, validated, approved, and ratified overlap, and they mix maturity with work type. A later model will pick a different word each time. This draft splits maturity from work type and uses a short status list. ChatGPT's commission is also longer than a preparer can apply without dropping clauses. Length was not treated as completeness.

Claude matched the original complaint most closely: phone reading, prose instead of grids, exhibits by item number, a non-claim, a purpose test, and a fallback when a format cannot be rendered. That core is kept. Claude's absolute ban on any table in the body is softened. A narrow labeled list may stay in place if it is numbered and readable. Claude under-specified versioning, repository naming, evidence labels, and how the standard itself changes. Those gaps are filled here.

Perplexity produced the most operational policy prompt. The role split is kept: Markdown as the maintainable source, DOCX as the editable copy, PDF as the stable copy. The recovery notice and the rule that a table is a data tool, not a layout tool, are kept. Two choices are not kept. The response demonstrated the failure mode it warned against, by presenting a wide control-block table as the recommended front matter. This draft uses a stacked label block instead. The request that every standard cite W3C and Section 508 is out of scope for ordinary project notes. Accessibility rules here are practical: heading order, selectable text, no color-only meaning, and no essential content that requires sideways scrolling.

The earlier Grok pass was a short executable prompt, correctly marked draft and not canon, and correctly unwilling to adopt itself. It is the seed of Sections 2, 3, 8, 9, 10, and 14. It was not yet a standard. It lacked document classes, version rules, repository rules, and a review of the other passes. This file is the execution that prompt asked for.

Copilot's prompt repeats the purpose test, the three formats, mobile reading, and preparer identity. Those points agree with the others. It is not used as a primary source, for the reason Copilot gave. Three of its instructions conflict with this draft. "No exceptions" on a full cover page fights the short-record class. An example status of Approved, on an unreviewed prompt, models the wrong maturity word. Requiring both an author and a preparer, without saying how they differ, will produce double attribution. The rendering note that a missing export must not stop the writing is kept, and it is already covered by the format-gap protocol.

No response is consensus. Agreement on phone reading, three formats, named preparers, and purpose-before-production is strong. Agreement on the status taxonomy is absent. This draft chooses the smaller taxonomy on purpose.

See Table 2.1 in Exhibits for the kept and rejected points.

## 18. Exhibits

### Table 1.1. Document classes

Purpose: show which front-matter rules apply to which class. Cited from Section 5.

Short record. Needs label block, purpose, preparer, timestamp, and non-claim. Does not need a long contents list.

Standard document. Needs the full front matter in Section 6, a prose body, numbered exhibits if any, and the completion gate.

Major report. Adds revision history, related documents, and a list of exhibits.

Technical annex. May be dense. Needs a prose cover stating derivation and non-claims.

### Table 1.2. Status words

Purpose: stop maturity and work type from sharing one list. Cited from Section 3.

Draft. Written, not accepted. This is the default.

Provisional. Usable for the stated next step, still subject to change.

Under review. Sent to a named reviewer. Not yet reviewed.

Reviewed. A named reviewer has read it. Not the same as adopted.

Adopted. The workspace coordinator accepted it for use.

Superseded. Replaced by a named later version.

Retired. Withdrawn. No current replacement, or replacement explicitly declined.

### Table 1.3. Format roles

Purpose: say why three files exist. Cited from Section 10.

Markdown. Version-controlled source. Must be readable as raw text.

DOCX. Editable office copy. Uses heading styles, not hand-formatted size changes only.

PDF. Stable reading copy. Selectable text, footer page numbers, no image-only pages.

A missing file is a format gap, not a silent omission.

### Table 2.1. Review disposition

Purpose: record what this draft did with the 2026-10-04 responses. Cited from Section 17. This table is a review aid, not a rule.

ChatGPT. Kept the governance frame, purpose test, format exception, and proportional classes. Rejected the long overlapping status list.

Claude. Kept phone reading, exhibits by number, non-claim, and fallback. Softened the total ban on in-body tables. Filled the gaps on versioning and change control.

Perplexity. Kept format roles, recovery notice, and tables-as-data. Rejected the wide control-block table and the requirement to cite accessibility standards in ordinary notes.

Grok, prior pass. Used as the seed prompt. Expanded into this standard. Not treated as already adopted.

Copilot. Used as a cross-check only, at Copilot's request, because of missing workspace history. Rejected "no exceptions," the Approved example, and undifferentiated author-plus-preparer.

## 19. Next action

No adoption is requested by this file. The next useful action is a coordinator review of Sections 3, 5, 10, and 14. If those four hold, the remaining sections can be edited without reopening the design. Until that review, later documents may follow this draft and must label the version they followed. They must not call it adopted.

## 20. Revision note

v0.1, 2026-10-04, 10:49 AM PDT. Initial independent draft, prepared by Grok 4.7. Includes the standard and the accompanying review of the same-day team responses. Not reviewed. Not adopted. Not canon.

Format gap: none at the time of writing. Markdown, DOCX, and PDF were produced together from this source. If a later copy is missing a format, treat that copy as format-incomplete and apply Section 10.
