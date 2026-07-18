# `model-training-ops`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Run model creation and training as a product: training pipeline architecture (Argo/Kubeflow, trigger taxonomy), MLflow experiment/registry standards, distributed-training topology selection (Ray/Dask/Spark), Ray on K8s operations, notebook-to-production golden path, and fine-tuning strategy (prompt vs RAG vs PEFT).

- Version: `1.0.0`
- Category: `ml`
- Skills: 6
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 6

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`distributed-training-advisor`](../../model-training-ops/skills/distributed-training-advisor/SKILL.md) | Choose a distributed-training topology and framework for GPU Kubernetes, including DDP/FSDP, data versus model parallelism, allreduce versus parameter servers, Ray/Dask/Spark selection, storage sharding, cost controls,… | [ZIP](../../model-training-ops/perplexity/distributed-training-advisor.zip) |
| [`experiment-registry-standard`](../../model-training-ops/skills/experiment-registry-standard/SKILL.md) | Define and enforce MLflow experiment and registry standards, including mandatory run metadata, naming and tags, promotion criteria, rollback, and a scalable tracking-server architecture. | [ZIP](../../model-training-ops/perplexity/experiment-registry-standard.zip) |
| [`finetuning-strategy-advisor`](../../model-training-ops/skills/finetuning-strategy-advisor/SKILL.md) | Decide among prompting, RAG, PEFT/LoRA, full fine-tuning, and continued pretraining, then design a response-masked PEFT workflow and Kubernetes training job. | [ZIP](../../model-training-ops/perplexity/finetuning-strategy-advisor.zip) |
| [`ml-pipeline-architect`](../../model-training-ops/skills/ml-pipeline-architect/SKILL.md) | Design automated ML training and retraining pipelines on Kubernetes with Argo Workflows or Kubeflow Pipelines, covering data validation, features, training, evaluation, registration, deployment, triggers, caching, and… | [ZIP](../../model-training-ops/perplexity/ml-pipeline-architect.zip) |
| [`notebook-to-production`](../../model-training-ops/skills/notebook-to-production/SKILL.md) | Move a Jupyter notebook into a tested, repeatable Kubernetes job by defining graduation criteria, removing hidden state, extracting modules, pinning environments, and adding data and pipeline tests. | [ZIP](../../model-training-ops/perplexity/notebook-to-production.zip) |
| [`ray-on-k8s-engineer`](../../model-training-ops/skills/ray-on-k8s-engineer/SKILL.md) | Stand up, secure, and operate KubeRay clusters and Ray workloads on GPU Kubernetes, including RayCluster, RayJob, RayService, Tune, autoscaling, MLflow, and Prometheus. | [ZIP](../../model-training-ops/perplexity/ray-on-k8s-engineer.zip) |

## Plugin files

- [Claude manifest](../../model-training-ops/.claude-plugin/plugin.json)
- [Codex manifest](../../model-training-ops/.codex-plugin/plugin.json)
- [Skill source directory](../../model-training-ops/skills/)
