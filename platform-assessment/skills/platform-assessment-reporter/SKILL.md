---
name: platform-assessment-reporter
description: Turn platform and agentic-readiness assessment results into evidence-backed reporting visuals for executive and stakeholder review. Use whenever someone wants to visualize assessment results, build an exec-ready report or readout deck, place an org on a maturity or production-system quadrant, chart platform value dimensions on a radar/spider diagram, show before/after platform impact, or render golden-path coverage. Fires on phrasing like "build the report", "visualize the assessment", "exec readout", "maturity chart", "radar chart of our platform", "where do we sit on the quadrant", "make this presentable to leadership". Every rendered score must trace to a named metric with a source and confidence tier; anything not measurable is explicitly marked as qualitative — this skill never lets a fuzzy judgment render as a hard number.
---

# Platform Assessment Reporter

## Purpose

Render the outputs of platform assessments — maturity scores, ROI evidence, org diagnostics — as reporting visuals a leadership audience can act on: a production-system quadrant placement, a six-vector value radar, golden-path coverage maps, and before/after ledgers.

The skill's one non-negotiable rule: **visuals inherit the evidence discipline of the data behind them.** Every plotted point carries a metric, a source, a date, and a confidence tier. Where no measurable metric exists, the point is rendered and labeled as qualitative — visibly distinct from measured data. A chart that hides fuzziness is a lie with better production values.

Sibling skills feed this one: `asdlc-maturity-assessment` (level scores, path matrix), `platform-roi-scorecard` (cost/value numbers, benchmark calibration), `platform-org-design-advisor` (structure diagnostics). Assess first, then report. Client context: [YOUR ORGANIZATION / CLIENT].

## Core model

### 1. Evidence tiers — the confidence vocabulary

Every data point rendered anywhere gets exactly one tier:

| Tier | Definition | Visual encoding |
|---|---|---|
| **Measured** | System data pulled from tooling (VCS, CI/CD, tracker, cloud APIs) with a stated query and date | Solid fill, full opacity |
| **Surveyed** | Structured survey of doers (not executives), with n and date stated | Solid fill, lighter shade, "n=X, survey MM/YYYY" footnote |
| **Estimated** | Derived arithmetic (e.g., hours-saved × rate) with stated assumptions | Outlined fill, assumptions footnoted |
| **Qualitative (fuzzy)** | Judgment, anecdote, or inherently unmeasurable dimension | Hatched/dashed rendering + explicit "qualitative" label on the axis or point |

Encoding rules: never render a Qualitative or Estimated point with the same visual weight as a Measured one. Never average tiers into a composite score without stating the mix (e.g., "composite of 4 measured, 2 qualitative axes"). Every chart ships with an evidence appendix table: axis → metric → source → date → tier.

### 2. Production-system quadrant

A 2×2 diagnostic of how an organization produces software:

- **X axis — ownership:** fragmented ↔ concentrated (end-to-end)
- **Y axis — design:** implicit (tribal, negotiated) ↔ explicit (deliberate, documented)

| Quadrant | Traits | Failure mode |
|---|---|---|
| **Artisanal** (implicit + fragmented) | Informal coordination, diffuse responsibility, negotiation-driven | High variance in execution |
| **Hero-based** (implicit + concentrated) | Expertise islands, high individual ownership | Fragile scalability; bus-factor risk |
| **Bureaucratic** (explicit + fragmented) | Prescribed process, strong controls, weak accountability | Stable but slow; optimizes compliance over flow; decays quietly under pressure |
| **Platform** (explicit + concentrated) | Deliberate design, explicit interfaces, end-to-end ownership, continuous improvement | Target quadrant |

Most organizations oscillate among the three non-platform quadrants rather than sitting still. Placement is a diagnosis of the production system, not the people: organizations rarely fail from incompetence — the production system makes competence fragile.

**Evidence-backed placement rubric.** Score each axis 0–4 from at least two evidence points; below two, the placement is Qualitative and must be rendered as such.

*Design explicitness (Y):*
- % of delivery workflows with a written path definition or definition of done (Measured — repo/wiki audit)
- Policy-as-code coverage: % of policy checks enforced in pipeline vs. in review comments (Measured — CI config audit)
- Pipeline definitions version-controlled vs. UI-defined (Measured)
- Onboarding time to first meaningful PR (Measured — tracker/VCS)

*Ownership concentration (X):*
- CODEOWNERS / service-catalog coverage: % of repos/services with a named owning team (Measured)
- Bus factor on critical components: contributors covering 80% of commits (Measured — VCS)
- On-call rotation breadth vs. single-hero pattern (Measured — paging tool)
- % of incidents resolved by the owning team without escalation (Measured/Surveyed)

Caution: concentrated ownership scores high on X only when ownership is *team-level and end-to-end*. A bus factor of 1 is Hero-based concentration, not Platform concentration — check breadth before placing high-right.

### 3. Six-vector value radar

Radar/spider chart comparing the org (and optionally: target state, industry benchmark, before/after) across six value dimensions. Each axis scored 0–4, each with a defined metric set and an honest tier ceiling:

| Vector | Metric set | Best achievable tier |
|---|---|---|
| **Delivery velocity** | Deployment frequency, lead time for changes | Measured |
| **Outcome predictability** | Change failure rate; forecast-vs-actual delivery variance | Measured |
| **Operational resiliency** | MTTR, error-budget adherence, incident recurrence | Measured |
| **Maintenance efficiency** | KTLO share of engineering time, rework/revert rate, dependency currency (N-1 version %) | Measured/Surveyed (KTLO share usually survey or time-tracking) |
| **Organizational learning** | Postmortem completion + action closure rate, onboarding time trend, internal-docs contribution rate | Surveyed/Estimated — partially measurable proxies; the construct itself is soft. Flag axis as mixed-tier. |
| **Structural incentive** | Whether the system rewards platform use vs. bypass: golden-path adoption %, voluntary vs. mandated usage split | Qualitative with measurable fragments — default to Qualitative unless adoption telemetry exists |

Rendering rules: axes at different tiers get different stroke treatments (solid for Measured, dashed for Qualitative) and the legend says so. If comparing to an industry benchmark, state the survey year — benchmarks age. Do not plot a "target state" polygon as if it were data; label it target.

### 4. Golden-path coverage map

Per-path structural diagram for reporting platform completeness. Each golden path renders as a column: **Interface** (how it's invoked) → **Capability** (tools & resources; lifecycle & guardrails; abstraction promise — what detail the path commits to hiding) → **Output**, with shared **Identity** entering above and shared **Policies/State** below, and a continuous-improvement loop from outcomes back into the platform.

Report per path: definition exists (Y/N), invocation telemetry (Measured adoption %), validation/guardrail coverage, and output feedback wiring. Paths with no telemetry render hatched — "defined but unobserved."

### 5. Before/after ledger

Two-column table for any claimed improvement: metric, before (value + date), after (value + date), delta, tier, source. A before/after claim without a baseline date is an anecdote — render it in the Qualitative style or cut it.

### 6. Adoption trajectory panel

For roll-out reporting: S-curve expectation (slow MVP → ramp → saturation), plotted actual (users, voluntary usage share, services migrated — Measured), annotated interventions. Flag the known failure pattern: early demand tempting the team to abandon structured onboarding, after which learning stalls and the platform team decays into reactive support. Rhythm metric: onboarding-loop runs per quarter and cohort size — measurable and honest.

## Workflow

1. **Intake.** Collect assessment outputs from sibling skills (maturity level + path matrix, ROI scorecard, org diagnostic). Identify audience ([EXEC / PLATFORM TEAM / BOARD]) and decision the report should enable.
2. **Build the evidence table first.** Before any chart: list every candidate data point as axis/claim → metric → source → date → tier. Data with no source gets Qualitative or gets cut. This table becomes the report appendix.
3. **Select visuals.** Quadrant for "where are we" framing; radar for multi-dimensional state (and before/after or benchmark overlay); path coverage map for platform completeness; ledger for ROI claims; trajectory panel for adoption. Skip any visual whose axes would be majority-Qualitative — replace with a findings list instead of faking precision.
4. **Score axes** per the rubrics above. Two-evidence-point minimum per quadrant axis; tier ceilings respected per radar vector.
5. **Render** with tier encodings (solid/lighter/outlined/hatched), axis footnotes, survey years, and an explicit legend entry for qualitative marks. Formats: Mermaid (quadrantChart for the 2×2; flowchart for path maps), SVG/HTML for radars, markdown tables for ledgers — match the medium the audience will actually view.
6. **Fuzziness callout pass.** Re-scan every visual: any point that reads as measured but isn't? Fix encoding or add the label. Add a one-line "what we could not measure and why" note per chart — absence of measurement is itself a finding (it usually indicates missing attribution or telemetry, which routes back to `asdlc-maturity-assessment`).
7. **Deliver** with the evidence appendix and a reproduction note (queries/sources used, so next quarter's report is comparable).

## Guardrails

- Never render a qualitative judgment in the same visual style as measured data — no exceptions for aesthetics.
- Never composite mixed-tier axes into a single score without disclosing the mix.
- No quadrant placement from fewer than two evidence points per axis — render as Qualitative hypothesis instead.
- Benchmarks and surveys always carry their year and n. Vendor-published numbers are Qualitative regardless of how precise they look.
- Illustrative/hypothetical comparison polygons (target state, idealized platform) must be labeled as such — never presented as observed data.
- A missing baseline kills a before/after claim; report the after-value as a snapshot, not an improvement.
- Report what could not be measured. An all-solid chart of a low-maturity org is a red flag, not an achievement.

## Suggested effort

- **Quick readout** (existing assessment data, 1–2 visuals): low — evidence table + radar or quadrant.
- **Full report** (all five visual types + appendix): medium — requires complete sibling-skill outputs.
- **Recurring reporting program** (quarterly comparable series): high first cycle (reproduction notes, query library), low thereafter.
