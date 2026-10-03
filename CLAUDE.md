# Boun - Bogazici Academic Hub

Bogazici IE ogrencileri icin akademik hub. Moodle API uzerinden ders iceriklerini ceker, organize eder ve calisma materyallerini bir arada tutar.

## Dersler (2026/2027-1)

| Kisa Ad | Ders | Moodle ID | Klasor |
|---------|------|-----------|--------|
| IE 201 | Intermediate Programming | 85966 | ie201_programming |
| IE 341 | Engineering Economics | 85764 | ie341_economics |
| IE 423 | Quality Engineering | 84679 | ie423_quality |
| IE 440 | Nonlinear Models in OR | 83575 | ie440_nonlinear |
| IE 450 | Stochastic Models in OR | 84273 | ie450_stochastic |
| HTR 311 | History of the Turkish Republic I | 85927 | htr311_tarih |

## Yapi

- `sync/` — Moodle API client ve sync scriptleri
- `courses/<ders>/materials/` — Moodle'dan indirilen dosyalar (gitignore'da)
- `courses/<ders>/notes/` — Kendi notlarimiz
- `courses/<ders>/exams/` — Cikmis sorular
- `dashboard/` — Durum ozeti

## Kullanim

```bash
# Moodle'dan tum materyalleri cek
python3 sync/sync_courses.py

# Durum ozeti
python3 dashboard/status.py
```

## Moodle API

Token `.env` dosyasinda. API endpoint: `https://moodle.bogazici.edu.tr/webservice/rest/server.php`

Kullanilan fonksiyonlar:
- `core_enrol_get_users_courses` — ders listesi
- `core_course_get_contents` — ders icerikleri (section/module/file)
- Dosya indirme: `moodle.bogazici.edu.tr/webservice/pluginfile.php/...?token=TOKEN`
