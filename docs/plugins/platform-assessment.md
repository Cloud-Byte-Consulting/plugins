# `platform-assessment`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Assess an engineering org's platform and agentic readiness: ASDLC maturity scoring, platform ROI scorecard, org design, security/governance playbook, industry benchmarking, and IDP/ADP target architecture.

- Version: `1.4.0`
- Category: `assessment`
- Skills: 9
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 9

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`asdlc-maturity-assessment`](../../platform-assessment/skills/asdlc-maturity-assessment/SKILL.md) | Assess where an organization sits across the five levels (0–4) of the Agentic Software Development Lifecycle (ASDLC) — from fully human-driven to fully autonomous — by scoring all eight delivery paths, and produce an… | [ZIP](../../platform-assessment/perplexity/asdlc-maturity-assessment.zip) |
| [`assessment-orchestrator`](../../platform-assessment/skills/assessment-orchestrator/SKILL.md) | Coordinate a platform-engineering and Agentic Developer Portal maturity assessment as permission-scoped increments run by different organizational roles, then merge the evidence into one auditable assessment state with… | [ZIP](../../platform-assessment/perplexity/assessment-orchestrator.zip) |
| [`idp-adp-architect`](../../platform-assessment/skills/idp-adp-architect/SKILL.md) | Design, evolve, or audit an Internal Developer Platform and its human-facing Internal Developer Portal into an Agentic Developer Portal (ADP) that lets AI coding agents consume organizational context and platform… | [ZIP](../../platform-assessment/perplexity/idp-adp-architect.zip) |
| [`platform-assessment-reporter`](../../platform-assessment/skills/platform-assessment-reporter/SKILL.md) | Turn platform and agentic-readiness assessment results into evidence-backed reports and executive visuals, including separate cited radar/spider maturity profiles for platform aspects, ASDLC paths, and Agentic… | [ZIP](../../platform-assessment/perplexity/platform-assessment-reporter.zip) |
| [`platform-industry-brief`](../../platform-assessment/skills/platform-industry-brief/SKILL.md) | ALWAYS use this skill when the user asks how platform engineering looks in a specific industry or vertical — automotive, mobility, gaming, healthcare, logistics, freight, finance, real estate, classifieds, retail, or… | [ZIP](../../platform-assessment/perplexity/platform-industry-brief.zip) |
| [`platform-maturity-discovery`](../../platform-assessment/skills/platform-maturity-discovery/SKILL.md) | Discover evidence of an organization's maturity toward platform engineering and an Agentic Developer Portal (ADP) by triangulating emails and chat, meetings, work items, code and repositories, CI/CD, infrastructure and… | [ZIP](../../platform-assessment/perplexity/platform-maturity-discovery.zip) |
| [`platform-org-design-advisor`](../../platform-assessment/skills/platform-org-design-advisor/SKILL.md) | Use PROACTIVELY whenever the conversation touches how a platform, DevEx, infrastructure, or AI-enablement team should be structured, sized, staffed, funded, or governed. | [ZIP](../../platform-assessment/perplexity/platform-org-design-advisor.zip) |
| [`platform-roi-scorecard`](../../platform-assessment/skills/platform-roi-scorecard/SKILL.md) | Build a developer-productivity and platform-ROI scorecard for a platform engineering team — combining DORA, SPACE, MVP-stage, and AI-workload metrics with a full dollar-value ROI calculation, survey + system-data… | [ZIP](../../platform-assessment/perplexity/platform-roi-scorecard.zip) |
| [`platform-security-playbook`](../../platform-assessment/skills/platform-security-playbook/SKILL.md) | Design, harden, and audit platform-level security and governance for development where humans and AI coding agents work side by side. | [ZIP](../../platform-assessment/perplexity/platform-security-playbook.zip) |

## Plugin files

- [Claude manifest](../../platform-assessment/.claude-plugin/plugin.json)
- [Codex manifest](../../platform-assessment/.codex-plugin/plugin.json)
- [Skill source directory](../../platform-assessment/skills/)
