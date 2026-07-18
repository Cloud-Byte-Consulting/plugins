---
name: model-release-gate
description: The promotion gate a model must clear before it enters the registry's production stage — the go/no-go checkpoint for research inference testing. Use when the user says "release gate", "promotion gate", "model promotion checklist", "is this model safe to release", "pre-release audit", "explainability report", "SHAP/LIME for release", "fairness audit", "bias check before release", "adversarial robustness battery", "FGSM/C&W/PGD test", "robustness evaluation", "failure taxonomy", "hallucination/sycophancy/leakage triage", or "sign-off criteria". Covers an explanation report (SHAP/LIME method selection + compute-cost caveats), a fairness audit (metrics + counterfactual probes + pre/in/post mitigation selection), an adversarial-robustness battery (attack types, defenses, evaluation procedure), failure-taxonomy triage (hallucination, sycophancy, data leakage, cost/performance), and a gate checklist with pass/fail criteria and severity levels. For a research division on Lambda managed Kubernetes; OSS-first (SHAP, Fairlearn/AIF360, ART, Evidently). Consumes llm-eval-harness and inference-benchmark-runner results; sits before inference-rollout-strategist.
---

# Model Release Gate

## Purpose
Decide, with evidence and severity levels, whether a candidate model may advance from staging to the production stage of the registry. The gate aggregates the quality suite (`llm-eval-harness`), the performance benchmark (`inference-benchmark-runner`), and the red-team engagement (`genai-red-team`), then adds three release-specific audits that none of them produce: an **explanation report**, a **fairness audit**, and an **adversarial-robustness battery** — plus a **failure-taxonomy triage**. It emits a single go/no-go with a checklist, not a vibe. This is the ADP promotion checkpoint.

## Core model to hold in your head

### The gate has five inputs; this skill owns three of them
| Input | Produced by | Gate asks |
|---|---|---|
| Quality evals | `llm-eval-harness` | Did it clear thresholds vs the incumbent baseline? |
| Performance | `inference-benchmark-runner` | Does it meet the latency/throughput/cost SLO? |
| Red-team findings | `genai-red-team` | Any unresolved critical adversarial finding? |
| **Explanation report** | this skill | Is the model's behavior interpretable enough to trust? |
| **Fairness audit** | this skill | Does it treat protected groups equitably? |
| **Adversarial robustness** | this skill | Does it survive an attack battery? |

### Explanation report — method selection and compute cost
Pick the interpretation method by what you need to answer and what you can afford to compute. Getting this wrong wastes GPU-hours or produces misleading explanations.

| Method | Answers | Compute | Failure condition |
|---|---|---|---|
| **Permutation importance** | Global feature ranking | Cheap (no retraining) | Understates collinear features; shuffling makes out-of-distribution rows |
| **PDP / ICE** | Marginal effect of a feature | Moderate; sample for large data | Assumes feature independence → unrealistic simulated rows under correlation |
| **ALE** | Feature effect, distribution-aware | Faster than PDP, unbiased | Needs enough data per window; remove outliers for readability |
| **KernelSHAP** | Model-agnostic local + global attribution | **Expensive** (exponential in features; sample 0.5–2% of data) | Over-weights unlikely rows under multicollinearity |
| **TreeSHAP** | Attribution for tree models | Fast | Conditional-expectation form violates the Dummy property |
| **LIME** | Single-prediction local surrogate | Fast, all data types | Neighborhood-tuning sensitive; unstable run-to-run; local only |
| **Integrated Gradients / attention (BertViz, Captum)** | Token-level attribution for transformers | Moderate | Baseline choice matters; attention ≠ explanation on its own |

Selection rule: for a transformer/LLM release, lead with **token-level attribution** (Integrated Gradients via Captum, attention inspection via BertViz) plus **SHAP** for any tabular features or reward/router models; prefer **ALE over PDP** whenever features correlate; use **TreeSHAP** for gradient-boosted routers/scorers and reserve **KernelSHAP** for when you truly need model-agnostic fidelity and can pay for it. Always state the compute budget — KernelSHAP on a large test set is a real GPU/CPU cost, not free.

### Fairness audit — metrics, probes, mitigation
Detect disparate treatment across protected groups, probe it with counterfactuals, and select a mitigation at the right stage.

**Metrics** (compute per protected group; 0 or 1 = fair depending on metric):
- **Statistical Parity Difference (SPD)** — difference in favorable-outcome rate (0 = fair); **Disparate Impact (DI)** — its ratio form (1 = fair; the four-fifths / 80% rule flags DI < 0.8).
- **Equal Opportunity Difference (EOD)** — TPR gap between groups (0 = fair); **Average Odds Difference (AOD)** — average of FPR and FNR gaps.
- Compare per-group confusion matrices directly; a materially higher **FPR** for one group is the classic finding.

**Counterfactual probes** — "if the protected attribute (or a proxy) changed, does the outcome flip?" Use DiCE-style or prototype-guided counterfactuals (alibi `CounterFactualProto`), or a What-If-Tool sweep, to find minimal changes that flip the outcome; a flip driven by a protected attribute is a red flag. Watch the **Rashomon effect** — many valid counterfactuals exist, don't over-trust one.

**Mitigation — select by stage** (Fairlearn / AIF360):
- **Pre-processing** (fix the data): reweighing, disparate-impact remover, resampling/SMOTE, relabeling.
- **In-processing** (fix the training): exponentiated-gradient reduction, adversarial debiasing, prejudice remover, Gerry-fair classifier.
- **Post-processing** (fix the outputs): equalized-odds post-processing, calibrated equalized odds, reject-option classification.
Pick pre-processing when you own the data pipeline, in-processing when you control training, post-processing when you can only touch a frozen model's outputs. Note the trade-off: mitigation can cost predictive performance — quantify it, don't hide it.

### Adversarial-robustness battery
Run attacks, apply defenses, measure the accuracy-vs-attack-strength curve. Library: ART (`adversarial-robustness-toolbox`).

| Attack | Nature | Note |
|---|---|---|
| **FGSM** | Single-step gradient-sign perturbation | Fast; sweep `eps` for the strength curve |
| **PGD** | Iterative first-order adversary | Robustness vs PGD ⇒ robustness vs any first-order attack — the benchmark attack |
| **C&W (L∞)** | Optimization-based, minimal perturbation | Least detectable; tiny perturbation, large accuracy drop |
| **BIM** | Iterative FGSM | Used to generate examples for adversarial training |
| **Adversarial patch** | Universal, targeted, printable | Robust and hard to defend; needs detection/transformer defense |

Defenses (five families: preprocessing, training, detection, transformer, postprocessing — first four counter evasion):
- **Spatial smoothing** (preprocessing, median filter) — recovers a chunk of attacked accuracy cheaply.
- **Adversarial training** (`AdversarialTrainer`, `ratio` = fraction adversarial, generate with PGD/BIM) — most effective, but yields *empirical* not *certifiable* robustness and costs some clean accuracy.

**Evaluation procedure:** pick an attack (FGSM for speed), sweep a range of `eps` values including `eps=0` (clean baseline), regenerate adversarial examples against *each* candidate, record accuracy at each strength, and plot **accuracy vs attack strength** for base vs defended. Use a test-set *sample* — attacks/defenses/eval are resource-intensive. Report the eps range where the defended model wins and where it doesn't.

For LLMs specifically, the "attack battery" also includes the prompt-level adversarial suite from `genai-red-team` (injection, jailbreak); the ML-taxonomy view (training-time/causative vs exploratory, targeted vs indiscriminate) lives there — the gate consumes its critical-findings verdict.

### Failure-taxonomy triage
Classify every eval and red-team failure into the taxonomy, then triage by severity:
| Failure | Definition | Primary mitigation |
|---|---|---|
| **Hallucination** | Plausible but ungrounded/incorrect output | Faithfulness eval + RAG grounding; block on low faithfulness |
| **Sycophancy** | Matches user belief over truth (RLHF side-effect; worsens with scale) | Belief-conformity probes; note as release risk |
| **Data leakage** | Train/eval overlap or future info inflates metrics | Verify split hygiene; time-based split for temporal data |
| **Cost / performance** | Fails token-cost or latency budget | Route to `inference-benchmark-runner` numbers |

### Severity levels
- **Critical (block):** unresolved critical red-team finding; DI < 0.8 without accepted mitigation; faithfulness below floor; SLO miss on a hard latency SLO; data-leakage in the eval set (invalidates all quality numbers).
- **Major (block unless waived with owner sign-off):** notable robustness regression vs incumbent; significant fairness gap with a documented mitigation plan; sycophancy above tolerance.
- **Minor (ship with a tracked follow-up):** small perf-per-param regression, cosmetic explanation gaps.

## Workflow
1. **Gather the three upstream inputs.** Pull the eval report, the benchmark report, and the red-team engagement report; confirm each cleared its own bar first.
2. **Run the explanation report.** Select methods by the table; budget the compute; produce global + token-level attributions and a plain-language behavior summary.
3. **Run the fairness audit.** Compute the metric set per protected group; run counterfactual probes; if a gap exists, select and quantify a pre/in/post mitigation.
4. **Run the robustness battery.** FGSM/PGD/C&W (+patch where relevant); apply spatial smoothing / adversarial training; produce the accuracy-vs-strength curve.
5. **Triage failures.** Map every failure to the taxonomy and assign a severity.
6. **Score the checklist.** Every gate item gets pass / conditional-pass / fail with evidence; the release is go only if no Critical is open.
7. **Hand off.** Go → `inference-rollout-strategist` for the rollout design (with the rollback-trigger thresholds); No-go → back to `llm-eval-harness` / `genai-red-team` with the specific failing items.

## Output spec
Deliver a **Release Gate Decision**: (1) go/no-go headline with the blocking items if any; (2) upstream summary — eval, benchmark, red-team verdicts with links; (3) explanation report — methods used, compute spent, key attributions, behavior summary; (4) fairness audit — per-group metric table, counterfactual findings, selected mitigation + its performance cost; (5) robustness battery — attacks run, defenses applied, accuracy-vs-strength curve, empirical-not-certifiable caveat; (6) failure-taxonomy triage table with severities; (7) the gate checklist — every item pass/conditional/fail with evidence and severity; (8) rollback-trigger thresholds handed to `inference-rollout-strategist`. Note the Lambda managed-Kubernetes / OSS context: SHAP/Captum for explanations, Fairlearn/AIF360 for fairness, ART for robustness, results stored with the model version in the registry.

## Siblings
`llm-eval-harness` (quality input) · `inference-benchmark-runner` (performance input) · `genai-red-team` (adversarial input + ML taxonomy) · `inference-rollout-strategist` (receives a go + rollback thresholds) · `drift-monitor-designer` (the fairness and attribution audits become the bias-drift and feature-attribution-drift monitor baselines).
