# Getting Started

If you installed `platform-assessment` and `authoring`, you now have 9 skills. Don't try to use all of them this week. This guide gives you a starting point, a growth path, and a quarterly rhythm — each stage produces something useful on its own and feeds the next. The separate `prompt-workflows` plugin has its own [guide](prompt-workflows/README.md).

## Which skill do I need right now?

| You're asking... | Use |
|---|---|
| "Where do we actually stand with platform/AI-agent maturity?" | `asdlc-maturity-assessment` |
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

Start with a quick maturity read. First prompt to try:

> Run a quick asdlc-maturity-assessment scan of our org. We have [N devs], use [GitHub/Azure DevOps/GitLab + Jira/ADO Boards], and agents are used for [autocomplete / PR generation / not at all]. Score conservatively from what I can tell you; list every score you had to mark as unverified.

What you get: a provisional level (most orgs land L1), a path-by-path read, and — most valuable — a list of things the assessment *couldn't verify*. That list is your Stage 2 work.

Optional same-session add-on:

> Using platform-assessment-reporter, place us on the production-system quadrant from what we discussed. Mark everything qualitative — this is a hypothesis, not a measurement.

**Expect mostly hatched/qualitative output here. That's the point.** A first baseline that admits fuzziness is honest; the growth path is turning hatched into solid.

### Stage 2 — Measure (weeks 2–6)

**Goal: replace self-report with system data.**

1. **Wire evidence sources.** Connect what you have — GitHub MCP or Azure DevOps MCP (PRs, pipelines), Atlassian MCP (work items), your cloud's MCP server (resources/cost). The skills know how to use them and will tell you which caveats apply.
2. **Run a 2–4 week observation window.** Don't change anything yet — collect: deploy frequency, lead time, PR merge rates, agent-PR attribution, onboarding time of the last few hires.
3. **Re-run the maturity assessment** with connectors live:

> Re-run asdlc-maturity-assessment. Pull evidence via the connected MCP servers instead of asking me. Compare against the Stage 1 baseline and show which unverified scores are now evidence-backed.

4. **Start the ROI baseline:**

> Using platform-roi-scorecard, design our measurement program: pick metrics for our maturity stage, design the developer survey (doers, 20–25 min), and set the baseline from the observation window. We'll re-measure quarterly.

Common trap at this stage: agent attribution. If agent-generated work is invisible in your history (squash merges erase it), the assessment will refuse to score L2+ — correctly. Fixing attribution *is* the improvement.

### Stage 3 — Report and decide (end of quarter 1)

**Goal: one leadership decision, backed by evidence.**

> Using platform-assessment-reporter, build the exec readout from our assessment and ROI data: quadrant placement, six-vector radar with confidence tiers, and a before/after ledger for anything we changed. Add the "what we could not measure" note per chart.

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

- **Running all 9 skills in week one.** Baseline → measure → report → iterate. The skills cross-reference each other and will route you when it's time.
- **Scoring optimistically.** The assessment skills are built to demand evidence; fighting that produces a pretty chart and a wrong roadmap.
- **All-solid charts from a low-maturity org.** If nothing renders as qualitative, the measurement is lying. Missing measurement is a finding.
- **Chasing L3/L4 from L1.** Build L2 capabilities first; L4 is explicitly non-scoreable — treat it as direction, not destination.
- **Vendor numbers as evidence.** Benchmarks calibrate expectations; only your own baseline proves your improvement.

## Cadence summary

| When | Do | Skills |
|---|---|---|
| Day 1 | Quick baseline scan | maturity-assessment (+ reporter) |
| Weeks 2–6 | Connect evidence, observe, re-baseline | maturity-assessment, roi-scorecard |
| Quarter end | Exec readout, pick 1–2 gaps | reporter, then architect / org-design / security / industry-brief |
| Every quarter | Re-run, compare, ship delta, next gap | the loop above |
