# Cloud Byte Consulting — Agent Skill Plugins

Reusable agent skills in the open [Agent Skills](https://agentskills.io) format (`SKILL.md`), packaged as two plugins. Compatible with Claude (Claude Code, claude.ai), GitHub Copilot, OpenAI Codex, and Google Gemini/Antigravity — no format conversion required.

## Plugins

### `platform-assessment`
Assess an engineering organization's platform and agentic readiness. Evidence-first: skills collect proof via first-party MCP connectors (GitHub, Azure DevOps, Atlassian, Microsoft Work IQ, AWS/Azure/GCP) rather than self-report.

| Skill | What it does |
|---|---|
| `asdlc-maturity-assessment` | Scores agentic development maturity on an 8-path × 5-level rubric (L0–L4); demands measurable attribution before scoring L2+ |
| `platform-roi-scorecard` | Builds a defensible platform ROI case: survey + system data doctrine, cost/value formulas, benchmark calibration, AI-workload velocity metrics |
| `platform-org-design-advisor` | Diagnoses platform team structure: reporting lines, role coverage (7 platform roles), autonomy-level-driven operating model, agent-transparency design |
| `platform-security-playbook` | Designs and audits governance for human+agent development: 5 control responsibilities, privilege-separation patterns, regulatory mapping, vulnerability management, sovereignty overlay |
| `platform-industry-brief` | Produces industry-contextualized briefs: benchmark databank + vertical pattern library (automotive, gaming, classifieds, healthcare, freight) |
| `idp-adp-architect` | Designs IDP → ADP target architectures: five-plane model with per-cloud mappings, golden paths, AI/ML sixth plane, sovereign variant |
| `platform-assessment-reporter` | Renders assessment results as evidence-backed reporting visuals: production-system quadrant, six-vector value radar, golden-path coverage maps — every point carries a metric/source/confidence tier; unmeasurable dimensions are explicitly marked qualitative |

### `authoring`
Turn research and interviews into publishable deliverables. Method skills — they generalize beyond platform engineering.

| Skill | What it does |
|---|---|
| `research-brief-writer` | Dense, evidence-first research briefs from reports and multi-source material |
| `interview-case-study-writer` | Interview transcripts → expert features and company case studies |

## Install

### Claude Code / claude.ai (plugin marketplace)
```bash
claude plugin marketplace add Cloud-Byte-Consulting/plugins
claude plugin install platform-assessment@cloud-byte-plugins
claude plugin install authoring@cloud-byte-plugins
```

### GitHub Copilot
Copilot loads skills from `.github/skills/`, `.claude/skills/`, or `.agents/skills/` in your project. Copy the skill folders in:

```bash
npx skills add Cloud-Byte-Consulting/plugins -a copilot
```

or manually:

```bash
mkdir -p .github/skills
cp -R <clone>/platform-assessment/skills/* .github/skills/
```

### OpenAI Codex
```bash
npx skills add Cloud-Byte-Consulting/plugins -a codex
```
or copy skill folders into `.agents/skills/` (repo) / `~/.agents/skills/` (user).

### Microsoft 365 Copilot (declarative agents)
Different surface from GitHub Copilot: M365 Copilot doesn't load SKILL.md. The path is a **declarative agent** (Agent Builder or Teams Toolkit) whose plain-English *Instructions* are derived from a skill body, with knowledge grounding (SharePoint/Graph connectors) and MCP tools as *Actions*. Instructions have a size cap, so a skill must be condensed to its Workflow + Guardrails core. Not included in this repo yet — see [Copilot Developer Camp](https://microsoft.github.io/copilot-camp/) for the build pattern.

### Google Gemini / Antigravity
```bash
npx skills add Cloud-Byte-Consulting/plugins -a gemini-cli
```
or copy skill folders into `.agents/skills/` or `.gemini/skills/`.

## Layout

```
.claude-plugin/marketplace.json     # marketplace manifest (both plugins)
platform-assessment/
├── .claude-plugin/plugin.json
└── skills/<name>/SKILL.md          # 6 assessment skills
authoring/
├── .claude-plugin/plugin.json
└── skills/<name>/SKILL.md          # 2 authoring skills
```

Each `SKILL.md` is self-contained (frameworks, rubrics, formulas, and checklists inline) and carries `[bracketed]` placeholders to fill in before use. Skills cross-reference sibling skills by name; installing a full plugin keeps those links resolvable.
