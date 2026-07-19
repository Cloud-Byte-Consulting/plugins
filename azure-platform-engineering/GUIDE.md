# Azure Platform Engineering Guide

Use this guide to assess an Azure estate, design the target platform, and move
workloads onto governed Radius and Dapr golden paths. The plugin is the Azure
implementation arm of the broader assessment and Agentic Developer Portal
suite; it does not replace the maturity scorers, organization-design skills, or
cloud-neutral architecture work.

## Installation and support boundary

Install the complete Claude plugin from the repository marketplace:

```bash
claude plugin marketplace add Cloud-Byte-Consulting/plugins
claude plugin install azure-platform-engineering@cloud-byte-plugins
```

The plugin currently has a Claude manifest and five Claude agent personas. Its
eight `SKILL.md` directories remain portable and can be installed individually
for Codex or GitHub Copilot with an Agent Skills-compatible installer. There is
no Codex plugin manifest or upload-ready Perplexity package yet because several
implementation workflows require an interactive CLI environment with `az`,
`rad`, `dapr`, `bicep`, and repository tooling.

## Choose the right skill

| Need | Skill | Primary result |
|---|---|---|
| Establish enforceable platform constraints | `platform-constitution` | Versioned constitution with `CON-xx` rules and approvals |
| Inventory a brownfield Azure estate | `azure-estate-assessor` | I9 evidence delta and workload disposition map |
| Choose platform count and Azure topology | `azure-platform-designer` | Architecture specification, ADRs, environment topology, and landing-zone plan |
| Move existing workloads onto the platform | `workload-onboarder` | One governed PR per disposition-map row |
| Build Radius and Dapr golden paths | `radius-golden-path-builder` | Resource Types, Recipes, environments, Dapr components, and GitOps layout |
| Design the platform API and MCP surface | `golden-path-api-designer` | OpenAPI contract, APIM policies, MCP tool schema, and orchestrator specification |
| Review generated or human-authored IaC | `iac-guardrail-verifier` | Per-layer pass, warning, or blocking findings |
| Build durable agentic operations | `agentic-ops-builder` | Approval, monitor, saga, and remediation workflows on Dapr Workflow |

## Operating modes and permissions

Keep assessment and implementation authority separate.

### Assessment mode

Increment I9 is read-only. Use Azure `Reader` at the approved subscription or
management-group scope. Add cost visibility only through separately approved I4
access. The operator may query Resource Graph, run azqr and Governance
Visualizer, and create draft exports with `aztfexport --hcl-only` or Bicep
decompilation. Do not request write roles, read secret values, or treat exported
IaC as deployable code.

### Design mode

Design mode needs the approved estate evidence, platform constitution, target
developer populations, application stacks, regions, regulatory boundaries, and
current landing-zone decisions. It produces specifications and ADRs; it does
not need Azure mutation rights.

### Implementation mode

Implementation requires a platform repository, protected PR workflow, human
approvers, CI validation, and deployment identities scoped to the intended
environment. Agents may propose branches, PRs, and approval requests. Direct
environment mutation, destructive action, identity changes, or retirement
remains approval-gated by the constitution.

## Workflow 1: run Azure estate discovery as I9

Use I9 when the organizational assessment cannot answer which Azure resources
exist, how consistently they are governed, how much is represented in source
control, or where each workload should land.

1. Charter subscriptions, management groups, regions, observation date, and
   prohibited fields in `assessment-orchestrator`.
2. Confirm Azure `Reader` access and the tools allowed inside the evidence
   boundary.
3. Run `azure-estate-assessor` across Resource Graph, azqr, Governance
   Visualizer, and approved IaC-coverage checks.
4. Emit immutable `I9-Exxx` findings with tool/query provenance, timestamp,
   confidence, restrictions, and formal-model targets.
5. Produce the disposition map: **Recipe-wrap**, **Refactor**, **Leave in
   place**, or **Retire** for each workload or resource group.
6. Return an assessment delta to I8. Do not edit the canonical assessment state
   directly.

Starting prompt:

> Use assessment-orchestrator and azure-estate-assessor to run I9 for these
> approved subscriptions. Confirm Reader-only access, emit an I9 delta and
> disposition map, keep cost under I4, exclude secret values, and label every
> exported IaC artifact as draft evidence.

## Workflow 2: design the target Azure platform

1. Run `platform-constitution` first. Record allowed regions, residency,
   compliance, naming, tagging, approved stacks, IaC rules, agent authority,
   and observability defaults as numbered constraints.
2. Provide `azure-platform-designer` the constitution, I9 disposition map,
   developer populations, application stacks, business units, and regulatory
   boundaries.
3. Start with one thin platform. Add Radius environments before adding separate
   platforms; split only when developer populations materially diverge.
4. Choose the environment ladder: simple, application-centric, or enterprise
   by business unit, region, and production boundary.
5. Produce an AVM-first landing-zone plan, central observability design,
   topology diagram, and ADR for every contested decision.

Starting prompt:

> Use platform-constitution and azure-platform-designer with this I9 disposition
> map. Recommend the smallest viable platform count, select the Radius
> environment rung, map landing zones to available AVM modules, and return ADRs
> plus a Mermaid topology. Keep opinions distinguishable from source mandates.

## Workflow 3: onboard workloads and build golden paths

Use `workload-onboarder` to execute the disposition map one workload per PR:

- **Recipe-wrap:** place acceptable existing Terraform or Bicep behind a Radius
  Recipe without rewriting it.
- **Refactor:** derive a specification from deployed evidence, then regenerate
  through `radius-golden-path-builder` with AVM modules.
- **Leave in place:** register ownership and dependencies for visibility and set
  a review date.
- **Retire:** create a dependency-checked, retention-aware decommission plan
  with explicit approval.

Every implementation PR must run `iac-guardrail-verifier`. It checks the
constitution at generation time, static analysis and recipe contracts at plan
time, Azure Policy alignment at deploy time, and runtime policy coverage as the
backstop. Exported IaC never bypasses this process.

## Radius and Dapr portability model

The platform uses two independent portability axes:

| Axis | Mechanism | Stable artifact |
|---|---|---|
| Code portability | Dapr building-block APIs with environment-specific components | Application source |
| Deployment portability | Radius Resource Types, Recipes, and Environments | Application definition |

For sovereignty-sensitive workloads, encode allowed regions as constitution
rules, route persistence and messaging through Dapr building blocks, create one
Radius environment per sovereignty boundary, pin recipes to the approved
region, prohibit cross-boundary data connections, and test relocation in
non-production. Treat backend-specific consistency and messaging semantics as
test obligations rather than assuming the abstraction makes every backend
identical.

Read the complete checklist and maturity caveats in
[references/dapr-radius-sovereignty.md](references/dapr-radius-sovereignty.md).

## Workflow 4: expose golden paths to humans and agents

`radius-golden-path-builder` is the transitional repository-stamping path. The
target state is `golden-path-api-designer`:

1. Define the OpenAPI contract before implementing the backend.
2. Put the platform API behind APIM with caller identity, rate limits, audit
   logging, and versioned operations.
3. Map operations to Radius, AVM, GitOps PRs, and approval-aware Dapr workflows.
4. Keep the platform MCP server thin: one tool per platform API operation, with
   authorization enforced by the API rather than duplicated in the adapter.
5. Use `agentic-ops-builder` for durable approval, monitor, saga, and
   remediation patterns on AKS.

Mutating operations must produce auditable events. Destructive operations and
high-risk changes require the human approval chain defined in the constitution.

## Cross-plugin delegation

| Question | Delegate to |
|---|---|
| Platform maturity and supported formal stages | `adp-enablement:platform-maturity-benchmark` |
| Organization design, funding, and ownership | `platform-assessment:platform-org-design-advisor` |
| ROI and measurement program | `platform-assessment:platform-roi-scorecard` |
| Cloud-neutral IDP/ADP architecture | `platform-assessment:idp-adp-architect` |
| Agent identity and short-lived credentials | `adp-enablement:agent-identity-engineer` |
| API contract and MCP authoring mechanics | `adp-enablement:agent-api-contract-designer` and `mcp-platform-api-author` |
| Platform security program and audit governance | `platform-assessment:platform-security-playbook` |

## Completion checklist

- Constitution is approved, versioned, and referenced by rule ID.
- I9 evidence contains provenance, dates, confidence, and no secret values.
- Every workload has a disposition, target environment, owner, and next action.
- Platform count and environment topology have ADRs and stated trade-offs.
- Sovereignty boundaries are encoded in environments and recipes, not prose
  alone.
- Every implementation is one PR per workload and passes all four guardrail
  layers.
- Agent credentials are short-lived and scoped; mutations are PR- or
  approval-gated.
- Platform API, MCP tools, workflows, and GitOps events share one auditable
  control path.
