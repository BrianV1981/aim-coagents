# Allowed Tools — `content-node` (Node.js / Next.js Content Co-Agent)

- **RAG & Memory:** `search_lancedb` (MCP) / `python3 joshua_os/.aim_core/aim_cli.py search`, `/aim-memory-wiki`, `/aim-handoff`
- **Content Generation Skills:** `/aim-mega-article`, `/aim-mega-guide`, `image-generator` subagent
- **Transcript & Research Pipeline:** `aim-youtube` (`/home/kingb/aim-youtube/content_library/` lookup + headless `yt-dlp` VTT extraction), `search_web`
- **Verification & Delivery:** `npm run build` (Next.js static build gatekeeper), `scripts/drip_next_article.sh`, `aim-communicate` (`tmux_send.sh` / 3-step tmux buffer handoff)
