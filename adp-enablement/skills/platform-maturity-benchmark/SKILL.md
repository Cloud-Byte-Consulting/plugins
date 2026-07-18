---
name: platform-maturity-benchmark
description: >-
  Score an organization's platform-engineering maturity on the CNCF Platform
  Engineering Maturity Model (4 stages x 5 aspects) and position every score
  against industry distribution percentages, then layer secondary axes (DOMM,
  Golden Path maturity, Cloud Native maturity) and produce a
  percentile-positioned gap register that feeds a platform roadmap. Use
  whenever the user asks for a platform maturity assessment, CNCF maturity
  model scoring, platform engineering benchmark, industry percentile
  comparison, "how mature is our platform", "how do we compare to other
  platform teams", DevOps maturity (DOMM) rating, cloud native maturity level,
  whether their org is ready for an IDP, or wants survey-calibrated evidence
  that their platform investment, adoption, interfaces, operations, or
  measurement are ahead of or behind the market. Disambiguation - the sibling
  platform-assessment plugin's asdlc-maturity-assessment skill scores
  AGENT-ADOPTION maturity (8-path x 5-level ASDLC rubric); this skill
  benchmarks PLATFORM-ENGINEERING maturity against the CNCF model and industry
  data. Run both for a full ADP engagement.
---

# Platform Maturity Benchmark

## Purpose
Turn "how good is our platform?" into a scored, percentile-positioned diagnosis. Score the organization on the CNCF Platform Engineering Maturity Model's 4×5 grid, place each score against the industry distribution (so "we're at Operational" becomes "we're with the 43% majority, and one stage from the top 12%"), cross-check with three secondary maturity axes, and emit a gap register the roadmap can consume. This is the platform-side twin of the sibling `asdlc-maturity-assessment` skill (platform-assessment plugin), which scores agent adoption; an Agentic Developer Portal engagement needs both readings, because agents amplify whatever platform maturity exists.

## Core model to hold in your head

### The CNCF 4×5 grid with industry distribution (the benchmark table)
Four stages — **Provisional → Operational → Scalable → Optimizing** — evaluated across five aspects. The percentages are the industry distribution from the State of Platform Engineering survey (281 platform professionals; respondents without a platform team filtered out). Score each aspect independently; orgs are almost never at one stage across the board.

| Aspect (question it answers) | Provisional | Operational | Scalable | Optimizing |
|---|---|---|---|---|
| **Investment** — how are staff & funds allocated? | Voluntary/temporary assignments — **8.8%** | Dedicated team, primarily reactive — **43.3%** | Platform as product, data-driven investment — **35.7%** | Enabled ecosystem, cross-functional — **12.2%** |
| **Adoption** — why do users discover & use it? | Erratic, no coherent strategy — **18.5%** | Extrinsic push, often mandated — **35.8%** | Intrinsic pull, genuine value — **28.4%** | Participatory, users contribute back — **17.3%** |
| **Interfaces** — how do users consume capabilities? | Custom processes, manual & inconsistent — **14.5%** | Standard tooling, some consistency — **42.2%** | Self-service solutions, high autonomy — **34.3%** | Integrated services embedded in existing tools — **9.1%** |
| **Operations** — how are capabilities planned & maintained? | By request, ad hoc — **21.3%** | Centrally tracked — **28.7%** | Centrally enabled, user-need focus — **38.9%** | Managed services, proactive & integrated — **10.7%** |
| **Measurement** — how is feedback gathered & used? | Ad hoc and inconsistent — **42.5%** | Consistent collection, limited analysis — **26.3%** | Insights-driven, some quant+qual — **20.8%** | Quant + qual fully integrated into decisions — **10.4%** |

Percentile mechanics: an org's position on an aspect = the cumulative share of orgs at lower stages. Example: scoring **Scalable on Interfaces** puts the org ahead of 56.7% of the market (14.5 + 42.2) with 9.1% still above it. Report every aspect this way — "score + who's behind you + who's ahead" — because the distribution is the deliverable's persuasive core. A worked readout for a typical mid-maturity client:

| Aspect | Scored | Behind them | Ahead of them | Reading |
|---|---|---|---|---|
| Investment | Operational | 8.8% | 47.9% | With the 43% majority; product-thinking is the next jump |
| Adoption | Operational | 18.5% | 45.7% | Mandated usage — intrinsic pull not yet earned |
| Interfaces | Scalable | 56.7% | 9.1% | A genuine strength; one stage from top-decile |
| Operations | Scalable | 50.0% | 10.7% | With the 38.9% plurality |
| Measurement | Provisional | 0% | 57.5% | The anchor dragging every other claim down |

Calibration anchors from the same survey (quote these to keep scores honest):
- **44.67% of organizations measure nothing at all**; 37.3% use DORA; 11.5% measure time-to-market. A claimed Scalable/Optimizing Measurement score should stand out against a market where near-half measure zero.
- Only 22.1% report significant metric improvements since introducing platform engineering; 26.6% don't know whether anything improved.
- Self-reported maturity runs ahead of reality — the survey itself flags the contradiction between high Operations self-scores (user-need focused) and dismal Measurement scores (not measuring users). If Measurement lands two stages below Operations, distrust the Operations self-report.
- Most platform initiatives are young: new teams dominate the survey population, so an org two years into a platform investment should expect to be — and can credibly claim to be — ahead of the median on at least one aspect.
- Aspect scores travel together loosely, not rigidly: a lone Optimizing score amid Provisional/Operational neighbors is more likely a scoring error than a genuine spike; re-examine the evidence.

### Structural diagnostics (score-independent red flags)
- **The portal trap.** Building the platform from the frontend — shoehorning business logic into a portal (Backstage or otherwise) to get a quick executive win. Portals are interfaces on top of the platform, not the platform; portal-first is "starting to build a house by the windows." A portal-first estate caps Interfaces at Operational no matter how polished the UI, and creates debt when the real backend arrives.
- **3-tier platform architecture** as the structural reading. Record which tiers actually exist:
  - **Application Choreography** — "code, ship, run": portals, CLIs, declarative config (Score, KubeVela).
  - **Platform Orchestration** — "design, enable, optimize": the platform API and orchestrator (Kratix Promises, Humanitec resource definitions, Argo/Flux CRDs).
  - **Infrastructure Orchestration** — "plan, build, maintain": IaC (Terraform, Crossplane managed resources).
  - A missing middle tier under a rich top tier is the portal trap in architectural form.
- **Pipeline vs. graph backend.** Pipeline-based backends (CI/CD + IaC) scale linearly with complexity and degrade into nested pipelines. Graph-based backends (Platform Orchestrators) are API-first, carry RBAC/SSO and secrets injection, and manage environment progression across handover points **whether the stakeholder is human or machine** — exactly the property an ADP needs, since agents are machine stakeholders at every handover. Rule of thumb: below ~100 developers a graph backend is probably overkill; above it, a pipeline-only backend is a Scalable-stage blocker. (Architecture design itself belongs to the sibling `idp-adp-architect` skill, platform-assessment plugin.)

### Secondary axes (triangulate, don't replace)
Layer these to catch cases where the CNCF grid under- or over-reads the org:

1. **DOMM (DevOps Maturity Model), 5 levels:** Initial (little/no automation or dev-ops collaboration) → Managed (some automation, basic processes) → Defined (standardized processes, strong automation focus) → Measured (integrated, continuously monitored and optimized) → Optimized (continuous learning and improvement). Maps roughly: Provisional≈1–2, Operational≈2–3, Scalable≈3–4, Optimizing≈5. A DOMM reading two levels off the CNCF reading means the evidence is inconsistent — dig.
2. **Golden Path maturity, 3 levels:** No golden path (teams own their DevOps) → Clone-and-forget (central templates, cloned then divergent) → Golden paths as products (integrated, versioned, upgradable). The sharpest single probe for the Interfaces aspect; hand remediation to the sibling `golden-path-designer` skill.
3. **Cloud Native maturity, 5 levels:** Build (containerize, basic orchestration, pre-prod) → Operate (production-ready, RBAC, monitoring, secrets) → Scale (standardization, cost optimization, extended automation) → Improve (security/policy/governance, policy-as-code like OPA) → Adapt (continuous optimization, feedback loops). **Gate: IDPs typically start becoming effective at the Scale stage.** An org at Build/Operate asking for an IDP — let alone an ADP — gets a foundations-first roadmap, not a platform buildout.

### From scores to gap register
Each aspect gap becomes a register entry: aspect, current stage, current percentile, target stage (usually +1; never +2 in one roadmap horizon), the blocking evidence, and the owning enablement skill:
- Interfaces / Adoption gaps → `golden-path-designer`.
- Measurement gaps → `platform-fitness-functions` (and sequence these FIRST — you cannot demonstrate any other gap closed without instrumentation, and the 44.67%-measure-nothing market makes it the cheapest differentiation available).
- Agent-facing Interfaces gaps → `mcp-platform-api-author` + `agent-api-contract-designer`.
- Identity prerequisites → `agent-identity-engineer`.
- Backend architecture gaps → `idp-adp-architect` (platform-assessment plugin).

## Workflow
1. **Interview per aspect.** For [YOUR ORGANIZATION / CLIENT], walk the five aspect questions and collect evidence, not aspiration: budget lines and team charters (Investment), adoption telemetry and mandate policies (Adoption), how the last five infra requests were actually fulfilled (Interfaces), the platform team's backlog source (Operations), what metrics exist and who reads them (Measurement). Prefer artifacts over self-report — for a managed-K8s research context: namespace request tickets, GPU quota processes, cluster onboarding docs.
2. **Score the 4×5 grid.** One stage per aspect, one line of evidence per score. Where evidence conflicts, score low and note the conflict.
3. **Position against industry.** Compute cumulative percentile per aspect from the benchmark table; render the five-row table with the org's cell highlighted and behind/ahead percentages.
4. **Run structural diagnostics.** Portal-trap check, 3-tier mapping, pipeline-vs-graph backend reading against developer headcount.
5. **Triangulate with secondary axes.** DOMM level, Golden Path level, Cloud Native level. Apply the "IDP effective at Scale" gate explicitly and say so if the org fails it.
6. **Apply the self-report discount.** Compare the Measurement score against all other aspects; flag any aspect scored 2+ stages above Measurement as unverified.
7. **Emit the gap register.** Table: aspect | current stage | percentile | target | blocking evidence | owning skill | sequence. Measurement first; then the aspect where one stage of movement crosses the biggest percentile mass (e.g., Operational→Scalable on Investment moves past 43% of the market).
8. **Output.** A benchmark report: the highlighted 4×5 table, per-aspect percentile narrative, secondary-axis triangulation, structural red flags, the gap register, and an explicit statement of whether the org clears the IDP-at-Scale gate and (with the ASDLC reading from `asdlc-maturity-assessment`) is fit to start ADP enablement.

## Guardrails
- Score aspects independently — never average into a single "maturity number" (a numeric index, if wanted, is `platform-fitness-functions`' MMI-style construction, built transparently).
- Never accept a self-reported stage the Measurement score can't support; the survey's own finding is that orgs "have a much better image of themselves than the reality."
- Quote the exact industry percentages; the credibility of the benchmark is the survey data, not the consultant's judgment.
- Optimizing is rare by construction (9–17% per aspect) — demand exceptional evidence before awarding it.
- Don't recommend ADP enablement work to an org below Cloud Native Scale or with a No-golden-path reading; foundations first.
- This skill benchmarks; it does not design. Architecture → `idp-adp-architect`; agent-adoption scoring → `asdlc-maturity-assessment` (both in the platform-assessment plugin).

## Suggested effort
Medium-high — structured interview, scored grid, percentile analysis, and a gap register that other skills consume.
