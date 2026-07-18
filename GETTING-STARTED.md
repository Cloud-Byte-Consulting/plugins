# Getting Started

If you installed `platform-assessment` and `authoring`, you now have 11 skills. Don't try to use all of them this week. This guide gives you a starting point, a growth path, and a quarterly rhythm — each stage produces something useful on its own and feeds the next. The separate `prompt-workflows` plugin has its own [guide](prompt-workflows/README.md).

> **Running the maturity assessment?** See the dedicated [ASSESSMENT-GUIDE.md](ASSESSMENT-GUIDE.md) for setup instructions, the read-only permissions matrix, and how to split the assessment into increments across roles when no single person has all the access.

## Which skill do I need right now?

| You're asking... | Use |
|---|---|
| "Where do we actually stand with platform and agentic maturity?" | `assessment-orchestrator` |
| "How mature are our agentic delivery paths specifically?" | `asdlc-maturity-assessment` |
| "We can't get all the access / need to split assessment work between people" | `assessment-orchestrator` |
| "Is the platform worth the money? How do I prove it?" | `platform-roi-scorecard` |
| "How should the platform team be structured / who owns AI?" | `platform-org-design-advisor` |
| "Are our coding agents safe/compliant/auditable?" | `platform-security-playbook` |
| "What are peers in our industry doing?" | `platform-industry-brief` |
| "What should the platform look like in 2 years?" | `idp-adp-architect` |
| "Make this presentable to leadership" | `platform-assessment-reporter` |
| "Turn this research pile into a brief" | `research-brief-writer` |
| "Write up this interview/customer call" | `interview-case-study-writer` |

## The growth path

Four stages. Each takes roughly one iteration of effort and unlocks the next. You can stop after any stage and still have gained something.

### Stage 1 — Baseline (first session, ~1 hour)

**Goal: know where you stand, and discover what you can't yet measure.**

Start by chartering a bounded assessment and identifying what can be measured now. First prompt to try:

> Use assessment-orchestrator to plan a pilot for [value stream / 2–3 teams]. Map the access we already hold to runnable increments, create the assessment state, and list every source and formal result that must remain Pending.

What you get: a permission-scoped evidence plan, initial coverage, and — most valuable — a list of things the assessment *cannot yet verify*. That list is your Stage 2 work. Formal maturity results remain Pending until their scorer prerequisites are met.

Optional same-session add-on:

> Using platform-assessment-reporter, show separate qualitative platform, ASDLC, and ADP evidence-coverage views. Do not assign formal stages or combine them into one number.

**Expect mostly hatched/qualitative output here. That's the point.** A first baseline that admits fuzziness is honest; the growth path is turning hatched into solid.

### Stage 2 — Measure (weeks 2–6)

**Goal: replace self-report with system data.**

1. **Wire evidence sources.** Connect what you have — GitHub MCP or Azure DevOps MCP (PRs, pipelines), Atlassian MCP (work items), your cloud's MCP server (resources/cost). The skills know how to use them and will tell you which caveats apply.
2. **Run a 2–4 week observation window.** Don't change anything yet — collect: deploy frequency, lead time, PR merge rates, agent-PR attribution, onboarding time of the last few hires.
3. **Run the authorized assessment increments** with connectors live:

> Use assessment-orchestrator to run the authorized increments through read-only connectors. Merge the evidence, then invoke the formal scorers only where their prerequisites are satisfied. Compare coverage with Stage 1.

4. **Start the ROI baseline:**

> Using platform-roi-scorecard, design our measurement program: pick metrics for our maturity stage, design the developer survey (doers, 20–25 min), and set the baseline from the observation window. We'll re-measure quarterly.

Common trap at this stage: agent attribution. If agent-generated work is invisible in your history (squash merges erase it), the assessment will refuse to score L2+ — correctly. Fixing attribution *is* the improvement.

### Stage 3 — Report and decide (end of quarter 1)

**Goal: one leadership decision, backed by evidence.**

> Using platform-assessment-reporter, build the exec readout from our assessment and ROI data: separate platform, ASDLC, and ADP radar profiles; adjacent evaluation ledgers; stable citations; confidence; and a before/after ledger. Add the "what we could not measure" note per chart.

Then pick **one or two gaps** — not five. Typical first picks:

- Structural gap (paths undefined, no validation loop) → `idp-adp-architect` for target design
- Ownership/staffing gap → `platform-org-design-advisor`
- Agents scaling faster than controls, or regulated environment → `platform-security-playbook` (do this one *before* scaling agent autonomy, not after)
- Leadership asks "what do peers do?" → `platform-industry-brief`

Write it up: `research-brief-writer` turns the quarter's findings into a brief; keep the reporter's evidence appendix attached.

### Stage 4 — Operate the loop (quarterly)

**Goal: gradual, compounding improvement.**

Each quarter:

1. Re-run the assessment with the same queries (the reporter's reproduction notes make quarters comparable).
2. Update the radar — the win condition is **hatched axes turning solid** and scores moving, in that order. Measurement quality improves before the scores do; that's normal and worth showing.
3. Ship the delta readout to leadership: what moved, what didn't, what we changed, what's next.
4. Pick the next one or two gaps. Level jumps take multiple quarters — L1→L2 is the hardest transition (dispatch, sandboxes, validation loops); don't promise it in one.

## Anti-patterns

- **Running all 11 skills in week one.** Baseline → measure → report → iterate. The skills cross-reference each other and will route you when it's time.
- **Scoring optimistically.** The assessment skills are built to demand evidence; fighting that produces a pretty chart and a wrong roadmap.
- **All-solid charts from a low-maturity org.** If nothing renders as qualitative, the measurement is lying. Missing measurement is a finding.
- **Chasing L3/L4 from L1.** Build L2 capabilities first; L4 is explicitly non-scoreable — treat it as direction, not destination.
- **Vendor numbers as evidence.** Benchmarks calibrate expectations; only your own baseline proves your improvement.

## Cadence summary

| When | Do | Skills |
|---|---|---|
| Day 1 | Charter, permissions map, and evidence plan | assessment-orchestrator (+ reporter for a coverage view) |
| Weeks 2–6 | Run increments, observe, and score supported domains | orchestrator, discovery, formal scorers, roi-scorecard |
| Quarter end | Exec readout, pick 1–2 gaps | reporter, then architect / org-design / security / industry-brief |
| Every quarter | Re-run, compare, ship delta, next gap | the loop above |
