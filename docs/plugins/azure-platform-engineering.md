# `azure-platform-engineering`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Azure implementation arm of the platform suite: read-only estate assessment (Resource Graph, azqr, Governance Visualizer, aztfexport) feeding assessment increment I9, platform/landing-zone topology design on Radius and Azure Verified Modules, durable agentic operations on Dapr Workflow, four-layer IaC guardrail verification, workload onboarding by disposition, and the golden-path-as-an-API contract behind APIM with a platform MCP server on the roadmap.

- Version: `0.1.0`
- Category: `platform`
- Skills: 8
- Claude plugin: yes
- Codex plugin manifest: no; install the portable skills directly
- Perplexity packages: not currently packaged

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`agentic-ops-builder`](../../azure-platform-engineering/skills/agentic-ops-builder/SKILL.md) | Build durable agentic operations for an Azure platform on Dapr Workflow: human-in-the-loop provisioning approvals that survive days-long pauses, monitor-pattern health checks, saga/compensation for multi-step… | — |
| [`azure-estate-assessor`](../../azure-platform-engineering/skills/azure-estate-assessor/SKILL.md) | Assess an existing Azure estate with open-source tooling and produce a disposition map for platform onboarding: Azure Resource Graph inventory, azqr best-practice findings, Azure Governance Visualizer policy/RBAC map,… | — |
| [`azure-platform-designer`](../../azure-platform-engineering/skills/azure-platform-designer/SKILL.md) | Recommend how many platforms to build and design their Azure topology: platform-count heuristic (thinnest viable platform, cognitive load, CAF platform teams), Radius environment ladder (simple / application-centric /… | — |
| [`golden-path-api-designer`](../../azure-platform-engineering/skills/golden-path-api-designer/SKILL.md) | Design the golden-path-as-a-service API: the contract-first platform API behind APIM (Azure Front Door later for global/WAF) whose endpoints perform golden-path operations (create service, provision datastore, promote… | — |
| [`iac-guardrail-verifier`](../../azure-platform-engineering/skills/iac-guardrail-verifier/SKILL.md) | Adversarially verify agent- or human-generated Azure IaC against the four-layer enforcement model: generation-time constitution rules (AVM-first, naming, tagging, data-classification networking), plan-time static… | — |
| [`platform-constitution`](../../azure-platform-engineering/skills/platform-constitution/SKILL.md) | Author or amend a platform constitution — the versioned, org-wide constraint document (allowed regions, compliance regimes, naming and tagging standards, approved stacks, IaC rules, agent authority boundaries) that… | — |
| [`radius-golden-path-builder`](../../azure-platform-engineering/skills/radius-golden-path-builder/SKILL.md) | Build Azure golden paths on Radius + Dapr + Azure Verified Modules from the azure-agentic-idp reference templates: custom Resource Types, per-environment Bicep Recipes (dev k8s / Azure Container Apps / AKS compute;… | — |
| [`workload-onboarder`](../../azure-platform-engineering/skills/workload-onboarder/SKILL.md) | Execute a disposition map: onboard existing Azure workloads onto the platform per their assessed disposition — Recipe-wrap (absorb existing Terraform/Bicep unchanged behind a Radius Recipe), Refactor (regenerate on the… | — |

## Plugin files

- [Usage guide](../../azure-platform-engineering/GUIDE.md)
- [Claude manifest](../../azure-platform-engineering/.claude-plugin/plugin.json)
- Codex: install individual skill directories through an Agent Skills-compatible installer.
- [Skill source directory](../../azure-platform-engineering/skills/)
