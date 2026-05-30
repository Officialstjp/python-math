# Analysis
## 05 - Integralrechnung: Einführung

Stammfunktion $F$ (mit $F' = f$), unbestimmtes Integral $\int f(x)dx = F(x) + C$, bestimmtes Integral $\int_a^b f(x)dx$ als orientierte Fläche unter der Kurve, Riemann-Summen und der Hauptsatz der Differential- und Integralrechnung: $\int_a^b f(x)dx = F(b) - F(a)$.

> Vorausgesetzt: Ableitungen.

### Lernziele

- Erklären, was eine **Stammfunktion** ist und wie sie mit der Ableitung zusammenhängt
- Das **unbestimmte Integral** berechnen und die Integrationskonstante begründen
- Das **bestimmte Integral** als Fläche unter einer Kurve interpretieren
- Den **Hauptsatz der Differential- und Integralrechnung** anwenden
- **Riemann-Summen** als Motivation für das Integral beschreiben

---

### 1. Von der Ableitung zurück: Die Stammfunktion

Bei der Ableitung fragten wir: *Gegeben $f(x)$, was ist $f'(x)$?*

Jetzt kehren wir die Frage um:

> **Stammfunktion:** $F(x)$ heißt Stammfunktion von $f(x)$, wenn $F'(x) = f(x)$.

**Beispiel:**
- $f(x) = 2x \quad\Rightarrow\quad F(x) = x^2 + C$
- Denn: $(x^2 + C)' = 2x$ ✓

**Warum $+C$?** Jede Konstante verschwindet beim Ableiten. Deshalb hat jede Funktion **unendlich viele** Stammfunktionen - sie unterscheiden sich nur um eine Konstante.

$$F_1(x) = x^2, \quad F_2(x) = x^2 + 5, \quad F_3(x) = x^2 - 3 \quad \text{alle sind Stammfunktionen von } 2x$$

---

### Das unbestimmte Integral

Die Schreibweise für „finde die Stammfunktion von $f(x)$“ ist:
$$\int f(x) \, dx = F(x) + C$$

| Symbol | Bedeutung |
|---|---|
| $f(x)$ | Integrand |
| $dx$ | Integrationsvariable |
| $F(x)$ | Stammfunktion |
| $C$ | Integrationskonstante |


    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_2_0.png)
    


### 2. Das bestimmte Integral: Fläche unter der Kurve

Während das unbestimmte Integral eine **Funktionsfamilie** liefert, berechnet das bestimmte Integral eine **Zahl** - die Fläche zwischen $f(x)$ und der $x$-Achse:

$$\int_a^b f(x)\, dx = \text{"Fläche unter } f(x) \text{ von } a \text{ bis } b\text{"}$$

**Wichtig:**
- Fläche **über** der $x$-Achse zählt **positiv**
- Fläche **unter** der $x$-Achse zählt **negativ** (orientierte Fläche)
- Für den tatsächlichen Flächeninhalt: $\displaystyle\int_a^b |f(x)|\, dx$

---

### Riemann-Summen: Die Idee dahinter

Wie berechnet man die Fläche unter einer Kurve? 
Riemann-Summen sind eine Methode, um das Integral zu approximieren:

1. Teile $[a,b]$ in $n$ gleich breite Streifen der Breite $\Delta x = \frac{b-a}{n}$
2. Wähle in jedem Streifen eine Höhe $f(x_i)$
3. Summiere: $\displaystyle S_n = \sum_{i=1}^{n} f(x_i) \cdot \Delta x$

Für $n \to \infty$ konvergiert die Summe zum exakten Integral:

$$\int_a^b f(x)\, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \cdot \Delta x$$


    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_4_0.png)
    


### 3. Der Hauptsatz der Differential- und Integralrechnung

Der **Hauptsatz** verbindet Ableitung und Integral - er ist *das* zentrale Ergebnis der Analysis:

> **Hauptsatz (HDI):** Ist $F$ eine Stammfunktion von $f$, dann gilt:
>
> $$\int_a^b f(x)\, dx = F(b) - F(a) = \bigl[F(x)\bigr]_a^b$$

**Das bedeutet:** Um eine Fläche zu berechnen, ist keine Riemann-Summe erforderlich - es genügt die Stammfunktion zu bestimmen!

**Beispiel:**

$$\int_0^3 x^2\, dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{27}{3} - \frac{0}{3} = 9$$

**Schritt für Schritt:**
1. Finde Stammfunktion: $F(x) = \frac{x^3}{3}$
2. Setze obere Grenze ein: $F(3) = 9$
3. Setze untere Grenze ein: $F(0) = 0$
4. Differenz: $F(3) - F(0) = 9$

---

### Was der Hauptsatz *wirklich* sagt

| Richtung | Aussage |
|----------|----------|
| **Integrieren hebt Ableiten auf** | $\displaystyle\int_a^b F'(x)\, dx = F(b) - F(a)$ |
| **Ableiten hebt Integrieren auf** | $\displaystyle\frac{d}{dx}\left(\int_a^x f(t)\, dt\right) = f(x)$ |

> *Hinweis:* Ableitung und Integration sind **Umkehroperationen** - wie Addition/Subtraktion oder Multiplikation/Division.


    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_6_0.png)
    


### 4. Grundintegrale - Die wichtigsten Stammfunktionen

Diese Tabelle ist grundlegend und sollte verinnerlicht werden (sie ergibt sich durch Umkehrung der Ableitungsregeln):

| $f(x)$ | $\int f(x)\, dx$ | Bedingung |
|---------|-------------------|----------|
| $x^n$ | $\dfrac{x^{n+1}}{n+1} + C$ | $n \ne -1$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert + C$ | $x \ne 0$ |
| $e^x$ | $e^x + C$ | |
| $a^x$ | $\dfrac{a^x}{\ln a} + C$ | $a > 0, a \ne 1$ |
| $\sin x$ | $-\cos x + C$ | |
| $\cos x$ | $\sin x + C$ | |
| $\dfrac{1}{\cos^2 x}$ | $\tan x + C$ | |

**Und die linearen Regeln:**

$$\int [f(x) \pm g(x)]\, dx = \int f(x)\, dx \pm \int g(x)\, dx$$

$$\int c \cdot f(x)\, dx = c \cdot \int f(x)\, dx$$

> *Hinweis:* Für Produkt und Quotient gibt es **keine** einfache Regel wie beim Ableiten - dafür braucht man Substitution und partielle Integration (→ nächstes Notebook).

### 5. Fläche unter und über der x-Achse

**Vorsicht:** Das bestimmte Integral kann **negativ** werden!

$$\int_0^\pi \sin x\, dx = 2 \qquad \text{(positiv - Fläche über x-Achse)}$$

$$\int_\pi^{2\pi} \sin x\, dx = -2 \qquad \text{(negativ - Fläche unter x-Achse)}$$

$$\int_0^{2\pi} \sin x\, dx = 0 \qquad \text{(Flächen heben sich auf!)}$$

**Gesamtfläche** (immer positiv):

$$A = \int_0^{2\pi} |\sin x|\, dx = 4$$


    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_9_0.png)
    


### 6. Bewegung: Weg, Geschwindigkeit und Beschleunigung

Ein besonders wichtiges Beispiel für Ableitungen und Integrale ist Bewegung entlang einer Linie.

Dabei beschreibt $s(t)$ den **Ort** zum Zeitpunkt $t$. Die Geschwindigkeit ist die momentane Änderung des Ortes:

$$v(t) = s'(t) = \frac{ds}{dt}$$

Die Beschleunigung ist die momentane Änderung der Geschwindigkeit:

$$a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}$$

In Ableitungsrichtung gilt also:

$$s(t) \xrightarrow{\text{Ableitung}} v(t) \xrightarrow{\text{Ableitung}} a(t)$$

Integrale gehen in die Gegenrichtung. Die Fläche unter der Beschleunigung liefert die Änderung der Geschwindigkeit, und die Fläche unter der Geschwindigkeit liefert die Änderung des Ortes:

$$v(b) - v(a) = \int_a^b a(t)\,dt$$

$$s(b) - s(a) = \int_a^b v(t)\,dt$$

**Wichtig:** Das Integral über $v(t)$ ist zunächst eine **Verschiebung**. Wenn die Geschwindigkeit negativ wird, bewegt sich das Objekt zurück. Dann zählen positive und negative Flächen gegeneinander.

Die tatsächlich zurückgelegte Strecke erhält man deshalb mit dem Betrag der Geschwindigkeit:

$$\text{Strecke} = \int_a^b |v(t)|\,dt$$

| Größe | Bedeutung | Ableitung | Integral |
|---|---|---|---|
| $s(t)$ | Ort / Position | $s'(t) = v(t)$ | - |
| $v(t)$ | Geschwindigkeit | $v'(t) = a(t)$ | $\int_a^b v(t)\,dt = s(b)-s(a)$ |
| $a(t)$ | Beschleunigung | - | $\int_a^b a(t)\,dt = v(b)-v(a)$ |


    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_11_0.png)
    



    
![png](04_Einf%C3%BChrung_in_die_Integralrechnung_files/04_Einf%C3%BChrung_in_die_Integralrechnung_11_1.png)
    


---

## Zusammenfassung

| Konzept | Formel / Idee |
|---------|---------------|
| **Stammfunktion** | $F'(x) = f(x)$ - Umkehrung der Ableitung |
| **Unbestimmtes Integral** | $\int f(x)\, dx = F(x) + C$ |
| **Bestimmtes Integral** | $\int_a^b f(x)\, dx = F(b) - F(a)$ |
| **Riemann-Summe** | Approximation durch $n$ Rechtecke → Grenzwert |
| **Hauptsatz** | Verbindet Ableitung ↔ Integral |
| **Orientierte Fläche** | Unter x-Achse zählt negativ |


---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Stammfunktion | Antiderivative |
| Integrand | Integrand |
| Integrationskonstante | Constant of integration |
| Bestimmtes Integral | Definite integral |
| Unbestimmtes Integral | Indefinite integral |
| Riemann-Summe | Riemann sum |
| Hauptsatz | Fundamental Theorem of Calculus |
| Obere / Untere Grenze | Upper / Lower bound |
| Orientierte Fläche | Signed area |
