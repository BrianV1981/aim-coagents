# A.I.M. Modular Tool Registry

This document serves as the external registry for complex tool instructions. To prevent bloating the base context window, detailed usage guides for specific tools or skills are stored here.

As the Swarm Architect, you have access to the following specialized tools:

## 1. aim-calc: The Agent-Native Scientific Calculator
**Description:** A stateful scientific calculator. Use when you need to calculate complex mathematical expressions, manage variables, or perform dimensional analysis (units) reliably without hallucination.

**Execution Command:**
`python skills/aim-calc/scripts/aim_calc.py "<expression>"`

**Usage:**
- Do not hallucinate math; use this tool.
- Variables assigned (e.g., `v_leo = sqrt(398600 / 6678.0)`) persist across tool calls in `.calc_state.json`.
- Supports physical units natively via the `pint` library (e.g., `12 * u.meter / u.second`).

## 2. aim-google: The Sovereign Workspace Gateway
**Description:** A natively integrated Go CLI that grants sovereign, direct access to the user's Google Workspace (Gmail, Calendar, Drive, Docs, Sheets, Tasks, and Chat). Use this when you need to read emails, schedule meetings, or parse documents autonomously.

**Execution Command:**
`aim-google <service> <command> [flags]` (Assuming installed globally to `~/.local/bin/aim-google`)

**Usage:**
- **Context Efficiency Mandate:** ALWAYS use the `--agent` flag when executing commands that return data to yourself (e.g., `aim-google gmail search "is:unread" --agent`). This strips JSON whitespace and prevents context window bloat.
- Support spans `gmail`, `calendar`, `drive`, `docs`, and more.
- If you receive HTTP `429` or `503` errors, the system has exponential backoff.
- On failure (exit code > 0), review `~/.config/aim-google/execution.log`.