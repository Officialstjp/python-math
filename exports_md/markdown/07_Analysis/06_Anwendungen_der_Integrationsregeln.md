# Analysis
## 06 – Integrationsregeln und Anwendungen

**Voraussetzungen:** [05_Integralrechnung_Einfuehrung](05_Integralrechnung_Einfuehrung.ipynb), [03_Ableitungsregeln](03_Ableitungsregeln.ipynb)

---

### Lernziele

Nach diesem Abschnitt kannst du:

- **Substitution** anwenden, um verkettete Funktionen zu integrieren
- **Partielle Integration** für Produkte einsetzen
- **Flächen zwischen zwei Kurven** berechnen
- Typische Integrale der Matura sicher lösen

### 1. Integration durch Substitution

Die Substitution ist das Gegenstück zur **Kettenregel** beim Ableiten.

> **Idee:** Ersetze einen komplizierten Ausdruck durch eine neue Variable $u$, integriere einfacher, und setze zurück.

**Formel:**

$$\int f(g(x)) \cdot g'(x)\, dx = \int f(u)\, du \quad \text{mit } u = g(x)$$

**Schritt-für-Schritt:**
1. Wähle $u = g(x)$ (der „innere Teil")
2. Berechne $\frac{du}{dx} = g'(x)$ und forme um zu $du = g'(x)\, dx$
3. Ersetze im Integral: $\int f(g(x)) \cdot g'(x)\, dx = \int f(u)\, du$
4. Integriere nach $u$
5. Rücksubstitution: Setze $u = g(x)$ wieder ein

---

**Beispiel 1:** $\displaystyle\int 2x \cdot e^{x^2}\, dx$

1. Setze $u = x^2$
2. $\frac{du}{dx} = 2x \Rightarrow du = 2x\, dx$
3. Das Integral wird: $\int e^u\, du$
4. Integrieren: $e^u + C$
5. Rücksubstitution: $e^{x^2} + C$ ✓

**Beispiel 2:** $\displaystyle\int \cos(3x)\, dx$

1. Setze $u = 3x$
2. $\frac{du}{dx} = 3 \Rightarrow dx = \frac{du}{3}$
3. Das Integral wird: $\int \cos(u) \cdot \frac{1}{3}\, du = \frac{1}{3}\int \cos(u)\, du$
4. Integrieren: $\frac{1}{3}\sin(u) + C$
5. Rücksubstitution: $\frac{1}{3}\sin(3x) + C$ ✓

---

### Substitution bei bestimmten Integralen

Bei bestimmten Integralen **müssen auch die Grenzen angepasst** werden!

**Beispiel:** $\displaystyle\int_0^2 x(x^2+1)^3\, dx$

1. Setze $u = x^2 + 1$
2. $du = 2x\, dx \Rightarrow x\, dx = \frac{du}{2}$
3. **Grenzen anpassen:**
   - $x = 0 \Rightarrow u = 0^2 + 1 = 1$
   - $x = 2 \Rightarrow u = 2^2 + 1 = 5$
4. Integral: $\displaystyle\int_1^5 u^3 \cdot \frac{1}{2}\, du = \frac{1}{2}\left[\frac{u^4}{4}\right]_1^5 = \frac{1}{8}(625 - 1) = 78$

### 2. Partielle Integration

Die partielle Integration ist das Gegenstück zur **Produktregel** beim Ableiten.

> **Formel:**
> $$\int u(x) \cdot v'(x)\, dx = u(x) \cdot v(x) - \int u'(x) \cdot v(x)\, dx$$

Kurz: $\int u\, dv = uv - \int v\, du$

**Wann anwenden?** Diese Regel ist angebracht, wenn ein Produkt zweier Funktionen unterschiedlichen Typs integriert werden soll, und weder Substitution noch andere Vereinfachungen möglich sind.

**Strategie - LIATE-Regel** (wähle $u$ nach dieser Priorität):

| Priorität | Typ | Beispiel |
|-----------|-----|----------|
| 1 | **L**ogarithmus | $\ln x$ |
| 2 | **I**nverse Trig | $\arctan x$ |
| 3 | **A**lgebraisch | $x^2, x, 3x+1$ |
| 4 | **T**rigonometrisch | $\sin x, \cos x$ |
| 5 | **E**xponentiell | $e^x$ |

---

**Beispiel:** $\displaystyle\int x \cdot e^x\, dx$

| Wahl | |
|------|---|
| $u = x$ | $u' = 1$ |
| $v' = e^x$ | $v = e^x$ |

$$\int x \cdot e^x\, dx = x \cdot e^x - \int 1 \cdot e^x\, dx = x e^x - e^x + C = e^x(x-1) + C$$

---

**Beispiel:** $\displaystyle\int \ln x\, dx$

| Wahl | |
|------|---|
| $u = \ln x$ | $u' = \frac{1}{x}$ |
| $v' = 1$ | $v = x$ |

$$\int \ln x\, dx = x \ln x - \int x \cdot \frac{1}{x}\, dx = x \ln x - x + C$$

### 3. Überblick: Welche Methode wann?

| Integraltyp | Methode | Beispiel |
|-------------|---------|----------|
| Grundintegral | Tabelle | $\int x^3\, dx$ |
| Lineares Argument | Schnelle Substitution | $\int e^{2x}\, dx = \frac{1}{2}e^{2x}$ |
| Verkettung mit $g'(x)$ sichtbar | Substitution | $\int 2x \cdot e^{x^2}\, dx$ |
| Produkt (verschiedene Typen) | Partielle Integration | $\int x \cdot e^x\, dx$ |
| Bruch mit Polynomen | Polynomdivision + Partialbrüche | $\int \frac{x^2}{x-1}\, dx$ |
| $\frac{0}{0}$-Form (Bruch, vereinfachbar) | Kürzen, dann integrieren | $\int \frac{x^2-1}{x-1}\, dx$ |

> *Hinweis:* In der Matura sind meist Substitution und partielle Integration die wichtigsten Techniken.

### 4. Fläche zwischen zwei Kurven

Die Fläche zwischen $f(x)$ (oben) und $g(x)$ (unten) auf $[a, b]$:

$$A = \int_a^b [f(x) - g(x)]\, dx$$

**Schritt-für-Schritt:**
1. Schnittpunkte finden: $f(x) = g(x)$
2. Bestimme, welche Funktion oben/unten liegt
3. Integriere die Differenz

**Beispiel:** Fläche zwischen $f(x) = -x^2 + 4$ und $g(x) = x^2 - 2x$

Schnittpunkte: $-x^2 + 4 = x^2 - 2x \Rightarrow 2x^2 - 2x - 4 = 0 \Rightarrow x = -1$ oder $x = 2$


    
![png](06_Anwendungen_der_Integrationsregeln_files/06_Anwendungen_der_Integrationsregeln_7_0.png)
    


### 5. Anwendungen der Integralrechnung

| Anwendung | Formel |
|-----------|--------|
| **Fläche unter Kurve** | $A = \int_a^b f(x)\, dx$ |
| **Fläche zwischen Kurven** | $A = \int_a^b [f(x) - g(x)]\, dx$ |
| **Mittlerer Funktionswert** | $\bar{f} = \frac{1}{b-a} \int_a^b f(x)\, dx$ |
| **Weg aus Geschwindigkeit** | $s(t) = \int_0^t v(\tau)\, d\tau$ |
| **Gesamtmenge aus Rate** | $\text{Menge} = \int_0^T \text{Rate}(t)\, dt$ |

---

**Beispiel: Mittlerer Funktionswert**

Die Durchschnittstemperatur von $T(t) = 20 + 5\sin\left(\frac{\pi t}{12}\right)$ über 24 Stunden:

$$\bar{T} = \frac{1}{24}\int_0^{24} \left[20 + 5\sin\left(\frac{\pi t}{12}\right)\right] dt$$


    
![png](06_Anwendungen_der_Integrationsregeln_files/06_Anwendungen_der_Integrationsregeln_9_0.png)
    


---

## Zusammenfassung

| Methode | Wann? | Formel |
|---------|-------|--------|
| **Substitution** | Verkettung $f(g(x)) \cdot g'(x)$ | $u = g(x)$, integriere nach $u$ |
| **Lineare Sub.** | Argument $ax+b$ | $\frac{1}{a}F(ax+b) + C$ |
| **Partielle Int.** | Produkt verschiedener Typen | $\int u\, dv = uv - \int v\, du$ |
| **Fläche zw. Kurven** | Eingeschlossene Fläche | $\int_a^b [f(x)-g(x)]\, dx$ |
| **Mittelwert** | Durchschnittswert von $f$ | $\frac{1}{b-a}\int_a^b f(x)\, dx$ |

> **Die Analysis-Reihe ist nun abgeschlossen!** Du beherrschst die Kernthemen: Grenzwerte → Ableitungen → Ableitungsregeln → Kurvendiskussion → Integration → Integrationsregeln → Partielle Ableitungen.

---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Substitution | Substitution / u-substitution |
| Partielle Integration | Integration by parts |
| Verkettung | Composition |
| Rücksubstitution | Back-substitution |
| Fläche zwischen Kurven | Area between curves |
| Mittlerer Funktionswert | Average value of a function |
| Partialbruchzerlegung | Partial fraction decomposition |
