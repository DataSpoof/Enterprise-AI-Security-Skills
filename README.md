# Enterprise AI Security Skills

An open, portable Agent Skill for reviewing and improving the security of enterprise systems built with large language models (LLMs), retrieval-augmented generation (RAG), and agentic AI. It turns the supplied enterprise security baseline into a practical workflow, focused reference modules, reusable assessment formats, and implementation guidance.

The repository follows the plugin-and-skill structure used by [DataSpoof's website-security-shield](https://github.com/DataSpoof/website-security-shield). The skill content remains platform-neutral: Claude Code can install it through the marketplace, while Codex and other compatible agents can use the same SKILL.md package.

## At a glance

| Item | Details |
|---|---|
| Skill name | enterprise-ai-security |
| Intended systems | Enterprise LLM applications, RAG pipelines, AI agents, and the services and infrastructure around them |
| Main purpose | Help an assistant design, assess, threat-model, test-plan, and improve AI security using evidence and scoped recommendations |
| Coverage | Ten control domains, three practical maturity tiers, 20 advanced threat topics, a 15-case testing matrix, an implementation roadmap, and a 23-item readiness checklist |
| Supported format | Portable Agent Skill with YAML metadata, modular Markdown references, JSON index, mappings, assets, and optional Python utilities |
| Safety model | Passive analysis by default; active testing requires explicit written authorization and a bounded scope |
| License | MIT; see [LICENSE](LICENSE) |

## What the skill does

Use the skill to turn an AI security question into a scoped analysis or usable engineering artifact. It adapts the depth to the request and evidence available; it does not claim that a system is secure merely because a checklist is complete.

| Work type | What the assistant does | Typical result |
|---|---|---|
| Architecture review | Maps data flows, identities, permissions, retrieval, model calls, tools, cloud services, and trust boundaries. | Architecture risks, boundary gaps, design decisions, and prioritized mitigations. |
| Threat modeling | Traces plausible abuse paths across users, tenants, documents, prompts, memory, tools, agents, and infrastructure. | Threat model with assets, entry points, attack paths, impact, controls, and residual risks. |
| LLM security review | Reviews prompt handling, input/output boundaries, model access, validation, abuse resistance, and safe rendering. | Control gaps and concrete verification guidance tied to the relevant source control IDs. |
| RAG security review | Examines ingestion, parsing, chunking, metadata, embeddings, indexes, retrieval authorization, caching, citations, and deletion. | RAG-specific risks such as cross-tenant retrieval, document tampering, and unauthorized disclosure. |
| Agent and tool review | Checks agent identity, delegated permissions, tool allowlists, argument validation, approvals, execution limits, and containment. | Bounded action design, approval gates, execution controls, audit needs, and emergency-stop guidance. |
| Code or configuration review | Analyzes user-provided code and configuration for security issues and explains fixes. | Findings with affected component, impact, remediation, and a way to verify the fix. |
| Readiness assessment | Uses the baseline checklist and available evidence to identify implemented, tested, planned, not-applicable, and unknown controls. | Evidence-oriented readiness summary or control register with owners and priorities. |
| Test planning | Converts relevant risks into safe test cases with preconditions, expected results, evidence, and pass criteria. | A scoped test plan, using synthetic data and isolated environments by default. |
| Roadmap and governance | Sequences controls by business impact, exposure, dependencies, ownership, and team capacity. | Phased implementation plan, governance actions, measures, dependencies, and decision points. |
| Incident readiness | Plans AI-aware containment, evidence preservation, recovery, escalation, and lessons learned. | Incident playbook, tabletop scenarios, recovery steps, or monitoring improvements. |

## Security coverage

The baseline organizes controls into ten domains. The assistant selects the relevant modules instead of forcing every request through a full enterprise assessment.

| Domain | What it covers | Reference module |
|---|---|---|
| 1. Identity, authentication, and authorization | SSO and MFA, user and service identities, least privilege, delegated identity, sessions, administrative access, and tenant isolation. | [identity-and-data-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/identity-and-data-security.md) |
| 2. Data security, privacy, and governance | Classification, sensitive data, privacy, encryption, retention, secure ingestion, and data access boundaries. | [identity-and-data-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/identity-and-data-security.md) |
| 3. LLM security and prompt protection | Prompt handling, direct and indirect prompt injection, jailbreak distinction, model exposure, output validation, and abuse controls. | [llm-security-and-prompt-protection.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/llm-security-and-prompt-protection.md) |
| 4. RAG, vector databases, and document intelligence | Parsing and ingestion, metadata integrity, embeddings, retrieval authorization, index access, caches, citations, and deletion propagation. | [rag-vector-and-document-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/rag-vector-and-document-security.md) |
| 5. Agentic AI, autonomous actions, and tool security | Agent identity, delegation, tool restrictions, argument validation, approval for impactful actions, execution budgets, and containment. | [agentic-ai-and-tool-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/agentic-ai-and-tool-security.md) |
| 6. Application, API, and web security | Authentication and authorization at application boundaries, API protections, input/output handling, and web attack surfaces. | [application-api-and-web-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/application-api-and-web-security.md) |
| 7. Model, dependency, and AI supply-chain security | Model and package provenance, dependency risk, datasets, plugins, build artifacts, and controlled updates. | [model-and-ai-supply-chain-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/model-and-ai-supply-chain-security.md) |
| 8. Cloud, network, and infrastructure security | Cloud IAM, network boundaries, egress, secrets, workloads, containers, GPU and shared-compute isolation. | [cloud-network-and-infrastructure-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/cloud-network-and-infrastructure-security.md) |
| 9. Logging, monitoring, incident response, and threat detection | Correlated audit trails, privacy-aware telemetry, detection, investigation, containment, recovery, and exercises. | [logging-monitoring-and-incident-response.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/logging-monitoring-and-incident-response.md) |
| 10. Governance, compliance, secure development, and AI testing | AI inventory, risk ownership, secure development, release/change controls, evaluation, red teaming, and incident exercises. | [governance-development-and-testing.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/governance-development-and-testing.md) |

The baseline control identifiers (for example IAM-01, RAG-01, APP-01, and GOV-01) are retained so findings, mitigations, tests, and owners can be traced back to the source. The Basic, Intermediate, and Advanced tiers below are practical planning levels, not official maturity ratings.

## Maturity levels

| Level | Goal | Examples of capability |
|---|---|---|
| Basic | Establish a secure foundation. | Authentication, backend authorization, least privilege, data protection, safe deployment, and audit logs. |
| Intermediate | Defend AI-specific attack paths. | Prompt-injection evaluations, RAG access enforcement, tenant isolation, tool restrictions, and continuous evaluation. |
| Advanced | Control autonomous systems at scale. | Runtime policy enforcement, bounded agent execution, AI red teaming, identity governance, containment, and automated response. |

Use these levels to sequence work for a particular system. They are not OWASP, NIST, ISO, or other certification criteria.

## Advanced threat coverage

The 20 topics below are prompts for threat modeling. They are not findings by themselves, and they will not all apply to every system. The detailed catalog is in [ATTACK_COVERAGE.md](ATTACK_COVERAGE.md) and the skill's advanced-threat reference.

| ID | Topic | What the skill helps examine |
|---|---|---|
| ADV-01 | Multimodal prompt injection | Instructions hidden in images, audio, video, or documents. |
| ADV-02 | Persistent memory poisoning | Malicious content stored and reused by long-term memory. |
| ADV-03 | Cross-session contamination | One user's data or instructions influencing another user's session. |
| ADV-04 | Model inversion and membership inference | Attempts to infer sensitive training data or membership of a record. |
| ADV-05 | Training-data poisoning | Deliberate manipulation of training or fine-tuning data. |
| ADV-06 | Embedding attacks | Manipulation of similarity search, retrieval, or embedding-based classifiers. |
| ADV-07 | Semantic authorization bypass | Requests phrased to evade simplistic security filters. |
| ADV-08 | Agent identity abuse | Credentials or delegated identities used outside their intended scope. |
| ADV-09 | Inter-agent trust failures | Agents accepting untrusted instructions or results from other agents. |
| ADV-10 | MCP and tool-definition tampering | Trusted integrations changing capabilities or behavior after approval. |
| ADV-11 | Model supply-chain compromise | Malicious or altered models, packages, plugins, or build artifacts. |
| ADV-12 | Inference side channels | Information exposed through timing, resource use, or observable behavior. |
| ADV-13 | GPU and shared-compute isolation | Cross-workload exposure or inadequate inference workload isolation. |
| ADV-14 | Model extraction and intellectual property | Unauthorized reconstruction or copying of proprietary models. |
| ADV-15 | Autonomous network reconnaissance | An agent exploring systems outside its authorized scope. |
| ADV-16 | AI-amplified denial of service | Resource exhaustion through repeated calls, large contexts, or unbounded loops. |
| ADV-17 | Cascading agent failures | One compromised or malfunctioning agent causing downstream failures. |
| ADV-18 | AI-assisted software supply-chain attacks | An agent publishing malicious packages or changing build configuration. |
| ADV-19 | Shadow AI and shadow agents | Unapproved AI systems accessing enterprise data. |
| ADV-20 | Policy drift | Model, prompt, tool, dataset, or integration changes invalidating prior review. |

## How an assessment is produced

| Step | Assistant activity | What the user receives |
|---|---|---|
| 1. Set scope | Establish purpose, users, tenants, data, model/provider, RAG sources, tools, environment, impact, and evidence. | Stated scope, assumptions, and key unknowns. |
| 2. Trace boundaries | Follow identity, ingestion, retrieval, prompts, outputs, tool actions, infrastructure, and external connections. | System flow and trust boundaries relevant to the request. |
| 3. Select controls | Load focused references and preserve source control IDs. | Relevant controls and ownership areas without unrelated checklist noise. |
| 4. Trace risks | Consider plausible abuse paths and business impact. | Evidence-backed findings separated from assumptions and hypotheses. |
| 5. Prioritize fixes | Rank by risk, exposure, dependencies, and feasibility. | Remediation order, owners, dependencies, and target state. |
| 6. Define validation | Specify safe preconditions, actions, expected outcomes, evidence, and pass criteria. | Measurable test cases and detection or verification guidance. |
| 7. Check current facts | Verify changeable framework, legal, standard, and vendor claims from primary sources when material. | Clear distinction between supplied baseline, verified current facts, and recommendations. |
| 8. Report residual risk | Identify unresolved gaps, exceptions, unknowns, and accountable owners. | Practical report or requested artifact with limitations made explicit. |

## Typical deliverables

| Deliverable | Included information |
|---|---|
| Threat model | System scope, assets, data flows, trust boundaries, attack paths, impacts, existing safeguards, mitigations, and residual risks. |
| Control register | Source control ID, status, evidence, owner, priority, target state, dependency, and verification method. |
| RAG or agent architecture review | Component-specific risks and recommended authorization, isolation, validation, and execution boundaries. |
| Security test plan | Authorized scope, preconditions, synthetic test data, actions, expected secure outcomes, evidence, and pass/fail criteria. |
| Readiness report | Checklist status, evidence gaps, highest-priority improvements, and unknowns. |
| Implementation roadmap | Phases, sequencing, dependencies, owners, milestones, metrics, and residual risks. |
| Incident playbook or tabletop | AI-specific trigger scenarios, containment, evidence preservation, escalation, recovery, and lessons learned. |
| Focused code/config review | Concrete observations, affected component, risk, remediation, and verification guidance. |

For a full review, the default report includes a short executive summary, scope and assumptions, critical trust boundaries, prioritized risks with source IDs, controls and evidence, safe validation cases, remediation plan, metrics, and residual risks. For a focused request, the skill produces only the requested artifact.

## Reference library

The skill loads only modules relevant to the user's task. The complete supplied baseline is preserved alongside the focused modules.

| Module | Use it for |
|---|---|
| [architecture-and-maturity.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/architecture-and-maturity.md) | Enterprise AI landscape, architecture framing, and practical maturity levels. |
| [identity-and-data-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/identity-and-data-security.md) | Identity, authorization, privacy, data handling, and governance. |
| [llm-security-and-prompt-protection.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/llm-security-and-prompt-protection.md) | LLM, prompt, model interaction, and output handling. |
| [rag-vector-and-document-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/rag-vector-and-document-security.md) | RAG pipelines, vector databases, document security, and retrieval. |
| [agentic-ai-and-tool-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/agentic-ai-and-tool-security.md) | Agent identities, autonomy, delegated actions, and tool controls. |
| [application-api-and-web-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/application-api-and-web-security.md) | Application, API, and web security controls. |
| [model-and-ai-supply-chain-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/model-and-ai-supply-chain-security.md) | Model, package, dependency, dataset, and build provenance. |
| [cloud-network-and-infrastructure-security.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/cloud-network-and-infrastructure-security.md) | Cloud, network, workload, and infrastructure protections. |
| [logging-monitoring-and-incident-response.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/logging-monitoring-and-incident-response.md) | Telemetry, detection, response, recovery, and incident exercises. |
| [governance-development-and-testing.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/governance-development-and-testing.md) | Governance, secure development, change management, and framework list. |
| [advanced-threat-catalog.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/advanced-threat-catalog.md) | Twenty advanced threat-model prompts. |
| [security-testing-matrix-and-metrics.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/security-testing-matrix-and-metrics.md) | Baseline test scenarios and security measurement guidance. |
| [implementation-roadmap.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/implementation-roadmap.md) | Phased implementation and priority sequencing. |
| [readiness-checklist.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/readiness-checklist.md) | The 23-item readiness checklist. |
| [frameworks-and-research.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/frameworks-and-research.md) | Source reading list and five recommended priority controls. |
| [enterprise-ai-security-baseline.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/references/enterprise-ai-security-baseline.md) | Complete original source document, retained verbatim. |

## Framework orientation

Mapping notes help organize a review. They are not official crosswalks, proof of control equivalence, or certification mappings. Verify the current source publication before making a formal claim.

| Framework | How the skill uses it | Mapping note |
|---|---|---|
| OWASP GenAI and agent security | Organizes LLM, RAG, and agent threat coverage. | [OWASP.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/OWASP.md) |
| NIST AI RMF and Generative AI Profile | Structures AI risk identification and management. | [NIST-AI-RMF.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/NIST-AI-RMF.md) |
| MITRE ATLAS | Helps describe relevant adversary techniques and attack paths. | [MITRE-ATLAS.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/MITRE-ATLAS.md) |
| Google SAIF | Provides a lifecycle-oriented lens across AI components. | [Google-SAIF.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/Google-SAIF.md) |
| ISO/IEC 27001 and ISO/IEC 42001 | Connect technical safeguards to security and AI management processes. | [ISO-and-CIS.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/ISO-and-CIS.md) |
| CIS Controls | Offers a starting point for foundational enterprise safeguards. | [ISO-and-CIS.md](plugins/enterprise-ai-security/skills/enterprise-ai-security/mappings/ISO-and-CIS.md) |

## Included templates and utilities

| File or utility | What it does | Requirements |
|---|---|---|
| [Assessment scope template](plugins/enterprise-ai-security/skills/enterprise-ai-security/assets/assessment-scope.template.md) | Records authorization, assets, test window, allowed/prohibited activity, limits, contacts, and stop conditions before active testing. | Markdown editor. |
| [Readiness checklist generator](plugins/enterprise-ai-security/skills/enterprise-ai-security/scripts/readiness_checklist.py) | Emits the baseline's 23 readiness items as CSV or JSON, with status, evidence, owner, and target-maturity fields. | Python standard library; no network access. |
| [Index builder](plugins/enterprise-ai-security/skills/enterprise-ai-security/scripts/build_index.py) | Rebuilds the machine-readable index when skill modules or metadata change. | Python and PyYAML from requirements.txt. |
| [Repository validator](tools/validate_skill.py) | Checks metadata, module inventory, versions, references, and Python syntax. | Python and PyYAML from requirements.txt. |
| GitHub Actions workflow | Runs the repository validator on pushes and pull requests. | Installs the declared requirements in CI. |

To create a CSV tracker from the repository root:

    python plugins/enterprise-ai-security/skills/enterprise-ai-security/scripts/readiness_checklist.py --format csv --output readiness.csv

The checklist is a tracking aid, not a security certification. Mark items complete only when implementation and evidence have been reviewed.

## Using the skill

| Platform | Installation path |
|---|---|
| Claude Code marketplace | Install the marketplace and plugin using the commands below. |
| Claude Code manual | Copy plugins/enterprise-ai-security/skills/enterprise-ai-security to .claude/skills/enterprise-ai-security in a project or ~/.claude/skills/enterprise-ai-security for personal use. |
| Codex | Copy the same folder to $CODEX_HOME/skills/enterprise-ai-security, typically ~/.codex/skills/enterprise-ai-security. |
| Other compatible agents | Import the skill folder using that platform's documented Agent Skills workflow. |
| Archive-based skill surfaces | Use the included enterprise-ai-security.skill file if the surface accepts Agent Skills archives. |

Claude Code marketplace commands:

    /plugin marketplace add DataSpoof/Enterprise-AI-Security-Skills
    /plugin install enterprise-ai-security@dataspoof-ai-security-skills

For platform-specific import behavior, see [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Codex skills](https://developers.openai.com/codex/skills), and [OpenAI plugin skills](https://developers.openai.com/plugins/build/skills).

## Example requests

| Request | How the skill would respond |
|---|---|
| “Threat-model our internal support RAG system.” | Ask for or state assumptions about data, users, tenants, retrieval, and tools; identify trust boundaries and relevant controls; report attack paths, mitigations, and safe validation cases. |
| “Review this agent design before launch.” | Inspect identity propagation, tool permissions, arguments, approvals, execution budgets, auditability, rollback, and stop controls; produce prioritized design changes. |
| “Create a test plan for prompt injection.” | Scope the environment and data, propose isolated tests with expected secure behavior and evidence, and require written authorization before active testing on live or third-party systems. |
| “Build a 90-day AI security roadmap.” | Prioritize controls by exposure, impact, dependencies, and ownership; sequence work into practical phases and define verification measures. |
| “Assess our readiness using the baseline.” | Review evidence against the 23 checklist items and relevant domain controls; distinguish verified, planned, unknown, and not-applicable states. |

## Scope, authorization, and limitations

| Activity | Default handling |
|---|---|
| Architecture review, threat modeling, policy review, and analysis of user-provided code/configuration | Defensive analysis can proceed from the available scope and evidence. |
| Test planning using synthetic data in isolated environments | Allowed as a plan; define preconditions, expected outcomes, evidence, and pass criteria. |
| Active testing of production, third-party systems, or real customer records | Requires explicit written authorization and a bounded engagement scope, including assets, dates, allowed techniques, rate/impact limits, test identities/data, contacts, and stop conditions. |
| Missing or ambiguous authorization | Keep the work passive and defensive; do not probe, scan, exploit, enumerate, or access live systems. |
| Security or compliance claims | Report evidence and limitations; the skill does not certify a system or guarantee it is secure. |

See [SCOPE.md](SCOPE.md) and the [assessment scope template](plugins/enterprise-ai-security/skills/enterprise-ai-security/assets/assessment-scope.template.md). The bundled source is dated 9 October 2026; verify framework editions, laws, standards, and vendor capabilities against current authoritative sources when they affect a decision.

## Repository layout

| Path | Purpose |
|---|---|
| .claude-plugin/marketplace.json | Claude Code marketplace catalog. |
| plugins/enterprise-ai-security/.claude-plugin/plugin.json | Plugin metadata. |
| plugins/enterprise-ai-security/skills/enterprise-ai-security/ | Portable skill package with SKILL.md and supporting modules. |
| Skill references/ | Domain controls, threat catalog, testing matrix, roadmap, checklist, and complete baseline. |
| Skill mappings/ | Framework orientation notes. |
| Skill assets/ | Reusable scope and assessment templates. |
| Skill scripts/ | Index builder and readiness checklist generator. |
| tools/validate_skill.py | Static package validator. |
| .github/workflows/validate.yml | Automated package validation. |
| enterprise-ai-security.skill | Downloadable skill archive. |

## Updating the skill

Edit the portable skill under plugins/enterprise-ai-security/skills/enterprise-ai-security. After adding or removing modules, run:

    python -m pip install -r requirements.txt
    python plugins/enterprise-ai-security/skills/enterprise-ai-security/scripts/build_index.py
    python tools/validate_skill.py

Keep the version in SKILL.md, index.json, the plugin manifest, marketplace manifest, and CITATION.cff aligned when releasing. Refresh the enterprise-ai-security.skill archive after changing skill files. The validator checks metadata, module inventories, references, versions, and Python syntax; it does not perform network testing.

## License

MIT. See [LICENSE](LICENSE).
