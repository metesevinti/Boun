---
name: check
description: Moodle'dan yeni materyal, mesaj ve deadline kontrolu yapar. Sync calistirir, haftalik ozet verir.
user_invocable: true
---

# /check — Hizli Durum Kontrolu

Bu skill calistirildiginda asagidaki adimlari sirayla yap:

## 1. Sync kontrol
`python3 ~/Desktop/Boun/sync/sync_courses.py` calistir. Yeni indirilen dosya varsa kullaniciya bildir.

## 2. Dashboard
`python3 ~/Desktop/Boun/dashboard/status.py` calistir ve sonucu goster.

## 3. Yaklasan sinavlar
Her dersin `courses/<ders>/course_info.md` dosyasini oku. Bugunun tarihine gore:
- 7 gun icindeki quiz, midterm, odev teslim tarihlerini UYARI olarak goster
- 14 gun icindeki sinavlari HATIRLATMA olarak goster
- Su anki haftanin konusunu belirt

## 4. Oncelik sirasi
Ders oncelikleri (zorluga gore):
1. IE 440 (zor) — quiz ve midterm'lere dikkat
2. IE 450 (zor) — midterm tarihleri onemli
3. IE 201 (zor) — odev deadline'lari
4. IE 423 (orta) — proje ve midterm
5. IE 341 (kolay) — attendance %10, devamsizlik yapma
6. HTR 311 (kolay) — minimum efor

## 5. Ozet
En sona kisa bir ozet yaz:
- Kac yeni materyal indirildi
- Kac okunmamis mesaj var
- En yakin sinav ne zaman
- Oneri: hangi derse odaklanmali
