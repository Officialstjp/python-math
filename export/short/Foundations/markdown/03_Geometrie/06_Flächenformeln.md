# Geometrie und Trigonometrie

## 06 - Geometrische Flächenformeln und Herleitungen

Herleitung der Flächenformeln für Parallelogramm ($A = g \cdot h$), Dreieck ($A = \frac{1}{2}gh$), Trapez ($A = \frac{a+c}{2} \cdot h$) und Kreis ($A = \pi r^2$) — Zerlegungsprinzip, Prinzip von Cavalieri (Scherung) und Exhaustionsmethode zur Definition von $\pi$.

> Vorausgesetzt: Satz des Pythagoras (03_Geometrie/05).

### Lernziele

- Du verstehst die **Herleitung** der Flächenformeln für Parallelogramm, Dreieck und Trapez.
- Du verstehst das Konzept der **Höhe** als orthogonalem Abstand.
- Du lernst, wie die Kreiszahl $\pi$ durch **Grenzwertprozess** definiert ist.

---

## 1. Das Axiom: Das Rechteck

In der Mathematik müssen wir uns auf eine grundlegende Wahrheit einigen, die wir nicht beweisen, sondern *setzen* (ein Axiom).

**Definition:**
Der Flächeninhalt $A$ eines Rechtecks mit den Seitenlängen $a$ und $b$ ist definiert als das Produkt der Seiten.

$$A = a \cdot b$$

*Warum?* Weil wir Fläche als "Anzahl der Einheitsquadrate" $(1 \times 1)$ definieren, die in die Form passen.

---

## 2. Das Parallelogramm & die Scherung

Ein Parallelogramm ist ein Viereck, bei dem gegenüberliegende Seiten parallel sind.
Die klassische Formel lautet $A = g \cdot h$ (Grundfläche mal Höhe), oder auch $A = a \cdot h_a$ (Seite $a$ mal Höhe auf $a$). Aber warum taucht die schräge Seite $b$ hier nicht auf?

**Der Beweis durch Zerlegung:**
Wir können links ein rechtwinkliges Dreieck abschneiden und es rechts wieder anfügen. Aus dem schiefen Parallelogramm wird ein perfektes Rechteck mit der Breite $a$ und der Höhe $h_a$.

**Das Prinzip von Cavalieri:**
Stellen wir uns ein Parallelogramm als einen Stapel Spielkarten - betrachtet von der Seite vor. Wenn man den Stapel zur Seite drückt (schert), ändert sich die Form des Stapels, aber das **Volumen** bleibt exakt gleich (hierbei bilden die Kanten des Stapels ein Parallelogramm - die Fläche dessen gleich bleiben muss, wenn das Volumen gleich bleibt). 


    
![png](06_Fl%C3%A4chenformeln_files/06_Fl%C3%A4chenformeln_3_0.png)
    


## 3. Animation: Scherung

Die untenstehende Animation veranschaulicht das Prinzp der Scherung weiter.
Wir starten mit einem Rechteck ($A = g \cdot h$) und schieben die obere Seite zur Seite
Die Grundseite $g$ bleibt gleich. Die Höhe $h$ bleibt gleich. Also muss auch die Fläche gleich bleiben, egal wie "schief" das Parallelogramm wird.


<div style="padding:0.75rem 1rem; border:1px solid #d8dee9; background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;">(Interaktive Matplotlib-Animation im statischen Export ausgelassen) </div>


## 4. Das Dreieck

Jedes beliebige Dreieck lässt sich durch Spiegelung an einer der Seitenmitten zu einem Parallelogramm verdoppeln.
- Das entstandene Parallelogramm hat die Grundseite $g$ und die Höhe $h$.
- Seine Fläche ist $A_{\text{Para}} = g \cdot h$.
- Da das Dreieck genau die Hälfte davon ist:

$$A_{\text{Dreieck}} = \frac{1}{2} \cdot g \cdot h$$

*Wichtige Erkenntnis:* Es ist egal, wo die Spitze des Dreiecks liegt (solange sie auf einer Paralleln zur Grundseite verschoben wird), die Fläche bleibt gleich.

---


## 5. Das Trapez

Ein Trapez hat zwei parallele Seiten $a$ und $c$. Die anderen beiden Seiten sind beliebig.
Um die Formel zu beweisen, gibt es einen eleganten Trick:
Wir verdoppeln das Trapez und legen das zweite verkehrt herum an das erste.

- Es entsteht ein riesiges Parallelogramm.
- Die Grundseite dieses Parallelogramms ist $(a + c)$.
- Die Höhe ist $h$.
- Fläche des Parallelogramms: $A_{\text{Gesamt}} = (a + c) \cdot h$.
- Da wir zwei Trapeze haben, ist die Fläche eines einzelnen:

$$A_{\text{Trapez}} = \frac{a + c}{2} \cdot h$$

Der Term $\frac{a+c}{2}$ ist dabei nichts anderes als die **Mittelparallele** $m$ (der Durchschnitt der beiden Längen).

## 6. Der Kreis: Die Ausschöpfung

Wie berechnet man die Fläche von etwas, das keine Ecken hat? Die antiken Griechen (besonders Archimedes) nutzten die **Exhaustionsmethode**.

Wir nähern den Kreis durch regelmäßige Vielecke an ($n$-Ecke).
- Ein 4-Eck (Quadrat) ist eine grobe Näherung.
- Ein 8-Eck ist besser.
- Ein 100-Eck ist fast nicht mehr von einem Kreis zu unterscheiden.

**Die Herleitung:**
Zerlegen wir ein regelmäßiges $n$-Eck in $n$ Dreiecke.
Jedes Dreieck hat die Grundseite $s$ (Seitenlänge des Polygons) und die Höhe $h$ (Abstand zum Mittelpunkt).
$$A_{\text{Dreieck}} = \frac{1}{2} \cdot s \cdot h$$

Die Gesamtfläche des Polygons ist:
$$A_n = n \cdot \left( \frac{1}{2} \cdot s \cdot h \right) = \frac{1}{2} \cdot (n \cdot s) \cdot h$$

Der Term $(n \cdot s)$ ist der **Umfang** $U$ des Polygons.
$$A_n = \frac{1}{2} \cdot U \cdot h$$

Wenn $n$ unendlich groß wird ($n \to \infty$):
1.  Der Umfang $U$ wird zum Kreisumfang $2\pi r$.
2.  Die Höhe $h$ wird zum Radius $r$.

Einsetzen:
$$A_{\text{Kreis}} = \frac{1}{2} \cdot (2\pi r) \cdot r = \pi r^2$$

Dies ist einer der ersten historischen Beweise, der Grenzwertbetrachtungen (Calculus) vorwegnahm.


<div style="padding:0.75rem 1rem; border:1px solid #d8dee9; background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;">(Interaktive Matplotlib-Animation im statischen Export ausgelassen) </div>


## Zusammenfassung

| Figur | Formel | Herleitung |
|-------|--------|------------|
| Rechteck | $A = a \cdot b$ | Axiom (Einheitsquadrate) |
| Parallelogramm | $A = g \cdot h$ | Zerlegung / Scherung (Cavalieri) |
| Dreieck | $A = \frac{1}{2} g \cdot h$ | Halbes Parallelogramm |
| Trapez | $A = \frac{a+c}{2} \cdot h$ | Verdopplung zum Parallelogramm |
| Kreis | $A = \pi r^2$ | Exhaustionsmethode ($n$-Eck → Grenzwert) |



---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Flächeninhalt | Area |
| Umfang | Perimeter (Polygon) / Circumference (Circle) |
| Rechteck | Rectangle |
| Parallelogramm | Parallelogram |
| Trapez | Trapezoid (US) / Trapezium (UK) |
| Kreis | Circle |
| Radius | Radius |
| Prinzip von Cavalieri | Cavalieri's principle |
| Scherung | Shear mapping |
| Exhaustionsmethode | Method of exhaustion |
