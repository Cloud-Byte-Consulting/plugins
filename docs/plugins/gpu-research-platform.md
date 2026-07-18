# `gpu-research-platform`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Operate GPU research workloads on managed Kubernetes (Lambda-class clouds): GPU sharing (MIG/MPS/time-slicing), KEDA autoscaling on DCGM metrics, cost chargeback, researcher tenancy vending, GitOps bootstrap, CIS-derived security baseline with shared-responsibility filter, and GPU workload troubleshooting.

- Version: `1.0.0`
- Category: `platform`
- Skills: 7
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 7

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`gitops-platform-bootstrap`](../../gpu-research-platform/skills/gitops-platform-bootstrap/SKILL.md) | Design the Git repository structure and Argo CD architecture that runs a GPU research platform: app-of-apps bootstrap of platform add-ons (GPU operator, DCGM monitoring, KEDA, JupyterHub, model serving), ApplicationSet… | [ZIP](../../gpu-research-platform/perplexity/gitops-platform-bootstrap.zip) |
| [`gpu-autoscaling-engineer`](../../gpu-research-platform/skills/gpu-autoscaling-engineer/SKILL.md) | Author and validate autoscaling for GPU workloads on Kubernetes: KEDA ScaledObjects with DCGM + application-metric dual triggers, scale-to-zero, asymmetric scale-up/scale-down behavior for expensive GPU nodes, warm… | [ZIP](../../gpu-research-platform/perplexity/gpu-autoscaling-engineer.zip) |
| [`gpu-cost-optimizer`](../../gpu-research-platform/skills/gpu-cost-optimizer/SKILL.md) | Run GPU cost visibility, chargeback, and reduction for a research Kubernetes cluster: Kubecost/OpenCost per-namespace and per-label allocation, Goldilocks rightsizing, spot/preemptible-with-checkpointing decision… | [ZIP](../../gpu-research-platform/perplexity/gpu-cost-optimizer.zip) |
| [`gpu-sharing-advisor`](../../gpu-research-platform/skills/gpu-sharing-advisor/SKILL.md) | Decide between MIG, MPS, and time-slicing for sharing NVIDIA GPUs across Kubernetes workloads, and produce the config to implement the choice. | [ZIP](../../gpu-research-platform/perplexity/gpu-sharing-advisor.zip) |
| [`gpu-workload-troubleshooter`](../../gpu-research-platform/skills/gpu-workload-troubleshooter/SKILL.md) | Decision-tree diagnosis for GPU workloads on Kubernetes: pods stuck Pending with Insufficient nvidia.com/gpu, FailedScheduling, missing device plugin signatures, nodes that launch but never register GPUs, node pools… | [ZIP](../../gpu-research-platform/perplexity/gpu-workload-troubleshooter.zip) |
| [`k8s-security-baseline`](../../gpu-research-platform/skills/k8s-security-baseline/SKILL.md) | Run a CIS-derived security audit of a MANAGED Kubernetes cluster (Lambda or similar), scoped by shared responsibility: filter out provider-owned control plane checks (CIS sections 1-3), execute the customer-side… | [ZIP](../../gpu-research-platform/perplexity/k8s-security-baseline.zip) |
| [`researcher-tenancy-provisioner`](../../gpu-research-platform/skills/researcher-tenancy-provisioner/SKILL.md) | Stamp out researcher and project environments on a shared GPU Kubernetes cluster: namespace + ResourceQuota (including GPU quota via requests.nvidia.com/gpu) + LimitRange + RBAC role patterns + default-deny… | [ZIP](../../gpu-research-platform/perplexity/researcher-tenancy-provisioner.zip) |

## Plugin files

- [Claude manifest](../../gpu-research-platform/.claude-plugin/plugin.json)
- [Codex manifest](../../gpu-research-platform/.codex-plugin/plugin.json)
- [Skill source directory](../../gpu-research-platform/skills/)
