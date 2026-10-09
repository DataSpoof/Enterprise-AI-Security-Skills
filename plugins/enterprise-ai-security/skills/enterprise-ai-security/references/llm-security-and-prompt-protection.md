# llm security and prompt protection

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
