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
