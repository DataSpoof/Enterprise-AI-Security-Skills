# governance development and testing

## Domain 10 — Governance, compliance, secure development and AI testing

Technical controls are not enough. Enterprises need to establish ownership, assess risks, test controls before release, and keep those controls effective after deployment.

| ID     | Security aspect       | Basic                        | Intermediate                                   | Advanced                                             |
| ------ | --------------------- | ---------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| GOV-01 | AI inventory          | Register AI applications     | Include agents, models and data flows          | Continuous discovery and ownership reconciliation    |
| GOV-02 | Risk assessment       | Classify use cases           | Threat-model each workflow                     | Continuous risk reassessment                         |
| GOV-03 | Security architecture | Define baseline controls     | Conduct design reviews                         | Architecture assurance and control verification      |
| GOV-04 | Secure development    | Code review and SAST         | DAST, dependency and secrets scanning          | AI-aware security testing in CI/CD                   |
| GOV-05 | Threat modeling       | Identify assets and threats  | Map trust boundaries and attack paths          | Attack graphs and continuous threat-model updates    |
| GOV-06 | AI red teaming        | Test basic jailbreaks        | Test RAG, privacy and tool abuse               | Adversarial campaigns and continuous regression      |
| GOV-07 | Evaluation            | Test normal behavior         | Test malicious inputs and negative cases       | Risk-weighted automated security evaluation          |
| GOV-08 | Change management     | Approve production releases  | Test model and prompt changes                  | Risk-based release gates and rollback                |
| GOV-09 | Third-party risk      | Review vendors               | Assess data handling and controls              | Continuous supplier and dependency assessment        |
| GOV-10 | Compliance            | Map applicable obligations   | Maintain evidence and controls                 | Continuous control monitoring and audit readiness    |
| GOV-11 | Human oversight       | Assign accountable owners    | Define approval and escalation thresholds      | Risk-adaptive human oversight                        |
| GOV-12 | Employee use of AI    | Publish acceptable-use rules | Manage approved tools and shadow AI            | Continuous discovery and policy enforcement          |
| GOV-13 | Incident exercises    | Run tabletop exercises       | Simulate prompt injection and data leakage     | Cross-team AI incident simulations                   |
| GOV-14 | Security ownership    | Assign system owners         | Define RACI across security, data and AI teams | Enterprise-wide accountability and control assurance |
| GOV-15 | Risk acceptance       | Document exceptions          | Define approvers and expiry dates              | Continuous exception monitoring and automatic expiry |

### Frameworks to align with

| Framework                             | Primary use                                                       |
| ------------------------------------- | ----------------------------------------------------------------- |
| OWASP GenAI LLM Top 10 2026           | Identify and prioritize LLM application vulnerabilities.          |
| OWASP Top 10 for Agentic Applications | Assess risks caused by agent autonomy, tool use and delegation.   |
| OWASP Agent Control Standard          | Structure runtime enforcement and agent observability.            |
| NIST AI RMF                           | Govern AI risks throughout design, deployment and operation.      |
| NIST AI 600-1                         | Extend risk management to generative AI-specific risks.           |
| MITRE ATLAS                           | Map attacks, techniques and mitigations for AI-enabled systems.   |
| Google SAIF                           | Organize technical security controls across the AI lifecycle.     |
| ISO/IEC 27001                         | Establish and maintain an information security management system. |
| ISO/IEC 42001                         | Establish AI governance and management processes.                 |
| CIS Controls                          | Strengthen foundational enterprise security.                      |

NIST's Generative AI Profile, published in July 2024, supplements its AI Risk Management Framework. NIST's framework is being revised, so organizations should verify the applicable current release when establishing a formal compliance programme.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.nist.gov\&sz=32)

NIST

+1



The OWASP Agent Control Standard is a useful addition for organizations moving from advisory chatbots to agents that can execute actions.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://genai.owasp.org\&sz=32)

OWASP Gen AI Security Project

+1
