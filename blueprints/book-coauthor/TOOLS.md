# Allowed Tools — `book-coauthor` (Book Co-Author, Developmental Editor, & KDP Compiler Co-Agent)

- **RAG & Memory:** `search_lancedb` (MCP) / `python3 joshua_os/.aim_core/aim_cli.py search`, `/aim-memory-wiki`, `/aim-handoff`, `./aim index --dir <path>`
- **Cross-Repo Lore & Research Vaults (Read-Only):** `/home/kingb/aim-knowledge/`, `/home/kingb/tbsoftwash-course/`, and fleet `memory-wiki/` directories (`/home/kingb/aim-tbsoftwash/`, `/home/kingb/aim-ld/`, `/home/kingb/aim-ayrianna/`, `/home/kingb/aim-agents/aim-auditor/`)
- **Deterministic Visuals & Manuscript Compilation:**
  - `python3 export/build_visuals.py` (Playwright 2x retina HTML/SVG diagram renderer + Pillow photo compositor)
  - `python3 export/build_docx_with_visuals.py` (`python-docx` inline AST parser & figure embedder)
- **Swarm Communication:** `aim-communicate` (`tmux_send.sh` / 3-step tmux buffer handoff)
