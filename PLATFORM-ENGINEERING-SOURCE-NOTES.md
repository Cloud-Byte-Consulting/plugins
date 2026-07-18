# Platform Engineering Source Notes

## Research inputs

The July 2025 book *Mastering Enterprise Platform Engineering: A Practical Guide to Platform Engineering and Generative AI for High-Performance Software Delivery* by Mark Peters and Gautham Pallapa (Packt Publishing, ISBN 978-1-83588-048-7) was used as a research input for the platform-engineering content refresh.

The source is copyrighted and marked “All rights reserved.” The book and its text are not included in this repository. Repository changes are original synthesis: no chapter, table, figure, case study, or substantial passage has been reproduced.

The user-provided July 2026 Markdown report *IDP/ADP Maturity Assessment Research: Discovering and Scoring Platform Engineering and Agentic AI Maturity* was also reviewed. It has no explicit redistribution license, so the report itself and its long-form text are not included. Framework claims selected for synthesis were checked against primary CNCF, Microsoft, DORA, and Cloud Security Alliance pages.

## Concepts synthesized into the skills

- platform capabilities operated as products and services rather than one-time projects;
- explicit reuse, buy, assemble, or build decisions with lifecycle cost and exit planning;
- internal service contracts connecting indicators, objectives, support, compatibility, and change policy;
- developer experience connected through delivery and operational outcomes to business value;
- team sponsorship, product management, psychological safety, autonomy, and continuous learning;
- living roadmaps with measurable checkpoints, feedback, and adjustment;
- metrics that drive decisions, expose trade-offs, resist gaming, and are retired when no longer useful.

These concepts were integrated into existing Cloud Byte frameworks rather than added as a book summary. Tool examples, benchmark figures, legal claims, and vendor case-study results from the book were deliberately not imported.

The book recommends practitioner interviews, standardized group sensing sessions, developer surveys, usage analytics, ticket-flow timing, operational metrics, and continuous feedback. It does not define an Agentic Developer Portal or a cross-system organizational discovery model. The repository's `platform-maturity-discovery` skill extends those research methods across communications, meetings, work items, code, infrastructure, telemetry, and sentiment, with explicit privacy boundaries.

The Markdown research added useful discovery mechanics: separate static scans from runtime/API observations and computed cross-references; distinguish unmatched live resources from configuration drift; reconcile findings as confirmed, contradicted, or gap-filled; design survey questions as CONFIRM or GAP-FILL; compare platform staff, platform users, security/operations, and leadership as separate cohorts; and validate agent instructions and tool inventories for coverage, completeness, freshness, and observed use rather than file presence.

The report's proposed unified Level 0–4 platform-and-agent maturity score was deliberately not adopted. It conflicts with this repository's three-part model, which reports CNCF-aligned platform maturity, ASDLC path maturity, and Agentic Developer Portal readiness gates separately. Vendor scorecards, product comparisons, numeric cutoffs, volatile industry statistics, legal conclusions, and draft security thresholds were not imported.

Terminology in this repository distinguishes the human-facing **Internal Developer Portal**, the backend **Internal Developer Platform**, and the broader **Agentic Developer Portal (ADP)** that supports both human and agent users.

## Updated skill scope

- `platform-assessment`: organizational discovery, architecture, organization design, and ROI/value mapping.
- `adp-enablement`: maturity cross-checks, golden-path service lifecycle, and fitness-function/service-level governance.

The security, agent identity, MCP API, agent API contract, and ASDLC scoring models retain their specialist boundaries because the source did not add a more specific control model for those scopes.
