# A.I.M. Co-Agents (Native Antigravity Skill)

This repository is the **Co-Agent Orchestration Skill** for the A.I.M. Operating System running on the Antigravity CLI. 

It upgrades the default, ephemeral "subagent" architecture into a true Sovereign Swarm. Rather than throwing away context when a subagent dies, this skill allows the Main Architect Agent to spawn fully independent **Co-Agents** in isolated `tmux` sessions. Each Co-Agent has its own OS layer, its own LanceDB memory pool, and its own `REINCARNATION_GAMEPLAN.md` protocol.

## Installation

This is a native Antigravity CLI Skill. Do not clone it into your project root.

1. Clone this repository directly into your Antigravity skills directory:
   ```bash
   git clone https://github.com/BrianV1981/aim-coagents.git ~/.gemini/skills/aim-coagents
   ```
2. That's it. Your A.I.M. agent will now automatically read `SKILL.md` when it wakes up and will know how to spawn Co-Agents when you ask it to delegate work.

## The Architecture
By packaging the swarm logic as an Antigravity Skill, it acts as a permanent upgrade to your agent's capabilities:
1. **The Factory (`scripts/aim_spawn.py`):** The main agent executes this to provision new Co-Agents. It clones a fresh, isolated A.I.M. OS from the upstream engine repo into a `teams/` directory, injects the custom blueprint, and sets up a GitOps chalkboard.
2. **The Chalkboard (`workspace/aim-chalkboard/`):** Agents do not chat. They communicate asynchronously via Git commits in a shared post office repository, preventing UI lockups and preserving context windows.
3. **The Blueprints (`blueprints/`):** Contains the specialized DNA (instructions, tools, manifests) for different roles (e.g., `python-developer`).