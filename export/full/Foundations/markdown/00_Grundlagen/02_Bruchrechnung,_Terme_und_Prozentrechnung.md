# Grundlagen
## 02 - Bruchrechnung, Terme und Prozentrechnung

Dieses Kapitel behandelt Brüche (addieren, kürzen, Doppelbrüche), Terme (vereinfachen, binomische Formeln, faktorisieren) und Prozentrechnung ($W = G \cdot p/100$).

### Lernziele

- Du kannst Brüche sicher **addieren, subtrahieren, multiplizieren und dividieren**.
- Du verstehst **Kürzen und Erweitern** und erkennst, wann ein Bruch vollständig gekürzt ist.
- Du kannst **Terme aufstellen, vereinfachen und umformen**.
- Du beherrschst die **binomischen Formeln** und kannst sie in beide Richtungen anwenden.
- Du kannst einfache Terme **faktorisieren** (ausklammern, binomische Formeln rückwärts).

---

## 1. Bruchrechnung

Ein Bruch $\frac{a}{b}$ besteht aus:
- **Zähler** $a$ (oben) - wie viele Teile wir haben
- **Nenner** $b$ (unten, $b \neq 0$) - in wie viele Teile das Ganze geteilt wird

### Erweitern und Kürzen

Erweitern (mit $k \neq 0$):
$$
\frac{a}{b} = \frac{a \cdot k}{b \cdot k}
$$

Kürzen (mit dem ggT von $a$ und $b$):
$$
\frac{a}{b} = \frac{a \div \gcd(a,b)}{b \div \gcd(a,b)}
$$

**Beispiel:** $\frac{12}{18} = \frac{12 \div 6}{18 \div 6} = \frac{2}{3}$

### Rechenregeln

| Operation | Regel | Beispiel |
|-----------|-------|----------|
| Addition / Subtraktion | $\frac{a}{b} \pm \frac{c}{d} = \frac{a \cdot d \pm c \cdot b}{b \cdot d}$ | $\frac{2}{3} + \frac{1}{4} = \frac{8 + 3}{12} = \frac{11}{12}$ |
| Multiplikation | $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$ | $\frac{3}{5} \cdot \frac{2}{7} = \frac{6}{35}$ |
| Division | $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}$ | $\frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8}$ |

> **Merke:** Bei Addition/Subtraktion braucht man einen **gemeinsamen Nenner** (kgV). Bei Multiplikation/Division nicht.

#### Addition im Detail

Die Schritte sind immer dieselben - der einzige Unterschied zu Zahlenbrüchen ist, dass die Nenner nun Terme statt Zahlen sind:

$$
\begin{align*}
    &\quad \frac{2}{x} + \frac{3}{x+1} \tag{Ausgangsgleichung} \\
    &= \frac{2 \cdot (x+1)}{x \cdot (x+1)} + \frac{3 \cdot x}{(x+1) \cdot x} \tag{Erweitern} \\
    &= \frac{2(x+1) + 3x}{x(x+1)} \tag{Gemeinsamer Nenner} \\
    &= \frac{2x + 2 + 3x}{x(x+1)} \tag{Zähler ausmultiplizieren} \\
    &= \frac{5x + 2}{x^2 + x} \tag{Zusammenfassen}
\end{align*}
$$

Spezialfall: Faktorisieren vor dem Addieren:

$$
\begin{align*}
    % Schritt 1: Nenner faktorisieren
    &\text{1. Nenner faktorisieren (Binomische Formel \& Ausklammern):} \\
    &\frac{3}{(x-2)(x+2)} + \frac{1}{2(x-2)} \\[1em]
    % Schritt 2: Hauptnenner bestimmen
    &\text{2. Hauptnenner (HN) bestimmen: } HN = 2(x-2)(x+2) \\[1em]
    % Schritt 3: Erweitern
    &\text{3. Brüche auf den Hauptnenner erweitern:} \\
    &\frac{3 \cdot 2}{(x-2)(x+2) \cdot 2} + \frac{1 \cdot (x+2)}{2(x-2) \cdot (x+2)} \\[1em]
    % Schritt 4: Zusammenfassen
    &\text{4. Auf einen gemeinsamen Bruchstrich schreiben:} \\
    &\frac{6 + (x+2)}{2(x-2)(x+2)} \\[1em]
    % Schritt 5: Vereinfachen
    &\text{5. Zähler zusammenfassen:} \\
    &\frac{x+8}{2(x^2-4)} \quad \text{oder} \quad \frac{x+8}{2x^2-8}
\end{align*}
$$

### Doppelbrüche

Ein Bruch im Bruch wird durch "Durchmultiplizieren" aufgelöst:

$$
\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}
$$

**Beispiel:** $\frac{\frac{3}{4}}{\frac{5}{6}} = \frac{3}{4} \cdot \frac{6}{5} = \frac{18}{20} = \frac{9}{10}$

### Brüche und Dezimalzahlen

| Bruch | Dezimal | Bruch | Dezimal |
|-------|---------|-------|---------|
| $\frac{1}{2}$ | $0{,}5$ | $\frac{1}{5}$ | $0{,}2$ |
| $\frac{1}{3}$ | $0{,}\overline{3}$ | $\frac{1}{6}$ | $0{,}1\overline{6}$ |
| $\frac{1}{4}$ | $0{,}25$ | $\frac{1}{8}$ | $0{,}125$ |

*Erinnerung aus Notebook 01:* Endliche oder periodische Dezimalzahlen $\in \mathbb{Q}$, nicht-periodische $\in \mathbb{R} \setminus \mathbb{Q}$.

## 2. Terme

Ein **Term** ist ein mathematischer Ausdruck, der aus Zahlen, Variablen und Rechenoperationen besteht. Terme haben (im Gegensatz zu Gleichungen) **kein Gleichheitszeichen**.

**Beispiele für Terme:** $\quad 3x + 5, \quad 2a^2 - 4ab + b^2, \quad \frac{x+1}{x-2}$

### Terme vereinfachen

**Gleichartige Glieder zusammenfassen** - nur Terme mit identischen Variablen und Exponenten:

$$
3x + 5x - 2x = 6x \qquad\qquad 4a^2 + 3a - 2a^2 + a = 2a^2 + 4a
$$

**Ausmultiplizieren** (Distributivgesetz):
$$
a(b + c) = ab + ac
$$

$$
3x(2x - 4) = 6x^2 - 12x
$$

**Klammern auflösen bei Multiplikation** von zwei Klammern ("jeder mit jedem"):
$$
(a + b)(c + d) = ac + ad + bc + bd
$$

$$
(x+3)(x-2) = x^2 - 2x + 3x - 6 = x^2 + x - 6
$$

### Binomische Formeln

Diese drei Identitäten tauchen so häufig auf, dass sie auswendig sitzen sollten - nicht nur *vorwärts* zum Ausmultiplizieren, sondern auch *rückwärts* zum Erkennen und Faktorisieren. Du wirst ihnen in quadratischen Gleichungen, Ableitungen und Integralen immer wieder begegnen:

| Nr. | Formel | Bezeichnung |
|-----|--------|-------------|
| 1. | $(a + b)^2 = a^2 + 2ab + b^2$ | Erste binomische Formel |
| 2. | $(a - b)^2 = a^2 - 2ab + b^2$ | Zweite binomische Formel |
| 3. | $(a + b)(a - b) = a^2 - b^2$ | Dritte binomische Formel |

**Beispiele - vorwärts (Ausmultiplizieren):**

$$
(x + 5)^2 = x^2 + 10x + 25
$$
$$
(3a - 2b)^2 = 9a^2 - 12ab + 4b^2
$$
$$
(x + 7)(x - 7) = x^2 - 49
$$

**Beispiele - rückwärts (Erkennen und Faktorisieren):**

$$
x^2 + 6x + 9 = (x + 3)^2
$$
$$
4y^2 - 25 = (2y + 5)(2y - 5)
$$

> **Tipp:** Die dritte binomische Formel rückwärts erkennt man an einer *Differenz zweier Quadrate*.

### Faktorisieren (Ausklammern)

Das Gegenteil vom Ausmultiplizieren: Gemeinsame Faktoren vor die Klammer setzen.

**Schritt 1:** Größten gemeinsamen Faktor (ggT) aller Terme finden.

$$
6x^3 + 9x^2 = 3x^2(2x + 3)
$$

**Schritt 2:** Prüfen, ob eine binomische Formel anwendbar ist.

$$
x^2 - 16 = (x+4)(x-4) \qquad \text{(3. binom. Formel)}
$$

**Schritt 3:** Ggf. Gruppierung versuchen.

$$
ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)
$$

### Bruchterme

Für Terme mit Variablen im Nenner gelten dieselben Regeln wie für Zahlenbrüche, **plus** eine wichtige Einschränkung:

> Der Nenner darf **nie** Null werden. $\frac{1}{x-3}$ ist definiert für alle $x \neq 3$.

**Kürzen** von Bruchtermen - nur Faktoren, nie einzelne Summanden:

$$
\frac{x^2 - 9}{x + 3} = \frac{(x+3)(x-3)}{x+3} = x - 3 \qquad (x \neq -3)
$$

$$
\frac{x + 3}{x + 5} \neq \frac{3}{5} \qquad \text{(FALSCH! Man darf } x \text{ nicht einzeln kürzen)}
$$

## 3. Prozentrechnung

Prozent bedeutet "von Hundert": $p\% = \frac{p}{100}$

### Grundformel

$$
W = G \cdot \frac{p}{100}
$$

| Größe | Bedeutung | Formel |
|-------|-----------|--------|
| $G$ | Grundwert (100%) | $G = \frac{W}{p} \cdot 100$ |
| $W$ | Prozentwert | $W = G \cdot \frac{p}{100}$ |
| $p$ | Prozentsatz | $p = \frac{W}{G} \cdot 100$ |

**Beispiel:** 20% von 350€:  $W = 350 \cdot \frac{20}{100} = 70$€

### Prozentuale Änderung

$$
\text{Änderung in \%} = \frac{\text{neu} - \text{alt}}{\text{alt}} \cdot 100
$$

**Beispiel:** Preis steigt von 80€ auf 92€: $\frac{92-80}{80} \cdot 100 = 15\%$

> **Achtung:** 20% Erhöhung und dann 20% Rabatt ergibt **nicht** den Originalpreis!  
> $100 \xrightarrow{+20\%} 120 \xrightarrow{-20\%} 96 \neq 100$

---

    ==================================================
    Verifikation: Bruchrechnung
    ==================================================
    
      2/3 + 1/4 = 11/12
      2/3 - 1/4 = 5/12
      2/3 × 1/4 = 1/6
      2/3 ÷ 1/4 = 8/3
    
      12/18 gekürzt = 2/3  ✓
      35/49 gekürzt = 5/7  ✓
    
      (3/4) ÷ (5/6) = 9/10  ✓
    
    ==================================================
    Verifikation: Binomische Formeln
    ==================================================
    
      a=7, b=3
      1. BF: (a+b)² = 100  |  a²+2ab+b² = 100  ✓
      2. BF: (a-b)² = 16  |  a²-2ab+b² = 16  ✓
      3. BF: (a+b)(a-b) = 40  |  a²-b² = 40  ✓
    

---

## Verständnis-Check

*Löse die folgenden Aufgaben auf Papier.*

**Aufgabe 1: Bruchrechnung**

Berechne und kürze vollständig:

a) $\frac{3}{5} + \frac{2}{7}$

b) $\frac{5}{6} - \frac{1}{4}$

c) $\frac{4}{9} \cdot \frac{3}{8}$

d) $\frac{7}{10} \div \frac{14}{5}$

e) $\frac{\frac{2}{3}}{\frac{4}{9}}$

**Aufgabe 2: Terme vereinfachen**

a) $5x + 3y - 2x + 7y$

b) $4a(3a - 2) - 2a(a + 5)$

c) $(2x + 1)(3x - 4)$

**Aufgabe 3: Binomische Formeln (vorwärts)**

Multipliziere aus:

a) $(x + 4)^2$

b) $(3a - 2b)^2$

c) $(5 + y)(5 - y)$

**Aufgabe 4: Faktorisieren (rückwärts)**

a) $x^2 + 8x + 16$

b) $9y^2 - 24y + 16$

c) $x^2 - 36$

d) $15x^3 - 10x^2 + 5x$

**Aufgabe 5: Bruchterme**

Kürze und vereinfache:

a) $\frac{x^2 - 4}{x + 2}$

b) $\frac{2x^2 + 6x}{4x}$

c) Für welche $x$ ist $\frac{x + 1}{x^2 - 1}$ nicht definiert?

**Aufgabe 6: Prozentrechnung**

a) Wie viel sind 35% von 240?

b) 72 ist welcher Prozentsatz von 300?

c) Ein Produkt kostet nach 15% Rabatt 170€. Was war der Originalpreis?

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $\frac{3}{5} + \frac{2}{7} = \frac{21 + 10}{35} = \frac{31}{35}$

b) $\frac{5}{6} - \frac{1}{4} = \frac{20 - 6}{24} = \frac{14}{24} = \frac{7}{12}$

c) $\frac{4}{9} \cdot \frac{3}{8} = \frac{12}{72} = \frac{1}{6}$

d) $\frac{7}{10} \div \frac{14}{5} = \frac{7}{10} \cdot \frac{5}{14} = \frac{35}{140} = \frac{1}{4}$

e) $\frac{\frac{2}{3}}{\frac{4}{9}} = \frac{2}{3} \cdot \frac{9}{4} = \frac{18}{12} = \frac{3}{2}$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

a) $5x + 3y - 2x + 7y = 3x + 10y$

b) $4a(3a-2) - 2a(a+5) = 12a^2 - 8a - 2a^2 - 10a = 10a^2 - 18a$

c) $(2x+1)(3x-4) = 6x^2 - 8x + 3x - 4 = 6x^2 - 5x - 4$
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

a) $(x+4)^2 = x^2 + 8x + 16$

b) $(3a-2b)^2 = 9a^2 - 12ab + 4b^2$

c) $(5+y)(5-y) = 25 - y^2$
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

a) $x^2 + 8x + 16 = (x + 4)^2$ (1. binomische Formel)

b) $9y^2 - 24y + 16 = (3y - 4)^2$ (2. binomische Formel)

c) $x^2 - 36 = (x + 6)(x - 6)$ (3. binomische Formel)

d) $15x^3 - 10x^2 + 5x = 5x(3x^2 - 2x + 1)$
</details>

<details open>
<summary>Lösung Aufgabe 5</summary>

a) $\frac{x^2 - 4}{x + 2} = \frac{(x+2)(x-2)}{x+2} = x - 2 \quad (x \neq -2)$

b) $\frac{2x^2 + 6x}{4x} = \frac{2x(x + 3)}{4x} = \frac{x + 3}{2} \quad (x \neq 0)$

c) $\frac{x+1}{x^2-1} = \frac{x+1}{(x+1)(x-1)}$ - nicht definiert für $x = 1$ und $x = -1$ (Nenner = 0).
</details>

<details open>
<summary>Lösung Aufgabe 6</summary>

a) $240 \cdot 0{,}35 = 84$

b) $\frac{72}{300} \cdot 100 = 24\%$

c) $G = \frac{170}{1 - 0{,}15} = \frac{170}{0{,}85} = 200$€
</details>

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Bruchrechnung | $+/-$: gemeinsamer Nenner nötig; $\cdot$: Zähler mal Zähler, Nenner mal Nenner; $\div$: mit Kehrwert multiplizieren |
| Kürzen & Erweitern | Nur mit gemeinsamen Faktoren kürzen, nie mit Summanden |
| Terme | Ausdrücke ohne Gleichheitszeichen; gleichartige Glieder zusammenfassen |
| Binomische Formeln | $(a+b)^2$, $(a-b)^2$, $(a+b)(a-b)$ - vorwärts und rückwärts beherrschen |
| Faktorisieren | Ausklammern, binomische Formeln rückwärts, Gruppierung |
| Bruchterme | Nenner $\neq 0$ beachten; nur Faktoren kürzen |
| Prozentrechnung | $W = G \cdot \frac{p}{100}$ - Grundwert, Prozentwert, Prozentsatz |

---

## Glossar

| Deutsch | English |
|---------|---------|
| Bruch | Fraction |
| Zähler | Numerator |
| Nenner | Denominator |
| Kürzen | Simplify / reduce |
| Erweitern | Expand (a fraction) |
| Gemeinsamer Nenner | Common denominator |
| ggT (größter gemeinsamer Teiler) | GCD (greatest common divisor) |
| kgV (kleinstes gemeinsames Vielfaches) | LCM (least common multiple) |
| Term | Expression |
| Ausmultiplizieren | Expand / distribute |
| Faktorisieren / Ausklammern | Factor / factorize |
| Binomische Formel | Binomial formula |
| Bruchterm | Rational expression |
| Prozentsatz | Percentage |
| Grundwert | Base value |
| Prozentwert | Percentage value |
