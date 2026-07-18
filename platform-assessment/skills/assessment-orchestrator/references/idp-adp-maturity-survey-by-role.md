# IDP/ADP Maturity Survey — By Role

> **Repository integration note (2026-07-18):** This is the optional extended
> I7 instrument. Obtain the approvals and apply the cohort-suppression rules in
> `../SKILL.md` before distribution. Responses are Attested evidence and never
> directly assign a platform stage, ASDLC level, Agentic Developer Portal gate,
> or employee score. Use automated telemetry when available, and preserve
> cross-role contradictions rather than averaging them.

## Contents

1. [Response format guide](#response-format-guide--statement-scale-or-truefalse)
2. [Respondent context](#respondent-context-answer-once-regardless-of-role)
3. [Engineers](#section-1--engineers-individual-contributors)
4. [Technical leads](#section-2--technical-leads-senior-ics--team-leads)
5. [Managers](#section-3--managers-engineering-managers)
6. [Directors](#section-4--directors)
7. [Leadership](#section-5--leadership-vp--c-level)
8. [Scope notes](#known-gaps-closed-in-this-revision-and-whats-still-intentionally-out-of-scope)
9. [Response roll-up](#how-responses-roll-up)

One document, five role-specific sections. Each person only fills out **their own section** — questions are selected for what that role can actually speak to authoritatively, not a one-size-fits-all form. Every question carries its source methodology ID (from the [Methodology-Specific Questionnaires](methodology-specific-confirmation-gap-fill-questionnaires.md)) so responses route to the relevant evidence target, and a tag: **[CONFIRM]** validates an automated-scan finding, **[GAP-FILL]** captures something scanning can't see.

**Distribution guidance:** Send each section only to the matching role. Where the same underlying question appears in more than one role's section (e.g. adoption motivation, measurement trust), that's intentional — comparing how different roles answer the same question is itself a maturity signal, since platform teams and their consumers routinely perceive adoption/measurement differently.

**Estimated time:** Engineers ~10 min · Technical Leads ~16 min · Managers ~14 min · Directors ~12 min · Leadership ~6 min.

---

## Response Format Guide — Statement, Scale, or True/False?

Format is chosen per question based on what's being measured — not applied uniformly across the survey.

| Format | Use when... | Example | Why |
|---|---|---|---|
| **Binary (Yes/No/Not sure)** | The question checks whether a fact or artifact exists — a true two-state condition, no real middle ground | "Does a documented AI tool policy exist?" | Cleanest to score automatically; reserve strictly for genuinely two-state facts — forcing a gradient question (e.g. "is measurement mature?") into Yes/No destroys signal |
| **Single-select multiple-choice (3-5 options)** | The underlying reality is continuous or has more than two real states, but the states are mutually exclusive and need bucketing into one ordinal tier for scoring | Deployment-frequency bands mapping to DORA's Elite/High/Medium/Low tiers | Preserves ordinal signal while staying directly and consistently scoreable across respondents |
| **Multi-select (checkboxes)** | More than one option can be simultaneously true — the states are *not* mutually exclusive | "Which cloud providers does your org actively use? (select all that apply)" | Forcing a naturally multi-valued reality (multi-cloud, several AI tools in parallel use, several DORA metrics tracked at once) into single-select either loses information or produces a misleading "primary" answer that hides real complexity |
| **Likert scale (1-5)** | The question is about intensity, frequency, sentiment, or perceived degree — inherently graded, not categorical | Satisfaction, burnout, trust in data, cognitive load | Binary/MC would force an artificial cutoff on something respondents experience as a gradient; this is also the native format SPACE, DORA, and Team Topologies use for these constructs |
| **Open statement (free text)** | The question asks "why," "what's missing," or surfaces something structured options can't anticipate | "What's the biggest obstacle...?" | Required for true GAP-FILL context; routed through the LLM extraction layer (see "How Responses Roll Up") to tag against rubric dimensions after collection — never scored directly as typed |

**Rule of thumb applied throughout:** every [CONFIRM] fact-check question uses Binary or tight single-select MC bands (2-5 options); every [GAP-FILL] perceived-degree question uses Likert-5; every [GAP-FILL] reasoning/context question uses an open statement; use multi-select instead of single-select whenever the real-world answer can legitimately include more than one option at once (tool inventories, cloud providers in use, metrics tracked). Avoid true/false for anything with a real "sometimes" or "partially" state — several of the questions added below were specifically corrected to multi-select or Likert for this reason.

---

## Respondent Context (answer once, regardless of role)

Collected once per respondent so cross-role and cross-team contradictions in "How Responses Roll Up" can be traced to a specific team or business unit — without this, a disagreement between "engineers" and "directors" can't be segmented.

| ID | Question | Type |
|---|---|---|
| RC-1 | Which team/business unit are you answering on behalf of? | Open (short text or dropdown of known teams) |
| RC-2 | How long have you been in your current role? *(<6 months / 6-12 months / 1-3 years / 3+ years)* | MC |
| RC-3 | Approximately how many services/systems does your team own? | Open (numeric) |

---

## Section 1 — Engineers (Individual Contributors)

*You're closest to the daily friction. This section is about what you actually experience day-to-day — not policy, not strategy.*

| ID | Question | Type | Source | Tag |
|---|---|---|---|---|
| E-1 | How satisfied are you with your current tools, processes, and workload? | Likert-5 | SPACE-1 | GAP-FILL |
| E-2 | How often do you feel burned out or overloaded in a typical two-week period? | Likert-5 | SPACE-2 | GAP-FILL |
| E-3 | How much of your day is spent on focused, uninterrupted work vs. context-switching/meetings? *(Mostly focused / Roughly balanced / Mostly fragmented)* | MC | SPACE-4 | GAP-FILL |
| E-4 | How do you primarily get things done using the internal platform? *(Self-service via templates or portal / Standard tooling, some manual steps / Custom scripts or manual requests / Fully integrated into existing workflow)* | MC | CNCF-4 | CONFIRM |
| E-5 | Does the repository you work in most have documented build/test/lint commands anywhere — an `AGENT.md`/`AGENTS.md` file, README, or wiki? *(Yes, in AGENT.md or AGENTS.md / Yes, but only in README/wiki / No, it's tribal knowledge)* | MC | AGENTMD-1 | GAP-FILL |
| E-6 | Do AI coding agents (Claude Code, Cursor, Copilot) working in your repos actually follow the documented conventions, in your experience? *(Consistently / Sometimes / Rarely or never)* | MC | AGENTMD-3 | CONFIRM |
| E-7 | Beyond what's officially registered, are you aware of anyone on your team using an unregistered MCP server or AI agent tool integration? *(No / Yes, at least one / Not sure)* | MC | CSA-1 | GAP-FILL |
| E-8 | Rate your current cognitive load — the number of distinct systems, tools, and responsibilities you must track day-to-day. | Likert-5 (low → overloaded) | TT-3 | GAP-FILL |
| E-9 | [Open] What is the single biggest source of daily friction that slows you down right now — a tool, a process, or a missing capability? | Open | — | GAP-FILL |
| E-10 | [Open] Describe an AI agent skill, prompt, or MCP integration you built that you think other teams could reuse but currently don't know exists. | Open | Agent skill/reuse (§ Agent Skill Discovery) | GAP-FILL |
| E-11 | Were you informed that meeting, email, or chat data might be analyzed (in aggregate, de-identified form) as part of this maturity assessment? *(Yes, clearly communicated / I heard about it informally / No, this is the first I'm hearing of it)* | Binary/MC | Privacy/governance (main report §7.2) | GAP-FILL |
| E-12 | Which AI coding tools/agents does your team use regularly? *(select all that apply: Claude Code / Cursor / GitHub Copilot / Codex / Windsurf / Other / None)* | Multi-select | Agent tool inventory (AGENT.md / CSA context) | CONFIRM |

---

## Section 2 — Technical Leads (Senior ICs / Team Leads)

*You sit between code and architecture. This section covers review practices, golden-path adoption, and team-level agent governance.*

| ID | Question | Type | Source | Tag |
|---|---|---|---|---|
| TL-1 | What percentage of new services your team created last quarter came from a standardized "golden path" template rather than built from scratch? *(0% / 1-25% / 26-50% / 51-75% / 76-100%)* | MC | Service Catalog §C-2 | CONFIRM |
| TL-2 | Has the linked runbook for your team's primary service actually been used/followed during a real incident in the last 6 months? *(Yes / No incidents occurred / No, ignored or out of date)* | MC | CORTEX-2 | CONFIRM |
| TL-3 | Are documented SLOs for your team's services actively monitored and alerted on, or just recorded? *(Actively monitored / Recorded but not monitored / No SLOs exist)* | MC | CORTEX-3 | CONFIRM |
| TL-4 | If an `AGENT.md`/`AGENTS.md` file exists for your primary repo, when was it last verified against the actual current build/test process? *(Within the last month / 1-6 months ago / Longer than 6 months / Never verified)* | MC | AGENTMD-2 | CONFIRM |
| TL-5 | Do any of your team's AI agent/MCP integrations use plaintext API keys or long-lived tokens instead of short-lived, rotated credentials? *(No / Some legacy exceptions / Not sure / Yes)* | MC | CSA-2 | CONFIRM |
| TL-6 | For your team's custom maturity checks (beyond standard frameworks), are they evaluated automatically via integration, or manually? | Open + MC per check | OPSLEVEL-2 | CONFIRM |
| TL-7 | Which best describes your team's primary function? *(Ships value directly to users — stream-aligned / Provides a self-service platform to others — platform / Helps teams adopt new capabilities — enabling / Owns a deep, specialized subsystem — complicated-subsystem)* | MC | TT-1 | CONFIRM |
| TL-8 | When your team interacts with the platform team, is it mostly collaboration, X-as-a-Service (self-service), or facilitation (temporary hands-on help)? | MC | TT-2 | CONFIRM |
| TL-9 | [Open] What's missing from your repos' agent-facing documentation that causes AI agents to make repeated mistakes? | Open | AGENTMD-4 | GAP-FILL |
| TL-10 | [Open] What is the most common reason your team bypasses the service catalog or self-service tooling and does something manually instead? | Open | Service Catalog §C-4 | GAP-FILL |
| TL-11 | *(Only if not already captured by an engineering-intelligence platform)* How often does your team deploy code to production? *(On-demand/multiple times a day / Once a day to once a week / Once a week to once a month / Less than once a month)* | MC | DORA-1 | GAP-FILL |
| TL-12 | *(Fallback only)* What is the typical lead time from code commit to production deployment? *(Less than a day / One day to one week / One week to one month / More than one month)* | MC | DORA-2 | GAP-FILL |
| TL-13 | *(Fallback only)* What percentage of deployments cause a failure requiring a fix (rollback, hotfix, patch)? *(0-15% / 16-30% / 31-45% / 46%+)* | MC | DORA-3 | GAP-FILL |
| TL-14 | *(Fallback only)* When a service fails in production, how long does it typically take to restore service? *(Less than an hour / Less than a day / Less than a week / More than a week)* | MC | DORA-4 | GAP-FILL |
| TL-15 | Does your organization maintain a central service catalog (Backstage, Cortex, OpsLevel, Port.io, or an internal equivalent), and is it kept current? *(Yes, and it's kept current / Yes, but frequently stale / No)* | MC | Service Catalog §C-1 | CONFIRM |

---

## Section 3 — Managers (Engineering Managers)

*You own team-level investment, staffing, and process. This section covers funding, adoption motivation, and measurement trust.*

| ID | Question | Type | Source | Tag |
|---|---|---|---|---|
| M-1 | How is your team's platform-related work currently funded and staffed relative to demand? *(Fully funded to plan / Funded but understaffed / Ad hoc, reactive to crises / No dedicated budget)* | MC | CNCF-1 | GAP-FILL |
| M-2 | Why did your team originally start using the internal platform? *(Top-down mandate / Clear intrinsic value / Peer recommendation / No clear reason — erratic)* | MC | CNCF-2 | GAP-FILL |
| M-3 | How is platform-related work for your team planned, prioritized, and maintained today? *(Centrally managed with clear backlog / Tracked but loosely organized / Ad hoc, by request only / Proactive roadmap with regular releases)* | MC | CNCF-3 | CONFIRM |
| M-4 | Does your team measure platform/tooling success today, and how? *(Not measured / Ad hoc, inconsistent / Consistent quant + qual feedback / Fully integrated, continuous)* | MC | CNCF-5 | CONFIRM |
| M-5 | Is your team's output (PRs, tickets, deployments) currently tracked anywhere, and do you and your team trust that data? *(Tracked and trusted / Tracked but not trusted / Not tracked)* | MC | SPACE-5 | CONFIRM |
| M-6 | Has AI tooling changed your team's typical change size (PR/commit size) for better or worse? *(Smaller, more frequent changes / No noticeable change / Larger, riskier changes)* | MC | DORAAI-3 | GAP-FILL |
| M-7 | Is there a recurring forum (platform review board, architecture guild, AI governance committee) where infrastructure/AI-tooling decisions affecting your team are discussed and documented? *(Yes, regular and well-attended / Exists but inconsistent / No such forum)* | MC | TT-4 | CONFIRM |
| M-8 | On a scale of 1-5, how much duplicated effort do you believe exists across teams building similar AI agent tooling or prompts? | Likert-5 | Agent Skill Discovery §E-3 | GAP-FILL |
| M-9 | When a High/Critical CVE is found affecting your team's MCP servers or AI tooling, how quickly is it typically remediated? *(Within 30 days, tracked / Sometimes longer / No tracked SLA)* | MC | CSA-3 | CONFIRM |
| M-10 | [Open] What is the biggest *organizational* (not technical) obstacle to improving platform or AI-agent maturity for your team right now? | Open | TT-5 / general | GAP-FILL |
| M-11 | [Open] List any custom maturity checks or scorecards your team defines beyond standard frameworks (CNCF/DORA/Cortex). | Open | OPSLEVEL-1 | GAP-FILL |
| M-12 | Does your team have visibility into, and accountability for, its own cloud cost (FinOps practices)? *(Full visibility and accountability / Some visibility, no accountability / No visibility)* | MC | Infra/FinOps ("shifting down") | GAP-FILL |
| M-13 | Which DORA metrics does your team actively track on a recurring (weekly/monthly) basis? *(select all that apply: Deployment frequency / Lead time for changes / Change failure rate / Mean time to restore / None of these)* | Multi-select | DORA metric coverage | CONFIRM |

---

## Section 4 — Directors

*You own cross-team strategy, infra investment decisions, and governance policy. This section covers portfolio-level trade-offs, not individual services.*

| ID | Question | Type | Source | Tag |
|---|---|---|---|---|
| D-1 | Which best describes your organization's primary infrastructure hosting model across the teams you oversee? *(All on-premises / Single public cloud / Multi-cloud, unplanned / Multi-cloud, deliberate strategy / Hybrid on-prem + cloud)* | MC | Infra §A-1 | CONFIRM |
| D-2 | Does your organization have a documented, funded strategy for GPU/AI-compute capacity (on-prem clusters, reserved cloud GPU instances, or both)? *(Yes, documented and funded / Informal plans only / No plan / Not sure)* | MC | Infra §A-3 | GAP-FILL |
| D-3 | Is there a clear, communicated organization-wide policy on which AI coding tools are approved for use, and under what conditions? *(Yes, clear and well-communicated / Exists but poorly communicated / No policy exists)* | MC | DORAAI-1 | CONFIRM |
| D-4 | Across the teams you oversee, where is platform Investment (staffing/funding) *today* on a 1-5 scale, and where should it be in 12 months? | Two Likerts | MS-1 | GAP-FILL |
| D-5 | Across the teams you oversee, how automated is the path from "a team needs a new service/environment" to "it exists and is usable"? | Likert-5 | MS-3 | CONFIRM |
| D-6 | Across your org, how would you describe demand for new golden-path templates or self-service capabilities relative to what the platform team can currently deliver? | Likert-5 (far exceeds supply → fully met) | Service Catalog §C-3 | GAP-FILL |
| D-7 | Do your platform team(s) operate with product-management discipline (roadmap, feedback loops) or as a purely reactive service? *(Dedicated team with roadmap & feedback loops / Dedicated team, no product-management practice / Informal function only / No dedicated team)* | MC | CNCF/TT structure | CONFIRM |
| D-8 | [Open] What is the single biggest infrastructure or cloud-strategy decision your organization is currently debating that has *not* yet been reflected in any documentation or code? | Open | Infra §A-5 | GAP-FILL |
| D-9 | [Open] Which capability — investment, governance, provisioning, or measurement — would you prioritize improving first, and what would unlock it? | Open | MS-4 | GAP-FILL |
| D-10 | How would you rate the quality and accessibility of internal data that AI tools across your org can actually use (docs, code context, ADRs)? *(High quality, unified, AI-accessible / Exists but fragmented across systems / Mostly inaccessible or low quality)* | MC | DORAAI-2 | GAP-FILL |
| D-11 | How does your organization currently benchmark platform/AI maturity against industry peers? *(Formal benchmarking against a named framework / Informal, anecdotal comparison / Not benchmarked at all)* | MC | Benchmarking | GAP-FILL |
| D-12 | Which cloud providers does your organization actively use in production? *(select all that apply: AWS / Azure / GCP / On-prem or private cloud / Other)* | Multi-select | Infra multi-cloud signal | CONFIRM |

---

## Section 5 — Leadership (VP / C-Level)

*You set the strategic stance and own the ROI conversation. This section is intentionally short — five to seven questions only leadership can answer.*

| ID | Question | Type | Source | Tag |
|---|---|---|---|---|
| L-1 | Is there a clear, organization-wide AI stance that has been actively communicated (not just written down) to engineering? *(Yes, actively communicated and reinforced / Exists but rarely referenced / No clear stance)* | MC | DORAAI-1 (leadership accountability) | CONFIRM |
| L-2 | Is platform/AI-tooling investment tied to a measurable business outcome (e.g., delivery speed, incident reduction, cost) that leadership actively tracks? *(Yes, tracked and reviewed regularly / Loosely tied, rarely reviewed / Not tied to any measurable outcome)* | MC | Measurement / ROI | CONFIRM |
| L-3 | What is your organization's risk tolerance for AI agent autonomy? *(Draft-only — agents propose, humans approve everything / Limited autonomy in low-risk paths / Broad autonomy with audit trails / Not yet decided)* | MC | CSA governance stance | GAP-FILL |
| L-4 | Is the platform engineering function treated internally as a cost center or as a product with its own roadmap and success metrics? *(Product with roadmap & metrics / Cost center, budget-justified annually / Not clearly positioned either way)* | MC | CNCF Investment/Measurement | GAP-FILL |
| L-5 | How does leadership currently benchmark this organization's platform/AI maturity against industry or competitors? *(Formal benchmarking against a named framework / Informal, anecdotal comparison / Not benchmarked at all)* | MC | Benchmarking | GAP-FILL |
| L-6 | Is leadership aware of the legal/works-council obligations (GDPR, employee-monitoring consultation requirements) before any organizational mining of email, meeting, or chat data is deployed to support this assessment? *(Yes, legal/HR has been consulted / Not yet, but planned / Not considered)* | MC | Privacy/governance (main report §7.2) | GAP-FILL |
| L-7 | [Open] What business outcome would most justify further investment in platform engineering or agentic developer tooling over the next 12 months? | Open | — | GAP-FILL |

---

## Known Gaps Closed in This Revision (and What's Still Intentionally Out of Scope)

**Closed in this revision:**
- Core DORA deployment metrics (frequency, lead time, change-failure rate, MTTR) had no home in the original by-role split — added as a *fallback-only* block to Technical Leads (TL-11–14), since telemetry from an engineering-intelligence platform should always be preferred when available.
- Service catalog existence/staleness was referenced but never directly asked — closed via TL-15.
- Custom (OpsLevel-style) rubric elicitation was only confirmed, never elicited — closed via M-11.
- FinOps/cloud-cost accountability, called out in the source research as part of platform engineering "shifting down," was missing entirely — closed via M-12.
- AI-accessible internal data quality (a DORA AI Capability) had no Director-level question — closed via D-10.
- Director-level benchmarking was missing (only Leadership had it) — closed via D-11.
- Engineers were never asked whether they'd actually been informed that meeting/email/chat mining might occur — closed via E-11, since Leadership being informed (L-6) doesn't mean the people being mined were told.
- No question captured actual AI-tool inventory (as opposed to just governance/security posture) — closed via E-12 (multi-select).
- Respondent segmentation (team, tenure, team size) was entirely absent, making cross-role contradictions impossible to trace to a specific team — closed via the new Respondent Context block.
- Several questions that implied "more than one can be true" were incorrectly forced into single-select — corrected to multi-select (E-12, M-13, D-12).

**Still intentionally out of scope for this survey** (better handled elsewhere):
- Raw, granular telemetry (exact deployment counts, precise cycle-time percentiles) — this survey captures self-reported *bands*, not precise metrics; use the automated scan/engineering-intelligence integration for precision.
- Longitudinal trend comparison ("better or worse than last quarter") — requires repeated administration and a stored baseline, not a single-instance question; handle in the reporting layer by diffing successive survey runs, not by adding a comparison question here.
- Individual psychological-safety/trust-in-leadership questions beyond what SPACE's Satisfaction dimension already covers — that's an HR/eNPS instrument's job, not this maturity survey's.
- Formal penetration-test or red-team findings for MCP/agent security — those require an actual security assessment, not a self-report question; the CSA questionnaire's self-report answers should be treated as a screening signal that triggers a real security review, not a substitute for one.

---

## How Responses Roll Up

- **Per-methodology routing:** Route each answer by its Source column into the corresponding evidence target in the [Methodology-Specific Questionnaires](methodology-specific-confirmation-gap-fill-questionnaires.md). Treat vendor and external-framework results as supplemental profiles; only the repository's controlling scorers assign formal platform, ASDLC, and Agentic Developer Portal results.
- **Cross-role contradiction check:** Where the same question appears in multiple sections (adoption motivation in E/M, measurement trust in E/M, golden-path demand in TL/D), a disagreement between roles (e.g. engineers say "no clear reason — erratic" while directors say "clear intrinsic value") is itself a high-value finding — flag it directly in the report rather than averaging it away.
- **Open-ended routing:** Analyze open text only inside the approved survey boundary, redact identifiers before external model use, and emit minimized, rubric-tagged findings with confidence. Do not enable meeting, email, or chat mining merely because this survey is authorized.
- **Cadence:** Re-issue approved questions on the cadence in the assessment charter, preserving wording, cohort definitions, counts, response rates, and suppression rules across cycles.
