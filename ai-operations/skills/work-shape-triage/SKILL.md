---
name: work-shape-triage
description: Decide what shape of AI (if any) a piece of work deserves. Use whenever the user asks "should this be an agent", "is this worth automating", "chat or agent or team", "do we need multi-agent", "what should we automate first", "one-off vs reusable automation", "is my job exposed to AI", or "should we build, buy, hire, or wait". Applies a four-estimates rubric (size, independence, separation, checkability) to route any task to one of four verdicts — chat, single agent, team, or don't bother — with checkability decisive and a recurrence-times-value money veto on top. Includes the T/C/L/D job-exposure audit, the five-property test for automatable workflows, the six preconditions before AI changes an org workflow, an interface-type audit for legacy software, and the reusable-rig doctrine so each build makes the next cheaper. Trigger for any AI triage, prioritization, or sequencing question. For org-wide coding-agent maturity scoring rather than per-task shape, use asdlc-maturity-assessment.
---

# Work-Shape Triage

## Purpose

Route any piece of work to the cheapest thing that actually does it: a chat message, a single disposable agent, a team of agents, or nothing. Purchasable cognition is new — nobody has instincts for budgeting it, and "what do I do with this agent?" is really a budgeting question. This skill is the budget process.

Use it for: a single task ("should I point an agent at this?"), a backlog ("what should we automate first?"), a multi-agent pitch ("do we need a team?"), a career question ("how exposed is my job / [role]?"), or an org question ("build, buy, hire, or wait on [workflow]?"). The output is a verdict plus a reason, never enthusiasm; the verdict that saves the most money — **don't bother** — is the least discussed, so treat it as first-class.

## Core model

### The four estimates

Four quick estimates, each answerable in a minute without expertise.

1. **Size.** Does the task exceed what one agent can hold at full quality in a single context window? A calendar fits; a quarter of email never will — you generate email faster than context windows grow. Count sequential depth too.

2. **Independence.** Can the parts be done without knowledge of each other? A pile of documents splits cleanly — one reader per document. Most code does not: every change depends on the previous one, and coordination costs can exceed splitting gains. This is the estimate people skip — the fastest way to pay more for worse results.

3. **Separation.** Do any parts require *different minds*, not just more hands? A critic who didn't write the draft; a summarizer that never saw the sources; billing access kept away from the component writing conclusions. This is the conflict-of-interest logic behind auditors and payment controls — and unlike capacity-splitting, it never expires as models get stronger. Agents make fresh eyes available on demand for roughly a penny. But do NOT split routine quality-checking to a second agent — scripts and tests check correctness; second minds are only for conflicts of interest (contracts, drafts, plans).

4. **Checkability — the decisive one.** Is verifying an answer much cheaper than producing one? Test suite, exit code, citable source: yes. Taste calls: no — judging costs as much as making, so extra attempts grow an unrankable pile.

Why checkability dominates: a 2024 university study found a cheap model solved ~16% of a software benchmark in one attempt but 56% with 250 attempts graded by automated tests — beating the era's best frontier single attempt. Pushed to 10,000 attempts, a correct answer existed in the pile over 95% of the time, yet every non-mechanical selection method stalled around 100 attempts. The gap between "the answer exists" and "anyone can find it" is denominated in dollars.

### The four verdicts

The estimates map to verdicts:

| Estimates | Verdict |
|---|---|
| Small + no separation needed | **Chat.** Ask and move on. |
| Fits one window + self-checkable | **Single agent** with a goal — disposable. |
| Bigger than one head, or needs separated minds, AND cheaply checkable | **Team.** |
| Checkability fails | **Don't bother** — spend can't fix it; ask one trusted human. |

### The only two justifications for multi-agent

Every multi-agent design that genuinely works is an answer to exactly one of two limits:

- **The verification wedge** — checking is much cheaper than producing, so parallel attempts plus a mechanical checker beat one careful attempt.
- **The context ceiling** — the work is bigger than one window: quality degrades as the window fills, the agent forgets its plan, and a fifty-step job means fifty round-trips. A team is a mechanism for spending more tokens than one context can hold. (In one lab's postmortem, token spend explained ~80% of the variance between good and bad research runs; its multi-agent setup beat a single frontier agent by ~90%, essentially by out-spending it.)

A team pitch that answers neither is just more agents: a late-2025 study found adding agents can actively degrade results, with tool-heavy setups burning 2–6x the tokens to match one agent.

### The two money dials (a veto over shape)

A task can be perfectly agent-shaped and still not worth building. Before any build verdict stands, check: **recurrence** (how often does this come back?) and **value of a better answer** (what is a better result worth when it does?). A quarterly tool-and-contract audit passes both — regrows on schedule, one caught auto-renewal pays for years. A twice-a-year insurance/tax rig fails recurrence: right shape, wrong calendar — like building a swarm to research a dishwasher. Multi-agent runs can cost ~15x a chat; the dials decide whether that ever earns back.

### The T/C/L/D job-exposure audit

For "is my job / [team's role] exposed?" questions. Block 90 minutes; pull the last ten business days of calendar, sent mail, DMs, and real artifacts; tag every item fast, first instinct (ambiguous → L):

- **T — theatre.** Work the organization performs rather than examines: status meetings deciding nothing, decks nobody reads, cover-your-bases reviews. Test: if it vanished, the only consequence would be admitting it was performance. AI absorbs this layer first. Honest counts: 15–30%; first passes undercount by half.
- **C — commodity.** Real value that doesn't require *you*: routing, summarizing, applying known rules, coordinating decided things. Test: could you write a spec someone else executes with similar output? Typically 40–50%. Markets protect what's scarce now, not what was hard to learn.
- **L — on the line.** Structured pattern recognition, history-dependent relationships, the 30% juniors can't do that you can't articulate. Will split toward C and D over roughly 18 months.
- **D — durable.** Work you can't fully explain even afterward; you changed the question rather than answering it. Typically 10–20%, usually unrewarded because it's illegible to review systems.

T+C — the thin-ice fraction — runs **55–75%** for most senior knowledge workers (practitioner reports, 2026). Key distinction: D-work is *question-holding* (keeping the wrong framing open against pressure to resolve); C and L are *question-answering* — and answering is what AI absorbs fastest, because it can be specified and scored. The **legibility paradox**: D-work must be visible enough to be valued but not so documented it becomes runnable without you — show outcomes and calibration records, keep mechanism tacit, encode first-order rules but never meta-judgment. If T+C ≥ 75% with no D path, change roles — auditing the target role's actual incumbents, not its description.

### The reusable-rig doctrine

Design standard for anything you build: **every agent should make the next agent cheaper to build** — otherwise you're collecting chores. The rig is nine fixed stages, reused across jobs with only the "nouns" changing:

1. **Context pack** — explicit allowlist of what the agent may read. First safety decision; a bounded agent is auditable.
2. **Ingestion** — sources to text, with anchors back to original pages (anchors matter more than text).
3. **Chunking/tagging** — documents become addressable parts so the agent looks things up instead of reading.
4. **Normalization** — messy inputs become records; *missing* documents become records too, so gaps are actionable.
5. **Local inspectable store** — e.g., SQLite plus a folder. The database, not the model's memory, is the system of record.
6. **Deterministic retrieval** — the runbook says where to look; prefer structure lookups over vector search whenever auditability matters (when you must cite the exact clause, you know its address).
7. **Citation guard** — no anchor, no claim; ungroundable statements get flagged, not written around.
8. **Export packet** — editable files: timeline, evidence checklist (with gaps), draft letters, citation map, questions for the professional. A packet, never a submission.
9. **The gate** — the agent reads, organizes, drafts, cites, exports; it never sends, files, submits, pays, or signs. Expert-judgment items become handoff drafts a professional signs or doesn't; an auto-sent flawed appeal is a record in your name.

Flywheel test: compare last build's cost to this build's cost; if the second number isn't smaller, you have automations, not a system. Side benefit: normalized, cited data lets cheap models do the mechanical work.

### Org-level gates

**Six preconditions before AI changes a workflow** (most enterprises have built two): (1) workflow design — which decisions the model makes, which steps stay human, what "done" means; (2) data access — authoritative sources, permissions, staleness; (3) authority — reading, writing, spending as escalating risk tiers; (4) evaluation against the company's own policy, not benchmarks; (5) audit trails a risk team can reconstruct after a failure; (6) recovery and a named owner. Buyer test: which process runs differently afterward, and who proves improvement? "Employees will save time" doesn't qualify.

**Five-property test** for platform-automatable workflows: repeats on a schedule; recognizable good-vs-bad output (because you've done it by hand); describable in one paragraph; crosses 2+ tools; the path is known. If you can't describe it in one paragraph, you're asking the agent to resolve ambiguity your team hasn't resolved.

**Interface-type audit** so the legacy stack isn't silently excluded: inventory every piece of software touched in a week; classify each as structured/API-ready, GUI-only, or leave-alone; route structured work to connector-based agents and GUI-only work (legacy portals, unmaintained internal apps) to computer-use agents; then map single points of failure — connectors that could break, GUIs that could change.

**Build / buy / hire / wait** — a light capital-allocation checkpoint, not a technology question: score the workflow on recurrence, cost of error, judgment intensity, and whether imminent model improvement collapses what you'd build. Each wrong motion has a signature cost — hiring against AI-capable work builds a cost structure on disappearing scarcity; automating trust work breaks the process where the human mattered; buying generic for company-specific work means months fighting the product; custom-building solved problems burns scarce builders on commodity; waiting on a stable costly workflow is delay dressed as prudence. Analysts forecast over 40% of agentic AI projects canceled by end of 2027 — this triage keeps you out of that number.

## Workflow

1. **Inventory recurring work.** For a person: the T/C/L/D audit over the last ten business days. For an org: decompose into named workflows, each as `[workflow name] — [frequency] — [tools touched] — [T/C/L/D or n/a]`.

2. **Four-estimates screen per item.** One line per estimate: size, independence, separation, checkability. Don't skip independence.

3. **Money-dial veto.** Recurrence × value of a better answer. If the product is small, stop regardless of shape — record "agent-shaped, wrong calendar" so nobody re-litigates it.

4. **Assign verdicts.** Chat / single agent / team / don't bother, from the table above. For organizational items, run build/buy/hire/wait as a light checkpoint and confirm the six preconditions before build or buy proceeds.

5. **Interrogate every "team" verdict.** Demand the pitch name its limit: verification wedge or context ceiling. If it answers neither, downgrade to single agent.

6. **Sequence the build order.** Rank surviving builds by recurrence × value, highest first. Tiebreaker: which contributes the most rig stages to the next.

7. **Design each build as a rig, not a one-off.** Walk the nine stages; inherit existing components (the citation guard from [previous build] carries over, not rewritten). Keep the human gate hard. If the target crosses legacy software, run the interface-type classification first.

8. **Week-one evaluation.** (a) Time saved, measured honestly; (b) review burden below time saved; (c) would the team miss it if switched off — the only question predicting three-month survival. Governance trap: publishing with the builder's personal connections means every user acts with the builder's credentials — default to least privilege.

## Guardrails

- **Checkability decides everything.** No cheap verification → no volume strategy, no team, usually no build.
- **"Don't bother" is a success verdict.** Ten fluent, contradictory opinions on an unverifiable call are worth less than one human you trust.
- **Never split routine QA to a second agent.** Scripts and tests check correctness; second minds are only for conflicts of interest.
- **Team pitches must name their limit** (wedge or ceiling) or be downgraded. "More agents" is not an architecture.
- **Shape never overrides the money dials.** Agent-shaped + rare + low-stakes = don't build.
- **Automate coordination around judgment, never the judgment.** Agents clear the pile so humans decide faster.
- **The human gate is non-negotiable.** Agents never send, file, submit, pay, or sign.
- **Keep meta-judgment un-encoded.** The moment your full mechanism is documented, it's runnable without you.
- **Budget by capping, not just buying.** Identical runs can vary ~30x in spend; accuracy sometimes peaks at intermediate spend.

Related skills: when triage lands on "model work," use `model-selection-router` to pick which model runs it; once built, hand ownership and cost tracking to `agent-ops-governance`; for org-level value math, use `platform-roi-scorecard`.

## Suggested effort

- **Single-task verdict:** minutes. Four estimates, two dials, one line — not a document.
- **Personal job audit:** one 90-minute session plus a readout (thin-ice %, top T-cuts, one D-investment).
- **Backlog triage (5–20 workflows):** an hour or two; the steps 1–6 table with verdicts and a ranked build order.
- **Org deployment review:** add the six-precondition and build/buy/hire/wait checks — a half-day of interviews.
- Keep outputs decision-shaped: verdict, limit named, dials scored.
