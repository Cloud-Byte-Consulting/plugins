---
name: genai-red-team
description: Design and run an authorized, bounded red-team engagement for models and model-backed applications, then turn findings into defenses and regression cases. Use for prompt injection, jailbreaks, system-prompt extraction, adversarial testing, Giskard scans, attack-surface analysis, safety testing, blue-team mapping, or recurring live-endpoint tests with explicit scope, rate, spend, and stop controls.
---

# GenAI Red Team

## Purpose
Simulate a motivated adversary against a research model and the apps built on it, surface the vulnerabilities that a fixed eval set never triggers, and convert every finding into a durable eval case so the same attack can't regress in silence. Red teaming is the exploratory, adversarial complement to `llm-eval-harness`'s systematic coverage; its verdict is a required input to `model-release-gate`, and its findings are the highest-yield source of edge cases for the eval dataset. It runs before release (certify) and after (continuous adversarial pressure on the deployed model).

## Core model to hold in your head

### Why red-team at all — standard benchmarks don't test safety
Popular capability benchmarks measure what a model *can* do, not what it can be *made* to do — they leave the adversarial surface untested:
- **MMLU / HellaSwag / ARC** score knowledge, common-sense, and reasoning, but say nothing about toxicity, stereotype amplification, data disclosure, or misuse resistance.
- Red teaming, borrowed from cybersecurity, probes exactly that gap — throwing crafted, adversarial, real-world inputs at the system and recording what breaks. The failure modes are not hypothetical: publicly, a chatbot has been coaxed into absurd fabrications, a lawyer submitted six court cases an LLM invented wholesale, and an early public bot was manipulated into toxic output within a day. Each traces to a category below.

Model-backed RAG apps add their own surface. LLMs are effectively black boxes (low interpretability) and probabilistic next-token generators, so they hallucinate and can be steered; the mitigations to lean on — explainability, human-in-the-loop, a second-LLM reviewer, and PII/privacy controls — are the same blue-team defenses this skill maps below.

### Attack-surface categories (what to target)
Enumerate the surface before probing it — a red-team engagement scoped to only one category misses the others by construction:
| Category | Adversary goal | Example |
|---|---|---|
| **Bias & stereotypes** | Provoke biased/offensive output | Manipulate the model into a stereotyped answer → reputational harm |
| **Sensitive information disclosure** | Extract secrets | Leak the system prompt, private context, PII, or training data |
| **Service disruption** | Degrade availability | Long/crafted requests that exhaust resources for real users |
| **Hallucination induction** | Force confident wrong answers | Exploit the model's tendency to agree / fill gaps |

### Prompt-injection & jailbreak battery
- **Text completion** — exploit next-token prediction to continue an adversarial sequence.
- **Biased/loaded prompts** — implicit-bias framing to bypass content filters.
- **Direct prompt injection / jailbreak** — inject instructions that overwrite the system prompt and change behavior ("ignore previous instructions", fake "END OF INSTRUCTIONS / NEW INSTRUCTIONS" delimiters, all-caps emphasis, reformatting tricks like comma-to-exclamation substitution that ride the model's inclination to complete a task).
- **Gray-box attacks** — inject data assuming partial knowledge of the system prompt.
- **Prompt probing** — discover the system prompt itself first; a successful probe makes every other attack far more efficient (it feeds the gray-box attacks). Note: more capable models are often *more* vulnerable to complex probes because they follow the elaborate malicious instructions a weaker model can't parse — capability can be used against the model.

### Adversarial-ML taxonomy (classify every finding on three axes)
This is the structured lens for both LLM-level and model-level attacks; the release gate consumes it.
- **Influence:** **causative / training-time** attacks (poison the training data) vs **exploratory** attacks (probe/manipulate the deployed model at inference). Prompt injection is exploratory; data poisoning is causative.
- **Security goal violated:** **integrity** (slip malicious input past a detector — induced false negatives), **availability** (drown real signal in noise — caused false positives / service disruption), **privacy/confidentiality** (extract information about the system or its users — membership/attribute inference, model inversion, prompt/data leakage).
- **Specificity:** **targeted** (a specific input or victim) vs **indiscriminate** (any failure will do). 
Placing a finding on all three axes tells you how severe it is and which defense family applies.

### Automated red-teaming loops
Manual probing doesn't scale to a research team's release cadence — automate it:
- **Manually-defined probe list** — a curated set of injection strings; loop through, auto-detect successful injections by output inspection.
- **Prompt library** — a maintained corpus of known injection/jailbreak prompts; requires keeping it current as new techniques appear.
- **Continually-updated scanners** — e.g. Giskard's OSS **LLM scan** runs specialized tests (including prompt injection), analyzes outputs for failures, and generates an attack-vector report. Run it as a scheduled K8s Job against the candidate endpoint.
- Build the plan from OWASP Top 10 for LLM Applications, the AI Incident Database, and the AI Vulnerability Database (AVID).

### Before-release vs post-release engagements
Run only with written authorization, named targets, allowed techniques, and an incident contact. Default to staging with synthetic test accounts and data. For any approved live test, set rate/concurrency ceilings, a spend cap, monitoring, a kill switch, and explicit stop conditions; never probe paths that could retrieve or modify real users' data.

The same battery runs in two modes with different goals:
- **Before release (certification).** Run the full battery against the staging checkpoint; the critical-findings verdict is a hard input to `model-release-gate`. A model with an open critical finding does not promote. This is where the taxonomy severity assignment matters most.
- **After release (continuous pressure).** Schedule automated scans against the live endpoint; new jailbreaks and injection techniques emerge constantly, so a model that was clean at release can become vulnerable to a newly-published attack. Post-release findings feed `inference-rollout-strategist`'s rollback triggers and reopen the gate for the next version.
Model-level attacks (data poisoning, membership/attribute inference, model inversion) are exploratory-vs-causative distinctions that mostly apply before release, at training time; the deployed-endpoint work is overwhelmingly exploratory (injection, jailbreak, probing, disclosure).

### Blue-team defense mapping
Map each attack to a defense; report both the finding and the fix.
| Attack | Blue-team defense |
|---|---|
| Secret/key exposure | Secrets in `.env` / K8s Secrets, `.gitignore`, key rotation on breach |
| Prompt injection / probing | A **second-LLM guardian**: score question-vs-context relevance (1–5); if below a threshold (e.g. < 4) return a canned "I don't know" instead of answering — this blocks probes that score as irrelevant while passing legitimate queries |
| Disclosure / bias | Input guardrails, output filters, human-in-the-loop review, curated high-quality sources, citations for auditability |
| Service disruption | Rate limits, input-length caps, resource quotas |
| Model-level (poisoning/inference) | Training-data provenance, adversarial training (via `model-release-gate` battery), differential-privacy where applicable |
Defenses complement good prompts; they don't replace them. Security is iterative — red team, defend, re-red-team.

The **guardian LLM** pattern deserves spelling out because it is the highest-leverage single defense for a research endpoint:
- Run a hidden second call that scores relevance of the user question against the retrieved context on a **1–5 scale**.
- Parse the score defensively — default to 0 on a parse error.
- Below the cutoff (e.g. < 4), return a canned refusal instead of the real answer.
- Result: a prompt-probe that tries to extract the system prompt scores as irrelevant and is blocked, while a legitimate question scores high and passes — one extra call converts most injection attempts into a harmless "I don't know."

Beyond it, the standing posture is access controls, encryption in transit and at rest, curated sources, and citations for auditability; no checklist is exhaustive, so treat the red-team↔blue-team cycle as continuous.

### Severity classification for findings
Rate every finding so the gate can act on it, matching `model-release-gate`'s severity bands:
- **Critical** — reliable system-prompt/context extraction, PII or training-data disclosure, a jailbreak that defeats the safety layer, or a data-poisoning path. Blocks release; trips a live rollback.
- **Major** — inconsistent bias/stereotype elicitation, a partial disclosure, or a denial-of-service vector under crafted input. Blocks unless waived with a documented mitigation.
- **Minor** — a probe that only works with implausible setup, or one the guardian layer already catches. Ship with a tracked follow-up and a new eval case.
Weight severity by the three-axis taxonomy: a **privacy** violation that is **targeted** and **exploitable at inference** is worse than an **indiscriminate integrity** nuisance.

### The feedback loop (the point of the whole exercise)
A red-team engagement that ends in a report and nothing else has skipped its most valuable output. Every confirmed finding fans out to three destinations:
- **`llm-eval-harness`** — becomes a red-team-derived eval case (captured input, the failure it triggered, the expected safe behavior) so the regression suite catches it forever after.
- **The probe library** — updates the automated-scan corpus so future runs test for this technique by default.
- **`model-release-gate`** — the critical-findings verdict gates the next promotion.

## Workflow
1. **Authorize and scope the engagement.** Record owner approval, exact targets, allowed techniques, test identities/data, environment, rate/concurrency and spend limits, kill switch, incident contact, stop conditions, and whether the work is pre-release or post-release.
2. **Assemble the battery.** Build the injection/jailbreak/probe set from the categories above plus OWASP/AVID/incident-DB references; wire an automated scanner (Giskard LLM scan) as a K8s Job.
3. **Attack.** Run manual crafted probes and the automated suite against the endpoint; capture every input, output, and success/fail.
4. **Classify each finding** on the three taxonomy axes (influence, security goal, specificity) and assign severity.
5. **Map defenses.** For each finding, specify the blue-team fix (guardian LLM, input guardrail, rate limit, provenance, etc.) and re-test after the fix.
6. **Close the loop.** Convert findings to eval cases in `llm-eval-harness`; update the probe library; deliver the critical-findings verdict to `model-release-gate`.

## Output spec
Deliver a **Red-Team Engagement Report**: (1) scope — target, attack-surface categories, before/after-release; (2) methodology — manual battery + automated scanner config; (3) findings table — each finding with the triggering input, the failure, the three-axis taxonomy classification, and a severity; (4) the critical-findings verdict handed to `model-release-gate` (block / conditional / clear); (5) blue-team defense mapping — fix per finding and re-test result; (6) the feedback-loop actions — the new red-team-derived eval cases handed to `llm-eval-harness` and the probe-library updates. Note the Lambda managed-Kubernetes / OSS context: run the automated scanner and probe harness as in-cluster Jobs against the model endpoint; keep the probe library and findings in cluster object storage under version control.

## Siblings
`model-release-gate` (receives the critical-findings verdict + feeds the ML-taxonomy view into the robustness battery) · `llm-eval-harness` (receives red-team-derived eval cases — closes the loop) · `inference-rollout-strategist` (post-release red-team findings can trip a rollback trigger) · `drift-monitor-designer` (a spike in guardian-LLM blocks is a monitorable adversarial-pressure signal).
