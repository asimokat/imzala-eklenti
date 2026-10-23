# imzala.net: yapay zekâ eklentisi

**GÜNLÜK GÜNCELLENİR, HEP TAZE:** yeni kararlar ve Resmî Gazete her gün arşive eklenir.

Bu depo imzala.net içtihat arşivini Claude dışındaki yapay zekâ araçlarına bağlayan eklentidir. Aynı içerik birkaç aracın eklenti biçimiyle birlikte durur; her araç kendi dosyasını okur. Claude için ayrı depo: [asimokat/imzala-claude-eklenti](https://github.com/asimokat/imzala-claude-eklenti).

Arşivde 11,5 milyon Türk yargı ve kurul kararı, doktrin künyeleri, Resmî Gazete tam metni, kanun maddesi haritası ve TCMB/TÜİK verisi bulunur. Yapay zekâ cevabı kendisi yazar; kararın metnini, künyesini ve resmî kaynak bağlantısını arşivden alır.

**English:** [tools, connection and sign-in for any MCP client](#english)

## İçindekiler

| Parça | Ne yapar |
|---|---|
| `mcp.json`, `mcp_config.json`, `gemini-extension.json` | `https://mcp.imzala.net/mcp` adresindeki uzak MCP sunucusuna bağlanır (12 alet). Arşive veri yazılmaz. |
| `skills/get-started` | İlk bağlantıyı ve ilk soruları anlatır. |
| `skills/ictihat-arastirma` | Arama yöntemi: kelime ve anlam araması birlikte, okumadan atıf yok, künye doğrulama. |
| `skills/dilekce-yazimi` | Dilekçe biçimi ve `md2udf.py` ile UYAP'ın UDF biçimine dönüştürme. |
| `rules/AGENTS.md`, `GEMINI.md` | Her zaman açık kısa çalışma kuralları (aynı metin). |
| `deepseek-harness/` | DeepSeek Harness için yama parçası, kurallar ve kurulum betiği. |

## Kurulum

| Araç | Kurulum |
|---|---|
| Codex | `codex plugin marketplace add asimokat/imzala-eklenti` |
| Gemini CLI | `gemini extensions install https://github.com/asimokat/imzala-eklenti` |
| Google Antigravity | `agy plugin install https://github.com/asimokat/imzala-eklenti` ya da depoyu `~/.gemini/config/plugins/imzala` klasörüne kopyalayıp Antigravity'yi yeniden başlatın. Elle eklenmiş bir `imzala` MCP sunucusu varsa aletler iki kez görünmesin diye onu kaldırın. |
| Qwen Code | `qwen extensions install asimokat/imzala-eklenti` |
| GitHub Copilot CLI | `copilot plugin install asimokat/imzala-eklenti` |
| Kiro | Powers → Add Custom Power → `https://github.com/asimokat/imzala-eklenti` |
| Cline | Cline'a "https://github.com/asimokat/imzala-eklenti deposundaki llms-install.md'ye göre imzala MCP sunucusunu kur" deyin ya da `llms-install.md`'deki girdiyi MCP ayarlarına ekleyin. |
| JetBrains Junie | `/extensions marketplace add asimokat/imzala-claude-eklenti` (Claude biçimindeki depo) |
| Cursor, VS Code, Goose, Perplexity ve diğerleri | MCP sunucusu olarak `https://mcp.imzala.net/mcp` adresini ekleyin (Streamable HTTP). |

İlk kullanımda imzala.net giriş sayfası açılır: e-postanızı yazın, gelen 6 haneli kodu girin ve izin verin. Giriş ekranını desteklemeyen araçlar için [mcp.imzala.net/anahtar](https://mcp.imzala.net/anahtar) adresinden kişisel anahtar alınır ve `Authorization: Bearer imz_…` başlığıyla kullanılır.

### DeepSeek Harness

DeepSeek Harness uzak MCP sunucusuna giriş ekranıyla bağlanamaz; kişisel anahtar kullanılır.

1. [mcp.imzala.net/anahtar](https://mcp.imzala.net/anahtar) adresinden anahtarınızı alın. Anahtar `imz_` ile başlar.
2. Depoyu indirip açın ve PowerShell'de şunu çalıştırın: `powershell -ExecutionPolicy Bypass -File deepseek-harness\kur.ps1`
   Betik `~/.dsh/profiles/desktop/cordis.patch.yml` dosyasının yedeğini alıp imzala girdisini ekler. Skill'leri `~/.dsh/skills` altına kopyalar, kısa kuralları `~/.dsh/AGENTS.md` dosyasına yazar ve anahtarı sorar.
3. DeepSeek Harness'tan tamamen çıkıp uygulamayı yeniden açın. Pencereyi kapatmak yetmez, çünkü uygulama arka planda çalışmaya devam eder. Sistem tepsisindeki simgeye sağ tıklayıp Çıkış'ı (Quit) seçin. Aletler `mcp__imzala__ictihat_ara` gibi adlarla görünür.
4. Anahtarı değiştirdiğinizde betiği `-AnahtarYenile` ile yeniden çalıştırın, sonra uygulamadan yine tamamen çıkıp açın.

Anahtar yalnız `IMZALA_ANAHTAR` kullanıcı ortam değişkeninde durur. Yapılandırma dosyasına ya da sohbete yazılmamalıdır.

Elle kurmak isterseniz:
- `deepseek-harness/cordis.patch.yml` içeriğini profilinizin `cordis.patch.yml` dosyasının sonuna ekleyin.
- `skills/` altındaki klasörleri `~/.dsh/skills/` altına kopyalayın.
- `IMZALA_ANAHTAR` adında bir kullanıcı ortam değişkeni tanımlayın.

## Ne gönderir, ne saklar

- Eklenti yalnız `https://mcp.imzala.net/mcp` adresine bağlanır. Kanca ve yerel sunucu içermez.
- `md2udf.py` dönüştürücüsü Python'un kendi kütüphaneleriyle çalışır, ağa bağlanmaz ve yalnız bir dilekçe UDF'ye çevrilirken çalışır.
- `deepseek-harness/kur.ps1` yalnız DeepSeek Harness kurulumunda elle çalıştırılır ve ağa bağlanmaz. Önce yedek alır, sonra `~/.dsh` altındaki dosyaları değiştirir. İsterseniz `IMZALA_ANAHTAR` kullanıcı ortam değişkenini de yazar.
- Arama aletlerinin sorgu metni sunucuda kaydedilmez. Derin araştırmada sorunun ilk 300 karakteri iş kaydına yazılır ve araştırma Google Gemini ile yürütülür.
- Ayrıntı: [API gizlilik bildirimi](https://imzala.net/api-gizlilik) · [API kullanım koşulları](https://imzala.net/api-kosullar)

Hizmet ücretlidir; her yeni hesap 14 günlük denemeyle başlar. Hesap ve planlar: [imzala.net/yapay-zeka](https://imzala.net/yapay-zeka)

## Destek

Sorular ve sorun bildirimi için: [imzala.net/yardim](https://imzala.net/yardim). Gizlilik politikası: [imzala.net/api-gizlilik](https://imzala.net/api-gizlilik).

## English

This plugin connects AI tools to the imzala.net Turkish case-law archive, updated daily, through a remote MCP server at `https://mcp.imzala.net/mcp` (12 tools; nothing is written to the archive). The same content ships in several formats side by side: Agent Plugins (`plugin.json`, `mcp.json`, `skills/`), Gemini CLI (`gemini-extension.json`, `GEMINI.md`), Google Antigravity (`plugin.json`, `mcp_config.json`, `rules/AGENTS.md`) and DeepSeek Harness (`deepseek-harness/`: a `cordis.patch.yml` fragment that connects with a personal API key, plus an installer script). It includes a research-method skill, a Turkish petition-writing skill with a Markdown-to-UDF converter (standard-library Python, no network access) and an onboarding skill. Sign-in is by e-mail code (OAuth 2.1 with dynamic client registration and client ID metadata documents); tools without OAuth can use a personal API key as a Bearer token. The service is paid and starts with a 14-day trial. The content is in Turkish.

<!-- Bu bölüm asimokat/imzala-claude-eklenti README'sindeki İngilizce bölümle aynıdır; ikisi birlikte güncellenir. -->
### Tools

The server exposes 12 tools. Eleven are read-only (`readOnlyHint: true`). `arastirma_baslat` is not read-only: each call starts a deep-research job and uses 10 units of the account's monthly quota. It deletes or changes nothing, and no tool writes to the archive. Tool descriptions and parameters are in Turkish.

| Tool | What it does | Read-only |
|---|---|---|
| `ictihat_ara` | Keyword search across 11.5 million decisions (Court of Cassation, Council of State, Constitutional Court, ECtHR, Court of Accounts, regional and first-instance courts, and boards such as the Competition Authority). Filters by court, year, civil or criminal branch, outcome, document type and the statute article a decision relies on. Each hit has the citation, a document ID, a snippet and the official source link. | yes |
| `ictihat_semantik` | Semantic search: takes a plain-language sentence and finds decisions close in meaning even when the words differ (vector index of 28.7 million passages). | yes |
| `karar_getir` | Returns a decision by document ID: the operative part (default), the passage around a given term, or the full text in pages, headed by the citation and the official source link. | yes |
| `kunye_dogrula` | Checks whether a citation exists. From the docket and/or decision number it returns the real court, date, outcome and source link, flags a court or date that does not match, and lists near matches when the citation is not found. | yes |
| `benzer_kararlar` | Lists decisions that rest on the same legal grounds as a given decision. For Constitutional Court decisions it can also list the later decisions that cite it. | yes |
| `madde_haritasi` | For a statute article (for example `hmk` 107), shows how the decisions relying on it are distributed: which courts, outcome rates and the trend by year. Returns aggregate counts, not individual decisions. | yes |
| `doktrin_ara` | Searches 98,651 theses and law-journal articles. Returns the title, citation, abstract and link; the full work is not returned because of copyright. | yes |
| `resmi_gazete_ara` | Full-text search of the Official Gazette of the Republic of Türkiye from 27 June 2000 onward: more than 110,000 documents, including notices. | yes |
| `hukuk_gundemi` | Legislative agenda: bills before the Turkish Parliament with their status, recent amendments published in the Official Gazette and legal-press headlines, each in the source's own words. | yes |
| `veri_getir` | Official figures used in legal calculations: the central bank's advance and rediscount interest rates, price indices (consumer, producer, construction and services) and exchange rates for 43 currencies, from the Central Bank of the Republic of Türkiye and the Turkish Statistical Institute, with the source named. | yes |
| `arastirma_baslat` | Starts a deep-research job for a broad legal question and returns a job ID. The report is usually ready in about 4 minutes and ties every claim to a verified citation and a verbatim quote. | **no**: starts a job and uses quota |
| `arastirma_sonuc` | Returns the report of a deep-research job by its job ID. While the job is still running, it waits up to 40 seconds and then returns the progress. | yes |

### Connecting from any MCP client

- Endpoint: `https://mcp.imzala.net/mcp`
- Transport: Streamable HTTP
- Authorization: OAuth 2.1 with sign-in by e-mail code, or a personal API key sent as a Bearer token
- MCP Registry name: `net.imzala/ictihat`

Clients that support remote servers and OAuth need only the URL; they start the sign-in on first use. The configuration format depends on the client. A common form:

```json
{
  "mcpServers": {
    "imzala": { "url": "https://mcp.imzala.net/mcp" }
  }
}
```

VS Code (`.vscode/mcp.json`) uses `"servers"` and `"type": "http"` for the same entry. In Claude Code: `claude mcp add --transport http imzala https://mcp.imzala.net/mcp`.

Clients that can only start local (stdio) servers can use the `mcp-remote` bridge, which opens the same browser sign-in:

```json
{
  "mcpServers": {
    "imzala": { "command": "npx", "args": ["-y", "mcp-remote@0.1.37", "https://mcp.imzala.net/mcp"] }
  }
}
```

### Sign-in with an e-mail code (OAuth 2.1)

What the user sees:

1. The client opens an imzala.net page in the browser.
2. The user types an e-mail address. A 6-digit code is sent to it. The code is valid for 10 minutes and allows 5 attempts.
3. The user enters the code. A consent page names the requesting application, and the user clicks **İzin ver** (Allow).
4. The browser returns to the client, which receives its tokens.

There is no password. A new e-mail address gets an account automatically, starting with a 14-day trial. After the first sign-in the browser keeps a 30-day cookie, so connecting another application from the same browser skips the code; the consent click is still required. The user can turn the cookie off on the consent page. Limits: 5 codes per hour and 10 per 24 hours for one e-mail address, and 20 per hour from one IP address.

For client developers:

- An unauthenticated request to `/mcp` returns `401` with `WWW-Authenticate: Bearer resource_metadata="https://mcp.imzala.net/.well-known/oauth-protected-resource/mcp", scope="ictihat"`.
- Authorization server metadata: `https://mcp.imzala.net/.well-known/oauth-authorization-server`
- Client registration: Dynamic Client Registration (RFC 7591) at `https://mcp.imzala.net/register`, or a Client ID Metadata Document (an HTTPS URL used as `client_id`). Public clients only (`token_endpoint_auth_method: none`).
- Authorization code flow with PKCE, `S256` only. Scopes: `ictihat`, plus `offline_access` for a refresh token. Resource indicator, if sent: `https://mcp.imzala.net/mcp`. Redirect URIs must be HTTPS or loopback HTTP (`localhost`, `127.0.0.1`, `[::1]`).
- Access tokens last 1 hour. Refresh tokens last 30 days and are replaced at each use.

### Personal API key (clients without OAuth)

1. Open https://mcp.imzala.net/anahtar and sign in with the e-mail code.
2. Create a key. It starts with `imz_` and is shown only once. When creating a new key you can revoke the old ones.
3. Send it with every request: `Authorization: Bearer imz_…`

```json
{
  "mcpServers": {
    "imzala": {
      "url": "https://mcp.imzala.net/mcp",
      "headers": { "Authorization": "Bearer ${IMZALA_API_KEY}" }
    }
  }
}
```

Keep the key in an environment variable or the client's secret store, never in a repository. How `${IMZALA_API_KEY}` is expanded depends on the client.

### Check the connection

Call `kunye_dogrula` with `esas` `2023/1532` and `karar` `2024/250`. The answer should report Yargıtay 3. Hukuk Dairesi (Court of Cassation, 3rd Civil Chamber), 18.01.2024, ONAMA (affirmed).

Support: https://imzala.net/yardim · Privacy policy: https://imzala.net/api-gizlilik · Terms of use: https://imzala.net/api-kosullar

## Lisans

MIT, bkz. [LICENSE](LICENSE). Lisans yalnız bu depodaki eklenti dosyalarını kapsar; imzala.net hizmeti ve arşiv içeriği [kullanım koşullarına](https://imzala.net/api-kosullar) tabidir.
