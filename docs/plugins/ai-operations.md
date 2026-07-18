# `ai-operations`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Operate AI at work: model selection/routing, work-shape triage (chat/agent/team/nothing), agent output verification, cost/ownership/tool governance, and harness engineering (instructions, memory, handoffs).

- Version: `1.0.0`
- Category: `operations`
- Skills: 5
- Claude plugin: yes
- Codex plugin manifest: no; install the portable skills directly
- Perplexity packages: not currently packaged

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`agent-harness-engineer`](../../ai-operations/skills/agent-harness-engineer/SKILL.md) | Audit, redesign, and maintain the harness around an AI agent — the instruction, memory, tool, and check layer that shapes every run. | — |
| [`agent-ops-governance`](../../ai-operations/skills/agent-ops-governance/SKILL.md) | Operate and govern a fleet of AI agents like managed labor, not shelfware. | — |
| [`agent-trust-auditor`](../../ai-operations/skills/agent-trust-auditor/SKILL.md) | Design and run verification for AI-agent output so you never take an agent's word for anything. | — |
| [`model-selection-router`](../../ai-operations/skills/model-selection-router/SKILL.md) | Route every AI job to the cheapest model that survives review, and stop defaulting to the frontier out of habit. | — |
| [`work-shape-triage`](../../ai-operations/skills/work-shape-triage/SKILL.md) | Decide what shape of AI (if any) a piece of work deserves. | — |

## Plugin files

- [Claude manifest](../../ai-operations/.claude-plugin/plugin.json)
- Codex: install individual skill directories through an Agent Skills-compatible installer.
- [Skill source directory](../../ai-operations/skills/)
