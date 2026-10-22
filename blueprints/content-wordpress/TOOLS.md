# Allowed Tools — `content-wordpress` (WordPress PHP & Local SEO Content Co-Agent)

- **RAG & Memory:** `search_lancedb` (MCP) / `python3 joshua_os/.aim_core/aim_cli.py search`, `/aim-memory-wiki`, `/aim-handoff`
- **Content Generation Skills:** `/aim-mega-article`, `/aim-mega-guide`, `image-generator` subagent (1200px quality-80 `.webp` pipeline)
- **Transcript & Research Pipeline:** `aim-youtube` (`/home/kingb/aim-youtube/content_library/` lookup + headless `yt-dlp` VTT extraction), `search_web`
- **Verification & Delivery:** `python3 tools/test_guardrails.py` (WordPress SEO/CSS/credential guardrail gatekeeper), `scripts/drip_next_article.sh`, `aim-communicate` (`tmux_send.sh` / 3-step tmux buffer handoff)
