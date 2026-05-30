# Geometrie und Trigonometrie

## 02 - Winkelbeziehungen, Kongruenz und Ähnlichkeit

- Winkel an Geradenkreuzungen (Scheitelwinkel: gleich; Nebenwinkel: supplementär, $\alpha + \beta = 180°$) 
- an parallelen Geraden (Stufenwinkel: gleich; Wechselwinkel: gleich); 
- Kongruenz (Deckungsgleichheit) und Ähnlichkeit (Formgleichheit, konstante Seitenverhältnisse).

> Vorausgesetzt: Winkelgrundlagen.

### Lernziele

- Du wirst die Gesetzmäßigkeiten an Geradenkreuzungen verstehen (Scheitel- und Nebenwinkel)
- Du wirst Winkel an parallelen Geraden identifizieren können (Stufen- und Wechselwinkel)
- Du wirst die Bedeutung von **Kongruenz** (Deckungsgleichheit) und **Ähnlichkeit** (Formgleichheit) kennenlernen

---

## 1. Winkel an Geradenkreuzungen

Wenn sich zwei Geraden in einer Ebene schneiden, entstehen um den Schnittpunkt vier Winkel. Diese stehen in einer festen Beziehung zueinander, welche wir verwenden können um fehlende Winkelgrößen ohne messen zu müssen.

### A. Nebenwinkel (Supplementäre Winkel)

Nehmen wir eine gerade Linie, die von einer anderen Linie geschnitten wird. 
Zwei Winkel, die **nebeneinander** liegen, einen gemeinsamen Schenkel und einen gemeinsamen Scheitelpunkt haben, nennt man **Nebenwinkel**

Die beiden äußeren Schenkel bilden zusammen eine gerade (einen gestreckten Winkel von $180°$), daher gilt für Nebenwinkel immer:

$$ \alpha + \beta = 180° $$

Man sagt auch: "Die Winkel ergänzen sich zu $180°$ (sie sind supplementär)"
Wenn man einen Winkel kennt, kann man sofort den anderen berechnen: $\beta = 180° - \alpha$.

### B. Scheitelwinkel

Zwei Winkel, die sich an einer Geradenkreuzung **gegenüberliegen**, nennt man **Scheitelwinkel**.
Sie teilen sich den Scheitelpunkt, haben aber keinen gemeinsamen Schenkel.

Scheitelwinkel sind **immer gleich groß**.

**Warum ist das so?**

Nehmen wir die Nebenwinkel $\alpha$ und $\beta$. Somit $\alpha + \beta = 180°$ 
Gleichzeitig sind aber auch $\beta$ und $\gamma$ Nebenwinkel. Also ist $\beta + \gamma = 180°$.
Daraus folgt logisch: $\alpha$ muss genau so groß sein wie $\gamma$, um $\beta$ zu $180°$ zu ergänzen.


    
![png](02_Winkelbeziehungen_files/02_Winkelbeziehungen_2_0.png)
    


## 2. Winkel an Parallelen

Wenn eine Gerade zwei andere Geraden schneiden, die **parallel** zueinander sind, treten zwei weitere Winkelarten auf: **F-Winkel** und **Z-Winkel** (Da die Linienführung an diese Buchstaben erinnert)
Diese Situation sieht man bspw. bei Eisenbahnschienen, Fensterrahmen oder Straßenkreuzungen.

### A. Stufenwinkel (F-Winkel)

Schneidet man die Kreuzung der oberen Parallele aus und schiebt die schneidende Gerade (**Transversale**) hinunter, bis sie genau auf der unteren Parallele liegt, würden sich die Winkel exakt decken.
Winkel, die auf derselben Seite der Transversale und auf derselben Seite der Parallelen liegen (also: beide "oben rechts" oder beide "unten links"), nennt man **Stufenwinkel**.

**Gesetz:** An parallelen Geraden sind Stufenwinkel gleich groß.
$$ \alpha_1 = \alpha_2 $$

### B. Wechselwinkel (Z-Winkel)
Wechselwinkel liegen auf entgegengesetzten Seiten der schneidenden Geraden. Man sie sich als Kombination der Scheitelwinkel und Stufenwinkel vorstellen.
Wenn man dem Buchstaben "Z" folgt, liegen die Winkel in den inneren Ecken des Z.

**Gesetz:** An parallelen Geraden sind Wechselwinkel gleich groß.
$$ \alpha_1 = \gamma_2 $$

Diese Gesetze gelten **nur**, wenn die geschnittenen Geraden auch wirklich parallel sind.
Umgekehrt, wenn wir gleich große Stufenwinkel finden, *müssen* die Geraden parallel sein.


    
![png](02_Winkelbeziehungen_files/02_Winkelbeziehungen_4_0.png)
    


## 3. Kongruenz und Ähnlichkeit

In der Geometrie vergleichen wir oft Figuren miteinander, dabei gibt es zwei Abstufungen der "Gleichheit":

### Kongruenz (Deckungsgleichheit)
Zwei Figuren sind **kongruent** ($\cong$), wenn sind in Form und Größe exakt übereinstimmen.
Man könnte eine Figur über die andere legen und nichts würde überstehen.

Matheamtisch bedeutet das: Eine Figur lässt sich durch eine **Kongruenzabbildung** (Verschiebung, Drehung oder Spiegelung) in die andere überführen. Dabei ändern sich weder Seitenlängen noch Winkel.

**Die Kongruenzsätze für Dreicke:**
Um zu bestimmen, ob zwei Dreiecke kongruent sind, müssen nicht alle Eigenschaften des Dreiecks betrachtet werden. Es reicht, wenn folgende Kombinationen übereinstimmen:

1. **SSS:** Alle drei Seiten sind gleich lang.
2. **SWS:** Zwei Seiten und der *eingeschlossene* Winkel sind gleich.
3. **WSW:** Eine Seite und die beiden anliegenden Winkel sind gleich.

*Wichtig: **AAA** (drei gleiche Winkel) ist kein Kongruenzsatz - er garantiert nur Ähnlichkeit, nicht Deckungsgleichheit. Ein gleichseitiges Dreieck mit 60°/60°/60° kann beliebig groß sein.*

### Ähnlichkeit (Formgleichheit)
Zwei Figuren sind **ähnlich** ($\sim$), wenn sie die gleiche Form haben, aber nicht unbedingt die selbe Größe.
Beispiel: Ein Foto, in das man hinein und hinaus zoomt: Das Bild wird größer, aber die Proportionen bleiben gleich (**zentrische Streckung**).

Mathematisch bedeutet das:

1. Alle entsprechenden **Winkel sind gleich groß**.
2. Alle entstprechenden **Seitenverhältnisse sind konstant** (wird Seite $a$ verdoppelt, müssen auch $b$ und $c$ verdoppelt werden).
3. Die Figur lässt sich *zusätzlich* zu **Kongruenzabbildungen** durch **zentrische Streckung** in eine andere überführen.



<div style="padding:0.75rem 1rem; border:1px solid #d8dee9; background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;">(Interaktive Matplotlib-Animation im statischen Export ausgelassen) </div>


---

## Verständnis-Check

**Aufgabe 1: Winkeljagd**
Zwei Geraden schneiden sich. Einer der entstehenden Winkel beträgt $\alpha = 35°$.
Berechne die anderen drei Winkel $\beta, \gamma, \delta$ unter Verwendung der Begriffe *Scheitelwinkel* und *Nebenwinkel*.

**Aufgabe 2: Parallelen-Check**
Eine Gerade schneidet zwei andere Geraden.
- An der oberen Kreuzung ist der Winkel oben rechts $50°$.
- An der unteren Kreuzung ist der Winkel unten links $55°$.
Sind die beiden Geraden parallel? Begründe deine Antwort mit *Scheitel-* und *Stufenwinkeln*.

**Aufgabe 3: Ähnlichkeit**
Du hast ein Foto von einem Dreieck mit den Seitenlängen $a=3$ cm, $b=4$ cm, $c=5$ cm.
Du vergrößerst das Foto auf dem Kopierer um den Faktor 2 (Skalierung).
- Wie lang sind die Seiten des neuen Dreiecks?
- Verändern sich die Innenwinkel des Dreiecks?
- Sind das ursprüngliche und das kopierte Dreieck kongruent?

### Lösungen

<details open><summary>Lösung Aufgabe 1</summary>

- $\gamma = 35°$ (Scheitelwinkel zu $\alpha$, daher gleich groß).
- $\beta = 180° - 35° = 145°$ (Nebenwinkel zu $\alpha$).
- $\delta = 145°$ (Scheitelwinkel zu $\beta$).

</details>

<details open><summary>Lösung Aufgabe 2</summary>

Nein, sie sind nicht parallel.
- Der Winkel oben rechts ist $50°$. Sein Scheitelwinkel (unten links an der oberen Kreuzung) ist ebenfalls $50°$.
- Wären die Geraden parallel, müsste dieser Winkel (50°) als *Stufenwinkel* zum Winkel unten links an der unteren Kreuzung (55°) identisch sein.
- Da $50° \neq 55°$, sind die Geraden nicht parallel.

</details>

<details open><summary>Lösung Aufgabe 3</summary>

- Die neuen Seitenlängen sind $a'=6$ cm, $b'=8$ cm, $c'=10$ cm (jede Seite $\times 2$).
- Die Innenwinkel verändern sich **nicht**. Bei Ähnlichkeit bleiben Winkel erhalten.
- Nein, sie sind **nicht kongruent**, da sie nicht deckungsgleich sind (unterschiedliche Größe). Sie sind **ähnlich**.

</details>

## Zusammenfassung

| Thema | Kernaussage |
|-------|-------------|
| Nebenwinkel | Liegen nebeneinander an einer Geradenkreuzung; ergänzen sich zu $180°$ |
| Scheitelwinkel | Liegen gegenüber an einer Kreuzung; sind immer gleich groß |
| Stufenwinkel (F) | An parallelen Geraden auf gleicher Seite; gleich groß |
| Wechselwinkel (Z) | An parallelen Geraden auf entgegengesetzter Seite; gleich groß |
| Kongruenz ($\cong$) | Gleiche Form und Größe (SSS, SWS, WSW) |
| Ähnlichkeit ($\sim$) | Gleiche Form, aber ggf. andere Größe; konstante Seitenverhältnisse |



---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Schnittpunkt | Intersection (point) |
| Nebenwinkel | Supplementary angles |
| Scheitelwinkel | Vertical angles |
| Stufenwinkel | Corresponding angles |
| Wechselwinkel | Alternate angles |
| Parallel | Parallel |
| Transversale | Transversal |
| Kongruenz | Congruence |
| Ähnlichkeit | Similarity |
| Deckungsgleich | Superimposable / Congruent |
| Verschiebung | Translation |
| Drehung | Rotation |
| Spiegelung | Reflection |
| Skalierung / Zentrische Streckung | Scaling / Homothety / Dilation |
