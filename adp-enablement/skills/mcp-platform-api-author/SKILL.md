---
name: mcp-platform-api-author
description: >-
  Design and build MCP (Model Context Protocol) servers that expose internal
  platform capabilities - job submission, cluster status, GPU quota, dataset
  catalogs, deploy actions - as tools AI agents can discover, select, and call
  safely. Use whenever the user wants to build an MCP server, wrap a platform
  API for agents, expose Kubernetes or cloud capabilities to Claude or LLM
  agents, choose STDIO vs StreamableHTTP transport, write tool schemas and
  descriptions, design tool naming conventions, scope permissions per tool,
  insert guardrails, make agents pick the right tool, handle tool failures
  with fallbacks and circuit breakers, test or version an MCP server, or asks
  about FastMCP, tool calling surfaces, "AI-ready APIs", or an agent gateway
  to the platform. Disambiguation - the sibling idp-adp-architect skill
  (platform-assessment plugin) decides WHERE the agent interface sits in the
  five-plane architecture; this skill ENGINEERS the MCP surface itself. For
  the REST/OpenAPI contract underneath, use sibling
  agent-api-contract-designer; for the credential the server runs as, use
  sibling agent-identity-engineer.
---

# MCP Platform API Author

## Purpose
Give agents a first-class, governed doorway into the platform. Every context source hand-wrapped per agent is duplicated work that doesn't scale; MCP standardizes the surface once so any host can subscribe. This skill takes a platform capability inventory (for a GPU-cloud research division: submit training job, query cluster/queue status, check GPU quota, browse the dataset catalog, deploy/rollback an endpoint) and produces a designed, permission-scoped, guardrailed, testable MCP server. The hard rule inherited from the reference architecture: agent-triggered infra changes execute through the governed platform API or CLI — the MCP server is a front door to the orchestrator, never a side door around it.

## Core model to hold in your head

### MCP architecture and transport selection
Classic client-server: the **host** process (the agent application) runs an **MCP client** per connection; each **MCP server** exposes a set of tools (plus optionally prompts and resources). Tools from MCP servers integrate into the agent identically to local tools — same tool-calling protocol — so a well-architected agent needs no logic changes to adopt them.

| Transport | Use when | Notes |
|---|---|---|
| **STDIO** (local subprocess) | Development; tools over local resources (files, kubeconfig) | Inherits the user's local credentials — fine for a researcher's laptop, wrong for shared platform capabilities |
| **StreamableHTTP** (remote) | Production platform surfaces | The default for an ADP: centrally deployed, centrally authenticated (OAuth2 client credentials per agent — see `agent-identity-engineer`), centrally versioned and observable |

Build with the current FastMCP (v2 line) or the language-native MCP SDK; a tool is a typed function + schema + description. The engineering is not the framework — it's the tool design below.

### Tool design rules (design for the selection funnel)
Agents pick tools through a **selection funnel** with three stages:
1. **Intent classification** — coarse category filter that prunes the search space.
2. **Embedding/semantic ranking** — the request is matched against tool name + description + parameter names, discarding candidates below a confidence threshold.
3. **Deterministic constraint filtering** — type checks, caller permissions, and the tool's historical failure status prune the shortlist to one executable choice.

Design every tool so the funnel selects it correctly:
- **Naming:** `verb_object` in the platform's domain vocabulary (`submit_training_job`, `get_gpu_quota`, `list_datasets`, `rollback_endpoint`). One capability per tool; no `do_platform_action(action=...)` dispatchers — they defeat all three funnel stages and make per-tool permissioning impossible.
- **Descriptions are retrieval documents.** The description is what the embedding stage ranks. Front-load what the tool does, when to use it, and when NOT to ("use `get_job_status` for a single job; use `list_jobs` to search"). Sibling tools must be contrastive, or the funnel coin-flips between them.
- **Schemas:** strict typed parameters, enums over free strings (`gpu_type: enum[a100, h100, gh200]`), defaults for everything optional, no parameter the agent must guess. Constrained schemas ARE the first guardrail — an invalid call fails at validation, before the platform.
- **Constraint metadata:** annotate each tool with required scope, read-only vs mutating, cost class, and rate class, so the funnel's third stage (and your gateway) can filter on permissions and failure history without invoking anything.

### Error surfaces agents can recover from
A tool result is context for the next model turn — design errors as instructions, not stack traces. Every error returns a machine-readable code, what was wrong, and what to do next (`QUOTA_EXCEEDED: requested 8xH100, quota 4. Retry with gpus<=4 or call request_quota_increase`). Never leak internals (connection strings, node names, other tenants' jobs) — the non-leaking-errors discipline from the API threat checklist in `agent-api-contract-designer` applies verbatim. Classify failures and wire recovery into the server, not into every agent:
- **Safe wrappers** — timeouts, input validation, structured error capture around every downstream call.
- **Fallback chains** — degraded alternatives (live cluster status unavailable → last-known snapshot, explicitly marked stale).
- **Circuit breakers + failure memory** — repeated failures open the circuit and surface `TOOL_UNAVAILABLE` immediately; the funnel's constraint stage reads this short-term failure memory to route around the tool, then re-enters the funnel for a fallback tool.
- **Retry discipline** — retries with backoff for transient classes only; never auto-retry mutating calls without idempotency keys.

### Permission scoping and guardrail insertion
Scope per-tool, not per-server: the server authenticates the calling agent identity, then enforces tool-level scopes (`jobs:read`, `jobs:submit`, `deploy:execute`).
- Read-only tools: cheap to grant.
- Mutating tools: require the narrow scope.
- Destructive tools (delete dataset, scale-to-zero): additionally require a human-approval flow, or are simply not exposed to autonomous callers.

Guardrails come in three types — **rule-based** (conditions/regex), **retrieval-based** (checks against approved sources), **model-based** (classifier/moderation models) — inserted at four points:
- **Pre-model** (host-side input checks) and **post-model** (output filtering) — useful, but outside your control.
- **Routing-stage** — should this query reach this tool category at all.
- **Tool-level, inside the server** — argument policy checks, namespace confinement, quota enforcement. This is the only layer the platform team fully controls, so it is the load-bearing one.

Log every call with agent identity, arguments, decision, and outcome into the same audit plane as human actions (`agent-identity-engineer` owns that plane).

### Testing and versioning an MCP server
Test at three levels:
1. **Direct client tests** — drive the server with an MCP client harness (e.g., FastMCP's client) asserting schema validity, error contracts, and permission denials per tool.
2. **Selection tests** — given a corpus of realistic researcher/agent requests, assert the funnel picks the intended tool. Description regressions are real regressions — treat description text as versioned API surface.
3. **Agent-in-the-loop evals** — scripted end-to-end tasks ("submit a 2-GPU smoke-test job and report queue position") scored pass/fail in CI.

Version like an API for uncoupled consumers: additive **expansion changes** (new tools, new optional params) are safe; renames, removals, and semantic changes are breaking — run old and new tools side by side with a deprecation window, and semver the server so hosts can pin. These become consumer-driven contract fitness functions in `platform-fitness-functions`.

## Workflow
1. **Inventory capabilities.** For [YOUR ORGANIZATION / CLIENT], list the platform capabilities agents need, sourced from the golden paths (`golden-path-designer`) and the gap register (`platform-maturity-benchmark`). For a managed-K8s GPU research platform, the canonical starter set: `submit_training_job`, `get_job_status`, `list_jobs`, `cancel_job`, `get_cluster_status`, `get_gpu_quota`, `request_quota_increase`, `list_datasets`, `get_dataset`, `deploy_endpoint`, `rollback_endpoint`.
2. **Classify each tool:** read-only / mutating / destructive; cost class; required scope; autonomous-callable or approval-gated.
3. **Design the tool cards.** Per tool: name, contrastive description, typed schema with enums/defaults, error catalog with recovery hints, scope, rate class. Review the card set as a whole against the funnel: could an embedding ranker distinguish every pair? Example card:

   | Field | Value |
   |---|---|
   | name | `submit_training_job` |
   | description | Submit a containerized training job to the research cluster. Use for NEW runs; use `get_job_status`/`cancel_job` for existing runs. Queues if GPUs unavailable. |
   | schema | `image:str`, `gpus:int<=quota`, `gpu_type:enum[a100,h100,gh200]`, `dataset_id:str`, `priority:enum[normal,preemptible]=preemptible`, `idempotency_key:str` |
   | classification | mutating; scope `jobs:submit`; cost-class high; rate 10/min |
   | errors | `QUOTA_EXCEEDED` (retryable_with_change), `DATASET_NOT_FOUND` (not_retryable), `QUEUE_FULL` (retryable_after) |
4. **Choose transport and topology.** StreamableHTTP behind the platform gateway for shared capabilities; STDIO only for local-resource dev tools. One server per platform domain (jobs, data, serving) rather than one mega-server — domain servers keep scopes and versioning tractable.
5. **Implement** on FastMCP/SDK: safe wrappers, fallback chains, circuit breakers with failure memory, tool-level guardrails, structured audit logging. All mutations route through the orchestrator/platform API — never raw cloud calls.
6. **Test** at all three levels; wire the selection-test corpus and contract tests into CI.
7. **Version and publish:** semver, deprecation policy, internal registry entry, and a changelog agents' owners can subscribe to.
8. **Output.** An MCP surface spec: tool-card table, transport/topology diagram, scope matrix, guardrail insertion map, error catalog, test plan, and versioning policy — plus skeleton server code if the user wants implementation.

## Guardrails
- Never expose a capability over MCP that bypasses the governed platform path — if the CLI/orchestrator API can't do it, the MCP server must not either.
- No god-tools: one capability per tool, per-tool scopes, or permissioning and selection both degrade.
- The agent is an untrusted caller: validate inside the server, never trust host-side validation (`agent-api-contract-designer` carries the full threat checklist).
- Errors must instruct recovery and must not leak internals or other tenants' state.
- Description text is API surface — changes go through review and selection-regression tests.
- Destructive actions are approval-gated or absent; autonomy expansion is an `asdlc-maturity-assessment` (platform-assessment plugin) decision, not a server default.
- Don't build agent-facing tools on an API with no contract — fix the contract first (`agent-api-contract-designer`).

## Suggested effort
Medium-high — produces a designed tool-card spec and test plan; implementation on top is mostly mechanical.
