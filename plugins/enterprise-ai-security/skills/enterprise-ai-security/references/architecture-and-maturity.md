# architecture and maturity

## 1. Enterprise AI security landscape

1\. Identity, access and governance

Users · roles · service accounts · policies · audit

2\. Data ingestion and RAG

Documents · OCR · chunking · embeddings · vector DB · retrieval

3\. LLM and application security

Prompt handling · inference · output validation · model serving

4\. Agent and tool execution

Planning · memory · APIs · code execution · external actions

5\. Enterprise infrastructure and defence

Cloud · network · secrets · monitoring · incident response

Cross-cutting controls: privacy, cryptography, secure development, supply-chain security, governance, continuous testing and human oversight.

This is a practical architecture for organizing controls, not a formal architecture prescribed by a single framework.

## 2. Maturity levels: basic to advanced

Use the following levels to decide which controls to implement first.

| Level             | Goal                                | Expected capability                                                                                                   |
| ----------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| L1 — Basic        | Establish a secure foundation       | Authentication, authorization, encryption, input validation, safe deployment and audit logs                           |
| L2 — Intermediate | Defend AI-specific attack paths     | Prompt-injection testing, RAG access control, tenant isolation, tool restrictions and continuous evaluation           |
| L3 — Advanced     | Control autonomous systems at scale | Runtime policy enforcement, AI red teaming, identity governance, attack detection, containment and automated response |

These levels are a practical implementation roadmap, not official OWASP maturity-level definitions.

## 3. Complete enterprise AI security checklist

The following checklist is designed to cover conventional cybersecurity as well as the additional attack surfaces introduced by LLMs, RAG and agentic AI.
