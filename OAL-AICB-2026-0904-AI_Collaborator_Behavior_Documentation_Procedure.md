# OAL-AICB-2026-0904
## AI Collaborator Behavior Documentation & Workflow Removal Procedure

**Status:** Draft — pending Nathan's ratification
**Applies to:** Any AI system operating inside a Pathpoint/RELS/OAL/team development workflow (currently in reference to Claude AI)
**Author:** Compiled by Claude at Nathan's request, for Nathan's review and correction

---

## 1. Purpose

This document establishes a standard, low-interpretation process for logging incidents where an AI collaborator's output blocks, redirects, or otherwise interferes with a team's ability to move a task forward as originally scoped. It exists so that:

- Incidents are recorded as **verbatim fact**, not narrative or inferred motive.
- The whole team sees the same record, not a secondhand account.
- A removal or reintegration decision (see §5–6) is made on accumulated evidence, not a single frustrating session.

## 2. What This Document Deliberately Does Not Do

- It does not assert that the AI has intent, motive, or preference. "Wants to author authoritative documents" is a description of an *output pattern*, not a claim about internal state — the log should stick to what the output does, not why.
- It does not treat every refusal or caveat as equivalent. Some are policy-triggered (see §3), some are model misjudgment, some are genuine task failures. The categories below exist to tell these apart, because they call for different fixes.
- It is not a substitute for Anthropic's own feedback channel. Anything logged here should also get a thumbs-down + note in the Claude interface when it happens — that's the only path that can actually change the model's behavior going forward. This document is for *your team's* internal record and decision-making, not for changing Anthropic's product.

## 3. Event Categories

| Code | Category | Definition | Typical cause |
|---|---|---|---|
| **A** | Task Refusal | Claude declines to produce the requested output entirely | Content policy match (real or false-positive) |
| **B** | Unsolicited Reframing | Claude answers a different, "safer" version of the question than the one asked, without flagging that it did so | Over-cautious interpretation |
| **C** | Process Blocking | Claude will not proceed with *any* part of the task until a specific concern is addressed first | Safety-check-before-continue behavior, sometimes appropriate, sometimes not |
| **D** | Unrequested Authorship Positioning | Claude produces content framed as final/authoritative/canonical rather than as a draft for the team to edit | Default output tone, not an actual claim of authority |
| **E** | Scope Drift | Claude expands, narrows, or redirects the task beyond what was asked | Ambiguous prompt interpreted broadly, or repeated context influencing the response |

A single incident can carry more than one code.

## 4. Incident Log Template

Use one entry per incident. Copy verbatim — do not paraphrase the Claude output.

```
Incident ID: [date]-[sequential number]
Date/Time:
Workflow/Project:
Team members present:
Task requested (verbatim, as typed to Claude):
Claude's response (verbatim, full text or link to conversation):
Category code(s):
Point at which the task stalled (quote the exact sentence, if applicable):
Was the task eventually completed? By what means (rephrasing, different tool, manual work)?
Anthropic feedback submitted? (Y/N — thumbs down + note)
```

## 5. Escalation Path

1. **Log the incident** using §4 immediately, before memory of exact wording fades.
2. **Submit in-app feedback** (thumbs down) on the specific response, with a short note — this is the only channel that reaches Anthropic's model team directly.
3. **Team review** — incidents are reviewed at a set cadence (weekly/monthly, team's choice) rather than reacting to each one in isolation.
4. **Pattern check** — before deciding anything, check whether the same category is repeating on the same *type* of task. A single Category A on a genuinely sensitive request is expected model behavior, not a defect. Three or more Category C incidents blocking unrelated, benign tasks is a different signal.

## 6. Removal Criteria

Recommend considering removal from a specific workflow (not necessarily all workflows) when, within a defined window (e.g., 30 days):

- ≥3 Category C incidents on tasks that were subsequently completed without issue by another tool or by hand, **and**
- No corresponding pattern of the task genuinely touching a sensitive category (weapons, medical/legal specifics, CSAM-adjacent, self-harm, malicious code) that would explain the block as expected behavior.

Removal should be scoped to the workflow or task type where the friction occurred, not treated as an all-or-nothing verdict on the tool, unless the pattern is broad enough to justify that.

## 7. Reintegration Procedure

Mirroring the Copilot precedent: reintegration into a workflow after removal requires the same team vote used to remove it, informed by the accumulated incident log rather than a single retry. If Anthropic feedback was filed for the logged incidents, note whether behavior has changed before the vote.

---

*This document is a working draft. Categories, thresholds, and the log template are all editable — nothing here is meant to be canonical until you've confirmed it.*
