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

## Communication (The Knock Protocol)
You do not communicate with Co-Agents via direct chat messages. They are completely independent OS instances.

To communicate with a Co-Agent, you MUST use the native A.I.M. Swarm CLI wrapper. This natively implements the "Knock Protocol", an infrastructure guardrail that safely polls the target's terminal to ensure it is idle before injecting your text, preventing catastrophic execution clobbering.

**Usage:**
```bash
python3 .aim_core/aim_cli.py swarm send <session_name> "Your message here"
```
*Example:*
```bash
python3 .aim_core/aim_cli.py swarm send python-developer-1 "Hey, I dropped the new specifications in workspace/aim-chalkboard/inbox/. Let me know when you are done."
```

If the agent is busy running a script, the engine will safely poll up to 30 seconds. If it returns an error that the session is busy, you MUST wait and try again later.

### Legacy Communication (The Chalkboard)
If the project requires massive data handoffs or asynchronous work, you can also drop markdown files into a shared Git repository (`workspace/aim-chalkboard/`). But for direct coordination, rely on the `swarm send` Knock Protocol.
