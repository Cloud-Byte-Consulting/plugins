# Plugin and skill documentation

This catalog is generated from the Claude marketplace, plugin manifests, and each skill's frontmatter. Edit those sources, then run `python3 scripts/generate_plugin_docs.py`.

| Plugin | Category | Focus | Skills | Codex manifest | Perplexity ZIPs |
|---|---|---|---:|:---:|---:|
| [`platform-assessment`](plugins/platform-assessment.md) | assessment | Assess an engineering org's platform and agentic readiness: ASDLC maturity scoring, platform ROI scorecard, org design, security/governance playbook, industry… | 9 | Yes | 9 |
| [`adp-enablement`](plugins/adp-enablement.md) | platform | Engineer the Agentic Developer Portal: CNCF platform-maturity benchmark with industry percentiles, MCP servers over platform APIs, agent identity (no standing secrets,… | 6 | Yes | 6 |
| [`azure-platform-engineering`](plugins/azure-platform-engineering.md) | platform | Azure implementation arm of the platform suite: read-only estate assessment (Resource Graph, azqr, Governance Visualizer, aztfexport) feeding assessment increment I9,… | 8 | — | — |
| [`gpu-research-platform`](plugins/gpu-research-platform.md) | platform | Operate GPU research workloads on managed Kubernetes (Lambda-class clouds): GPU sharing (MIG/MPS/time-slicing), KEDA autoscaling on DCGM metrics, cost chargeback,… | 7 | Yes | 7 |
| [`model-training-ops`](plugins/model-training-ops.md) | ml | Run model creation and training as a product: training pipeline architecture (Argo/Kubeflow, trigger taxonomy), MLflow experiment/registry standards,… | 6 | Yes | 6 |
| [`inference-testing`](plugins/inference-testing.md) | ml | Test and release models with evidence: model-level eval harnesses (synthetic ground truth, LLM-as-judge), GPU inference benchmarking (TTFT, tokens/sec, cost), release… | 6 | Yes | 6 |
| [`research-data-platform`](plugins/research-data-platform.md) | data | Make research data collection trustworthy without gatekeeping: ODCS data contracts with CI enforcement, dataset QoS/SLOs, data-product reviews (DAUTNIVS), right-sized… | 6 | Yes | 6 |
| [`authoring`](plugins/authoring.md) | writing | Turn research and interviews into publishable deliverables: evidence-first research briefs and interview-based case studies. | 2 | — | — |
| [`ai-operations`](plugins/ai-operations.md) | operations | Operate AI at work: model selection/routing, work-shape triage (chat/agent/team/nothing), agent output verification, cost/ownership/tool governance, and harness… | 5 | — | — |
| [`engineering-career`](plugins/engineering-career.md) | career | Engineering career coaching: senior/staff level-up behaviors, org signal reading, behavioral interview prep, AI-era positioning. | 1 | — | — |
| [`ai-engineering`](plugins/ai-engineering.md) | engineering | Ship production LLM apps: eval engineering (tracing, RAG metrics, LLM-as-judge, guardrails) and deployment (containers, cloud rollout, vector-store tuning). | 2 | — | — |
| [`prompt-workflows`](plugins/prompt-workflows.md) | productivity | Thirty-five reusable workflows for model routing, personal productivity, code comprehension, knowledge systems, agent evaluation, consumer AI strategy, and Office… | 35 | Yes | 35 |

## Related documentation

- [Getting started](../GETTING-STARTED.md)
- [Azure platform-engineering guide](../azure-platform-engineering/GUIDE.md)
- [Platform-engineering source notes](../PLATFORM-ENGINEERING-SOURCE-NOTES.md)
- [Research-division provenance](../RESEARCH-DIVISION-PROVENANCE.md)
- [Prompt-workflow provenance](../prompt-workflows/PROVENANCE.md)
