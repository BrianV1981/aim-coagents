# Allowed Tools — `content-node` (Node.js / Next.js Content Co-Agent)

- **RAG & Memory:** `search_lancedb` (MCP) / `python3 joshua_os/.aim_core/aim_cli.py search`, `/aim-memory-wiki`, `/aim-handoff`
- **Content Generation Skills:** `/aim-mega-article`, `/aim-mega-guide`, `image-generator` subagent
- **YouTube Recon Co-Agent (`aim-youtube` Hub-and-Spoke via `aim-communicate`):** Delegate YouTube discovery, `.vtt` -> `.txt` transcript sanitization (`content_library/<project>/raw_transcripts/`), and structured quote/summary extraction (`content_library/<project>/research_summaries/`) to the `aim-youtube` tmux session via `bash .gemini/skills/aim-communicate/scripts/tmux_send.sh --target aim-youtube`, `search_web`
- **Verification & Delivery:** `npm run build` (Next.js static build gatekeeper), `scripts/drip_next_article.sh`, `aim-communicate` (`tmux_send.sh` / 3-step tmux buffer handoff)
