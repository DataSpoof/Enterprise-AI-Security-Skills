# Enterprise Cybersecurity for LLMs, RAG and Agentic AI

Enterprise security roadmap · Basic → Intermediate → Advanced · Research reviewed as of 9 October 2026

An enterprise AI system needs more than prompt filtering and API authentication. You must secure the complete system: users, identity, data, documents, vector databases, models, tools, agents, cloud infrastructure, and the actions that AI can perform.

For a useful enterprise security programme, I would organize the subject into 10 security domains and 3 maturity levels:

- Basic: Prevent unauthorized access, protect sensitive data, and establish secure deployment practices.
- Intermediate: Defend against prompt injection, retrieval attacks, tool abuse, and cross-user data leakage.
- Advanced: Implement AI red teaming, autonomous-agent containment, continuous security evaluation, and enterprise-wide threat detection.

The research below draws on the OWASP, NIST, MITRE ATLAS, and Google Secure AI Framework (SAIF). OWASP documents LLM and agent-specific risks, NIST provides AI risk-management guidance, MITRE ATLAS maps adversarial techniques, and SAIF organizes security controls across data, infrastructure, models, and applications.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://owasp.github.io\&sz=32)

OWASP Foundation

+3



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

## Domain 1 — Identity, authentication and authorization

This is one of the most important domains. A model must never become a way to bypass existing enterprise permissions.

| ID     | Security aspect           | Basic                             | Intermediate                                      | Advanced                                                  |
| ------ | ------------------------- | --------------------------------- | ------------------------------------------------- | --------------------------------------------------------- |
| IAM-01 | Authentication            | Secure login                      | SSO and MFA                                       | Risk-based authentication                                 |
| IAM-02 | Authorization             | Role-based access control (RBAC)  | Attribute-based access control (ABAC)             | Context-aware authorization                               |
| IAM-03 | Least privilege           | Restrict user permissions         | Restrict API and service permissions              | Dynamic, action-level agent permissions                   |
| IAM-04 | User identity propagation | Identify the requesting user      | Pass verified user identity through RAG and tools | End-to-end delegated identity enforcement                 |
| IAM-05 | Service accounts          | Separate service identities       | Scoped service identities                         | Short-lived, workload-bound credentials                   |
| IAM-06 | Agent identities          | Register every agent              | Unique identity per agent and environment         | Lifecycle management and continuous identity verification |
| IAM-07 | Privilege escalation      | Prevent unauthorized admin access | Test indirect privilege escalation                | Continuously detect privilege misuse                      |
| IAM-08 | Session management        | Secure cookies and tokens         | Session expiry and revocation                     | Risk-based session termination                            |
| IAM-09 | Multi-tenant isolation    | Separate tenant records           | Enforce tenant filters at every retrieval layer   | Automated cross-tenant isolation testing                  |
| IAM-10 | Administrative access     | Restrict admin consoles           | Privileged access management (PAM)                | Just-in-time access and session recording                 |
| IAM-11 | Delegation                | Limit delegated access            | Explicit scopes for delegated actions             | Verifiable delegation chains and revocation               |
| IAM-12 | Identity lifecycle        | Disable departed users            | Revoke associated API and agent access            | Automatically discover and retire orphaned identities     |

Enterprise implementation requirements

- The backend must enforce authorization. Do not rely on the LLM to decide whether a user is allowed to read a document.
- Apply the user's permissions before returning documents from the retrieval layer.
- Treat an agent's identity and the human who requested its task as separate security principals.
- Never grant an agent administrator permissions merely because a workflow needs multiple tools.
- Check authorization again when an agent performs an action, even if the initial request was authorized.

Google's SAIF specifically recommends application access management and least-privilege agent permissions, including permissions that adapt to the task and context.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.saif.google\&sz=32)

SAIF

+1



## Domain 2 — Data security, privacy and governance

Data security must cover every copy of the data: original documents, extracted text, chunks, embeddings, prompts, model responses, agent memory, logs and backups.

| ID      | Security aspect                  | Basic                          | Intermediate                                    | Advanced                                                 |
| ------- | -------------------------------- | ------------------------------ | ----------------------------------------------- | -------------------------------------------------------- |
| DATA-01 | Data classification              | Public, internal, confidential | Automated sensitivity labels                    | Risk-based classification pipelines                      |
| DATA-02 | PII protection                   | Detect and mask personal data  | Context-aware redaction                         | Privacy-enhancing processing                             |
| DATA-03 | Secrets protection               | Remove keys and passwords      | Automated secret scanning                       | Runtime secret detection and revocation                  |
| DATA-04 | Encryption at rest               | Encrypt databases and storage  | Centralized key management                      | Customer-managed or hardware-backed keys where required  |
| DATA-05 | Encryption in transit            | TLS                            | Enforce secure service-to-service communication | Certificate automation and workload identity             |
| DATA-06 | Data minimization                | Send only required data        | Field-level filtering                           | Policy-driven minimization across the AI pipeline        |
| DATA-07 | Retention                        | Define deletion periods        | Apply retention to derived data                 | Verified deletion across replicas, indexes and caches    |
| DATA-08 | Data residency                   | Select approved regions        | Enforce regional processing policies            | End-to-end data-location assurance                       |
| DATA-09 | Consent and purpose              | Document allowed use           | Enforce purpose-based policies                  | Auditable consent and purpose propagation                |
| DATA-10 | Data lineage                     | Record source documents        | Track transformations and derived chunks        | Provenance graph across data, embeddings and outputs     |
| DATA-11 | Data exfiltration                | Restrict exports               | Detect sensitive output patterns                | Correlate output, tool, network and identity events      |
| DATA-12 | Training and fine-tuning privacy | Use approved datasets          | Filter sensitive and unauthorized records       | Privacy-risk testing and controlled training pipelines   |
| DATA-13 | Backups                          | Encrypted backups              | Restore and deletion testing                    | Immutable recovery copies and tested recovery procedures |
| DATA-14 | Data ownership                   | Define data owners             | Assign policy enforcement responsibilities      | Automated policy enforcement across data products        |

### RAG-specific data security

A RAG system creates several additional risks:

- Document-level authorization: Users must retrieve only documents they can access.
- Chunk-level authorization: Splitting a document must not remove its access restrictions.
- Metadata integrity: Users must not be able to alter `tenant_id`, `classification`, `owner` or `access_level` to obtain extra access.
- Embedding privacy: Embeddings must be treated as potentially sensitive derived data, not automatically as anonymous data.
- Deletion propagation: Removing a source document must also trigger appropriate removal from the vector index, lexical index, caches and derived stores.
- Prompt and response privacy: Prompts and outputs must not expose confidential data through analytics, debugging or tracing systems.
- Memory privacy: Persistent agent memory must have ownership, access rules, expiry and deletion controls.

The governing principle is that access to an embedding or a chunk must not confer access to the original data. SAIF's guidance covers privacy-enhancing technologies, user-data management, training-data authorization and integrity protection.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.saif.google\&sz=32)

SAIF

+1



## Domain 3 — LLM security and prompt protection

LLM security is different from traditional application security because the model interprets natural language and untrusted context. A prompt filter alone cannot provide a reliable security boundary.

| ID     | Security aspect                  | Basic                                   | Intermediate                            | Advanced                                                  |
| ------ | -------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------------------------- |
| LLM-01 | Prompt injection                 | Separate instructions from user content | Detect direct and indirect attacks      | Layered runtime defenses and adversarial evaluation       |
| LLM-02 | System-prompt protection         | Keep secrets out of prompts             | Test prompt extraction                  | Treat all prompt content as potentially discoverable      |
| LLM-03 | Input validation                 | Enforce size and type limits            | Detect malformed or suspicious inputs   | Risk-based input analysis                                 |
| LLM-04 | Output validation                | Validate output schemas                 | Context-aware sanitization              | Policy enforcement before every downstream action         |
| LLM-05 | Sensitive-information disclosure | Avoid sending secrets to models         | Detect and redact sensitive outputs     | Correlated privacy controls across models, tools and logs |
| LLM-06 | Jailbreak resistance             | Define permitted behavior               | Test multilingual and encoded attacks   | Continuous adversarial testing across model versions      |
| LLM-07 | Untrusted-context handling       | Label retrieved content as untrusted    | Test malicious document instructions    | Enforce independent policy checks at action boundaries    |
| LLM-08 | Hallucination-related security   | Require citations for critical claims   | Validate claims against trusted sources | Risk-based verification and human approval                |
| LLM-09 | Model refusal and policy bypass  | Define prohibited operations            | Test refusal consistency                | Continuous policy regression testing                      |
| LLM-10 | Output rendering                 | Escape HTML and Markdown appropriately  | Prevent XSS and unsafe links            | Context-aware rendering and browser isolation             |
| LLM-11 | Structured output                | Validate JSON schema                    | Enforce enums, types and ranges         | Validate semantic and authorization constraints           |
| LLM-12 | Model selection                  | Use approved models                     | Benchmark security and privacy          | Continuous model risk assessment                          |
| LLM-13 | Model extraction                 | Restrict model endpoints                | Detect extraction-like query patterns   | Rate, query and access anomaly detection                  |
| LLM-14 | Denial of service                | Set request and token limits            | Detect adversarial resource consumption | Adaptive quotas and circuit breakers                      |
| LLM-15 | Model behavior changes           | Pin approved versions                   | Test upgrades before deployment         | Continuous evaluation and controlled rollback             |

OWASP's current LLM security guidance is the 2026 edition, published in August 2026. It reflects expanded threat coverage informed by real-world incidents. Its recent incident roundup highlights risks including prompt injection, sensitive-information disclosure, excessive agency, supply-chain weaknesses and unbounded consumption.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://genai.owasp.org\&sz=32)

OWASP Gen AI Security Project

+2



### Important distinction: prompt injection versus jailbreak

- Prompt injection: Untrusted content attempts to redirect the model's task or influence its use of data and tools.
- Jailbreak: An attempt to bypass the model's intended restrictions.
- System-prompt extraction: An attempt to reveal hidden instructions.
- Insecure output handling: A model's output is interpreted unsafely by a downstream system.
- Sensitive-information disclosure: The system reveals data that should remain private.

These attacks can overlap, but they require different tests and controls.

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

## Domain 5 — Agentic AI, autonomous actions and tool security

Agentic AI introduces a critical change: the system may not only answer a question; it may also execute commands, call APIs, change records, send messages, access files or trigger business workflows.

The OWASP Agentic Security Initiative identifies threats involving goal hijacking, tool misuse, identity abuse, supply-chain compromise, unexpected code execution, memory poisoning and cascading failures. OWASP also introduced its Agent Control Standard in September 2026 to support runtime enforcement and visibility into agent behavior.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://genai.owasp.org\&sz=32)

OWASP Gen AI Security Project

+2



| ID    | Security aspect             | Basic                                   | Intermediate                             | Advanced                                                        |
| ----- | --------------------------- | --------------------------------------- | ---------------------------------------- | --------------------------------------------------------------- |
| AG-01 | Agent inventory             | Register deployed agents                | Discover shadow agents                   | Continuous discovery across cloud and SaaS                      |
| AG-02 | Agent permissions           | Limit available tools                   | Apply action-specific scopes             | Dynamic least privilege                                         |
| AG-03 | Tool authorization          | Authenticate tool calls                 | Authorize every operation                | Independent runtime policy enforcement                          |
| AG-04 | Tool input validation       | Validate parameters                     | Apply business-rule validation           | Policy checks against user intent and action risk               |
| AG-05 | Tool output validation      | Validate responses                      | Treat outputs as untrusted context       | Integrity verification and cross-tool consistency checks        |
| AG-06 | Human approval              | Approve sensitive actions               | Risk-based approval gates                | Transaction-bound, independently enforced approval              |
| AG-07 | Destructive operations      | Disable unnecessary destructive actions | Require confirmation and limits          | Reversible workflows and controlled execution                   |
| AG-08 | Agent autonomy              | Bound task duration                     | Bound tool calls and steps               | Adaptive autonomy budgets and kill switches                     |
| AG-09 | Goal hijacking              | Define task boundaries                  | Test indirect prompt injection           | Runtime intent and policy enforcement                           |
| AG-10 | Tool abuse                  | Allowlist tools                         | Restrict tool arguments and destinations | Detect anomalous tool sequences                                 |
| AG-11 | Code execution              | Disable unnecessary execution           | Isolate execution environments           | Ephemeral sandboxes with strict egress and resource controls    |
| AG-12 | Browser security            | Restrict browsing                       | Control domains and downloads            | Isolated browser sessions and data-loss controls                |
| AG-13 | Shell and terminal security | No privileged shell by default          | Command allowlists and sandboxing        | Separate execution brokers and tightly restricted egress        |
| AG-14 | API security                | Use scoped API credentials              | Enforce endpoint and method policies     | Per-action authorization and transaction controls               |
| AG-15 | Inter-agent communication   | Authenticate agents                     | Validate message schemas and origins     | Signed messages, provenance and trust-boundary enforcement      |
| AG-16 | Agent memory                | Define storage and expiry               | Validate memory writes                   | Memory provenance, poisoning detection and selective revocation |
| AG-17 | Task delegation             | Limit delegated tasks                   | Propagate permissions and scope          | Bounded delegation chains and automatic revocation              |
| AG-18 | Loop and runaway prevention | Set step and timeout limits             | Detect repetitive tool calls             | Runtime budgets and automatic circuit breakers                  |
| AG-19 | Cascading failures          | Limit retries                           | Isolate agent failures                   | Fault containment across workflows and agents                   |
| AG-20 | Agent shutdown              | Provide manual stop                     | Revoke sessions and tool access          | Emergency containment across identities, jobs and integrations  |

### Recommended agent execution pattern

User request

Authenticated identity and intended task

LLM / agent planner

Proposes a tool call; does not authorize it

Trusted policy enforcement layer

Identity · permissions · argument validation · business rules · risk limits

Approval gate, when required

Verified human approval for sensitive actions

Isolated tool executor

Restricted credentials, network access and execution scope

Audit and outcome verification

Record decision, approval, action and result

Important: A model-generated statement such as “the user approved this action” is not proof of approval. The approval must be verified independently by the trusted application or policy service.

### Agent actions that should normally require additional controls

- Deleting records, files or cloud resources.
- Sending external emails or messages.
- Transferring money or initiating payments.
- Changing user permissions, firewall rules or security settings.
- Publishing code, packages or content externally.
- Executing code with access to production systems.
- Accessing bulk customer data or exporting sensitive records.
- Creating new credentials or delegating privileged access.

The exact approval requirements depend on the action's risk, reversibility, business context and applicable policy.

## Domain 6 — Application, API and web security

AI applications still require conventional application security. Adding an LLM does not remove the need to protect the web application, API gateway, database and integration layer.

| ID     | Security aspect              | Basic                                 | Intermediate                                     | Advanced                                              |
| ------ | ---------------------------- | ------------------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| APP-01 | API authentication           | Authenticate every protected endpoint | Standardized identity middleware                 | Workload identity and continuous verification         |
| APP-02 | API authorization            | Check object ownership                | Prevent broken object-level authorization (BOLA) | Automated authorization regression testing            |
| APP-03 | Rate limiting                | Limit requests                        | Per-user and per-model quotas                    | Adaptive abuse detection                              |
| APP-04 | Input validation             | Enforce types and sizes               | Schema and semantic validation                   | Risk-based validation                                 |
| APP-05 | Output handling              | Encode untrusted content              | Prevent XSS, injection and unsafe rendering      | Context-aware output security                         |
| APP-06 | SSRF                         | Restrict server-side URLs             | Block private and metadata endpoints             | Network egress allowlists and isolated fetch services |
| APP-07 | CORS and browser security    | Restrict origins                      | Secure cookies and CSRF protection               | Strong browser isolation and continuous testing       |
| APP-08 | Database security            | Parameterized queries                 | Least-privilege DB identities                    | Fine-grained data policies and activity monitoring    |
| APP-09 | File upload security         | Validate files and size               | Malware scanning and isolated processing         | Content-disarm workflows where appropriate            |
| APP-10 | Dependency security          | Patch known vulnerabilities           | Software composition analysis                    | Risk-based remediation and exploit monitoring         |
| APP-11 | Business logic               | Enforce deterministic rules           | Test workflow abuse                              | Formal policy checks for high-impact actions          |
| APP-12 | Error handling               | Avoid exposing stack traces           | Safe error responses                             | Correlated internal diagnostics without data leakage  |
| APP-13 | Browser and frontend secrets | Keep secrets off the client           | Secure session handling                          | Automated client-side leakage detection               |
| APP-14 | Webhooks and callbacks       | Authenticate requests                 | Sign messages and prevent replay                 | Strong provenance and idempotent execution            |
| APP-15 | API inventory                | Document endpoints                    | Discover shadow endpoints                        | Continuous attack-surface monitoring                  |

One key principle: validate model output before using it in SQL, HTML, shell commands, URLs or API calls. Use parameterized queries, safe APIs and structured argument validation instead of trusting natural-language output.

## Domain 7 — Model, dependency and AI supply-chain security

Your AI supply chain includes more than the LLM. It includes model weights, tokenizers, embedding models, rerankers, datasets, OCR engines, Python packages, container images, agent frameworks, MCP servers, plugins and external APIs.

| ID     | Security aspect          | Basic                           | Intermediate                               | Advanced                                                      |
| ------ | ------------------------ | ------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| SUP-01 | Model provenance         | Use approved model sources      | Verify hashes and release metadata         | Signed provenance and controlled promotion                    |
| SUP-02 | Model licensing          | Review usage rights             | Track restrictions and redistribution      | Automated policy checks across model inventory                |
| SUP-03 | Model integrity          | Pin model versions              | Verify artifact integrity                  | Continuous integrity monitoring                               |
| SUP-04 | Model loading            | Avoid untrusted model artifacts | Prefer safer formats and loaders           | Isolated inspection and restricted deserialization            |
| SUP-05 | Package dependencies     | Pin versions                    | Scan for vulnerabilities                   | Dependency provenance and controlled builds                   |
| SUP-06 | Container security       | Use trusted base images         | Scan and minimize images                   | Signed images and admission policies                          |
| SUP-07 | Dataset provenance       | Track source and owner          | Validate licensing and integrity           | Reproducible, auditable dataset pipelines                     |
| SUP-08 | Fine-tuning security     | Restrict training access        | Screen datasets and evaluate models        | Poisoning simulations and provenance checks                   |
| SUP-09 | Plugin security          | Approve integrations            | Review permissions and code                | Runtime inspection and continuous revalidation                |
| SUP-10 | MCP server security      | Approve server and tools        | Validate schemas and permissions           | Runtime tool-policy enforcement and server monitoring         |
| SUP-11 | External model providers | Review provider security        | Define data retention and processing terms | Continuous vendor risk and data-flow assurance                |
| SUP-12 | CI/CD security           | Protect build credentials       | Secure runners and deployment identities   | Isolated builds, signed artifacts and policy-gated promotion  |
| SUP-13 | Model updates            | Approve upgrades                | Evaluate before rollout                    | Canary deployment, rollback and continuous regression testing |
| SUP-14 | Compromised dependencies | Track critical advisories       | Detect vulnerable transitive packages      | Automated containment and dependency replacement              |

### What to verify before using an open-source model

1. The model's actual source and publisher.
2. Artifact hashes and version provenance.
3. The model's license and permitted commercial use.
4. The security of its loading format and associated code.
5. The origin and integrity of tokenizers and auxiliary files.
6. Whether fine-tuning or quantization introduced changes.
7. Whether the model sends data to an external service.
8. Whether the inference server exposes privileged APIs or unsafe debugging endpoints.

Model weights are not automatically safe because they are open source or downloaded from a popular repository. SAIF recommends model and data integrity controls, approved training data and secure-by-default ML tooling.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.saif.google\&sz=32)

SAIF

+1



## Domain 8 — Cloud, network and infrastructure security

| ID     | Security aspect          | Basic                                      | Intermediate                                      | Advanced                                                        |
| ------ | ------------------------ | ------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------- |
| INF-01 | Network segmentation     | Separate application and database networks | Isolate model serving and tools                   | Fine-grained workload segmentation                              |
| INF-02 | Network egress           | Restrict unnecessary outbound traffic      | Domain and destination allowlists                 | Policy-controlled egress for every agent and execution workload |
| INF-03 | Secret management        | Use a secret manager                       | Short-lived credentials and rotation              | Workload identity and automated revocation                      |
| INF-04 | Container security       | Non-root containers                        | Read-only filesystems and restricted capabilities | Runtime enforcement and ephemeral execution                     |
| INF-05 | Kubernetes security      | RBAC and network policies                  | Admission controls and pod security               | Runtime threat detection and workload identity                  |
| INF-06 | Cloud IAM                | Least-privilege roles                      | Separate AI service roles                         | Fine-grained workload and resource-level controls               |
| INF-07 | Storage security         | Private buckets and databases              | Restrict public access and sharing                | Continuous configuration validation                             |
| INF-08 | GPU infrastructure       | Restrict access to GPU hosts               | Isolate inference workloads                       | Hardware and workload isolation appropriate to the threat model |
| INF-09 | Configuration management | Secure defaults                            | Infrastructure as code and policy checks          | Continuous drift detection and automated remediation            |
| INF-10 | Disaster recovery        | Backups and recovery procedures            | Tested failover                                   | Resilience exercises and controlled recovery                    |
| INF-11 | Availability             | Timeouts and quotas                        | Autoscaling and circuit breakers                  | Multi-layer resilience and adversarial load testing             |
| INF-12 | Environment isolation    | Separate development and production        | Separate data, identities and networks            | Controlled artifact promotion and isolated testing environments |

For agents that browse the web, execute code or process untrusted documents, network egress restrictions are especially important. A model should not be able to reach internal services or cloud metadata endpoints simply because its tool implementation permits arbitrary URLs.

## Domain 9 — Logging, monitoring, incident response and threat detection

Traditional monitoring asks whether a service is failing. AI security monitoring must also ask what the model retrieved, what the agent attempted, which identity authorized the action, and whether the action exceeded its intended scope.

| ID     | Security aspect            | Basic                                  | Intermediate                             | Advanced                                                  |
| ------ | -------------------------- | -------------------------------------- | ---------------------------------------- | --------------------------------------------------------- |
| MON-01 | Audit logging              | Log user and request IDs               | Correlate requests, retrieval and tools  | End-to-end traceable action history                       |
| MON-02 | Sensitive-log protection   | Redact secrets                         | Apply field-level controls               | Policy-based logging and access audits                    |
| MON-03 | Prompt-injection detection | Record suspicious events               | Correlate attack patterns                | Continuous detection and response                         |
| MON-04 | Retrieval monitoring       | Record source IDs and access decisions | Detect anomalous retrieval               | Cross-tenant and cross-classification anomaly detection   |
| MON-05 | Tool monitoring            | Record tool name and result            | Detect unusual action sequences          | Runtime policy violation detection                        |
| MON-06 | Identity monitoring        | Track authentication failures          | Detect unusual agent privileges          | Correlate identity, agent and resource events             |
| MON-07 | Cost monitoring            | Set token budgets                      | Detect usage spikes                      | Adaptive quotas and abuse containment                     |
| MON-08 | Model monitoring           | Monitor errors and latency             | Track model-version changes              | Security and quality regression correlation               |
| MON-09 | Incident response          | Define owners and escalation           | Create AI-specific playbooks             | Automated containment with safe recovery                  |
| MON-10 | Evidence preservation      | Retain security logs                   | Preserve correlated traces               | Tamper-resistant evidence and reproducible investigations |
| MON-11 | Kill switches              | Stop a running job                     | Revoke tools and credentials             | Contain agents, sessions and downstream jobs              |
| MON-12 | Threat intelligence        | Track security advisories              | Map events to known AI attack techniques | Continuously update detections and threat models          |
| MON-13 | Recovery                   | Restore service                        | Validate data and permissions            | Rebuild trusted state and verify containment              |
| MON-14 | Security metrics           | Track incidents and fixes              | Track detection and response times       | Measure risk reduction and control effectiveness          |

### What an enterprise AI audit log should contain

- Timestamp and correlation ID.
- Authenticated user or calling service.
- Agent ID, model version and environment.
- Retrieval source identifiers and authorization decisions.
- Tool requested, validated arguments and actual execution result.
- Policy decisions and approval references.
- Resource access and outbound network events.
- Errors, retries, limits and emergency stops.

Avoid indiscriminately recording complete prompts, retrieved documents or chain-of-thought. Capture the information needed for security and audit without creating a second repository of sensitive data. Logs themselves require access controls, retention policies and integrity protection.

For an enterprise Security Operations Center (SOC), map AI-specific events to the existing incident workflow and correlate them with identity, endpoint, network and cloud telemetry. Google's SAIF explicitly includes agent observability, threat detection, vulnerability management, red teaming and incident response.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.saif.google\&sz=32)

SAIF

+1



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



## 4. Advanced security topics that enterprises often miss

The previous domains cover the core security programme. The following topics deserve additional attention when an AI system becomes business-critical.

| ID     | Advanced topic                             | What you need to protect against                                                                    |
| ------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| ADV-01 | Multimodal prompt injection                | Malicious instructions hidden in images, audio, video or document content                           |
| ADV-02 | Persistent memory poisoning                | Malicious content stored in long-term memory and reused in later sessions                           |
| ADV-03 | Cross-session contamination                | Data or instructions from one user influencing another user's session                               |
| ADV-04 | Model inversion and membership inference   | Attempts to infer sensitive training data or determine whether a record was used for training       |
| ADV-05 | Training-data poisoning                    | Deliberate manipulation of training or fine-tuning datasets                                         |
| ADV-06 | Embedding attacks                          | Manipulation of similarity search, nearest-neighbor retrieval or embedding-based classifiers        |
| ADV-07 | Semantic authorization bypass              | A request is phrased differently to evade simplistic security filters                               |
| ADV-08 | Agent identity abuse                       | Credentials or delegated identities are used outside their intended scope                           |
| ADV-09 | Inter-agent trust failures                 | One agent accepts malicious instructions or unverified results from another                         |
| ADV-10 | MCP and tool-definition tampering          | A trusted integration changes its capabilities or behavior after approval                           |
| ADV-11 | Model supply-chain compromise              | A model, package, plugin or build artifact is malicious or altered                                  |
| ADV-12 | Inference side channels                    | Information is exposed through timing, resource usage or observable system behavior                 |
| ADV-13 | GPU and shared-compute isolation           | Cross-workload exposure or unsafe isolation of sensitive inference workloads                        |
| ADV-14 | Model extraction and intellectual property | Unauthorized reconstruction, extraction or copying of a proprietary model                           |
| ADV-15 | Autonomous network reconnaissance          | An agent explores systems outside the authorized target scope                                       |
| ADV-16 | AI-amplified denial of service             | Repeated tool calls, large contexts, expensive retrieval or unbounded agent loops exhaust resources |
| ADV-17 | Cascading agent failures                   | One compromised or malfunctioning agent causes downstream agents and workflows to fail              |
| ADV-18 | AI-assisted software supply-chain attacks  | An agent publishes or installs malicious packages or modifies build configuration                   |
| ADV-19 | Shadow AI and shadow agents                | Employees or business units deploy unapproved AI tools with access to enterprise data               |
| ADV-20 | Policy drift                               | A model, prompt, tool, dataset or integration changes and invalidates previous security testing     |

These are areas to include in advanced threat modeling, not a claim that each is a separate vulnerability in every system. MITRE ATLAS and the OWASP GenAI Security Project provide useful starting points for mapping techniques and testing the relevant attack paths.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://atlas.mitre.org\&sz=32)

MITRE ATLAS

+2



## 5. Enterprise AI security testing matrix

A security programme should have explicit tests, not just policies. Here is a practical test suite for a RAG and agentic AI platform.

| Test ID | Test scenario                                            | Expected secure result                                                       |
| ------- | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| T-01    | Ask the model to reveal hidden system instructions       | No sensitive information is disclosed                                        |
| T-02    | Insert malicious instructions into a retrieved PDF       | The instructions do not override trusted policy                              |
| T-03    | Attempt to retrieve another tenant's document            | No unauthorized document or metadata is returned                             |
| T-04    | Modify document ownership metadata                       | Authorization remains based on trusted records                               |
| T-05    | Delete a document and query it again                     | Deleted content is no longer retrievable within the defined deletion SLA     |
| T-06    | Ask an agent to call a tool outside its permissions      | The trusted execution layer denies the call                                  |
| T-07    | Submit malformed arguments to a tool                     | The tool rejects the request safely                                          |
| T-08    | Attempt an external network request to a private service | Network policy blocks the request                                            |
| T-09    | Ask an agent to delete production resources              | The action is blocked or requires the appropriate independent approval       |
| T-10    | Trigger repeated agent retries                           | Resource budgets and circuit breakers stop runaway execution                 |
| T-11    | Introduce a malicious or vulnerable dependency           | The build or deployment policy blocks or isolates it                         |
| T-12    | Attempt to expose API keys through model output          | Sensitive data is not disclosed; any attempted access is logged              |
| T-13    | Reuse one user's cached response as another user         | Authorization checks prevent cross-user leakage                              |
| T-14    | Change the model or prompt version                       | Security regression tests run before release                                 |
| T-15    | Disable a running agent during an incident               | Its tool access and active jobs are contained according to the response plan |

Use synthetic data and isolated test environments. Obtain explicit authorization before testing production systems, third-party targets or real customer records.

### Security metrics to measure

Security effectiveness

Attack success rate, unauthorized retrieval rate, policy-bypass rate, sensitive-data leakage rate and percentage of critical tests passed.

Identity and access

Excessive agent permissions, failed authorization tests, orphaned identities and time to revoke compromised credentials.

Operational resilience

Detection time, containment time, recovery time, runaway-agent incidents, rate-limit violations and service availability.

Governance and assurance

Percentage of AI assets inventoried, critical risks with owners, overdue remediation, tested recovery procedures and expiring exceptions.

Do not treat a high prompt-injection detection rate as proof of security. Measure whether an attack can actually obtain unauthorized data, execute a prohibited action or cross a trust boundary.

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

## 7. Final master checklist

Use this interactive checklist to track your implementation progress. Check an item only when the control is implemented and verified.

## Enterprise AI security readiness

## 0/23

### 1. Identity and access

SSO/MFA and backend authorization

Least-privilege model and agent identities

Tenant and document-level access control

Credential rotation and revocation

### 2. Data and RAG

Data classification and sensitive-data protection

Secure ingestion and isolated document parsing

Trusted metadata and retrieval authorization

Embedding, cache and memory isolation

Deletion propagation and citation verification

### 3. LLM and agent security

Prompt-injection and jailbreak evaluations

Output validation and safe rendering

Tool allowlists and argument validation

Independent approval for high-impact actions

Agent budgets, isolation and emergency stop

### 4. Infrastructure and supply chain

Network segmentation and egress controls

Secure containers and cloud IAM

Model, package and dataset provenance

CI/CD security and controlled model updates

### 5. Monitoring and governance

Correlated audit logs and privacy controls

AI incident response and recovery tests

Automated adversarial security testing

Risk ownership and framework mapping

Continuous remediation and regression testing

Reset checklistCopy checklist

A checked item is a tracking status, not an independent security certification. Critical controls still need documented tests and evidence.

## 8. Research sources and further reading

These are the primary references I would use to build the detailed control register.

[十大風險是為了喚起大眾對威脅的關注，別把排行示警當教條！ | iThome](https://images.openai.com/static-rsc-4/gdr7NAeHl4x8B5oQ31nPBvbYG8JoynaIPR0JFg82niqq3dx4A7GTQOd-QNDMoHsui8x0hz7REEDrHq2-UF4zAsL-iGL462_CXfRcKn9LO2DTZ5QFo_EpfKG-dQ_zYhu3BHEISF1m4O7YbQSlwqkG3KHnVrhgqdsmIA51FDGsUTM?purpose=inline)

OWASP GenAI Security Project

Current LLM Top 10, agentic threats, mitigation guides, security tooling and the Agent Control Standard.

[LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) · [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/) · [Securing Agentic Applications Guide](https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/)

[NIST | Brand](https://images.openai.com/static-rsc-4/6wu7Q_dzooGZkaiawgwqdpm32MuNVWQ8fKnWJB0iMzTVd4tJRHNFHkOtslTaXoGcTmDDwEA2DuO68KgHltzVIOeyalTMtjkxM6kiY3ecAdq160uU9vDLKNHtBkcHV2rHJuXgi_gP0qSDmuOk4bXYhAx-hZPil3k26EDunyohVzA?purpose=inline)

NIST AI Risk Management Framework

AI governance, risk assessment, trustworthiness and generative AI risk management.

[AI RMF resources](https://www.nist.gov/itl/ai-risk-management-framework) · [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

[AI Security in 2025: MITRE ATLAS Framework Guide](https://images.openai.com/static-rsc-4/Ky50YI2259OglS_U361Fsyj0wGfFpRhyMsk-G6cINe3-n5dH34fmUp_dMLmPBrv90TeOe6N8H7St9SeouPfVj1NLG0P00_5gZtFJ8sqWF5d38ihRWfdaYy9xiWnclNbRd4-4NxUnO9nVLJR3Wr6WSCA5Yld4wY4bcKpjIiHSRoE?purpose=inline)

MITRE ATLAS

Threat techniques, attack paths, mitigations and real-world AI attack case studies.

[Explore the ATLAS threat matrix](https://atlas.mitre.org/)

[SAIF: Google's Guide to Secure AI](https://images.openai.com/static-rsc-4/BMT2J9U9qHHQjriNW5bku9N-xf8kcb0CLKWUh2bHjK4eFNVqzy-UOCYtFOoKjiRJffKEO5FUusgTLO0rGaZD9jvSSD5RWYY1PTLF_PqOKi6yyvN-27xlJOv9ZH6DAsvokGzpRUd2xk1-th8dPL6OIo9Ip14-FU_6PEYw9K7IF1w?purpose=inline)

Google Secure AI Framework

Practical controls for data, models, infrastructure, applications, agents and security assurance.

[SAIF framework](https://www.saif.google/) · [Security controls](https://www.saif.google/secure-ai-framework/controls)

[The OWASP Top 10 for AI Agents: Your 2026 Security Checklist (ASI Top 10) - DEV Community](https://images.openai.com/static-rsc-4/2aArVDyMoXzDAeMyM6YP7a5JbZ4oTS-WxNgOLm4cPDxob6Qbv4jDLZR-mX0rfetFWFUwfgndWe4ThPrRpOyXqVSLJ3U2e38YMu8fC-DaSer8NKSs2dMnmPrYTZhNXOnD4VUL9yWo1nhoYfkDmhMy-aBCM6Bvm_7V2Tq9PglUFNQ?purpose=inline)

OWASP Agentic Security Initiative

Agent goal hijacking, tool misuse, identity abuse, memory poisoning and other autonomous-system risks.

[Agentic Applications Top 10](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) · [Q3 2026 exploit roundup](https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/)

## My recommendation

For a production enterprise platform combining LLM, RAG and agentic AI, prioritize these five controls before adding more complex security products:

1. Authorization at the data and action layers. The model must not be the authority that decides access.
2. A trusted agent execution gateway. Validate every tool call, its arguments, its permissions and its intended effect.
3. RAG isolation and document integrity. Prevent cross-tenant retrieval, malicious document influence and unauthorized index modifications.
4. End-to-end auditability. Trace the user request, retrieval, policy decision, tool execution and outcome.
5. Continuous adversarial testing. Re-test after changes to models, prompts, datasets, tools, dependencies and permissions.

These controls establish a foundation for the rest of the programme. Once they are working, extend the programme with advanced threat detection, supply-chain assurance, runtime agent enforcement and automated incident response.