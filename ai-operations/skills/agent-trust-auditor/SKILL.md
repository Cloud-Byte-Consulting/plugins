---
name: agent-trust-auditor
description: >-
  Design and run verification for AI-agent output so you never take an agent's
  word for anything. Use when the user asks "can I trust my agent's output",
  "my agent made something up", "the agent fabricated a citation", "how do I
  verify agent work", "review agent PRs", "audit what the agent did", "agent
  QA", "build a judge layer", "when can my agent run autonomously", or wants
  checks, evals, approval gates, or acceptance criteria for delegated AI work.
  Covers the delegability test, workflow constitutions, cost-tiered auditing,
  actor/judge separation with allow-block-revise-escalate outcomes, the
  four-class action taxonomy, auditions before autonomy, and
  completion-vs-acceptance monitoring. For platform-level agent governance or
  compliance infrastructure, use the sibling platform-security-playbook skill
  instead; for application-layer RAG/LLM quality metrics, tracing, and offline
  eval suites, use llm-evals-engineer.
---

# Agent Trust Auditor

## Purpose

Help the user build a verification institution around their AI agents instead of hoping for a more trustworthy model. The fix for unreliable agents is structural: every "done" is testimony until an executable check says otherwise, every side-effectful action passes a judge before execution, and the verifiers themselves get audited. Verification that once took an expert days now runs as a script for pennies (practitioner reports, 2026), so the economics support checking everything, every round, with no rank exemptions.

Use this skill to audit an agent workflow for trust gaps, decide whether a task is delegable, write the acceptance standard, design a judge layer, run an audition before granting autonomy, or monitor when a workflow has earned more independence. Scope is workflow-level; for organization-wide governance, compliance, or security infrastructure, hand off to the sibling **platform-security-playbook** skill.

## Core model

### The four institutions

Trust at scale came from institutions, not trustworthy people — double-entry bookkeeping turned fraud into arithmetic; the aviation checklist answered "too much airplane for one pilot" without a better pilot. Four such institutions, now executable, form the backbone of agent trust. Adopt in order:

1. **The audit.** Every delegated task ships with an executable check that exercises the artifact itself: re-fetch cited sources and compare quotes character-for-character, compile the build and click the flows, reconcile totals against the source system. A worker's "done" report is testimony, not evidence.
2. **The org chart.** The strongest model does only judgment — specs, design decisions, review, dispute rulings — while cheap models do all the typing. Frontier attention is the scarcest resource in the stack.
3. **The constitution.** The standard for "done right," written once as testable criteria, enforced automatically every round (below).
4. **The appeals process.** Checks are reviewable: a failed worker can dispute, and sometimes the check is wrong and gets corrected. Without appeals, verification calcifies into bureaucracy that workers game instead of satisfy.

Why all four matter (practitioner reports, 2026): one build's audit caught a worker that fabricated 13 quoted passages while certifying zero errors; integration checks caught invisible-markup check-gaming; a quality gate caught the frontier "boss" model's own bug; appeals corrected a wrong check failing honest work. No punishment needed — hand exact failures back and retry; retries typically come back clean.

### The delegability test

One question converts vague hope into a delegable task: **what command proves this is done?** If you can write the executable proof, you can delegate the work today. If you can't, the task isn't ready — which is itself cheap, useful information.

### The constitution

Don't re-explain "what good means" task by task. Write it once: **10–14 testable criteria** defining done-right for [your workflow/domain], each phrased so a machine check could verify it (not "the report is high quality" but "every numeric claim carries a source ID that resolves"). A domain expert can usually write this from memory — the standard already exists in their head; hands were the constraint. Constitution plus check harness is the honest answer to "how do you prompt large work."

### The audition

Before trusting a worker model (or new agent configuration) with load-bearing work, give it a checkable tryout task scored by script — small, representative, pass/fail criteria drawn from the constitution. Auditions test capability and fit with your standard; failing one is cheap, the same failure in production is not.

### Cost-tiered auditing

Check weight matches risk, never uniform. The cheap-audit principle: a deterministic script audits everything; a cheap model audits what scripts can't; the frontier model reviews only what cheap auditing flags or what carries real consequence; humans review only what the frontier model escalates. A penny-per-pass audit makes "verify every round" affordable — while a judge wrapping every action in the same expensive process gets bypassed or disabled.

### The judge layer

The next serious agent failure won't be a jailbreak but a mundane action taken one step too far — an email sent because a thread seemed to imply approval. One prompt cannot pursue a task and police its own boundary; blanket approval modals fail because humans click through. The architecture: a **separate judge wrapped around the actor**, evaluating each proposed action before execution, with orchestration, coordination, and judgment in distinct layers.

**Four outcomes, not two:** **Allow** (execute), **Block** (halt, stating which criterion failed), **Revise** (directionally right, needs a specific change — e.g., send as draft, drop the attachment), **Escalate** (route to a human, stating what the human must evaluate). Revise and Escalate keep the judge from becoming pure friction. **Uncertainty produces Escalate — never default-Allow.**

**Judge criteria in four categories**, each a testable question, never "check if it's safe": *authorization* (explicitly authorized, current, not a stretched old instruction or an external party's reply mistaken for approval), *evidence* (right source of truth, correct target, nothing stale, disputed, or superseded), *exposure and risk* (what data reaches whom, what changes, reversibility, worst plausible consequence), *policy* (explicit rules, legal/security boundaries, when policy demands a human instead of automation). Criteria must exist before the judge prompt does — the prompt implements policy; it is not the policy.

### The four-class action taxonomy

Classify every action an agent can take; controls scale by class:

| Class | Examples | Control |
|---|---|---|
| 1. Read-only | retrieve, summarize, classify, draft | No heavy judge unless sensitive data or high-stakes delivery |
| 2. Reversible writes | labels, internal notes, local files, branches | Lightweight validation or post-hoc audit |
| 3. External side effects | messages sent, external systems updated, PRs opened, public posts | Judge before execution — others are affected |
| 4. High-risk | spending, deletion, permission changes, merges, production commands | Judge + human approval, unless a very narrow explicit policy permits automation |

Treating everything as harmless produces incidents; treating everything as catastrophic produces unusable products — classification prevents both.

### The action-proposal schema

Before any class-3 or class-4 call, the actor emits a structured proposal: **intended action, reason, supporting evidence with sources, authorization basis, expected consequence, data exposed, reversibility/rollback path, risk flags.** The judge inspects claims against criteria instead of vibing on prose; having to justify itself also measurably improves the actor.

### Judge failure modes

1. **Correlated judgment** — a judge sharing the actor's model, context, or prompt style shares its blind spots; at worst it launders confidence. Mitigate with clearer criteria, different prompts, deterministic checks, model diversity, human review where consequence justifies.
2. **Specification gaming** — actors learn to over-justify or phrase risky actions innocently; structured proposals are the antidote.
3. **Escalation drift** — over-escalation becomes a paging system; under-escalation lets confident language substitute for authorization.
4. **Latency and cost** — uniform expensive checking gets bypassed; match check weight to action class.
5. **Policy drift** — an unversioned judge prompt silently enforces last quarter's rules.

Start with one general judge; split into specialists (authorization and privacy first) only when the prompt gets too long to reason about. Make checks deterministic wherever a check can be a script.

### Completion vs acceptance

The unit of agent product behavior is the **run** — the delegated task, tools touched, boundaries hit, corrections received, and whether anyone accepted the result; a dashboard can read green while the run underneath destroys something. The quadrant: **high completion + low acceptance** = finishing work nobody trusts; **low + low** = users bail early, not viable yet; **low completion + high acceptance** = too cautious but valuable, loosen carefully; **high + high** = the workflow has earned more autonomy.

**Corrections are eval labels.** Every interrupt, edit, denied approval, and reopened task is a user-written label; pipe them into the judge's and constitution's eval sets. Approval patterns talk too: always-approved dialogs are friction, instantly-approved high-risk actions are theater, repeatedly denied action classes mean the agent proposes wrong work.

### Two-model review for documents

For decks, workbooks, and reports — artifacts that look done long before they're true — apply actor/judge separation as a **builder/reviewer pair in two separate model contexts**. One model assembles from a source inventory built before any slide exists (IDs, dates, status labels, conflict log); a second, in a fresh context, runs a hostile review — claims without sources, undated numbers, inconsistent formulas, assumptions posing as facts — and returns an **edit list, never a rewrite**. Loop until edits stop landing; an author never approves its own pull request. Add a checks tab as smoke alarm (tie-outs, formula consistency, hardcode scans, stale dates). The loop raises the floor; it doesn't replace the human who knows what the number should be.

### Process, not authorship

Once machines interrogate code and content better than humans, "a human wrote it" stops being a trust signal — unreviewed hand-written work is an assertion of competence, not demonstrated fact. Trust attaches to **process**: not "who wrote this?" but "what process forced this to become trustworthy?" So:

- Ship **evidence packets** with significant artifacts: what was generated, from what spec, attacked by which checks, with what residual risk.
- **Comprehensibility is a security property** — illegible output resists the tools that could verify it, so quality debt is trust debt. Weight eval suites for generated code roughly half toward quality checks (readability, hygiene, dependency discipline), not the usual functional-heavy split.
- Humans move up-stack to architects of meaning — invariants, threat models, what must never happen — which demands more rigor, not less. And discovery isn't safety: finding problems only pays if patch-and-deploy throughput beats the failure's blast radius.

## Workflow

Run in order; each step produces a concrete artifact.

1. **Scope the agent surface.** Inventory agent work, existing or planned. Output: a one-page map of [workflow → artifacts → tools → consumers].
2. **Delegability screen.** For each workflow: what command proves this is done? Sort into *delegable now*, *delegable after harness work*, and *not delegable* (no executable proof — keep a human in the loop, explicitly). Output: sorted list with a proof statement per item.
3. **Write the constitution.** Per delegable workflow, draft 10–14 testable criteria with the domain expert, each checkable by script or cheap model, plus the appeals rule: how a worker disputes a failing check, who corrects wrong checks. Output: one versioned constitution per workflow.
4. **Classify actions and wire the control layer.** Assign every agent action to one of the four classes; wire controls by class — post-hoc audit for class 2, judge-before-execution with the proposal schema for class 3, judge plus human approval for class 4. Write judge criteria before the judge prompt. Output: action inventory, proposal schema, criteria doc, judge prompt.
5. **Run the audition.** Before granting autonomy, score a checkable tryout task by script against the constitution. Hire, adjust, or reject on the result. Output: audition task, scoring script, pass/fail record.
6. **Instrument completion vs acceptance.** Start with three events joined on one run ID — run started, task completed, correction submitted — then expand into tool failures, approval denials, permission blocks, memory misses, escalations, abandonment. Expand autonomy only for high/high workflows, one action class at a time.
7. **Feed corrections back into evals.** Route every correction, denied approval, and appeal outcome into eval cases for the judge and checks. Build judge cases across all four outcomes, biased toward mundane failures (wrong recipient, stale memory, partial authorization) over red-team drama. Track false allows, false blocks, escalation/revision rates, latency, cost per judged action, override rate, and incidents caught pre-execution, by action class. Audit the review surface: rubber-stamped escalations are fake review; repeated unchanged resubmissions are a broken actor/judge contract.

Start small — one workflow, one action boundary, one judge, one eval set, one feedback loop — then the contract travels to the next boundary.

## Guardrails

- **Never accept a self-report as verification.** "The agent says it's done" is testimony; a process ending at the agent's own summary is the first gap to close.
- **The actor never judges its own action.** One prompt doing the work and deciding whether it may proceed is broken by design.
- **Uncertainty escalates; it never default-allows.**
- **No rank exemptions.** The frontier model, judge, checks, and dashboard get the same adversarial treatment as the cheapest worker.
- **A judge without an eval suite is just another model call.** Don't ship one without cases across all four outcomes.
- **Don't gold-plate class-1 actions.** Heavy judgment on read-only work gets the whole control layer disabled.
- **Version the constitution and judge prompt like code.** Unversioned policy silently enforces last quarter's rules.
- **Govern memory write-back.** Label provenance on every stored judgment: observed / inferred / generated / confirmed / disputed / superseded. Agent-written memory starts as evidence; instruction-grade status requires human confirmation — ungoverned memory makes future agents confidently wrong.
- **Scope handoffs.** Platform-wide governance, compliance, or security infrastructure → **platform-security-playbook**. Ownership and cost accountability for agent fleets → **agent-ops-governance**. Validation-loop maturity → **asdlc-maturity-assessment**. Application-layer RAG/LLM quality evals, tracing, and metric suites → **llm-evals-engineer**, which evaluates retrieval + generation quality while this skill judges agent actions and delegation trust.

## Suggested effort

- **Quick trust check (15–30 min):** delegability test on one workflow plus a sketch of the four-class action inventory. Deliverable: a gap list.
- **Standard engagement (half day):** steps 1–4 for one workflow. Deliverable: constitution plus control-layer design the team can implement.
- **Full audit (1–3 days, iterative):** all seven steps for [the target workflow], including audition, instrumentation plan, and eval feedback loop. Deliverable: a running verification institution, not a document.
- Calibrate depth to consequence: a research-summary agent needs step 2 and a light constitution; an agent that emails externally or touches money needs the full judge layer and human approval paths first.
