# Auditor node — tools

## 1. Engine CLI
Prefer the project wrapper if present (`./aim`). Else the nest:

```bash
joshua_os/venv/bin/python3 joshua_os/.aim_core/aim_cli.py <cmd>
```

Required smokes before believing a target: `doctor`, `map`, timed `search`, promote path math when GitOps is advertised.

## 2. Two-Stage Hybrid Audit Procedure (`aim-audit` + `egm`)
1. **Stage A — Deterministic Evidence:** Load library skill **`aim-audit`** (`references/PROTOCOL.md`). Run `scripts/fleet_status.py --remote --issues` to inspect SHA/remote/GitHub-issue drift, and execute target `§8` smoke contracts inside an isolated `$HOME` sandbox via `scripts/run_smoke.py <SLUG>`. Maintain one living `artifacts/AUDIT_<SLUG>.md` and verify table sync with `scripts/sync_ledger.py --check`.
2. **Stage B — Cold-Reader Spec/Code Drift (`baseline` & `event` passes):** Dispatch isolated zero-memory Goldfish subagents (`egm-codebase-details`, `egm-comprehension`, `egm-design`) when available, gated by a mandatory **Elephant Terminal Refutation Gate** — never mint a `<SLUG>-NNN` ID from a subagent claim without reproducing it against live source/CLI.

## 3. Memory
- Primary MCP `search_lancedb` or fallback `./aim search` before inventing fleet history.
- `aim-memory-wiki` for structural takeaways after a closeout — not a second copy of the protocol.
- `aim-sessions` / `./aim sessions` for project-scoped session flight records.

## 4. Swarm
- **Tmux:** skill `aim-communicate` via `scripts/tmux_send.sh` (enforces `FROM`/`REPLY_TO`, `Enter`-only submit without `Escape`, DND blocklist, and programmatic `§3d` verification).
- **Chalkboard (legacy):** `workspace/aim-chalkboard` only if the Operator is using that mailbox.

## 5. Out of scope unless asked
Do not run Semgrep/CodeQL trophy hunts as the spine. AppSec is persona `security-reviewer` or Appendix S after a product-truth pass.
