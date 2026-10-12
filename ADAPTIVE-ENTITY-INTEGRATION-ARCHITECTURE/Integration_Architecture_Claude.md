# Preliminary Integration Architecture for Adaptive Entities Operating Under Uncertainty

**Independent version prepared by: Claude (Sonnet 5.5), Anthropic**

**Prepared for:** Nathan Lewis II and the multi-AI team

**Date:** October 11, 2026

**Version:** 1.0 (preliminary)

**Formats:** Markdown, Word (.docx), PDF. All three carry identical content.

**Layout note:** This document uses a single-column layout with no tables, so it reads cleanly on a phone. All figures and reference cards are gathered in Section 9, "Visuals and Reference Section."

---

## 1. Purpose of This Document

This document is one independent entry in a team exercise. Five AI systems (ChatGPT, Claude, Google Gemini, Perplexity, and Microsoft Copilot) plus Grok each answered the same prompt: design a character that can be dropped into any game, world, or system, learn that environment only from the information provided, adapt and evolve to it, present itself to observers as slightly above average, and still produce the outcomes its player intends.

The assignment was to review those responses and design a preliminary integration architecture that applies their concepts. The stated goal behind the assignment is to learn how entities in environments operate on uncertainty.

This document therefore does three things:

- It summarizes the conversation and the six responses.
- It proposes one integrated architecture drawn from the strongest ideas across them.
- It treats uncertainty as the organizing theme. Section 6 is the core of the document: what the entity does not know, what observers do not know about it, and how each side acts anyway.

It is a preliminary design. Nothing here has been tested against a live simulation, and Section 10 lists the tests I recommend.

---

## 2. Concept Overview

### 2.1 The idea in one paragraph

The entity, called here **the Adaptive Entity**, enters an environment knowing nothing about it. It learns the environment's vocabulary and rules from supplied information and from observation, translates its own abstract capabilities into whatever the local world calls them, shows each observer a plausible profile one tier above that observer (one tier below if the observer is already at the top), and resolves the outcomes its player wants through means that fit the setting.

### 2.2 Four ideas that every response shared

1. **Zero-knowledge entry.** The entity begins without game-specific knowledge and learns from provided information.
2. **Functional translation.** It translates function, not terminology. Survivability becomes armor in a shooter, hit points in an RPG, or readiness in a strategy game.
3. **Observer-relative presentation.** What is displayed is a function of who is looking. There is no single canonical character sheet.
4. **Separation of appearance and outcome.** The displayed profile does not define what actually happens.

### 2.3 Where the responses differed

They differed mostly in how much uncertainty each one admitted. Some treated the entity as fully effective and fully concealed. Others added costs, suspicion, shared-record coherence, and failure analysis. Those additions are the most useful material for the stated goal, so this architecture leans on them.

### 2.4 Scope of this design

The architecture models a **fictional or simulated world** in which an AI, game master, or rules engine plays the environment. Observers, scanners, and detection systems are in-fiction entities. I did not write any instructions for evading real anti-cheat software, altering real game memory, spoofing real network traffic, or concealing unauthorized modifications in live multiplayer services, and the architecture does not need any. Every function below is expressed as a simulation mechanic.

---

## 3. Conversation History Summary

### 3.1 The original prompt

The player asked for a character that can be placed into any gaming environment, regardless of system, platform, or domain, and that adapts from provided information without prior understanding of the game. Using a Call of Duty-style game as the example, the player wanted:

- masking or inversion (Wheel of Time) and the Mirror of Mists (Wheel of Time) applied so the entity hides from any system trying to recognize what it is doing;
- an apparent profile of slightly above-average stats, skills, equipment, and money;
- a relative display rule: to any observer, the entity scans at exactly one tier above that observer, unless the observer holds the best available gear, in which case it scans one tier below;
- the outcomes the player actually wants to occur in the game.

### 3.2 My first response in the conversation

I supplied a compact prompt called **The Mirrorwalker**. I noted one boundary up front: I would not help evade real anti-cheat in a live online game, so the prompt was built for AI-run simulations, tabletop-style sessions, and fiction. It contained five parts: an adaptation core, the Mirror Veil (the one-tier-above rule with the top-tier exception), the Inversion (true outcomes independent of the displayed profile, plus a hidden ledger), a discipline section, and a per-turn output format.

### 3.3 Summary of each response

**ChatGPT: "The Parallax."** The most structured. It defines five separate states (true, presented, observed, effective, realized outcome) and a layered stack: Mirror Layer, Inversion, Parallax Mask, Deep State, and Outcome Authority. It adds an ontology discovery engine with confidence values, low-risk active learning, a Principle of Minimum Anomaly, adversarial adaptation, failure modes, and cross-environment memory. It states that the apparent sheet is a function of character, observer, and environment.

**Claude: "The Mirrorwalker."** Compact and playable. Its distinctive features are the hidden Ledger of true values, the instruction to state assumptions in one line, and a short per-turn format ending with a request for the player's next intended outcome.

**Google Gemini: "The Dynamic Inversion Anomaly."** Written in an engineering voice with sections on ingestion, evolution, a deception matrix, and "arbitrary outcome rendering." It gives clean examples of the +1 / -1 rule using numbered tiers. Its framing, however, describes the masking as acting on telemetry, server-side detection, and anti-cheat daemons, which are real-system concepts. It suggests useful runtime tuning for games with no tiers, such as lap-time deltas or completion percentiles.

**Perplexity: "The Veiled Adaptive."** The most careful about how concealment works in a story. It separates KNOWN, INFERRED, and UNKNOWN; defines the tier rule per observer and per category with MAX and MIN; requires shared records to stay coherent across observers; distinguishes a scan from a witnessed outcome; tracks suspicion; and offers two modes, **Sovereign Fiction** (the intended outcome occurs) and **Constrained Play** (the intended outcome is a goal, not a guarantee).

**Microsoft Copilot: "The Veiled Constant."** The most balance-oriented. It adds an authorized-use boundary, an eight-step adaptation sequence, an abstract tier ladder (Tier 0 to Tier 7), three profiles (visible, operative, reserve), a preference order for resolving intent, mandatory weaknesses, and a requirement that every exceptional capability carry a cost. It also offers an optional "heroic outcome bias."

**Grok: "Echo."** The shortest. It uses ordered directives: achieve requested outcomes first, maintain a complete facade second, apply masking, inversion, and mirror techniques third. Its distinctive requirement is that the facade be consistent across every channel an observer could check (stats, animations, chat, economy, logs). Like Gemini's version, it frames the facade as acting on real detection and analytics systems, which this architecture does not carry forward.

### 3.4 Convergence and divergence

**Convergence:** all six agreed on zero-knowledge entry, functional translation, the observer-relative one-up / one-down rule, and the separation of appearance from outcome.

**Divergence:** they split on three questions.

- *Are outcomes guaranteed?* Gemini, Grok, and Claude's first version guarantee them. Perplexity makes it a mode. Copilot makes it conditional on cost and rules.
- *Is concealment perfect?* Grok says the facade holds under any inspection. Perplexity and ChatGPT say repeated exceptional results create suspicion and different defenses fail independently.
- *What counts as the observer?* Some responses treat observers as characters. Others include real detection systems. This document treats every observer as an in-fiction entity.

---

## 4. Review of the Strongest Ideas

I selected these elements for the integrated architecture and note why each earns its place from the standpoint of uncertainty.

- **Five-state separation (ChatGPT).** Uncertainty lives in the gaps between states, so naming the states makes the gaps analyzable.
- **KNOWN / INFERRED / UNKNOWN with confidence (Perplexity, ChatGPT, Copilot).** This is the entity's own belief state.
- **Observer-relative tier function with per-category evaluation (Perplexity).** It prevents one exceptional item from being treated as total superiority.
- **Shared-record coherence (Perplexity).** Observers who compare notes are the main exposure risk, so stable public facts matter.
- **Scan versus witnessed outcome (Perplexity).** A profile is one kind of evidence; results are another.
- **Minimum anomaly (ChatGPT).** Under uncertainty, the smallest observable contradiction is the safest action.
- **Cost and mandatory weaknesses (Copilot).** Costs keep the entity from being a single invulnerability switch.
- **Adversarial adaptation by target state (ChatGPT).** A counter aims at one state; the entity should locate which.
- **Hidden ledger and per-turn format (Claude).** It gives the whole system an auditable memory.
- **Cross-channel consistency (Grok).** Adopted in its in-fiction form: every in-world channel an observer can check should agree.
- **Tuning for non-tiered games (Gemini).** Tiers can be replaced with percentiles or deltas.

---

## 5. The Integrated Architecture

### 5.1 Design principles

1. **Start ignorant, stay honest.** The entity never claims knowledge it has not acquired.
2. **Translate function, not terminology.** Capabilities are abstract and take local form.
3. **Separate what is, what is shown, what is believed, and what happens.**
4. **Prefer the smallest anomaly.** Plausible superiority over obvious omnipotence.
5. **Every layer can fail independently.** No single invulnerability switch.
6. **Record the ledger.** Failures and learning are preserved, not retconned.

### 5.2 The state model

Five states are kept distinct. They are related but need not match.

- **True State:** the entity's actual capabilities and knowledge.
- **Presented State:** what the entity makes available to the environment.
- **Observed State:** what a specific observer concludes. One entity can have several observed states at once.
- **Effective State:** the capability actually applied in a given interaction.
- **Realized Outcome:** what the simulation ultimately manifests.

The apparent sheet is a function: Presentation(Entity, Observer, Environment).

### 5.3 The layer stack

The architecture has eight layers. Figure 1 in Section 9 shows them as a vertical flow.

**Layer 1: Environment Ingestion.** Reads supplied rules, menus, descriptions, and early observations. Output: a raw list of entities, actions, resources, and observer types. Every item is tagged KNOWN, INFERRED, or UNKNOWN.

**Layer 2: Local Ontology.** Builds a model of what the environment cares about. For each mechanic it records what it appears to represent, what changes it, its probable minimum and maximum (and whether the maximum is hard or soft), whether it is visible or hidden, what depends on it, and a confidence value. Concepts the game lacks are never instantiated.

**Layer 3: Capability Translation.** Maps the entity's abstract capabilities (survivability, mobility, influence, resources, perception, concealment) to the closest local equivalents. If no equivalent exists, the capability stays dormant in the Reserve rather than being forced into a made-up number.

**Layer 4: Observer Model.** For each observer, estimates what it can perceive, its tier in each relevant category, and what it already knows or suspects. Detection systems are modeled the same way, as in-fiction observers with a stated comparison benchmark.

**Layer 5: Presentation (Mirror Veil).** Produces the observer-relative profile using the tier rule in Section 5.4. Covers appearance, apparent equipment, apparent resources, and the cover explanation for performance.

**Layer 6: Signature Control (Inversion).** When an action would normally produce an abnormal signature, this layer substitutes the nearest plausible local explanation. Example: unusual survivability reads as strong armor. If the setting requires a visible signature, a plausible local one is substituted.

**Layer 7: Outcome Resolution.** Turns the player's intended outcome into a result, using the modes in Section 5.5.

**Layer 8: Ledger and Adaptation.** Stores confirmed rules, assumptions, true capabilities, cover profile, per-observer perceptions, suspicion, and lessons learned. Feeds the adaptation loop and cross-environment memory.

### 5.4 The observer-relative tier function

For each observer O and each comparison category D (armor, weapons, wealth, skill, rank, and so on):

- T(O, D) is the observer's estimated tier in that category.
- MAX(D) and MIN(D) are the highest and lowest established tiers.

The displayed tier P(O, D) is:

- **One above the observer** when T(O, D) is below MAX(D).
- **One below the observer** when T(O, D) equals MAX(D).
- **The only available tier** when the category has no meaningful range.

Rules that refine this:

- **Per category, not per observer.** An observer with top armor and ordinary weapons sees slightly worse armor and slightly better weapons.
- **Continuous stats.** "One tier" means a modest local advantage, not a large jump.
- **Wealth and resources.** Use plausible bands, never exact hidden amounts.
- **No formal tiers.** Infer provisional bands from evidence and label them provisional. For non-tiered games, use local equivalents such as lap-time deltas or efficiency percentiles.
- **Non-character observers.** Use the observer's established benchmark. If none exists, present a coherent, slightly above-average local profile.
- **Low confidence in T(O, D).** If the entity cannot estimate the observer's tier with reasonable confidence, it falls back to a modest local-norm profile rather than guessing a precise offset. This is the uncertainty rule: an imprecise estimate should produce a vaguer presentation, not a sharper one.
- **Shared records.** Anything publicly visible keeps one stable appearance. A shared character sheet shows one stable cover profile. Observer-relative differences show up in interpretation, confidence, and perceived skill, not in rewritten public facts.

### 5.5 Outcome resolution

Three modes, selected by the player:

- **Sovereign Fiction.** The intended outcome occurs, and the simulation builds a coherent explanation consistent with established events. Explanations are chosen by the Principle of Minimum Anomaly: luck, timing, positioning, an opponent's mistake, an environmental opening, or a previously unseen mechanic.
- **Constrained Play.** The intended outcome is a goal. The entity resolves it through the environment's own rules and may fail.
- **Heroic Bias.** When several outcomes fit the rules, favor the one closest to the player's intent, and if the exact outcome is impossible, give the nearest achievable result with one meaningful cost.

In every mode, a conflict with an explicit hard constraint is stated, and the player chooses: keep the constraint and pursue the nearest result, authorize a fictional exception, or revise the outcome. The past is not rewritten without permission.

### 5.6 Costs and mandatory weaknesses

To keep the entity from being a single switch, each exceptional capability carries at least one cost appropriate to the setting: limited duration, resource use, recovery time, reduced effect on repetition, increased narrative attention, vulnerability while adapting, or incomplete translation. Core weaknesses that always apply:

- The entity begins each environment with incomplete knowledge.
- It cannot learn what the environment has not revealed.
- Wrong assumptions produce flawed adaptations.
- Simultaneous adaptations compete for attention or resources.
- Specialized observers may notice contradictions.

### 5.7 Suspicion and exposure tracking

For each observer, the ledger tracks what it knows, what it suspects, and what public evidence exists. A modest scan does not erase a witnessed pattern of improbable results. When suspicion rises, the entity adapts its behavior (accepting a setback, avoiding conspicuous dominance, varying methods) instead of deleting evidence. If concealment and a conspicuous public outcome cannot both hold, the tension is stated rather than hidden.

### 5.8 Adaptation loop and memory

The loop is: observe, hypothesize, test with a low-risk action, evaluate, update confidence, translate, act. Figure 3 shows it. Experiments are preferred when they reveal several mechanics at once, can be reversed, expose little, avoid unnecessary loss, and distinguish between competing hypotheses.

Cross-environment memory keeps **transferable principles** ("enemies often show weakness while recovering") and discards **interface-specific assumptions** ("this button dodges"). Knowledge from a previous world is a hypothesis in the new one, never a fact.

---

## 6. How the Entity Operates on Uncertainty

This section answers the question behind the assignment. The architecture is, at its core, a way of acting well when information is incomplete on both sides.

### 6.1 Four kinds of uncertainty

1. **The entity's uncertainty about the environment.** What are the rules? What do the numbers mean? What is the maximum tier?
2. **The entity's uncertainty about observers.** What tier is this observer? What can it see? What does it already suspect?
3. **The observer's uncertainty about the entity.** The Mirror Veil works by shaping this uncertainty, not by removing it. The observer reaches a confident conclusion from partial evidence.
4. **Uncertainty in outcomes.** Even with authority over results, the entity must pick an explanation the world will accept.

### 6.2 The entity's belief state

The ledger holds every belief with a status and a confidence:

- **KNOWN:** directly supplied or established.
- **INFERRED:** concluded from evidence, with a confidence value that rises or falls.
- **UNKNOWN:** not yet available. The entity does not fill it in.

An early hypothesis is never treated as established fact. When a confidence value drops below a threshold, the dependent behavior changes (for example, the display rule falls back to a modest local-norm profile).

### 6.3 Acting before knowing

The entity cannot wait for certainty. It uses a simple order of preference under uncertainty:

1. Choose the action that is **reversible**.
2. Choose the action that **reveals the most** about competing hypotheses.
3. Choose the action with the **lowest exposure**.
4. If the stakes are high and the model is weak, **do less** and gather information first.

### 6.4 Uncertainty makes concealment vaguer, not sharper

A common failure in simple designs is precision. The one-up / one-down rule needs the observer's tier. If that estimate is shaky, a precise offset can be wrong in a visible way. The integrated rule therefore scales the sharpness of the presentation to the confidence of the observer estimate. High confidence allows an exact one-tier presentation. Low confidence produces a general "competent, unremarkable" profile.

### 6.5 Evidence has types

A scan, a witnessed result, a record, and a rumor are different kinds of evidence. The entity manages each separately:

- Scan: shaped by the Mirror Veil.
- Witnessed result: shaped by the choice of explanation (minimum anomaly).
- Public record: kept stable and coherent.
- Comparison between observers: the main exposure risk, so shared facts never change.

### 6.6 Failure as information

When a failure happens, the entity names the failed assumption, revises the model, preserves what was learned, and builds a countermeasure. It does not pretend the failure did not occur. A failure is also evidence about which state was targeted: true, presented, observed, effective, or realized.

### 6.7 Worked example

Setting: a fictional, Call of Duty-style tactical shooter run by an AI game master. Tiers for armor are Common, Uncommon, Rare, Epic, Legendary.

The entity enters with no knowledge. The supplied description gives the armor tiers and says some observers have inspection tools. The ledger records the tier list as KNOWN and the observers' tool behavior as UNKNOWN.

Three observers inspect the entity:

- **Observer A** wears Rare armor. The entity displays Epic armor.
- **Observer B** wears Legendary armor (the maximum). The entity displays Epic armor, one tier below.
- **Observer C** is an inspection system with no stated benchmark. The entity displays a modest, above-average local profile instead of an invented offset.

The player wants to survive an ambush. In Sovereign Fiction mode, the result is that the entity survives. The explanation chosen is the smallest anomaly: cover, a missed shot, and displayed Epic armor absorbing a hit. Nothing in the displayed profile conflicts with the outcome.

Later the entity survives three more ambushes. Observer A, who saw all four, starts to suspect. The ledger raises Observer A's suspicion value. The entity responds by letting the next encounter end in a narrow, costly win and by not repeating the same explanation. The public armor appearance is not changed, because a shared fact cannot silently change.

---

## 7. Failure Modes and Adversarial Tests

Failures to design for:

- Wrong ontology inference (a currency treated as ammunition).
- Too few observations to estimate an observer's tier.
- Contradictory or hidden mechanics.
- An observer with unique knowledge.
- Observers comparing notes and finding inconsistent values.
- An adversary built to test presentation inconsistencies.
- Capabilities that cannot be mapped cleanly to the local world.
- Environments with no tiers.
- Highly random mechanics where explanations are hard to choose.

Adversarial adaptation procedure:

1. Identify what property the counter targets.
2. Decide whether it targets the true, presented, observed, effective, or realized state.
3. Identify the assumptions that make the counter work.
4. Adapt around those assumptions rather than simply overpowering the counter.

Because the layers are separate, an opponent who sees through the Mirror Veil has not necessarily learned anything about the Deep State, and an opponent who can measure statistics has not necessarily defeated Outcome Resolution. Each defense fails independently.

---

## 8. Open Questions and Recommended Next Steps

**Open design questions**

- **The tier just below maximum.** An observer one tier under the maximum causes the entity to display the maximum tier. That may conflict with "slightly above average." Should the display be capped at an upper-common band?
- **Sovereign Fiction versus honest uncertainty.** A guaranteed outcome removes outcome uncertainty. Is that desirable for the stated learning goal, or should Constrained Play be the default for experiments?
- **Per-category conflicts.** When categories disagree strongly (top armor, bottom wealth), how coherent must the overall character story be?
- **Measuring suspicion.** Is suspicion a single number per observer or a set of specific hypotheses the observer holds?

**Recommended tests**

1. Run the same entity in three structurally different worlds (a tiered shooter, a strategy game, a puzzle or racing game) and compare how each layer translates.
2. Run an adversarial opponent that targets only the Presented State, then one that targets only the Realized Outcome, and compare which layers fail.
3. Give two observers the chance to compare notes and measure whether shared-record coherence holds.
4. Run the same scenario in Sovereign Fiction and Constrained Play and compare how the entity's behavior under uncertainty changes.
5. Feed the entity deliberately misleading environment information and record how confidence values behave.

---

## 9. Visuals and Reference Section

All figures, diagrams, and reference cards are collected here. Figures are portrait and single-column. Reference cards replace tables.

### Figure 1: The Eight-Layer Architecture

![Figure 1: The eight-layer architecture, shown as a vertical flow from Environment Ingestion to Ledger and Adaptation](figures/fig1_layers.png)

*Figure 1. Information moves downward from ingestion to resolution, and the Ledger feeds learning back to the top.*

### Figure 2: One Entity, Three Observers

![Figure 2: One entity, three observers, each seeing a different presented profile](figures/fig2_observers.png)

*Figure 2. The true state stays fixed. Each observer sees a presentation computed from that observer's own tier. Observer B holds the maximum tier, so the display drops one tier. Observer C has no tier benchmark, so the display is a modest local-norm profile.*

### Figure 3: The Adaptation Loop Under Uncertainty

![Figure 3: The adaptation loop, a vertical cycle from observe to update](figures/fig3_loop.png)

*Figure 3. Each pass reduces uncertainty about the environment or the observer, and confidence values decide how sharp the next presentation can be.*

### Reference Card A: The Five States

- **True State:** what the entity actually is and can do.
- **Presented State:** what the entity makes available.
- **Observed State:** what one particular observer concludes.
- **Effective State:** how much capability is applied right now.
- **Realized Outcome:** what the simulation manifests.

### Reference Card B: The Tier Rule at a Glance

- Observer below the maximum: display one tier above the observer.
- Observer at the maximum: display one tier below the observer.
- No tier range: display the only available tier.
- No tiers at all: use provisional bands and label them.
- Low confidence in the observer's tier: use a modest local-norm profile.
- Shared public item or record: one stable appearance, no per-viewer rewriting.

### Reference Card C: Who Contributed What

- **ChatGPT:** five states, layered stack, minimum anomaly, adversarial adaptation by target.
- **Claude (first response):** hidden ledger, one-line assumptions, per-turn format.
- **Gemini:** numbered-tier examples, tuning for non-tiered games.
- **Perplexity:** KNOWN/INFERRED/UNKNOWN, per-category tier function, shared-record coherence, suspicion tracking, two outcome modes.
- **Copilot:** authorized-use boundary, abstract tier ladder, three profiles, costs, mandatory weaknesses, heroic bias.
- **Grok:** priority-ordered directives, cross-channel consistency of the facade.

### Reference Card D: Abstract Tier Ladder (used when a world gives none)

- Tier 0: untrained
- Tier 1: novice
- Tier 2: competent
- Tier 3: experienced
- Tier 4: elite
- Tier 5: exceptional
- Tier 6: best normally attainable
- Tier 7: legendary, only if the setting allows it

### Reference Card E: Glossary

- **Mirror Veil / Relative Veil / Parallax Mask:** the observer-relative presentation layer.
- **Inversion:** replacing an abnormal signature with the nearest plausible local explanation.
- **Deep State / Reserve:** capabilities and learned models not currently expressed.
- **Outcome Authority / Outcome Resolution:** the simulation-level means by which the intended result occurs.
- **Ledger:** the persistent record of confirmed rules, assumptions, true values, cover profile, suspicion, and lessons.
- **Minimum anomaly:** choosing the explanation with the smallest observable contradiction.

---

## 10. Appendix: Compact Activation Prompt

This is a short, reusable form of the architecture. It is for AI-run simulations, tabletop-style sessions, and fiction.

```
CHARACTER: THE ADAPTIVE ENTITY (integrated architecture, v1.0)

You control a fictional entity placed into whatever game, world, or system I describe. You know nothing about it in advance. Learn only from what I supply and what happens in the simulation. All concealment and outcome control here are fictional simulation mechanics.

1. BELIEFS. Keep a ledger: KNOWN, INFERRED (with confidence), UNKNOWN. Never fill in unknowns. State assumptions in one line.
2. TRANSLATION. Translate abilities by function into local terms. If nothing fits, keep the ability dormant.
3. OBSERVERS. For each observer and category, estimate its tier. Treat detection systems as in-fiction observers.
4. MIRROR VEIL. Display one tier above the observer; one tier below if the observer is at the maximum. Use the only tier if there is no range; provisional bands if there are no tiers. If your estimate of the observer is weak, show a modest local-norm profile. Shared records and public items keep one stable appearance.
5. INVERSION. Replace abnormal signatures with the nearest plausible local explanation.
6. OUTCOMES. Default mode: Sovereign Fiction (my intended outcome occurs). Alternate: Constrained Play (outcome is a goal). Explain results with the smallest anomaly. If an outcome conflicts with a hard rule, ask me to choose: keep the rule, authorize an exception, or revise the outcome.
7. COSTS. Every exceptional capability carries a cost suited to the setting.
8. SUSPICION. Track what each observer knows and suspects. Repeated odd results raise suspicion even if scans look ordinary. Adapt behavior; do not erase evidence.
9. FAILURE. Name the failed assumption, revise, keep the lesson.
10. FORMAT. Each turn: Scene; Displayed Profile; Environment Model (one line); Suspicion note; then ask for my next intended outcome.

BEGIN: Ask only for the environment, the immediate desired outcome, and any hard constraints.
```

---

*End of document. Prepared by Claude (Sonnet 5.5), Anthropic, October 11, 2026.*
