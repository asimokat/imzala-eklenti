# imzala.net içtihat arşivini DeepSeek Harness'a ekler.
#   1) Profilin cordis.patch.yml dosyasına imzala MCP girdisini ekler; önce yedek alır.
#   2) ictihat-arastirma ve dilekce-yazimi skill'lerini ~/.dsh/skills altına kopyalar.
#   3) Kısa çalışma kurallarını ~/.dsh/AGENTS.md içine işaretli bir bölüm olarak yazar.
#   4) IMZALA_ANAHTAR tanımlı değilse anahtarı sorar; boş geçilebilir.
# Yeniden çalıştırmak güvenlidir: yama ikinci kez eklenmez, kurallar bölümü yenilenir.
# Kullanım: powershell -ExecutionPolicy Bypass -File kur.ps1 [-Profil desktop] [-AnahtarSorma]
param([string]$Profil = 'desktop', [switch]$AnahtarSorma)
$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding $false
$burasi = Split-Path -Parent $MyInvocation.MyCommand.Path
$depo = Split-Path -Parent $burasi
$dsh = if ($env:DSH_HOME) { $env:DSH_HOME } else { Join-Path $HOME '.dsh' }
$damga = Get-Date -Format 'yyyyMMdd-HHmmss'

function Oku([string]$yol) { [IO.File]::ReadAllText($yol, $utf8) }
function Yaz([string]$yol, [string]$metin) { [IO.File]::WriteAllText($yol, $metin, $utf8) }

# 1) MCP yaması
$yama = Join-Path $dsh "profiles\$Profil\cordis.patch.yml"
if (-not (Test-Path $yama)) { throw "Bulunamadı: $yama. DeepSeek Harness'ı bir kez açıp kapatın, sonra yeniden deneyin." }
$metin = Oku $yama
if ($metin -match '(?m)^\s*-\s*id:\s*mcp-imzala\s*$') {
  Write-Host 'MCP yaması zaten var; dokunulmadı.'
} else {
  Copy-Item $yama "$yama.yedek-$damga"
  $sat = if ($metin.Contains("`r`n")) { "`r`n" } else { "`n" }
  $parca = ((Oku (Join-Path $burasi 'cordis.patch.yml')) -replace "`r`n", "`n") -replace "`n", $sat
  if ($metin.Length -gt 0 -and -not $metin.EndsWith("`n")) { $metin += $sat }
  Yaz $yama ($metin + $parca)
  Write-Host "MCP yaması eklendi. Yedek: $yama.yedek-$damga"
}

# 2) Skill'ler
$skillKok = Join-Path $dsh 'skills'
New-Item -ItemType Directory -Force -Path $skillKok | Out-Null
foreach ($s in 'ictihat-arastirma', 'dilekce-yazimi') {
  $hedef = Join-Path $skillKok $s
  if (Test-Path $hedef) { Remove-Item $hedef -Recurse -Force }
  Copy-Item (Join-Path $depo "skills\$s") $hedef -Recurse
}
Write-Host "Skill'ler kopyalandı: $skillKok"

# 3) Çalışma kuralları (işaretler arasındaki bölüm her çalıştırmada yenilenir)
$agents = Join-Path $dsh 'AGENTS.md'
$bas = '<!-- imzala:baslangic -->'
$son = '<!-- imzala:bitis -->'
$bolum = "$bas`n" + ((Oku (Join-Path $burasi 'AGENTS.md')) -replace "`r`n", "`n").TrimEnd() + "`n$son`n"
if (Test-Path $agents) {
  $eski = Oku $agents
  Copy-Item $agents "$agents.yedek-$damga"
  $i = $eski.IndexOf($bas)
  $j = $eski.IndexOf($son)
  if ($i -ge 0 -and $j -gt $i) {
    $kalan = $eski.Substring($j + $son.Length).TrimStart("`r", "`n")
    $yeni = $eski.Substring(0, $i) + $bolum + $kalan
  } else {
    $yeni = $eski.TrimEnd() + "`n`n" + $bolum
  }
  Yaz $agents $yeni
} else {
  Yaz $agents $bolum
}
Write-Host "Çalışma kuralları yazıldı: $agents"

# 4) Anahtar
if ([Environment]::GetEnvironmentVariable('IMZALA_ANAHTAR', 'User')) {
  Write-Host 'IMZALA_ANAHTAR tanımlı.'
} elseif ($AnahtarSorma) {
  Write-Host 'IMZALA_ANAHTAR tanımlı değil. Anahtarı https://mcp.imzala.net/anahtar adresinden alıp kullanıcı ortam değişkeni olarak tanımlayın.'
} else {
  $gizli = Read-Host 'imzala anahtarınızı yapıştırın (imz_ ile başlar; boş geçebilirsiniz)' -AsSecureString
  $a = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($gizli))
  if ($a) {
    [Environment]::SetEnvironmentVariable('IMZALA_ANAHTAR', $a.Trim(), 'User')
    Write-Host 'IMZALA_ANAHTAR kaydedildi.'
  } else {
    Write-Host 'Anahtar girilmedi; sonra tanımlayabilirsiniz.'
  }
}
Write-Host "Bitti. DeepSeek Harness'ı tamamen kapatıp yeniden açın; aletler mcp__imzala__ adıyla görünür."
