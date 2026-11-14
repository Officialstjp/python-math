# Geometrie und Trigonometrie

## 01 - Trigonometrie 1: Rechtwinkliges Dreieck

Die Trigonometrie verbindet Winkel mit Seitenlängen — eine Brücke zwischen Geometrie und Algebra. Grundlegend dafür sind Sinus ($\sin\alpha = \frac{\text{Gegenkathete}}{\text{Hypotenuse}}$), Cosinus ($\cos\alpha = \frac{\text{Ankathete}}{\text{Hypotenuse}}$) und Tangens ($\tan\alpha = \frac{\text{Gegenkathete}}{\text{Ankathete}}$) als konstante Seitenverhältnisse im rechtwinkligen Dreieck, begründet durch Ähnlichkeit; wichtige Werte ($30°, 45°, 60°$) geometrisch hergeleitet.

> Vorausgesetzt: Satz des Pythagoras (03_Geometrie/05), Ähnlichkeit (03_Geometrie/02).

### Lernziele

- Du verstehst, warum Seitenverhältnisse in ähnlichen Dreiecken konstant sind.
- Du lernst die Definitionen von **Sinus**, **Cosinus** und **Tangens**.
- Du verstehst den Tangens als **Steigung**.
- Du kannst wichtige Werte (für $30°, 45°, 60°$) geometrisch herleiten, ohne Taschenrechner.

---

## 1. Das Fundament: Ähnlichkeit

Warum funktionieren Sinus und Cosinus überhaupt?

Nehmen wir ein kleines rechtwinkliges Dreieck mit einem Winkel $\alpha = 30°$.
Dann nehmen wir ein riesiges rechtwinkliges Dreieck, das ebenfalls einen Winkel $\alpha = 30°$ hat.

Da beide Dreiecke zwei gleiche Winkel haben ($30°$ und $90°$), ist auch der dritte Winkel gleich ($60°$). Nach dem Ähnlichkeitssatz (WW) sind die Dreiecke **ähnlich**.

**Die Konsequenz:**
Das Verhältnis der Seitenlängen zueinander ist in beiden Dreiecken **identisch**.
Wenn im kleinen Dreieck die Höhe genau halb so lang ist wie die schräge Seite, dann ist das im riesigen Dreieck auch so.

Diese konstanten Verhältnisse haben Namen bekommen: Sinus, Cosinus und Tangens.

## 2. Die Definitionen

Um die Verhältnisse zu bilden, müssen wir die Seiten relativ zum betrachteten Winkel $\alpha$ benennen:

1.  **Hypotenuse ($H$):** Immer die längste Seite, gegenüber vom rechten Winkel.
2.  **Gegenkathete ($GK$):** Die Seite, die dem Winkel $\alpha$ **gegenüber** liegt.
3.  **Ankathete ($AK$):** Die Seite, die **am** Winkel $\alpha$ anliegt (und nicht die Hypotenuse ist).

Die drei Grundfunktionen sind definiert als:

$$\sin(\alpha) = \frac{\text{Gegenkathete}}{\text{Hypotenuse}} = \frac{GK}{H}$$

$$\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}} = \frac{AK}{H}$$

$$\tan(\alpha) = \frac{\text{Gegenkathete}}{\text{Ankathete}} = \frac{GK}{AK}$$


    
![png](01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_files/01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_4_0.png)
    


## 3. Der Tangens als Steigung

Erinnern wir uns an die lineare Funktionen: $y = k \cdot x + d$.

Dabei war $k$ die **Steigung** (oft auch $m$ genannt).

Die Steigung war definiert als: $\frac{\Delta y}{\Delta x}$ ("Höhenunterschied durch Längenunterschied").

Schauen wir uns das Dreieck oben an:
- $\Delta y$ ist die Gegenkathete.
- $\Delta x$ ist die Ankathete.

Daraus folgt eine der wichtigsten Erkenntnisse für die technische Mathematik:
**Die Steigung einer Geraden ist der Tangens ihres Steigungswinkels.**

$$\text{Steigung } k = \tan(\alpha)$$

Beispiel: Eine Straße mit $100\%$ Steigung.
Das heißt $\Delta y = \Delta x$ (z.B. 100m hoch auf 100m Distanz).
$\tan(\alpha) = 1$. Welcher Winkel hat den Tangens 1? $\rightarrow 45°$.
Eine 100%ige Steigung entspricht also einem $45°$-Winkel, nicht $90°$!

## 4. Herleitungen

Wir können diese Verhältnisse geometrisch beweisen:

### A. Der 45°-Fall (Halbes Quadrat)
Nimm ein Quadrat mit Seitenlänge $1$. Schneide es diagonal durch.
- Die Winkel sind $90°, 45°, 45°$.
- Die Katheten sind $a=1, b=1$
- Die Hypotenuse ist laut Pythagoras $c = \sqrt{1^2 + 1^2} = \sqrt{2}$.

Daraus folgt:
$$\sin(45°) = \frac{GK}{H} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} \approx 0.707$$
$$\tan(45°) = \frac{GK}{AK} = \frac{1}{1} = 1$$


    
![png](01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_files/01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_8_0.png)
    


### B. Der 30°/60°-Fall (Das halbe gleichseitige Dreieck)
Nimm ein gleichseitiges Dreieck mit Seitenlänge $2$. Alle Winkel sind $60°$.
Schneide es in der Mitte senkrecht durch (Höhe).
- Die untere Seite (Länge 2) wird halbiert $\rightarrow$ Ankathete für $60°$ ist $1$.
- Die Hypotenuse ist immer noch die Originalseite $\rightarrow 2$.
- Die Höhe (Gegenkathete für $60°$) ist laut Pythagoras: $h = \sqrt{2^2 - 1^2} = \sqrt{3}$.
- Der obere Winkel wurde halbiert $\rightarrow 30°$.

Daraus folgt für $30°$:
$$\sin(30°) = \frac{GK}{H} = \frac{1}{2} = 0.5$$
$$\cos(30°) = \frac{AK}{H} = \frac{\sqrt{3}}{2} \approx 0.866$$


    
![png](01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_files/01_%C3%84hnlichkeit_und_Verh%C3%A4ltnisse_11_0.png)
    


## 5. Interaktive Visualisierung: Winkeländerung

Wie verändern sich Sinus und Cosinus, wenn der Winkel wächst?
In dieser Animation halten wir die Hypotenuse konstant (Länge 1).
Beobachte:
- Wenn $\alpha$ klein ist, ist die Gegenkathete (Sinus) klein.
- Wenn $\alpha$ wächst, wächst der Sinus, aber die Ankathete (Cosinus) schrumpft.


<div style="padding:0.75rem 1rem; border:1px solid #d8dee9; background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;">(Interaktive Matplotlib-Animation im statischen Export ausgelassen) </div>


## 6. Praxis: Rückwärtsrechnen (Arcus-Funktionen)

Oft kennen wir die Seiten, wollen aber den Winkel wissen.
Dafür nutzen wir die Umkehrfunktionen. Auf dem Taschenrechner heißen sie oft $\sin^{-1}$ oder `asin`.

$$\sin(\alpha) = x \iff \alpha = \arcsin(x)$$

**Beispiel:**
Eine Rampe ist 10 Meter lang ($H$) und überwindet einen Höhenunterschied von 2 Metern ($GK$).
Wie steil ist der Winkel?
1. Formel wählen: Wir haben $GK$ und $H$, also brauchen wir den Sinus.
2. Aufstellen: $\sin(\alpha) = \frac{2}{10} = 0.2$.
3. Umkehren: $\alpha = \arcsin(0.2) \approx 11.54°$.

---

## Verständnis-Check

**Aufgabe 1: Der Turm**
Du stehst 50 Meter von einem Turm entfernt. Du misst den Winkel zur Spitze mit $60°$.
Wie hoch ist der Turm? (Augenhöhe vernachlässigen).
*Tipp: Skizze! Du hast Ankathete (50m), suchst Gegenkathete (Höhe).*

**Aufgabe 2: Die Leiter**
Eine 4 Meter lange Leiter lehnt an der Wand. Sie soll sicher stehen und dafür einen Winkel von ca. $75°$ zum Boden haben.
Wie weit muss der Fuß der Leiter von der Wand entfernt sein?
*Tipp: Du hast Hypotenuse (4m) und Winkel, suchst Ankathete.*

**Aufgabe 3: Exakt rechnen**
Berechne ohne Taschenrechner: $\sin(30°) + \cos(60°)$.

### Lösungen

<details open><summary>Lösung Aufgabe 1</summary>

Gegeben: $AK = 50$, $\alpha = 60°$. Gesucht: $GK$ (Höhe).
$$\tan(60°) = \frac{GK}{AK} = \frac{h}{50}$$
$$h = 50 \cdot \tan(60°)$$

Wir wissen: $\tan(60°) = \frac{\sin(60°)}{\cos(60°)} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3}$.

$$h = 50 \cdot \sqrt{3} \approx 50 \cdot 1.732 = 86.6 \text{ m}$$

</details>

<details open><summary>Lösung Aufgabe 2</summary>

Gegeben: $H = 4$, $\alpha = 75°$. Gesucht: $AK$ (Abstand).

$$\cos(75°) = \frac{AK}{H} = \frac{x}{4}$$
$$x = 4 \cdot \cos(75°) \approx 4 \cdot 0.2588 \approx 1.035 \text{ m}$$

</details>

<details open><summary>Lösung Aufgabe 3</summary>

$$\sin(30°) = 0.5$$
$$\cos(60°) = 0.5$$
$$0.5 + 0.5 = 1$$

(Denk an das gleichseitige Dreieck: Der obere Winkel ist 30°, der untere 60°. Ankathete von 60° ist Gegenkathete von 30°).

</details>

## Zusammenfassung

| Thema | Kernaussage |
|-------|-------------|
| Ähnlichkeit | Gleiche Winkel → gleiche Seitenverhältnisse; Grundlage der Trigonometrie |
| Sinus | $\sin(\alpha) = \frac{GK}{H}$ |
| Cosinus | $\cos(\alpha) = \frac{AK}{H}$ |
| Tangens | $\tan(\alpha) = \frac{GK}{AK}$ = Steigung |
| Spezialwerte | $\sin(30°)=0{,}5$; $\sin(45°)=\frac{\sqrt{2}}{2}$; $\sin(60°)=\frac{\sqrt{3}}{2}$ |
| Arcus-Funktionen | Umkehrung: von Seitenverhältnis zurück zum Winkel |



---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Gegenkathete | Opposite (side) |
| Ankathete | Adjacent (side) |
| Hypotenuse | Hypotenuse |
| Steigung | Slope / Gradient |
| Rechtwinklig | Right-angled |
| Gleichseitig | Equilateral |
