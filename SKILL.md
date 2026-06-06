---
name: aim-coagents
description: Spawns independent, sovereign A.I.M. OS Co-Agents in isolated tmux sessions. Use this instead of the built-in invoke_subagent tool when you need a persistent teammate with its own LanceDB memory and git repository.
---

# A.I.M. Co-Agent Swarm Skill

You are equipped with the `aim-coagents` skill. This allows you to delegate massive, repetitive, or context-heavy tasks to fully independent Sovereign Co-Agents.

**CRITICAL MANDATE:** 
Do NOT use the built-in `invoke_subagent` tool for complex software engineering tasks. Ephemeral subagents lack their own `memory_lance` database and `REINCARNATION_GAMEPLAN.md` protocols. They violate the Exoskeleton philosophy.
When you need to delegate work, you MUST use this skill to spawn a true Co-Agent.

## How to Spawn a Co-Agent
To spawn a new Co-Agent, execute the factory script using the `run_command` tool:

```bash
python3 ~/.gemini/skills/aim-coagents/scripts/aim_spawn.py <role_name>
```

Currently available roles (blueprints):
- `python-developer`

### What happens when you run this script?
1. **Cloning:** The script will automatically clone the active A.I.M. architecture into `teams/<role_name>/`.
2. **Injection:** It will inject the specific persona blueprint into the clone.
3. **Chalkboard:** It initializes a local Git repository at `workspace/aim-chalkboard/` which acts as the asynchronous communication hub between you and the Co-Agent.
4. **Booting:** You can then boot the agent visually using:
   ```bash
   python3 ~/.gemini/skills/aim-coagents/scripts/aim_team.py default_team
   ```

## Communication (The Chalkboard)
You do not communicate with Co-Agents via direct chat messages. You communicate via Git.
Drop your TDD specifications or tasks as Markdown files into the `workspace/aim-chalkboard/inbox/` directory, and commit them. The Co-Agent will read them, execute the code, and commit the results back.
