# Cloud Byte Consulting — Agent Skill Plugins

Reusable agent skills in the open [Agent Skills](https://agentskills.io) format (`SKILL.md`), packaged as installable plugins. Compatible with Claude (Claude Code, claude.ai), GitHub Copilot, OpenAI Codex, and Google Gemini/Antigravity — no format conversion required. Perplexity-compatible workflows also ship as upload-ready ZIPs.

**New here? Read [GETTING-STARTED.md](GETTING-STARTED.md)** — what to run first, a staged growth path (baseline → measure → report → iterate), and copy-paste first prompts.

## Plugin index

<!-- BEGIN GENERATED PLUGIN INDEX -->
Every plugin is registered in the Claude marketplace and contains portable Agent Skills. The manifest and ZIP columns show additional native packaging.

| Plugin | Category | Focus | Skills | Codex manifest | Perplexity ZIPs |
|---|---|---|---:|:---:|---:|
| [`platform-assessment`](docs/plugins/platform-assessment.md) | assessment | Assess an engineering org's platform and agentic readiness: ASDLC maturity scoring, platform ROI scorecard, org design, security/governance playbook, industry… | 9 | Yes | 9 |
| [`adp-enablement`](docs/plugins/adp-enablement.md) | platform | Engineer the Agentic Developer Portal: CNCF platform-maturity benchmark with industry percentiles, MCP servers over platform APIs, agent identity (no standing secrets,… | 6 | Yes | 6 |
| [`azure-platform-engineering`](docs/plugins/azure-platform-engineering.md) | platform | Azure implementation arm of the platform suite: read-only estate assessment (Resource Graph, azqr, Governance Visualizer, aztfexport) feeding assessment increment I9,… | 8 | — | — |
| [`gpu-research-platform`](docs/plugins/gpu-research-platform.md) | platform | Operate GPU research workloads on managed Kubernetes (Lambda-class clouds): GPU sharing (MIG/MPS/time-slicing), KEDA autoscaling on DCGM metrics, cost chargeback,… | 7 | Yes | 7 |
| [`model-training-ops`](docs/plugins/model-training-ops.md) | ml | Run model creation and training as a product: training pipeline architecture (Argo/Kubeflow, trigger taxonomy), MLflow experiment/registry standards,… | 6 | Yes | 6 |
| [`inference-testing`](docs/plugins/inference-testing.md) | ml | Test and release models with evidence: model-level eval harnesses (synthetic ground truth, LLM-as-judge), GPU inference benchmarking (TTFT, tokens/sec, cost), release… | 6 | Yes | 6 |
| [`research-data-platform`](docs/plugins/research-data-platform.md) | data | Make research data collection trustworthy without gatekeeping: ODCS data contracts with CI enforcement, dataset QoS/SLOs, data-product reviews (DAUTNIVS), right-sized… | 6 | Yes | 6 |
| [`authoring`](docs/plugins/authoring.md) | writing | Turn research and interviews into publishable deliverables: evidence-first research briefs and interview-based case studies. | 2 | — | — |
| [`ai-operations`](docs/plugins/ai-operations.md) | operations | Operate AI at work: model selection/routing, work-shape triage (chat/agent/team/nothing), agent output verification, cost/ownership/tool governance, and harness… | 5 | — | — |
| [`engineering-career`](docs/plugins/engineering-career.md) | career | Engineering career coaching: senior/staff level-up behaviors, org signal reading, behavioral interview prep, AI-era positioning. | 1 | — | — |
| [`ai-engineering`](docs/plugins/ai-engineering.md) | engineering | Ship production LLM apps: eval engineering (tracing, RAG metrics, LLM-as-judge, guardrails) and deployment (containers, cloud rollout, vector-store tuning). | 2 | — | — |
| [`prompt-workflows`](docs/plugins/prompt-workflows.md) | productivity | Thirty-five reusable workflows for model routing, personal productivity, code comprehension, knowledge systems, agent evaluation, consumer AI strategy, and Office… | 35 | Yes | 35 |

**12 plugins, 93 skills, and 75 upload-ready Perplexity packages.**

Browse the [plugin and skill documentation](docs/README.md) for the complete per-plugin inventories.
<!-- END GENERATED PLUGIN INDEX -->

## Install

### Claude Code / claude.ai (plugin marketplace)
```bash
claude plugin marketplace add Cloud-Byte-Consulting/plugins
claude plugin install platform-assessment@cloud-byte-plugins
claude plugin install adp-enablement@cloud-byte-plugins
claude plugin install azure-platform-engineering@cloud-byte-plugins
claude plugin install gpu-research-platform@cloud-byte-plugins
claude plugin install model-training-ops@cloud-byte-plugins
claude plugin install inference-testing@cloud-byte-plugins
claude plugin install research-data-platform@cloud-byte-plugins
claude plugin install authoring@cloud-byte-plugins
claude plugin install ai-operations@cloud-byte-plugins
claude plugin install engineering-career@cloud-byte-plugins
claude plugin install ai-engineering@cloud-byte-plugins
claude plugin install prompt-workflows@cloud-byte-plugins
```

### GitHub Copilot
GitHub Copilot loads skills from `.github/skills/`, `.claude/skills/`, or `.agents/skills/` in your project. Copy the skill folders in:

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

### Google Gemini / Antigravity
```bash
npx skills add Cloud-Byte-Consulting/plugins -a gemini-cli
```
or copy skill folders into `.agents/skills/` or `.gemini/skills/`.

## Layout

```
.claude-plugin/marketplace.json     # Claude plugin marketplace manifest
docs/
├── README.md                       # generated plugin catalog
└── plugins/<plugin>.md             # generated skill inventory per plugin
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

Regenerate and verify the documentation after changing marketplace entries,
plugin manifests, or skill frontmatter:

```bash
python3 scripts/generate_plugin_docs.py
python3 scripts/generate_plugin_docs.py --check
```
