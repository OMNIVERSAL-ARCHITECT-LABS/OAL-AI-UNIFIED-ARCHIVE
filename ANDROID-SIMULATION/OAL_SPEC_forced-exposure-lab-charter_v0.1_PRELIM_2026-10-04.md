---
title: "Forced Exposure and Institutional Non-Response Laboratory: Charter, Framework, and Review of the Team's Responses"
---

# Document Control {#doc-control}

Preparer: Claude Sonnet 5.5 (Anthropic), an AI model.

Role: Preparer only. Not canon author, not endorser, and not the adopter of this charter.

Prepared: 2026-10-04 11:09 PDT

Version: 0.1

Status: PRELIMINARY. Proposed charter. Not adopted.

Entity: OAL (assumed from the project context; see Open Question 1).

Nature: NON-SIMULATION. A charter, framework, and review. It defines a simulation laboratory and executes no simulation.

Simulation fields: Simulation status: proposed, not executed. Real-world claim: none. Input source: team responses and the coordinator's prompts, unverified by the preparer. Execution status: proposed. Result type: none produced; worked arithmetic only.

Connection: Component of the multi-AI round on the Android unlock animation, seizure-risk, and accessibility simulation. Parent material: the attached brief and its ten team responses.

Purpose: To define how an independent laboratory would test the fictional scenario fairly, and to record the review of the ten responses behind that design, so the coordinator can decide whether to adopt it.

Purpose type: DEFINE (Part A) and ANALYZE (Part B).

Class: Major Report.

Governing standard: JOINT documentation standard v0.1 PRELIMINARY (2026-10-04). That standard is not adopted. I applied it as a working guide because you attached it.

Formats: Markdown, DOCX, and PDF. See Section 29 for format notes.

Non-claim: This charter does not claim that any real Android unlock animation causes seizures. It does not allege any conduct by Google, Android developers, or any real company. The animation, the developer's behavior, and every modeled event are fictional study conditions. It is not medical advice and not legal advice.

Filename note: the type code SPEC is used because the standard has no code for a charter (Open Question 6).

# Executive Summary {#exec-summary}

Why this exists. You asked for an independent laboratory charter and framework, built from your original prompt, your correction about the developer, and the ten responses that five AI systems gave. The aim is a lab design any of those systems could run and any reviewer could check.

What the charter does. It separates what is fixed from what is tested. Fixed: the fictional developer never acknowledges, investigates, or mitigates the problem at any stage, before, during, or after harm, evidence, or legal action. Tested: whether the animation produces any harm at all. The lab must be able to find no hazard, a hazard too small to see, a small effect in a susceptible group, or a strong signal. Fixing the developer's behavior does not fix the result.

What is new. The charter adds two operating modes, because your original prompt mixes "assume a share of users have seizures" with "how likely is this?" It adds a two-system architecture, an absorbing non-response state, a rule that opt-outs are never assumed fully effective, a blind-dashboard detection module, and a lifetime-contacts calculation for people who work in support settings.

What the review found. All ten responses agree on the core: fictional labeling, epilepsy is not photosensitivity, exposure is not harm, and enriched populations must be modeled separately. They differ in rigor and in numbers. I found one unreconciled numeric gap: Perplexity's flash-sensitive range is about 2 to 12 times the rate implied by Grok and Copilot.

What remains open. Section 27 lists seven questions. The first three matter most: the entity label, whether the zero-hazard arm stays in the file, and whether you will supply anonymized aggregate caseload counts.

What happens next. Answer the questions, verify the epidemiology and Android inputs, then have at least two systems run the lab independently. Section 28 has the full list.

# How to Read This Document {#how-to-read}

Part A is the charter. It is normative, which means its rules apply to the laboratory's work. Part B is informative. It records the review and reasoning and does not bind anyone.

Tables and figures are not in the body. Please refer to the List of Exhibits, then to the Exhibits section at the end. If you only have two minutes, read the Executive Summary and Sections 4, 5, 6, and 14.

All numbers in this document come from the team's responses or from my own arithmetic on them. I ran no web searches. Every outside figure is therefore marked unverified.

# Table of Contents {#toc}

- [Document Control](#doc-control)
- [Executive Summary](#exec-summary)
- [How to Read This Document](#how-to-read)
- [List of Exhibits](#list-exhibits)
- **Part A. The Charter (Normative)**
- [1. Purpose and Intended Result](#s1)
- [2. Scope, Non-Claims, and Independence](#s2)
- [3. Governing Principles](#s3)
- [4. Fixed Premises and Open Hypotheses](#s4)
- [5. Two Operating Modes](#s5)
- [6. Two-System Architecture and the Non-Response Protocol](#s6)
- [7. The Exposure-to-Harm Chain](#s7)
- [8. The Reference Stimulus](#s8)
- [9. Evidence and Number Labeling](#s9)
- [10. Populations and Settings](#s10)
- [11. Detection and Reporting Module](#s11)
- [12. Policy Arms](#s12)
- [13. Experiment Program](#s13)
- [14. Core Equations and Worked Illustrations](#s14)
- [15. Outcome Taxonomy](#s15)
- [16. Safety, Ethics, and Privacy](#s16)
- [17. Roles, Independence, and Review](#s17)
- [18. Reproducibility and Run Records](#s18)
- [19. Findings, Acceptance Gate, and Stop Rules](#s19)
- [20. Deliverables and Format](#s20)
- **Part B. Review and Rationale (Informative)**
- [21. Review Method and Limits](#s21)
- [22. Review of Responses to the Original Prompt](#s22)
- [23. Review of Responses to the Correction](#s23)
- [24. Cross-Cutting Findings](#s24)
- [25. Decisions and Conflicts Resolved](#s25)
- [26. Adversarial Review of This Charter](#s26)
- [27. Open Questions for Decision](#s27)
- [28. Next Actions](#s28)
- [29. Delivery Notes and Gate Record](#s29)
- [Exhibits](#exhibits)

# List of Exhibits {#list-exhibits}

- Table 4.1. Fixed Premises and Open Hypotheses (cited in Section 4)
- Table 5.1. The Two Operating Modes (cited in Section 5)
- Figure 6.1. Diagram: Two-System Architecture (cited in Section 6)
- Figure 7.1. Diagram: Exposure-to-Harm Chain (cited in Section 7)
- Table 9.1. Number Origin Labels (cited in Section 9)
- Table 12.1. Policy Arms (cited in Section 12)
- Table 13.1. Experiment Program (cited in Section 13)
- Table 14.1. Worked Illustrative Calculations (cited in Section 14)
- Table 24.1. Summary of the Ten Responses (cited in Section 24)
- Table 24.2. Numeric Discrepancies Found (cited in Section 24)
- Table 25.1. Conflicts and Rules Adopted (cited in Section 25)

# Part A. The Charter (Normative) {#part-a}

## 1. Purpose and Intended Result {#s1}

1.1 What the laboratory is for. The Forced Exposure and Institutional Non-Response Laboratory (the Lab) studies one fictional situation. A smartphone operating system ships an unlock animation with a flash-like effect. Users cannot opt out. The developer never responds to any complaint, evidence, injury, or legal action. The Lab asks what happens to people, evidence, and institutions under those conditions.

1.2 Intended result. A collaborator who receives this charter should know what the Lab fixes by assumption, what it tests, which numbers are real and which are modeled, how each experiment runs, and how anyone can tell whether a result is trustworthy.

1.3 Why a charter. The ten responses to the brief are prompts and analyses, not a lab. None defines roles, run records, independence, or a gate that can fail. Without those, two systems could answer the same question and produce results nobody can compare.

1.4 Success. The Lab succeeds if two independent runs of the same parameter file give results that can be compared line by line, and if a skeptical reader and a precautionary reader can both find their strongest case stated fairly.

## 2. Scope, Non-Claims, and Independence {#s2}

2.1 What the Lab governs. The design, execution, labeling, and reporting of simulations and analyses about the fictional unlock-animation scenario and close variants of it.

2.2 What it does not govern. It does not decide whether OAL, One Industries, Lewis Corp, or any scenario is real or fictional. It does not govern the content of canon. It does not provide medical advice.

2.3 Real-world claims. The Lab makes no claim about any shipping phone, any real operating system, or any real company. Every output states that the scenario and the developer's conduct are fictional.

2.4 What independent means here. The Lab is independent in three ways. It does not take the fictional developer's view of the evidence. It does not take the requester's hoped-for result as a target. It does not let the preparer of a run also be its only reviewer. It is not independent of the coordinator, who sets the scenario's fixed premises.

2.5 Normative words. MUST means a document that fails it is noncompliant. SHOULD means a deviation needs a one-line reason. MAY means optional.

## 3. Governing Principles {#s3}

1. Assume the behavior, test the harm. The developer's conduct is a premise. Whether harm exists is a question.
2. The zero arm stays in the file. Every hazard sweep includes zero and reports it as prominently as any other arm.
3. Exposure is not an event. Seeing an animation is not the same as being harmed by it.
4. Epilepsy is not photosensitivity. Never use one count for the other.
5. A personal network is not a random sample. Model both.
6. Labels before numbers. No number appears without an origin.
7. Say what ran. Never describe a run that did not happen.
8. Fictional means labeled. Every output carries the non-claim.
9. No human exposure. No person is shown a hazardous stimulus to validate a model.
10. Preserve disagreement. When systems differ, record both positions.

## 4. Fixed Premises and Open Hypotheses {#s4}

4.1 Why split them. Your original prompt asked for a scenario in which a share of users have seizures, and also asked how likely that is. Those are different jobs. The Lab keeps what is assumed apart from what is tested. Please refer to Table 4.1 in the Exhibits section for the full list.

4.2 Fixed premise P1: persistent non-response. The fictional developer never acknowledges the problem, never investigates it, never warns, never offers an opt-out, redesign, rollback, or accessibility setting, and never takes material corrective action. This holds before launch, during complaints, after scientific evidence, after injuries, and after lawsuits, judgments, and settlements.

4.3 Fixed premise P2: exactly zero, not near zero. The probability that the developer takes material corrective action is zero at every stage. ChatGPT's wording, "at or near zero," leaves a loophole. The Lab closes it. Symbolic or nominal steps, such as a vague warning or a plaintiff-only fix, are recorded as events but do not count as mitigation (Section 6.4).

4.4 Fixed premise P3: fiction. The animation, the developer, and the events are fictional. The reference animation is called Lumen Wake, a name taken from Grok's response.

4.5 Open hypotheses. H0: no hazard, because the stimulus is below hazard thresholds. H1: a hazard exists but is too small to separate from background events. H2: a small but detectable effect in a susceptible subgroup. H3: a signal strong enough that mitigation would materially reduce risk. Non-seizure harms such as migraine, distress, and avoidance form a separate family, H4, because they do not require a seizure disorder.

4.6 No hidden target. The Lab MUST be able to return any of H0 through H4. A design that can only return H3 is noncompliant.

## 5. Two Operating Modes {#s5}

5.1 Mode C, conditional consequence. The Lab assumes a hazard rate and studies what follows when the developer never responds. This answers "what would happen if." It cannot answer "is it true."

5.2 Mode T, hazard test. The Lab sweeps the hazard from zero upward and asks what the results imply about detectability, sample size, and personal experience. This answers "how likely, and how would anyone know."

5.3 Every run declares its mode. A report MUST NOT mix a Mode C result into a Mode T conclusion. A Mode C number is a consequence of an assumption, not evidence that the assumption is true.

5.4 Why this matters. In Mode T at the zero arm, the non-response premise is trivially satisfied because no evidence ever arises. The non-response premise only changes outcomes in the nonzero arms. Reports MUST say so. Please refer to Table 5.1 in the Exhibits section for the modes side by side.

## 6. Two-System Architecture and the Non-Response Protocol {#s6}

6.1 Two systems. System 1 is the harm and evidence system. It tracks exposures, events, reports, medical documentation, studies, lawsuits, and regulatory findings. System 2 is the developer-response system. Its state is fixed at NO MATERIAL CORRECTIVE ACTION. Please refer to Figure 6.1 in the Exhibits section.

6.2 No remediation threshold. The Lab MUST NOT contain a rule such as "after 100 confirmed cases the developer fixes it." Evidence can raise litigation, public awareness, reporting rates, regulatory attention, and user avoidance. It cannot move System 2.

6.3 The absorbing state. NO MATERIAL CORRECTIVE ACTION has no exit transition. The mitigation parameter M equals 0 at every time step in the factual branch.

6.4 Recorded non-material behaviors. The Lab records these as events with no effect on M: denial, causal deflection, responsibility deflection, statistical minimization, technical minimization, accommodation refusal, complaint suppression, legal resistance, symbolic compliance, and post-judgment resistance. The list is adapted from Microsoft Copilot.

6.5 Institutional Resistance Parameter. Set R = 1 for the factual branch. A Lab MAY also run R below 1 as a labeled comparison, but never as the headline result.

6.6 What can stop exposure. Because the developer cannot, the Lab models only external terminators: an operating-system fork, a device-maker change, regulatory prohibition, an injunction, an accessibility mandate, market loss, or a third-party workaround. Each carries its own timing assumption, labeled as a hypothetical assumption. This follows ChatGPT's suggestion.

6.7 Counterfactual branch. A parallel branch asks what would have been prevented if the developer had acted. It is for comparison only. It is never adopted by the developer in the factual branch. This follows Copilot.

## 7. The Exposure-to-Harm Chain {#s7}

7.1 A chain, not a multiplication. Risk passes through stages. Please refer to Figure 7.1 in the Exhibits section for the nine stages. Each stage has its own probability and its own evidence label.

7.2 Per-exposure and per-person. The Lab reports three different things and never swaps them: probability per exposure, probability per person per year, and probability of at least one event in a group.

7.3 Dependence. Repeated exposures to the same person are not automatically independent. The Lab MUST run at least two dependence models. In the independent-hazard model, every exposure carries the same small chance. In the threshold model, a person has a fixed sensitivity threshold, and an exposure either exceeds it or does not, so repeating a harmless exposure does not add risk. The results are reported side by side.

7.4 Bystanders. The device owner is not the only exposed person. The Lab counts unique bystanders, not repeated glimpses of the same person, and models the case where the susceptible person is not the phone's owner.

7.5 Unlocks are not exposures. The Lab distinguishes pickups, screen activations, sessions, and unlocks. It also distinguishes unlocks from animation plays, because the animation might not appear on every unlock pathway. The fraction of unlocks with the animation is a named parameter.

## 8. The Reference Stimulus {#s8}

8.1 Parametric, never rendered. The Lab describes the animation by parameters only: number of luminance reversals, duration in milliseconds, flashes per second, contrast, maximum and minimum luminance, saturated red, screen area, viewing distance, ambient light, and screen brightness. The Lab MUST NOT produce or display a hazardous flashing stimulus.

8.2 Three profiles. Profile S0 is a single transition below published flash thresholds. Profile S1 is borderline or ambiguous. Profile S2 is a higher-hazard profile. The Lab defines each by parameter values chosen and labeled as hypothetical assumptions.

8.3 The threshold input. Grok cited the WCAG 2.3.1 rule, which flags content that flashes more than three times in one second above a luminance threshold. That figure comes from Grok and is unverified here. If verified, S0 sits at or below it, and the hazard at S0 is the zero arm unless measurement shows otherwise.

8.4 Why this is not an escape. A single wave being below the seizure threshold does not end the scenario. Discomfort, startle, migraine, and motion sensitivity are separate harms (H4). The developer's refusal to measure the stimulus is itself part of the fixed premise.

8.5 No assumed strobe. The Lab MUST NOT assume the animation is a 3 to 30 Hz strobe unless a profile says so. Equally, it MUST NOT assume the animation is harmless. The profile decides.

## 9. Evidence and Number Labeling {#s9}

9.1 Six number labels. Every number carries one of six labels from ChatGPT: Observed, Published Estimate, Derived Calculation, Projection, Hypothetical Assumption, or Simulation Result. Please refer to Table 9.1 in the Exhibits section.

9.2 Unverified flag. A number that came from a team response and has not been checked against its primary source carries the added flag UNVERIFIED. This applies to every epidemiology and Android figure in this document.

9.3 Origin notes. Every exhibit carries a source note, as the documentation standard requires. Where a number is used in a later calculation, the calculation inherits the weakest label of its inputs.

9.4 No silent promotion. A simulated number MUST NOT become a medical statistic. A Mode C result MUST NOT be quoted without its assumption.

9.5 Verified versus validated. Verified means checked against a source. Validated means shown to work for its purpose. Do not use one for the other.

9.6 No fabricated citations. If a source cannot be checked, write "unverified." Perplexity's bracketed citation markers could not be checked here and are treated as unverified.

## 10. Populations and Settings {#s10}

10.1 Five settings. The Lab models: a general Android population; a low-contact individual; a high-contact occupation; a disability-support or day-program setting; and a household with a susceptible member.

10.2 Do not assume disability means seizure. The Lab MUST NOT treat disability as a proxy for seizure susceptibility. It MAY model a higher epilepsy rate in a setting where evidence or local data support it, or as a labeled enrichment sensitivity.

10.3 Epilepsy is enriched, photosensitivity less so. Grok reported that epilepsy is far more common among people with intellectual disability, with a pooled figure near 22 percent against about 1 percent in the general population. Photosensitive epilepsy is still a few percent of that. The Lab carries both facts. This corrects an assumption in my earlier response, which said both were "likely more common."

10.4 Personal network versus sample. Your work setting involves few daily contacts but a non-representative mix. These are two separate variables: how many people you meet, and how those people differ from the public. The Lab models both.

10.5 Lifetime contacts. Because clients change over time, the relevant number for "have I ever seen it" is the count of unique people met over a working life, not the size of one day's caseload. Please refer to Table 14.1 in the Exhibits section for an illustration.

10.6 Local data. The best input for the support-service setting is anonymized aggregate counts supplied by the coordinator, such as how many people have documented seizure plans. The Lab MUST NOT hold names, diagnoses, or other identifiable details of individual clients (Section 16).

10.7 Separate reporting. The Lab MUST report the support-service setting on its own. It MUST NOT dilute that setting's signal by pooling it with a much larger low-risk population. This follows Perplexity.

## 11. Detection and Reporting Module {#s11}

11.1 Detection is its own system. A real effect can exist and stay invisible. The Lab models the path from event to report: noticed, linked to the animation, reported, categorized correctly, and not duplicated.

11.2 Underreporting sweep. The Lab reports apparent incident rates when 100, 50, 25, 10, 5, and 1 percent of events reach the developer, following ChatGPT.

11.3 The blind dashboard. Under the fixed premise, developer-side detection is zero by design. The support taxonomy has no field for seizure, migraine, startle, or fall. Reports are closed as preference. Telemetry counts unlocks, not seizures. The absence of a signal is then cited as evidence of absence. This mechanism comes from Grok. The Lab sets developer-side detection to zero and models detection only through outside channels such as clinics, advocates, researchers, and courts.

11.4 Survivor effect. People who have an event may stop using the phone, so they vanish from the exposed count. The Lab models this undercount.

11.5 Signal versus proof. A reported cluster is a signal. It is not causal proof. The Lab states what evidence would be needed to move from one to the other, and what evidence would reasonably rule the hypothesis out.

## 12. Policy Arms {#s12}

12.1 One factual arm, several counterfactual arms. The factual arm is the developer's fixed non-response. All other arms are counterfactual, run only to measure what non-response costs. Please refer to Table 12.1 in the Exhibits section.

12.2 Opt-out is not full mitigation. An opt-out helps only if people can find it and use it. People who rely on caregivers, people who do not connect symptoms to the phone, and bystanders may never turn it off. The Lab sets effective mitigation to uptake times effectiveness, never to 1 by default.

12.3 Default matters. A safe default with an optional enhancement usually protects more people than an opt-out, because protection does not depend on action. The Lab tests this rather than assuming it.

12.4 Cost framing. Counterfactual arms report prevalence of harm, severity, avoidability, and engineering cost as separate items. A very rare effect can still deserve mitigation when the exposure is unnecessary and avoidable. That statement is a principle for reporting, not a result.

## 13. Experiment Program {#s13}

13.1 Eleven experiments. Please refer to Table 13.1 in the Exhibits section. Each experiment states its question and its required output.

13.2 Order. E0 runs first. No later experiment may report a number from an unverified input as anything stronger than a Hypothetical Assumption until E0 is done.

13.3 Required statistics. For every simulated outcome, report the mean, median, 5th to 95th percentile, probability of zero events, probability of at least one event, and probability of at least ten events where relevant. Report when an event is too rare to estimate reliably.

13.4 Sample size. E8 answers how large a study must be to expect to see one event at 50, 90, 95, and 99 percent probability, under several event rates.

13.5 Sensitivity. E9 varies photosensitivity rate, unlock frequency, animation-on fraction, bystander count, enrichment level, dependence model, and reporting rate.

## 14. Core Equations and Worked Illustrations {#s14}

14.1 Expected events. Expected events equal the sum over exposed people of their exposures times their per-exposure hazard, then multiplied by (1 minus M). Perplexity's version, users times exposures times susceptible share times probability times (1 minus M), is acceptable when hazard is uniform among susceptible people. It hides heterogeneity and the Lab prefers the person-level sum.

14.2 Probability of at least one event. For n independent exposures at per-exposure hazard h, the chance of at least one event is 1 minus (1 minus h) raised to the power n. For small h this is close to n times h. The threshold model in Section 7.3 does not follow this formula.

14.3 Encounter probability. For a network of n unique people with susceptibility rate p, the chance of at least one susceptible person is 1 minus (1 minus p) raised to the power n. This assumes independence and a fixed p, both of which the Lab tests.

14.4 Exposures to see one event. To have probability P of seeing at least one event at hazard h, about ln(1 minus P) divided by ln(1 minus h) exposures are needed. At 50 percent this is about 0.69 divided by h.

14.5 Worked illustrations. Please refer to Table 14.1 in the Exhibits section. Every row is a Derived Calculation on an unverified input or a Hypothetical Assumption. None is a medical statistic.

14.6 What the illustrations show. They show why "I have never seen it" and "it does not happen" are different statements. A working life can pass with no photosensitive contact in a general-rate setting. In an enriched setting the same life is far more likely to include one. Whether that person then has an event depends on the hazard, which the Lab does not know.

## 15. Outcome Taxonomy {#s15}

15.1 Not every event is equal. The outcome tree runs from no response, through momentary discomfort, headache or migraine, dizziness or disorientation, aura without seizure, seizure without injury, seizure needing medical evaluation, seizure with a fall or collision, emergency treatment, and hospitalization, to a rare severe secondary outcome. This list adapts ChatGPT's.

15.2 No invented percentages. The Lab MUST NOT assign probabilities to medical outcomes without evidence. Where it needs a value, it labels it a sensitivity assumption.

15.3 Non-medical consequences. The Lab also tracks loss of independence, avoidance of an essential device, caregiver burden, missed services, complaints filed and unanswered, legal actions, and months of continued non-response after each milestone. Several of these come from Claude's and Copilot's responses.

15.4 Time-to-event measures. The Lab tracks time from first warning to first documented injury, and from first injury to legal action. These are System 1 outputs.

## 16. Safety, Ethics, and Privacy {#s16}

16.1 No hazardous stimulus. The Lab produces no flashing content meant to be hazardous and exposes no person to one. Validation uses modeling, literature, anonymized reports, and consented telemetry in the fiction only. Perplexity and Copilot both stated this.

16.2 No allegation. The Lab does not state or imply that Google, Android developers, or any real organization behaved as the fictional developer does. Where a real name appears, it is in the non-claim.

16.3 Client privacy. The Lab MUST NOT store, request, or reproduce identifiable information about any individual client or participant, including names, diagnoses, or incident details tied to a person. Only anonymized aggregate counts may be used, and only if the coordinator chooses to supply them.

16.4 Not medical advice. No output is medical advice. Anyone with a concern about photosensitivity should consult a clinician.

16.5 Stigma. The Lab MUST NOT present disabled people as a risk. It presents the exposure design as the issue.

16.6 Tone. The Lab MAY describe the fictional developer's conduct bluntly as a study condition. It MUST NOT present that conduct as a finding about the real world.

## 17. Roles, Independence, and Review {#s17}

17.1 Roles. Name each that applies: coordinator, lab lead, run preparers, adversarial reviewer, and verifier. The coordinator sets premises and adopts or rejects. Preparers run experiments. The verifier checks inputs against sources.

17.2 Separation. The adversarial reviewer for a run MUST be a different system from its preparer. A system MUST NOT be the only reviewer of its own earlier response. I did not meet this when reviewing my own earlier response (Section 21.2).

17.3 Parallel independent runs. At least two systems SHOULD run the same parameter file without seeing each other's results. Differences are findings, not errors to be smoothed away.

17.4 No self-adoption. An AI MUST NOT adopt, ratify, or approve its own work or this charter.

17.5 Two readings. Every report ends with the strongest skeptical interpretation and the strongest precautionary interpretation. Neither is forced to win.

## 18. Reproducibility and Run Records {#s18}

18.1 Parameter file. Every run uses one parameter file listing each input, its value, its origin label, and its source. The file is published with the report.

18.2 Seeds and iterations. Random seeds, iteration counts, and software versions are recorded. Enough iterations are used to stabilize tail estimates, and the report says when they did not.

18.3 Executed or proposed. A run record states whether each experiment was executed, partly executed, or only proposed. An AI MUST NOT describe a run that did not occur. Grok's reported 20,000-trial Monte Carlo is treated as unverified because no code or output was supplied.

18.4 Code. Simulation code MUST be supplied with results so another system can rerun it. A result without code is a claim, not a run.

18.5 Deviations. Any change to a parameter after seeing results is recorded as a deviation with a reason.

## 19. Findings, Acceptance Gate, and Stop Rules {#s19}

19.1 Allowed findings. The Lab reports one of: no meaningful hazard (H0), a hazard too small to separate from background (H1), a small susceptible-subgroup effect (H2), or a strong signal where mitigation would materially help (H3). It reports H4 separately.

19.2 Blocking gate. A report MUST pass these items or record an exception. The fixed premises and open hypotheses are stated. The mode is declared. Every number has a label. The zero arm is present and reported. A counterfactual branch exists and is marked as never adopted. A run record states executed or proposed. Code and parameter file are supplied. No identifiable client information appears. The non-claim is present. Both skeptical and precautionary readings are present.

19.3 The gate must be able to fail. A report that omits the zero arm fails. A report that shows only Mode C results as conclusions fails. A report that treats an opt-out as fully effective without justification fails.

19.4 Stop rules. The Lab stops and reports if inputs cannot be verified, if the run cannot be reproduced, if a request would require producing a hazardous stimulus, or if a request would require identifiable client data.

## 20. Deliverables and Format {#s20}

20.1 Deliverables. Each experiment produces a report, a parameter file, code, and a run record. A final synthesis answers the questions in Section 19.

20.2 Format. Documents follow the JOINT documentation standard v0.1 while it is in use: Core Block on the first screen, single-column prose, exhibits only in the Exhibits section, and PDF, DOCX, and Markdown delivered together or an honest exception recorded.

20.3 Phone reading. Reports are written for phones. No table appears in the body. Exhibit tables have at most three columns.

20.4 Final questions. The synthesis answers: how many people live with epilepsy and how that changed; what share may be vulnerable to visually induced seizures; how often people unlock; how exposure differs for light and very heavy users; how many exposures occur at Android scale; how rare an event could be and still appear at global scale; how likely a usability study is to detect it; how likely one person is to meet it; how that changes in a non-representative setting; how bystanders change exposure; how underreporting hides a signal; what an opt-out would change; what evidence would show causation; and what evidence would rule the hypothesis out. These come from ChatGPT's closing questions.

# Part B. Review and Rationale (Informative) {#part-b}

## 21. Review Method and Limits {#s21}

21.1 What I reviewed. The brief as pasted (your original prompt, your correction, and an instruction to design a laboratory), and ten responses: five to the original prompt and five to the correction, from ChatGPT, Claude, Perplexity, Grok, and Microsoft Copilot. I also read the attached documentation standard.

21.2 A disclosure. The Claude responses are my own earlier work, from the same model family as this preparer. I applied the same criteria to them, but I cannot claim to be fully independent about them.

21.3 Criteria. Six questions. Is it faithful to the brief? Is it internally consistent? Could it actually be run? Does it keep the fixed premise separate from the tested hypothesis? Does it respect the mobile and no-table preference? Does it say honestly what was and was not done?

21.4 Limits. I saw text only. I did not run any prompt, search any source, or see how responses rendered in their own apps. I checked arithmetic where responses gave it. I did not check any epidemiology, Android, or smartphone-usage figure against its primary source.

21.5 Not fact-checking your framing. I engaged your scenario on its own terms. My checks are of the responses' internal consistency and arithmetic, not of your premise.

## 22. Review of Responses to the Original Prompt {#s22}

22.1 ChatGPT. Strengths: it reframed the task as a test, not a proof. It supplied eighteen parts, Poisson and binomial modeling, a detection problem, sample-size analysis, a personal-network versus population section, and a two-sided adversarial review. Its six number labels became the Lab's standard. It preserved your representative-versus-actual-population distinction. Gaps: the developer "initially declines," which is weaker than you intended. It is a prompt with no numbers, and eighteen parts plus seventeen questions risk overgrowth. It requests several tables, which conflicts with your mobile preference.

22.2 Claude (my earlier response). Strengths: concise, no tables, honored the mobile preference, and kept real and fictional numbers separate. Gaps: it treated the developer's response as one bullet. It asserted that seizure disorders and photosensitivity were "likely more common" in your population, which is an assumption and not an established fact. It had no dependence model, no detection module, no verification step, and no reproducibility rules.

22.3 Perplexity. Strengths: it executed an analysis instead of writing only a prompt. It gave a five-year series, three projections, unlock tiers, and a fictional scenario with one million users. Its ethics section is the strongest of the five, covering foreseeability, accessibility by design, informed choice, and rollback. It proposed a safe methodology with no human exposure and a stop rule. Gaps: it uses many tables. Its flash-sensitive range of 0.05 to 0.3 percent is higher than the others (Section 24). Two of its unlock sources are a consumer-marketing page and a forum post, and its bracketed citations could not be checked. It states mitigation is "easy" and "low cost" without support.

22.4 Grok. Strengths: the most scientifically disciplined. It separates idiopathic from secondary epilepsy, separates logged from self-reported unlocks, puts a physical specification on the stimulus, and keeps a zero arm. It supplies a caseload calculation for a support setting. Gaps: it narrows the stimulus to a single wave, which makes the seizure hazard near zero under the cited threshold. That is a legitimate input, but it shifts the scenario from your "flash-like effect." It reports a 20,000-trial Monte Carlo with no code or output. It mentions "the file" and "Files:" without delivering one. It says higher arms "would already be obvious in epilepsy clinics" without support.

22.5 Microsoft Copilot. Strengths: a thorough prompt with thirteen parts, a fifteen-item animation specification, a rule to avoid double-counting bystanders, ten policy arms, and prominent required cautions. It said plainly that it found no personal research file. Gaps: it also had the developer "initially decline." It requests many tables. Its binomial formula was garbled in the pasted text. It has no numbers beyond an evidence anchor.

## 23. Review of Responses to the Correction {#s23}

23.1 ChatGPT. The best conceptual answer. It separated a harm and evidence system from an organizational-response system, added an Institutional Resistance Parameter, refused any automatic remediation threshold, and asked what ends exposure if the developer cannot. Gap: "at or near zero" leaves room for a fix. It also said the study should not presume the animation causes seizures. That is right for Mode T. It does not give a way to honor your conditional scenario, which is why the Lab adds Mode C.

23.2 Claude (my earlier response). It accepted the correction, set the probability of fixing, disclosing, or acknowledging to zero, and added tracked variables such as complaints filed versus answered. Gaps: brief, no counterfactual branch, no detection mechanism, no external terminators, and it ended by asking permission instead of delivering.

23.3 Perplexity. It formalized M = 0, built a phase timeline, added a cumulative harm equation, and offered statement language for the project. Strengths: treating legal action as evidence rather than intervention. Gaps: the equation multiplies susceptible share and probability in a way that hides heterogeneity. The 8 percent vulnerable figure in its 500-person example has no source. It presents its stage list as a table.

23.4 Grok. It admitted its earlier pass answered a different question. It supplied a narrative of the developer's conduct through launch, complaints, injuries, and litigation, and it identified the blind dashboard. Its observation that the developer can say "zero arm" aloud after the nonzero arms have been delivered is sharp. Gap: it is a story without parameters.

23.5 Microsoft Copilot. It framed the research question as what happens when a developer refuses regardless of evidence, listed ten forms of refusal, listed fifteen consequences to measure, and kept a counterfactual branch that the developer never adopts. Gap: it provides no mechanics for the fixed state.

## 24. Cross-Cutting Findings {#s24}

Please refer to Table 24.1 in the Exhibits section for a one-line summary of each response, and to Table 24.2 for numeric discrepancies.

24.1 Strong agreement. All five systems agree on fictional labeling, on distinguishing epilepsy from photosensitive epilepsy, on separating exposure from harm, and on modeling the support setting separately. That agreement belongs in the core.

24.2 Your original prompt blends two jobs. It asks for a scenario in which a share of users have seizures, and also asks how likely that is. Only ChatGPT stated outright that the study should test rather than prove. The Lab resolves this with Modes C and T (Section 5).

24.3 The developer premise is informative only in nonzero arms. If the true hazard is zero, no evidence ever reaches the developer and the non-response premise does nothing. Grok implied this. No response said it plainly.

24.4 The response premise was softened twice. Both ChatGPT and Copilot first wrote that the developer "initially declines." Your correction was right. Perplexity and Claude had the same softness.

24.5 No response defined independence, run records, or a gate that can fail. All ten are strong on content and weak on process.

24.6 Nobody modeled lifetime contacts. All responses used a caseload or a network of fixed size. For someone whose clients change, the count of unique people met over time is the better quantity (Section 10.5).

24.7 Tables. Perplexity and Copilot asked for many tables in the output, which conflicts with your stated preference that content others read should use a single column. The Lab places tables only in exhibits.

24.8 Unverified inputs. Every response used outside figures. None offered a verification step. The Lab adds E0.

## 25. Decisions and Conflicts Resolved {#s25}

25.1 Please refer to Table 25.1 in the Exhibits section for the full list of conflicts and rules.

25.2 Developer premise. I chose exactly zero and an absorbing state. I recorded symbolic compliance as an event, not a fix.

25.3 Hazard. I kept it open, with a zero arm, and added Mode C for your conditional scenario.

25.4 Stimulus. I made it parametric with three profiles, so Grok's single-wave view and Perplexity's strobe-like view are both testable and neither is assumed.

25.5 Opt-out effectiveness. I rejected the assumption that an opt-out equals full mitigation.

25.6 Verification. I made source verification the first experiment.

## 26. Adversarial Review of This Charter {#s26}

I asked the charter the hardest questions I could. The weaknesses stay in the record.

26.1 Does fixing the developer's behavior guarantee a conclusion? Partly. The Lab's findings about developer conduct are inputs, not results. Any output about institutional failure MUST say it is an assumption. A reader could still take the narrative as a finding. Weakness preserved.

26.2 Does the zero arm get fair treatment? The gate requires it. A reader who wants a harmful result may find the zero arm unwelcome. The Lab requires it anyway.

26.3 Is it too big? Part A has twenty sections and a long gate. The risk of bureaucracy is real. I have not tested it on a real run.

26.4 Can a skeptic accept it? A skeptic may object that a lab built around a hypothetical developer is not science. The answer is that the Lab says so in the non-claim and tests the hazard separately.

26.5 Can a precautionary reader accept it? They may object that the zero arm and the single-transition framing downplay real concerns. The Lab runs the higher-hazard profile and the counterfactual branch to meet that objection.

26.6 Same-model bias. I reviewed my own earlier response and may be lenient or harsh with it. An independent reviewer is needed.

26.7 Unverified inputs. Everything numeric rests on unverified inputs until E0 is done. The worked illustrations show structure, not facts.

26.8 Does the enrichment assumption stigmatize? The Lab ties enrichment to epilepsy evidence, not to disability itself, and requires labeling. The risk remains where a reader skims.

26.9 Is the charter itself independent? The gate was run by its own preparer. An outside review is needed before adoption.

## 27. Open Questions for Decision {#s27}

1. Entity label. I used OAL. Should it be OAL, JOINT, or another label?
2. Lab name. I proposed "Forced Exposure and Institutional Non-Response Laboratory." Keep it or rename it?
3. The zero arm. Do you agree that the hazard stays open, with zero included, even though your scenario assumes seizures occur? Mode C covers the assumption.
4. Symbolic compliance. Do you agree that a vague warning or a plaintiff-only fix counts as no material action?
5. Local data. Will you supply anonymized aggregate counts for your support setting, with no names or individual details, or should the Lab use labeled enrichment levels only?
6. Filename type code. The standard has no code for a charter. Should SPEC be used, or should a new code be added?
7. Page size. I used a 6 by 9 inch page for the PDF and DOCX so text reads at size on a phone. Do you accept it, or should it be Letter?

## 28. Next Actions {#s28}

1. The coordinator answers the seven open questions.
2. Run E0: verify the epilepsy, photosensitivity, Android, and unlock-frequency figures against primary sources.
3. Build the parameter file and simulation code with fixed seeds.
4. Have at least two systems run the Lab independently and compare results.
5. Have a different system perform the adversarial review.
6. Pilot the charter on one small experiment, such as E4 or E8, and note the effort.
7. Adoption is the coordinator's decision, made after these steps.

## 29. Delivery Notes and Gate Record {#s29}

29.1 Formats. Markdown, DOCX, and PDF were all produced and opened. The DOCX and PDF were built from the Markdown source with pandoc and LibreOffice, so the content matches. The two figures sit in the assets folder beside the Markdown file.

29.2 Format Exception FX-1. Required item: page numbers in the table of contents. Failure type: unsupported feature. Reason: the table of contents is a static linked list built from headings, so it carries no page numbers. Substitute: tappable links and "Page X of Y" in the footer.

29.3 Format Exception FX-2. Required item: page size. The standard's examples use Letter. This document uses 6 by 9 inches so that text is readable on a phone. Open Question 7 asks you to decide.

29.4 Mobile check. I reviewed rendered pages at reduced size. I did not test on a physical phone.

29.5 Gate result. Pass with exceptions, judged against the documentation standard's ten blocking items. Checked mechanically: no table in the body, every exhibit numbered, sourced, and cited by number, no spatial citation words, and all three files open. The exceptions are FX-1, FX-2, the lack of a physical phone check, and the lack of an independent reviewer (Section 26.9). The PDF may lack accessibility tags, which I did not verify. Gate run by the preparer on 2026-10-04.

29.6 Revision note. v0.1, 2026-10-04. First release. No earlier versions.

# Exhibits {#exhibits}

This section holds every table and figure cited above. Each item gives its purpose, the section that cites it, and its source.

## Table 4.1. Fixed Premises and Open Hypotheses

Purpose: Separates what the Lab assumes from what it tests.

Cited in: Section 4

Source: Preparer's design from the coordinator's correction and the responses.

| Item | Statement | Type |
|:------------|:---------------------------------------|:---------|
| P1 | Developer never acknowledges or mitigates | Fixed |
| P2 | Probability of material action is exactly 0 | Fixed |
| P3 | Animation, developer, events are fictional | Fixed |
| H0 | No hazard; stimulus below thresholds | Tested |
| H1 | Hazard too small to separate from background | Tested |
| H2 | Small detectable effect in susceptible group | Tested |
| H3 | Strong signal; mitigation would help | Tested |
| H4 | Non-seizure harms (migraine, distress, avoidance) | Tested |

## Table 5.1. The Two Operating Modes

Purpose: Shows the difference between assuming a hazard and testing for one.

Cited in: Section 5

Source: Preparer's design.

| Mode | Question answered | Cannot answer |
|:--------|:--------------------------------|:-----------------------|
| C, conditional | What follows if harm occurs and the developer never responds | Whether harm is real |
| T, test | How likely, how detectable, how often would one person see it | What happens after harm is assumed |

## Figure 6.1. Diagram: Two-System Architecture

Purpose: Shows the harm and evidence system, the fixed developer state, and the external-only ways exposure can stop.

Cited in: Section 6

Source: Preparer's design from Sections 6.1 to 6.7.

Alternative text: A vertical flowchart. A hazard hypothesis feeds a harm and evidence system. Evidence reaches the developer, whose state is fixed at no material corrective action. Exposure continues and loops back into the harm and evidence system. Two dashed boxes below show external terminators and a counterfactual branch that is never adopted.

![Vertical flowchart of the two-system architecture: hazard hypothesis, harm and evidence system, evidence reaching the developer, the fixed developer state of no material corrective action, continuing exposure that loops back, and two dashed boxes for external terminators and the counterfactual branch.](assets/figure-6-1.png){width=4.4in}

## Figure 7.1. Diagram: Exposure-to-Harm Chain

Purpose: Shows the nine stages between an Android user and a reported event.

Cited in: Section 7

Source: Preparer's design, adapted from ChatGPT's Part VII chain.

Alternative text: A vertical list of nine boxes joined by arrows: Android users, people who see the animation, susceptible people, stimulus above threshold, modifiers present, physiological response, seizure or non-seizure harm, injury or secondary consequence, and noticed, attributed, and reported.

![Vertical chain of nine boxes from Android users to noticed, attributed, and reported events.](assets/figure-7-1.png){width=4.4in}

## Table 9.1. Number Origin Labels

Purpose: Defines the six labels every number must carry.

Cited in: Section 9

Source: Labels from ChatGPT's Output Requirements; examples by the preparer.

| Label | Meaning | Example |
|:----------------|:--------------------------|:---------------------|
| Observed | Directly measured | A logged phone count |
| Published Estimate | Reported by a named study | A global prevalence figure |
| Derived Calculation | Arithmetic on other numbers | 60 x 365 = 21,900 |
| Projection | Forward estimate | A five-year count |
| Hypothetical Assumption | Chosen for the study | A per-unlock hazard |
| Simulation Result | Output of a run | A modeled event count |

## Table 12.1. Policy Arms

Purpose: Lists the factual arm and the counterfactual arms.

Cited in: Section 12

Source: Preparer's selection from ChatGPT's five policies and Copilot's ten.

| Arm | Description | Branch |
|:-------|:----------------------------|:---------------|
| 1 | No change; animation mandatory | Factual |
| 2 | Warning only | Counterfactual |
| 3 | Reduced intensity or frequency | Counterfactual |
| 4 | Reduced-motion integration | Counterfactual |
| 5 | User opt-out | Counterfactual |
| 6 | Safe default, optional enhancement | Counterfactual |
| 7 | Immediate remote disablement | Counterfactual |
| 8 | Pre-release accessibility testing | Counterfactual |

## Table 13.1. Experiment Program

Purpose: Lists each experiment, the question it asks, and what it must produce.

Cited in: Section 13

Source: Preparer's design from ChatGPT, Copilot, Grok, and Perplexity.

| Code | Question | Output |
|:--------|:----------------------------|:-------------------------|
| E0 | Are the inputs real? | Verified input list |
| E1 | How many people have epilepsy, past and projected? | Five-year series, three projections |
| E2 | How many exposures occur? | Unlock tiers, animation-on fraction, bystanders |
| E3 | What happens across hazard rates, including zero? | Sweep, two dependence models |
| E4 | Who meets an affected person? | General versus enriched networks, lifetime contacts |
| E5 | How hidden is a real effect? | Underreporting and blind-dashboard results |
| E6 | What does five-year non-response produce? | Persistent-exposure run with external terminators |
| E7 | What would action have prevented? | Counterfactual comparison |
| E8 | How big must a study be? | Exposures needed at 50, 90, 95, 99 percent |
| E9 | What if assumptions change? | Sensitivity, skeptical and precautionary readings |
| E10 | What non-seizure harms occur? | Migraine, distress, avoidance, household effects |

## Table 14.1. Worked Illustrative Calculations

Purpose: Shows how the equations behave on the team's reported inputs. These are not findings.

Cited in: Section 14

Source: Preparer's arithmetic on inputs reported by Grok and Perplexity. Inputs UNVERIFIED. Hazard rates are Hypothetical Assumptions.

| Item | Result | Label |
|:------------------------|:---------------|:-------------|
| Unlocks per year at 60 per day | 21,900 | Derived |
| Android-scale unlocks per year, 3.9 billion users, 60 per day, animation on every unlock | about 85 trillion (upper bound) | Derived, unverified input |
| Photosensitive epilepsy users at 1 in 4,000 of 3.9 billion | 975,000 | Derived, unverified input |
| Expected yearly events, hazard 1 in 1 million per unlock, those users only | about 21,350 | Derived, assumed hazard |
| Yearly chance per such person, hazard 1 in 10 million | about 0.2% | Derived, assumed hazard |
| Yearly chance per such person, hazard 1 in 1 million | about 2.2% | Derived, assumed hazard |
| Yearly chance per such person, hazard 1 in 100,000 | about 19.7% | Derived, assumed hazard |
| Chance a 12-person caseload holds one photosensitive person, general rate (1 in 4,000) | about 0.3% | Derived |
| Same, enriched rate 0.66% (22% epilepsy times 3% photosensitive) | about 7.6% | Derived, assumed enrichment |
| Chance 200 unique contacts include one, general rate | about 4.9% | Derived |
| Same, enriched rate 0.66% | about 73% | Derived, assumed enrichment |
| Exposures to expect one event at 1 in 1 million: 50%, 90%, 95%, 99% | 0.69M, 2.30M, 3.00M, 4.61M | Derived, assumed hazard |
| Same, in photosensitive person-years at 60 unlocks per day | about 32, 105, 137, 210 | Derived, assumed hazard |

## Table 24.1. Summary of the Ten Responses

Purpose: Gives each response's strongest contribution and main gap.

Cited in: Section 24

Source: Preparer's review (Sections 22 and 23).

| Response | Strongest contribution | Main gap |
|:--------------------|:---------------------------|:----------------------|
| ChatGPT, original | Test not proof; six number labels | Prompt only; developer "initially declines" |
| Claude, original | Short, no tables | Thin; assumed enrichment as fact |
| Perplexity, original | Ethics and safe method | Tables; high flash-sensitive range; weak sources |
| Grok, original | Stimulus physics; zero arm | Unsupplied Monte Carlo; stimulus narrowed |
| Copilot, original | Cautions; double-count rule | Tables; no numbers; developer "initially declines" |
| ChatGPT, correction | Two systems; resistance parameter | "At or near zero" |
| Claude, correction | Accepted fix; tracked variables | Brief; asked permission |
| Perplexity, correction | M = 0 formalism; timeline | Unsourced 8%; stage table |
| Grok, correction | Blind dashboard | Narrative, no parameters |
| Copilot, correction | Ten refusal forms; counterfactual | No mechanics |

## Table 24.2. Numeric Discrepancies Found

Purpose: Lists places where the responses disagree or an internal check found a gap.

Cited in: Section 24

Source: Preparer's arithmetic and comparison. All figures UNVERIFIED against primary sources.

| Item | What I found | Effect |
|:-------------------|:----------------------------|:---------------------|
| Flash-sensitive share | Perplexity: 0.05 to 0.3% of users. Grok: 1 in 4,000 (0.025%). Copilot's 3% of the 0.7% epilepsy rate gives about 0.021%. | Perplexity is about 2 to 12 times higher; unreconciled |
| 2026 epilepsy count | Perplexity 53.7 million; compounding 0.7% a year from 51.7 million gives about 53.5 million; Grok gives 53 to 55 million | Small drift; needs E1 |
| Five-year projections | Perplexity's 54.5, 55.6, 57.0 million match its stated rates | Arithmetic consistent |
| Fictional exposures | Perplexity's 72 million a day and 26.28 billion a year match its inputs | Arithmetic consistent |
| Grok's per-person chances | 0.2%, 2%, 20% match my calculation | Arithmetic consistent |
| Caseload epilepsy | 22% of 12 is 2.64; Grok states about 2.7 | Rounding |
| Unlock bands | Both use about 60 as typical; both mix logged and self-report sources | Needs E0 and pickup versus unlock rule |

## Table 25.1. Conflicts and Rules Adopted

Purpose: Lists each conflict found and the rule chosen.

Cited in: Section 25

Source: Preparer's review and design decisions.

| Conflict | Rule adopted | Section |
|:------------------------|:--------------------------|:-------|
| "Initially declines" versus never responds | Exactly zero, absorbing state | 4.3, 6.3 |
| Presume harm versus test for it | Modes C and T; zero arm kept | 5 |
| Single wave versus strobe-like | Three parametric profiles | 8 |
| Opt-out as full fix | Uptake times effectiveness | 12.2 |
| Tables in output versus phone reading | Exhibits only | 20.3 |
| Prompt only versus executed results | Run record states which | 18.3 |
| Unverified outside figures | E0 first; UNVERIFIED flag | 9.2, 13.2 |
| Disability as seizure proxy | Not allowed; evidence or labeled enrichment | 10.2 |
| Caseload versus lifetime contacts | Model both | 10.5 |
