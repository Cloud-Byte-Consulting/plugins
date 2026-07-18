# Cloud Byte Consulting — Agent Skill Plugins

Reusable agent skills in the open [Agent Skills](https://agentskills.io) format (`SKILL.md`), packaged as installable plugins. Compatible with Claude (Claude Code, claude.ai), GitHub Copilot, OpenAI Codex, and Google Gemini/Antigravity — no format conversion required. Perplexity-compatible workflows also ship as upload-ready ZIPs.

**New here? Read [GETTING-STARTED.md](GETTING-STARTED.md)** — what to run first, a staged growth path (baseline → measure → report → iterate), and copy-paste first prompts.

## Plugins

### `platform-assessment`
Assess an engineering organization's platform and agentic readiness. Evidence-first: skills collect proof via first-party MCP connectors (GitHub, Azure DevOps, Atlassian, Microsoft Work IQ, AWS/Azure/GCP) rather than self-report.

The enterprise operating-model additions are documented in [`PLATFORM-ENGINEERING-SOURCE-NOTES.md`](PLATFORM-ENGINEERING-SOURCE-NOTES.md).

A fully scored discovery uses both `platform-assessment` and `adp-enablement`: the first gathers evidence and scores agentic delivery maturity; the second supplies the source-versioned platform-maturity benchmark. A standalone `platform-maturity-discovery` ZIP produces an evidence package and ADP gate readout, while marking unavailable formal scores as pending.

| Skill | What it does |
|---|---|
| `platform-maturity-discovery` | Discovers platform-engineering and Agentic Developer Portal readiness from privacy-bounded signals across communications, meetings, work items, code, infrastructure, telemetry, and developer sentiment |
| `asdlc-maturity-assessment` | Scores agentic development maturity on an 8-path × 5-level rubric (L0–L4); demands measurable attribution before scoring L2+ |
| `platform-roi-scorecard` | Builds a defensible platform ROI case: survey + system data doctrine, cost/value formulas, benchmark calibration, AI-workload velocity metrics |
| `platform-org-design-advisor` | Diagnoses platform team structure: reporting lines, role coverage (7 platform roles), autonomy-level-driven operating model, agent-transparency design |
| `platform-security-playbook` | Designs and audits governance for human+agent development: 5 control responsibilities, privilege-separation patterns, regulatory mapping, vulnerability management, sovereignty overlay |
| `platform-industry-brief` | Produces industry-contextualized briefs: benchmark databank + vertical pattern library (automotive, gaming, classifieds, healthcare, freight) |
| `idp-adp-architect` | Designs Internal Developer Platform capabilities and an Agentic Developer Portal target architecture: five-plane model, human and machine interfaces, golden paths, AI/ML sixth plane, sovereign variant |
| `platform-assessment-reporter` | Renders assessment results as evidence-backed reporting visuals: production-system quadrant, six-vector value radar, golden-path coverage maps — every point carries a metric/source/confidence tier; unmeasurable dimensions are explicitly marked qualitative |

### `authoring`
Turn research and interviews into publishable deliverables. Method skills — they generalize beyond platform engineering.

| Skill | What it does |
|---|---|
| `research-brief-writer` | Dense, evidence-first research briefs from reports and multi-source material |
| `interview-case-study-writer` | Interview transcripts → expert features and company case studies |

### `ai-operations`
Operate AI at work — routing, triage, verification, governance, harness. Frameworks distilled from practitioner literature (2025–2026).

| Skill | What it does |
|---|---|
| `work-shape-triage` | Decides what work should be a chat, one agent, a team, or nothing — four-estimates rubric + money-dial veto |
| `model-selection-router` | Routes work across model tiers; personal eval sets, benchmark-interpretation discipline, launch triage |
| `agent-trust-auditor` | Verifies agent output: judge layers, delegability tests, constitutions, completion-vs-acceptance analytics |
| `agent-ops-governance` | Ownership cards, tool pruning, token cost measurement, prototype ladder, license/renewal review |
| `agent-harness-engineer` | Audits and builds the instruction/memory/handoff/knowledge layer around agents |

### `engineering-career`
| Skill | What it does |
|---|---|
| `engineering-career-coach` | Level-up behaviors, junior anti-signals, org signal reading, behavioral interview prep, AI-era positioning |

### `ai-engineering`
Production LLM app practices, sourced from public educational materials.

| Skill | What it does |
|---|---|
| `llm-evals-engineer` | Tracing, RAG metric suites, LLM-as-judge, guardrails, prompt versioning, budget gateways |
| `llm-app-deployer` | Prototype → production: service extraction, container recipe, cloud rollout, vector-store tuning |

### `prompt-workflows`
Thirty-five reusable workflows imported from the Cloud Byte Document Hub.

| Group | Skills |
|---|---:|
| Model fit and routing | 4 |
| Personal productivity | 5 |
| Code comprehension | 4 |
| Knowledge systems | 5 |
| Agent evaluation and packaging | 7 |
| Consumer AI strategy | 5 |
| Office documents | 5 |

See [`prompt-workflows/README.md`](prompt-workflows/README.md) for the group summary and Perplexity packaging workflow.
See [`prompt-workflows/PROVENANCE.md`](prompt-workflows/PROVENANCE.md) for publication and third-party-source handling.

### Research division suites

Thirty-one operational skills for AI research platforms, imported from the Cloud Byte research-division bundle and hardened for publication.

| Plugin | Skills | Focus |
|---|---:|---|
| `gpu-research-platform` | 7 | GPU tenancy, sharing, autoscaling, FinOps, GitOps, security, troubleshooting |
| `model-training-ops` | 6 | Training pipelines, experiment standards, distributed training, Ray, fine-tuning |
| `inference-testing` | 6 | Evaluation, benchmarking, release gates, rollout, drift, authorized red-teaming |
| `research-data-platform` | 6 | Data contracts, SLOs, governance, catalogs, reproducible training storage |
| `adp-enablement` | 6 | Platform maturity, MCP APIs, agent identity, API contracts, golden paths, fitness functions |

See [`RESEARCH-DIVISION-PROVENANCE.md`](RESEARCH-DIVISION-PROVENANCE.md) for source history, review scope, and publication notes.

## Install

### Claude Code / claude.ai (plugin marketplace)
```bash
claude plugin marketplace add Cloud-Byte-Consulting/plugins
claude plugin install platform-assessment@cloud-byte-plugins
claude plugin install authoring@cloud-byte-plugins
claude plugin install prompt-workflows@cloud-byte-plugins
claude plugin install gpu-research-platform@cloud-byte-plugins
claude plugin install model-training-ops@cloud-byte-plugins
claude plugin install inference-testing@cloud-byte-plugins
claude plugin install research-data-platform@cloud-byte-plugins
claude plugin install adp-enablement@cloud-byte-plugins
```

### GitHub Copilot
Copilot loads skills from `.github/skills/`, `.claude/skills/`, or `.agents/skills/` in your project. Copy the skill folders in:

```bash
npx skills add Cloud-Byte-Consulting/plugins --full-depth -a github-copilot
```

or manually:

```bash
mkdir -p .github/skills
cp -R <clone>/platform-assessment/skills/* .github/skills/
```

### OpenAI Codex
```bash
npx skills add Cloud-Byte-Consulting/plugins --full-depth -a codex
```
or copy skill folders into `.agents/skills/` (repo) / `~/.agents/skills/` (user).

### Perplexity Computer

Download an individual ZIP from a plugin's `perplexity/` directory and upload it as a Computer Skill. Each archive contains `SKILL.md` at its root and is limited to 10 MB. The available collections are:

- [`prompt-workflows/perplexity/`](prompt-workflows/perplexity/)
- [`platform-assessment/perplexity/`](platform-assessment/perplexity/)
- [`gpu-research-platform/perplexity/`](gpu-research-platform/perplexity/)
- [`model-training-ops/perplexity/`](model-training-ops/perplexity/)
- [`inference-testing/perplexity/`](inference-testing/perplexity/)
- [`research-data-platform/perplexity/`](research-data-platform/perplexity/)
- [`adp-enablement/perplexity/`](adp-enablement/perplexity/)

Rebuild the packages after edits with:

```bash
python3 prompt-workflows/scripts/package_perplexity.py
python3 scripts/package_research_perplexity.py
```

### Microsoft 365 Copilot (declarative agents)
Different surface from GitHub Copilot: M365 Copilot doesn't load SKILL.md. The path is a **declarative agent** (Agent Builder or Teams Toolkit) whose plain-English *Instructions* are derived from a skill body, with knowledge grounding (SharePoint/Graph connectors) and MCP tools as *Actions*. Instructions have a size cap, so a skill must be condensed to its Workflow + Guardrails core. Not included in this repo yet — see [Copilot Developer Camp](https://microsoft.github.io/copilot-camp/) for the build pattern.

### Google Gemini / Antigravity
```bash
npx skills add Cloud-Byte-Consulting/plugins -a gemini-cli
```
or copy skill folders into `.agents/skills/` or `.gemini/skills/`.

## Layout

```
.claude-plugin/marketplace.json     # Claude plugin marketplace manifest
platform-assessment/
├── .claude-plugin/plugin.json
├── .codex-plugin/plugin.json
├── skills/<name>/
│   ├── SKILL.md                    # 8 assessment skills
│   └── agents/openai.yaml
└── perplexity/<name>.zip
authoring/
├── .claude-plugin/plugin.json
└── skills/<name>/SKILL.md          # 2 authoring skills
prompt-workflows/
├── .claude-plugin/plugin.json
├── .codex-plugin/plugin.json
├── skills/<name>/SKILL.md           # 35 portable workflows
├── perplexity/<name>.zip            # upload-ready packages
└── scripts/package_perplexity.py
gpu-research-platform/              # same cross-tool shape for each research suite
├── .claude-plugin/plugin.json
├── .codex-plugin/plugin.json
├── skills/<name>/
│   ├── SKILL.md
│   └── agents/openai.yaml
└── perplexity/<name>.zip
```

Each `SKILL.md` is self-contained (frameworks, rubrics, formulas, and checklists inline) and carries `[bracketed]` placeholders to fill in before use. Skills cross-reference sibling skills by name; installing a full plugin keeps those links resolvable.
