# Framework mapping notes

These are working orientation notes for organizing a security review. They are not official crosswalks, certification mappings, or proof of compliance. Verify current editions and exact requirements from the framework owner before making a formal claim. The complete source document's framework table and research links are retained in references/enterprise-ai-security-baseline.md.

| Framework | Start with these skill modules | Use |
|---|---|---|
| OWASP GenAI and agent security | OWASP.md; LLM, RAG, agent, and testing references | Organize application and agent threat coverage. |
| NIST AI RMF and Generative AI Profile | NIST-AI-RMF.md; governance and threat-model references | Structure AI risk identification, prioritization, and management. |
| MITRE ATLAS | MITRE-ATLAS.md; advanced threat and testing references | Map relevant adversary behavior after checking the current matrix. |
| Google SAIF | Google-SAIF.md; data, model, agent, infrastructure, and operations references | Review lifecycle controls across AI components. |
| ISO/IEC 27001 and ISO/IEC 42001 | ISO-and-CIS.md; governance, identity, data, and operations references | Connect AI-specific risks to management-system processes. |
| CIS Controls | ISO-and-CIS.md; identity, cloud, supply chain, logging references | Check foundational enterprise security practices. |

Preserve the enterprise baseline's native control IDs (for example IAM-01, RAG-01, AGT-01, and GOV-01). Add a framework identifier only when its current official source supports the mapping. Document the source edition, rationale, evidence, and any gaps.
