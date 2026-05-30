# Funktionen

## 03 - Lineare und Quadratische Funktionen

Lineare Funktionen ($f(x) = kx + d$: Steigung, y-Achsenabschnitt, Nullstelle) und quadratische Funktionen - Umwandlung zwischen Normalform, Scheitelpunktform und Produktform; Nullstellen und Scheitelpunkt.

> Vorausgesetzt: Funktionsbegriff, quadratische Gleichungen.

### Lernziele

- **Lineare Funktionen** aufstellen, zeichnen und ihre Parameter deuten
- **Quadratische Funktionen** in Normal-, Scheitel- und Produktform umwandeln
- **Nullstellen** und **Scheitelpunkt** berechnen
- Beide Funktionstypen sicher auf Papier skizzieren

---

## Teil A: Lineare Funktionen

### 1. Definition und Parameter

Eine **lineare Funktion** hat die allgemeine Form:

$$f(x) = kx + d$$

| Parameter | Bedeutung | Grafisch |
|-----------|-----------|----------|
| $k$ | **Steigung** (Änderungsrate) | Neigung der Geraden |
| $d$ | **y-Achsenabschnitt** | Schnittpunkt mit der y-Achse |

**Steigung $k$:**  
Die Steigung gibt an, um wie viele Einheiten sich $f(x)$ ändert, wenn $x$ um 1 zunimmt.

$$k = \frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

Ist $k > 0$, steigt die Gerade von links nach rechts; ist $k < 0$, fällt sie. Für $k = 0$ ergibt sich eine horizontale Gerade. Je größer $|k|$, desto steiler der Graph.

**Nullstelle:** $f(x) = 0 \Rightarrow x = -\frac{d}{k}$ (für $k \ne 0$)

---

### Geradengleichung aufstellen

Kennt man die Steigung und einen Punkt - oder zwei Punkte - lässt sich die Geradengleichung direkt aufstellen:

| Gegeben | Methode |
|---------|---------|
| Steigung $k$ + Punkt $P(x_0, y_0)$ | $f(x) = k(x - x_0) + y_0$ |
| Zwei Punkte $P_1, P_2$ | $k = \frac{y_2 - y_1}{x_2 - x_1}$, dann einsetzen |


    
![png](03_Lineare_und_Quadratische_Funktionen_files/03_Lineare_und_Quadratische_Funktionen_2_0.png)
    


## Teil B: Quadratische Funktionen

### 2. Die drei Darstellungsformen

| Form | Formel | Daraus direkt ablesbar |
|------|--------|------------------------|
| **Normalform** | $f(x) = ax^2 + bx + c$ | y-Achsenabschnitt $c$ |
| **Scheitelpunktform** | $f(x) = a(x - h)^2 + k$ | Scheitelpunkt $S(h, k)$ |
| **Produktform** | $f(x) = a(x - x_1)(x - x_2)$ | Nullstellen $x_1, x_2$ |

**Parameter $a$:**

| $a$ | Wirkung |
|-----|--------|
| $a > 0$ | Parabel nach oben geöffnet (U-Form) |
| $a < 0$ | Parabel nach unten geöffnet (∩-Form) |
| $\|a\| > 1$ | Schmaler (gestreckt) |
| $\|a\| < 1$ | Breiter (gestaucht) |

---

### 3. Scheitelpunkt

Der **Scheitelpunkt** $S(h, k)$ ist der höchste oder tiefste Punkt der Parabel.

Aus der Normalform $ax^2 + bx + c$:

$$h = -\frac{b}{2a}, \qquad k = f(h) = c - \frac{b^2}{4a}$$

---

### 4. Nullstellen und Diskriminante

Wie viele Schnittpunkte hat eine Parabel mit der x-Achse? Die Antwort steckt vollständig in der **Diskriminante**.

Die Nullstellen von $ax^2 + bx + c = 0$ ergeben sich aus der **Lösungsformel**:

> Siehe Algebra/Quadratische Gleichungen für Details.

$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Die **Diskriminante** $D = b^2 - 4ac$ bestimmt die Anzahl der Lösungen:

| $D$ | Nullstellen | Grafisch |
|-----|-------------|----------|
| $D > 0$ | Zwei verschiedene | Parabel schneidet x-Achse zweimal |

| $D = 0$ | Eine doppelte | Parabel berührt x-Achse || $D < 0$ | Keine reelle | Parabel schneidet x-Achse nicht |


    
![png](03_Lineare_und_Quadratische_Funktionen_files/03_Lineare_und_Quadratische_Funktionen_4_0.png)
    



    
![png](03_Lineare_und_Quadratische_Funktionen_files/03_Lineare_und_Quadratische_Funktionen_5_0.png)
    


## Anwendungen Quadratischer Funktionen

### 1. Physik: Projektilbewegung
Die Höhe eines geworfenen Objekts folgt einer quadratischen Funktion:
$$h(t) = h_0 + v_0 \,t - \frac{1}{2}g \,t^2$$

wobei:
- $h_0$ = Anfangshöhe
- $v_0$ = Anfangsgeschwindigkeit
- $g$ = Gravitationsbeschleunigung (=~ 9.81 m/s²)

Die Nullstellen zeigen, wann das Objekt den Boden berührt.

### 2. Geometrie: Flächenoptimierung
Bei rechteckigen Grundstücken mit begrenztem Umfang ist die Fläche eine quadratische Funktion:
$$A(x) = x(U/2 - x)$$

Der Scheitelpunkt zeigt die Abmessungen für maximale Fläche.

### 3. Optik & Akustik: Parabolische Reflektoren
Die Form von Satellitenschüsseln, Spiegeln und Mikrofonen folgt Parabeln. Der Grund ist geometrisch elegant: Alle von einer Parabel reflektierten parallelen Strahlen treffen sich exakt in ihrem **Brennpunkt** - das macht Parabeln ideal zum Bündeln von Licht, Schall oder Funksignalen. Die Gleichung $f(x) = ax^2$ bestimmt dabei, wie spitz oder flach die Parabel und damit der Fokus ist.


    
![png](03_Lineare_und_Quadratische_Funktionen_files/03_Lineare_und_Quadratische_Funktionen_7_0.png)
    



    
![png](03_Lineare_und_Quadratische_Funktionen_files/03_Lineare_und_Quadratische_Funktionen_7_1.png)
    


---

## Zusammenfassung

| Thema | Kernformel |
|-------|------------|
| **Lineare Funktion** | $f(x) = kx + d$ - Steigung $k$, Abschnitt $d$ |
| **Geradenbestimmung** | $k = \frac{\Delta y}{\Delta x}$ aus zwei Punkten |
| **Normalform** | $f(x) = ax^2 + bx + c$ |
| **Scheitelpunktform** | $f(x) = a(x-h)^2 + k$, Scheitel $S(h,k)$ |
| **Lösungsformel** | $x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$, $D = b^2-4ac$  |
| **Diskriminante** | $D>0$: 2 NS, $D=0$: 1 NS, $D<0$: 0 NS |

---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Steigung | Slope |
| y-Achsenabschnitt | y-intercept |
| Scheitelpunkt | Vertex |
| Diskriminante | Discriminant |
| Nullstelle | Root / Zero |
| Parabel | Parabola |
| Normalform | Standard form |
| Quadratische Ergänzung | Completing the square |


