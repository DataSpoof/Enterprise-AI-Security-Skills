# rag vector and document security

## Domain 4 — RAG, vector databases and document intelligence

This domain deserves its own security programme. A conventional LLM security assessment may not adequately test the ingestion, indexing, retrieval and document-processing pipeline.

| ID     | Security aspect        | Basic                                 | Intermediate                                            | Advanced                                                         |
| ------ | ---------------------- | ------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------- |
| RAG-01 | Document ingestion     | Accept approved file types            | Validate MIME types and file signatures                 | Isolated ingestion with policy enforcement                       |
| RAG-02 | Malware scanning       | Scan uploaded files                   | Scan extracted content and embedded objects             | Multi-engine scanning and isolated detonation where appropriate  |
| RAG-03 | Parser security        | Patch PDF, OCR and document libraries | Sandbox parsers                                         | Disposable, restricted processing workers                        |
| RAG-04 | OCR and hidden content | Extract visible text                  | Detect hidden text and suspicious layers                | Multimodal adversarial-document testing                          |
| RAG-05 | Document provenance    | Record source and owner               | Verify source authenticity and integrity                | Signed provenance and chain-of-custody records                   |
| RAG-06 | Document poisoning     | Restrict upload permissions           | Detect suspicious or conflicting content                | Poisoning simulation and continuous corpus validation            |
| RAG-07 | Chunking integrity     | Preserve document metadata            | Maintain permissions and source references              | Test access-control inheritance through every transformation     |
| RAG-08 | Embedding integrity    | Use approved embedding models         | Version and validate embedding pipelines                | Detect embedding drift and suspicious index changes              |
| RAG-09 | Vector DB access       | Authenticate database access          | Enforce tenant and document-level policies              | Independently verify authorization at retrieval time             |
| RAG-10 | Vector DB isolation    | Separate production and development   | Restrict network access and credentials                 | Isolated environments and controlled index promotion             |
| RAG-11 | Retrieval poisoning    | Restrict corpus writers               | Detect malicious instructions and anomalous documents   | Adversarial retrieval testing and provenance-based trust         |
| RAG-12 | Retrieval manipulation | Validate search parameters            | Detect abnormal ranking manipulation                    | Hybrid retrieval, independent verification and attack simulation |
| RAG-13 | Unauthorized retrieval | Filter results by user access         | Apply ACL filters before returning chunks               | Negative authorization tests across users and tenants            |
| RAG-14 | Metadata tampering     | Protect metadata writes               | Validate trusted metadata against authoritative sources | Signed or independently verified security-critical metadata      |
| RAG-15 | Index integrity        | Restrict index modifications          | Audit index writes and deletions                        | Reproducible rebuilds and integrity verification                 |
| RAG-16 | Cache leakage          | Separate user sessions                | Partition caches by identity and permissions            | Authorization-aware cache invalidation and adversarial tests     |
| RAG-17 | Citation integrity     | Link responses to sources             | Validate cited source IDs                               | Verify citations and permissions against original records        |
| RAG-18 | Retrieval leakage      | Limit retrieved context               | Test cross-user retrieval                               | Automated cross-tenant and cross-classification testing          |
| RAG-19 | Deletion               | Delete source and indexed data        | Verify derived-data removal                             | Reconciliation across indexes, replicas and caches               |
| RAG-20 | Retrieval monitoring   | Log query and result metadata         | Detect unusual access patterns                          | Correlate retrieval, identity and exfiltration indicators        |

### RAG attacks you must test

1\. Malicious PDF or document

A document contains hidden instructions that attempt to override the assistant's task or cause unauthorized tool use.

Defence: isolated parsing, content inspection, trust separation and action-level authorization.

2\. Cross-tenant vector search

A user searches for information and receives chunks belonging to another customer.

Defence: server-enforced authorization, trusted metadata, tenant isolation and negative tests.

3\. Knowledge-base poisoning

An attacker adds or alters content to influence retrieval or the answers generated from it.

Defence: controlled ingestion, provenance, review, integrity monitoring and poisoning evaluations.

4\. Citation and source manipulation

The model cites an untrusted source, an unauthorized document or a source that no longer supports the answer.

Defence: server-generated source references, access rechecks and citation verification.

For an enterprise implementation, I recommend a hybrid retrieval design where applicable: keyword retrieval plus vector retrieval, followed by trusted access-control filtering and optional reranking. However, hybrid search is a retrieval-quality technique, not a substitute for authorization or security controls.
