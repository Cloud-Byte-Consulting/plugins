# Methodology-Specific Confirmation & Gap-Fill Questionnaires

> **Repository integration note (2026-07-18):** Use these as supplemental,
> methodology-specific evidence prompts after automated evidence leaves a gap
> or needs confirmation. Responses are Attested evidence, not tie-breakers and
> not formal scores. Only the controlling scorers named in `../SKILL.md` assign
> platform, ASDLC, or Agentic Developer Portal results. Preserve contradictory
> evidence instead of averaging it.

## Contents

1. [Trigger matrix](#0-master-trigger-matrix--which-questionnaire-to-fire-and-why)
2. [CNCF platform engineering](#1-cncf-platform-engineering-maturity-model)
3. [Microsoft platform engineering](#2-microsoft-platform-engineering-capability-model)
4. [DORA core metrics](#3-dora-core-metrics--quick-check)
5. [DORA AI capabilities](#4-dora-ai-capabilities-model)
6. [SPACE](#5-space-framework)
7. [Cortex AI readiness](#6-cortex-ai-readiness-scorecard)
8. [OpsLevel-style custom rubric](#7-opslevel-style-custom-maturity-rubric)
9. [CSA MCP security](#8-csa-mcp-security-maturity-model)
10. [Agent instructions](#9-agentmd--agentsmd-standard)
11. [Team Topologies](#10-team-topologies-assessment)
12. [Deployment notes](#deployment-notes-applies-to-all-ten)

This set gives each scoring methodology from the [IDP/ADP Maturity Assessment Research](idp-adp-maturity-assessment-research.md) its own dedicated, native-scale questionnaire — instead of one blended survey. Deploy a questionnaire only when the automated scan (repo/API/telemetry) for that specific methodology **can't reach a verdict** or **needs confirmation**. Each question is tagged:

- **[CONFIRM]** — validates/triangulates a score the automated scan already produced
- **[GAP-FILL]** — captures information the automated scan structurally cannot see (intent, culture, roadmap, trust)

Every questionnaire preserves that methodology's own native scale (not the unified Level 0-4 rubric from the main report), so results feed straight back into that methodology's own reporting format.

---

## 0. Master Trigger Matrix — Which Questionnaire to Fire, and Why

| Situation encountered during automated scanning | Fire this questionnaire | Why |
|---|---|---|
| No engineering-intelligence platform (LinearB/Jellyfish/Swarmia/Faros) integrated; can't compute deployment frequency/lead time/MTTR/CFR from raw Git/CI data | **§3 DORA Quick Check** | These four metrics can't be reliably inferred from static files alone |
| Deployment metrics ARE captured automatically, but you need to know if AI tooling changed them | **§4 DORA AI Capabilities** | AI-usage attribution requires self-report; not visible in commit metadata |
| No SPACE-aligned survey/pulse tool exists (no Officevibe/Culture Amp/eNPS data) | **§5 SPACE Framework** | Satisfaction, wellbeing, and Communication/Collaboration dimensions are inherently unscannable |
| Service catalog is populated (hard signal = high maturity) but you suspect "maturity theater" | **§1 CNCF** + **§2 Microsoft** (Measurement/Interfaces sections) | Confirms whether populated metadata is actually trusted/used, not just present |
| Cortex/OpsLevel-style scorecard exists but some checks can't be verified via API (e.g., "is the runbook actually followed") | **§6 Cortex AI Readiness** or **§7 OpsLevel Rubric** | Closes the gap between "field is filled in" and "practice is real" |
| MCP server scanner finds some registered servers but you suspect shadow/unregistered agent tool usage | **§8 CSA MCP Security** | Static/API scanners can only find what's registered; unregistered usage is a self-report gap |
| Repo has no `AGENT.md`/`AGENTS.md` file, or one exists but content looks templated | **§9 AGENT.md/AGENTS.md** | Confirms whether an equivalent convention exists elsewhere (tribal knowledge) before scoring Level 0 |
| Org chart / repo ownership data is ambiguous or you can't tell if a "platform team" behaves like Team Topologies' definition | **§10 Team Topologies** | Team interaction mode and cognitive load are perceptual, not structural |
| Any hard signal and any approved human-sensing signal disagree | Fire the questionnaire matching the **contradicting dimension** | Add the response as another evidence record; preserve the contradiction for the controlling scorer rather than treating the survey as a tie-breaker |
| Scheduled re-validation cycle | Select only the questionnaires justified by current gaps, the approved population, and the assessment charter | Avoid unnecessary collection and preserve comparability for questions that are re-issued |

---

## 1. CNCF Platform Engineering Maturity Model

**Native scale:** 5 aspects — Investment, Adoption, Operations, Interfaces, Measurement — each independently rated across four descriptive levels (Ad hoc → Erratic/Mandate-driven → Centrally tracked → Fully embedded), following the categorical breakdowns used in the Puppet/Weave operationalization of this model.

**When to use:** Trigger for any of the five CNCF aspects that automated scanning cannot directly observe — specifically Investment (funding/staffing decisions live in budget systems, not code) and Adoption (motivation/intent is never visible in a repo). Also fire the Operations/Measurement questions whenever a populated catalog or dashboard needs a "is this actually used" check.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| CNCF-1 | How is the platform team currently funded and staffed relative to demand? *(Fully funded to plan / Funded but understaffed / Ad hoc funding, reactive to crises / No dedicated budget)* | MC | GAP-FILL | Investment |
| CNCF-2 | Why did your team originally start using the internal platform? *(Top-down mandate / Clear intrinsic value / Peer recommendation / No clear reason — erratic)* | MC | GAP-FILL | Adoption |
| CNCF-3 | How is platform work planned, prioritized, and maintained today? *(Centrally managed with clear backlog / Tracked centrally but loosely organized / Ad hoc, by request only / Proactive roadmap with regular releases)* | MC | CONFIRM | Operations |
| CNCF-4 | How do you primarily interact with the platform to get things done? *(Self-service via templates or portal / Standard tooling, some manual steps / Custom scripts or manual requests / Fully integrated into existing workflow, no separate interface)* | MC | CONFIRM | Interfaces |
| CNCF-5 | Does your organization measure platform success today, and how? *(Not measured at all / Ad hoc, inconsistent feedback / Consistent quant + qual feedback / Fully integrated, continuous measurement)* | MC | CONFIRM | Measurement |
| CNCF-6 | [Open] If the catalog/dashboard data suggests high maturity but you disagree, explain the gap between what's recorded and what actually happens. | Open | GAP-FILL | Cross-aspect contradiction check |

**Interpretation guidance:** Map each answer to the relevant CNCF aspect as
Attested evidence. Keep platform-team and consumer cohorts separate, report
counts and denominators, and preserve perception gaps. Send the evidence to
`platform-maturity-benchmark`; do not average respondent roles or assign a CNCF
stage from this questionnaire alone.

---

## 2. Microsoft Platform Engineering Capability Model

**Native scale:** 6 capabilities — Investment, Adoption, Governance, Provisioning & Management, Interfaces, Measurement/Feedback — each self-plotted on a current-state vs. desired-state radar/spider chart (informal 1-5 stage scale per capability, no fixed universal labels).

**When to use:** Trigger whenever you need the org to explicitly state both *current* and *desired* maturity per capability — this dual current/desired framing is unique to Microsoft's model and something automated scanning can never produce (it can only observe current state). Best used once per business unit per assessment cycle, run by a facilitated workshop rather than a blind form.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| MS-1 | On a 1-5 scale, where is Investment (staffing/funding) *today*, and where should it be in 12 months? | Two Likerts | GAP-FILL | Investment (current + desired) |
| MS-2 | On a 1-5 scale, rate current Governance maturity: is there a clear, enforced policy for who can change what, and how consistently is it followed? | Likert-5 | CONFIRM | Governance |
| MS-3 | On a 1-5 scale, rate Provisioning & Management: how automated is the path from "I need a new service/environment" to "it exists and is usable"? | Likert-5 | CONFIRM | Provisioning & Management |
| MS-4 | Which capability, if improved first, would unlock the most value for your team in the next quarter? | Open | GAP-FILL | Prioritization signal (feeds roadmap, not a scan output) |
| MS-5 | [Open] Where does the radar-chart gap between current and desired state feel most painful day-to-day? | Open | GAP-FILL | Qualitative context for biggest current/desired delta |

**Scoring guidance:** Plot current-state Likert averages directly onto the six-axis radar chart; keep desired-state as a second overlay series. The delta between the two series — not the absolute score — is the primary output Microsoft's model is designed to produce, and should drive roadmap prioritization directly.

---

## 3. DORA Core Metrics / Quick Check

**Native scale:** Four performance tiers — **Elite, High, Medium, Low** — across four metrics: deployment frequency, lead time for changes, change failure rate, mean time to restore (MTTR).

**When to use:** Trigger only when these four metrics cannot be computed automatically from CI/CD and incident systems (no engineering-intelligence platform integrated, or partial API access). If telemetry is available, skip this questionnaire entirely and use the hard signal — DORA's own instrument is designed as a substitute for missing telemetry, not a complement to it.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| DORA-1 | How often does your team deploy code to production? *(On-demand/multiple times a day / Between once a day and once a week / Between once a week and once a month / Less than once a month)* | MC | GAP-FILL | Deployment frequency tier |
| DORA-2 | What is the typical lead time from code commit to production deployment? *(Less than a day / One day to one week / One week to one month / More than one month)* | MC | GAP-FILL | Lead time tier |
| DORA-3 | What percentage of deployments cause a failure requiring a fix (rollback, hotfix, patch)? *(0-15% / 16-30% / 31-45% / 46%+)* | MC | GAP-FILL | Change failure rate tier |
| DORA-4 | When a service fails in production, how long does it typically take to restore service? *(Less than one hour / Less than one day / Less than one week / More than one week)* | MC | GAP-FILL | MTTR tier |
| DORA-5 | [Open] What is the single biggest bottleneck currently preventing faster/safer deployment? | Open | GAP-FILL | Root-cause context, not directly scored |

**Scoring guidance:** Use DORA's own published tier boundaries directly (Elite/High/Medium/Low) per metric; do not average across the four metrics into one number — DORA explicitly evaluates and reports them as a profile, not a composite score.

---

## 4. DORA AI Capabilities Model

**Native scale:** Seven capabilities (Clear/communicated AI stance, Healthy data ecosystems, AI-accessible internal data, Strong version control, Small batch sizes, User-centric focus, Quality internal platforms), each rated Present/Partial/Absent, feeding into an overall organizational AI-capability profile.

**When to use:** Trigger for capabilities that are inherently attitudinal or policy-based and cannot be scanned — especially "clear AI stance" and "user-centric focus," which live in leadership communication and product strategy, not code. Skip "quality internal platforms" here — that capability is already covered by the CNCF/Microsoft questionnaires above, since DORA explicitly treats it as the IDP-maturity prerequisite, not a distinct AI-specific question.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| DORAAI-1 | Is there a clear, communicated organizational policy on which AI tools are approved, and under what conditions? *(Yes, clear and well-communicated / Exists but poorly communicated / No policy exists)* | MC | CONFIRM | Clear/communicated AI stance |
| DORAAI-2 | How would you rate the quality and accessibility of internal data that AI tools can actually use (docs, code context, ADRs)? *(High quality, unified, AI-accessible / Exists but fragmented across systems / Mostly inaccessible or low quality)* | MC | GAP-FILL | Healthy data ecosystems / AI-accessible internal data |
| DORAAI-3 | Has AI tooling changed your team's batch size (size of individual changes/PRs) for better or worse? *(Smaller, more frequent changes / No noticeable change / Larger, riskier changes) | MC | GAP-FILL | Working in small batches |
| DORAAI-4 | Since adopting AI coding tools, has product/strategy clarity kept pace with increased delivery speed? *(Yes, clear priorities guide the increased output / Somewhat, occasional misalignment / No, we're shipping faster without clear direction)* | MC | GAP-FILL | User-centric focus |
| DORAAI-5 | [Open] Describe a specific instance where AI tooling amplified either a strength or a dysfunction already present in your team's process. | Open | GAP-FILL | Validates DORA's "AI as amplifier" thesis at the team level |

**Scoring guidance:** Score each capability Present/Partial/Absent independently, then cross-reference against the CNCF/Microsoft platform-quality scores — DORA's model predicts that AI capability gains will track platform quality; a high AI-capability score paired with a low platform-quality score is itself a flag worth surfacing in the report.

---

## 5. SPACE Framework

**Native scale:** Five dimensions (Satisfaction & wellbeing, Performance, Activity, Communication & collaboration, Efficiency & flow) — not leveled, but scored by instrumentation coverage (Not measured / Partially measured / Comprehensively measured) plus the underlying sentiment/metric values themselves.

**When to use:** Trigger for Satisfaction/wellbeing and Communication/collaboration in every cycle — these two dimensions are structurally unmeasurable by code/API scanning. Trigger Performance/Activity/Efficiency only when no engineering-intelligence platform is deployed to compute them automatically.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| SPACE-1 | How satisfied are you with your current tools, processes, and workload? *(5-point Likert)* | Likert-5 | GAP-FILL | Satisfaction & wellbeing |
| SPACE-2 | How often do you feel burned out or overloaded in a typical two-week period? *(5-point Likert)* | Likert-5 | GAP-FILL | Satisfaction & wellbeing |
| SPACE-3 | How would you rate the quality of communication and knowledge-sharing across your team and adjacent teams? *(5-point Likert)* | Likert-5 | GAP-FILL | Communication & collaboration |
| SPACE-4 | How much of your day is spent on focused, uninterrupted work vs. context-switching/meetings? *(Mostly focused / Roughly balanced / Mostly fragmented)* | MC | GAP-FILL | Efficiency & flow |
| SPACE-5 | Is your output (PRs, tickets, deployments) currently tracked anywhere, and do you trust that data? *(Tracked and trusted / Tracked but not trusted / Not tracked)* | MC | CONFIRM | Activity / Performance measurement coverage |
| SPACE-6 | [Open] What is the biggest source of friction preventing focused, satisfying work right now? | Open | GAP-FILL | Root-cause context for Satisfaction/Efficiency |

**Scoring guidance:** Report each dimension separately — SPACE explicitly warns against collapsing multiple dimensions into one composite score, since that reintroduces the single-metric gaming problem the framework was designed to avoid.

---

## 6. Cortex AI Readiness Scorecard

**Native scale:** Three cumulative tiers — **Bronze** (ownership defined, runbook linked, on-call rotation configured), **Silver** (SLOs defined, CI/CD pipeline active, dependency inventory current), **Gold** (AI model security scanning enabled, test coverage minimum met, DORA metrics within target).

**When to use:** Trigger per-service when the Cortex/OpsLevel-style scorecard shows a field as "filled in" but you need to confirm the underlying practice is real (e.g., a runbook link exists but nobody follows it) — this is the classic maturity-theater gap.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| CORTEX-1 | Is there a single, current owner for this service who would be paged if it broke tonight? *(Yes, confirmed and current / Listed but likely stale / No owner)* | MC | CONFIRM | Bronze — ownership |
| CORTEX-2 | Has the linked runbook for this service been used/followed during an actual incident in the last 6 months? *(Yes / No incidents occurred / No, it was ignored or out of date)* | MC | CONFIRM | Bronze — runbook validity |
| CORTEX-3 | Are the documented SLOs for this service actively monitored and alerted on, or just recorded? *(Actively monitored and alerted / Recorded but not monitored / No SLOs exist)* | MC | CONFIRM | Silver — SLOs |
| CORTEX-4 | Is the dependency inventory for this service accurate as of today? *(Yes, verified recently / Probably stale / Never verified)* | MC | CONFIRM | Silver — dependency inventory |
| CORTEX-5 | Has this service's DORA metrics (deployment frequency, MTTR) actually been reviewed against target benchmarks in the last quarter? *(Yes, reviewed and within target / Reviewed but missed target / Never reviewed)* | MC | CONFIRM | Gold — DORA metrics |
| CORTEX-6 | [Open] Which scorecard field for this service do you personally distrust, and why? | Open | GAP-FILL | Maturity-theater detection |

**Scoring guidance:** A service only advances to the next tier once every field in the lower tier is confirmed (not just present) — treat any "stale/ignored/distrusted" response as a hard block on tier advancement regardless of what the automated scorecard check shows.

---

## 7. OpsLevel-Style Custom Maturity Rubric

**Native scale:** Organization-defined — custom levels per service, each backed by automated checks pulled from integrated tools. No universal levels; the rubric itself must first be elicited from the org before it can be scored.

**When to use:** Trigger when the org has (or wants) bespoke maturity criteria not covered by any standard framework above, or when integrated check sources are incomplete and a manual attestation is the only way to evaluate a custom check this cycle.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| OPSLEVEL-1 | List the custom maturity checks your organization currently defines (or wants to define) for a service, beyond what CNCF/DORA/Cortex already cover. | Open | GAP-FILL | Rubric elicitation |
| OPSLEVEL-2 | For each custom check, is it currently evaluated automatically (via integration) or manually? | MC per check | CONFIRM | Automation coverage of custom rubric |
| OPSLEVEL-3 | For any custom check currently marked "automated," has anyone manually verified the automation is actually correct in the last quarter? *(Yes / No / Not sure)* | MC | CONFIRM | Automation trust check |
| OPSLEVEL-4 | Which custom check, if it failed silently, would cause the most damage before anyone noticed? | Open | GAP-FILL | Risk prioritization for rubric design |

**Scoring guidance:** Because this rubric is bespoke, scoring is org-specific by design — the questionnaire's real output is a maintained, versioned rubric definition (feed OPSLEVEL-1 answers into the scorecard config), with OPSLEVEL-2/3 used to flag which "automated" checks actually need re-validation.

---

## 8. CSA MCP Security Maturity Model

**Native scale:** Four cumulative levels — **Level 1** (authenticated connections, TLS 1.2+, complete MCP server inventory, least-privilege accounts, 90-day audit logs, quarterly vuln review), **Level 2** (tool integrity/hashing, session hardening, <30-day CVE remediation SLA), **Level 3-4** (execution isolation, behavioral/runtime monitoring, supply-chain validation, mapped to OWASP ASI/MITRE ATLAS).

**When to use:** Trigger whenever the automated MCP scanner (`mcp-scan`, MCP Gateway & Registry, etc.) can only see *registered* servers — shadow/unregistered agent tool usage is common and structurally invisible to any inventory-based scanner. Also trigger to confirm process-level controls (remediation SLA adherence, quarterly review cadence) that a point-in-time scan can't verify.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| CSA-1 | Beyond what's in the central MCP registry, are you aware of any team using an unregistered MCP server or AI agent tool integration? *(No, registry is complete / Yes, at least one / Not sure)* | MC | GAP-FILL | Level 1 — inventory completeness |
| CSA-2 | Do any of your AI agent/MCP integrations use plaintext API keys or long-lived tokens instead of short-lived, rotated credentials? *(No, all short-lived/rotated / Some legacy exceptions / Not sure / Yes, plaintext keys are used)* | MC | CONFIRM | Level 1-2 — authentication hygiene |
| CSA-3 | When a High/Critical CVE is found in an MCP server or dependency, how quickly is it typically remediated? *(Within 30 days, tracked / Sometimes longer than 30 days / No tracked SLA)* | MC | CONFIRM | Level 2 — CVE remediation SLA |
| CSA-4 | Is there a documented, actually-followed quarterly review process for MCP server vulnerabilities? *(Yes, followed consistently / Documented but inconsistently followed / No such process)* | MC | CONFIRM | Level 1 — quarterly vuln review |
| CSA-5 | [Open] Describe any recent instance where an AI agent or MCP integration had access to more data/systems than it actually needed. | Open | GAP-FILL | Least-privilege violations (Level 1) + supply-chain risk (Level 3-4) |

**Scoring guidance:** This model is explicitly cumulative — an org cannot claim Level 2 if any Level 1 control fails, so score conservatively: the lowest confirmed level across all questions is the org's overall CSA level, regardless of how advanced any individual answer looks.

---

## 9. AGENT.md / AGENTS.md Standard

**Native scale:** Binary presence, then content completeness — Absent / Present-but-templated (empty placeholders) / Present-partial (some sections filled) / Present-complete-and-fresh (build/test commands, code style, PR conventions all documented and recently updated).

**When to use:** Trigger when static scanning finds no `AGENT.md`/`AGENTS.md` (or predecessor tool-specific file) in a repo — to confirm whether an equivalent convention exists elsewhere (README, wiki, tribal knowledge) before scoring the repo at Level 0. Also trigger when a file exists but appears templated, to check whether its content is actually followed.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| AGENTMD-1 | Does this repository have documented build/test/lint commands anywhere (even outside a formal AGENT.md file)? *(Yes, in AGENT.md or AGENTS.md / Yes, but only in README/wiki / No, it's tribal knowledge)* | MC | GAP-FILL | Presence equivalence check |
| AGENTMD-2 | If an AGENT.md/AGENTS.md file exists, when was it last verified against the actual current build/test process? *(Within the last month / 1-6 months ago / Longer than 6 months / Never verified)* | MC | CONFIRM | Freshness |
| AGENTMD-3 | Have AI coding agents (Claude Code, Cursor, Copilot) working in this repo actually followed the documented conventions, in your experience? *(Consistently / Sometimes / Rarely or never used the file)* | MC | CONFIRM | Content quality / actual utility |
| AGENTMD-4 | [Open] What's missing from this repo's agent-facing documentation that causes agents to make repeated mistakes? | Open | GAP-FILL | Content-gap detection for remediation |

**Scoring guidance:** A "Present-complete" file that's never actually followed by agents (AGENTMD-3 = "rarely/never") should be down-scored to "Present-partial" — presence and freshness alone overstate maturity if agents demonstrably ignore the file.

---

## 10. Team Topologies Assessment

**Native scale:** Four team types (stream-aligned, platform, enabling, complicated-subsystem) and three interaction modes (collaboration, X-as-a-Service, facilitating), plus a separate Cognitive Load rating (low/manageable/high/overloaded) from the companion Team Cognitive Load Assessment.

**When to use:** Trigger whenever org-chart or repo-ownership data is ambiguous about which team-type a given team actually functions as, or whenever you need direct perceptual input on cognitive load and interaction-mode friction — none of this is inferable from static artifacts alone.

| ID | Question | Type | Tag | Maps to |
|---|---|---|---|---|
| TT-1 | Which best describes your team's primary function? *(Ships a stream of business value directly to users — stream-aligned / Provides a self-service platform to other teams — platform / Helps other teams adopt new capabilities — enabling / Owns a deep, specialized subsystem — complicated-subsystem)* | MC | CONFIRM | Team type classification |
| TT-2 | When your team interacts with the platform team, is it mostly collaboration (working together), X-as-a-Service (self-service, minimal contact), or facilitation (temporary hands-on help)? | MC | CONFIRM | Interaction mode |
| TT-3 | Rate your team's current cognitive load — the number of distinct systems, tools, and responsibilities you must track day-to-day. *(5-point Likert, low to overloaded)* | Likert-5 | GAP-FILL | Cognitive load |
| TT-4 | Is there a recurring forum (platform review board, architecture guild, AI governance committee) where infra/AI-tooling decisions are discussed and documented? *(Yes, regular and well-attended / Exists but inconsistent / No such forum)* | MC | CONFIRM | Culture/process ritual maturity |
| TT-5 | [Open] What responsibility does your team carry today that would ideally belong to a platform or enabling team instead? | Open | GAP-FILL | Team-boundary misallocation signal |

**Scoring guidance:** Flag any team whose self-reported type (TT-1) doesn't match what repo-ownership/ticket-routing data would suggest — that mismatch is itself one of the highest-value outputs of this questionnaire, since it usually indicates an org-chart team boundary that no longer matches actual working reality.

---

## Deployment Notes (applies to all ten)

- **Targeting:** Same as the main report — distribute separately to platform engineers, product/feature engineering (the platform's "customers"), and leadership; compare response patterns across groups as a maturity signal in its own right.
- **Routing open-ended answers:** Analyze open text only inside the approved survey boundary, redact identifiers before any external model use, and tag minimized findings against the relevant model target with a confidence rating. Never store raw verbatim text or PII in the shared state or final report.
- **Versioning:** Because several of these methodologies are still evolving rapidly (DORA AI Capabilities, CSA MCP Security), review and re-issue each questionnaire whenever its source framework publishes an update, not just on a fixed calendar.
