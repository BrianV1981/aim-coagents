#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import shutil

def find_aim_root():
    current = os.path.abspath(os.getcwd())
    while current != '/':
        if os.path.exists(os.path.join(current, "core", "CONFIG.json")) or os.path.exists(os.path.join(current, "setup.sh")):
            return current
        current = os.path.dirname(current)
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = find_aim_root()

def clone_aim_core(node_dir):
    print(f"Cloning A.I.M. OS to {node_dir}...")
    # Use git clone --local to quickly copy the repo state
    subprocess.run(["git", "clone", "--local", BASE_DIR, node_dir], check=True, capture_output=True)
    
    # Run clean sweep (remove git, teams, workspace, agents, archive, etc)
    print("Running clean sweep on clone...")
    shutil.rmtree(os.path.join(node_dir, ".git"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "teams"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "workspace"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "archive"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "agents"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "engrams"), ignore_errors=True)
    shutil.rmtree(os.path.join(node_dir, "continuity"), ignore_errors=True)
    
    # Recreate necessary empty directories
    for d in ["workspace", "archive/raw", "archive/history", "archive/sync", "continuity/private", "engrams"]:
        os.makedirs(os.path.join(node_dir, d), exist_ok=True)

def inject_blueprint(node_dir, role_name):
    blueprint_dir = os.path.join(BASE_DIR, "agents", role_name)
    if not os.path.exists(blueprint_dir):
        print(f"[WARNING] Blueprint '{role_name}' not found in agents/. Using default templates.")
        return

    print(f"Injecting blueprint '{role_name}' into clone...")
    for item in os.listdir(blueprint_dir):
        s = os.path.join(blueprint_dir, item)
        d = os.path.join(node_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def setup_chalkboard(node_dir):
    global_chalkboard = os.path.join(BASE_DIR, "workspace", "aim-chalkboard")
    if not os.path.exists(global_chalkboard):
        print("Initializing global aim-chalkboard repository...")
        os.makedirs(global_chalkboard, exist_ok=True)
        subprocess.run(["git", "init"], cwd=global_chalkboard, check=True, capture_output=True)
        os.makedirs(os.path.join(global_chalkboard, "inbox"), exist_ok=True)
        
        # Create a simple mail.sh script
        mail_script = os.path.join(global_chalkboard, "mail.sh")
        with open(mail_script, "w") as f:
            f.write("#!/bin/bash\n")
            f.write("if [ \"$1\" == \"send\" ]; then\n")
            f.write("  echo \"Sent message to $2\"\n")
            f.write("fi\n")
        os.chmod(mail_script, 0o755)
        
        with open(os.path.join(global_chalkboard, "README.md"), "w") as f:
            f.write("# A.I.M. Swarm Chalkboard\\n\\nGlobal post office for inter-agent communication.")
        
        subprocess.run(["git", "add", "."], cwd=global_chalkboard, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=global_chalkboard, check=True, capture_output=True)

    node_workspace = os.path.join(node_dir, "workspace")
    os.makedirs(node_workspace, exist_ok=True)
    node_chalkboard = os.path.join(node_workspace, "aim-chalkboard")
    
    print(f"Cloning aim-chalkboard into {node_chalkboard}...")
    subprocess.run(["git", "clone", global_chalkboard, node_chalkboard], check=True, capture_output=True)


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Sovereign Node (V3 Fractal Clone) for the A.I.M. Swarm.")
    parser.add_argument("role_name", type=str, help="The role/persona for the new agent (e.g., 'python-developer').")
    parser.add_argument("--output_dir", type=str, help="Optional custom output directory. Defaults to 'teams/<role_name>/'.")
    
    args = parser.parse_args()
    role_name = args.role_name
    
    if args.output_dir:
        node_dir = os.path.abspath(args.output_dir)
    else:
        node_dir = os.path.join(BASE_DIR, "teams", role_name)
        
    if os.path.exists(node_dir):
        print(f"Error: Target directory {node_dir} already exists.")
        sys.exit(1)
        
    try:
        clone_aim_core(node_dir)
        inject_blueprint(node_dir, role_name)
        setup_chalkboard(node_dir)
        
        # Git Initialization
        subprocess.run(["git", "init"], cwd=node_dir, check=True, capture_output=True)
        print(f"Initialized isolated git repository in {node_dir}")
        
        print(f"\n[SUCCESS] Successfully scaffolded Fractal Sovereign Node: {role_name} at {node_dir}")
        print(f"To initialize this node, run: cd {node_dir} && ./setup.sh")
    except Exception as e:
        print(f"Error creating node: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
