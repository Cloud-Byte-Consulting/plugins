# Prompt Workflows

Thirty-five portable Agent Skills for recurring knowledge-work tasks. Install the
plugin once or copy individual skill directories into any Agent Skills-compatible
tool.

## Skill groups

- **Model fit and routing (4):** choose a model or AI surface for a task.
- **Personal productivity (5):** audit open loops, delegate, automate, and brief.
- **Code comprehension (4):** explain unfamiliar systems and gate risky changes.
- **Knowledge systems (5):** design, synthesize, and audit durable knowledge bases.
- **Agent evaluation and packaging (7):** design judges and package workflows safely.
- **Consumer AI strategy (5):** evaluate products, markets, and anticipation gaps.
- **Office documents (5):** preserve evidence and truth across workbooks and decks.

Every skill retains its source-page link in `SKILL.md` and includes Codex UI metadata
under `agents/openai.yaml`. Publication and third-party handling are documented in
[`PROVENANCE.md`](PROVENANCE.md).

## Install

From the Cloud Byte Claude marketplace:

```bash
claude plugin marketplace add Cloud-Byte-Consulting/plugins
claude plugin install prompt-workflows@cloud-byte-plugins
```

For Codex, GitHub Copilot, Claude, Gemini, or another Agent Skills-compatible tool:

```bash
npx skills add Cloud-Byte-Consulting/plugins --full-depth -a codex
npx skills add Cloud-Byte-Consulting/plugins --full-depth -a github-copilot
```

## Perplexity Computer Skills

The `perplexity/` directory contains one upload-ready ZIP per skill. Each ZIP has
`SKILL.md` at its root and is capped at 10 MB.

Rebuild and verify them after changing a skill:

```bash
python3 prompt-workflows/scripts/package_perplexity.py
python3 prompt-workflows/scripts/package_perplexity.py --check
```
