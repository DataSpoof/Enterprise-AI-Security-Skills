# Enterprise AI Security skill

This portable Agent Skill helps an AI assistant apply an enterprise security roadmap to LLM, RAG, and agentic AI systems. The complete source document is included at `references/enterprise-ai-security-baseline.md`; the `SKILL.md` explains how to apply it and preserve its control IDs.

## Package contents

- `SKILL.md` — portable skill instructions and discovery metadata.
- `references/enterprise-ai-security-baseline.md` — complete source text supplied for this skill.

The folder uses the shared `SKILL.md` plus YAML `name` and `description` structure supported by Claude Agent Skills and OpenAI/Codex skills. No platform-specific metadata, scripts, network access, or external dependencies are required.

## Use it

- **Codex / ChatGPT local skills:** place this folder under `.agents/skills/` in a repository, or under the user skills directory supported by your installation.
- **Claude Code:** place this folder under `.claude/skills/` in a project or `~/.claude/skills/` for personal use.
- **Claude.ai or an API skill surface:** upload the folder or a ZIP containing this top-level folder where that product supports custom skills. Product surfaces have separate upload and sharing settings.
- **OpenAI Skills API or plugins:** use the platform's skill upload or plugin packaging flow. This package contains one skill folder and one `SKILL.md` manifest.

Check the platform's current documentation for its installation path and upload flow:

- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenAI Codex skills](https://developers.openai.com/codex/skills)
- [Build skills for OpenAI plugins](https://developers.openai.com/plugins/build/skills)

The source document is bundled as provided. Its dated framework and product claims should be checked against authoritative current sources when they affect a decision.
