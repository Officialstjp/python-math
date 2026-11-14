# Geometrie und Trigonometrie

## 04 - Flächeninhalte und Skalierung (Das Pizza-Prinzip)

Lineare vs. quadratische Skalierung: Wird eine Figur um Faktor $k$ vergrößert, vervierfacht sich die Fläche bei $k = 2$ ($A' = k^2 \cdot A$); Anwendung auf Alltagsprobleme (Preisvergleich, Kartenmaßstäbe).

> Vorausgesetzt: Ähnlichkeit (03_Geometrie/02).

### Lernziele

- Du verstehst den Unterschied zwischen linearer Skalierung (Länge) und quadratischer Skalierung (Fläche).
- Du kannst den neuen Flächeninhalt berechnen, wenn der Vergrößerungsfaktor $k$ bekannt ist.
- Du kannst dieses Wissen auf Alltagsprobleme (Preise, Kartenmaßstäbe) anwenden.

---

## 1. Das Pizza-Problem

Stellen wir uns vor, wir sind in einer Pizzeria und wollen Pizza bestellen.
- Eine **kleine Pizza** (20cm Durchmesser) kostet **$5\text{€}$**.
- Eine **große Pizza** (40 cm Durchmesser) kostet **$15\text{€}$**.

Welches Angebot ist besser?
Intuitiv denken viele: "Die große ist doppelt so groß ($40 * 2 = 20$), kostet aber dreimal so viel, daher ist eine kleine Pizza ein besseres Angebot ($5 * 2 = 10 < 15$)

Mathematisch ist das jedoch falsch. Wenn wir den Durchmesser verdoppeln ($k = 2$), vierfacht sich die Fläche. Aber warum ist das so?

## 2. Mathematische Herleitung

Betrachten wir ein Rechteck mit den Seitenlängen $a$ und $b$.
Der Flächeninhalt ist $A = a \cdot b$.

Nun vergrößern wir das Rechteck um den **Skalierungsfaktor** $k$.
Die neuen Seitenlängen sind $a' = k \cdot a$ und $b' = k \cdot b$.

Wie groß ist die neue Fläche $A'$?

$$
\begin{aligned}
A' &= a' \cdot b' \\
A' &= (k \cdot a) \cdot (k \cdot b) \\
A' &= k \cdot k \cdot a \cdot b \\
A' &= k^2 \cdot (a \cdot b) \\
A' &= k^2 \cdot A \\
\end{aligned}
$$

**Gesetz der Flächenskalierung:**
Wird eine Figur um den Faktor $k$ vergrößert, wächst ihr Flächeninhalt um den Faktor $k^2$.
- Doppelte Länge ($k=2$) $\rightarrow$ $2^2 = 4$-fache Fläche
- Dreifach Länge ($k=3$) $\rightarrow$ $3^2 = 9$-fache Fläche
- Halbe Länge ($k=0.5$) $\rightarrow$ $0.5^2 = 0.25$-fache Fläche (Ein Viertel)


    
![png](04_Flaecheninhalte_und_Skalierung_files/04_Flaecheninhalte_und_Skalierung_3_0.png)
    


## 3. Verallgemeinerung

Das Gesetz $A' = k^2 \cdot A$ gilt nicht nur für Quadrate, sondern für alle 2-dimensionalen geometrischen Figuren, solange sie **ähnlich** sind.

**Beispiel Kreis:**
$$A = r^2 \cdot \pi$$
Verdoppeln wir den Radius ($r' = 2r$), dann gilt:
$$A' = (2r)^2 \cdot \pi = 4r^2 \cdot \pi = 4 \cdot A$$

**Beispiel Landkarten:**
Eine Karte hat den Maßstab $1:50.000$.
Das bedeutet $1$ cm auf der Karte sind $50.000$ cm ($500$ m) in der Realität.
Der Längen-Faktor ist also $k = 50.000$.

Wie verhält es sich mit der Fläche?
$1 \text{ cm}^2$ auf der Karte entspricht in der Realität:
$$1 \text{ cm}^2 \cdot (50.000)^2 = 1 \cdot 2.500.000.000 \text{ cm}^2 = 250.000 \text{ m}^2 = 25 \text{ Hektar}$$
Der Flächenmaßstab ist also $1 : k^2$.


## 4. Interaktive Visualisierung: Längen- vs. Flächenwachstum

In der folgenden Animation sehen wir uns an, wie sich die Fläche verändert, wenn wir den Skalierungsfaktor $k$ kontinuierlich von 1 bis 3 erhöhen.
Wir stellen dies in einem Graphen dar. Während die Seitenlänge linear wächst (eine Gerade), wächst die Fläche quadratisch (eine Parabel).


<div style="padding:0.75rem 1rem; border:1px solid #d8dee9; background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;">(Interaktive Matplotlib-Animation im statischen Export ausgelassen) </div>


---

## Verständnis-Check

**Aufgabe 1: Pizza-Finale**
Zurück zu unserem Beispiel vom Anfang:
- Pizza A: 20 cm Durchmesser, 5 €
- Pizza B: 40 cm Durchmesser, 15 €
Berechne den Skalierungsfaktor $k$ und den Flächenfaktor. Wie viel mal mehr Pizza bekommst du bei B im Vergleich zu A? Ist der Preis von 15 € gerechtfertigt?

**Aufgabe 2: Grundstückspreise**
Ein quadratisches Grundstück hat eine Seitenlänge von 30 Metern und kostet 90.000 €.
Ein Nachbargrundstück ist ebenfalls quadratisch, hat aber eine Seitenlänge von 60 Metern.
Wenn der Quadratmeterpreis gleich bleibt, wie viel müsste das große Grundstück kosten?

**Aufgabe 3: Der Fernseher**
Du wechselst von einem 30-Zoll Bildschirm auf einen 60-Zoll Bildschirm (die Diagonale verdoppelt sich).
Wie verändert sich die Bildfläche?

### Lösungen

<details open><summary>Lösung Aufgabe 1</summary>

- Skalierungsfaktor $k = \frac{40}{20} = 2$.
- Flächenfaktor $k^2 = 2^2 = 4$.
- Die Pizza B hat die **4-fache Fläche** (also 4-mal so viel Belag und Teig) wie Pizza A.
- Preisvergleich: $4 \times 5\,\text{€} = 20\,\text{€}$.
- Da Pizza B nur 15 € kostet, ist sie das deutlich bessere Angebot (mehr Pizza pro Euro).

</details>

<details open><summary>Lösung Aufgabe 2</summary>

- Seitenlänge verdoppelt sich ($30 \text{m} \rightarrow 60 \text{m}$), also $k=2$.
- Die Fläche vervierfacht sich ($k^2 = 4$).
- Preis: $90.000\,\text{€} \cdot 4 = 360.000\,\text{€}$.

</details>

<details open><summary>Lösung Aufgabe 3</summary>

- Die Angabe "Zoll" bei Bildschirmen bezieht sich auf die Diagonale (eine Länge).
- Verdopplung der Diagonale ($k=2$) bedeutet auch hier eine **Vervierfachung** der Bildfläche ($k^2=4$).

</details>

## Zusammenfassung

| Thema | Kernaussage |
|-------|-------------|
| Flächenskalierung | $A' = k^2 \cdot A$ - Flächen wachsen quadratisch mit dem Skalierungsfaktor |
| Pizza-Prinzip | Doppelter Durchmesser = vierfache Fläche |
| Kartenmaßstab | Längenmaßstab $1:k$, Flächenmaßstab $1:k^2$ |



---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Flächeninhalt | Area |
| Skalierung | Scaling |
| Skalierungsfaktor | Scale factor ($k$) |
| Maßstab | Scale (on a map) |
| Quadratisch | Quadratic / Square |
| Verhältnis | Ratio |
| Ähnlich | Similar |
| Umfang | Perimeter |
