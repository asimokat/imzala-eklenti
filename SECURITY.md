# Security Policy · Güvenlik Politikası

## Reporting a Vulnerability / Güvenlik Bildirimi

If you discover a security or privacy issue in this plugin or in `https://mcp.imzala.net/mcp`, please do **not** open a public GitHub issue. Report it directly to:

- **E-mail:** imza@imzala.net
- **Support:** https://imzala.net/yardim

We acknowledge reports within 48 hours and coordinate disclosure once a fix is deployed.

## Scope & Data Handling

- **Remote MCP only:** This plugin connects only to `https://mcp.imzala.net/mcp` (Streamable HTTP over TLS). It bundles no local servers and no lifecycle hooks.
- **Read-only archive:** 23 of 24 tools are strictly read-only (`readOnlyHint: true`). `arastirma_baslat` starts an asynchronous deep-research job and deducts quota; no tool modifies or deletes archive records.
- **No query-text storage:** Search tool query text is not stored in server logs. Only the first 300 characters of a deep-research question are recorded in the job entry (processed via Google Gemini).
- **Offline bundled scripts:** `skills/dilekce-yazimi/scripts/md2udf.py` uses Python's standard library only and makes no network requests.
- **Credentials:** OAuth 2.1 + PKCE (`S256`) with dynamic client registration (RFC 7591) and CIMD, or user-supplied Bearer keys (`imz_...`) stored solely in the user's client/environment.
- **Policies:** [API Privacy Notice](https://imzala.net/api-gizlilik) · [API Terms of Use](https://imzala.net/api-kosullar)
