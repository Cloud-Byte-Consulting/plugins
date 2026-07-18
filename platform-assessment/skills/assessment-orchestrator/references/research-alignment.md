# Assessment Research Alignment

## Purpose

Use this reference to keep incremental assessment work aligned with the
repository's source policy and maturity models. The user supplied the full
research report and two expanded questionnaire documents for inclusion on
2026-07-18. They are now bundled as non-controlling references alongside this
alignment layer.

The supplied research uses ADP to mean Agentic Developer Platform and explores
a unified 0–4 rubric. The repository uses ADP to mean Agentic Developer Portal
and does not adopt the unified score. Treat the supplied report as framework
context and a source-discovery aid; this file and `../SKILL.md` control whenever
terminology, scoring, privacy, or evidence-handling guidance differs.

## Controlling model boundaries

Keep three independent outputs:

1. **Platform engineering:** the CNCF four-stage, five-aspect model—Investment,
   Adoption, Interfaces, Operations, and Measurement—scored by
   `platform-maturity-benchmark`.
2. **Agentic delivery:** the eight ASDLC paths—Retrieve, Implement, Validate,
   Promote, Deploy, Observe, Remediate, and Dispatch—scored by
   `asdlc-maturity-assessment`.
3. **Agentic Developer Portal readiness:** seven use-case-specific gates scored
   pass, partial, fail, or unobserved by `platform-maturity-discovery`.

Do not create a unified 0–4 platform-and-agent score. Display ordinals used for
charts are not formal scores. An Internal Developer Portal is a human-facing
interface; an Internal Developer Platform supplies backend capabilities; an
Agentic Developer Portal supports human and agent users through governed
knowledge and capability interfaces.

## Research mechanics retained

- Split collection into static scans, runtime/API observations, computed
  cross-references, and human sensing.
- Record Behavioral, Derived, or Attested evidence and the collection method.
- Reconcile findings as confirmed, contradicted, or gap-filled.
- Treat catalog, agent-instruction, and MCP configuration files as leads until
  completeness, freshness, adoption, and runtime use are checked.
- Compare platform staff, platform users, security/operations, and leadership
  as separate survey cohorts.
- Tag survey questions CONFIRM when they test a system finding and GAP-FILL when
  the answer cannot be observed reliably.
- Preserve contradictions such as high catalog coverage with low trust as
  findings; never average them away.

## Research proposals not adopted

- One blended IDP/ADP maturity level or enterprise-wide average.
- File-presence scoring as proof of readiness.
- Vendor Bronze/Silver/Gold scorecards as formal assessment authority.
- Fixed security thresholds copied from draft guidance.
- Automatic maturity scoring from survey response bands.
- Passive email, chat, or transcript mining without explicit authority,
  jurisdiction review, minimization, and aggregation.

## Included source documents

- `idp-adp-maturity-assessment-research.md`: full background research and source
  links; its synthesized rubric is a research hypothesis, not a formal score.
- `methodology-specific-confirmation-gap-fill-questionnaires.md`: use only the
  sections triggered by a documented evidence gap; answers remain Attested
  evidence for the controlling scorer.
- `idp-adp-maturity-survey-by-role.md`: optional extended I7 survey; distribute
  only the relevant role section after the required approvals and suppression
  rules are recorded.

## Primary references

- [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/wgs/platforms/maturity-model/readme/)
- [Microsoft Platform Engineering Capability Model](https://learn.microsoft.com/en-us/platform-engineering/platform-engineering-capability-model)
- [DORA AI Capabilities Model](https://dora.dev/ai/capabilities-model/report/)
- [DORA survey questions](https://dora.dev/ai/capabilities-model/questions/)
- [GitHub fine-grained token permissions](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens)
- [Kubernetes RBAC guidance](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [AWS Billing read-only policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSBillingReadOnlyAccess.html)
- [Azure Cost Management scopes and roles](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-work-scopes)
- [Google Cloud Billing access control](https://cloud.google.com/billing/docs/how-to/billing-access)

Reverify provider permissions, product availability, legal requirements, and
security guidance at engagement time; they change independently of this skill.
