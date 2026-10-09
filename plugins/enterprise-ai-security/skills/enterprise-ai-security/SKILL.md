---
name: enterprise-ai-security
description: Create security reviews, threat models, control registers, roadmaps, secure designs, incident plans, and authorized test plans for enterprise LLM, RAG, and agentic AI systems.
version: 1.1.0
license: MIT
domain: cybersecurity
subdomain: enterprise-ai-security
author: DataSpoof
tags:
  - enterprise-security
  - llm-security
  - rag-security
  - agentic-ai
  - threat-modeling
  - ai-governance
frameworks:
  owasp:
    - GenAI LLM Top 10 2026
    - Top 10 for Agentic Applications
    - Agent Control Standard
  nist:
    - AI Risk Management Framework
    - Generative AI Profile NIST AI 600-1
  mitre:
    - ATLAS
  google:
    - Secure AI Framework SAIF
  iso:
    - ISO/IEC 27001
    - ISO/IEC 42001
  cis:
    - CIS Controls
---

# Enterprise AI Security

Use this skill to design, assess, threat-model, test, and improve enterprise security across LLM, retrieval-augmented generation (RAG), and agentic AI systems. Adapt the supplied enterprise baseline to the system, evidence, and scope at hand. Do not present the baseline as a certification or a guarantee of security.

## Start with the work mode and scope

Choose the smallest mode that satisfies the request:

- **Design or architecture review:** map the data flow, trust boundaries, identities, permissions, model, retrieval, tools, deployment, and owners.
- **Control or readiness review:** use the relevant domain references and checklist; record status, evidence, owner, priority, and verification.
- **Threat model or test plan:** trace plausible attack paths and propose safe cases with preconditions, expected results, evidence, and pass criteria.
- **Code or configuration review:** inspect user-provided material and identify concrete weaknesses with fixes and verification steps.
- **Roadmap or governance:** prioritize controls by business impact, exposure, dependencies, and team capacity.
- **Incident readiness or response:** identify containment, evidence preservation, recovery, communications, and lessons for the AI-specific path.

Before any active testing, establish written authorization and a bounded scope covering assets, test window, allowed techniques, rate and impact limits, test identities/data, stop conditions, and emergency contact. Use assets/assessment-scope.template.md to record it. A signed engagement or an in-scope public bug bounty can establish authority. If authorization is absent or ambiguous, provide passive analysis and isolated test plans using synthetic data; do not probe production, third-party systems, or real customer records.

## Workflow

1. **Set the boundary.** Identify system purpose, users and tenants, data classes, deployment and model provider, RAG sources, agents and tools, permissions, external connections, environment, business impact, applicable obligations, and evidence. State assumptions and continue when missing details do not block useful work.
2. **Trace the system.** Follow identity and authorization; ingestion, parsing, OCR and indexing; retrieval, cache and memory; prompts and inference; output handling; tool execution and delegation; and cloud, network, monitoring, and supply chain. Include cross-user and cross-tenant boundaries.
3. **Select references.** Read the applicable topic modules below. Use the complete baseline when a task spans domains or exact wording matters. Preserve its control IDs in findings, mitigations, tests, and ownership records.
4. **Analyze attack paths.** Consider direct and indirect prompt injection, sensitive-data exposure, unauthorized retrieval, index or metadata tampering, tool misuse, identity/delegation abuse, memory poisoning, unsafe code or browser activity, supply-chain compromise, denial of service, and cascading failures where relevant. Distinguish prompt injection from jailbreaks. Treat advanced topics as hypotheses to assess, not findings by themselves.
5. **Prioritize controls.** Start with identity, authorization, data protection, safe deployment, and auditability. Then address RAG, prompt, tool, and tenant-isolation paths. For meaningful autonomy, add runtime policy enforcement, bounded execution, independent approvals, containment, and continuous assurance. Map each recommendation to control IDs, accountable roles, dependencies, verification evidence, and a maturity tier where useful.
6. **Make testing measurable and safe.** Prefer synthetic data and isolated environments. State preconditions, action, expected secure result, evidence, and pass/fail criteria. Validate whether data, permissions, or actions cross a boundary; a prompt-detector score alone is not proof. Apply the authorization gate above before active testing.
7. **Check changeable claims.** The bundled source is dated 9 October 2026. Verify current framework editions, laws, standards, vendor capabilities, and incident claims against authoritative primary sources when they affect a decision. Separate source claims, verified current facts, and recommendations.
8. **Report clearly.** Distinguish evidence-backed findings from assumptions. For each material risk, explain affected asset and boundary, plausible impact, existing controls, gap, priority rationale, remediation, verification, residual risk, and owner. Identify unknowns; a written policy alone does not prove implementation.

## Reference map

Load only the modules needed. All topic modules are under references/.

- architecture-and-maturity.md — system landscape, maturity levels, and baseline orientation.
- identity-and-data-security.md — identity, authorization, data protection, privacy, and governance.
- llm-security-and-prompt-protection.md — model interaction and prompt protections.
- rag-vector-and-document-security.md — retrieval, vector databases, and document intelligence.
- agentic-ai-and-tool-security.md — agents, autonomy, tools, and action boundaries.
- application-api-and-web-security.md — application, API, and web controls.
- model-and-ai-supply-chain-security.md — models, dependencies, and provenance.
- cloud-network-and-infrastructure-security.md — cloud, networks, workloads, and infrastructure.
- logging-monitoring-and-incident-response.md — observability, detection, and response.
- governance-development-and-testing.md — ownership, secure development, governance, and framework list.
- advanced-threat-catalog.md — 20 advanced topics to consider where relevant.
- security-testing-matrix-and-metrics.md — baseline test scenarios and measurement guidance.
- implementation-roadmap.md — phased implementation sequence.
- readiness-checklist.md — 23-item enterprise readiness checklist.
- frameworks-and-research.md — source references and five recommended priorities.
- enterprise-ai-security-baseline.md — the complete supplied source document, retained verbatim.

Framework notes are in mappings/. They help organize a crosswalk; verify the current official publication and do not imply exact equivalence unless the evidence supports it.

## Reporting format

For a full review, provide a short executive summary followed by scope and assumptions, critical trust boundaries, prioritized risks with baseline IDs, controls and evidence, safe validation cases, remediation owners and phases, metrics, and residual risks. For a focused request, deliver only the requested artifact. Mark controls as implemented, tested, planned, not applicable, or unknown; do not mark a control complete merely because a policy exists.

## Core principles

- The model is not an authorization authority. Enforce user, tenant, document, and action permissions in trusted application and execution layers.
- Treat input, retrieved content, tool results, memory, inter-agent messages, and model output as untrusted data. Validate at each data and action boundary.
- Secure the whole system: identity, data, ingestion, parsing, embeddings, indexes, retrieval, prompts, models, applications, agents, tools, vendors, infrastructure, and operations.
- The baseline's Basic, Intermediate, and Advanced tiers are a practical roadmap, not official maturity levels.
- Do not claim that a system is secure or compliant without evidence and a defined assessment scope.
