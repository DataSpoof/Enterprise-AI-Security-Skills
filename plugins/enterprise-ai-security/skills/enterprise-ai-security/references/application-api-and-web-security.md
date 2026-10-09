# application api and web security

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
