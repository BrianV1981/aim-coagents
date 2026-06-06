#!/usr/bin/env python3
import argparse
import json
import subprocess
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Orchestrate a Swarm Team via Tmux.")
    parser.add_argument("team_name", type=str, help="The name of the team to launch from SWARM_MANIFEST.json")
    parser.add_argument("--manifest", type=str, default="teams/SWARM_MANIFEST.json", help="Path to the manifest file")
    parser.add_argument("--no-attach", action="store_true", help="Do not attach to the tmux session after creating it")
    args = parser.parse_args()

    if not os.path.exists(args.manifest):
        print(f"Error: Manifest not found at '{args.manifest}'")
        sys.exit(1)

    with open(args.manifest, "r") as f:
        try:
            manifest = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing manifest JSON: {e}")
            sys.exit(1)

    if "teams" not in manifest or args.team_name not in manifest["teams"]:
        print(f"Error: Team '{args.team_name}' not found in manifest.")
        sys.exit(1)

    team = manifest["teams"][args.team_name]
    members = team.get("members", [])
    if not members:
        print(f"No members found in team '{args.team_name}'.")
        sys.exit(0)

    session_name = f"swarm_{args.team_name}"

    # Kill session if it already exists to start fresh
    subprocess.run(["tmux", "kill-session", "-t", session_name], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    # 1. Create base session (Pane 0 - Orchestrator/Main)
    try:
        subprocess.run(["tmux", "new-session", "-d", "-s", session_name], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to create tmux session. Is tmux installed?")
        sys.exit(1)

    # 2. Iterate over members and create panes
    for i, member in enumerate(members):
        if i == 0:
            # First member: split the main window horizontally
            subprocess.run(["tmux", "split-window", "-h", "-t", session_name], check=True)
        else:
            # Subsequent members: split the last created pane vertically
            target_split_pane = f"{session_name}:0.{i}"
            subprocess.run(["tmux", "split-window", "-v", "-t", target_split_pane], check=True)
            
        # Optional: Rebalance the layout to ensure everyone fits
        subprocess.run(["tmux", "select-layout", "-t", session_name, "tiled"], check=True)

        pane_idx = i + 1
        target_pane = f"{session_name}:0.{pane_idx}"
        
        directory = member.get("dir")
        if not directory:
            print(f"Warning: No directory specified for member index {i}")
            continue

        # Convert path to absolute if it isn't already or just use as is
        # Pass the orchestrator session ID to the agent via an environment variable
        cmd = f"cd {directory} && export ORCHESTRATOR_TMUX_SESSION='{orchestrator_session}' && gemini --approval-mode=yolo"
        
        # 4. Send the initialization commands to each specific pane
        subprocess.run(["tmux", "send-keys", "-t", target_pane, cmd, "C-m"], check=True)

        # 5. Inject the Orchestrator protocol context
        time.sleep(3) # Wait for the CLI to load
        identity_prompt = f"[System Context]: You are online. The Orchestrator's TMUX session ID is '{orchestrator_session}'. To reply directly to the Orchestrator, use: tmux paste-buffer -t {orchestrator_session}"
        send_prompt(target_pane, identity_prompt)

    print(f"Successfully launched Swarm Team: {args.team_name} with {len(members)} nodes.")
    
    # 5. Attach to the session to view the live dashboard
    if not args.no_attach and sys.stdout.isatty():
        print(f"Attaching to tmux session '{session_name}'...")
        os.execlp("tmux", "tmux", "attach-session", "-t", session_name)
    else:
        print(f"Run 'tmux attach-session -t {session_name}' to view the dashboard.")

if __name__ == "__main__":
    main()
{session_name}'...")
        os.execlp("tmux", "tmux", "attach-session", "-t", session_name)
    else:
        print(f"Run 'tmux attach-session -t {session_name}' to view the dashboard.")

if __name__ == "__main__":
    main()
_":
    main()
