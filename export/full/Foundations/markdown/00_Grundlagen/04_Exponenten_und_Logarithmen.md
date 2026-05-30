# Grundlagen
## 04 - Exponenten und Logarithmen

Potenzgesetze ($a^m \cdot a^n = a^{m+n}$, negative und gebrochene Exponenten), Logarithmus als Umkehrung der Exponentialfunktion ($\log_a(a^x) = x$), Logarithmengesetze und Basiswechsel.

> Vorausgesetzt: Grundrechenarten, Bruchrechnung.

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

Diese Schreibweise vereinfacht auch bei Schrift auf Papier die Darstellung von extrem großen oder kleinen Zahlen, z.B. $10^{18}$ statt $1.000.000.000.000.000.000$.

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

Die drei am häufigsten verwendeten Basen haben eigene Namen auf den meisten Taschenrechnern entspricht die Taste `log` dem dekadischen Logarithmus und `ln` dem natürlichen Logarithmus:

| Name | Schreibweise | Basis | Verwendung |
|------|-------------|-------|------------|
| Dekadischer Logarithmus | $\log_{10}(x)$ oder $\lg(x)$ | $10$ | Dezimalsystem, Dezibel, pH-Wert |
| Natürlicher Logarithmus | $\ln(x) = \log_e(x)$ | $e \approx 2{,}718$ | Analysis, Naturwissenschaft, ML |
| Binärer Logarithmus | $\log_2(x)$ oder $\text{ld}(x)$ | $2$ | Informatik, Bits |

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

Da die meisten Taschenrechner und Programmiersprachen nur $\ln$ und $\log_{10}$ direkt berechnen können, ist diese Formel der praktische Schlüssel für jeden anderen Logarithmus. Der Logarithmus zur Basis $a$ lässt sich wie folgt umrechnen:

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

    =======================================================
    Verifikation: Potenzgesetze
    =======================================================
    
      2^3 · 2^4 = 128  |  2^(3+4) = 128  ✓
      5^6 / 5^2 = 625  |  5^(6-2) = 625  ✓
      (3^2)^3 = 729  |  3^(2·3) = 729  ✓
      2^3 · 5^3 = 1000  |  (2·5)^3 = 1000  ✓
    
      7^0 = 1  ✓ (Jede Zahl hoch 0 ist 1)
      2^(-3) = 0.125  |  1/2^3 = 0.125  ✓
      8^(1/3) = 2.0000  |  ∛8 = 2  ✓
      27^(2/3) = 9.0000  |  (∛27)² = 9  ✓
    
    =======================================================
    Verifikation: Logarithmusgesetze
    =======================================================
    
      log₂(8) = 3  (weil 2³ = 8)  ✓
      log₁₀(1000) = 3  (weil 10³ = 1000)  ✓
      ln(e²) = 2.0000  ≈ 2  ✓
    
      Potenzregel:    log₂(8) = log₂(2³) = 3·log₂(2) = 3·1 = 3  ✓
      Produktregel:   log(6) = log(2·3) = log(2) + log(3)
                      0.7782 = 0.3010 + 0.4771 = 0.7782  ✓
      Quotientregel:  log(100/10) = log(100) - log(10) = 2 - 1 = 1  ✓
    
      Basiswechsel:   log₃(81) = ln(81)/ln(3) = 4.3944/1.0986 = 4  ✓
                      log₅(200) = log(200)/log(5) = 2.3010/0.6990 = 3.2920
    

---

## Verständnis-Check

*Löse die folgenden Aufgaben auf Papier.*

**Aufgabe 1: Potenzgesetze vereinfachen**

Vereinfache so weit wie möglich:

a) $2^5 \cdot 2^3$

b) $\frac{a^7}{a^3}$

c) $(x^4)^3$

d) $\frac{12^3}{4^3}$

e) $5^0 + 3^0 + (-7)^0$

**Aufgabe 2: Spezielle Exponenten**

Berechne ohne Taschenrechner:

a) $4^{-2}$

b) $8^{\frac{2}{3}}$

c) $\left(\frac{1}{9}\right)^{-\frac{1}{2}}$

d) $27^{\frac{4}{3}}$

e) $100^{-\frac{3}{2}}$

**Aufgabe 3: Logarithmen berechnen**

Bestimme den Wert:

a) $\log_2(32)$

b) $\log_3(81)$

c) $\log_{10}(0{,}001)$

d) $\ln(e^5)$

e) $\log_4(1)$

f) $\log_9(3)$

**Aufgabe 4: Logarithmus-Rechenregeln**

Schreibe als einzelnen Logarithmus:

a) $\log(a) + \log(b)$

b) $3 \cdot \ln(x) - \ln(y)$

c) $\frac{1}{2} \cdot \log(25) + \log(2)$

d) $2 \cdot \log_3(x) + \log_3(y) - \log_3(z)$

**Aufgabe 5: Gleichungen lösen**

Löse nach $x$ auf:

a) $2^x = 64$

b) $5^x = 125$

c) $3^x = 20$ (Ergebnis als Logarithmus und als Dezimalzahl)

d) $e^{2x} = 7$

e) $\log_2(x) = 5$

f) $\ln(x+1) = 3$

**Aufgabe 6: Wissenschaftliche Notation**

a) Schreibe in wissenschaftlicher Notation: $0{,}00042$

b) Schreibe als Dezimalzahl: $6{,}022 \times 10^{12}$

c) Berechne: $(3 \times 10^4) \cdot (2 \times 10^{-7})$

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $2^5 \cdot 2^3 = 2^{5+3} = 2^8 = 256$

b) $\frac{a^7}{a^3} = a^{7-3} = a^4$

c) $(x^4)^3 = x^{4 \cdot 3} = x^{12}$

d) $\frac{12^3}{4^3} = \left(\frac{12}{4}\right)^3 = 3^3 = 27$

e) $5^0 + 3^0 + (-7)^0 = 1 + 1 + 1 = 3$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

a) $4^{-2} = \frac{1}{4^2} = \frac{1}{16}$

b) $8^{\frac{2}{3}} = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4$

c) $\left(\frac{1}{9}\right)^{-\frac{1}{2}} = \left(9\right)^{\frac{1}{2}} = \sqrt{9} = 3$

d) $27^{\frac{4}{3}} = \left(\sqrt[3]{27}\right)^4 = 3^4 = 81$

e) $100^{-\frac{3}{2}} = \frac{1}{100^{\frac{3}{2}}} = \frac{1}{\left(\sqrt{100}\right)^3} = \frac{1}{10^3} = \frac{1}{1000} = 0{,}001$
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

a) $\log_2(32) = \log_2(2^5) = 5$

b) $\log_3(81) = \log_3(3^4) = 4$

c) $\log_{10}(0{,}001) = \log_{10}(10^{-3}) = -3$

d) $\ln(e^5) = 5$

e) $\log_4(1) = 0$ (weil $4^0 = 1$)

f) $\log_9(3) = \log_9(9^{\frac{1}{2}}) = \frac{1}{2}$
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

a) $\log(a) + \log(b) = \log(a \cdot b)$

b) $3 \cdot \ln(x) - \ln(y) = \ln(x^3) - \ln(y) = \ln\!\left(\frac{x^3}{y}\right)$

c) $\frac{1}{2} \cdot \log(25) + \log(2) = \log(25^{\frac{1}{2}}) + \log(2) = \log(5) + \log(2) = \log(10) = 1$

d) $2\log_3(x) + \log_3(y) - \log_3(z) = \log_3(x^2) + \log_3(y) - \log_3(z) = \log_3\!\left(\frac{x^2 \cdot y}{z}\right)$
</details>

<details open>
<summary>Lösung Aufgabe 5</summary>

a) $2^x = 64 = 2^6 \implies x = 6$

b) $5^x = 125 = 5^3 \implies x = 3$

c) $3^x = 20 \implies x = \log_3(20) = \frac{\ln(20)}{\ln(3)} \approx 2{,}727$

d) $e^{2x} = 7 \implies 2x = \ln(7) \implies x = \frac{\ln(7)}{2} \approx 0{,}973$

e) $\log_2(x) = 5 \implies x = 2^5 = 32$

f) $\ln(x + 1) = 3 \implies x + 1 = e^3 \implies x = e^3 - 1 \approx 19{,}086$
</details>

<details open>
<summary>Lösung Aufgabe 6</summary>

a) $0{,}00042 = 4{,}2 \times 10^{-4}$

b) $6{,}022 \times 10^{12} = 6\,022\,000\,000\,000$

c) $(3 \times 10^4) \cdot (2 \times 10^{-7}) = 6 \times 10^{4+(-7)} = 6 \times 10^{-3} = 0{,}006$
</details>

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


