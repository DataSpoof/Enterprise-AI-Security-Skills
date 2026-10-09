# logging monitoring and incident response

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
