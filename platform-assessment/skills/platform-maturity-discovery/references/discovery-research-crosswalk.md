# Discovery Research Crosswalk

Use this reference when designing the evidence plan, scanner architecture, survey, or framework reconciliation for a platform-engineering and Agentic Developer Portal discovery.

## Contents

1. Source stance
2. Framework roles
3. Evidence pipeline
4. Signal families
5. Reconciliation rules
6. Survey design
7. Source register

## Source stance

Treat the user-provided *IDP/ADP Maturity Assessment Research: Discovering and Scoring Platform Engineering and Agentic AI Maturity* as a research input and question catalog. Do not copy its proposed unified Level 0-4 score. It conflates platform engineering, agentic delivery, and Agentic Developer Portal readiness, and it uses “IDP” and “ADP” ambiguously.

Keep the suite's three outputs separate:

1. CNCF-aligned platform-engineering maturity;
2. ASDLC path maturity;
3. use-case-specific Agentic Developer Portal readiness gates.

Use **Agentic Developer Portal** for ADP. Write Internal Developer Portal and Internal Developer Platform in full. Treat a human-facing Internal Developer Portal as one interface within the broader Agentic Developer Portal experience, backed by Internal Developer Platform capabilities.

## Framework roles

Use each framework only for the role it can support:

| Framework | Use in discovery | Do not use it for |
|---|---|---|
| CNCF Platform Engineering Maturity Model | Platform aspect questions and source-versioned scoring through `platform-maturity-benchmark` | A combined ADP or ASDLC score |
| Microsoft Platform Engineering Capability Model | Coverage check for investment, adoption, governance, provisioning and management, interfaces, measurement and feedback | Replacing the CNCF scorer or assuming every organization targets the final stage |
| DORA AI Capabilities Model | Human-sensing prompts about AI stance, data accessibility, AI-accessible context, version control, small batches, user focus, and platform quality | An autonomous-agent security or ADP readiness score |
| SPACE | Multi-dimensional developer-experience and outcome measurement | Individual productivity ranking or a fixed maturity level |
| Security maturity guidance | Candidate controls and questions for specialist security review | Silent import of draft thresholds into a production scorer |

Use platform quality as a prerequisite and amplifier for agentic delivery, not as proof that agentic delivery or the ADP is mature.

## Evidence pipeline

Run a privacy-gated pipeline:

1. Charter the purpose, scope, authority, population, fields, retention, and decisions supported.
2. Collect through least-privilege, read-only connectors.
3. Separate static scans from runtime/API observations.
4. Compute deterministic cross-references before using an LLM.
5. Redact direct identifiers inside the approved boundary.
6. Extract qualitative evidence into a constrained schema.
7. Map evidence to questions, aspects, paths, and gates.
8. Reconcile behavioral, derived, and attested evidence.
9. Run the two formal scorers and the seven ADP gates separately.
10. Publish confidence, blind spots, and contradictions, then delete raw data on schedule.

Require every extracted evidence record to include:

- source system and stable artifact/event reference;
- observation window and population;
- evidence class and collection method;
- question, maturity aspect/path/gate, and direction of evidence;
- redacted supporting summary rather than raw private content;
- confidence, corroboration status, and retention date.

Do not let an LLM assign authoritative scores directly from raw messages or transcripts. Use it to produce reviewable candidate evidence; apply scoring only after provenance and corroboration checks.

## Signal families

### Static repository and configuration

Inspect presence, coverage, completeness, freshness, and consistency for:

- CI/CD definitions and required validation stages;
- IaC, deployment manifests, and policy-as-code;
- service ownership, tier, runbook, on-call, SLO, and dependency metadata;
- golden-path templates and template provenance;
- agent instructions, prompts, skills, and tool configurations;
- branch, review, attribution, and release controls.

File presence is only a lead. Test whether the artifact is substantive, current, used, and connected to runtime behavior.

### Runtime and API evidence

Measure actual use and control posture through:

- pull requests, reviews, pipelines, deployments, rollbacks, and policy outcomes;
- live cloud and Kubernetes inventory matched to authoritative IaC/state;
- catalog queries, template instantiations, self-service executions, and support escalations;
- approved agent identities, sessions, tool calls, exceptions, evaluations, and audit trails;
- work-item transitions, approval hops, blocked reasons, rework, and incident actions.

Keep **unmatched live resources** distinct from **configuration drift**: the first lacks an authoritative code/state match; the second differs from its declared state.

### Human and organizational evidence

Use authorized, aggregated evidence to learn what telemetry cannot show:

- why teams adopt or bypass supported paths;
- whether automation and metrics are trusted;
- whether the AI stance and allowed tools are clear;
- whether internal knowledge is accessible and useful to humans and agents;
- whether platform demand exceeds the team's delivery capacity;
- whether decisions, incidents, and exceptions have durable records;
- whether teams can challenge unsafe or ineffective automation.

Never infer these conditions from message volume, attendance, tone, or one isolated statement.

## Reconciliation rules

Classify each material finding:

- **Confirmed** — independent behavioral and human/secondary evidence agree.
- **Contradicted** — declared/static evidence conflicts with runtime use or practitioner experience. Treat this as a first-class “maturity theater” finding.
- **Gap-filled** — human evidence answers a question that static/runtime evidence cannot observe. Keep confidence below a corroborated structural fact.
- **Unresolved** — evidence is insufficient or the visibility boundary is too narrow. Leave the score or gate unassigned where necessary.

Favor objective evidence for structural questions such as IaC coverage, authentication, or branch enforcement. Favor properly sampled human evidence for trust, intent, perceived friction, and adoption motivation. Never use one fixed weighting formula across both kinds of question.

## Survey design

Tag every question:

- **CONFIRM** — validate or challenge a signal already observed in systems of record.
- **GAP-FILL** — collect intent, trust, political context, demand, or another condition automation cannot see reliably.

Keep a stable observation window, normally 90 days, and ask the same core items of separate cohorts:

- platform/infrastructure staff;
- product or stream-aligned teams, including supported-path bypassers;
- security and operations;
- engineering leadership.

Compare cohort distributions instead of averaging them into one sentiment score. Publish response counts, nonresponse, suppression thresholds, and wording changes.

Cover six prompt families without copying a vendor survey verbatim:

1. infrastructure and cloud control;
2. measurement quality and metric trust;
3. catalog, golden-path, and self-service experience;
4. AI stance, agent governance, identity, and tool inventory;
5. reusable agent context, skills, and tool discovery;
6. platform product culture, cognitive load, user focus, and organizational obstacles.

Do not ask for individual output counts or use responses for performance management. Keep survey-based claims attested unless independently corroborated.

## Source register

Verify versions and status at engagement time:

- CNCF Platform Engineering Maturity Model: `https://tag-app-delivery.cncf.io/wgs/platforms/maturity-model/readme/`
- Microsoft Platform Engineering Capability Model: `https://learn.microsoft.com/en-us/platform-engineering/platform-engineering-capability-model`
- DORA 2025 State of AI-assisted Software Development: `https://dora.dev/research/2025/dora-report/`
- DORA AI Capabilities Model and survey questions: `https://dora.dev/ai/capabilities-model/report/` and `https://dora.dev/ai/capabilities-model/questions/`
- Cloud Security Alliance Agentic MCP Security Best Practices Guide: `https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/`

As of July 2026, the CSA page labels its guide **draft**. Route protocol and security thresholds to the specialist security skills and re-verify the current MCP specification and control source before using them. Treat vendor scorecards, product features, connector availability, legal claims, and industry percentages as volatile until checked against current primary sources.
