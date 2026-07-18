# `research-data-platform`

[← Plugin catalog](../README.md) · [Repository README](../../README.md)

Make research data collection trustworthy without gatekeeping: ODCS data contracts with CI enforcement, dataset QoS/SLOs, data-product reviews (DAUTNIVS), right-sized governance with steward roles and certification, agent-consumable dataset catalogs, and lakehouse storage architecture for training data.

- Version: `1.0.0`
- Category: `data`
- Skills: 6
- Claude plugin: yes
- Codex plugin manifest: yes
- Perplexity packages: 6

## Skills

| Skill | Purpose | Perplexity |
|---|---|:---:|
| [`data-contract-author`](../../research-data-platform/skills/data-contract-author/SKILL.md) | Draft, review, and validate contracts for research training and evaluation datasets using ODCS, Data Contract CLI, or JSON Schema, with field-level sensitivity classification and semantic versioning. | [ZIP](../../research-data-platform/perplexity/data-contract-author.zip) |
| [`data-product-reviewer`](../../research-data-platform/skills/data-product-reviewer/SKILL.md) | Review whether a research dataset qualifies as a secure, usable data product using the DAUTNIVS attributes, evidence, API affordances, and source/consumer/aggregate archetypes. | [ZIP](../../research-data-platform/perplexity/data-product-reviewer.zip) |
| [`dataset-catalog-designer`](../../research-data-platform/skills/dataset-catalog-designer/SKILL.md) | Design an identity-aware dataset catalog or marketplace that supports human and agent discovery without leaking unauthorized metadata. | [ZIP](../../research-data-platform/perplexity/dataset-catalog-designer.zip) |
| [`dataset-qos-slo-designer`](../../research-data-platform/skills/dataset-qos-slo-designer/SKILL.md) | Define measurable dataset SLOs and executable quality checks for research training and evaluation data across accuracy, completeness, conformity, consistency, coverage, timeliness, and uniqueness. | [ZIP](../../research-data-platform/perplexity/dataset-qos-slo-designer.zip) |
| [`research-data-governance`](../../research-data-platform/skills/research-data-governance/SKILL.md) | Design right-sized research-data governance with steward roles, a lightweight council, policy-as-code, and certification that distinguishes hard-stop security/legal failures from visibility-only quality gaps. | [ZIP](../../research-data-platform/perplexity/research-data-governance.zip) |
| [`training-storage-architect`](../../research-data-platform/skills/training-storage-architect/SKILL.md) | Architect secure, reproducible training and evaluation storage on Kubernetes, including lakehouse zones, Iceberg/Delta/Hudi selection, MinIO or S3 access controls, snapshot retention, immutable materialized-input… | [ZIP](../../research-data-platform/perplexity/training-storage-architect.zip) |

## Plugin files

- [Claude manifest](../../research-data-platform/.claude-plugin/plugin.json)
- [Codex manifest](../../research-data-platform/.codex-plugin/plugin.json)
- [Skill source directory](../../research-data-platform/skills/)
