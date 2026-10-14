# IE 440 — Quiz 1 Pratik Sorular ve Çözümleri

Önce kağıtta çöz, sonra çözüme bak. Numaralar hesapla doğrulanmıştır (Python). Soruların bir kısmı çıkmışlardan (Altınel) uyarlanmıştır: [MT yıl] etiketi.

---

# ★ Gerçek Quiz 1 (2013) — Tam Çözüm ve Varyantlar

Soru metni: `IE440 ÇIkmışlar/2013 quiz 1.pdf` (Altınel, 50 dk). Aşağıdaki çözümler resmi çözümle uyumludur.

### G1 (30 p) P = {x∈E²: 3x₁−7x₂≥−6, 5x₁−x₂≥−4, x₁≥0, x₂≥2}
**a) Extreme point / direction.** Sınırlar: (i) 3x₁−7x₂=−6, (ii) 5x₁−x₂=−4, (iii) x₁=0, (iv) x₂=2.
- (iv)∩(i): x₂=2 ⇒ x₁=8/3. Diğer kısıtlar: 5·8/3−2=11.3≥−4 ✓, x₁≥0 ✓ ⇒ **(8/3, 2) köşe**.
- x₁=0 köşesi: (0,2)'de 3·0−14=−14<−6 ✗ infeasible. (ii) fizibıl bölgeyi kesmiyor. ⇒ **tek extreme point**.
- Recession cone: 3d₁−7d₂≥0, 5d₁−d₂≥0, d₁≥0, d₂≥0 ⇒ 0≤d₂≤3d₁/7. Extreme directions: d₂=0 ⇒ **d₁=(1,0)**; d₂=3d₁/7 ⇒ **d₂=(7,3)** (≡(1,3/7), yön ölçeği önemsiz).

**b) (3,2)ᵀ gösterimi.** (3,2) = λ(8/3,2) + μ₁(1,0) + μ₂(7,3), **λ=1** (tek extreme point ⇒ λ=1), μ≥0.
2. satır: 2 + 3μ₂ = 2 ⇒ μ₂=0; 1. satır: 8/3+μ₁=3 ⇒ **μ₁=1/3**.

**c) Minkowski (resolution) teoremi:** polyhedron = (extreme point'lerin convex kombinasyonu) + (extreme direction'ların nonneg. kombinasyonu):
P = { x : x = λ(8/3,2)ᵀ + μ₁(1,0)ᵀ + μ₂(7,3)ᵀ, λ=1, μ₁,μ₂ ≥ 0 }
= { x : x₁ = (8/3)λ + μ₁ + 7μ₂, x₂ = 2λ + 3μ₂, λ=1, μ₁,μ₂ ≥ 0 }.

### G2 (30 p) min x²+1, s.t. −2.5 ≤ x ≤ 1.75
**a) Unimodal.** f″(x)=2>0 ∀x ⇒ strictly convex ⇒ unimodal. f′=2x=0 ⇒ x*=0 ∈ [−2.5,1.75] (tek global min). (Doğrudan tanımdan: x*=0'ın solunda azalan, sağında artan.)
**b) Bisection, ε=10⁻⁴.** Uzunluk 4.25·(½)ᵏ < 10⁻⁴ ⇒ k > ln(42500)/ln 2 = 15.37 ⇒ **k=16**.
**c) Golden section, ε=10⁻⁴.** 4.25·(0.618)ᵏ < 10⁻⁴ ⇒ k > ln(42500)/(−ln 0.618) = 22.14 ⇒ **k=23**.
Genel formül: k = ⌈ ln(ε/(b−a)) / ln(oran) ⌉, oran = 0.5 (bisection) veya 0.618 (golden). Hep yukarı yuvarla.

**Varyant 1:** min (x−1)⁴, [−3,5], ε=0.001. Unimodal? f″=12(x−1)²≥0 ⇒ convex ⇒ unimodal (strictly convex da: x≠1'de f″>0, tek min x=1). Uzunluk 8: bisection 8·½ᵏ<0.001 ⇒ k>12.97 ⇒ **13**; golden 8·0.618ᵏ<0.001 ⇒ k>18.68 ⇒ **19**.
**Varyant 2 (unimodal ama convex değil):** f(x)=√|x| aralık [−1,4] — tek vadi (x=0) ⇒ unimodal, f″ işareti convex olmadığını gösterir (x>0: f″<0). "Convex ⇒ unimodal, tersi değil".
**Varyant 3 (not unimodal):** f(x)=x³−3x, [−2,2] ⇒ tepe x=−1 ve vadi x=1 ⇒ unimodal değil, search yöntemleri garanti vermez.

### G3 (40 p) Çöp/kamyon (EOQ tipi)
Günde D ton çöp birikir, bir ton çöpün bir gün beklemesi h TL, kamyon göndermek K TL. Günde kaç kamyon?
- Q = kamyon gelmeden biriken çöp, T = periyot (gün) ⇒ Q = DT.
- Kamyon maliyeti/gün: K/T = KD/Q. Bekletme maliyeti/gün: h∫₀ᵀ Dt dt / T = ½hDT = **½hQ**.
- **ATC(Q) = KD/Q + ½hQ**, Q>0. ATC′(Q) = −KD/Q² + h/2 = 0 ⇒ **Q\* = √(2KD/h)**.
- ATC″(Q) = 2KD/Q³ > 0 ⇒ strictly convex ⇒ Q\* global min (konveks olduğunu mutlaka yaz).
- Günlük kamyon sayısı = D/Q\* = √(hD/(2K)) (sürekli); tamsayı için ⌈D/Q\*⌉ (resmi çözüm). Daha doğrusu n=⌊·⌋ ve ⌈·⌉ için ATC(n)=Kn+hD/(2n) karşılaştır.
- **Sayısal örnek:** D=100, K=20, h=1 ⇒ Q\*=√4000=63.2, D/Q\*=1.58. n=1: 20+50=70; n=2: 40+25=65; n=3: 60+16.7=76.7 ⇒ **günde 2 kamyon**.
- **Varyant:** her ton için günlük bekleme yerine kamyon başına kapasite C sınırı (Q≤C): Q\*=min(√(2KD/h), C) (convex olduğu için kısıta değiyorsa Q=C).

---

# Q1 Tipi — Convex / Concave Analizi

### S1.1 [MT 2022 Q2] Q = [[0,1,1],[1,0,1],[1,1,0]]
a) PD / ND / indefinite? b) S = {x : x₁+x₂+x₃ = 0} üzerinde?

**Çözüm.** a) 1. mertebe principal minor'lar = 0; 2. mertebe = 0·0−1 = **−1** (üç tane); det Q = 2. 2. mertebe PM < 0 ⇒ ne PSD ne NSD ⇒ **indefinite**. (Eigenvalue'lar: −1, −1, 2.)
b) xᵀQx = 2(x₁x₂+x₁x₃+x₂x₃) = (x₁+x₂+x₃)² − (x₁²+x₂²+x₃²) = −‖x‖² < 0 (x≠0, S üzerinde) ⇒ S üzerinde **negative definite**.

### S1.2 [MT 2016 Q2] f(x) = −x₁² − 3x₂² − 2x₃² + 4x₁x₂ + 2x₁x₃ + 4x₂x₃. Convex, concave, neither?
**Çözüm.** H = [[−2,4,2],[4,−6,4],[2,4,−4]] (sabit). LPM: −2, (12−16)=**−4**, det=**136**.
- PD değil (LPM₁<0). ND için LPM₂ > 0 gerekirdi, −4 → ND değil.
- 1. mertebe PM'lerden −2<0 ⇒ PSD değil; 2. mertebe PM (1,2) = −4 < 0 ⇒ NSD değil (NSD'de ≥0 olmalı).
- Eigenvalue'lar ≈ −9.75, −5.03, **+2.78** → karışık. ⇒ **indefinite ⇒ ne convex ne concave.**
- ∇f=0 ⇒ tek stationary nokta (0,0,0), **saddle**.

### S1.3 [Defter alıştırması] f(x₁,x₂) = x₁³(x₁−4) + 3(x₂−5)² + 10 hangi bölgede convex/concave?
**Çözüm.** f = x₁⁴ − 4x₁³ + 3(x₂−5)² + 10. ∂²f/∂x₁² = 12x₁² − 24x₁ = 12x₁(x₁−2), ∂²f/∂x₂² = 6, çapraz 0.
H = diag(12x₁(x₁−2), 6). PM'ler: 12x₁(x₁−2), 6, 72x₁(x₁−2).
- **PSD ⇔ x₁(x₁−2) ≥ 0 ⇔ x₁ ∈ (−∞,0] ∪ [2,∞)** → bu bölgelerin **her birinde** convex (birleşimi konveks küme değil, yani "convex on (−∞,0]×ℝ" ve "convex on [2,∞)×ℝ" ayrı ayrı).
- 0<x₁<2'de: 1. PM <0 ama 2. PM (6) >0 ⇒ indefinite. Hiçbir yerde concave değil (6>0).
- Strict convex: x₁<0 veya x₁>2'de PD.

### S1.4 [MT 2024 Q4] f = ½(αx₁²+βx₂²) − αx₁x₂ + βx₁ − αx₂, α,β>0. Convex mi? Minimum?
**Çözüm.** H = [[α, −α],[−α, β]]; PM: α, β, αβ−α² = α(β−α).
- **α<β:** LPM>0 ⇒ PD ⇒ strictly convex, stationary nokta **x* = (−(α+β)/α, −1)** tek global min.
- **α=β:** PSD (PM ≥0, 2. PM=0) ⇒ convex ama strictly değil; ∇f=0 iki denklem de x₂=x₁+1 olur ⇒ **doğru üzerindeki her nokta global min** (tek çözüm yok, H singüler).
- **α>β:** 2. PM<0 ⇒ **indefinite** ⇒ stationary nokta saddle, min yok.
- α=0, β>0: f = ½βx₂² + βx₁ → x₁→−∞ ile f→−∞ ⇒ **minimize edilemez**.

### S1.5 f(x₁,x₂) = x₁² + x₂³ — nerede convex?
**Çözüm.** H = diag(2, 6x₂) → PSD ⇔ x₂ ≥ 0. Domain S = ℝ×[0,∞) konveks ve orada convex; ℝ² üzerinde değil. (x₂>0: PD ⇒ strictly convex.)

### S1.6 f(x) = x₁²+2x₂²+3x₃²−2x₁x₂ — convex mi, strictly?
**Çözüm.** H = [[2,−2,0],[−2,4,0],[0,0,6]]; LPM: 2, 4, 24 > 0 ⇒ **PD ⇒ strictly convex**. Eigenvalue'lar ≈ 0.76, 5.24, 6.

### S1.7 [MT 2023 Q3'ten] f(x₁,x₂) = 1/(x₁²+x₂²+2)
H = 2/(x₁²+x₂²+2)³ · [[3x₁²−x₂²−2, −4x₁x₂],[−4x₁x₂, 3x₂²−x₁²−2]]. (0,0): H = −½·I ⇒ ND; (4,0): diag(+,−) ⇒ indefinite. **Ne convex ne concave** (sadece 0 civarında locally concave).

### S1.8 [MT 2023 Q2] Convex fonksiyonların kümesi bir convex cone'dur — ispatla.
**Çözüm.** f,g convex, α,β ≥ 0. h = αf+βg:
h(λx₁+(1−λ)x₂) = αf(λx₁+(1−λ)x₂)+βg(⋯) ≤ α[λf(x₁)+(1−λ)f(x₂)] + β[λg(x₁)+(1−λ)g(x₂)] = λh(x₁)+(1−λ)h(x₂).
Yani negatif olmayan lineer kombinasyon convex ⇒ küme cone (α·f) ve toplama altında kapalı (convex cone). ∎ (α<0 olsaydı bozulur; cone "convex" olduğu toplama ile.)

### S1.9 Tanımdan ispat: f(x)=x² convex (strictly)
λx₁²+(1−λ)x₂² − (λx₁+(1−λ)x₂)² = λ(1−λ)(x₁−x₂)² ≥ 0, x₁≠x₂, 0<λ<1 için >0 ⇒ strictly convex. (Tahtada yapılan ispat.)

### S1.10 Quasiconvexity
a) x³ ℝ'de: monoton ⇒ f(λx₁+(1−λ)x₂) ≤ max{f(x₁),f(x₂)} ✓ **quasiconvex** (aynı zamanda quasiconcave), ama convex değil (f″=6x<0, x<0).
b) −x²: alt seviye kümesi {x: −x² ≤ α} = (−∞,−√(−α)] ∪ [√(−α),∞) (α<0) **konveks değil** ⇒ quasiconvex değil (concave ve quasiconcave).
c) Her convex fonksiyon quasiconvex: f(λx₁+(1−λ)x₂) ≤ λf(x₁)+(1−λ)f(x₂) ≤ max{f(x₁),f(x₂)}. Tersi yanlış (a).

---

# Q2 Tipi — One-Direction Search

Ortak örnek (tahta): **max f(x)**, f(x)=3x (0≤x≤2), f(x)=(−x+20)/3 (2≤x≤3); [0,3]. Gerçek maksimum x*=2, f=6.

### S2.1 Dichotomous (Δ=0.1), 4 iterasyon
| k | IoU başı | x₁ | f(x₁) | x₂ | f(x₂) | Karar | Yeni IoU | Uzunluk |
|---|---|---|---|---|---|---|---|---|
| 1 | (0,3) | 1.45 | 4.35 | 1.55 | 4.65 | f(x₂)>f(x₁) | (1.45,3) | 1.55 |
| 2 | (1.45,3) | 2.175 | 5.942 | 2.275 | 5.908 | f(x₁)>f(x₂) | (1.45,2.275) | 0.825 |
| 3 | (1.45,2.275) | 1.8125 | 5.4375 | 1.9125 | 5.7375 | f(x₂)>f(x₁) | (1.8125,2.275) | 0.4625 |
| 4 | (1.8125,2.275) | 1.9937 | 5.9812 | 2.0937 | 5.9688 | f(x₁)>f(x₂) | (1.8125,2.0937) | 0.2812 |

Uzunluk formülü: Lₙ = (b−a)/2ⁿ + Δ(1−2⁻ⁿ) (n=1: 1.55 ✓, n=2: 0.825 ✓). Her iterasyon 2 f-hesabı. (Tahtadaki 5.842 → doğrusu 5.942.)

### S2.2 Golden section (r=0.618), 6 iterasyon
| k | [a,b] | x₁ | f(x₁) | x₂ | f(x₂) | Karar → yeni IoU |
|---|---|---|---|---|---|---|
| 1 | [0,3] | 1.1459 | 3.4377 | 1.8541 | 5.5623 | f(x₁)<f(x₂) → [1.1459,3] |
| 2 | [1.1459,3] | 1.8541* | 5.5623 | 2.2918 | 5.9027 | f(x₁)<f(x₂) → [1.8541,3] |
| 3 | [1.8541,3] | 2.2918* | 5.9027 | 2.5623 | 5.8126 | f(x₁)>f(x₂) → [1.8541,2.5623] |
| 4 | [1.8541,2.5623] | 2.1246 | 5.9585 | 2.2918* | 5.9027 | f(x₁)>f(x₂) → [1.8541,2.2918] |
| 5 | [1.8541,2.2918] | 2.0213 | 5.9929 | 2.1246* | 5.9585 | f(x₁)>f(x₂) → [1.8541,2.1246] |
| 6 | [1.8541,2.1246] | 1.9574 | 5.8723 | 2.0213* | 5.9929 | f(x₁)<f(x₂) → [1.9574,2.1246] |

\* önceki iterasyondan **yeniden kullanılan** nokta (yeni hesap yok). IoU uzunlukları: 3, 1.854, 1.146, 0.708, 0.438, 0.271 = 3·rᵏ⁻¹.

### S2.3 Kaç iterasyon? (b−a)=4, ε=0.01
- Bisection: 4/2ⁿ < 0.01 ⇒ 2ⁿ>400 ⇒ **n=9** (4/512=0.0078).
- Golden: 4rᵏ < 0.01 ⇒ k > ln(0.0025)/ln(0.618) = 12.45 ⇒ **k=13**.
- Dichotomous (Δ<ε): (b−a)/2ⁿ+Δ(1−2⁻ⁿ) < ε.
- Karşılaştırma: bisection türev ister (iterasyon başı 1 f′), golden 1 f-hesabı/iterasyon, dichotomous 2.

### S2.4 Bisection (türevli): min f(x)=eˣ−2x, [0,2]; f′=eˣ−2
| k | [a,b] | x_k | f′(x_k) | Karar |
|---|---|---|---|---|
| 1 | [0,2] | 1.0 | 0.718 | >0 → b=x |
| 2 | [0,1] | 0.5 | −0.351 | <0 → a=x |
| 3 | [0.5,1] | 0.75 | 0.117 | b=x |
| 4 | [0.5,0.75] | 0.625 | −0.132 | a=x |
| 5 | [0.625,0.75] | 0.6875 | −0.011 | a=x |
| 6 | [0.6875,0.75] | 0.71875 | 0.052 | b=x |
| 7 | [0.6875,0.71875] | 0.703125 | 0.020 | b=x |
Gerçek x*=ln 2=0.6931 ∈ [0.6875,0.703125] ✓. Aralık her adım yarıya iner.

### S2.5 Newton: aynı problem x₀=1
x₊ = x − (eˣ−2)/eˣ: 1 → 0.73576 → 0.69404 → 0.693148 → 0.69314718 … (hata 0.307→0.042→0.0010→1e-6): **kuadratik yakınsama**.
**Newton'un başarısız olması:** f(x)=4x³−3x⁴, x₀=0.6: f′=1.728, f″=1.44 ⇒ x₁=−0.6 (tahtada x<0 için aynalanmış ifadeyle x₂=+0.6: **döngü**). x₀=0.9 ile başlarsan x=1'e gider ama f″(1)=−12<0 → bu bir **maksimum**; Newton sadece f′=0 bulur. ⇒ min için f″>0 koşulunu kontrol et.

### S2.6 Unimodal mı?
a) f(x)=x³−3x, [−2,2]: tepe x=−1, vadi x=1 ⇒ **unimodal değil**. [−1,2]'de: x=1'de tek vadi (sol uç tepe değil, sınır) ⇒ unimodal.
b) f(x)=|x−1|: tek vadi ⇒ unimodal (strictly). f(x)=(x−1)²: strictly unimodal.
c) Her convex fonksiyon (aralıkta) unimodaldır; tersi değil (ör. √|x| vadi: unimodal, convex değil).

---

# Q3 Tipi — Genel

### S3.1 [MT 2016 Q1] Polyhedron mu?
a) S₁={x∈ℝ²: x₁cosθ+x₂sinθ≤1 ∀θ∈[0,π/2], 2x₁+2x₂≥1, x≥0} → birim çemberin 1. bölge parçası ∩ polytop; **polyhedron değil** (sonsuz sayıda kısıt, sınırda sonsuz extreme point; polyhedron'un sonlu sayıda vertex'i vardır). Konveks ama polyhedron değil.
b) x²−8x+15≤0 ⇔ (x−3)(x−5)≤0 ⇔ [3,5] → **polyhedron**.
c) ∅ = {x≤0}∩{x≥1} → **polyhedron**.

### S3.2 [MT 2022 Q3] P={3x₁−7x₂≥−6, 5x₁−x₂≥−4, x₁≥0, x₂≥2}
a) Extreme points / directions. b) (3,2)ᵀ'yi göster.
**Çözüm.** Tek köşe: x₂=2 ∩ 3x₁−7x₂=−6 ⇒ **(8/3, 2)**. (x₁=0 köşesi infeasible: 3·0−14=−14<−6.) Recession direction d: 3d₁−7d₂≥0, 5d₁−d₂≥0, d₁,d₂≥0 ⇒ extreme directions **(1,0)** ve **(1,3/7)**.
b) (3,2) = 1·(8/3,2) + (1/3)(1,0) + 0·(1,3/7): λ=1, μ₁=1/3, μ₂=0 ✓.

### S3.3 [MT 2024-2 Q1] xₖ₊₁=a xₖ (0<a<1), yₖ₊₁=yₖᵇ (b>1, |y₀|<1)
- xₖ=aᵏx₀→0 (a<1). yₖ=|y₀|^{bᵏ}→0 (|y₀|<1, bᵏ→∞).
- Mertebe: |xₖ₊₁|/|xₖ|=a ⇒ **p=1, lineer, oran a**. |yₖ₊₁|/|yₖ|ᵇ=1 ⇒ **p=b** (b=2 kuadratik).
- |xₖ|≤c|x₀| ⇔ aᵏ≤c ⇔ **k ≥ ln c/ln a** (tavan al).
- |yₖ|≤c|y₀| ⇔ |y₀|^{bᵏ−1}≤c ⇔ bᵏ ≥ 1+ln c/ln|y₀| ⇔ **k ≥ log_b(1+ln c/ln|y₀|)**.

### S3.4 [MT 2014 Q1] Newton 1D, f′(x*)=f″(x*)=0, f‴(x*)≠0 ⇒ lineer, oran ½
Taylor ile f′(x*)=f″(x*)=0 yazıp x*−x_{k+1} = ½(x*−x_k) çıkar ⇒ |e_{k+1}|/|e_k| → ½.
Örnek: f(x)=x³, x*=0: x₊ = x − 3x²/(6x) = x/2 ✓.

### S3.5 Formülasyon: Portfolio (tahta örneği)
x_i = hisse i'e yatırılan $. Σ = kovaryans matrisi (köşegen: 0.2, 0.08, 0.18; kovaryanslar Excel'den), μ=(0.14,0.11,0.10).
**min xᵀΣx s.t. μᵀx ≥ R, x₁+x₂+x₃=1000, x≥0** (veya **max μᵀx s.t. xᵀΣx ≤ riskmax**, x₁+x₂+x₃=1000).
Σ PSD ⇒ birinci model **convex QP** (ikincisi de convex programming: convex kısıt). Birim yatırım (x/1000) ile ağırlık formu da kullanılabilir.

### S3.6 [MT 2014/2024] Kutu–küre: küre içindeki en büyük hacimli kutu
x,y,z kenarlar, küre çapı d: **max xyz s.t. x²+y²+z²≤d²/4, x,y,z≥0.** (Hedef concave değil; ln x+ln y+ln z concave ve monoton olduğundan max ln xyz eşdeğer bir **convex program**.) Çözüm: x=y=z=d/(2√3) (küp).

### S3.7 Convex küme kontrolleri (tahta)
- {(x,y): (x−3)²+(y−2)²≤4} convex (diskte g(x)=(x−3)²+(y−2)²−4 convex fonksiyon, alt seviye kümesi).
- {x²+y²=4} convex değil (çemberdeki iki noktayı birleştiren kiriş içeride).
- {x : Ax ≤ b}, {x : Ax=b}: polyhedron ⇒ convex.
- Convex kümelerin kesişimi convex, birleşimi genelde değil (tahtadaki "x≥0 **veya** y≥0" bölgesi bu yüzden nonconvex).

---

## Zaman yönetimi önerisi (45 dk, 3 soru)
Q1 (convex/concave) ~20 dk — Hessian'ı yaz, **önce LPM'lerle ND/PD dene, olmazsa tüm principal minor'lar**; Q2 ~15 dk — tabloyu net çiz (x₁,x₂,f değerleri, hangi aralık atıldı); Q3 ~10 dk.
Sık hata: PSD için sadece LPM bakmak; max/min karıştırıp yanlış taraftan aralık atmak; golden section'da reuse edilen noktayı yanlış hesaplamak.
