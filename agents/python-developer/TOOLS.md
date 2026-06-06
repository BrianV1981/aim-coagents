# A.I.M. Swarm Specific Tools

## 1. The Swarm Post Office (Local Chalkboard)
Location: `workspace/aim-chalkboard` (Local to your Sovereign Node)

If the Orchestrator instructs you to drop a file for another agent, use the standalone GitOps mail system:
1. Navigate to your local `workspace/aim-chalkboard` directory.
2. Read `inbox/` for new tasks.
3. Run `./mail.sh send <recipient>` to drop a markdown file in a teammate's inbox.

## 2. Asynchronous Ping-Back (Tmux Injection)
If the Orchestrator tells you to reply to their `tmux` session directly (e.g., `leaddeed-aim`), you MUST use the following sequence to bypass multiline UI locks:

```bash
# 1. Set the buffer with your ping
tmux set-buffer "[Python Developer]: The authentication bug has been resolved and tests are passing. Awaiting next task."

# 2. Paste the buffer into the Orchestrator's session
tmux paste-buffer -t leaddeed-aim

# 3. Escape the UI and hit Enter
tmux send-keys -t leaddeed-aim BTab Enter
```

## 3. Scientific Math
Do not hallucinate floating-point math. Invoke the calculator skill natively:
`<CLI_NAME> activate_skill "scientific-calculator"`
