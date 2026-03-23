# Grundlagen

## 05 – Notation & Konventionen

Mathematik hat eine eigene Sprache. Dieses Notebook ist ein Nachschlagewerk für Symbole und Schreibweisen, die überall auftauchen — von Matura-Aufgaben bis zu Machine-Learning-Papern.

### Lernziele

- Du kannst **Mengennotation** lesen und schreiben ($\in, \subset, \cup, \cap, \setminus$).
- Du verstehst **Summen-** ($\sum$) und **Produktzeichen** ($\prod$).
- Du kennst die **wichtigsten griechischen Buchstaben** und ihre Verwendung.
- Du beherrschst die **SI-Vorsilben** (nano, kilo, mega, …) und kannst Einheiten sicher umrechnen.

---

## 1. Mengennotation

### Grundlegende Schreibweisen

| Symbol | Bedeutung | Beispiel |
|--------|-----------|----------|
| $\{\ldots\}$ | Menge (aufzählend) | $\{1, 2, 3\}$ |
| $\{x \mid \ldots\}$ | Menge (beschreibend) | $\{x \mid x > 0\}$ = alle positiven Zahlen |
| $\in$ | „ist Element von" | $3 \in \mathbb{N}$ |
| $\notin$ | „ist nicht Element von" | $\sqrt{2} \notin \mathbb{Q}$ |
| $\subset$ | „ist echte Teilmenge von" | $\mathbb{N} \subset \mathbb{Z}$ |
| $\subseteq$ | „ist Teilmenge von" (inkl. Gleichheit) | $A \subseteq A$ |
| $\cup$ | Vereinigung ("oder") | $A \cup B$ |
| $\cap$ | Schnittmenge ("und") | $A \cap B$ |
| $\setminus$ | Differenz ("ohne") | $\mathbb{R} \setminus \mathbb{Q}$ = irrationale Zahlen |
| $\emptyset$ oder $\{\}$ | Leere Menge | $\mathbb{N} \cap \{-1, -2\} = \emptyset$ |
| $|A|$ | Mächtigkeit / Anzahl Elemente | $|\{a, b, c\}| = 3$ |

### Mengenoperationen — Beispiel

Sei $A = \{1, 2, 3, 4\}$ und $B = \{3, 4, 5, 6\}$:

$$
A \cup B = \{1, 2, 3, 4, 5, 6\}
$$
$$
A \cap B = \{3, 4\}
$$
$$
A \setminus B = \{1, 2\}
$$

## 2. Summen- und Produktzeichen

### Summenzeichen $\sum$

$$
\sum_{i=a}^{b} f(i) = f(a) + f(a+1) + \ldots + f(b)
$$

- $i$ — **Laufvariable** (Laufindex)
- $a$ — **untere Grenze** (Start)
- $b$ — **obere Grenze** (Ende)
- $f(i)$ — **Summand** (was summiert wird)

**Beispiele:**

$$
\sum_{i=1}^{4} i = 1 + 2 + 3 + 4 = 10
$$

$$
\sum_{k=0}^{3} k^2 = 0 + 1 + 4 + 9 = 14
$$

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2} \qquad \text{(Gaußsche Summenformel)}
$$

### Produktzeichen $\prod$

$$
\prod_{i=a}^{b} f(i) = f(a) \cdot f(a+1) \cdot \ldots \cdot f(b)
$$

**Beispiele:**

$$
\prod_{i=1}^{4} i = 1 \cdot 2 \cdot 3 \cdot 4 = 24 = 4!
$$

$$
\prod_{k=1}^{3} (k+1) = 2 \cdot 3 \cdot 4 = 24
$$

### Fakultät

Die Fakultät ist ein Spezialfall des Produktzeichens:

$$
n! = \prod_{i=1}^{n} i = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot n \qquad (0! = 1 \text{ per Definition})
$$

| $n$ | $n!$ |
|-----|------|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 10 | 3 628 800 |

> **Wo taucht das auf?** Kombinatorik, Wahrscheinlichkeitsrechnung, Binomialkoeffizienten, Taylor-Reihen.

## 3. Weitere wichtige Symbole

| Symbol | Bedeutung | Kontext |
|--------|-----------|---------|
| $\implies$ | „daraus folgt" | $x > 2 \implies x^2 > 4$ |
| $\iff$ | „genau dann, wenn" (Äquivalenz) | $x^2 = 4 \iff x = \pm 2$ |
| $\forall$ | „für alle" | $\forall x \in \mathbb{R}: x^2 \geq 0$ |
| $\exists$ | „es existiert" | $\exists x \in \mathbb{R}: x^2 = 2$ |
| $\approx$ | „ungefähr gleich" | $\pi \approx 3{,}14$ |
| $\propto$ | „proportional zu" | $F \propto m$ (Kraft proportional zur Masse) |
| $\infty$ | Unendlich (keine Zahl!) | $\lim_{x \to \infty}$ |
| $\Delta$ | Differenz / Änderung | $\Delta x = x_2 - x_1$ |
| $\binom{n}{k}$ | Binomialkoeffizient „$n$ über $k$" | $\binom{5}{2} = 10$ |

> **Lesebeispiel:** $\forall \varepsilon > 0 \;\; \exists N \in \mathbb{N} \;\; \forall n \geq N: |a_n - L| < \varepsilon$
>
> → Das ist die formale Definition von Konvergenz einer Folge (kommt in 07_Analysis).

## 4. Griechische Buchstaben

In Mathematik, Physik und Informatik werden griechische Buchstaben ständig benutzt, meist mit fester Bedeutung:

| Buchstabe | Name | Typische Verwendung |
|-----------|------|--------------------|
| $\alpha, \beta, \gamma$ | Alpha, Beta, Gamma | Winkel, Parameter |
| $\delta, \Delta$ | Delta | Kleine Änderung / Differenz |
| $\varepsilon$ | Epsilon | Kleine positive Zahl (Grenzwerte) |
| $\theta$ | Theta | Winkel, Modellparameter (ML) |
| $\lambda$ | Lambda | Eigenwert, Streckfaktor, Regularisierung |
| $\mu$ | My | Mittelwert, Micro-Vorsilbe |
| $\sigma, \Sigma$ | Sigma | Standardabweichung / Summe |
| $\pi, \Pi$ | Pi | Kreiszahl / Produkt |
| $\rho$ | Rho | Dichte, Korrelation |
| $\tau$ | Tau | Zeitkonstante |
| $\phi, \varphi$ | Phi | Winkel, goldener Schnitt |
| $\omega, \Omega$ | Omega | Kreisfrequenz / Ergebnisraum |
| $\nabla$ | Nabla | Gradient (Analysis/ML) |

## 5. SI-Vorsilben (Präfixe)

Das **Internationale Einheitensystem** (SI) verwendet Vorsilben, um Zehnerpotenzen auszudrücken. Diese begegnen dir nicht nur in Physik, sondern auch in Informatik und Alltag.

| Vorsilbe | Symbol | Faktor | Zehnerpotenz | Beispiel |
|----------|--------|--------|-------------|----------|
| Tera | T | $1\,000\,000\,000\,000$ | $10^{12}$ | 1 TB = $10^{12}$ Byte |
| Giga | G | $1\,000\,000\,000$ | $10^{9}$ | 2,4 GHz |
| Mega | M | $1\,000\,000$ | $10^{6}$ | 5 MP (Megapixel) |
| Kilo | k | $1\,000$ | $10^{3}$ | 3 kg = 3000 g |
| Hekto | h | $100$ | $10^{2}$ | 1 hPa (Hektopascal) |
| Deka | da | $10$ | $10^{1}$ | (selten) |
| — | — | $1$ | $10^{0}$ | Grundeinheit |
| Dezi | d | $0{,}1$ | $10^{-1}$ | 1 dl = 0,1 l |
| Zenti | c | $0{,}01$ | $10^{-2}$ | 1 cm = 0,01 m |
| Milli | m | $0{,}001$ | $10^{-3}$ | 500 mg |
| Mikro | $\mu$ | $0{,}000\,001$ | $10^{-6}$ | 50 µm (Haar) |
| Nano | n | $0{,}000\,000\,001$ | $10^{-9}$ | 7 nm (Chipgröße) |
| Piko | p | $10^{-12}$ | $10^{-12}$ | 100 pF (Pikofarad) |

### Umrechnung

Immer über die Zehnerpotenz:

$$
3{,}5 \text{ km} = 3{,}5 \times 10^3 \text{ m} = 3500 \text{ m}
$$

$$
250 \text{ nm} = 250 \times 10^{-9} \text{ m} = 2{,}5 \times 10^{-7} \text{ m}
$$

$$
0{,}47 \text{ mg} = 0{,}47 \times 10^{-3} \text{ g} = 4{,}7 \times 10^{-4} \text{ g}
$$

> **Informatik-Hinweis:** In der Informatik werden oft binäre Präfixe verwendet (1 KiB = $2^{10}$ = 1024 Byte, nicht 1000). Das SI-Kilo ist aber immer $10^3$.

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Mengennotation | $\in, \subset, \cup, \cap, \setminus$ — Elemente, Teilmengen, Operationen |
| Summenzeichen $\sum$ | Kompakte Schreibweise für Summen mit Laufvariable |
| Produktzeichen $\prod$ | Kompakte Schreibweise für Produkte; Spezialfall: $n!$ |
| Logische Symbole | $\implies, \iff, \forall, \exists$ — formale Aussagenlogik |
| Griechische Buchstaben | $\alpha, \beta, \sigma, \pi, \ldots$ — Standardsymbole in MINT-Fächern |
| SI-Vorsilben | Kilo ($10^3$), Mega ($10^6$), Milli ($10^{-3}$), Nano ($10^{-9}$), … |

> **Nächster Schritt:** Mit den Grundlagen aus Kapitel 00 bist du bereit für **Algebra** — quadratische Gleichungen, Polynome und fortgeschrittene Gleichungstypen.

---

## Glossar

| Deutsch | English |
|---------|---------|
| Menge | Set |
| Element | Element |
| Teilmenge | Subset |
| Vereinigung | Union |
| Schnittmenge | Intersection |
| Differenzmenge | Set difference |
| Leere Menge | Empty set |
| Summenzeichen | Summation sign |
| Produktzeichen | Product sign |
| Laufvariable / Index | Index variable |
| Fakultät | Factorial |
| Binomialkoeffizient | Binomial coefficient |
| Vorsilbe / Präfix | Prefix |
| Einheit | Unit |
| Zehnerpotenz | Power of ten |
