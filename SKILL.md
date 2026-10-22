---
name: aim-coagents
description: Spawns independent, sovereign A.I.M. OS Co-Agents in isolated environments. Use this instead of the built-in invoke_subagent tool when you need a persistent teammate with its own LanceDB memory and git repository.
---

# A.I.M. Co-Agent Swarm Skill

You are equipped with the `aim-coagents` skill: **personas** (role prompts) and **blueprints** (sovereign peers).

**Taxonomy:** Skills teach tools. Personas teach roles (`personas/*/PERSONA.md`). Co-agents are full peers from `blueprints/` + spawn.

**When to spawn a co-agent (not a persona):** long-running work that needs its own memory, isolation, or parallel desk session. For a one-shot role (audit, Python implementer), load a **persona** file instead of spawning.

**CRITICAL MANDATE:**  
Do NOT use the built-in `invoke_subagent` tool for complex software engineering tasks that need lasting memory. Ephemeral subagents lack their own `memory_lance` and reincarnation protocols. When you need a true independent peer, spawn a Co-Agent.

## How to Spawn a Co-Agent
To spawn a new Co-Agent, you must use the `run_command` tool to execute the official installation bash script in a completely new, isolated directory outside of your current project. 

For example, to spawn a `python-developer`:
```bash
mkdir -p ~/aim-agents/python-developer-1
cd ~/aim-agents/python-developer-1
curl -fsSL https://raw.githubusercontent.com/BrianV1981/aim-joshua/main/joshua_os/install-agent.sh | bash -s python-developer
```

### What happens when you run this script?
1. **OS Provisioning:** It pulls a clean, fresh A.I.M. architecture.
2. **DNA Injection:** It dynamically downloads the `python-developer` blueprint from the cloud DNA bank (`BrianV1981/aim-coagents/blueprints`) and overwrites the default OS memory.
3. **Sovereignty:** The Co-Agent is now completely independent. It has its own vector database and will not pollute your active context.

## Communication
Co-agents can be worked with just like standard agents! They are literally no different in how you interact with them.

### Same-Host Communication (The Default)
If the agents are on the same server, you will utilize the `aim-communicate` skill (via `tmux`) to perform agent-to-agent (co-agent) communication. You interact with their terminal directly using the `aim-communicate` tool.

### Out-of-Network Communication (The Chalkboard)
If the agents are on different servers or require out-of-network asynchronous coordination, you can pass data via a shared Git repository/mailbox called `workspace/aim-chalkboard/`.
