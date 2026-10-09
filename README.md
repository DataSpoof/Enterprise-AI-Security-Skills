# Enterprise AI Security Skills

Portable, modular agent skills for assessing and improving enterprise security across LLM, RAG, and agentic AI systems. The repository follows the plugin-plus-skill layout used by DataSpoof's website-security-shield project while keeping the skill content platform-neutral.

## Install

Claude Code marketplace:

    /plugin marketplace add DataSpoof/Enterprise-AI-Security-Skills
    /plugin install enterprise-ai-security@dataspoof-ai-security-skills

Manual installation:

- Claude Code: copy plugins/enterprise-ai-security/skills/enterprise-ai-security to .claude/skills/enterprise-ai-security or ~/.claude/skills/enterprise-ai-security.
- Codex: copy the same skill directory to $CODEX_HOME/skills/enterprise-ai-security (typically ~/.codex/skills/enterprise-ai-security).
- Other agent platforms: use the skill folder's SKILL.md, references, mappings, and assets with the platform's documented skill import mechanism.
- A ready-to-download enterprise-ai-security.skill archive is included for products that accept Agent Skills archives.

See the current platform documentation for supported installation and upload options: [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Codex skills](https://developers.openai.com/codex/skills), and [OpenAI plugin skills](https://developers.openai.com/plugins/build/skills).

## What is included

- One portable skill with YAML metadata and a concise operating workflow.
- Topic-specific control references across all ten enterprise AI security domains.
- Framework mapping notes for OWASP, NIST AI RMF, MITRE ATLAS, Google SAIF, ISO, and CIS.
- The complete supplied baseline, retained verbatim at plugins/enterprise-ai-security/skills/enterprise-ai-security/references/enterprise-ai-security-baseline.md.
- An assessment scope template, readiness checklist generator, index builder, and repository validator.
- A Claude Code marketplace manifest and plugin manifest.

## Security use

Threat modeling, architecture review, secure coding guidance, and local analysis can proceed from the available evidence. Active testing of production systems, third-party systems, or real customer data requires explicit written authorization and a bounded engagement scope. Use synthetic data and isolated environments by default. See SCOPE.md and the template in the skill's assets directory.

## Repository layout

- .claude-plugin and plugins: marketplace and plugin distribution metadata.
- plugins/enterprise-ai-security/skills/enterprise-ai-security: portable skill package.
- references: modular source-derived guidance plus the complete original baseline.
- mappings: framework-oriented crosswalk notes; mappings do not imply certification.
- assets: reusable assessment templates.
- scripts and tools: deterministic package-generation and static validation utilities.
- .github/workflows: automated package checks.

## Updating the skill

Edit the portable skill under plugins/enterprise-ai-security/skills/enterprise-ai-security. After adding or removing modules, run python plugins/enterprise-ai-security/skills/enterprise-ai-security/scripts/build_index.py, then run python tools/validate_skill.py. Keep the index.json version aligned with SKILL.md and the plugin manifests. The validator checks metadata, module inventories, referenced files, package versions, and Python syntax; it does not perform network testing.

## License

MIT. See LICENSE.
