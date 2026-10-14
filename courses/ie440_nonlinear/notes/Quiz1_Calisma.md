# IE 440 — Quiz 1 Çalışma Dosyası

**Format (hoca söyledi):** 3 soru.
1. **Convex / concave analizi** (Hessian, principal minors, tanım/ispat)
2. **One-direction search** (dichotomous, golden section, bisection, Newton)
3. **Genel** (hoca konu vermedi) → aşağıda çıkmışlardan tahmin listesi

Kapsam: Hafta 1–4 (Intro NLP, One Direction, Convexity). Teori için `Ders_Notlari_Ozet.md`.

## ★ Gerçek Quiz 1 çıkmışı: `2013 quiz 1.pdf` (Altınel, 23 Ekim 2013, 50 dk, closed book)
Bu, elimizdeki **tek gerçek Quiz 1** — hocanın söylediği 3 soru yapısıyla birebir örtüşüyor ("search / convex check / general"):

| Soru | Puan | İçerik | Çözüm özeti |
|---|---|---|---|
| Q1 | 30 | Polyhedron P={3x₁−7x₂≥−6, 5x₁−x₂≥−4, x₁≥0, x₂≥2}: a) extreme point/direction, b) (3,2)ᵀ'yi göster, c) **Minkowski teoremi** ile eşdeğer tanım | Extreme point (8/3,2); extreme directions d₁=(1,0), d₂=(7,3) [= (1,3/7)·7]. (3,2)=1·(8/3,2)+⅓·d₁+0·d₂. Minkowski: P={x : x=λ(8/3,2)+μ₁d₁+μ₂d₂, **λ=1**, μ₁,μ₂≥0} |
| Q2 | 30 | min x²+1, −2.5≤x≤1.75: a) **unimodality** göster, b) Bisection kaç iterasyon (ε=0.0001), c) Golden Section kaç iterasyon | a) f″=2>0 ⇒ strictly convex ⇒ unimodal (x*=0 aralıkta). b) 4.25·(½)ᵏ<10⁻⁴ ⇒ **k=16**. c) 4.25·(0.618)ᵏ<10⁻⁴ ⇒ **k=23** |
| Q3 | 40 | **Formülasyon + optimizasyon** (EOQ benzeri): günde D ton çöp, bekleme maliyeti h TL/ton-gün, kamyon K TL; günde kaç kamyon? | Q=DT; ATC(Q)=KD/Q+½hQ; ATC′=0 ⇒ **Q\*=√(2KD/h)**; günde ⌈D/Q\*⌉ kamyon |

**Çıkarımlar (güncellenmiş tahmin):**
- Q1 **convex set / polyhedron / extreme point-direction / Minkowski gösterimi** olabilir (2022 MT'de de aynı P çıkmış: aynı küme!). Convex/concave Hessian sorusu da çok muhtemel (hoca "convex/concave analizi" dedi) — ikisine de hazırlan.
- Q2 **unimodality gösterme + iterasyon sayısı formülü** (bisection: ln(ε/(b−a))/ln ½, golden: ln(ε/(b−a))/ln 0.618; hep yukarı yuvarla). Formüller tablolu tur hesaplamasından daha kısa — hızlıca yap.
- Q3 "genel": **kelime problemi → matematiksel model → türev ile çöz** (EOQ/envanter tipi). Hoca "bi şey soracağım" dedi: modelleme + tek değişkenli optimizasyon (f′=0, f″>0 kontrolü) en olası.
- Süre kısa (50 dk): ispat uzatma, formüle odaklan.

> ⚠ `IE440 ÇIkmışlar/` içindeki diğer sınavlar **Kuban Altınel**'e ait (Fall 2014–2024). Bu dönemin hocası **Necati Aras** → soru stili farklı olabilir. Çıkmışlar konu havuzu olarak değerlendirilmeli; sorular birebir gelmez.
> Midterm çıkmışlarında one-direction search yok (midterm konuları unconstrained/KKT), **ama 2013 Quiz 1'de var** (iterasyon sayısı). Q2 için ders notlarındaki tahta örnekleri + 2013 quiz tipi hesaplar.

---

## A. Çıkmışlardan konu havuzu (Q1 + Q3 için)

| Sınav | Soru | Konu | Quiz 1 ilgisi |
|---|---|---|---|
| **Quiz 2013 Q1** | P polyhedron: extreme pts/dirs, (3,2) gösterimi, Minkowski | Polyhedral set | **Çok yüksek** |
| **Quiz 2013 Q2** | min x²+1 [−2.5,1.75]: unimodal, bisection/golden iterasyon sayısı | One-direction | **Çok yüksek** |
| **Quiz 2013 Q3** | Çöp/kamyon (EOQ) formülasyonu, Q*=√(2KD/h) | Modelleme + 1D opt. | **Çok yüksek** |
| MT 2016 Q1 | Küme polyhedron mu? (cos θ kısıtları, x²−8x+15≤0, ∅) | Convex set / polyhedron | **Yüksek (Q3)** |
| MT 2016 Q2 | f=−x₁²−3x₂²−2x₃²+4x₁x₂+2x₁x₃+4x₂x₃ convex/concave? + stationary points | Hessian, LPM | **Çok yüksek (Q1)** |
| MT 2022 Q2 | Q=[[0,1,1],[1,0,1],[1,1,0]] PD/ND/indefinite; x₁+x₂+x₃=0 üzerinde | Definiteness, subspace | **Çok yüksek (Q1)** |
| MT 2022 Q1 | −log(−log Σexp(aᵢᵀx+bᵢ)) convex | Convex ispat (kompozisyon) | Orta (zor) |
| MT 2022 Q3 | P={…} extreme points & extreme directions, bir noktayı gösterme | Convex set / polyhedral | **Yüksek (Q3)** |
| MT 2023 Q2 | Convex fonksiyonlar kümesi bir convex cone | Convex ispat | **Yüksek (Q1/Q3)** |
| MT 2023 Q1 | Eigenvalue/eigenvector 3×3 | Lineer cebir | Orta |
| MT 2024 Q1 | Affinely independent ⇒ aᵢ−a₁ lineer bağımsız | Convex set teori | Orta |
| MT 2024 Q3 | MINLP: feasible set, convex hull, extreme points/directions | Convex hull | Orta |
| MT 2024 Q4 | f=½(αx₁²+βx₂²)−αx₁x₂+βx₁−αx₂, α,β durumları | Hessian, PM | **Yüksek (Q1)** |
| MT 2014 Q1 | f′=f″=0, f‴≠0 iken Newton lineer yakınsar, oran ½ | One-direction, convergence | **Yüksek (Q2/Q3)** |
| MT 2024-2 Q1 | xₖ₊₁=axₖ, yₖ₊₁=yₖᵇ: yakınsama, mertebe, iterasyon sayısı | Convergence order | **Yüksek (Q3)** |
| Final 2021 Q3 | log Σeˣⁱ convex | Convex ispat | Orta |
| Final 2023 Q2 | (Σxᵢᵖ)^{1/p}, p<1 concave | Convex ispat | Düşük |
| MT 2022/2014 Q4-V | Steepest descent exact line search ⇒ ardışık adımlar dik; Newton/SD adımı | Unconstrained | Düşük (Quiz 2) |
| MT 2014/2024 | Kutu-küre (xyz max s.t. x²+y²+z²≤d²) formülasyonu | Formülasyon | Orta (Q3) |

**Öncelik sırası (2013 quiz ışığında güncellendi):**
1. **Iterasyon sayısı formülleri** (bisection/golden/dichotomous) + unimodality gösterme (f″>0 ⇒ strictly convex ⇒ unimodal) — Q2.
2. **Polyhedron: extreme point/direction, convex+nonneg kombinasyon, Minkowski** — Q1 olası.
3. Hessian + principal minors ile convex/concave/indefinite bölgesi bulma — hoca "convex concave analizi" dedi.
4. **Kelime problemi formülasyonu + f′=0** (EOQ, portfolio, kutu-küre) — Q3 olası.
5. Iterasyon tabloları (dichotomous/golden/Newton), yakınsama mertebesi, convexity ispatı.

---

## B. Formül kartı

### Convexity
- Convex f: f(λx₁+(1−λ)x₂) ≤ λf(x₁)+(1−λ)f(x₂); gradient: f(y) ≥ f(x)+∇f(x)ᵀ(y−x); Hessian PSD ∀x.
- Convex ⇔ epigraph convex. Concave ⇔ hypograph convex.
- Convex ⇒ quasiconvex (tersi değil). Quasiconvex: f(λx₁+(1−λ)x₂) ≤ max{f(x₁),f(x₂)}.
- **Convex fonksiyonlar için kapalılık:** α·f (α≥0), f+g, max{f,g}, f(Ax+b) convex; h convex ve azalmayan, g convex ⇒ h(g) convex; h convex ve azalan, g concave ⇒ h(g) convex.
- x² convex; eˣ convex; −ln x convex (x>0); 1/x convex (x>0); x³ sadece x≥0'da convex; |x| convex.

### Definiteness (A simetrik n×n)
| Sonuç | Test |
|---|---|
| PD | tüm LPM > 0 |
| PSD | **tüm** principal minor ≥ 0 (LPM yetmez!) |
| ND | LPMₖ işareti (−1)ᵏ (−, +, −, …) |
| NSD | k. mertebe tüm principal minor'lar (−1)ᵏ·(≥0) |
| Indefinite | PSD ve NSD değil; veya eigenvalue'lar farklı işaretli |
- 2×2 [[a,b],[b,c]]: PD ⇔ a>0, ac−b²>0. PSD ⇔ a≥0, c≥0, ac−b²≥0.
- Eigenvalue testi: hepsi >0 PD, ≥0 PSD, <0 ND, karışık indefinite.
- Alt uzayda (xᵀQx, Ax=0) test: kısıtı yerine koy (2022 Q2b).

### One-direction search
- IoU kısalması: **bisection** (½)ⁿ(b−a); **dichotomous** (b−a)/2ⁿ + Δ(1−1/2ⁿ) (n iterasyon, 2n değerlendirme); **golden** rᵏ(b−a), r=0.618 (k+1 değerlendirme).
- Dichotomous: x₁,₂ = (a+b)/2 ∓ Δ/2. Golden: x₁=b−r(b−a), x₂=a+r(b−a); sonra bir nokta yeniden kullanılır.
- **Max** problemi: f(x₁)>f(x₂) ⇒ sağı at ([a,x₂]); f(x₂)>f(x₁) ⇒ solu at ([x₁,b]). **Min** için ters.
- Bisection (türevli, min): f′(x_k)>0 ⇒ b=x_k; f′<0 ⇒ a=x_k.
- Newton (min): x⁺ = x − f′/f″ (f″>0 gerekli); kök: x⁺ = x − f/f′.
- Yakınsama: lim|eₖ₊₁|/|eₖ|ᵖ = c. p=1 lineer (c<1), p=2 kuadratik. Newton: kuadratik (f″(x*)≠0); f′=f″=0, f‴≠0 ⇒ lineer, c=½.

---

## C. Pratik sorular (çözümlü) — `Quiz1_Soru_Cozum.md`
Tüm çözümler ayrı dosyada: **`Quiz1_Soru_Cozum.md`** — başta **2013 Quiz 1'in tam çözümü + varyantları**, sonra Q1/Q2/Q3 tipi pratik sorular.

## D. Çalışma planı (öneri)
0. (45 dk, **zamanlı**) `2013 quiz 1.pdf` soru kısmını çöz (50 dk), sonra çözümle karşılaştır.
1. (30 dk) `Ders_Notlari_Ozet.md` §3.5–3.6 + bu dosyada formül kartı — LPM/PM tablosunu ezberle.
2. (45 dk) `Quiz1_Soru_Cozum.md` Q1 tipi soruları kağıtta çöz, sonra çözüme bak.
3. (30 dk) Q2 tipi: dichotomous/golden tablolarını elle yeniden üret (hesap makinesiyle), iterasyon sayısı formülleri.
4. (30 dk) Q3 tipi: polyhedron/extreme point, yakınsama mertebesi, bir convexity ispatı.
5. Çıkmışlar: `16 mt + sol.pdf` Q2, `22 mt` Q2–Q3, `24 mt` Q4, `24 mt2` Q1 (zamanlı).
