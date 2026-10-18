---
name: dilekce-yazimi
description: Dilekçe, layiha, mütalaa ya da ihtarname yazarken uygulanır. Gerekçe ile içtihat ayrı paragrafta durur, alıntı birebirdir, aleyhe içtihat gösterilir, ekler listelenir.
---

# Dilekçe ve hukuki metin yazımı

Dilekçe, layiha, mütalaa, ihtarname: hangi hukuki metin olursa olsun bu kurallar geçerlidir.

## Künye anlatımı bölmez

İçtihat cümlenin içine parantezle serpiştirilmez; paragrafın altında ayrı bir delil satırı olarak durur. Metin iki katmanlıdır.

**1. Gerekçe paragrafı.** Numaralı, tek fikri anlatan, akıcı metin. İçinde karar künyesi bulunmaz. Kanun maddesi atfı (TBK m.112, TKHK m.5/2) cümle içinde kalabilir; kısadır, okumayı bozmaz. Ek atfı (EK-3) da kalabilir.

**2. İçtihat paragrafı.** Hemen altında, ayrı paragraf, tamamı italik:

> *Yargıtay … Hukuk Dairesi'nin GG.AA.YYYY tarihli ve YYYY/NNNN E., YYYY/NNNN K. sayılı kararı: "…kararın kendi metninden birebir alıntı…"*

İçtihat paragrafının kuralları:

- Alıntı 1-3 cümleyi geçmez ve karar metninde **birebir** geçer. Metinde bulamadığın cümleyi tırnak içine alma.
- Bir gerekçe paragrafının altına en çok iki içtihat konur. Fazlaysa gerekçeyi böl.
- İçtihat paragrafı yalnız üstündeki gerekçeyi destekler.
- Alıntı kararın kendi gerekçesi değil de aktardığı önceki bozma ilamıysa bunu künyede belirt ("…kararında aktarıldığı üzere").
- Bağlam farkı varsa künyede söyle ("arsa payı karşılığı inşaat sözleşmesine ilişkin olmakla birlikte ölçü ortaktır").
- Aleyhe içtihadı saklama. Ayrı paragrafta göster ve nasıl ayrıştığını yaz.

Alıntıyı ve künyeyi kararın kendi metninden al. imzala bağlayıcısı bağlıysa metni `karar_getir` ile oku, künyeyi `kunye_dogrula` ile doğrula; yöntem `ictihat-arastirma` skill'indedir. Okunmamış ya da doğrulanmamış karar metne girmez.

## Yasak biçim

Künyenin cümle içinden geçtiği bu biçim kullanılmaz:

> [Önerme] (TBK m.112; [Merci], GG.AA.YYYY, YYYY/NNNN E., YYYY/NNNN K.). Yargıtay; [önerme] ([Daire], GG.AA.YYYY, YYYY/NNNN E., YYYY/NNNN K.) … kabul etmektedir.

Bu biçimde numaralar ve daireler cümlenin içinden art arda geçer, anlatım okunmaz hâle gelir. Doğrusu: önerme gerekçe paragrafında anlatılır, her karar altta kendi italik paragrafında durur.

## Dil

- Sade Türkçe hukuk dili kullanılır, süslü giriş yapılmaz.
- Her paragraf tek fikir anlatır.
- "Yani", "kaldı ki", "takvim şudur" gibi konuşma dili ve doldurma bağlaçlar kullanılmaz.

## Biçim ve UDF teslimi

- Metni Markdown ile yaz: `### ` başlık, `**kalın**`, `*italik*`, `> ` alıntı bloğu, `- ` madde.
- UYAP'a verilecek metin UDF biçiminde teslim edilir. Kullanıcı UDF isterse ya da metin UYAP'a gidecekse Markdown dosyasını bu skill'in klasöründeki dönüştürücüyle çevir (`<skill klasörü>`, bu SKILL.md dosyasının bulunduğu klasördür):

  ```bash
  python "<skill klasörü>/scripts/md2udf.py" dilekce.md dilekce.udf
  ```

- Dönüştürücü art arda gelen satırları tek paragrafta birleştirir. DAVACI, VEKİLİ, KONU gibi ayrı satırda kalması gereken her satırın arasına boş satır koy.
- Dönüştürücü yalnız Python'un kendi kütüphanelerini kullanır ve ağa bağlanmaz. Çıktı Times New Roman 12 punto, iki yana yaslıdır. Başlıklar kalın yazılır, alıntı blokları ve maddeler girintili olur. Başarılı çalışınca paragraf ve karakter sayısını yazar; bu satırı kullanıcıya ilet.
- Python yoksa ya da dönüştürücü çalışmazsa bunu kullanıcıya söyle ve metni Markdown olarak teslim et.
- e-imzalı gelen UDF belgeler (arabuluculuk tutanağı, tensip zaptı) PDF'e çevrilmez, orijinal hâliyle ek yapılır.

## Ekler

Dosya sistemine erişim varsa:

- Dilekçeyle aynı yerde `ekler/` klasörü açılır.
- Dosya adları `EK-01-...` biçimindedir; numaralar dilekçedekiyle birebir aynı ve boşluksuzdur.
- Elde olmayan belge ek listesine yazılmaz; gerekiyorsa delil listesinde "celbi talep olunur" satırı olur.
- Klasöre `00-EKLER-LISTESI.md` konur: hangi ek ne, hangisi eksik, nereden gelecek.

Dosya sistemi yoksa (yalnız sohbet) aynı ek listesi metnin sonunda verilir.
