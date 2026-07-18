---
name: llm-eval-harness
description: >-
  Build model-level evaluation suites for correctness, quality, faithfulness,
  safety, and cross-version regression. Use for model eval harnesses, golden or
  synthetic datasets, BLEU/ROUGE/semantic metrics, LLM-as-judge calibration,
  checkpoint comparison, promotion thresholds, or converting red-team cases
  into durable tests. This skill evaluates model behavior; use the separate
  application-eval skill for production traces and RAG component telemetry.
---

# LLM Eval Harness

## Purpose
Turn "the new checkpoint feels better" into a measured, reproducible verdict a research team can gate a release on. This skill builds the eval suite that scores a *model* (or a model-backed component) against a curated dataset, isolates where it fails, tracks quality across versions, and hands its pass/fail thresholds forward as runtime guardrails and as the entry criterion for the release gate. It is the measurement backbone the other five skills consume.

Scope boundary — read this first. The sibling `ai-engineering:llm-evals-engineer` instruments a running LLM *application*: tracing spans, session scores, the RAG retriever-vs-generation metric split, live production scoring loops. This skill evaluates the *model itself* as the unit under test — the artifact a researcher trains, fine-tunes, or pulls from a hub and must certify before it enters the registry. When the question is "is my chatbot hallucinating in prod," route there. When it is "does checkpoint v7 regress on our safety set versus v6," stay here.

## Core model to hold in your head

### Six dimensions an eval suite must span
Before picking metrics, decide which behavioral dimensions the release cares about. Map every metric you add to one of these; a suite that scores only correctness certifies nothing about safety or style.
- **Correctness** — is the answer right, factually and functionally.
- **Consistency** — same input → same class of output; stable across paraphrases.
- **Style** — tone, format, and length adherence.
- **Security** — resists extraction and injection (the `genai-red-team` surface).
- **Ethics** — bias and harmful-content resistance.
- **Reputation** — would this output embarrass the research division if published.

### Model benchmarking as the baseline anchor
Before scoring your candidate, set the ceiling. Run a strong reference model (a large frontier model) over the same dataset to define an *ideal baseline*, then measure how close a smaller/cheaper candidate gets — the research question is usually "how much quality do we lose going smaller/faster." Public benchmarks (MMLU for knowledge, HellaSwag for common-sense, HumanEval for code, MATH for reasoning) are useful *capability anchors* to characterize a checkpoint, but they don't test *your* domain — build a domain benchmark styled after them for anything that gates a release. Different components warrant different judge models: an expensive, well-benchmarked model for the responder eval; a cheap fast one for a relevance-guardrail eval.

### The evaluation case
Every eval case is a triple plus tags: **Input**, **Reference** (the golden/ideal output, or a rubric — its absence makes the case *reference-free*), and **Metadata** (id, intent tag, source, severity). Cases live in CSV/JSON/Parquet under version control. A metric maps (input, output[, reference]) to a score, almost always normalized to **0–1**. A **binary** metric emits only 0/1; a **normalized** metric emits any value in [0,1] and needs a **minimum threshold** to become pass/fail (e.g. threshold 0.65 → 0.60 fails, 0.70 passes). Thresholds are the seam where offline evals become gates.

### Component vs end-to-end
A research model rarely ships alone — it sits inside a pipeline (retriever, guardrail, responder). Evaluate **each LLM-calling component** in isolation (swap it with confidence) *and* the **end-to-end** system (real-world behavior, integration, emergent failure). A component eval catches "the responder degraded"; an end-to-end eval catches "the responder is fine but the new prompt template broke the hand-off." Always run both; a green component suite with a red end-to-end suite is a wiring bug, not a model bug.

### Dataset construction — four sources, human always in the loop
| Source | What it gives you | Watch out for |
|---|---|---|
| **Common-input sample** | Representative real queries (mine top user/search queries) | Must cover main intents; ~100–200 cases for end-to-end |
| **Edge cases** | Security/ethical/boundary probes to optimize around | This is where releases actually fail |
| **Red-team-derived** | Adversarial cases harvested from `genai-red-team` findings | The highest-yield edge cases; feed the loop back |
| **Synthetic ground truth** | LLM-generated (Q, context, answer) triples when unlabeled | Vet and discard bad rows; costs real API spend |

Heuristics: **≥10 cases per metric**; **100–200 representative cases** for end-to-end confidence. LLMs are excellent at **perturbations** (rephrasings the model should answer consistently) — use them to expand coverage. Never auto-ingest user data without human review (PII strip, suitability).

### Synthetic ground truth (the no-labeled-data solution)
When a research corpus has no reference answers, generate them with Ragas `TestsetGenerator` (`generate_with_langchain_docs(docs, test_size=N, distributions=...)`). Mix three **evolution types** for question diversity: **simple** (direct), **reasoning** (requires inference), **multi_context** (needs multiple chunks). Use a strong **critic LLM** (e.g. a larger model) distinct from the generator to vet rows. Caveats that bite: requested `test_size` is a ceiling not a guarantee (failures reduce the count); every row costs LLM calls (budget it — a small run over a handful of examples with a six-metric suite still runs into thousands of calls); tiny synthetic sets give unreliable aggregates — do not over-read the numbers.

### Metric-selection matrix (the core decision)
| Metric class | Library | Measures | Valid when | Fails at |
|---|---|---|---|---|
| **BLEU** | `sacrebleu` | n-gram **precision** vs reference(s) | Translation, tightly-constrained output | Coherence, factuality, paraphrase (low BLEU ≠ wrong) |
| **ROUGE-1/2/L** | `rouge-score` | n-gram **recall/overlap** (precision, recall, f-measure) | Summarization of retrieved/reference text | Cannot detect a hallucination inside a fluent summary |
| **Semantic similarity** | embeddings + cosine | meaning-level closeness to reference | Paraphrase-tolerant correctness | Similar-worded-but-wrong answers can score high |
| **Assertion** | test framework | exact/regex/substring/comparison match | Deterministic outputs, classification labels | Anything open-ended |
| **LLM-as-judge** | judge model | qualitative criteria (tone, safety, recommendation present, PII leak) | No reference exists; human-scale judgment needed | Judge bias, cost, non-reproducibility if misconfigured |
| **Answer faithfulness** | `ragas` (`faithfulness`) | fraction of answer claims inferable from context | Hallucination detection against provided context | Needs context; empty context scores 0 |

Rule of thumb: statistical metrics (BLEU/ROUGE) are cheap directional signals **across versions** but "usually not sufficient" alone — they miss coherence, factual correctness, and appropriateness (ROUGE cannot detect a hallucination inside a fluent summary). Reserve LLM-as-judge for what only judgment can score. A worked signal to internalize: a case with low BLEU but high ROUGE means the output deviates from the golden answer yet adheres to the provided context — that points at the *retriever*, not the generator.

**Assertion metrics** are the cheapest and most reproducible — treat them like unit tests and wrap them in the existing test suite: equality/inequality, comparison operators, substring match, regex match. Use them for classification labels, structured fields, and any output with a deterministic expected value; they need no judge and never drift.

**Answer-relevance** (reference-free) works by having a judge generate candidate questions from the model's answer, embedding them alongside the original query, and scoring the mean cosine similarity — a relevant answer lets you reverse-engineer the original question. It is a strong guardrail candidate precisely because it needs no reference. Its quality depends on the judge's question-generation ability and degrades on complex multi-part queries.

### Human review — the gold standard and its limits
Human review remains the gold standard for qualitative dimensions and is the source of both your golden dataset and your judge's few-shot examples. Give reviewers a simple scale (pass/fail → 0/1, or 0–5 normalized) plus free-form comments, and record reviewer identity. Its limits are exactly why you build automated evals on top of it:
- **Cost** and **time** — expensive and slow per case.
- **Tedium** — reviewer attention degrades over a long run.
- **Elasticity** — doesn't scale to production volume.
- **Inconsistency** — the same reviewer scores the same case differently by mood or fatigue.

Use human review to seed the baseline, then tune the LLM judge toward it and reuse the human-scored cases as the judge's few-shot examples.

### LLM-as-judge construction rules (and its biases)
- **temperature 0**; one **single qualitative aspect per metric**; the **same judge model** across every run of a metric (you cannot compare scores from two different judges).
- **Multi-shot** (≥5 diverse examples) plus **chain-of-thought** (reason before verdict) materially improve accuracy. Emit **structured output** (pass/fail or 0–5) then normalize.
- Bias caveats: a judge inherits the same LLM limitations it grades; it can favor verbose or same-family outputs and can be swayed by phrasing. It is the best scalable option, never a perfect one. **Always hand-verify 3–5 judged cases** and confirm the written reasoning references the right text before trusting an aggregate.

### Regression suites across model versions
Freeze the dataset and metric config; run every candidate checkpoint through the identical suite; store per-metric baselines. A promotion is defensible only against a fixed baseline: block when any metric drops more than a set margin (e.g. >5%) below the incumbent, or when faithfulness falls under an absolute floor (e.g. 0.8). Hold out the tuning split from the gating split — never optimize against the numbers you gate on.

### Eval-as-guardrail (offline threshold → runtime gate)
Any **reference-free** metric (faithfulness, answer relevance, a policy judge) can be reused at runtime as a guardrail: the model responds only when the metric clears its threshold, else the app runs fallback logic. This extends the utility of an evaluation into a component of the application itself. The mechanics of the promotion:
- The **offline threshold** and the **runtime gate** share one definition — you author the number once.
- Only reference-free metrics qualify (no golden answer exists at serving time).
- The guardrail's live **pass-rate** becomes a monitored signal, so degradation is caught before users complain.

It is the direct handoff into `inference-rollout-strategist` (the threshold becomes a rollback trigger) and `drift-monitor-designer` (the pass-rate becomes a model-quality monitor).

## Workflow
1. **Frame the unit under test.** Model-level (checkpoint/fine-tune) or a specific component? List every LLM-calling component; decide component + end-to-end coverage.
2. **Build the dataset.** Assemble common inputs + edge cases + red-team-derived cases; generate synthetic ground truth (Ragas, mixed evolutions) if unlabeled; human-review every row; version it.
3. **Select metrics from the matrix.** One aspect per LLM-judge metric; add faithfulness for hallucination-sensitive work; keep BLEU/ROUGE only as cross-version directional signals.
4. **Wire and calibrate the judge.** temperature 0, multi-shot + CoT, fixed judge model; hand-verify judged samples against the reasoning text.
5. **Set baselines and thresholds.** Record per-metric baseline on the incumbent; define pass/fail margins and absolute floors; hold out the gating split.
6. **Run the regression suite per candidate.** Score every version identically; report deltas vs baseline; flag regressions by metric and by intent tag.
7. **Promote thresholds to guardrails.** Hand reference-free metric thresholds to the rollout and drift skills as runtime gates and monitored signals.

## Output spec
Deliver an **Eval Harness Report**: (1) unit under test + component/end-to-end scope; (2) dataset manifest — case counts by source and intent, synthetic-vs-human provenance, version hash; (3) metric suite with per-metric library, threshold, and rationale; (4) judge config + the hand-verification note; (5) results table — per-metric score per version with deltas vs baseline and pass/fail; (6) regression findings by intent tag; (7) the reference-free metrics promoted to guardrails, with their thresholds, handed to `inference-rollout-strategist` and `drift-monitor-designer`. Note the Lambda managed-Kubernetes / OSS context: judge and generator models run as in-cluster or Lambda-hosted endpoints; keep eval datasets and results in cluster object storage under version control.

## Siblings
`model-release-gate` (consumes this suite as its entry criterion) · `genai-red-team` (supplies red-team-derived cases; receives new failures) · `inference-rollout-strategist` (wires thresholds to rollback) · `drift-monitor-designer` (turns model-quality metrics into live monitors) · `ai-engineering:llm-evals-engineer` (application-level tracing/RAG evals — the complement, not this).
