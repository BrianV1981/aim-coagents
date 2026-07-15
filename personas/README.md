# Personas

**Skills** teach tools. **Personas** teach roles. **Co-agents** are full peers spawned from blueprints.

| Layer | What | This repo |
|-------|------|-----------|
| **Persona** | Role prompt only — same session / subagent hat | `personas/<name>/PERSONA.md` |
| **Blueprint** | Full DNA (rules + tools) for a sovereign peer | `blueprints/<name>/` |
| **Live co-agent** | Provisioned peer (own dir, memory, often tmux) | Spawn via aim-agy `install-agent.sh` |

## Available personas

| Persona | File | Role |
|---------|------|------|
| **technical-auditor** | `technical-auditor/PERSONA.md` | Scoped architectural review |
| **python-specialist** | `python-specialist/PERSONA.md` | TDD-first Python implementer |

## How to use

1. Open the `PERSONA.md` for the role.  
2. Paste / attach it when the Operator wants that hat (or load it as a system/role prompt for a subagent).  
3. Pair with **skills** from [aim-skill-library](https://github.com/BrianV1981/aim-skill-library) and companions (browser, google, …) as needed.  
4. Need a **lasting peer** with its own memory? Use a **blueprint** + spawn — not a persona alone.

Personas are **not** installed into vessel `.grok/skills` / `.gemini/skills` tool menus by default.
