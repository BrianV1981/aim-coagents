# Tmux Co-Agent Communication Protocol

> **Audience:** AI agents orchestrating other AI agents or humans via tmux.  
> **Principle:** Co-agents have their own workspaces, memories, and identities. They are peers, not subprocesses.

---

## 0. Co-Agents vs Sub-Agents — Critical Distinction

**Sub-agents** are temporary workers spawned within a single parent session. They inherit the parent's context, don't persist across sessions, and lack their own memory or workspace. Example: OpenCode's `task` tool, Gemini CLI's agent delegation.

**Co-agents** are fully sovereign, persistent AI sessions with their own tmux window, working directory, AGENTS.md, continuity files, memory-wiki, and git history. They survive reboots, maintain their own context, and can be messaged, inspected, and directed independently. They are **peers**, not subordinates.

### 0.1 TUI Mode vs Run Mode — The Spawning Trap

Every CLI agent has two modes. Choosing the wrong one kills your co-agent:

| Mode | Command | Behavior | Co-Agent? |
|---|---|---|---|
| **Run (single-shot)** | `opencode run "prompt"`, `gemini -p "prompt"` | Processes one prompt, writes output, **exits**. Session dies after completion. | NO — fire-and-forget only |
| **TUI (interactive)** | `opencode`, `gemini` | Opens interactive terminal. **Persists** until killed. Accepts injected messages. | YES — persistent co-agent |

**The Rule:** When spawning a co-agent via tmux, ALWAYS use TUI mode (the bare binary, no `run`/`-p` flags). Then inject the startup prompt via tmux buffer AFTER the session boots.

### 0.2 Correct Co-Agent Spawn Pattern

```bash
# 1. Start TUI in detached session (bare binary, no run/-p flag)
tmux new-session -d -s <agent_name> -c <workdir> opencode
sleep 3   # CRITICAL: wait for TUI to render and accept input

# 2. Write prompt to temp file (avoids shell escaping issues)
cat > /tmp/wakeup.txt << 'EOF'
Your full mandate, tasks, and context here.
Multi-line is fine. Keep it comprehensive.
EOF

# 3. Inject via tmux buffer system (NOT send-keys for long text)
tmux set-buffer "$(cat /tmp/wakeup.txt)"
tmux paste-buffer -t <agent_name>
tmux send-keys -t <agent_name> Enter   # Submit the prompt
```

**Why this works:**
- `opencode` (no `run`) opens the interactive TUI — it stays alive indefinitely
- The sleep ensures the TUI has rendered before we paste into it
- The buffer system avoids keystroke dropout on long prompts
- `send-keys Enter` is separate from the paste — the Enter key doesn't get swallowed

### 0.3 Correct Co-Agent Follow-Up Message Pattern

Once a co-agent is running, send follow-up instructions without restarting:

```bash
tmux set-buffer "New directive: switch to Issue #5 instead"
tmux paste-buffer -t aim-opencode-builder
tmux send-keys -t aim-opencode-builder Enter
```

### 0.4 Co-Agent State Inspection

Check what a co-agent is doing without attaching:

```bash
# See recent output
tmux capture-pane -t <agent_name> -p -S -30

# Check if still alive
tmux has-session -t <agent_name> && echo "ALIVE" || echo "DEAD"

# List all active co-agents
tmux list-sessions -F "#{session_name}"
```

---

## 1. Foundational Rules: Message Delivery

- When messaging other agents in a tmux session (e.g., Gemini CLI), you MUST send the message text first, then execute a separate shell command to send the 'Enter' key (e.g., `tmux send-keys -t <session> Enter`). Sending the text and Enter simultaneously in the same command causes the interactive CLI prompt to swallow the Enter key, leaving the message sitting in the prompt unsubmitted.

- When sending long messages or prompts to other agents in a tmux session, DO NOT use `tmux send-keys` with the raw text, as it can cause keystroke dropouts or swallow the Enter key. Instead, you MUST use the tmux clipboard buffer system: 1. Load the message into the buffer (`tmux set-buffer "your long message"`), 2. Paste the buffer into the target session (`tmux paste-buffer -t <session>`), and 3. Send the Enter key separately (`tmux send-keys -t <session> Enter`).

---

## 2. Spawning Co-Agents

> **WARNING:** Never pass `run` or `-p` flags when spawning a co-agent. Those are single-shot modes that exit after one prompt. Use the bare binary (TUI mode) and inject the prompt via tmux buffer instead. See Section 0.1.

### 2.1 New Session (Isolated Agent)

Creates a completely independent tmux session with its own workspace:

```bash
# Start TUI in detached mode (no flags, no run, no -p)
tmux new-session -d -s <agent_name> -c <working_directory> opencode
sleep 3

# Then inject the wake-up prompt
tmux set-buffer "Your mandate..."
tmux paste-buffer -t <agent_name>
tmux send-keys -t <agent_name> Enter
```

**Examples:**

```bash
# OpenCode persistent co-agent (correct — bare TUI, injected prompt)
tmux new-session -d -s aim_opencode_builder -c /home/kingb/aim-opencode opencode
sleep 3
tmux set-buffer "Read AGENTS.md and docs/aim-opencode-transition.md. Begin Phase 2, Issue #1."
tmux paste-buffer -t aim_opencode_builder
tmux send-keys -t aim_opencode_builder Enter

# Gemini CLI persistent co-agent (correct — bare YOLO, injected prompt)
tmux new-session -d -s wiki_agent -c /home/kingb/aim gemini --yolo
sleep 3
tmux set-buffer "You are the Wiki Scribe. Process files in memory-wiki/_ingest/."
tmux paste-buffer -t wiki_agent
tmux send-keys -t wiki_agent Enter
```

**Key arguments:**
| Flag | Purpose |
|---|---|
| `-d` | Detached — creates session in background, does not attach terminal |
| `-s <name>` | Session name — used for targeting with `send-keys`, `paste-buffer`, etc. |
| `-c <dir>` | Working directory — the agent's `$PWD` on startup |
| `<binary>` | The agent binary in TUI mode: `opencode`, `gemini`, `gemini --yolo` (NO `run`/`-p` flags) |

### 2.2 New Window in Existing Session (Shared View)

Creates a new window inside the current session — visible to the human operator. Useful for tasks that need human interaction (sudo passwords, confirmation):

```bash
tmux new-window "<command>; echo '--- DONE --- Press Enter to close'; read"
```

**Why this pattern works:**
1. `tmux new-window` opens a visible pane the operator can tab into
2. The `<command>` runs and inherits the terminal's TTY (enables interactive password entry for `sudo`, `ssh`, etc.)
3. `read` blocks at the end, keeping the window open so the operator can verify output
4. Operator presses Enter → window closes → auto-returns to previous pane

**Example — Request sudo from operator:**

```bash
tmux new-window "sudo systemctl disable ollama; echo '--- Service disabled --- Press Enter to close'; read"
```

The operator sees this, enters their password, and presses Enter to dismiss.

### 2.3 Existing Session Check

Always verify a session exists before sending keys to it:

```bash
tmux has-session -t <session_name> 2>/dev/null
# Exit code 0 = exists, exit code 1 = not found
```

Pattern for idempotent agent creation:

```bash
if ! tmux has-session -t wiki_agent 2>/dev/null; then
    tmux new-session -d -s wiki_agent -c "$AIM_ROOT" gemini --yolo
    sleep 2  # give it time to boot
fi
```

---

## 3. Sending Messages to Co-Agents

### 3.1 Short Messages (≤ ~200 chars): Direct keystroke injection

```bash
tmux send-keys -t <session> "your message here"
# NEVER include the Enter key in the same command
# Always send Enter separately:
tmux send-keys -t <session> Enter
```

**Anti-pattern (DO NOT USE):**
```bash
# WRONG — Enter gets swallowed by interactive CLI prompts
tmux send-keys -t wiki_agent "process wiki files" Enter
```

### 3.2 Long Messages (> ~200 chars): Clipboard buffer system

```bash
# Step 1: Load message into tmux buffer
tmux set-buffer "your very long multi-line message or prompt..."

# Step 2: Paste buffer into agent session
tmux paste-buffer -t <session>

# Step 3: Send Enter separately
tmux send-keys -t <session> Enter
```

**Why:** The buffer system avoids keystroke dropout that occurs when `send-keys` processes long strings character-by-character. The buffer pastes atomically.

### 3.3 Multi-line Messages: Use a temp file + buffer

```bash
# Write message to temp file (avoids shell escaping issues)
cat > /tmp/agent_message.txt << 'EOF'
MANDATE: Process the following files in memory-wiki/_ingest/:
- file1.md
- file2.md
Archive them into memory-wiki/index.md under appropriate sections.
Delete source files from _ingest/ when complete.
EOF

# Load from file into buffer, then paste
tmux set-buffer "$(cat /tmp/agent_message.txt)"
tmux paste-buffer -t wiki_agent
tmux send-keys -t wiki_agent Enter
```

---

## 4. Session Lifecycle Management

### 4.1 Listing Sessions

```bash
tmux list-sessions        # all sessions
tmux list-sessions -F "#{session_name}"  # names only
```

### 4.2 Switching Operator View (Teleport)

Move the operator's attached client from one session to another:

```bash
# Get current session name
CURRENT_SESSION=$(tmux display-message -p "#S")

# Get all clients attached to current session
tmux list-clients -t "$CURRENT_SESSION" -F "#{client_name}"

# Move each client to the new session
for client in $(tmux list-clients -t "$CURRENT_SESSION" -F "#{client_name}"); do
    tmux switch-client -c "$client" -t <new_session>
done

# Kill the old session to free resources
tmux kill-session -t "$CURRENT_SESSION"
```

### 4.3 Killing Sessions

```bash
# Kill a single session
tmux kill-session -t <session_name>

# Kill all sessions except current
tmux kill-session -a

# Kill a specific window
tmux kill-window -t <session>:<window_index>
```

### 4.4 Renaming Sessions

```bash
tmux rename-session -t <old_name> <new_name>
```

---

## 5. Co-Agent Workspace Isolation

Each co-agent MUST have its own working directory. Never spawn two agents in the same directory unless they are explicitly collaborating on the same files.

### 5.1 The Teams Directory Pattern

```
teams/
├── python-specialist/
│   ├── AGENTS.md          # Role-specific instructions
│   ├── core/CONFIG.json   # Isolated AIM config
│   └── continuity/        # Agent's own memory
├── technical-auditor/
│   └── ...
└── wiki-scribe/
    └── ...
```

### 5.2 Spawning Into a Workspace

```bash
tmux new-session -d -s python_spec -c /home/kingb/aim-swarm/teams/python-specialist gemini --yolo
```

The agent's `$PWD` is its isolated workspace. Paths it references are relative to that directory.

---

## 6. Co-Agent Communication Patterns

### 6.1 Fire-and-Forget (Async Task Delegation)

Send a task and don't wait for response:

```bash
tmux set-buffer "Audit aim_core/plugins/datajack/ for SQL injection vulnerabilities. Write findings to teams/auditor/findings.md."
tmux paste-buffer -t auditor
tmux send-keys -t auditor Enter
```

### 6.2 Request-Response (via Shared Files)

Have one agent write a request file, another reads and responds:

```bash
# Agent A writes request
echo "Review teams/python-spec/app.py for performance issues" > teams/coordinator/inbox/audit_request.md

# Agent B (auditor) is instructed via its AGENTS.md to poll teams/coordinator/inbox/
# It writes response to teams/coordinator/outbox/audit_response.md
```

### 6.3 Pomodoro Delegation (Background + Join)

Spawn agent on a task, do other work, join to check progress:

```bash
# Spawn
tmux new-session -d -s benchmark_runner -c /home/kingb/aim gemini --yolo
tmux set-buffer "Run the full locomo benchmark suite. Save results to benchmarks/locomo/results.json."
tmux paste-buffer -t benchmark_runner
tmux send-keys -t benchmark_runner Enter

# Later: attach to check progress
tmux attach-session -t benchmark_runner

# Or: peek without attaching
tmux capture-pane -t benchmark_runner -p | tail -20
```

### 6.4 Capture Output (Read Agent Response)

Read what an agent last wrote without attaching:

```bash
# Capture entire visible pane
tmux capture-pane -t <session> -p

# Capture with more scrollback lines
tmux capture-pane -t <session> -p -S -100  # last 100 lines of history

# Save to file for parsing
tmux capture-pane -t <session> -p -S -500 > /tmp/agent_output.txt
```

---

## 7. Human Escalation via Tmux

### 7.1 Request sudo/Password

```bash
tmux new-window "sudo <command>; echo '--- COMPLETE --- Press Enter'; read"
```

Operator tabs in (`Ctrl+b n` or tmux prefix + arrow), enters password, presses Enter to dismiss.

### 7.2 Request Confirmation

```bash
tmux new-window "echo 'Proceed with deploying to production? (y/n)'; read CONFIRM; if [ \"\$CONFIRM\" = 'y' ]; then <deploy_command>; else echo 'Aborted.'; fi; echo '--- Press Enter to close ---'; read"
```

### 7.3 Display Status Without Interruption

```bash
# Show a temporary message in the status bar (disappears after interval)
tmux display-message "Agent wiki_agent: 45/100 files processed"

# Flash the current pane border to alert operator
tmux display-message -d 3000 "⚠️  benchmark_runner reports ERROR"
```

---

## 8. Environment Inheritance

When spawning co-agents, be explicit about environment variables. Tmux sessions inherit the spawning shell's environment, which may not include required keys:

```bash
# Explicitly pass environment
tmux new-session -d -s agent_name -c "$WORKDIR" \
    -e "OPENAI_API_KEY=$OPENAI_API_KEY" \
    -e "OLLAMA_HOST=127.0.0.1:11434" \
    gemini --yolo
```

Or source a shared env file:
```bash
tmux new-session -d -s agent_name -c "$WORKDIR" \
    "source ~/.aim_env && gemini --yolo"
```

---

## 9. Debugging Co-Agent Sessions

### 9.1 Is the agent alive?

```bash
tmux has-session -t <name> && echo "ALIVE" || echo "DEAD"
```

### 9.2 What is the agent seeing?

```bash
tmux capture-pane -t <name> -p | tail -30
```

### 9.3 Did the agent crash?

Check if the session still exists but the pane is dead:
```bash
tmux list-panes -t <name> -F "#{pane_dead}"  # "1" = dead
```

### 9.4 What processes are running inside?

```bash
tmux list-panes -t <name> -F "#{pane_pid}" | xargs ps -p
```

---

## 10. Complete Example: Spawning a Wiki Scribe Co-Agent

```bash
#!/bin/bash
# Co-agent wiki scribe deployment

SCRIBE_NAME="wiki_scribe"
SCRIBE_DIR="/home/kingb/aim-swarm/teams/wiki-scribe"

# 1. Check if already alive
if tmux has-session -t "$SCRIBE_NAME" 2>/dev/null; then
    echo "[SKIP] $SCRIBE_NAME is already running"
    exit 0
fi

# 2. Ensure workspace exists
mkdir -p "$SCRIBE_DIR/memory-wiki/_ingest"

# 3. Spawn TUI in detached mode (NO run flag — persistent!)
tmux new-session -d -s "$SCRIBE_NAME" -c "$SCRIBE_DIR" gemini --yolo
sleep 3  # CRITICAL: wait for TUI to render

# 4. Inject role mandate via buffer (NOT as a startup argument)
cat > /tmp/scribe_mandate.txt << 'EOF'
You are the Wiki Scribe. Your MANDATE: 
1. Read AGENTS.md and acknowledge your constraints.
2. Watch memory-wiki/_ingest/ for new markdown files.
3. Process each file: extract key insights, update index.md and log.md.
4. Delete processed files from _ingest/.
5. Report "READY" when done with each batch.
EOF

tmux set-buffer "$(cat /tmp/scribe_mandate.txt)"
tmux paste-buffer -t "$SCRIBE_NAME"
tmux send-keys -t "$SCRIBE_NAME" Enter

echo "[OK] $SCRIBE_NAME spawned and mandate injected"
```
```
