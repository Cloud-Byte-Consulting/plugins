# `adp-enablement`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Engineer the Agentic Developer Portal: CNCF platform-maturity benchmark with industry percentiles, MCP servers over platform APIs, agent identity (no standing secrets, ephemeral credentials), agent-consumable API contracts, golden paths as products, and fitness-function instrumentation for the maturity roadmap.

- Version: `1.1.0`
- Category: `platform`
- Skills: 6
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 6

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`agent-api-contract-designer`](../../adp-enablement/skills/agent-api-contract-designer/SKILL.md) | Design secure, contract-first platform APIs for AI agents and machine consumers using OpenAPI, tolerant versioning, consumer-driven tests, recoverable errors, BFF boundaries, and STRIDE-based threat modeling. | [ZIP](../../adp-enablement/perplexity/agent-api-contract-designer.zip) |
| [`agent-identity-engineer`](../../adp-enablement/skills/agent-identity-engineer/SKILL.md) | Engineer identity, credentials, and authorization for AI-agent principals on Kubernetes and cloud platforms using workload identity, projected tokens, OIDC, SPIFFE/SPIRE, OAuth2 client credentials, and short-lived… | [ZIP](../../adp-enablement/perplexity/agent-identity-engineer.zip) |
| [`golden-path-designer`](../../adp-enablement/skills/golden-path-designer/SKILL.md) | Design golden paths as versioned products for human and AI-agent users, using maturity levels, Thinnest Viable Platform scoping, Backstage templates, Crossplane abstractions, CI gates, and adoption metrics. | [ZIP](../../adp-enablement/perplexity/golden-path-designer.zip) |
| [`mcp-platform-api-author`](../../adp-enablement/skills/mcp-platform-api-author/SKILL.md) | Design secure MCP servers that expose governed platform capabilities to AI agents through scoped, testable tools. | [ZIP](../../adp-enablement/perplexity/mcp-platform-api-author.zip) |
| [`platform-fitness-functions`](../../adp-enablement/skills/platform-fitness-functions/SKILL.md) | Instrument a platform roadmap with executable architectural fitness functions and metrics using CI tests, staged warning-to-error thresholds, DORA signals, GQM workshops, and transparent maturity indexes. | [ZIP](../../adp-enablement/perplexity/platform-fitness-functions.zip) |
| [`platform-maturity-benchmark`](../../adp-enablement/skills/platform-maturity-benchmark/SKILL.md) | Score platform-engineering maturity on the CNCF four-stage, five-aspect model and compare it with a source-versioned industry distribution before producing a gap register. | [ZIP](../../adp-enablement/perplexity/platform-maturity-benchmark.zip) |

## Plugin files

- [Claude manifest](../../adp-enablement/.claude-plugin/plugin.json)
- [Codex manifest](../../adp-enablement/.codex-plugin/plugin.json)
- [Skill source directory](../../adp-enablement/skills/)
