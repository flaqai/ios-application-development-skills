# XcodeBuildMCP Compatibility

The nine OpenAI skills and `.mcp.json` are intentionally preserved byte-for-byte from the tracked `build-ios-apps` upstream. The upstream MCP command uses `xcodebuildmcp@latest`, so the runtime API is not pinned by `OPENAI_UPSTREAM.json` and can drift independently of the skill text.

## Required Runtime Preflight

Before a Simulator workflow:

1. Inspect the XcodeBuildMCP tools and input schemas currently exposed to Codex.
2. Discover projects/workspaces and schemes with the available discovery tools; do not guess among multiple targets.
3. Map an upstream skill action to a current tool only when the tool description makes the equivalence clear.
4. Take a fresh UI snapshot before interaction and use the current snapshot's element references when the runtime requires them.
5. If a required capability is absent or its replacement is ambiguous, stop and report the exact compatibility gap. Do not fabricate a tool call or continue UI automation.

## Point-in-Time Finding

Verified 2026-08-14: the tracked OpenAI v0.1.2 `ios-debugger-agent` snapshot names `describe_ui`, `start_sim_log_cap`, and `stop_sim_log_cap`, while XcodeBuildMCP 2.7.0 exposes a newer UI snapshot/element-reference flow and returns log paths through build/launch operations. Its current workflow list also no longer includes the configured `logging` workflow.

This repository does not silently edit those nine upstream skills because doing so would break provenance and weekly hash verification. The weekly OpenAI sync will surface upstream changes in a review PR. Re-run this preflight after either OpenAI or XcodeBuildMCP changes.
