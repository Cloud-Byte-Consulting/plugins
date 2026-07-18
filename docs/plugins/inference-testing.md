# `inference-testing`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Test and release models with evidence: model-level eval harnesses (synthetic ground truth, LLM-as-judge), GPU inference benchmarking (TTFT, tokens/sec, cost), release gates (explainability, fairness, adversarial robustness), rollout strategies (shadow/canary/bandit), 4-monitor drift stack, and GenAI red-teaming.

- Version: `1.0.0`
- Category: `ml`
- Skills: 6
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 6

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`drift-monitor-designer`](../../inference-testing/skills/drift-monitor-designer/SKILL.md) | Design privacy-safe post-deployment monitoring for data, concept, prediction, bias, and feature-attribution drift on Kubernetes. | [ZIP](../../inference-testing/perplexity/drift-monitor-designer.zip) |
| [`genai-red-team`](../../inference-testing/skills/genai-red-team/SKILL.md) | Design and run an authorized, bounded red-team engagement for models and model-backed applications, then turn findings into defenses and regression cases. | [ZIP](../../inference-testing/perplexity/genai-red-team.zip) |
| [`inference-benchmark-runner`](../../inference-testing/skills/inference-benchmark-runner/SKILL.md) | Benchmark model-inference latency, throughput, GPU efficiency, and cost on Kubernetes without conflating performance with answer quality. | [ZIP](../../inference-testing/perplexity/inference-benchmark-runner.zip) |
| [`inference-rollout-strategist`](../../inference-testing/skills/inference-rollout-strategist/SKILL.md) | Choose and design a safe production rollout for model inference on GPU Kubernetes, including shadow, canary, blue-green, A/B, and bandit strategies. | [ZIP](../../inference-testing/perplexity/inference-rollout-strategist.zip) |
| [`llm-eval-harness`](../../inference-testing/skills/llm-eval-harness/SKILL.md) | Build model-level evaluation suites for correctness, quality, faithfulness, safety, and cross-version regression. | [ZIP](../../inference-testing/perplexity/llm-eval-harness.zip) |
| [`model-release-gate`](../../inference-testing/skills/model-release-gate/SKILL.md) | Produce an evidence-based go or no-go model-release decision from quality, performance, fairness, explainability, authorized red-team, and empirical robustness results. | [ZIP](../../inference-testing/perplexity/model-release-gate.zip) |

## Plugin files

- [Claude manifest](../../inference-testing/.claude-plugin/plugin.json)
- [Codex manifest](../../inference-testing/.codex-plugin/plugin.json)
- [Skill source directory](../../inference-testing/skills/)
