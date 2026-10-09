# Security scope and authorization

This repository provides defensive security guidance, architecture review methods, and test-planning material for enterprise LLM, RAG, and agentic AI systems.

## Allowed by default

- Threat modeling, design review, policy and control review, and analysis of user-provided code or configuration.
- Building test plans for isolated environments that use synthetic data and non-production credentials.
- Explaining mitigations, monitoring, incident response, and evidence needed to validate controls.

## Requires explicit written authorization

Any active probing or testing of production systems, third-party services, customer records, or systems the requester does not own or administer. Before proposing or executing such work, establish the authorized assets, test window, allowed techniques, rate and impact limits, test accounts/data, emergency contacts, and stop conditions. Use assets/assessment-scope.template.md to record the scope.

If authorization or scope is missing, keep the work passive and defensive. Do not treat a request to “test security” as permission to scan, exploit, enumerate, or access live systems.

This scope statement is a project policy, not legal advice or a substitute for an organization's engagement approval process.
