---
name: study
description: Ders calisma modu. Belirtilen dersin materyallerini yukler, ozetler ve pratik yaptirir.
user_invocable: true
---

# /study — Ders Calisma Modu

Kullanim: `/study ie450`, `/study ie201`, `/study ie440` vb.

Arguman olarak ders kisa adi verilir (ie201, ie341, ie423, ie440, ie450, htr311).

## Ders klasor eslesmesi
- ie201 → courses/ie201_programming
- ie341 → courses/ie341_economics
- ie423 → courses/ie423_quality
- ie440 → courses/ie440_nonlinear
- ie450 → courses/ie450_stochastic
- htr311 → courses/htr311_tarih

## Adimlar

### Otomatik Check (her study basinda)
Oncelikle su iki komutu calistir:
1. `python3 ~/Desktop/Boun/sync/sync_courses.py` — yeni materyal var mi kontrol et
2. `python3 ~/Desktop/Boun/dashboard/status.py` — genel durumu goster

Yeni indirilen dosya veya okunmamis mesaj varsa kullaniciya kisa bildir, sonra derse gec.

### Ders calisma
1. `courses/<ders>/course_info.md` dosyasini oku — kitaplar, haftalik program, sinav tarihleri, notlandirma burada
2. Bugunun tarihine gore hangi haftada oldugunu belirle ve o haftanin konusunu bul
3. `courses/<ders>/materials/` altindaki ilgili PDF dosyalarini oku (su anki konuyla ilgili olanlari oncelikle)
4. `courses/<ders>/notes/` altinda kullanicinin kendi notlari varsa onlari da oku
5. `courses/<ders>/exams/` altinda cikmis sorular varsa onlari da oku
6. Yaklasan sinav varsa (7 gun icinde) uyar ve o sinava yonelik calisma plani olustur

## Ders bazli strateji

### IE 440 (Nonlinear OR) — ZOR
- Ders notlarindaki teoriyi adim adim acikla
- Optimizasyon formülasyonlarini orneklerle goster
- Problem cozme teknikleri ve adimlarini anlat

### IE 450 (Stochastic OR) — ZOR
- Markov zincirleri, stokastik surecler gibi konulari acikla
- Study set ve problem set'lerdeki sorulari birlikte coz
- Formul ve kavram kartlari olustur

### IE 201 (Programming/OOP) — ZOR
- Lecture kodlarini acikla, calistir
- OOP kavramlarini (class, inheritance, polymorphism) orneklerle goster
- Pratik kodlama sorulari uret ve kullaniciya cozdur

### IE 423 (Quality Eng.) — ORTA
- Odev odakli: yaklasan odevi bul ve yardim et
- Istatistik/kalite kontrol konularini ozetle

### IE 341 (Eng. Economics) — KOLAY
- TVM, annuity formulleri hizli ozet
- Problem cozmede yardim

### HTR 311 (Tarih) — KOLAY
- Haftalik okumalarin kisa ozetleri
- Sinav oncesi kronolojik ozet

## Cikti
- Oncelikle dersin su anki konusunun ozetini ver
- Kullaniciya ne yapmak istedigini sor: ozet mi, soru cozme mi, pratik mi
