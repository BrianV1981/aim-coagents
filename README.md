# A.I.M. Co-Agents (The DNA Bank)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support%20solo%20dev-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/BrianV1981)

Central **DNA bank** for A.I.M.: **personas** (roles) and **blueprints** (sovereign co-agent DNA).

**Skills** teach tools. **Personas** teach roles. **Co-agents** are full peers spawned from blueprints.

| Layer | What | Path |
|-------|------|------|
| **Persona** | Role prompt only — hat for this session / subagent | [`personas/`](personas/) |
| **Blueprint** | Full DNA (rules + tools) for a lasting peer | [`blueprints/`](blueprints/) |
| **Live co-agent** | Isolated OS clone (own dir, memory, often tmux) | Spawn via **aim-joshua** `joshua_os/install-agent.sh` |

This upgrades throwaway “subagents” into optional **colleagues** when you need persistence — without forcing every task into a full spawn.

---

## Personas (roles)

Lightweight. No spawn required. See [`personas/README.md`](personas/README.md).

| Persona | Role |
|---------|------|
| [technical-auditor](personas/technical-auditor/PERSONA.md) | Staff-level architecture / design audit |
| [aim-auditor](personas/aim-auditor/PERSONA.md) | Product-truth E2E auditor (living `AUDIT_<SLUG>.md`) |
| [python-specialist](personas/python-specialist/PERSONA.md) | TDD-first Python implementer |
| [qa-tester](personas/qa-tester/PERSONA.md) | QA lead — risk-based plan, repro, ship call |
| [security-reviewer](personas/security-reviewer/PERSONA.md) | AppSec review — exploit scenario + fix |
| [sovereign-os-engineer](personas/sovereign-os-engineer/PERSONA.md) | Sovereign OS tech lead — GitOps, TDD, RAG, handoff |
| [b2b-content-creator](personas/b2b-content-creator/PERSONA.md) | Node / Next.js Content & SEO Architect (Markdown + YAML frontmatter + `npm run build` gate) |
| [tbsoftwash-content-creator](personas/tbsoftwash-content-creator/PERSONA.md) | WordPress PHP Content & SEO Architect (`blog-*.php` + Router SEO + local `1200px` WebP + guardrail gate) |

**Typical flow:** design review (`technical-auditor`) or product-truth (`aim-auditor`) → implementer → QA → security (as needed).  
Open the `PERSONA.md`, attach or paste when the Operator wants that hat. Pair with tool skills from [aim-skill-library](https://github.com/BrianV1981/aim-skill-library) as needed.

---

## Blueprints (sovereign co-agents)

Full peers: own directory, own memory pool, own lifecycle.

### Spawn (via aim-joshua)

You do not need to clone this repo by hand for a standard spawn:

```bash
mkdir -p ~/aim-agents/dev-node-1
cd ~/aim-agents/dev-node-1

curl -fsSL https://raw.githubusercontent.com/BrianV1981/aim-joshua/main/joshua_os/install-agent.sh | bash -s python-developer
```

That injects DNA from `blueprints/<name>/` into a fresh agent home.

### Add a blueprint

1. Create `blueprints/<name>/` with `AGENTS.md` (rules) and `TOOLS.md` (allowed tools).  
2. Commit and push.  
3. Spawn with: `…/install-agent.sh | bash -s <name>`

Current blueprints: see `blueprints/` (`python-developer`, `aim-auditor`, `lead-analyst`, `content-node`, `content-wordpress`).

---

## Communication & Skill install (optional)

So a vessel *knows how to spawn* and talk to co-agents, clone this repo:

```bash
git clone https://github.com/BrianV1981/aim-coagents.git ~/.gemini/skills/aim-coagents
# or link into .grok/skills / .opencode/skills as your host prefers
```

Read [`SKILL.md`](SKILL.md) for spawn and communication notes (`aim-communicate` via tmux for same-host, `aim-chalkboard` for out-of-network).

---

## Support

Solo-built. Optional: **[Buy Me a Coffee](https://www.buymeacoffee.com/BrianV1981)**.

---

<!-- AIM_ECOSYSTEM_START -->
### 🧬 The A.I.M. Ecosystem

AIM-Coagents is just one module in the larger A.I.M. (Actual Intelligent Memory) architecture. 

To see how the sovereign OS, AI agents, MCP servers, and terminal multiplexers all connect, please visit the central ecosystem repository:

👉 **[The A.I.M. Ecosystem Directory](https://github.com/BrianV1981/aim-ecosystem)**
<!-- AIM_ECOSYSTEM_END -->
