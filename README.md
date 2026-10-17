# imzala.net: yapay zekâ eklentisi

Bu depo imzala.net içtihat arşivini Claude dışındaki yapay zekâ araçlarına bağlayan eklentidir. Ortak eklenti biçimini (Agent Plugins, kökte `plugin.json`) kullanır. Claude için ayrı depo: [asimokat/imzala-claude-eklenti](https://github.com/asimokat/imzala-claude-eklenti).

Arşivde 11,5 milyon Türk yargı ve kurul kararı, doktrin künyeleri, Resmî Gazete tam metni, kanun maddesi haritası ve TCMB/TÜİK verisi bulunur. Yapay zekâ cevabı kendisi yazar; kararın metnini, künyesini ve resmî kaynak bağlantısını arşivden alır.

## İçindekiler

| Parça | Ne yapar |
|---|---|
| `mcp.json` | `https://mcp.imzala.net/mcp` adresindeki uzak MCP sunucusuna bağlanır. 12 alet, hepsi salt okunur. |
| `skills/get-started` | İlk bağlantıyı ve ilk soruları anlatır. |
| `skills/ictihat-arastirma` | Arama yöntemi: kelime ve anlam araması birlikte, okumadan atıf yok, künye doğrulama. |
| `skills/dilekce-yazimi` | Dilekçe biçimi ve `md2udf.py` ile UYAP'ın UDF biçimine dönüştürme. |

## Kurulum

- **Codex:** `codex plugin marketplace add asimokat/imzala-eklenti`
- **Cursor, Perplexity ve diğerleri:** Aracın eklenti ekleme ekranına bu deponun adresini yazın.

İlk kullanımda imzala.net giriş sayfası açılır: e-postanızı yazın, gelen 6 haneli kodu girin ve izin verin.

## Ne gönderir, ne saklar

- Eklenti yalnız `https://mcp.imzala.net/mcp` adresine bağlanır. Kanca ve yerel sunucu içermez.
- Eklentideki tek program `md2udf.py` dönüştürücüsüdür. Python'un kendi kütüphaneleriyle çalışır, ağa bağlanmaz ve yalnız bir dilekçe UDF'ye çevrilirken çalışır.
- Arama aletlerinin sorgu metni sunucuda kaydedilmez. Derin araştırmada sorunun ilk 300 karakteri iş kaydına yazılır ve araştırma Google Gemini ile yürütülür.
- Ayrıntı: [API gizlilik bildirimi](https://imzala.net/api-gizlilik) · [API kullanım koşulları](https://imzala.net/api-kosullar)

Hizmeti kullanmak için bir imzala.net hesabı gerekir: [imzala.net/yapay-zeka](https://imzala.net/yapay-zeka)

## English summary

This plugin connects AI tools to the imzala.net Turkish case-law archive through a read-only remote MCP server at `https://mcp.imzala.net/mcp`. It uses the Agent Plugins format (root `plugin.json`, `mcp.json`, `skills/`). It includes a research-method skill, a Turkish petition-writing skill with a Markdown-to-UDF converter (standard-library Python, no network access) and an onboarding skill. Sign-in is by e-mail code. An imzala.net account is required. The content is in Turkish.

## Lisans

MIT, bkz. [LICENSE](LICENSE). Lisans yalnız bu depodaki eklenti dosyalarını kapsar; imzala.net hizmeti ve arşiv içeriği [kullanım koşullarına](https://imzala.net/api-kosullar) tabidir.
