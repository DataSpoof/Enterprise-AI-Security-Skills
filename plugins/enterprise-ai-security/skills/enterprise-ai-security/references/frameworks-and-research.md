# frameworks and research

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
