# identity and data security

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
