# Boun - Bogazici Academic Hub

Bogazici ogrencileri icin akademik hub. Moodle'dan ders materyallerini otomatik ceker, durum dashboard'u olusturur ve Claude Code ile ders calisma ortami saglar.

## Kurulum

### 1. Repo'yu klonla

```bash
git clone https://github.com/metesevinti/Boun.git
cd Boun
```

### 2. Python bagimliliklar

```bash
pip install requests python-dotenv
```

### 3. Moodle token'ini al

1. https://moodle.bogazici.edu.tr adresine giris yap
2. **Preferences** > **Security keys** sayfasina git
3. **Mobile web service** token'ini kopyala (yoksa olustur)

### 4. `.env` dosyasini olustur

```bash
cp .env.example .env
```

`.env` dosyasini duzenle:

```env
MOODLE_TOKEN=senin_moodle_tokenin
MOODLE_URL=https://moodle.bogazici.edu.tr
MOODLE_USER_ID=senin_user_idn
COURSES=12345:ders1_adi,67890:ders2_adi
```

**Moodle User ID nasil bulunur:**
- Moodle'da profiline git, URL'deki `id=` parametresine bak
- Veya: `python3 -c "import requests; r=requests.get('https://moodle.bogazici.edu.tr/webservice/rest/server.php', params={'wstoken':'TOKENIN','wsfunction':'core_webservice_get_site_info','moodlewsrestformat':'json'}); print(r.json()['userid'])"`

**Ders ID nasil bulunur:**
- Moodle'da dersin sayfasina git, URL'deki `course/view.php?id=XXXXX` — o `XXXXX` ders ID'si

**COURSES formati:**
```
COURSES=DERS_ID:klasor_adi,DERS_ID:klasor_adi,...
```

Ornek:
```
COURSES=85966:ie201_programming,85764:ie341_economics,83575:ie440_nonlinear
```

### 5. Ilk sync

```bash
python3 sync/sync_courses.py
```

Bu komut tum ders materyallerini `courses/<ders>/materials/` altina indirir.

## Kullanim

### Terminal komutlari

```bash
# Moodle'dan yeni materyalleri cek
python3 sync/sync_courses.py

# Terminal'de durum ozeti
python3 dashboard/status.py

# HTML dashboard olustur
python3 dashboard/generate.py
```

### Claude Code skills

[Claude Code](https://claude.com/claude-code) yukluyse bu skill'leri kullanabilirsin:

| Komut | Aciklama |
|-------|----------|
| `/check` | Sync + durum kontrolu + yaklasan sinavlar |
| `/study ie440` | Belirtilen derse calisma modu (otomatik check dahil) |
| `/weekly` | Haftalik akademik ozet ve calisma plani |

## Kendi derslerini ekleme

Farkli dersler aliyorsan:

1. `.env`'deki `COURSES`'a kendi ders ID ve klasor adlarini ekle
2. Sync'i calistir — klasorler otomatik olusur
3. `courses/<ders>/course_info.md` dosyasini olustur (syllabus bilgileri, haftalik program, sinav tarihleri)
4. `.claude/skills/` altindaki skill dosyalarini kendi derslerine gore duzenle

### course_info.md sablonu

```markdown
# DERS_KODU — Ders Adi

## Genel
- Hoca: ...
- Office Hours: ...

## Notlandirma
- Midterm: %X
- Final: %X
- Odev: %X

## Kaynaklar
- Kitap1
- Kitap2

## Haftalik Program
| Hafta | Tarih | Konu |
|-------|-------|------|
| 1 | ... | ... |
| 2 | ... | ... |
```

## Klasor yapisi

```
Boun/
├── .env                    # Moodle token (PAYLASILMAZ, gitignore'da)
├── .env.example            # Ornek .env sablonu
├── .claude/skills/         # Claude Code skill'leri
│   ├── check.md
│   ├── study.md
│   └── weekly.md
├── sync/
│   ├── moodle_client.py    # Moodle API wrapper
│   └── sync_courses.py     # Materyal indirici
├── courses/
│   └── <ders>/
│       ├── course_info.md  # Syllabus, program, sinavlar
│       ├── materials/      # Moodle'dan indirilen dosyalar (gitignore'da)
│       ├── notes/          # Kendi notlarin
│       └── exams/          # Cikmis sorular
└── dashboard/
    ├── status.py           # Terminal dashboard
    ├── generate.py         # HTML dashboard olusturucu
    └── index.html          # Olusturulan dashboard
```

## Onemli notlar

- `.env` dosyasi **asla commit edilmez** — icinde Moodle token'in var
- `courses/*/materials/` gitignore'da — herkes kendi sync'ler
- `courses/*/notes/` ve `courses/*/exams/` paylasilabilir — cikmis sorulari ve notlari buraya koy
