# imzala MCP server: installation guide for AI agents

imzala.net is a hosted remote MCP server for Turkish case law. There is nothing to clone, build or run locally. Do not install packages.

- Endpoint: `https://mcp.imzala.net/mcp`
- Transport: Streamable HTTP
- Authorization: OAuth 2.1 with dynamic client registration. Sign-in is by e-mail code; a 14-day trial account is created on first sign-in.

## Cline

1. Open Cline's own MCP settings file. Cline reads only this file; do not create a new `cline_mcp_settings.json` in the project folder.
   - Cline 4.x (VS Code, Cursor, JetBrains, CLI): `~/.cline/data/settings/cline_mcp_settings.json` (Windows: `%USERPROFILE%\.cline\data\settings\cline_mcp_settings.json`).
   - Older Cline 3.x VS Code extension: `<editor user folder>/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json` (Windows VS Code: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`).
   - If neither exists, ask the user to open it with MCP Servers → Configure → Configure MCP Servers.
2. Read the file, then add this entry under `mcpServers` and keep any existing entries:

```json
"imzala": {
  "type": "streamableHttp",
  "url": "https://mcp.imzala.net/mcp",
  "disabled": false,
  "autoApprove": []
}
```

3. Save the file. When the server asks for authorization, use the **Authenticate** action for `imzala` in the MCP Servers view. An imzala.net page opens in the browser: the user types their e-mail address, enters the 6-digit code sent to it and approves the connection.
4. If OAuth is not possible in this client, ask the user for a personal API key from https://mcp.imzala.net/anahtar (it starts with `imz_`) and add `"headers": { "Authorization": "Bearer <key>" }` to the entry. Never invent a key; the user must paste it.
5. Check the connection: the server exposes 12 tools, among them `ictihat_ara`, `karar_getir` and `kunye_dogrula`. Call `kunye_dogrula` with `esas` "2023/1532" and `karar` "2024/250"; the result should say the decision exists (Yargıtay 3. Hukuk Dairesi, 18.01.2024).

## Other MCP clients

Add `https://mcp.imzala.net/mcp` as a Streamable HTTP server. Clients that support OAuth sign in on first use; others use the personal API key as a Bearer token.

## Optional skills

The `skills/` folder of this repository holds two skills in the Agent Skills format (`ictihat-arastirma`, `dilekce-yazimi`). Copy them into the client's skills folder if it supports skills.
