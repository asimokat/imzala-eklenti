---
name: ictihat-arastirma
description: Türk hukukunda içtihat, emsal karar ya da "Yargıtay bu konuda ne diyor" sorusunda imzala.net arşiviyle araştırma yöntemi. İki arama birlikte, okumadan atıf yok, künye doğrulanır.
---

# İçtihat araştırması

Bu skill, imzala içtihat bağlayıcısının aletleriyle Türk hukukunda karar araştırmasının yöntemini anlatır. Aletleri bağlayıcı sağlar; bu skill yalnız nasıl kullanılacaklarını söyler.

## Bağlayıcı bağlı değilse

Aşağıdaki aletler görünmüyorsa kullanıcıdan imzala bağlayıcısını bağlamasını iste: eklentinin **Connectors** sekmesi → bağlan → imzala.net sayfasında e-posta → gelen 6 haneli kod. Bağlantı yokken ezberden karar, künye ya da alıntı yazma.

## Çalışma düzeni

1. **Arşivle başla.** İçtihat için web araması yapma. Arşivde 11,5 milyon karar var: Yargıtay, Danıştay, Hukuk ve Ceza Genel Kurulları, İçtihadı Birleştirme, Anayasa Mahkemesi, AİHM, Sayıştay, KİK, KDK, Rekabet Kurumu, TİHEK, Uyuşmazlık Mahkemesi, bölge adliye ve yerel mahkemeler.
2. **İki aramayı birlikte kullan.** Kelime araması kesin ve dardır, anlam araması kelimenin kaçırdığını bulur. Aynı vakada farklı kararlar getirirler; biri diğerinin yerine geçmez.
   - `ictihat_ara`: kısa terim ve süzgeç (daire, yıl, dal, sonuç, belge türü, dayanılan madde). Cümleyle arama sıfır sonuç döndürür: "belirsiz alacak ıslah" yaz, "müvekkilin ıslah dilekçesi geçerli midir" yazma.
   - `ictihat_semantik`: olayı doğal cümleyle anlat.
3. **Anlam aramasında Türkçe harf kullan.** Kelime araması harfleri ASCII'ye katlar, anlam araması katlamaz. "muvekkil isten cikarildi" alakasız kararlar getirir, "müvekkil işten çıkarıldı" doğru daireyi bulur. Hata vermez, sessizce yanlış sonuç verir.
4. **Atıf yapmadan önce kararı oku.** `karar_getir` ile metni aç. Okumadığın karara dayanma, arama sonucundaki özetten çıkarım yapma. Varsayılan `hukum` (hüküm fıkrası) çoğu iş için yeterlidir. `kesit` bir terimin geçtiği yeri çevresiyle getirir. `tam` bütün metni verir; kararlar 30-60 bin karakter olduğundan yalnız gerçekten gerektiğinde iste.
5. **Künyeyi metinden al, sonra doğrula.** Künyeyi ve resmî kaynak bağlantısını kararın kendi metninden al; ezberden künye yazma. Kullanıcının verdiği ya da metne girecek her künyeyi `kunye_dogrula` ile doğrula. Arşivde bulunamayan künyeyi kullanıcıya bildir; doğrulanmadan metne alma.
6. **Çevreyi tara.** İşe yarayan bir karar için `benzer_kararlar` ile aynı dayanağa oturan başka kararları ara.
7. **Kapsamlı soruda derin araştırma yap.** Tek aramaya sığmayan soruda `arastirma_baslat` ile işi başlat, sonucu `arastirma_sonuc` ile al. İş genelde 4 dakika sürer; "SÜRÜYOR" cevabında aynı iş kimliğiyle yeniden çağır.

## Hangi alet ne zaman

| Alet | Ne zaman |
|---|---|
| `ictihat_ara` | Kısa terimle kelime araması. `atif` süzgeci bir maddeye gerçekten dayanan kararları bulur ("hmk 107"). |
| `ictihat_semantik` | Olayı doğal cümleyle anlatarak anlam araması. |
| `karar_getir` | Bir kararın metni: `hukum`, `kesit` ya da `tam`. |
| `kunye_dogrula` | Esas ve karar numarasıyla "bu karar gerçekten var mı". Daire ve tarih verilirse arşivdekiyle karşılaştırır. |
| `benzer_kararlar` | Aynı dayanaklara oturan kararlar. AYM kararlarında sonradan atıf yapan kararlar da gelir. |
| `madde_haritasi` | Bir kanun maddesine dayanan kararlarda merci, sonuç ve yıl dağılımı. Strateji sorusu için. |
| `doktrin_ara` | Tez ve makale künyeleri. İçtihat değil görüş aranırken. |
| `resmi_gazete_ara` | 2000'den bugüne Resmî Gazete tam metni: yayım günü, ilan, değişikliğin çıktığı sayı. |
| `hukuk_gundemi` | TBMM kanun teklifleri, yeni yasalaşan değişiklikler ve hukuk basını. |
| `veri_getir` | Faiz (avans, reeskont), endeks (TUFE, UFE_TOPLAM, YIUFE, INSAAT, HUFE) ve döviz kuru. Kaynak TCMB ve TÜİK. |
| `arastirma_baslat`, `arastirma_sonuc` | Derin araştırma: soruyu alt sorulara bölen, atıfları doğrulanmış rapor. |

## Dikkat edilecekler

- **Aletleri sırayla çağır.** Sunucu bir hesaptan aynı anda tek çağrı kabul eder; iki alet birlikte çağrılırsa biri "Aynı anda en çok 1 çağrı" hatasıyla döner. Dakikalık istek tavanı dolarsa doğrulanamayan künyeleri kullanıcıya açıkça söyle.
- **Tırnak içine yalnız birebir söz al.** Karar metninde aynen geçmeyen ifadeyi tırnağa koyma. Özetlediğin görüşü, karşı oy dahil, tırnaksız yaz.
- **Teklif kanun değildir.** `hukuk_gundemi` ile gelen kanun teklifi yasalaşmamıştır ve dilekçeye dayanak yapılmaz. Anılacaksa durumuyla birlikte yazılır: KOMİSYONDA, GÜNDEMDE ya da KANUNLAŞTI.
- **Sayıyı hafızadan yazma.** Faiz oranı, endeks ve kur `veri_getir` ile alınır ve kaynağı yazılır. Endekste hangi ölçütün kullanıldığı açıkça belirtilir.
- **Doktrinde telif vardır.** Kararlar FSEK m.31 gereği serbesttir; tez ve makaleler değildir. Doktrini künye vererek özetle, gövdesini kopyalama.
- **Resmî Gazete aramasında harfleri aynen yaz.** Bu indeks harf katlaması yapmaz: "iflas" ile "iflâs" farklı eşleşir.
