# Contributing

Contributions should improve practical, evidence-based security for enterprise LLM, RAG, and agentic AI systems.

- Keep the portable skill entry point concise and place topic detail in references.
- Preserve the supplied baseline and its control IDs; make new guidance distinguishable from source material.
- Cite primary sources for framework or product claims and note when a framework edition may change.
- Do not state that a control proves security or compliance without evidence.
- Keep active testing within the repository's authorization policy in SCOPE.md.
- Update the skill index and all version fields when package metadata changes. Use the skill's scripts/build_index.py to refresh its module inventory.
- Run python tools/validate_skill.py before submitting structural or metadata changes.

Small, focused pull requests with a clear reason and affected module are easiest to review.
