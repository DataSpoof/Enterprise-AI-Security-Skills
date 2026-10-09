---
name: enterprise-ai-security
description: Design, assess, threat-model, test, and improve enterprise security for LLM, RAG, and agentic AI systems. Use for architecture reviews, control registers, AI red-team plans, security roadmaps, governance, and incident-readiness work.
---

# Enterprise AI Security

Use this skill to produce practical, evidence-oriented security work for enterprise systems that use large language models, retrieval-augmented generation (RAG), tools, or autonomous agents. The bundled reference contains the complete source roadmap and its control IDs. Treat it as a reusable baseline and adapt it to the system and the user's scope.

## Operating principles

- The model is not an authorization authority. Enforce user, tenant, document, and action permissions in trusted application and execution layers.
- Treat user input, retrieved documents, tool results, memory, inter-agent messages, and model output as untrusted data. Separate instructions from data, validate outputs, and check authorization again at every data or action boundary.
- Secure the full system: identity, data, ingestion, parsers, embeddings, indexes, retrieval, prompts, models, applications, tools, agents, infrastructure, vendors, and operations.
- Apply controls according to exposure, business impact, threat paths, and evidence. The reference's Basic, Intermediate, and Advanced tiers are a practical roadmap, not a formal certification or official maturity model.
- Do not claim a control is effective, a system is secure, or an organization is compliant without evidence. Distinguish implemented, tested, planned, not applicable, and unknown states.

## Workflow

1. **Set the boundary.** Establish the system purpose, users and tenants, data classes, deployment and model, RAG sources, tools and permissions, external connections, environment, business impact, applicable jurisdictions, and available evidence. Ask only for details that materially change the result. Otherwise state assumptions and continue.
2. **Read the relevant reference sections.** Use `references/enterprise-ai-security-baseline.md` as the complete control library. Load only the portions needed for the task, and retain its control IDs when mapping gaps, mitigations, tests, or ownership.
3. **Map assets and trust boundaries.** Trace identity and governance; ingestion, parsing, OCR and indexing; retrieval, cache and memory; prompts and model inference; output handling; tool execution and agent delegation; and cloud, network, monitoring, and supply chain. Include cross-user and cross-tenant boundaries.
4. **Model concrete abuse paths.** Consider direct and indirect prompt injection, sensitive-data exposure, unauthorized retrieval, metadata or index tampering, tool misuse, privilege escalation, identity/delegation abuse, memory poisoning, unsafe code or browser activity, supply-chain compromise, denial of service, and cascading failures where relevant. Distinguish prompt injection from jailbreaks and explain the applicable threat path rather than treating every topic as a finding.
5. **Prioritize controls.** Start with foundational identity, authorization, data protection, safe deployment, and audit controls. Then address AI-specific RAG, prompt, tool, and tenant-isolation paths. For systems with meaningful autonomy, add runtime policy enforcement, bounded execution, independent approvals, containment, and continuous assurance. Map each recommendation to relevant reference IDs, an owner or role, dependencies, verification evidence, and a target maturity tier where useful.
6. **Make tests measurable and safe.** Use synthetic data and isolated environments by default. Adapt the reference's 15 test scenarios to the architecture; state preconditions, action, expected secure result, evidence to capture, and pass/fail criteria. A prompt-injection detector score alone is not proof: test whether data, permissions, or actions cross a boundary. Do not probe production, third-party systems, or real customer data without explicit authorization and a defined scope.
7. **Check facts that can change.** The bundled document is the user's supplied baseline, marked as reviewed on 9 October 2026. Verify current framework editions, laws, standards, vendor capabilities, and incident claims from authoritative primary sources when they matter to the answer. Separate source claims, verified current facts, and your recommendations. Do not describe the reference's tiers or checklist as official OWASP, NIST, ISO, or other certification criteria.
8. **Report gaps and decisions clearly.** Separate evidence-backed findings from assumptions. For each material risk, explain the affected asset and trust boundary, plausible impact, existing controls, gap, priority rationale, remediation, verification, and residual risk. Identify unknowns and ownership needs; do not mark a checkbox complete merely because a policy exists.

## Reference map

The full source is bundled in `references/enterprise-ai-security-baseline.md`. It includes the landscape and maturity model; all control tables across ten domains; RAG-specific and agent-specific guidance; advanced topics; the 15-case test matrix; metrics; a five-phase roadmap; the 23-item readiness checklist; frameworks and research sources; and the five recommended priority controls.

The ten control domains are:

1. Identity, authentication, and authorization
2. Data security, privacy, and governance
3. LLM security and prompt protection
4. RAG, vector databases, and document intelligence
5. Agentic AI, autonomous actions, and tool security
6. Application, API, and web security
7. Model, dependency, and AI supply-chain security
8. Cloud, network, and infrastructure security
9. Logging, monitoring, incident response, and threat detection
10. Governance, compliance, secure development, and AI testing

For a readiness review, use the master checklist but report evidence and status per item. For an implementation roadmap, adapt the five source phases to actual dependencies and team capacity; its week ranges are illustrative. For a threat model, use the advanced-topics list as prompts, not as a claim that every item applies to every system.

## Useful deliverable shape

Choose only the sections that fit the request. For a full assessment or roadmap, provide:

- Scope, architecture summary, assumptions, and critical trust boundaries
- Prioritized risks and the relevant control IDs
- A control register with status, evidence, owner, priority, target state, and verification method
- Safe test cases with expected results and evidence
- A phased remediation plan, dependencies, metrics, and residual risks

Keep executive summaries short and put detailed control mappings in tables. If the user asks for one artifact (such as a test plan or policy), deliver that artifact directly instead of forcing the full assessment format.
