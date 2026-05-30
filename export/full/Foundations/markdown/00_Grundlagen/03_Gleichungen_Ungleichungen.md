# Grundlagen
## 03 - Gleichungen & Ungleichungen

Lineare Gleichungen mit Äquivalenzumformungen, Ungleichungen, Betragsgleichungen und lineare Gleichungssysteme lösen.

> Vorausgesetzt: Termumformungen, Bruchrechnung.

### Lernziele

- Du kannst **lineare Gleichungen** sicher lösen und Äquivalenzumformungen begründen.
- Du verstehst **Ungleichungen** und die Besonderheit beim Multiplizieren mit negativen Zahlen.
- Du beherrschst den **Betrag** $|x|$ und kannst Betragsgleichungen/-ungleichungen lösen.
- Du kennst **Intervallschreibweise** und kannst Lösungsmengen korrekt angeben.
- Du kannst einfache **Systeme linearer Gleichungen** (2 Unbekannte) lösen.

---

## 1. Äquivalenzumformungen

Eine Gleichung bleibt **äquivalent** (hat dieselbe Lösungsmenge), wenn man auf **beiden Seiten** dieselbe Operation durchführt:

| Erlaubt | Einschränkung |
|---------|---------------|
| $+ c$ oder $- c$ auf beiden Seiten | keine |
| $\cdot c$ oder $\div c$ auf beiden Seiten | $c \neq 0$ |
| Quadrieren, Wurzelziehen | kann Scheinlösungen erzeugen → **Probe!** |

> **Merke:** Dividiere nie durch einen Ausdruck, der Null sein könnte, ohne diesen Fall separat zu prüfen.

---

## 2. Lineare Gleichungen

Allgemeine Form: $ax + b = 0 \quad (a \neq 0)$

Lösung: $x = -\frac{b}{a}$

**Beispiel:**

$$
3x - 7 = 2x + 5
$$
$$
3x - 2x = 5 + 7
$$
$$
x = 12
$$

**Beispiel mit Brüchen:**

$$
\frac{x+1}{3} = \frac{2x-1}{5}
$$

Kreuzweise multiplizieren (oder kgV = 15):

$$
5(x+1) = 3(2x-1) \implies 5x + 5 = 6x - 3 \implies x = 8
$$

### Sonderfälle

Manchmal fallen beim Vereinfachen alle Variablen weg. Das Ergebnis sagt dir sofort, was mit der Lösungsmenge passiert:

- **Unendlich viele Lösungen:** Es bleibt eine *wahre* Aussage übrig.  
  $2(x+1) = 2x + 2 \implies 2 = 2$ - gilt immer. $\mathbb{L} = \mathbb{R}$

- **Keine Lösung:** Es bleibt eine *falsche* Aussage übrig.  
  $2x + 3 = 2x + 7 \implies 3 = 7$ - niemals wahr. $\mathbb{L} = \emptyset$

## 3. Lineare Gleichungssysteme (2 Variablen)

Zwei Gleichungen, zwei Unbekannte - gesucht ist das Wertepaar $(x, y)$, das **beide** Gleichungen gleichzeitig erfüllt:

$$
\begin{cases}
a_1 x + b_1 y = c_1 \\
a_2 x + b_2 y = c_2
\end{cases}
$$

Geometrisch: Jede lineare Gleichung beschreibt eine **Gerade**. Die Lösung ist der **Schnittpunkt**.

### Einsetzungsverfahren

**Idee:** Eine Gleichung nach einer Variablen auflösen, in die andere einsetzen.

**Beispiel:**

$$
\begin{cases}
x + 2y = 7 \quad (I) \\
3x - y = 7 \quad (II)
\end{cases}
$$

**Schritt 1:** $(I)$ nach $x$ auflösen: $\quad x = 7 - 2y$

**Schritt 2:** In $(II)$ einsetzen:

$$
3(7 - 2y) - y = 7 \implies 21 - 6y - y = 7 \implies -7y = -14 \implies y = 2
$$

**Schritt 3:** Rückeinsetzen: $\quad x = 7 - 2(2) = 3$

**Lösung:** $(x, y) = (3, 2)$

**Probe:** $3 + 2 \cdot 2 = 7$ ✓ und $3 \cdot 3 - 2 = 7$ ✓

> **Wann?** Gut geeignet, wenn eine Variable schon alleine steht oder den Koeffizienten $1$ hat.

### Additionsverfahren (Eliminationsverfahren)

**Idee:** Gleichungen so multiplizieren und addieren/subtrahieren, dass eine Variable wegfällt.

**Beispiel 1 - Koeffizienten passen direkt:**

$$
\begin{cases}
2x + 3y = 12 \quad (I) \\
4x - 3y = 6 \quad (II)
\end{cases}
$$

Die $y$-Koeffizienten sind $+3$ und $-3$ - Addition eliminiert $y$ direkt:

$$
(I) + (II): \quad 6x = 18 \implies x = 3
$$

Rückeinsetzen in $(I)$: $\quad 2(3) + 3y = 12 \implies 3y = 6 \implies y = 2$

**Lösung:** $(x, y) = (3, 2)$

**Beispiel 2 - vorher multiplizieren:**

$$
\begin{cases}
3x + 2y = 16 \quad (I) \\
5x + 3y = 26 \quad (II)
\end{cases}
$$

Ziel: $y$ eliminieren. Koeffizienten $2$ und $3$ → kgV ist $6$:

$$
(I) \cdot 3: \quad 9x + 6y = 48
$$
$$
(II) \cdot (-2): \quad -10x - 6y = -52
$$

Addition: $\quad -x = -4 \implies x = 4$

Rückeinsetzen: $\quad 3(4) + 2y = 16 \implies 2y = 4 \implies y = 2$

**Lösung:** $(x, y) = (4, 2)$

> **Wann?** Standard-Verfahren, wenn Koeffizienten sich leicht ergänzen lassen. Häufigstes Verfahren bei der Matura.

### Gleichsetzungsverfahren

**Idee:** Beide Gleichungen nach derselben Variablen auflösen, dann gleichsetzen.

$$
\begin{cases}
y = 2x - 1 \\
y = -x + 5
\end{cases}
$$

Gleichsetzen: $\quad 2x - 1 = -x + 5 \implies 3x = 6 \implies x = 2, \quad y = 2(2) - 1 = 3$

> Besonders praktisch, wenn beide Gleichungen schon nach $y$ (oder $x$) aufgelöst sind.

### Sonderfälle bei LGS

| Situation | Geometrisch | Erkennungsmerkmal |
|-----------|-------------|-------------------|
| Genau eine Lösung | Geraden schneiden sich | Normaler Lösungsweg liefert $(x_0, y_0)$ |
| Keine Lösung | Geraden sind parallel | Variablen fallen weg, falsche Aussage ($0 = 5$) |
| Unendlich viele Lösungen | Geraden sind identisch | Variablen fallen weg, wahre Aussage ($0 = 0$) |

**Beispiel - keine Lösung:** $\begin{cases} x + y = 1 \\ x + y = 3 \end{cases}$ → Subtraktion ergibt $0 = -2$ ✗

## 4. Ungleichungen

Ungleichungen begegnen dir überall dort, wo es nicht um einen exakten Wert geht, sondern um einen **Bereich** - Toleranzen in der Technik, Definitionsbereiche von Funktionen, Konvergenzbedingungen in der Analysis. Das Lösen funktioniert wie bei Gleichungen, mit **einer wichtigen Ausnahme**:

> Beim Multiplizieren oder Dividieren mit einer **negativen Zahl** dreht sich das Ungleichungszeichen um!

$$
a < b \quad \xrightarrow{\cdot(-1)} \quad -a > -b
$$

**Beispiel:**

$$
-3x + 6 > 0 \implies -3x > -6 \implies x < 2
$$

**Doppelungleichung:**

$$
-1 \leq 2x + 3 < 7 \implies -4 \leq 2x < 4 \implies -2 \leq x < 2
$$

## 5. Betrag

Der **Absolutbetrag** gibt den Abstand einer Zahl zum Nullpunkt an:

$$
|x| = \begin{cases} x & \text{wenn } x \geq 0 \\ -x & \text{wenn } x < 0 \end{cases}
$$

**Beispiele:** $|5| = 5, \quad |-3| = 3, \quad |0| = 0$

### Wichtige Eigenschaft

$$
|a \cdot b| = |a| \cdot |b| \qquad\qquad |a + b| \leq |a| + |b| \quad \text{(Dreiecksungleichung)}
$$

> Die **Dreiecksungleichung** klingt abstrakt, ist aber fundamental: Der direkte Abstand zwischen zwei Werten kann nie größer sein als der Umweg über einen Zwischenpunkt. In der Analysis taucht sie in fast jedem Konvergenzbeweis auf - in Kapitel 07 wirst du sie wiedersehen.

### Betragsgleichungen

$|x| = a$ (mit $a \geq 0$) hat **zwei Lösungen**: $x = a$ oder $x = -a$

**Beispiel:**
$$
|2x - 5| = 3
$$
$$
\text{Fall 1: } 2x - 5 = 3 \implies x = 4
$$
$$
\text{Fall 2: } 2x - 5 = -3 \implies x = 1
$$

### Betragsungleichungen

$$
|x| < a \quad \Longleftrightarrow \quad -a < x < a
$$
$$
|x| > a \quad \Longleftrightarrow \quad x < -a \text{ oder } x > a
$$

**Beispiel:** $|x - 2| \leq 5 \implies -5 \leq x - 2 \leq 5 \implies -3 \leq x \leq 7$

## 6. Intervall-Schreibweise

Lösungsmengen von Ungleichungen schreibt man oft als **Intervalle**:

| Notation | Bedeutung | Beschreibung |
|----------|-----------|-------------|
| $[a, b]$ | $a \leq x \leq b$ | Abgeschlossenes Intervall (Grenzen inklusive) |
| $(a, b)$ | $a < x < b$ | Offenes Intervall (Grenzen exklusive) |
| $[a, b)$ | $a \leq x < b$ | Halboffen (links geschlossen, rechts offen) |
| $(a, b]$ | $a < x \leq b$ | Halboffen (links offen, rechts geschlossen) |
| $(-\infty, a]$ | $x \leq a$ | Alles bis einschließlich $a$ |
| $[a, \infty)$ | $x \geq a$ | Alles ab einschließlich $a$ |

> $\infty$ ist **keine Zahl** - daher steht bei $\pm\infty$ immer eine runde Klammer.

**Beispiele:**

$$
-2 \leq x < 2 \quad \Longleftrightarrow \quad x \in [-2, 2)
$$

$$
x > 5 \quad \Longleftrightarrow \quad x \in (5, \infty)
$$

**Vereinigung und Schnitt:**

$$
x < -1 \text{ oder } x > 3 \quad \Longleftrightarrow \quad x \in (-\infty, -1) \cup (3, \infty)
$$

---

## Verständnis-Check

*Löse die folgenden Aufgaben auf Papier.*

**Aufgabe 1: Lineare Gleichungen**

Löse nach $x$:

a) $5x - 3 = 2x + 9$

b) $\frac{x}{2} + 3 = \frac{2x+1}{4}$

c) $7(x - 2) = 3(x + 6)$

**Aufgabe 2: Gleichungssysteme**

a) Löse mit dem Einsetzungsverfahren:

$$
\begin{cases}
3x + 2y = 16 \\
x - y = 2
\end{cases}
$$

b) Löse mit dem Additionsverfahren:

$$
\begin{cases}
2x + 5y = 16 \\
3x - 2y = 5
\end{cases}
$$

**Aufgabe 3: Ungleichungen**

Löse und gib die Lösungsmenge als Intervall an:

a) $4x - 5 > 7$

b) $-2x + 1 \leq 9$

c) $1 < 3x - 2 \leq 10$

**Aufgabe 4: Betrag**

a) Löse: $|3x + 1| = 7$

b) Löse: $|x - 4| < 2$

c) Löse: $|2x + 3| \geq 5$

**Aufgabe 5: Intervalle zuordnen**

Schreibe als Intervall:

a) $x \geq -3$

b) $-1 < x \leq 5$

c) $x < 0$ oder $x > 4$

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $5x - 3 = 2x + 9 \implies 3x = 12 \implies x = 4$

b) $\frac{x}{2} + 3 = \frac{2x+1}{4}$ - mit 4 multiplizieren: $2x + 12 = 2x + 1 \implies 12 = 1$ - **keine Lösung!** $\mathbb{L} = \{\}$

c) $7x - 14 = 3x + 18 \implies 4x = 32 \implies x = 8$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

**a) Einsetzungsverfahren:**

Aus Gleichung 2: $x = y + 2$. In Gleichung 1 einsetzen:

$3(y + 2) + 2y = 16 \implies 3y + 6 + 2y = 16 \implies 5y = 10 \implies y = 2$

Rückeinsetzen: $x = 2 + 2 = 4$

**Lösung:** $(x, y) = (4, 2)$

**b) Additionsverfahren:**

Ziel: $y$ eliminieren. Koeffizienten $5$ und $-2$ → kgV ist $10$.

$(I) \cdot 2$: $4x + 10y = 32$. $\quad (II) \cdot 5$: $15x - 10y = 25$.

Addition: $19x = 57 \implies x = 3$

Rückeinsetzen in $(I)$: $6 + 5y = 16 \implies y = 2$

**Lösung:** $(x, y) = (3, 2)$
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

a) $4x > 12 \implies x > 3 \implies x \in (3, \infty)$

b) $-2x \leq 8 \implies x \geq -4$ (Zeichen dreht!) $\implies x \in [-4, \infty)$

c) $1 < 3x - 2 \leq 10 \implies 3 < 3x \leq 12 \implies 1 < x \leq 4 \implies x \in (1, 4]$
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

a) $|3x+1| = 7$:
- Fall 1: $3x + 1 = 7 \implies x = 2$
- Fall 2: $3x + 1 = -7 \implies x = -\frac{8}{3}$

b) $|x - 4| < 2 \implies -2 < x - 4 < 2 \implies 2 < x < 6 \implies x \in (2, 6)$

c) $|2x + 3| \geq 5$:
- $2x + 3 \geq 5 \implies x \geq 1$
- $2x + 3 \leq -5 \implies x \leq -4$
- $x \in (-\infty, -4] \cup [1, \infty)$
</details>

<details open>
<summary>Lösung Aufgabe 5</summary>

a) $[-3, \infty)$

b) $(-1, 5]$

c) $(-\infty, 0) \cup (4, \infty)$
</details>

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Äquivalenzumformung | Dieselbe Operation auf beiden Seiten - Lösungsmenge bleibt gleich |
| Lineare Gleichungen | $ax + b = 0 \implies x = -b/a$; Sonderfälle: keine oder unendlich viele Lösungen |
| Gleichungssysteme | Einsetzungs-, Additions- oder Gleichsetzungsverfahren |
| Ungleichungen | Wie Gleichungen, aber Zeichen dreht bei Multiplikation mit negativer Zahl |
| Betrag | $\|x\| = a$ hat zwei Fälle; $\|x\| < a$ ergibt Intervall, $\|x\| > a$ ergibt Vereinigung |
| Intervalle | $[a,b]$ geschlossen, $(a,b)$ offen, Mischformen möglich; $\infty$ immer mit runder Klammer |

---

## Glossar

| Deutsch | English |
|---------|---------|
| Gleichung | Equation |
| Ungleichung | Inequality |
| Äquivalenzumformung | Equivalent transformation |
| Lösungsmenge | Solution set |
| Betrag / Absolutbetrag | Absolute value |
| Intervall | Interval |
| Abgeschlossen | Closed |
| Offen | Open |
| Halboffen | Half-open |
| Vereinigung | Union |
| Schnitt | Intersection |
| Gleichungssystem | System of equations |
| Einsetzungsverfahren | Substitution method |
| Additionsverfahren | Elimination method |
| Dreiecksungleichung | Triangle inequality |


