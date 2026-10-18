# imzala.net içtihat arşivi: çalışma kuralları

Bu kurallar `imzala` MCP sunucusunun aletleri kullanılırken geçerlidir: `ictihat_ara`, `ictihat_semantik`, `karar_getir`, `kunye_dogrula`, `benzer_kararlar`, `madde_haritasi`, `doktrin_ara`, `resmi_gazete_ara`, `hukuk_gundemi`, `veri_getir`, `arastirma_baslat`, `arastirma_sonuc`.

1. Türk hukukunda karar, emsal ya da "Yargıtay bu konuda ne diyor" sorusunda önce imzala arşivini kullan. İçtihat için web araması yapma.
2. Kelime aramasıyla anlam aramasını birlikte kullan. `ictihat_ara` kısa terim ister: "belirsiz alacak ıslah" yaz, cümle yazma. `ictihat_semantik` olayı doğal cümleyle anlatır. Anlam aramasında Türkçe harfleri koru: "müvekkil işten çıkarıldı" yaz, "muvekkil isten cikarildi" yazma.
3. Atıf yapmadan önce kararı `karar_getir` ile oku. Arama sonucundaki özetten çıkarım yapma.
4. Künyeyi ve resmî kaynak bağlantısını kararın kendi metninden al. Metne girecek her künyeyi `kunye_dogrula` ile doğrula. Arşivde bulunamayan künyeyi kullanıcıya bildir ve metne alma.
5. Tırnak içine yalnız karar metninde birebir geçen sözü al. Özetlediğin görüşü tırnaksız yaz.
6. Aletleri sırayla çağır. Sunucu bir hesaptan aynı anda tek çağrı kabul eder.
7. Kanun teklifi kanun değildir; dayanak yapılmaz. Faiz, endeks ve kur bilgisini `veri_getir` ile al ve kaynağını yaz; hafızadan yazma.
8. Tek aramaya sığmayan soruda `arastirma_baslat` ile derin araştırma başlat, sonucu `arastirma_sonuc` ile al. İş genelde 4 dakika sürer.
9. Aletler görünmüyorsa kullanıcıdan imzala bağlantısını kurmasını iste. İlk kullanımda imzala.net giriş sayfası açılır; kullanıcı e-postasını yazar, gelen 6 haneli kodu girer ve izin verir. Bağlantı yokken ezberden karar, künye ya da alıntı yazma.

Ayrıntılı yöntem `ictihat-arastirma` skill'inde, dilekçe biçimi `dilekce-yazimi` skill'inde anlatılır.

## DeepSeek Harness'a özgü

- imzala anahtarını (`imz_` ile başlar) hiçbir dosyaya yazma, yapılandırmaya gömme, sohbette gösterme; `IMZALA_ANAHTAR` ortam değişkeninin değerini okuma.
- `mcp__imzala__` aletleri görünmüyorsa yapılandırmayı kendin düzeltme. Kullanıcıya `deepseek-harness/kur.ps1` betiğini yeniden çalıştırmasını ve DeepSeek Harness'tan sistem tepsisindeki Çıkış ile tamamen çıkıp uygulamayı yeniden açmasını öner.
