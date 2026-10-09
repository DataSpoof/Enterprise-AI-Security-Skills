# implementation roadmap

## 6. Implementation roadmap for an enterprise

I would implement these controls in the following order. The time estimates are illustrative and assume an existing application and cloud environment.

### Phase 1 — Establish the security baseline

Weeks 1–2 · Basic

- Inventory AI applications, models, agents, tools and data sources.
- Implement SSO/MFA, RBAC, secrets management and TLS.
- Restrict database, model-server and cloud access.
- Define data classification, retention and acceptable-use policies.
- Establish audit logging and incident ownership.

### Phase 2 — Secure the RAG pipeline

Weeks 3–4 · Basic to intermediate

- Secure document ingestion, OCR and parsing.
- Enforce document-level and tenant-level authorization.
- Validate metadata provenance and protect index writes.
- Test cache isolation, deletion propagation and citation integrity.
- Create a baseline suite for retrieval and privacy attacks.

### Phase 3 — Harden LLMs and tools

Weeks 5–8 · Intermediate

- Test prompt injection, sensitive-data disclosure and unsafe outputs.
- Introduce a trusted tool-execution layer.
- Apply per-action permissions, quotas and network restrictions.
- Require independent approval for high-impact operations.
- Add model, prompt and dependency security checks to CI/CD.

### Phase 4 — Continuous assurance

Weeks 9–12 · Intermediate to advanced

- Run AI-specific red-team assessments.
- Map attack paths to OWASP and MITRE ATLAS.
- Add runtime monitoring and automated policy enforcement.
- Test emergency shutdown, credential revocation and recovery.
- Create an evidence trail for audits and recurring security reviews.

### Phase 5 — Advanced enterprise defence

Ongoing

- Implement continuous agent discovery and runtime policy enforcement.
- Monitor inter-agent communication and delegated privileges.
- Automate threat detection, containment and regression testing.
- Perform supply-chain assurance and adversarial resilience exercises.
- Reassess controls whenever models, tools, permissions or data flows change.
