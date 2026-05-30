# Algebra
## 01 - Quadratische Gleichungen

Lösen von $ax^2 + bx + c = 0$ - Diskriminante $\Delta = b^2 - 4ac$, abc-Formel (Mitternachtsformel), quadratische Ergänzung, Satz von Vieta und biquadratische Gleichungen durch Substitution $u = x^2$.

> Vorausgesetzt: lineare Gleichungen, Äquivalenzumformungen.

### Lernziele

- Du kannst die **abc-Formel** (Mitternachtsformel) sicher anwenden.
- Du kennst die **Diskriminante** $\Delta = b^2 - 4ac$ und weißt, was sie über die Lösungsanzahl aussagt.
- Du beherrschst die **quadratische Ergänzung** als Lösungstechnik.
- Du kennst den **Satz von Vieta** und kannst ihn zur Probe und zum Lösen nutzen.
- Du kannst **biquadratische Gleichungen** durch Substitution auf quadratische zurückführen.

---

## 1. Grundfrom der quadratische Gleichung

Eine **quadratische Gleichung** hat die allgemeine Form:

$$
ax^2 + bx + c = 0, \quad a \neq 0
$$

Dabei heißt $a$ der **Leitkoeffizient**, $b$ der **lineare Koeffizient** und $c$ das **Absolutglied**.

**Sonderfall Reinform** ($b = 0$): $\quad ax^2 + c = 0 \implies x^2 = -\frac{c}{a}$

$$
x^2 = 9 \implies x = \pm 3 \qquad\qquad x^2 = -4 \implies \text{keine reelle Lösung}
$$

**Sonderfall** ($c = 0$): $\quad ax^2 + bx = 0 \implies x(ax + b) = 0$

$$
x_1 = 0 \quad \text{oder} \quad x_2 = -\frac{b}{a}
$$

> **Merke:** Teile nie durch $x$ - damit verliert man die Lösung $x = 0$. Immer ausklammern!

## 2. Die Diskriminante

Die **Diskriminante** $\Delta$ (griech. Delta) ist definiert als:

$$
\Delta = b^2 - 4ac
$$

Das Vorzeichen von $\Delta$ entscheidet, wie viele reelle Lösungen existieren - und damit auch, ob überhaupt eine Lösung gefunden werden kann. 

Ein negatives $\Delta$ bedeutet: keine reelle Lösung, alle weitere Rechnung erübrigt sich. Die geometrische Bedeutung (Parabel und x-Achse) wird klarer, wenn wir in Kapitel **Funktionen** die Parabel als Graph betrachten.

| Diskriminante | Anzahl der Lösungen | Bedeutung |
|---|---|---|
| $\Delta > 0$ | 2 verschiedene reelle Lösungen | Parabel schneidet x-Achse zweimal |
| $\Delta = 0$ | 1 Lösung (doppelte Nullstelle) | Parabel berührt x-Achse |
| $\Delta < 0$ | keine reelle Lösung | Parabel schneidet x-Achse nicht |

**Beispiele:**

$$
x^2 - 5x + 6 = 0: \quad \Delta = 25 - 24 = 1 > 0 \quad \Rightarrow \text{zwei Lösungen}
$$
$$
x^2 - 4x + 4 = 0: \quad \Delta = 16 - 16 = 0 \quad \Rightarrow \text{eine Lösung}
$$
$$
x^2 + x + 1 = 0: \quad \Delta = 1 - 4 = -3 < 0 \quad \Rightarrow \text{keine reelle Lösung}
$$


    
![png](01_Quadratische_Gleichungen_files/01_Quadratische_Gleichungen_3_0.png)
    


## 3. Die abc-Formel (Mitternachtsformel)

Für $ax^2 + bx + c = 0$ gilt:

$$
\boxed{x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}
$$

Sie heißt **Mitternachtsformel**, weil man sie auch um Mitternacht auswendig wissen sollte (das ist wirklich der Grund).

**Beispiel 1:** $\quad 2x^2 - 5x - 3 = 0$

$$
\Delta = (-5)^2 - 4 \cdot 2 \cdot (-3) = 25 + 24 = 49
$$
$$
x_{1,2} = \frac{5 \pm \sqrt{49}}{4} = \frac{5 \pm 7}{4}
\implies x_1 = \frac{12}{4} = 3, \quad x_2 = \frac{-2}{4} = -\frac{1}{2}
$$

**Probe:** $\quad 2(3)^2 - 5(3) - 3 = 18 - 15 - 3 = 0$ ✓ $\quad$ und $\quad 2(-\tfrac{1}{2})^2 - 5(-\tfrac{1}{2}) - 3 = \tfrac{1}{2} + \tfrac{5}{2} - 3 = 0$ ✓

**Beispiel 2:** $\quad x^2 - 6x + 9 = 0$

$$
\Delta = 36 - 36 = 0 \implies x_{1,2} = \frac{6}{2} = 3 \quad \text{(doppelte Nullstelle)}
$$

**Sonderfall pq-Formel** (wenn $a = 1$): $\quad x^2 + px + q = 0$

$$
x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q}
$$

**Beispiel:** $\quad x^2 - 5x + 6 = 0 \implies x_{1,2} = \frac{5}{2} \pm \sqrt{\frac{25}{4} - 6} = \frac{5}{2} \pm \frac{1}{2} \implies x_1 = 3,\ x_2 = 2$

## 4. Quadratische Ergänzung als Lösungstechnik

Die **quadratische Ergänzung** ist eine alternative Lösungsmethode und liefert automatisch den Rechenweg zur abc-Formel. Außerdem ist sie die Grundlage der Scheitelpunktform (→ Kapitel **Funktionen**).

**Idee:** Forme $ax^2 + bx + c = 0$ so um, dass links ein vollständiges Quadrat steht, dann ziehe die Wurzel.

**Rezept für $a = 1$:** $\quad x^2 + px + q = 0$

$$
x^2 + px = -q \qquad\text{(Konstanten nach rechts bringen)}
$$
$$
x^2 + px + \left(\frac{p}{2}\right)^2 = -q + \left(\frac{p}{2}\right)^2 \qquad\text{(quadratische Ergänzung: $\left(\frac{p}{2}\right)^2$ auf beiden Seiten)}
$$
$$
\left(x + \frac{p}{2}\right)^2 = \left(\frac{p}{2}\right)^2 - q \qquad\text{(linke Seite als vollständiges Quadrat schreiben)}
$$
$$
x + \frac{p}{2} = \pm\sqrt{\left(\frac{p}{2}\right)^2 - q} \;\Longrightarrow\; x_{1,2} = -\frac{p}{2} \pm \sqrt{\left(\frac{p}{2}\right)^2 - q} \qquad\text{(Wurzel ziehen, nach $x$ auflösen)}
$$

**Beispiel:** $\quad x^2 + 6x + 5 = 0$

$$
x^2 + 6x = -5 \qquad\text{(Konstanten $+5$ nach rechts)}
$$
$$
x^2 + 6x + 9 = -5 + 9 = 4 \qquad\text{(Ergänzung: $(6/2)^2 = 9$)}
$$
$$
(x + 3)^2 = 4 \;\Longrightarrow\; x + 3 = \pm 2 \;\Longrightarrow\; x_1 = -1,\; x_2 = -5 \qquad\text{(Wurzel $\to$ zwei Lösungen)}
$$

**Beispiel mit $a \neq 1$:** $\quad 3x^2 - 12x + 9 = 0$

Zunächst durch $a = 3$ dividieren: $\quad x^2 - 4x + 3 = 0$

$$
x^2 - 4x = -3 \qquad\text{(Konstanten nach rechts)}
$$
$$
(x - 2)^2 = -3 + 4 = 1 \;\Longrightarrow\; x - 2 = \pm 1 \;\Longrightarrow\; x_1 = 3,\; x_2 = 1 \qquad\text{(Ergänzung $(4/2)^2 = 4$, dann Wurzel)}
$$

> **Merke:** Ergänze immer den Term $\left(\frac{p}{2}\right)^2$ auf **beiden Seiten** der Gleichung.

## 5. Satz von Vieta

Der Satz von Vieta stellt eine direkte Beziehung zwischen den Lösungen einer Gleichung und ihren Koeffizienten her - ohne dass man die Lösungen selbst berechnet haben muss. 

Das kann zur schnellen Probe, aber auch zum Lösen von Gleichungen durch Raten genutzt werden.

Sind $x_1$ und $x_2$ die Lösungen von $x^2 + px + q = 0$, dann gilt:

$$
\boxed{x_1 + x_2 = -p \qquad x_1 \cdot x_2 = q}
$$

Für die allgemeine Form $ax^2 + bx + c = 0$:

$$
x_1 + x_2 = -\frac{b}{a} \qquad x_1 \cdot x_2 = \frac{c}{a}
$$

**Herleitung:** Wenn $x_1, x_2$ die Nullstellen sind, dann lässt sich das Polynom faktorisieren:

$$
x^2 + px + q = (x - x_1)(x - x_2) = x^2 - (x_1 + x_2)x + x_1 x_2
$$

Koeffizientenvergleich liefert $x_1 + x_2 = -p$ und $x_1 x_2 = q$.

**Anwendung - Lösen durch Raten:** Bei $x^2 + px + q = 0$ suche zwei Zahlen, deren **Summe** $-p$ und deren **Produkt** $q$ ist.

**Beispiel:** $\quad x^2 - 7x + 12 = 0$

Gesucht: $x_1 + x_2 = 7$ und $x_1 \cdot x_2 = 12 \implies$ Kandidaten: $3$ und $4$ ✓

$$
\implies x_1 = 3, \quad x_2 = 4
$$

**Probe mit Vieta:** $\quad 3 + 4 = 7 = -(-7)$ ✓ $\quad$ und $\quad 3 \cdot 4 = 12$ ✓

> **Merke:** Vieta eignet sich perfekt als schnelle **Probe** nach der abc-Formel. Einfach Summe und Produkt der Lösungen nachrechnen.

## 6. Biquadratische Gleichungen (Substitution)

Eine **biquadratische Gleichung** hat die Form:

$$
ax^4 + bx^2 + c = 0, \quad a \neq 0
$$

**Lösungsstrategie:** Substitution $u = x^2$ reduziert sie auf eine quadratische Gleichung in $u$:

$$
au^2 + bu + c = 0
$$

**Vorgehen:**

1. Substituiere $u = x^2$, löse die quadratische Gleichung in $u$.
2. Rücksubstitution: $x^2 = u_i \implies x = \pm\sqrt{u_i}$ (nur wenn $u_i \geq 0$!)
3. Negative $u_i$ liefern keine reellen Lösungen.

**Beispiel:** $\quad x^4 - 5x^2 + 4 = 0$

**Schritt 1:** Substitution $u = x^2$:

$$
u^2 - 5u + 4 = 0 \implies (u - 1)(u - 4) = 0 \implies u_1 = 1, \quad u_2 = 4
$$

**Schritt 2:** Rücksubstitution:

$$
x^2 = 1 \implies x_{1,2} = \pm 1 \qquad x^2 = 4 \implies x_{3,4} = \pm 2
$$

**Beispiel mit negativer Teillösung:** $\quad x^4 - 3x^2 - 4 = 0$

$$
u^2 - 3u - 4 = 0 \implies u_1 = 4, \quad u_2 = -1
$$

$u_2 = -1 < 0$ → keine reellen Lösungen daraus. Nur $u_1 = 4$ liefert $x = \pm 2$.

> **Merke:** Die Substitution $u = x^2$ funktioniert immer dann, wenn nur gerade Potenzen von $x$ auftreten.

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Grundform | $ax^2 + bx + c = 0$, Sonderfälle bei $b=0$ oder $c=0$ |
| Diskriminante | $\Delta = b^2 - 4ac$ bestimmt Anzahl reeller Lösungen |
| abc-Formel | $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$ - universelle Lösungsformel |
| Quadratische Ergänzung | Umformung zum vollständigen Quadrat, Basis der Scheitelpunktform |
| Satz von Vieta | $x_1 + x_2 = -\frac{b}{a}$, $x_1 \cdot x_2 = \frac{c}{a}$ - ideal für Probe und Raten |
| Biquadratische Gleichungen | Substitution $u = x^2$ reduziert $ax^4 + bx^2 + c = 0$ auf Quadratische |

---

## Glossar

| Deutsch | English |
|---------|---------|
| Quadratische Gleichung | Quadratic equation |
| Leitkoeffizient | Leading coefficient |
| Diskriminante | Discriminant |
| Mitternachtsformel / abc-Formel | Quadratic formula |
| pq-Formel | pq-formula |
| Quadratische Ergänzung | Completing the square |
| Doppelte Nullstelle | Double root / repeated root |
| Nullstelle | Root / zero |
| Satz von Vieta | Vieta's formulas |
| Biquadratische Gleichung | Biquadratic equation |
| Substitution | Substitution |
| Rücksubstitution | Back-substitution |
| Probe | Verification / check |
