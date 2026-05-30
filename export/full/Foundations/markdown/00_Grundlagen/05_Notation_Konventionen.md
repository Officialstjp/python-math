# Grundlagen

## 05 - Notation & Konventionen

Mengennotation ($\in, \subset, \cup, \cap, \setminus$), Summen- und Produktzeichen ($\sum, \prod$), die wichtigsten griechischen Buchstaben und SI-Vorsilben (nano bis tera) — ein Nachschlagewerk für mathematische Schreibweisen.

### Lernziele

- Du kannst **Mengennotation** lesen und schreiben ($\in, \subset, \cup, \cap, \setminus$).
- Du verstehst **Summen-** ($\sum$) und **Produktzeichen** ($\prod$).
- Du kennst die **wichtigsten griechischen Buchstaben** und ihre Verwendung.
- Du beherrschst die **SI-Vorsilben** (nano, kilo, mega, …) und kannst Einheiten sicher umrechnen.

---

## 1. Mengennotation

Eine **Menge** ist eine Zusammenfassung von Objekten zu einem Ganzen. Die Mengennotation ist universell: Egal ob man Zahlenmengen ($\mathbb{N}, \mathbb{Z}, \mathbb{R}$), Lösungsmengen von Gleichungen oder Datenkollektionen beschreibst, man begegnet ihr überall in der Mathematik.

Mengen können auf zwei Arten definiert werden:
- **Aufzählend:** direkte Angabe aller Elemente, z.B. $A = \{1, 2, 3\}$
- **Beschreibend:** Eigenschaft, die Elemente erfüllen müssen, z.B. $\{x \mid x > 0\}$

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
| $\lvert A \rvert$ | Mächtigkeit / Anzahl Elemente | $\lvert\{a, b, c\}\rvert = 3$ |

### Mengenoperationen - Beispiel

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

> **Merkhilfe:** $\cup$ sieht wie ein „U" aus - denke an „**U**nion" (Vereinigung). $\cap$ ist das Gegenteil - die Schnittmenge, was **beiden** Mengen gemeinsam ist.

## 2. Summen- und Produktzeichen

Statt viele gleichartige Terme einzeln aufzuzählen ($1 + 2 + 3 + \ldots + 100$), gibt es Kurzschreibweisen: Das **Summenzeichen** $\sum$ (griechisch: *Sigma*) und das **Produktzeichen** $\prod$ (griechisch: *Pi*) beschreiben wiederholte Addition bzw. Multiplikation kompakt mit einer **Laufvariable**.

### Summenzeichen $\sum$

$$
\sum_{i=a}^{b} f(i) = f(a) + f(a+1) + \ldots + f(b)
$$

- $i$ - **Laufvariable** (Laufindex): nimmt nacheinander alle ganzzahligen Werte von $a$ bis $b$ an
- $a$ - **untere Grenze** (Start)
- $b$ - **obere Grenze** (Ende)
- $f(i)$ - **Summand** (was für jeden Wert von $i$ summiert wird)

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

> **Lesehilfe:** Lies $\displaystyle\sum_{i=1}^{4} i$ als: „Summiere $i$, wobei $i$ von $1$ bis $4$ läuft."

### Produktzeichen $\prod$

Analog zur Summe, aber mit Multiplikation:

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

Die Fakultät ist ein Spezialfall des Produktzeichens - das Produkt aller natürlichen Zahlen von $1$ bis $n$:

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

Die folgende Notation stammt aus der **Logik und Analysis**. Sie ermöglicht es, mathematische Aussagen präzise und kompakt zu formulieren - statt ganzer Sätze steht ein Symbol für „für alle", „es existiert" oder „genau dann wenn".

Das ist besonders wichtig beim Lesen von Definitionen und Beweisen: Ein einzelner Satz wie
$$\forall \varepsilon > 0 \;\; \exists N \in \mathbb{N} \;\; \forall n \geq N: \lvert a_n - L \rvert < \varepsilon$$
ist die vollständige formale Definition von Konvergenz - ohne diese Symbole würde sie einen langen Absatz benötigen.

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

> **Wichtig:** $\implies$ und $\iff$ sind nicht dasselbe! $A \implies B$ bedeutet nur, dass aus $A$ folgt $B$ - nicht umgekehrt. $A \iff B$ bedeutet beide Richtungen gelten.

> **Lesebeispiel:** $\forall \varepsilon > 0 \;\; \exists N \in \mathbb{N} \;\; \forall n \geq N: \lvert a_n - L \rvert < \varepsilon$
>
> → Das ist die formale Definition von Konvergenz einer Folge (kommt in 07_Analysis).

## 4. Griechische Buchstaben

Griechische Buchstaben sind in Mathematik, Physik und Informatik allgegenwärtig. Manche haben eine **fest zugewiesene Bedeutung** (z.B. $\pi \approx 3{,}14159\ldots$ für die Kreiszahl), andere dienen als flexible Variablennamen vor allem für Winkel, Parameter und Konstanten, um sie von lateinischen Variablen zu unterscheiden.

Du musst die Tabelle nicht auswendig lernen. Wichtiger ist, dass du einen Buchstaben **wiedererkennst** und seinen typischen Kontext kennst, wenn er dir in einer Formel begegnet.

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

> **Beispiel aus der Physik:** Die Formel $F = m \cdot \alpha$ verwendet $\alpha$ für die Winkelbeschleunigung - sofort erkennbar als „ein Winkelparameter", weil es ein griechischer Buchstabe ist.

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
| - | - | $1$ | $10^{0}$ | Grundeinheit |
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

## Verständnis-Check

*Löse die folgenden Aufgaben auf Papier.*

**Aufgabe 1: Mengennotation**

Sei $A = \{1, 3, 5, 7\}$ und $B = \{2, 3, 5, 8\}$. Bestimme:

a) $A \cup B$

b) $A \cap B$

c) $A \setminus B$

d) $\lvert A \cap B \rvert$

**Aufgabe 2: Summenzeichen**

Berechne:

a) $\displaystyle\sum_{i=1}^{5} i$

b) $\displaystyle\sum_{k=0}^{3} 2^k$

c) $\displaystyle\sum_{i=1}^{n} i = ?$ (Formel angeben)

d) Schreibe als Summenzeichen: $1^2 + 2^2 + 3^2 + \ldots + 10^2$

**Aufgabe 3: Produktzeichen & Fakultät**

a) $\displaystyle\prod_{i=1}^{5} i$

b) $\frac{6!}{4!}$

c) $\binom{5}{2} = \frac{5!}{2! \cdot 3!}$

**Aufgabe 4: Vorsilben umrechnen**

a) 4,7 km in m

b) 350 nm in m (wissenschaftliche Notation)

c) 2,5 MHz in Hz

d) 0,003 g in mg

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $A \cup B = \{1, 2, 3, 5, 7, 8\}$

b) $A \cap B = \{3, 5\}$

c) $A \setminus B = \{1, 7\}$

d) $\lvert A \cap B \rvert = 2$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

a) $1 + 2 + 3 + 4 + 5 = 15$

b) $2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15$

c) $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$

d) $\displaystyle\sum_{i=1}^{10} i^2$
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

a) $5! = 120$

b) $\frac{6!}{4!} = \frac{720}{24} = 30$

c) $\binom{5}{2} = \frac{120}{2 \cdot 6} = \frac{120}{12} = 10$
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

a) $4{,}7 \times 10^3 = 4700$ m

b) $350 \times 10^{-9} = 3{,}5 \times 10^{-7}$ m

c) $2{,}5 \times 10^6 = 2\,500\,000$ Hz

d) $0{,}003 \text{ g} = 3 \text{ mg}$
</details>

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Mengennotation | $\in, \subset, \cup, \cap, \setminus$ - Elemente, Teilmengen, Operationen |
| Summenzeichen $\sum$ | Kompakte Schreibweise für Summen mit Laufvariable |
| Produktzeichen $\prod$ | Kompakte Schreibweise für Produkte; Spezialfall: $n!$ |
| Logische Symbole | $\implies, \iff, \forall, \exists$ - formale Aussagenlogik |
| Griechische Buchstaben | $\alpha, \beta, \sigma, \pi, \ldots$ - Standardsymbole in MINT-Fächern |
| SI-Vorsilben | Kilo ($10^3$), Mega ($10^6$), Milli ($10^{-3}$), Nano ($10^{-9}$), … |

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
