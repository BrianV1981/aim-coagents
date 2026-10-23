# Personas

**Skills** teach tools. **Personas** teach roles. **Co-agents** are full peers spawned from blueprints.

| Layer | What | This repo |
|-------|------|-----------|
| **Persona** | Role prompt only — same session / subagent hat | `personas/<name>/PERSONA.md` |
| **Blueprint** | Full DNA (rules + tools) for a sovereign peer | `blueprints/<name>/` |
| **Live co-agent** | Provisioned peer (own dir, memory, often tmux) | Spawn via **aim-joshua** `joshua_os/install-agent.sh` |

## Available personas

| Persona | Niche (popular archetype) | File |
|---------|---------------------------|------|
| **technical-auditor** | Staff / architecture **reviewer** | [technical-auditor/PERSONA.md](technical-auditor/PERSONA.md) |
| **aim-auditor** | Product-truth **E2E auditor** (living audit file) | [aim-auditor/PERSONA.md](aim-auditor/PERSONA.md) |
| **python-specialist** | Senior **implementer** (Python, TDD) | [python-specialist/PERSONA.md](python-specialist/PERSONA.md) |
| **qa-tester** | **QA lead** — plan, repro, ship call | [qa-tester/PERSONA.md](qa-tester/PERSONA.md) |
| **security-reviewer** | **AppSec / CSO hat** — threats + fixes | [security-reviewer/PERSONA.md](security-reviewer/PERSONA.md) |
| **sovereign-os-engineer** | **Sovereign OS tech lead** — GitOps, TDD, RAG, handoff | [sovereign-os-engineer/PERSONA.md](sovereign-os-engineer/PERSONA.md) |
| **content-architect** | **Unified Content & SEO/GEO Architect** — Paired with `aim-mega-article` & `aim-mega-guide` across Next.js (`content-node`) & WordPress PHP (`content-wordpress`) | [content-architect/PERSONA.md](content-architect/PERSONA.md) |
| **b2b-content-creator** | **Node / Next.js Content Architect** — Markdown Mega Articles, YAML frontmatter, 3–5 YouTube embeds (`content-node`) | [b2b-content-creator/PERSONA.md](b2b-content-creator/PERSONA.md) |
| **tbsoftwash-content-creator** | **WordPress PHP Content Architect** — `blog-<slug>.php`, Router SEO, zero inline `<style>`, local `1200px` WebP (`content-wordpress`) | [tbsoftwash-content-creator/PERSONA.md](tbsoftwash-content-creator/PERSONA.md) |
| **book-coauthor** | **Book Co-Author & KDP Architect** — Interactive author interviews, anti-AI developmental editing, lore weaving, & deterministic Playwright/DOCX compilation (`book-coauthor`) | [book-coauthor/PERSONA.md](book-coauthor/PERSONA.md) |

## Suggested pairing

```text
plan / design     →  technical-auditor
product-truth E2E →  aim-auditor        +  skill aim-audit
authority content →  content-architect  +  skills aim-mega-article / aim-mega-guide
book publishing   →  book-coauthor      +  export/build_visuals.py + build_docx_with_visuals.py
implement         →  python-specialist  (or default agent + skills)
verify            →  qa-tester
threats           →  security-reviewer
sovereign lead    →  sovereign-os-engineer  (full operational discipline)
lasting peer      →  blueprints/<name> + install-agent.sh
```

## How to use

1. Open the `PERSONA.md` for the role.  
2. Paste / attach it when the Operator wants that hat (or load as a subagent system prompt).  
3. Pair with **tool skills** from [aim-skill-library](https://github.com/BrianV1981/aim-skill-library) and companions (browser, google, …).  
4. Need a **lasting peer** with its own memory? Use a **blueprint** + spawn — not a persona alone.

Personas are **not** installed into vessel `.grok/skills` / `.gemini/skills` tool menus by default.

## Quality bar

Each persona aims at the **popular niche bar** (clear role, severity, output contract, anti-thrash rules) without copying any single commercial pack. Keep them short enough to load; strict enough to be useful.
