# advanced threat catalog

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
