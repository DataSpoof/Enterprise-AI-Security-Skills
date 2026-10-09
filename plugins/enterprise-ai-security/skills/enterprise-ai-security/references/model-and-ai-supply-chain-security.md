# model and ai supply chain security

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
