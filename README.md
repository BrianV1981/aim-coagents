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