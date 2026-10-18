# imzala.net: yapay zekâ eklentisi

Bu depo imzala.net içtihat arşivini Claude dışındaki yapay zekâ araçlarına bağlayan eklentidir. Aynı içerik birkaç aracın eklenti biçimiyle birlikte durur; her araç kendi dosyasını okur. Claude için ayrı depo: [asimokat/imzala-claude-eklenti](https://github.com/asimokat/imzala-claude-eklenti).

Arşivde 11,5 milyon Türk yargı ve kurul kararı, doktrin künyeleri, Resmî Gazete tam metni, kanun maddesi haritası ve TCMB/TÜİK verisi bulunur. Yapay zekâ cevabı kendisi yazar; kararın metnini, künyesini ve resmî kaynak bağlantısını arşivden alır.

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
| JetBrains Junie | `/extensions marketplace add asimokat/imzala-claude-eklenti` (Claude biçimindeki depo) |
| Cursor, VS Code, Goose, Perplexity ve diğerleri | MCP sunucusu olarak `https://mcp.imzala.net/mcp` adresini ekleyin (Streamable HTTP). |

İlk kullanımda imzala.net giriş sayfası açılır: e-postanızı yazın, gelen 6 haneli kodu girin ve izin verin. Giriş ekranını desteklemeyen araçlar için [mcp.imzala.net/anahtar](https://mcp.imzala.net/anahtar) adresinden kişisel anahtar alınır ve `Authorization: Bearer imz_…` başlığıyla kullanılır.

### DeepSeek Harness

DeepSeek Harness uzak MCP sunucusuna giriş ekranıyla bağlanamaz; kişisel anahtar kullanılır.

1. [mcp.imzala.net/anahtar](https://mcp.imzala.net/anahtar) adresinden anahtarınızı alın. Anahtar `imz_` ile başlar.
2. Depoyu indirip açın ve PowerShell'de şunu çalıştırın: `powershell -ExecutionPolicy Bypass -File deepseek-harness\kur.ps1`
   Betik `~/.dsh/profiles/desktop/cordis.patch.yml` dosyasının yedeğini alıp imzala girdisini ekler. Skill'leri `~/.dsh/skills` altına kopyalar, kısa kuralları `~/.dsh/AGENTS.md` dosyasına yazar ve anahtarı sorar.
3. DeepSeek Harness'ı tamamen kapatıp yeniden açın. Aletler `mcp__imzala__ictihat_ara` gibi adlarla görünür.

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

## English summary

This plugin connects AI tools to the imzala.net Turkish case-law archive through a remote MCP server at `https://mcp.imzala.net/mcp` (12 tools; nothing is written to the archive). The same content ships in several formats side by side: Agent Plugins (`plugin.json`, `mcp.json`, `skills/`), Gemini CLI (`gemini-extension.json`, `GEMINI.md`), Google Antigravity (`plugin.json`, `mcp_config.json`, `rules/AGENTS.md`) and DeepSeek Harness (`deepseek-harness/`: a `cordis.patch.yml` fragment that connects with a personal API key, plus an installer script). It includes a research-method skill, a Turkish petition-writing skill with a Markdown-to-UDF converter (standard-library Python, no network access) and an onboarding skill. Sign-in is by e-mail code (OAuth 2.1 with dynamic client registration and client ID metadata documents); tools without OAuth can use a personal API key as a Bearer token. The service is paid and starts with a 14-day trial. The content is in Turkish. Support: https://imzala.net/yardim · Privacy policy: https://imzala.net/api-gizlilik

## Lisans

MIT, bkz. [LICENSE](LICENSE). Lisans yalnız bu depodaki eklenti dosyalarını kapsar; imzala.net hizmeti ve arşiv içeriği [kullanım koşullarına](https://imzala.net/api-kosullar) tabidir.
