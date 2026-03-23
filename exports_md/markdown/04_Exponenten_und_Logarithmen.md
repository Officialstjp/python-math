# Grundlagen

## 04 – Exponenten und Logarithmen

Potenzen und Logarithmen sind eines der wichtigsten Konzepte in der Mathematik, da diese die Grundlage für viele technische und wissenschaftliche Anwendungen bilden. In diesem Abschnitt werden wir die Grundlagen von Potenzen und Logarithmen behandeln, einschließlich ihrer Definitionen, Eigenschaften und Anwendungen.

### Lernziele

- Du kennst die **Potenzgesetze** und kannst sie sicher anwenden.
- Du verstehst **negative und gebrochene Exponenten**.
- Du kannst den **Logarithmus** als Umkehrung der Exponentialfunktion erklären.
- Du kennst die **Rechenregeln für Logarithmen** und kannst die Basis wechseln.
- Du erkennst den Zusammenhang zwischen $e$, $\ln$, $\log_{10}$ und $\log_2$.

---

## Potenzen

Eine Potenz ist eine Kurzschreibweise für die wiederholte Multiplikation einer Zahl mit sich selbst. Die allgemeine Form einer Potenz ist $a^n$, wobei:

$$
a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ Faktoren}}, \quad a \in \mathbb{R}, \ n \in \mathbb{N}
$$

- $a$ ist die **Basis**
- $n$ ist der **Exponent** (auch: Hochzahl)
- $a^n$ ist die **Potenz** (auch: Potenzwert)

### Potenzgesetze

Für Potenzen gelten folgende Rechenregeln (für $a, b \in \mathbb{R}$, $m, n \in \mathbb{Z}$, $a \neq 0$, $b \neq 0$ wo nötig):

| Regel | Formel | Beispiel |
|-------|--------|----------|
| Gleiche Basis, Multiplikation | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7 = 128$ |
| Gleiche Basis, Division | $\frac{a^m}{a^n} = a^{m-n}$ | $\frac{5^6}{5^2} = 5^4 = 625$ |
| Potenz einer Potenz | $(a^m)^n = a^{m \cdot n}$ | $(3^2)^3 = 3^6 = 729$ |
| Gleicher Exponent, Multiplikation | $a^n \cdot b^n = (a \cdot b)^n$ | $2^3 \cdot 5^3 = 10^3 = 1000$ |
| Gleicher Exponent, Division | $\frac{a^n}{b^n} = \left(\frac{a}{b}\right)^n$ | $\frac{6^2}{3^2} = 2^2 = 4$ |

### Spezielle Exponenten

#### Exponent 0
Jede Zahl (außer 0) hoch 0 ergibt 1:
$$
a^0 = 1 \quad (a \neq 0)
$$

*Begründung:* Aus $a^n \cdot a^0 = a^{n+0} = a^n$ folgt $a^0 = 1$.

#### Negative Exponenten
Ein negativer Exponent erzeugt den Kehrwert:
$$
a^{-n} = \frac{1}{a^n} \quad (a \neq 0)
$$

**Beispiele:**
$$
2^{-3} = \frac{1}{2^3} = \frac{1}{8} = 0{,}125 \qquad\qquad 10^{-2} = \frac{1}{100} = 0{,}01
$$

#### Gebrochene (rationale) Exponenten - Wurzeln als Potenzen

Der Zusammenhang zwischen Wurzeln und Potenzen ist:
$$
a^{\frac{1}{n}} = \sqrt[n]{a} \quad (a \geq 0, \ n \in \mathbb{N}, \ n \geq 2)
$$

Allgemeiner:
$$
a^{\frac{p}{q}} = \sqrt[q]{a^p} = \left(\sqrt[q]{a}\right)^p
$$

**Beispiele:**
$$
8^{\frac{1}{3}} = \sqrt[3]{8} = 2 \qquad\qquad 27^{\frac{2}{3}} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9
$$
$$
4^{\frac{3}{2}} = \left(\sqrt{4}\right)^3 = 2^3 = 8 \qquad\qquad 16^{-\frac{1}{2}} = \frac{1}{\sqrt{16}} = \frac{1}{4}
$$

### Zehnerpotenzen und wissenschaftliche Notation

Sehr große oder sehr kleine Zahlen werden mithilfe von Zehnerpotenzen dargestellt:

$$
a \times 10^n, \quad 1 \leq |a| < 10
$$

| Dezimalschreibweise | Wissenschaftliche Notation |
|---------------------|---------------------------|
| $300\,000\,000$ | $3 \times 10^8$ |
| $0{,}000\,001$ | $1 \times 10^{-6}$ |
| $6\,370\,000$ | $6{,}37 \times 10^6$ |

*Lichtgeschwindigkeit: $c \approx 3 \times 10^8 \text{ m/s}$, Elektronenmasse: $m_e \approx 9{,}109 \times 10^{-31} \text{ kg}$*

## Logarithmen

### Definition

Der Logarithmus ist die **Umkehrfunktion** zur Exponentialfunktion. Er beantwortet die Frage:

> *"Mit welchem Exponenten muss ich die Basis $a$ potenzieren, um $b$ zu erhalten?"*

$$
\log_a(b) = c \quad \Longleftrightarrow \quad a^c = b \qquad (a > 0, \ a \neq 1, \ b > 0)
$$

gesprochen: *"Der Logarithmus von $b$ zur Basis $a$ ist $c$."*

**Beispiele:**
$$
\log_2(8) = 3 \quad \text{weil} \quad 2^3 = 8
$$
$$
\log_{10}(1000) = 3 \quad \text{weil} \quad 10^3 = 1000
$$
$$
\log_5(25) = 2 \quad \text{weil} \quad 5^2 = 25
$$

### Wichtige Spezialfälle

Für jede gültige Basis $a$ gilt:
$$
\log_a(1) = 0 \quad \text{(weil } a^0 = 1\text{)}
$$
$$
\log_a(a) = 1 \quad \text{(weil } a^1 = a\text{)}
$$
$$
\log_a(a^n) = n
$$
$$
a^{\log_a(x)} = x
$$

### Gebräuchliche Logarithmen

| Name | Schreibweise | Basis | Verwendung |
|------|-------------|-------|------------|
| Dekadischer Logarithmus | $\log_{10}(x)$ oder $\lg(x)$ | $10$ | Dezimalsystem, Dezibel, pH-Wert |
| Natürlicher Logarithmus | $\ln(x) = \log_e(x)$ | $e \approx 2{,}718$ | Analysis, Naturwissenschaft, ML |
| Binärer Logarithmus | $\log_2(x)$ oder $\text{ld}(x)$ | $2$ | Informatik, Bits |


> **Hinweis:** Auf vielen Taschenrechnern (auch dem TI-Nspire) ist die Taste `log` der dekadische Logarithmus ($\log_{10}$) und `ln` der natürliche Logarithmus.

### Rechenregeln für Logarithmen

Alle Regeln gelten für $a > 0, a \neq 1$ und $x, y > 0$:

| Regel | Formel | Herleitung |
|-------|--------|------------|
| **Potenzregel** | $\log_a(x^r) = r \cdot \log_a(x)$ | Exponent wird zum Faktor |
| **Produktregel** | $\log_a(x \cdot y) = \log_a(x) + \log_a(y)$ | Multiplikation → Addition |
| **Quotientenregel** | $\log_a\!\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)$ | Division → Subtraktion |
| **Wurzelregel** | $\log_a\!\left(\sqrt[n]{x}\right) = \frac{1}{n} \cdot \log_a(x)$ | Spezialfall der Potenzregel |

**Beispiele:**

$$
\log(10^3) = 3 \cdot \log(10) = 3 \cdot 1 = 3
$$

$$
\log_2(64) = \log_2(2^6) = 6 \cdot \log_2(2) = 6
$$

$$
\log(1000) = \log(10 \cdot 10 \cdot 10) = \log(10) + \log(10) + \log(10) = 3
$$

$$
\log\!\left(\frac{100}{10}\right) = \log(100) - \log(10) = 2 - 1 = 1
$$

$$
\ln\!\left(\sqrt{e}\right) = \frac{1}{2} \cdot \ln(e) = \frac{1}{2}
$$

> **Merke:** Der Logarithmus verwandelt "schwere" Operationen in "leichte":  
> Multiplikation → Addition, Division → Subtraktion, Potenzen → Multiplikation.  
> Genau deshalb ist er in der Praxis so nützlich (z.B. Dezibel-Skala, pH-Wert, Log-Loss in ML).

### Wechsel der Logarithmus-Basis

Der Logarithmus zur Basis $a$ kann in jeden anderen Logarithmus umgerechnet werden:

$$
\log_a(x) = \frac{\log_b(x)}{\log_b(a)}
$$

**Wichtigster Spezialfall** (für den Taschenrechner, der nur $\ln$ und $\log$ hat):

$$
\log_a(x) = \frac{\ln(x)}{\ln(a)} = \frac{\log(x)}{\log(a)}
$$

**Beispiele:**

$$
\log_3(81) = \frac{\ln(81)}{\ln(3)} = \frac{\ln(3^4)}{\ln(3)} = \frac{4 \cdot \ln(3)}{\ln(3)} = 4
$$

$$
\log_5(200) = \frac{\log(200)}{\log(5)} \approx \frac{2{,}301}{0{,}699} \approx 3{,}292
$$

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Potenzgesetze | $a^m \cdot a^n = a^{m+n}$, $\frac{a^m}{a^n} = a^{m-n}$, $(a^m)^n = a^{mn}$ |
| Exponent 0 | $a^0 = 1$ für alle $a \neq 0$ |
| Negative Exponenten | $a^{-n} = \frac{1}{a^n}$ |
| Gebrochene Exponenten | $a^{m/n} = \sqrt[n]{a^m}$ |
| Logarithmus | $\log_a(x) = y \iff a^y = x$ — Umkehrung der Potenz |
| Log-Rechenregeln | $\log(xy) = \log(x)+\log(y)$, $\log(x/y) = \log(x)-\log(y)$, $\log(x^n) = n\log(x)$ |
| Basiswechsel | $\log_a(x) = \frac{\ln(x)}{\ln(a)}$ |

> **Nächster Schritt:** Im nächsten Kapitel geht es um **mathematische Notation und Konventionen** — Symbole und Schreibweisen, die in allen weiteren Kapiteln verwendet werden.

---

## Glossar

| Deutsch | English |
|---------|---------|
| Potenz | Power |
| Basis | Base |
| Exponent / Hochzahl | Exponent |
| Potenzgesetz | Power law / Exponent rule |
| Negativer Exponent | Negative exponent |
| Gebrochener Exponent | Fractional exponent |
| Wurzel | Root |
| Quadratwurzel | Square root |
| Kubikwurzel | Cube root |
| Logarithmus | Logarithm |
| Natürlicher Logarithmus | Natural logarithm |
| Dekadischer Logarithmus | Common logarithm |
| Basiswechsel | Change of base |
| Umkehrfunktion | Inverse function |
| Wissenschaftliche Notation | Scientific notation |
| Zehnerpotenz | Power of ten |
| Eulersche Zahl | Euler's number |
