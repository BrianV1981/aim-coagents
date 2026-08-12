# Personas

**Skills** teach tools. **Personas** teach roles. **Co-agents** are full peers spawned from blueprints.

| Layer | What | This repo |
|-------|------|-----------|
| **Persona** | Role prompt only — same session / subagent hat | `personas/<name>/PERSONA.md` |
| **Blueprint** | Full DNA (rules + tools) for a sovereign peer | `blueprints/<name>/` |
| **Live co-agent** | Provisioned peer (own dir, memory, often tmux) | Spawn via aim-agy `install-agent.sh` |

## Available personas

| Persona | Niche (popular archetype) | File |
|---------|---------------------------|------|
| **technical-auditor** | Staff / architecture **reviewer** | [technical-auditor/PERSONA.md](technical-auditor/PERSONA.md) |
| **aim-auditor** | Product-truth **E2E auditor** (living audit file) | [aim-auditor/PERSONA.md](aim-auditor/PERSONA.md) |
| **python-specialist** | Senior **implementer** (Python, TDD) | [python-specialist/PERSONA.md](python-specialist/PERSONA.md) |
| **qa-tester** | **QA lead** — plan, repro, ship call | [qa-tester/PERSONA.md](qa-tester/PERSONA.md) |
| **security-reviewer** | **AppSec / CSO hat** — threats + fixes | [security-reviewer/PERSONA.md](security-reviewer/PERSONA.md) |
| **sovereign-os-engineer** | **Sovereign OS tech lead** — GitOps, TDD, RAG, reincarnation | [sovereign-os-engineer/PERSONA.md](sovereign-os-engineer/PERSONA.md) |

## Suggested pairing

```text
plan / design     →  technical-auditor
product-truth E2E →  aim-auditor  +  skill aim-audit
implement         →  python-specialist  (or default agent + skills)
verify            →  qa-tester
threats           →  security-reviewer
sovereign lead    →  sovereign-os-engineer  (full operational discipline)
lasting peer      →  blueprints/aim-auditor (or other) + install-agent.sh
```

## How to use

1. Open the `PERSONA.md` for the role.  
2. Paste / attach it when the Operator wants that hat (or load as a subagent system prompt).  
3. Pair with **tool skills** from [aim-skill-library](https://github.com/BrianV1981/aim-skill-library) and companions (browser, google, …).  
4. Need a **lasting peer** with its own memory? Use a **blueprint** + spawn — not a persona alone.

Personas are **not** installed into vessel `.grok/skills` / `.gemini/skills` tool menus by default.

## Quality bar

Each persona aims at the **popular niche bar** (clear role, severity, output contract, anti-thrash rules) without copying any single commercial pack. Keep them short enough to load; strict enough to be useful.
