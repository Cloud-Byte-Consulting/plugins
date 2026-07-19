---
name: platform-constitution
description: >-
  Author or amend a platform constitution — the versioned, org-wide constraint
  document (allowed regions, compliance regimes, naming and tagging standards,
  approved stacks, IaC rules, agent authority boundaries) that every downstream
  platform skill and agent treats as its governing contract. Use when starting
  an Azure platform engagement, capturing org guardrails, defining what agents
  may and may not do, or when any platform decision lacks a written constraint
  to cite. Modeled on spec-driven development: the constitution is the first
  SDD artifact, upstream of specs, plans, and code.
---

# Platform Constitution

## Purpose
Agentic platform engineering moves the system of record upstream of IaC: agents
generate code, so the durable artifacts are the constraints the code must obey.
The constitution is that artifact — the equivalent of Spec Kit's
`/speckit.constitution` phase, applied to a whole platform. Every other skill in
this plugin reads it before acting; the `iac-guardrail-verifier` enforces it.

## What a constitution contains
Capture only decided, enforceable constraints — aspirations belong in roadmaps:

1. **Scope and sovereignty** — allowed Azure regions, data-residency rules,
   allowed clouds (this plugin assumes Azure + OSS), sovereignty requirements.
   Where residency boundaries apply, encode them as enforceable rules: every
   persistence/messaging dependency goes through a Dapr building block (no
   native backing-store SDK on a sovereignty-critical path), and each boundary
   gets its own Radius environment with region-pinned Recipes — so relocation
   is a deployment decision, not a rewrite. See
   `../../references/dapr-radius-sovereignty.md`.
2. **Compliance regimes** — which of SOC 2 / ISO 27001 / NIS2 / DORA / sector
   rules apply, and the evidence each demands from the platform.
3. **Naming, tagging, hierarchy** — management-group layout, subscription
   vending policy (avm/ptn/lz/sub-vending parameters), resource naming tokens,
   mandatory tags (owner, cost-center, environment, data-classification).
4. **Approved stacks** — the opinionated core (e.g. Radius + Dapr + Flux + AVM
   Bicep + AKS/ACA) and the documented swap paths; IaC language policy
   (Bicep-first; Terraform/OpenTofu where, and under what license stance).
5. **IaC rules** — AVM-first with justified-exception comments, pinned module
   versions resolved from the registry (never invented), PR-only writes,
   four-layer enforcement expectations.
6. **Agent authority boundaries** — what agents may do autonomously (read,
   propose PRs, open issues), what requires human approval (deploys, deletes,
   identity changes), and which credentials agents hold (read-only by default,
   short-lived, no standing secrets).
7. **Observability defaults** — every landing zone ships Log Analytics + Azure
   Monitor workspace wired to the central Managed Grafana; diagnostic settings
   on by default.

## Workflow
1. Interview for existing standards (CAF alignment, existing landing zones,
   naming conventions already in force) — do not invent where the org decided.
2. Draft the constitution as versioned Markdown in the platform repo; each
   rule gets an ID (`CON-xx`) so specs, PRs, and verifier findings cite rules.
3. Review with security/compliance owners; record approvals in the document.
4. Amendments follow the same PR + approval path — the constitution is code.

## Output
`platform-constitution.md` — versioned, rule-ID'd, with an approvals log and a
changelog. Downstream skills cite rule IDs in every recommendation.

## Delegates to
- Org structure, funding, and operating model → `platform-assessment:platform-org-design-advisor`
- Security governance depth and audit-trail design → `platform-assessment:platform-security-playbook`
- Agent credential and identity mechanics → `adp-enablement:agent-identity-engineer`
