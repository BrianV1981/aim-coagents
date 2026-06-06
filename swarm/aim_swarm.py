#!/usr/bin/env python3
import os
import subprocess
import argparse
import sys
import time

def send_prompt(session_pane, prompt):
    """Sends a multiline prompt safely using the tmux paste-buffer technique."""
    print(f"Sending prompt to {session_pane}...")
    
    # 1. Load prompt into tmux buffer
    subprocess.run(["tmux", "set-buffer", prompt], check=True)
    
    # 2. Paste the buffer into the target pane
    subprocess.run(["tmux", "paste-buffer", "-t", session_pane], check=True)
    
    # 3. Escape the multiline editor (Shift+Tab) and Submit (Enter)
    # Give the UI a millisecond to register the pasted text before escaping
    time.sleep(0.5)
    subprocess.run(["tmux", "send-keys", "-t", session_pane, "BTab", "Enter"], check=True)
    print(f"Prompt successfully submitted to {session_pane}.")

def create_swarm(session_name="aim_swarm", workers=2):
    """Creates a new tmux session with a grid of worker panes running Gemini CLI."""
    # Check if session exists
    res = subprocess.run(["tmux", "has-session", "-t", session_name], capture_output=True)
    if res.returncode == 0:
        print(f"[ERROR] Session '{session_name}' already exists. Attach to it with 'tmux attach -t {session_name}' or kill it first.")
        return
        
    print(f"Orchestrating new Swarm session: '{session_name}' with {workers} workers...")
    
    # Create the primary session (detached) - Pane 0 will be the "Orchestrator" terminal
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name], check=True)
    
    # For each worker, split the window and start the Gemini CLI
    for i in range(1, workers + 1):
        print(f"  -> Spawning Worker {i}...")
        # Split pane
        split_flag = "-h" if i % 2 != 0 else "-v"
        subprocess.run(["tmux", "split-window", split_flag, "-t", session_name], check=True)
        
        # The new pane is the highest index (i)
        target_pane = f"{session_name}:0.{i}"
        
        # Start Gemini CLI in the new pane
        subprocess.run(["tmux", "send-keys", "-t", target_pane, "gemini", "Enter"], check=True)
        
        # Wait a moment for the CLI UI to fully load
        time.sleep(3)
        
        # Send an initial persona/identity prompt
        identity_prompt = f"[System Setup]: You are Swarm Worker {i}. Acknowledge your identity and await the Orchestrator's commands."
        send_prompt(target_pane, identity_prompt)

    # Balance the layout to a tiled grid
    subprocess.run(["tmux", "select-layout", "-t", f"{session_name}:0", "tiled"], check=True)
    
    # Put the cursor back in pane 0 (the Orchestrator command shell)
    subprocess.run(["tmux", "select-pane", "-t", f"{session_name}:0.0"], check=True)
    
    print("\n[SUCCESS] Swarm successfully orchestrated!")
    print(f"To watch it live, run:  tmux attach-session -t {session_name}")
    print(f"To command a worker:    python3 aim_swarm.py --send {session_name}:0.1 --prompt \"[Orchestrator]: Hello Worker 1!\"")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A.I.M. Synchronous Swarm Orchestrator")
    parser.add_argument("--create", action="store_true", help="Create a new Swarm session grid")
    parser.add_argument("--workers", type=int, default=2, help="Number of worker panes (default: 2)")
    parser.add_argument("--send", type=str, metavar="PANE", help="Send a prompt to a specific pane (e.g., 'aim_swarm:0.1')")
    parser.add_argument("--prompt", type=str, help="The message to send")
    
    args = parser.parse_args()
    
    if args.create:
        create_swarm(workers=args.workers)
    elif args.send and args.prompt:
        send_prompt(args.send, args.prompt)
    else:
        parser.print_help()
