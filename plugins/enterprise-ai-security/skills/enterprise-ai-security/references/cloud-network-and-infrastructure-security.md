# cloud network and infrastructure security

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
