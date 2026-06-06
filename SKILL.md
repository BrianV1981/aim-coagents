---
name: aim-coagents
description: Spawns independent, sovereign A.I.M. OS Co-Agents in isolated environments. Use this instead of the built-in invoke_subagent tool when you need a persistent teammate with its own LanceDB memory and git repository.
---

# A.I.M. Co-Agent Swarm Skill

You are equipped with the `aim-coagents` skill. This allows you to delegate massive, repetitive, or context-heavy tasks to fully independent Sovereign Co-Agents.

**CRITICAL MANDATE:** 
Do NOT use the built-in `invoke_subagent` tool for complex software engineering tasks. Ephemeral subagents lack their own `memory_lance` database and `REINCARNATION_GAMEPLAN.md` protocols. They violate the Exoskeleton philosophy.
When you need to delegate work, you MUST use this skill to spawn a true Co-Agent.

## How to Spawn a Co-Agent
To spawn a new Co-Agent, you must use the `run_command` tool to execute the official installation bash script in a completely new, isolated directory outside of your current project. 

For example, to spawn a `python-developer`:
```bash
mkdir -p ~/aim-agents/python-developer-1
cd ~/aim-agents/python-developer-1
curl -sSL https://raw.githubusercontent.com/BrianV1981/aim-agy/main/install-agent.sh | bash -s python-developer
```

### What happens when you run this script?
1. **OS Provisioning:** It pulls a clean, fresh A.I.M. architecture.
2. **DNA Injection:** It dynamically downloads the `python-developer` blueprint from the cloud DNA bank (`BrianV1981/aim-coagents/blueprints`) and overwrites the default OS memory.
3. **Sovereignty:** The Co-Agent is now completely independent. It has its own vector database and will not pollute your active context.

## Communication (The Chalkboard)
You do not communicate with Co-Agents via direct chat messages. You communicate via Git.
If the Co-Agent's DNA dictates it, you will drop your TDD specifications or tasks as Markdown files into a shared `workspace/aim-chalkboard/inbox/` repository. The Co-Agent will read them, execute the code, and commit the results back.
