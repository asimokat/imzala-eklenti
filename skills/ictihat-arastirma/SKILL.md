---
name: ictihat-arastirma
description: Türk hukukunda içtihat, emsal karar, mevzuat maddesi, kurul kararı ya da süre/tarife hesabı sorusunda imzala.net arşiviyle araştırma yöntemi. İki arama birlikte, okumadan atıf yok, künye doğrulanır.
---

# İçtihat ve mevzuat araştırması

Bu skill, imzala içtihat ve mevzuat bağlayıcısının 24 aletiyle Türk hukukunda araştırma yöntemini anlatır. Aletleri bağlayıcı sağlar; bu skill yalnız nasıl kullanılacaklarını söyler.

## Bağlayıcı bağlı değilse

Aşağıdaki aletler görünmüyorsa kullanıcıdan imzala bağlantısını kurmasını iste. Yol araca göre değişir (https://github.com/asimokat/imzala-eklenti README'sindeki kurulum tablosu): giriş ekranını destekleyen araçlarda imzala.net sayfası açılır, e-posta ve gelen 6 haneli kodla bağlanılır; desteklemeyenlerde https://mcp.imzala.net/anahtar adresinden alınan kişisel anahtar kullanılır. Bağlantı yokken ezberden karar, kanun maddesi, künye ya da alıntı yazma.

## Çalışma düzeni

1. **Arşivle başla.** İçtihat ve mevzuat için web araması yapma. Arşivde 11,6 milyon karar (Yargıtay, Danıştay, Hukuk ve Ceza Genel Kurulları, İçtihadı Birleştirme, Anayasa Mahkemesi, AİHM Türkçe çevirileri, Sayıştay, KİK, KDK, Rekabet, TİHEK, KVKK, SPK, BDDK, BTK, HSK, TBB, Ticaret Sicili Gazetesi, Uyuşmazlık Mahkemesi, bölge adliye ve yerel mahkemeler, GİB özelgeleri) ve yürürlükteki mevzuat (kanun, KHK, CBK, tüzük, yönetmelik) vardır.
2. **İki aramayı birlikte kullan.** Kelime araması kesin ve dardır, anlam araması kelimenin kaçırdığını bulur. Aynı vakada farklı kararlar getirirler; biri diğerinin yerine geçmez.
   - `ictihat_ara`: kısa terim ve süzgeç (daire, yıl, dal, sonuç, belge türü, dayanılan madde). Cümleyle arama sıfır sonuç döndürür: "belirsiz alacak ıslah" yaz, "müvekkilin ıslah dilekçesi geçerli midir" yazma.
   - `ictihat_semantik`: olayı doğal cümleyle anlat.
3. **Anlam aramasında Türkçe harf kullan.** Kelime araması harfleri ASCII'ye katlar, anlam araması katlamaz. "muvekkil isten cikarildi" alakasız kararlar getirir, "müvekkil işten çıkarıldı" doğru daireyi bulur. Hata vermez, sessizce yanlış sonuç verir.
4. **Atıf yapmadan önce kararı ve kanun maddesini oku.** Kararı `karar_getir` ile, dayanılacak kanun veya mevzuat maddesini `mevzuat_getir` ile aç (kanunu bulmak için önce `mevzuat_ara` ya da `mevzuat_icinde_ara`). Okumadığın karara ya da ezberden madde metnine dayanma. Kararda varsayılan `hukum` (hüküm fıkrası) çoğu iş için yeterlidir; `kesit` bir terimin geçtiği yeri çevresiyle getirir; `tam` bütün metni verir (kararlar 30-60 bin karakter olduğundan yalnız gerektiğinde iste).
5. **Künyeyi metinden al, sonra doğrula.** Künyeyi ve resmî kaynak bağlantısını kararın kendi metninden al; ezberden künye yazma. Kullanıcının verdiği ya da metne girecek her künyeyi `kunye_dogrula` ile doğrula. Arşivde bulunamayan künyeyi kullanıcıya bildir; doğrulanmadan metne alma.
6. **Çevreyi ve atıf ağını tara.** İşe yarayan bir karar için `benzer_kararlar` ile aynı dayanağa oturan emsalleri, `karar_atiflari` ile kararlar arası çift yönlü atıf ağını ("bu karara sonradan hangi kararlar atıf yaptı" ve "bu karar hangilerine atıf yapıyor" — Yargıtay, Danıştay, HGK, İBK, BAM ve AYM) sorgula.
7. **Süre ve parasal hesabı deterministik aletle yap.** Usul sürelerini (UETS `+5 gün`, adli/mali tatil ve resmî/dinî bayram kaydırması dahil) `sure_hesapla` ile; dönem kırılımlı faiz, 2026–2027 AAÜT vekâlet ücreti, 2026 yargı/icra harçları + gider avansı ve SMM hesabını `hukuk_hesapla` ile yap; endeks, kur ve oran serilerini `veri_getir` ile al.
8. **Kapsamlı soruda derin araştırma yap.** Tek aramaya sığmayan soruda `arastirma_baslat` ile işi başlat, sonucu `arastirma_sonuc` ile al. İş genelde 4 dakika sürer; "SÜRÜYOR" cevabında aynı iş kimliğiyle yeniden çağır.

## Hangi alet ne zaman

| Alet | Ne zaman |
|---|---|
| `ictihat_ara` | Kısa terimle kelime araması. `atif` süzgeci bir maddeye gerçekten dayanan kararları bulur ("hmk 107"). |
| `ictihat_semantik` | Olayı doğal cümleyle anlatarak anlam araması. |
| `karar_getir` | Bir kararın (veya açık erişim `CC BY` / `CC0` makalenin) metni: `hukum`, `kesit` ya da `tam`. |
| `kunye_dogrula` | Esas ve karar numarasıyla "bu karar gerçekten var mı" kontrolü (kotasız). |
| `mevzuat_ara` | Kanun, KHK, CBK ve yönetmelikleri ad, numara veya konuyla tam başlık ve RG/kabul tarihiyle bulmak için. |
| `mevzuat_icinde_ara` | Belirli bir kanun veya yönetmeliğin maddeleri içinde kavram taraması yapmak için. |
| `mevzuat_getir` | Belirli madde(ler)in birebir metni (`"344"`, `"Ek 1"`, `"Geçici 2"`, `"343,344,345"`), içindekiler ya da sayfalı metin. |
| `sure_hesapla` | HMK, CMK, İYUK, İİK, VUK/6183 usul süreleri (UETS `+5 gün`, adli/mali tatil ve 2024–2035 dinî bayramlar dahil). |
| `hukuk_hesapla` | Kademeli faiz (`3095`, `6183`, `VUK`), 2026–2027 AAÜT vekâlet ücreti, 2026 yargı/icra harçları + gider avansı ve SMM hesabı. |
| `karar_atiflari` | Yargıtay, Danıştay, HGK, İBK, BAM ve AYM kararlarında gelen/giden karar→karar atıf ağı. |
| `benzer_kararlar` | Aynı dayanaklara oturan kararlar ve sonradan atıf yapan kararlar (`atifYapanlar`). |
| `kurum_karari_ara` | BTK, HSK, TBB, Ticaret Sicili Gazetesi (TTSG), Rekabet, KİK, KVKK, BDDK, SPK, Sayıştay, KDK, TİHEK, Reklam, GİB, SGK, MASAK, KGK ve TÜRMOB kararları. |
| `aym_ara`, `aihm_ara` | Anayasa Mahkemesi (bireysel başvuru/norm denetimi, ihlal/iptal) ve AİHM Türkçe çeviri araması. |
| `madde_haritasi` | Bir kanun maddesine dayanan kararlarda merci, sonuç ve yıl dağılımı. Strateji sorusu için. |
| `doktrin_ara` | 98 bin tez ve makale künyesi + özet (açık erişim `CC BY` / `CC0` makalelerde tam metin). |
| `resmi_gazete_ara` | 2000'den bugüne Resmî Gazete tam metni: yayım günü, ilan, değişikliğin çıktığı sayı. |
| `turkpatent_bulten_ara` | TÜRKPATENT Resmî Bültenleri (Marka, Tasarım, Patent, Coğrafi İşaret, İlanen Tebligat): yayım tarihi, 6769 s. SMK itiraz son günü ve tam metin araması. |
| `hukuk_gundemi` | TBMM kanun teklifleri, yeni yasalaşan değişiklikler ve hukuk basını. |
| `veri_getir` | TCMB faiz ve döviz kurları, TÜİK endeksleri, GİB vergi takvimi/KDV oranları, gecikme zammı ve tecil faizi serileri. |
| `hukuk_rehberi`, `abonelik_karti` | Kotasız araştırma/dilekçe/UDF kılavuzu ve hesap/kota durumu. |
| `arastirma_baslat`, `arastirma_sonuc` | Derin araştırma: soruyu alt sorulara bölen, atıfları doğrulanmış rapor. |

## Dikkat edilecekler

- **Aletleri sırayla çağır.** Sunucu bir hesaptan aynı anda sınırlı sayıda çağrı çalıştırır; fazlası sıraya girer, süren çağrı uzarsa "Aynı anda en çok … çağrı" hatasıyla döner. Bu hatada öncekinin bitmesini bekleyip yeniden çağır. Dakikalık istek tavanı dolarsa doğrulanamayan künyeleri kullanıcıya açıkça söyle. Bir alet cevabının başında "imzala.net bildirimi" varsa kullanıcıya aynen ilet.
- **Tırnak içine yalnız birebir söz al.** Karar veya kanun metninde aynen geçmeyen ifadeyi tırnağa koyma. Özetlediğin görüşü, karşı oy dahil, tırnaksız yaz.
- **Teklif kanun değildir.** `hukuk_gundemi` ile gelen kanun teklifi yasalaşmamıştır ve dilekçeye dayanak yapılmaz. Anılacaksa durumuyla birlikte yazılır: KOMİSYONDA, GÜNDEMDE ya da KANUNLAŞTI.
- **Sayıyı ve süreyi hafızadan yazma.** Usul süresi `sure_hesapla`, faiz/tarife/harç `hukuk_hesapla`, faiz oranı/endeks/kur `veri_getir` ile alınır ve kaynağı yazılır.
- **Doktrinde telif sınırını koru.** Kararlar ve resmî mevzuat FSEK m.31 gereği serbesttir; telif korumalı tez ve makalelerde FSEK m.35 gereği yalnız künye, özet ve kaynak bağlantısı kullanılır. Yalnız açık erişim (`CC BY` / `CC0`) lisanslı makalelerde `karar_getir` tam metin döndürür; yine kaynak gösterilerek kullanılır.
- **Resmî Gazete aramasında harfleri aynen yaz.** Bu indeks harf katlaması yapmaz: "iflas" ile "iflâs" farklı eşleşir.
