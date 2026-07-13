# A.I.M. Co-Agents (The DNA Bank)

This repository is the central **DNA Bank** and **Antigravity Skill** for the A.I.M. Operating System's Sovereign Swarm architecture.

It upgrades the default, ephemeral "subagent" architecture into true independent colleagues. Rather than throwing away context when a subagent dies, Co-Agents are full OS clones running in isolated directories with their own LanceDB memory pools.

## 🧬 How to Spawn a Co-Agent

You do not need to clone this repository manually to spawn an agent! 

The core A.I.M. engine (`aim-agy`) comes with a built-in bash installer specifically for provisioning Co-Agents. You simply execute it in a new folder and provide the name of the blueprint from this repo's `blueprints/` directory.

```bash
mkdir -p ~/aim-agents/dev-node-1
cd ~/aim-agents/dev-node-1

# This automatically fetches the 'python-developer' DNA from this repo!
curl -fsSL https://raw.githubusercontent.com/BrianV1981/aim-agy/main/install-agent.sh | bash -s python-developer
```

## 🛠 Adding Custom Co-Agents

This repository is infinitely extensible. To create a new specialized Co-Agent for the community or your own use:

1. Create a new folder in `blueprints/` (e.g., `blueprints/database-architect`).
2. Add your custom `AGENTS.md` (the rules) and `TOOLS.md` (the allowed API tools).
3. Commit it to GitHub.

Once merged, anyone can immediately spawn your agent by running:
`curl -fsSL .../install-agent.sh | bash -s database-architect`

## 🧠 For Antigravity Agents (The Skill)

If you are an A.I.M. agent running on Antigravity, you can install this entire repository as a **Skill** so you inherently know how to delegate work to Co-Agents automatically.

```bash
git clone https://github.com/BrianV1981/aim-coagents.git ~/.gemini/skills/aim-coagents
```

Once installed, your base LLM will read `SKILL.md` on boot, overriding its default `invoke_subagent` instructions with the exact Bash commands needed to spawn a true Sovereign node.
<!-- AIM_ECOSYSTEM_START -->
### 🧬 The A.I.M. Ecosystem

Modular A.I.M. (Actual Intelligent Memory) repositories. **Flagship engine: [aim-agy](https://github.com/BrianV1981/aim-agy).**

**Active vessels (CLI hosts):**
- **[aim-agy](https://github.com/BrianV1981/aim-agy)** — Core engine (Antigravity / post–Gemini-CLI line). *Flagship.*
- **[aim-grok](https://github.com/BrianV1981/aim-grok)** — Grok CLI vessel (hybrid memory, GitOps, wiki).
- **[aim-opencode](https://github.com/BrianV1981/aim-opencode)** — OpenCode CLI vessel.
- **[aim-codex](https://github.com/BrianV1981/aim-codex)** — Codex-native vessel (**on the horizon** — not deprecated).

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
- **aim-claude / Anthropic-line vessels** — **Done.** Operator does not develop against Anthropic. Use aim-agy / aim-grok / aim-opencode (or aim-codex when ready).

Full map: see **aim-skills** `docs/AIM_ECOSYSTEM_MAP.md` or Operator artifact `AIM_ECOSYSTEM_MAP.md`.
<!-- AIM_ECOSYSTEM_END -->
