# IE 440 — Ders Notları Özeti (Hafta 1–4)

Kaynak: `Ders Notları Foto/` içindeki tahta ve defter fotoğrafları (konu klasörleri: `01_…`, `02_…`, `03_…`).
Hoca: Necati Aras. Syllabus haftaları: Intro NLP → One Direction → Convexity (Quiz 1, hafta 4).

> Notasyon: ✎ = fotoğraftan okunamayan / emin olmadığım yer. Foto yolları `Ders Notları Foto/` altındadır.

---

## 1. Intro to Nonlinear Programming (`01_Intro_NLP_ve_Formulasyon`)

### 1.1 Portfolio örneği (`01_portfolio_ornegi`)
- Bütçe: $1000, 3 hisse. E[S₁]=0.14, E[S₂]=0.11, E[S₃]=0.10; Var(S₁)=0.2, Var(S₂)=0.08, Var(S₃)=0.18.
- İki eşdeğer bakış: **max beklenen getiri s.t. risk ≤ …** veya **min risk s.t. beklenen getiri ≥ hedef** (tahtada "≥120" yazılıp çizilmiş).
- Risk = portföy varyansı = xᵀΣx (kovaryanslar Excel'de, `cor(S1,S2)` vs.; fotoda görünmüyor ✎). Moodle: `portfolio-optimization.pdf`, `Portfolio Optimization.xlsx`.
- Genel model: min xᵀΣx s.t. μᵀx ≥ R, Σxᵢ = 1000, x ≥ 0 → **konveks QP** (Σ PSD).

### 1.2 Kısıtlı problemler, grafik çözüm
| Problem | Çözüm |
|---|---|
| min (x−1)²+(y−1)² s.t. x+y≤4, x,y≥0 | Hedef konturları (1,1) merkezli çemberler, (1,1) fizibıl → optimum x=1,y=1 |
| min (x+2)²+(y+1)² s.t. x²+y²≤9, **x≥0 veya y≥0** | Fizibıl bölge **konveks değil** (çemberin iki parçasının birleşimi). Global optimum (−2,0) |
| aynı problem | (0,−1) **lokal optimum**: z=4, komşu fizibıl noktalar (0,−1±ε), (0+ε,−1) hepsi z ≥ 4 |

**Local optimum tanımı:** x* için, ε-komşuluğundaki tüm fizibıl x'lerde f(x*) ≤ f(x) (min için). Global ≠ lokal; konveks olmayan fizibıl kümede lokal optimum global olmayabilir.

---

## 2. Nonlinear Optimization in One Direction (`02_One_Direction_Search`)

### 2.1 Unimodal fonksiyon
Bir aralıkta **en fazla bir tepe (peak) veya vadi (valley)** varsa unimodal.
C ⊂ ℝ aralığında f, **(strictly) unimodal** ⇔ f'nin minimumunu aldığı x* ∈ C var ve ∀ x′<x″ ∈ C:
- x″ ≤ x* ⇒ f(x′) ≥ f(x″)  (strictly: >)
- x* ≤ x′ ⇒ f(x″) ≥ f(x′)  (strictly: >)

Yani x*'ın solunda azalan, sağında artan. (Tahtada a–b arası vadi ve tepe çizimi.)

### 2.2 Derivative-free yöntemler (`02_interval_of_uncertainty` … `05_golden_section_defter`)
**Interval of Uncertainty (IoU):** [a,b]. Orta nokta (a+b)/2 etrafında iki nokta (maksimizasyon çizilmiş):
- x₁ = (a+b)/2 − Δ/2, x₂ = (a+b)/2 + Δ/2
- Case 1: f(x₁) > f(x₂) ⇒ yeni IoU = (a, x₂)
- Case 2: f(x₂) > f(x₁) ⇒ yeni IoU = (x₁, b)
- Case 3: f(x₁) = f(x₂) ⇒ yeni IoU = (x₁, x₂)
- Durma: |IoU| < ε.

**Dichotomous search örneği** (`03_dichotomous_ornek`): max f(x) = 3x (0≤x≤2), (−x+20)/3 (2≤x≤3); Δ=0.1, I₀=(0,3)
- Iter 1: x₁=1.45 (f=4.35), x₂=1.55 (f=4.65); f(x₂)>f(x₁) ⇒ x_L=1.45, I₁=(1.45, 3)
- Iter 2: x₁=2.175, x₂=2.275 (f=5.908); f(x₁)>f(x₂) ⇒ x_R=2.275, I₂=(1.45, 2.275)
- ⚠ Tahtada f(x₁)=5.842 yazıyor; doğrusu (−2.175+20)/3 = **5.942**. Karar değişmiyor.
- Her iterasyonda 2 yeni fonksiyon değerlendirmesi.

**Golden Section Search** (`04_golden_section_tahta`, `05_golden_section_defter`):
- Golden ratio r = (√5 − 1)/2 ≈ 0.618; r² = 1 − r ⇔ 1/r = r/(1−r).
- x₁ = b − r(b−a), x₂ = a + r(b−a); (a,x₂) uzunluğu = r(b−a); (x₁,b) uzunluğu = r(b−a).
- Maksimizasyon için: Case 1: f(x₁) < f(x₂) ⇒ IoU = [x₁, b]; Case 2: f(x₁) > f(x₂) ⇒ IoU = [a, x₂]; Case 3: eşit ⇒ ikisinden biri.
- **Nokta yeniden kullanımı:** Case 1'de yeni x₃ = b − r(b − x₁) = a + r(b−a) = **eski x₂** ("new x₃ becomes x₂") ⇒ iterasyon başına **1** yeni değerlendirme.
- k iterasyon sonra IoU uzunluğu = rᵏ (b−a).

### 2.3 Derivative-based yöntemler (`06_…`, `07_bisection_defter`)
**Bisection (türev tabanlı):** I₀=[a₁,b₁], x_k = (a_k+b_k)/2.
- f′(x_k) = 0 ⇒ dur, x_k optimal.
- f′(x_k) > 0 ⇒ a_{k+1}=a_k, b_{k+1}=x_k (minimum solda)
- f′(x_k) < 0 ⇒ a_{k+1}=x_k, b_{k+1}=b_k
- Durma: (½)ⁿ(b₁−a₁) < ε. Örnek (tahta): (b−a)=4, ε=0.01 ⇒ 4/2ⁿ < 0.01 ⇒ 2ⁿ>400 ⇒ **n = 9**.

**Newton–Raphson (kök bulma):** f(x)=0 için Taylor: f(x_k)+f′(x_k)(x−x_k)=0 ⇒
x_{k+1} = x_k − f(x_k)/f′(x_k).

**Newton (optimizasyon):** 2. derece Taylor, f′(x)=0:
f′(x_k)+f″(x_k)(x−x_k)=0 ⇒ **x_{k+1} = x_k − f′(x_k)/f″(x_k)**.
Çok değişkenli: **x_{k+1} = x_k − H(x_k)⁻¹ ∇f(x_k)**.

**Newton örneği** (`12_…`, `13_…`): f(x) = 4x³ − 3x⁴, f′ = 12x² − 12x³, f″ = 24x − 36x², x₀ = 0.6
| k | x_k | f′(x_k) | f″(x_k) | x_{k+1} |
|---|---|---|---|---|
| 1 | 0.6 | 1.728 | 1.440 | −0.6 |
| 2 | −0.6 | 1.728 | −1.440 | 0.6 |
→ iterasyonlar 0.6 ↔ −0.6 arasında **döngüye giriyor** (yakınsamıyor). Tahtada x<0 için ayrı bir ifade (f′=12x²+12x³) kullanılmış ✎; ders mesajı: Newton başlangıç noktasına duyarlı, f″ işaretine bakılmalı. (Not: x=1'de f′=0 ama f″(1)=−12<0 → orası maksimum.)

Defter notu: Newton'ı **f″ > 0** olmadan minimizasyon için kullanma; bisection garantili ama yavaş.

---

## 3. Convexity (`03_Convexity`)

### 3.1 Convex set
S konveks ⇔ x₁,x₂ ∈ S ⇒ λx₁+(1−λ)x₂ ∈ S, λ∈[0,1].
Örnekler (`01_convex_set_ornekleri`): {Ax ≤ b}, {Ax = b} (polyhedron, konveks); (x−3)²+(y−2)² ≤ 4 (disk, r=2, konveks); x²+y²=4 (çember, **konveks değil**); iki parçadan oluşan "V" bölge (konveks değil).

### 3.2 Convex function (`02_convex_function_tanimi`, `07_…`)
f: S→ℝ, S ⊂ ℝⁿ konveks küme. **Convex** ⇔ ∀x₁,x₂∈S, 0<λ<1:
f(λx₁+(1−λ)x₂) ≤ λf(x₁)+(1−λ)f(x₂). **Strictly convex:** "<" (x₁≠x₂).
Tek değişken: f convex ⇔ f″(x) ≥ 0; concave ⇔ f″(x) ≤ 0. Çizim: kiriş fonksiyonun üstünde.

**İspat örneği** (`03_x2_convex_ispat`): f(x)=x²:
(λx₁+(1−λ)x₂)² ≤ λx₁²+(1−λ)x₂² ⇔ λ²x₁²+(1−λ)²x₂²+2λ(1−λ)x₁x₂ ≤ λx₁²+(1−λ)x₂² ⇔ … ⇔ −λ(1−λ)(x₁−x₂)² ≤ 0 ✓.
(Tahtada aday fonksiyonlar: x², x·ln x, x⁴.)

### 3.3 Hypograph / Epigraph (`04_hypograph`, `05_`, `06_`, `07_`)
- Hypograph: H(f) = {(x,y) ∈ Eₙ₊₁ : x∈S, y ≤ f(x)}
- Epigraph:  E(f) = {(x,y) ∈ Eₙ₊₁ : x∈S, y ≥ f(x)}
- **Teorem:** S konveks; f convex ⇔ epigraph E(f) konveks küme. (f concave ⇔ hypograph konveks.)
- Seviye kümesi: {x : f(x) ≤ α} convex f için konveks (tahtada f(x) ≤ α notu).

### 3.4 Gradient (birinci derece) karakterizasyonu (`08_gradient_esitsizligi`)
S konveks, f türevlenebilir: **f convex ⇔ f(y) ≥ f(x) + ∇f(x)ᵀ(y−x), ∀x,y∈S**
(teğet doğrusu/düzlemi fonksiyonun altında).

### 3.5 Hessian (ikinci derece) karakterizasyonu (`09_…`, `10_…`, `11_…`)
H(x) = ∇²f(x) = [∂²f/∂xᵢ∂xⱼ] (n×n, **simetrik**). Örnek: f(x₁,x₂)=x₁²+x₂³.
**Teorem:** S konveks, f iki kez türevlenebilir. f **convex** ⇔ H(x) **PSD** ∀x∈S.
Strictly convex ⇐ H PD. Concave ⇔ NSD; strictly concave ⇐ ND. (Tek boyutta f″ ≥ 0.)

**f(x)=x³ örneği** (`10_x3_ornek`): f′=3x², f″=6x ≥ 0 ? → sadece x ≥ 0 için; ℝ üzerinde convex **değil** (x³ x≥0'da convex).

### 3.6 Definite matrisler (`12_PSD_xQx`, `13_principal_minors_kriteri`)
- PSD: xᵀQx ≥ 0 ∀x (3×3 Q için x=[x₁ x₂ x₃]ᵀ).
- **A PSD ⇔ tüm principal minor'lar ≥ 0**
- **A PD ⇔ tüm leading principal minor'lar > 0**
- **A NSD ⇔ k. mertebeden sıfırdan farklı principal minor'lar (−1)ᵏ işaretli** (tüm k)
- **A ND ⇔ k. leading principal minor'ların işareti (−1)ᵏ**
- Principal minor = aynı satır-sütun indeksleriyle alt matrisin determinantı (leading = ilk k satır/sütun).

**Alıştırma (defter, `14_`, `15_`):** f(x₁,x₂) = x₁³(x₁−4) + 3(x₂−5)² + 10 — "domain'in hangi kısmında convex/concave?"
- ∂f/∂x₁ = 4x₁³ − 12x₁², ∂f/∂x₂ = 6(x₂−5); ∂²f/∂x₁² = 12x₁(x₁−2), ∂²f/∂x₂² = 6, çapraz = 0.
- H = diag(12x₁(x₁−2), 6). PM: 12x₁(x₁−2), 6, 72x₁(x₁−2) ≥ 0 ⇔ **x₁ ∈ (−∞,0] ∪ [2,∞)** → bu bölgelerde convex (her biri ayrı konveks küme).
- Defterin sonu (muhtemelen quiz yapısı): **1) Search procedure, 2) Convex/concave check (45 dk), 3) General.**

### 3.7 Quasiconvexity (`16_`, `17_`, `18_`)
f: S→E₁, S ⊂ Eₙ konveks. **Quasiconvex** ⇔ ∀x₁,x₂∈S: f(λx₁+(1−λ)x₂) ≤ max{f(x₁), f(x₂)}.
**Quasiconcave** ⇔ ≥ min{f(x₁), f(x₂)}. Strictly: "<" / ">".
**Her convex fonksiyon quasiconvex'tir, tersi doğru değil** (örn. x³ veya tek vadili ama kirişi aşan eğriler; f(x)=1/x, x≥0 çizilmiş: f′=−x⁻², f″=2x⁻³ ≥ 0 ⇒ convex).

---

## Eksik / sonraki haftalar
Syllabus: Unconstrained NLO (hafta 5–7, Quiz 2), Constrained NLO (hafta 8–10, Midterm), ML (hafta 11–12, Quiz 3). Eski sınavlar için bkz. `Quiz1_Calisma.md`.
