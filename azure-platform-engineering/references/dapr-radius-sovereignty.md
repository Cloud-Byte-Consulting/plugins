# Dapr + Radius best practices: portability and cloud sovereignty

Shared reference for the `azure-platform-engineering` skills. Grounds the
plugin's opinionated Radius + Dapr core in the portability model from
Microsoft's *"Designing for cloud sovereignty with Radius and Dapr"*
(techcommunity, July 2026) and the Dapr/Radius product docs. Skills cite this
file rather than repeating the reasoning.

Source: https://techcommunity.microsoft.com/blog/LinuxandOpenSourceBlog/designing-for-cloud-sovereignty-with-radius-and-dapr/4535067

## The core idea: sovereignty is a portability problem, solved on two axes

Cloud sovereignty is the ability for an organization to retain control over
**where its data and compute run** — increasingly an operational and
architectural problem (data-residency law, the EU Data Act, sector rules),
not just a policy discussion. You cannot relocate a workload across a
sovereignty boundary if moving it means rewriting it. The Radius + Dapr pairing
attacks this by separating two kinds of portability so they can be solved
independently:

| Axis | Owned by | Mechanism | What stays constant |
|---|---|---|---|
| **Code portability** | **Dapr** | Building-block APIs behind a sidecar; backing services are swappable components | The application source |
| **Deployment portability** | **Radius** | Resource Types (contracts) + Recipes (per-environment IaC) + Environments (locations) | The application definition |

Held together, the result the blog states plainly: **"Where a workload runs
becomes a deployment decision rather than a redevelopment project."** Relocating
to meet a sovereignty requirement changes *recipes and environment bindings*,
not code.

## Code portability — Dapr best practices

1. **Program against building blocks, never a backend's native SDK.** The app
   calls the Dapr state, pub/sub, secrets, bindings, or workflow API — if it
   imports the Cosmos DB or Event Hubs SDK directly, portability is already
   lost and no amount of recipe swapping restores it. This is the single most
   important rule; the `iac-guardrail-verifier` should treat a native
   backing-store SDK on a sovereignty-critical path as a finding.
2. **One component name per capability, swapped per environment.** The app
   references a stable component name (e.g. `statestore`); the component's
   `type`/`metadata` (Redis vs Cosmos vs PostgreSQL) is environment config, set
   by the Radius recipe. The app never learns which backend it got.
3. **Choose building blocks with production-grade component parity across your
   target clouds.** State, pub/sub, and secrets have mature implementations on
   both Kubernetes-native and Azure-managed backings; that parity is what makes
   the swap real. Keep alpha APIs (e.g. the Conversation building block) off
   the sovereignty-critical path until they stabilize.
4. **Route secrets through the Dapr secrets building block / secret stores** so
   credential *sourcing* relocates with the workload (Key Vault in one
   environment, a Kubernetes secret store in another) without app changes.
5. **Let resiliency and mTLS travel with the app.** Dapr resiliency policies
   (retries, circuit breakers, timeouts) and sidecar mTLS are declared
   alongside the app, so behavior is identical wherever it lands.

## Deployment portability — Radius best practices

1. **Model each dependency as an abstract Resource Type, not a concrete
   resource.** The app claims `stateStores`, `redisCaches`, or a custom type
   (`ByteCloud.App/apiBackends`) — never a specific Azure resource. The
   Resource Type is the contract; the developer never names infrastructure.
2. **Author one Recipe per environment per type.** The same `app.bicep` binds
   to a local container in dev and a managed Azure service in prod because the
   Environment selects the Recipe. Across a sovereignty boundary, **only the
   Recipes differ** — the blog's whole demonstration.
3. **Environments are deployment locations** (Kubernetes namespace, Azure
   subscription/resource group, region). Organize them by **business unit ×
   region × prod/non-prod** for sovereignty splits — the "enterprise" rung of
   the environment ladder in `azure-platform-designer`.
4. **Keep recipe output contracts stable.** The `result.values` a recipe emits
   (host/port/baseUrl for backends; Dapr type/version/metadata for state
   stores; publicUrl for routes) are the seam between infra and app. Stable
   outputs mean swapping a recipe — including across clouds — never touches the
   application.

## The reference the blog uses, and how our golden path mirrors it

The blog's sample is an **order-console** app — a Next.js frontend, an
`orders-api`, and a `fulfillment-worker` — deployed unchanged to two very
different substrates: on **Kubernetes** it binds PostgreSQL + Kafka; on
**Azure** it binds managed PostgreSQL + Event Hubs. Dapr supplies state and
pub/sub so the code is identical; Radius supplies the per-environment Recipes so
only the IaC differs.

The `azure-agentic-idp` golden path this plugin stamps embodies the same model:

- The sample app's **only persistence contract is the Dapr state API**, so the
  `statestore` component swaps across **Redis (dev) → Cosmos DB (azure-aca) →
  PostgreSQL Flexible Server (azure-aks)** with zero application change.
- The **`apiBackends` / `apiRoutes` abstract types + per-environment recipes**
  give deployment portability for compute and ingress (Container Apps vs AKS;
  APIM route re-points automatically because `backendUrl` flows from the recipe
  output).
- A **sovereignty split maps directly to the enterprise environment rung**: one
  Radius environment per sovereignty boundary, each with region-pinned recipes.

## Sovereignty checklist to encode in the platform constitution

- Declare **data-residency boundaries and allowed regions** as numbered
  constitution rules (`CON-xx`); the designer and verifier cite them.
- Require every **persistence and messaging dependency to go through a Dapr
  building block** — no native backing-store SDK on a sovereignty-critical
  path (a verifier check).
- Require **one Radius environment per sovereignty boundary**, with
  region-pinned Recipes and no cross-boundary data connections.
- Keep an **exit / relocation runbook**: because only recipes differ, a
  relocation is a recipe + environment change, provable in non-prod before it
  is exercised in prod. Portability you have not tested is a claim, not a
  capability.

## Honest caveats

- **Pub/sub parity is not perfect.** Kafka and Event Hubs differ at the edges
  (ordering, delivery, partitioning semantics). Dapr abstracts the API, not
  every guarantee — test the messaging contract on each target backing, don't
  assume fungibility.
- **Alpha building blocks aren't sovereignty-grade** (Conversation API is
  alpha; no Azure OpenAI component as of this writing).
- **Radius is CNCF Sandbox, v0.x** ("not yet ready for production workloads"
  per its README); the abstractions survive a control-plane swap, which is
  itself part of the sovereignty exit story.
- **Some backends leak semantics** into the app despite the building block
  (consistency models, TTL behavior). Validate per backend rather than trusting
  the abstraction blindly.
