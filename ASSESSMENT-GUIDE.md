# Assessment Guide: Platform Engineering and ADP Maturity

Use this guide to prepare and run an evidence-based assessment when access is
split across repository, delivery, platform, finance, security, data, and
leadership roles. Start with the `assessment-orchestrator` skill; it coordinates
`platform-maturity-discovery`, the formal scorers, and the reporter.

The assessment produces three independent readings:

1. platform-engineering maturity across Investment, Adoption, Interfaces,
   Operations, and Measurement;
2. ASDLC maturity across eight agentic delivery paths;
3. Agentic Developer Portal readiness across seven use-case gates.

There is no combined maturity number. An Internal Developer Portal is one
human-facing interface; the Internal Developer Platform supplies backend
capabilities; the Agentic Developer Portal supports governed human and agent use.

## Before starting

1. Read [GETTING-STARTED.md](GETTING-STARTED.md) and install the relevant plugin
   using [README.md](README.md). Perplexity users upload
   `platform-assessment/perplexity/assessment-orchestrator.zip` as a Computer
   Skill.
2. Name an assessment lead and the business decision the assessment will support.
3. Define scope: value streams, teams/cohorts, repositories, clusters, cloud
   accounts, systems, and observation windows.
4. Approve the privacy and evidence charter: allowed sources, fields, queries,
   raw-evidence owners, aggregation, retention/deletion, and prohibited uses.
5. Map current access to the increments below. Start authorized work immediately;
   missing access becomes a documented gap, not permission to broaden collection.

## Permissions matrix

Default system collection is read-only. Survey distribution, interviews, and any
communication-content analysis are separate actions requiring explicit authority.
Provider names below are examples; verify roles and endpoint permissions when the
engagement starts.

| ID | Operator | Minimum read-only access | Explicit exclusions / approval notes |
|---|---|---|---|
| I1 Repositories and artifacts | Git organization reader | Selected repository list and contents; PR/merge metadata; ownership/catalog/IaC/agent-instruction files; rulesets and branch protection | No repository write, secret access, issue mutation, or private repo outside scope. For GitHub fine-grained tokens, select the organization as resource owner, limit repositories, request Contents read + Pull requests read + Administration read for protection/rulesets; organization approval may be required. |
| I2 CI/CD and delivery flow | Delivery/release engineer | Pipeline/check run metadata, workflow definitions, deployment events, artifact/provenance metadata; existing DORA tool viewer where available | No rerun, cancel, approve, deploy, artifact delete, or environment-secret access. Logs may contain secrets or personal data; collect aggregates first and retrieve log content only when specifically approved. |
| I3 Kubernetes and platform infrastructure | Platform engineer | Custom `get/list/watch` access for approved namespaces, workloads, quotas/limits, nodes, CRDs, policy and RBAC metadata; Prometheus/Grafana viewer | No `cluster-admin`, create/update/delete, `exec`, port-forward, Secret read, or pod logs by default. Kubernetes `view` excludes Secrets and role/binding visibility, so use a narrow custom ClusterRole only when those metadata are required. |
| I4 Cloud spend and FinOps | FinOps/cloud analyst | Cost viewer at the smallest useful scope; Kubecost/OpenCost viewer; approved allocation/tag metadata | No budget/export mutation, purchase, reservation change, resource change, or cross-account access. Prefer a narrow AWS Cost Explorer policy; use `AWSBillingReadOnlyAccess` only if its broader bill visibility is approved. Use Azure `Cost Management Reader`. Use Google Cloud `roles/billing.viewer` only if billing-account transaction visibility is approved; otherwise provide a scoped project-cost view/export. |
| I5 Security and agent governance | Security/identity engineer | Security finding/status viewer; approved AI tool and MCP inventory; non-human identity/application metadata; audit-event viewer | No credential/token value, Secret read, policy mutation, incident response action, or unrestricted audit export. Security may run this increment internally and provide only aggregate findings. |
| I6 Data platform | Data platform owner | Catalog/metastore metadata, lineage, schema, data-contract, quality-result, and pipeline metadata viewer | No production row data, customer/employee records, unrestricted samples, data export, or pipeline mutation by default. Sample content requires a separate approved purpose and minimization plan. |
| I7 Surveys and interviews | Platform product or assessment lead | Authority to distribute the approved survey and conduct standardized interviews; approved cohort definitions and suppression threshold | No mailbox/chat/transcript mining by default. Keep raw answers with the survey owner; state receives aggregate counts and themes. Complete privacy/HR/legal and worker-representation review where applicable. |
| I8 Reconciliation and synthesis | Assessment lead | Canonical assessment state, increment deltas, scorer versions, and approved evidence summaries | No raw source access is required. The lead may reject evidence that lacks provenance, scope, date, restriction, or confidence. |
| I9 Cloud estate (Azure) | Platform engineer | Azure `Reader` at the approved subscription/management-group scope for Resource Graph queries, azqr scans, and Azure Governance Visualizer collection; `aztfexport --hcl-only` / `az bicep decompile` for IaC-coverage analysis (no state writes) | No write scopes, role/policy mutation, or secret/connection-string values in evidence — resource IDs and configuration flags only. Exported IaC is draft evidence, never production code. Cost visibility stays under I4. Runs via the companion `azure-platform-engineering` plugin's `azure-estate-assessor` skill and returns a standard increment delta (evidence IDs `I9-Exxx`) merged by I8 like any other increment. |

### Permission references

- GitHub documents `Administration: read` for branch-protection endpoints and
  explains organization approval for fine-grained tokens:
  [protected branches](https://docs.github.com/en/rest/branches/branch-protection),
  [token approval](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/managing-requests-for-personal-access-tokens-in-your-organization).
- Kubernetes documents that the default `view` role omits Secrets and role or
  role-binding visibility: [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
- Cloud-provider examples:
  [AWS Billing read-only](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingReadOnlyAccess.html),
  [Azure Cost Management roles](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes), and
  [Google Cloud Billing roles](https://cloud.google.com/billing/docs/how-to/billing-access).

The GitHub fine-grained-token failure mode deserves care: a token scoped to the
user instead of the organization—or awaiting organization approval—can still read
public resources while private organization endpoints appear unavailable. Select
the organization as resource owner, select the intended repositories, request
only the read permissions above, and obtain approval if enforced. A `404` alone
does not prove which permission is missing, and a failed write is expected for an
assessment token.

## State and handoffs

The assessment lead owns one canonical `assessment-state.yaml`. Every evidence
record is immutable, dated, scoped, classified, and linked to a stable source
locator. Corrections append a new record that supersedes the old one.

For sequential work, pass the latest state to the next operator. For parallel
work, each operator returns
`assessment-delta-<increment>-<date>.yaml`; the lead or I8 imports deltas into the
canonical state. Do not have multiple people edit the canonical YAML concurrently.

State contains findings, not raw data:

- use increment-prefixed IDs such as `I2-E004`;
- record Behavioral, Derived, or Attested evidence;
- record static scan, runtime/API observation, computed cross-reference, or
  human sensing as the collection method;
- record Measured, Surveyed, Estimated, or Qualitative evidence tier;
- target one or more formal domains without assigning a combined level;
- keep names, secrets, raw responses, message text, and unrestricted locators out.

## Running the assessment

### 1. Plan

Start with:

> Use assessment-orchestrator to charter this assessment and map our current
> roles and permissions to runnable increments. Do not request write access or
> assign a formal score yet.

The output should include scope, models and versions, approved sources, privacy
boundary, runnable increments, access gaps, state location, and owners by role.

### 2. Run increments

Each operator works only inside their authorization boundary:

> Use assessment-orchestrator to run increment I3. Here is the current state (or
> base-state version). Return an assessment delta, a coverage/confidence summary,
> and the next-role handoff.

Within the increment, `platform-maturity-discovery` controls evidence quality.
Static file presence is a lead; validate completeness, freshness, adoption, and
runtime behavior. Reconcile independent evidence as confirmed, contradicted, or
gap-filled. Preserve “maturity theater” contradictions instead of averaging them.

### 3. Merge and resume

When work resumes after a pause, load the canonical state and read `open_gaps`,
`reconciliations`, model versions, source dates, and deletion dates first. Refresh
stale snapshots; do not discard still-valid evidence merely because time passed.

### 4. Synthesize

I8 may produce a partial coverage report after two increments. Formal results are
assigned only when each scorer's evidence prerequisites are satisfied:

- `platform-maturity-benchmark` assigns the five platform stages;
- `asdlc-maturity-assessment` assigns path levels and the permitted overall ASDLC
  result;
- `platform-maturity-discovery` assigns the seven use-case-specific ADP gates.

Contradictions reduce confidence and remain visible. They do not automatically
become an average or a lower numeric score. Unsupported domains remain Pending or
unobserved.

### 5. Report

Pass the reconciled state to `platform-assessment-reporter`:

> Build the cited assessment report from this state. Show separate platform,
> ASDLC, and ADP radar profiles, adjacent evaluation ledgers, stable evidence
> citations, confidence, contradictions, coverage, and could-not-measure gaps.

Then send the gap register to `idp-adp-architect` for the target architecture and
sequenced roadmap.

## Privacy and people data

For I7, use the [concise core survey](platform-assessment/skills/assessment-orchestrator/references/maturity-survey-instrument.md)
by default. Use the [extended by-role survey](platform-assessment/skills/assessment-orchestrator/references/idp-adp-maturity-survey-by-role.md)
when the charter calls for cross-role comparison, or select only the relevant
section of the [methodology-specific questionnaires](platform-assessment/skills/assessment-orchestrator/references/methodology-specific-confirmation-gap-fill-questionnaires.md)
when an evidence gap needs confirmation. Record the instrument version and
question IDs. Do not administer all questionnaires merely because they are
available. The [full research synthesis](platform-assessment/skills/assessment-orchestrator/references/idp-adp-maturity-assessment-research.md)
is bundled as background material; its unified scoring proposal is not the
suite's controlling assessment model.

- Assess systems, paths, controls, queues, and aggregate experience—never people.
- Prefer metadata and aggregates; collect content only when necessary and
  explicitly authorized.
- Preserve cohort response rate and suppression; never expose a small cohort.
- Redact direct identifiers inside the approved boundary before external LLM use.
- Keep raw survey/interview data with its owner and delete it on schedule.
- Do not use findings for discipline, individual ranking, protected-trait
  inference, or covert monitoring.
- Treat jurisdiction-specific privacy impact assessment and worker consultation
  as prerequisites where required; this repository is not legal advice.

## Cadence

- I1–I6: refresh the same bounded queries weekly, monthly, or on an agreed event;
  continuous scans require separate operational approval.
- I7: normally quarterly, retaining identical core wording and cohort definitions.
- I8: rerun when material evidence changes; retain model versions and prior
  readings so trends are comparable.

A useful baseline can be partial. The defensible statement is “six increments
complete; Investment and Data unobserved,” not a complete-looking score built from
missing access.
