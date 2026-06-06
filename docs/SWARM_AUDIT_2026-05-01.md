# A.I.M. Swarm Repository Audit

> **Date:** 2026-05-01  
> **Auditor:** OpenCode Agent (DeepSeek V4 Pro)  
> **Branch:** `master`  
> **Working Tree:** Clean

---

## Executive Summary

The `aim-swarm` repo has a **clear architectural vision** — sovereign co-agent orchestration via tmux, factory provisioning, chalkboard communication. However, the implementation has critical code-level defects that prevent `aim_team.py` (the primary orchestrator) from even parsing, and `aim_spawn.py` (the factory) from cloning the correct source.

**Overall: 11 files, 0 tests, 0 setup scripts. Two orchestrators overlap in purpose. No build system. One agent blueprint.**

---

## File-by-File Findings

### README.md — Clear vision, broken references

- Good elevator pitch: Factory → Orchestrator → Blueprints
- References `teams/SWARM_MANIFEST.json` and `default_team` — neither exists
- Implies cloning this repo as a starter, but spawn script clones base A.I.M. OS instead

### AGENTS.md — Swarm Architect persona well-defined

- Autonomous execution mode (correct for orchestrator)
- References `continuity/ISSUE_TRACKER.md` — directory doesn't exist in this repo
- References `SOVEREIGN_NODES_ARCHITECTURE.md` — file doesn't exist
- Uses `.geminiignore` — Gemini-specific; needs `.opencodeignore`

### TOOLS.md — Missing tool paths

- References `skills/aim-calc/scripts/aim_calc.py` — doesn't exist in repo (lives in global A.I.M. OS)
- References `~/.local/bin/aim-google` — global binary, not managed here
- No OpenCode-specific tool entries

### .geminiignore — Gemini-only

- Lists `teams/`, `workspace/`, `archive/`, `planning-artifacts/`
- No `.gitignore` exists at all — repo has no version control ignore rules

### swarm/aim_team.py — **BROKEN, WILL NOT PARSE**

This is the **primary orchestrator** — the file that boots a swarm team from `SWARM_MANIFEST.json`. It is non-functional.

| Line | Defect |
|------|--------|
| 71 | `orchestrator_session` is undefined — used in `cmd` string |
| 77 | `time.sleep(3)` called but `import time` is missing |
| 78 | `orchestrator_session` used again in `identity_prompt` — still undefined |
| 79 | `send_prompt()` called but never defined or imported |
| 90-100 | Tail section is corrupted: duplicate `main()`, orphaned strings, invalid syntax |

**Additionally:** the default manifest path `teams/SWARM_MANIFEST.json` does not exist. The file has no valid execution path.

### swarm/aim_spawn.py — **WRONG SOURCE**

The factory provisions new agent nodes by cloning the base A.I.M. OS. But `find_aim_root()` walks up from the script location looking for `core/CONFIG.json` or `setup.sh` — neither exists in `aim-swarm`. The fallback resolves to `/home/kingb/aim-swarm` itself. Result: it clones `aim-swarm` into the new node, not the A.I.M. OS engine.

Other issues:
- Clean sweep removes `.git`, then runs `git init` — but after cloning the wrong repo, the directory is nearly empty
- References `./setup.sh` post-spawn — doesn't exist in the cloned source
- `mail.sh` is a bare stub (just echoes); no real chalkboard mail system
- No error handling for individual clone failures

### swarm/aim_swarm.py — Functional but Gemini-locked

The synchronous orchestrator. Creates a tmux grid and boots agents. Unlike `aim_team.py`, this file is syntactically valid.

| Line | Issue |
|------|-------|
| 48 | Hardcoded `gemini` — sends `gemini` binary to each pane |
| 48 | No `--yolo` flag — agents will wait for human approval on every action |
| 48 | Uses `send_keys` not buffer system (fine for short strings) |
| 49 | `BTab Enter` — BTab may be Gemini-specific escape sequence |

**Overlap:** This file and `aim_team.py` both create tmux grids and spawn agents. They should be unified into one orchestrator.

### agents/python-developer/ — Only blueprint, but solid

| File | Status |
|------|--------|
| `AGENTS.md` | Clear persona. Typo: "atomicaly" → "atomically". References nonexistent `scripts/aim_cli.py`. |
| `TOOLS.md` | Good chalkboard + tmux injection docs. References Gemini `activate_skill` pattern. |
| `manifest.json` | Clean, no issues. |

This is the only agent blueprint. The swarm can currently only spawn Python developers.

### docs/TMUX_AIM_SWARM.md — **EXCELLENT**

The best file in the repo. 476 lines of correct, well-tested tmux co-agent patterns covering:
- Co-agent vs sub-agent distinction
- TUI vs Run mode spawning trap (correct: always use bare binary TUI + buffer injection)
- Session lifecycle, message delivery, human escalation, debugging
- Already dual-platform aware (both `opencode` and `gemini` examples)

**Irony:** The code in `aim_team.py` does NOT follow the patterns documented here.

---

## Defect Severity Summary

### Critical — Code Cannot Execute

| # | File | Defect |
|---|------|--------|
| 1 | `swarm/aim_team.py` | `send_prompt()` undefined |
| 2 | `swarm/aim_team.py` | `import time` missing |
| 3 | `swarm/aim_team.py` | `orchestrator_session` undefined |
| 4 | `swarm/aim_team.py` | Malformed tail section — invalid Python |
| 5 | `swarm/aim_team.py` | `SWARM_MANIFEST.json` does not exist |
| 6 | `swarm/aim_spawn.py` | Clones wrong repo (aim-swarm, not A.I.M. OS) |

### High — Functional Breaks

| # | File | Defect |
|---|------|--------|
| 7 | `swarm/aim_spawn.py` | References nonexistent `./setup.sh` |
| 8 | `swarm/aim_swarm.py:48` | Hardcoded `gemini` binary |
| 9 | `swarm/aim_swarm.py` | No autonomous mode flag |
| 10 | `swarm/aim_swarm.py` | Overlaps with `aim_team.py` |
| 11 | Repo-wide | Zero tests |

### Medium — Design / Consistency

| # | Defect |
|---|--------|
| 12 | AGENTS.md references nonexistent continuity/ and architecture docs |
| 13 | README references nonexistent SWARM_MANIFEST and default_team |
| 14 | `.geminiignore` needed but no `.gitignore` |
| 15 | Only one agent blueprint (python-developer) |
| 16 | `activate_skill` is Gemini-specific; no OpenCode equivalent |
| 17 | `mail.sh` chalkboard stub — not a real communication system |

### Low — Polish

| # | Defect |
|---|--------|
| 18 | `agents/python-developer/AGENTS.md` — typo "atomicaly" |
| 19 | No `.gitignore` (only `.geminiignore`) |
| 20 | `BTab Enter` key sequence may not work in OpenCode TUI |

---

## Gemini → OpenCode Adaptation Map

| Current (Gemini) | Target (OpenCode) |
|---|---|
| `.geminiignore` | `.opencodeignore` + `.gitignore` |
| `gemini` / `gemini --yolo` | `opencode` (TUI mode, no flags) |
| `activate_skill "name"` | OpenCode tool call (no direct equivalent) |
| `BTab Enter` escape | Check OpenCode TUI multiline escape (likely different) |
| `aim bug/fix/push/search/map/pulse` | A.I.M. OS commands — unchanged if global engine installed |

---

## Recommended Remediation Order

1. **Fix `aim_team.py`** — define `send_prompt()`, add `import time`, define `orchestrator_session`, fix tail corruption, create `SWARM_MANIFEST.json`
2. **Fix `aim_spawn.py`** — point `find_aim_root()` fallback at actual A.I.M. OS path or accept it as a required argument
3. **Unify orchestrators** — merge `aim_team.py` and `aim_swarm.py` into one, following `TMUX_AIM_SWARM.md` patterns
4. **Replace `gemini`** — change binary to `opencode` throughout, use documented buffer injection
5. **Add infrastructure** — tests, `.gitignore`, `requirements.txt`, a sample `SWARM_MANIFEST.json`
6. **Add more blueprints** — technical-auditor, wiki-scribe, etc.
7. **Build real chalkboard** — replace `mail.sh` stub with git-based message passing
