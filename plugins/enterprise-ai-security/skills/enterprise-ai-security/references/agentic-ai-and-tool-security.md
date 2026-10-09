# agentic ai and tool security

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
