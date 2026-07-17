# A.I.M. Co-Agents (The DNA Bank)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support%20solo%20dev-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/BrianV1981)

Central **DNA bank** for A.I.M.: **personas** (roles) and **blueprints** (sovereign co-agent DNA).

**Skills** teach tools. **Personas** teach roles. **Co-agents** are full peers spawned from blueprints.

| Layer | What | Path |
|-------|------|------|
| **Persona** | Role prompt only — hat for this session / subagent | [`personas/`](personas/) |
| **Blueprint** | Full DNA (rules + tools) for a lasting peer | [`blueprints/`](blueprints/) |
| **Live co-agent** | Isolated OS clone (own dir, memory, often tmux) | Spawn via **aim-agy** `install-agent.sh` |

This upgrades throwaway “subagents” into optional **colleagues** when you need persistence — without forcing every task into a full spawn.

---

## Personas (roles)

Lightweight. No spawn required. See [`personas/README.md`](personas/README.md).

| Persona | Role |
|---------|------|
| [technical-auditor](personas/technical-auditor/PERSONA.md) | Staff-level architecture / design audit |
| [python-specialist](personas/python-specialist/PERSONA.md) | TDD-first Python implementer |
| [qa-tester](personas/qa-tester/PERSONA.md) | QA lead — risk-based plan, repro, ship call |
| [security-reviewer](personas/security-reviewer/PERSONA.md) | AppSec review — exploit scenario + fix |

**Typical flow:** auditor → implementer → QA → security (as needed).  
Open the `PERSONA.md`, attach or paste when the Operator wants that hat. Pair with tool skills from [aim-skill-library](https://github.com/BrianV1981/aim-skill-library) as needed.

---

## Blueprints (sovereign co-agents)

Full peers: own directory, own memory pool, own lifecycle.

### Spawn (via aim-agy)

You do not need to clone this repo by hand for a standard spawn:

```bash
mkdir -p ~/aim-agents/dev-node-1
cd ~/aim-agents/dev-node-1

curl -fsSL https://raw.githubusercontent.com/BrianV1981/aim-agy/main/install-agent.sh | bash -s python-developer
```

That injects DNA from `blueprints/<name>/` into a fresh agent home.

### Add a blueprint

1. Create `blueprints/<name>/` with `AGENTS.md` (rules) and `TOOLS.md` (allowed tools).  
2. Commit and push.  
3. Spawn with: `…/install-agent.sh | bash -s <name>`

Current blueprints: see `blueprints/` (e.g. `python-developer`).

---

## Skill install (optional)

So a vessel *knows how to spawn* co-agents (not the same as loading a persona):

```bash
git clone https://github.com/BrianV1981/aim-coagents.git ~/.gemini/skills/aim-coagents
# or link into .grok/skills / .opencode/skills as your host prefers
```

Read [`SKILL.md`](SKILL.md) for spawn + knock/swarm messaging notes.

---

## Support

Solo-built. Optional: **[Buy Me a Coffee](https://www.buymeacoffee.com/BrianV1981)**.

---

<!-- AIM_ECOSYSTEM_START -->
### 🧬 The A.I.M. Ecosystem

Modular A.I.M. (Actual Intelligent Memory) repositories. **Flagship engine: [aim-agy](https://github.com/BrianV1981/aim-agy).**

**Active vessels (CLI hosts):**
- **[aim-agy](https://github.com/BrianV1981/aim-agy)** — Core engine / *soul* (Antigravity CLI). *Flagship.* Shared nested `aim-agy_os/` ships here first.
- **[aim-grok](https://github.com/BrianV1981/aim-grok)** — Grok CLI vessel (hybrid memory, GitOps, wiki, fleet orchestration tooling).
- **[aim-opencode](https://github.com/BrianV1981/aim-opencode)** — OpenCode CLI vessel.
- **[aim-codex](https://github.com/BrianV1981/aim-codex)** — OpenAI Codex CLI vessel (greenfield nested soul + Codex overlays; primary `main`).

**Tools & workspaces:**
- **[aim-connect](https://github.com/BrianV1981/aim-connect)** — Self-hosted remote workspace web UI.
- **[aim-tmux-dashboard](https://github.com/BrianV1981/aim-tmux-dashboard)** — Terminal multi-session monitor.
- **[aim-browser](https://github.com/BrianV1981/aim-browser)** — Headed Chromium CDP engine + browser **skill suite**.
- **[aim-google](https://github.com/BrianV1981/aim-google)** — Google Workspace CLI (Gmail, Drive, Calendar, …).
- **[aim-flight-recorder](https://github.com/BrianV1981/aim-flight-recorder)** — Forensic Markdown session extractor.
- **[aim-boardroom](https://github.com/BrianV1981/aim-boardroom)** — Multi-agent orchestration room (OS multiplexing + artifacts).
- **[aim-skills](https://github.com/BrianV1981/aim-skills)** — **Skills index / multi-CLI install registry** (agy, grok, opencode, codex).

**DNA, comms & lore:**
- **[aim-coagents](https://github.com/BrianV1981/aim-coagents)** — DNA bank for sovereign co-agent blueprints.
- **[aim-knowledge](https://github.com/BrianV1981/aim-knowledge)** — Public Obsidian vault / deep-lore archive.
- **[aim-chalkboard](https://github.com/BrianV1981/aim-chalkboard)** — Optional cross-host async git mailbox (PoC; default same-host comms = **aim-communicate** skill).

**Deprecated / not maintained:**
- **[aim](https://github.com/BrianV1981/aim)** — Original **Gemini CLI** framework. Deprecated after loss of practical subscription access; **Great Migration → aim-agy**.
- **[aim-swarm](https://github.com/BrianV1981/aim-swarm)** — Legacy Python swarm factory → use **aim-coagents** + aim-agy spawn.
- **aim-claude / Anthropic-line vessels** — **Done.** Operator does not develop against Anthropic. Use **aim-agy / aim-grok / aim-opencode / aim-codex**.

Full map: see **aim-skills** `docs/AIM_ECOSYSTEM_MAP.md` or Operator artifact `AIM_ECOSYSTEM_MAP.md`.
<!-- AIM_ECOSYSTEM_END -->
