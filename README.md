# A.I.M. Swarm Extension

This repository is the **Swarm Orchestration Extension** for the A.I.M. (Actual Intelligent Memory) Operating System. 

It is designed as a standalone, modular add-on. Rather than mutating the base A.I.M. engine, this repository provides specialized factory scripts, Orchestrator personas, and agent blueprints that run *on top* of a globally installed A.I.M. core.

## The Architecture
By decoupling the swarm logic from the A.I.M. OS, `aim-swarm` serves as a pure orchestration layer:
1. **The Factory (`swarm/aim_spawn.py`):** Provisions new agents by cloning a fresh, isolated A.I.M. OS from the upstream engine repository, injecting the custom persona blueprint into it, and setting up an asynchronous git-based chalkboard for inter-agent communication.
2. **The Tmux Orchestrator (`swarm/aim_team.py`):** Splits your terminal into a live grid, booting up each specialized agent in its own isolated pane, and passing session metadata so agents can asynchronously paste multiline responses back to you without UI lockups.
3. **The Blueprints (`agents/`):** Contains the specialized DNA (instructions, tools, manifests) for different roles (e.g., `python-developer`).

## Installation for A.I.M. Agents

If you are an A.I.M. agent tasked with deploying a swarm:

1. Clone this repository into your working directory:
   ```bash
   git clone https://github.com/BrianV1981/aim-swarm.git my-swarm-project
   cd my-swarm-project
   ```
2. Review the `AGENTS.md` and `TOOLS.md` files in this repository to adopt the **Swarm Architect** persona.
3. To spawn a new team member (e.g., the `python-developer`), use the factory script:
   ```bash
   python3 swarm/aim_spawn.py python-developer
   ```
   *This will clone the base A.I.M. OS into `teams/python-developer/`, inject the blueprint, and set up the GitOps chalkboard.*
4. Boot the team visually using the Tmux orchestrator:
   ```bash
   python3 swarm/aim_team.py default_team
   ```