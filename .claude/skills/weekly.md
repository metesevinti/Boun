---
name: weekly
description: Haftalik akademik ozet — derslerin durumu, haftanin konulari, yaklasan sinavlar, calisma plani.
user_invocable: true
---

# /weekly — Haftalik Akademik Ozet

Bu skill her hafta baslangicinda (veya istendiginde) calistirilir.

## Adimlar

### 1. Sync ve guncelleme
- `python3 ~/Desktop/Boun/sync/sync_courses.py` calistir
- `python3 ~/Desktop/Boun/dashboard/generate.py` calistir (HTML dashboard guncelle)

### 2. Bu haftanin konulari
Her dersin `courses/<ders>/course_info.md` dosyasini oku. Bugunun tarihine gore hangi haftadayiz belirle ve her ders icin:
- Bu haftanin konusu
- Yapilmasi gereken (okuma, odev, lab)

### 3. Yaklasan sinavlar ve teslimler
Onumuzdeki 14 gun icindeki tum sinav ve teslim tarihlerini listele:
- Quiz, midterm, final tarihleri
- Odev/proje teslim tarihleri
- Proje grubu olusturma gibi deadline'lar

### 4. Gecen haftanin ozeti
Moodle mesajlarindan gecen haftaki onemli duyurulari ozetle:
- Iptal olan dersler
- Tarih degisiklikleri
- Yeni materyaller

### 5. Haftalik calisma plani onerisi
Ders onceliklerine gore (IE440 > IE450 > IE201 > IE423 > IE341 > HTR311) bir haftalik calisma plani oner:
- Hangi gün hangi derse calismali
- Sinav yaklasiyorsa o derse ekstra zaman ayir
- Zor dersler icin spesifik calisma onerisi (problem coz, konu tekrar et, kod yaz)

### 6. Cikti formati
Kisa ve taranabilir olsun:
```
=== HAFTALIK OZET — [tarih araligi] ===

UYARI: [yaklasan sinavlar]

BU HAFTA:
  IE 440: [konu]
  IE 450: [konu]
  ...

CALISMA PLANI:
  Pazartesi: ...
  Sali: ...
  ...

GECEN HAFTA:
  - [onemli duyurular]
```
