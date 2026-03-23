# Geometrie und Trigonometrie

## 02 – Trigonometrie 2: Einheitskreis und Funktionen

Im vorigen Kapitel haben wir Sinus und Cosinus als Seitenverhältnisse im rechtwinkligen Dreieck kennengelernt. Das hat ein Problem: Ein Dreieck kann keinen Winkel haben, der größer als $90^\circ$ ist (da die Winkelsumme $180^\circ$ ist).

In der Physik und Technik (z.B. bei Schwingungen, Wechselstrom, Wellen) brauchen wir aber Funktionen, die für **alle** Winkel definiert sind und sich periodisch wiederholen.

### Lernziele

- Du verstehst den **Einheitskreis** als Erweiterung des Dreiecks.
- Du lernst die **Graphen** von Sinus und Cosinus kennen (Wellenform).
- Du verstehst **Symmetrien** (warum es oft zwei Lösungen für einen Winkel gibt).
- Du lernst Strategien zum **Lösen trigonometrischer Gleichungen** (Substitution).

## 1. Der Einheitskreis (The Unit Circle)

Statt eines beliebigen Dreiecks betrachten wir einen Kreis mit Radius $r=1$ im Koordinatensystem.
Der Mittelpunkt liegt bei $(0|0)$.

Jeder Winkel $\alpha$ (gemessen von der positiven x-Achse gegen den Uhrzeigersinn) definiert einen Punkt $P$ auf dem Kreis:

$$P = (\cos\alpha,\ \sin\alpha)$$

- Die **x-Koordinate** dieses Punktes ist der **Cosinus**.
- Die **y-Koordinate** dieses Punktes ist der **Sinus**.

Damit können wir plötzlich auch den Sinus von $120°$ oder $-30°$ bestimmen - das Dreieck ist nicht mehr nötig.

### Wertetabelle (wichtige Winkel)

| $\alpha$ | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $270°$ | $360°$ |
|---|---|---|---|---|---|---|---|---|
| $\sin\alpha$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ | $0$ | $-1$ | $0$ |
| $\cos\alpha$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ | $0$ | $1$ |
| $\tan\alpha$ | $0$ | $\frac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | - | $0$ | - | $0$ |

### Bogenmaß (Radians)

Neben der Gradangabe gibt es das **Bogenmaß**: Die Bogenlänge auf dem Einheitskreis.

$$\text{rad} = \text{deg} \cdot \frac{\pi}{180}$$

| Grad | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $360°$ |
|---|---|---|---|---|---|---|---|
| Bogenmaß | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $2\pi$ |

> **Merke:** In der Mathematik und Physik wird fast immer das Bogenmaß verwendet. Python-Funktionen wie `math.sin()` erwarten ebenfalls Bogenmaß.


    
![png](02_Einheitskreis_und_Funktionen_files/02_Einheitskreis_und_Funktionen_2_0.png)
    



    
![png](02_Einheitskreis_und_Funktionen_files/02_Einheitskreis_und_Funktionen_2_1.png)
    



    
![png](02_Einheitskreis_und_Funktionen_files/02_Einheitskreis_und_Funktionen_2_2.png)
    


## 2. Die Funktionsgraphen (Wellen)

Wenn wir den Winkel $\alpha$ (oder $x$) auf der horizontalen Achse abtragen und den Sinuswert auf der vertikalen, entsteht die typische Wellenform.

Wichtige Eigenschaften:
- **Periode:** $360^\circ$ oder $2\pi$. Danach wiederholt sich alles.
- **Amplitude:** Pendelt zwischen $+1$ und $-1$.
- **Nullstellen:** Wo schneidet die Kurve die Achse?


    
![png](02_Einheitskreis_und_Funktionen_files/02_Einheitskreis_und_Funktionen_4_0.png)
    


## 3. Symmetrie und Vorzeichen

Der Taschenrechner gibt bei `asin(0.5)` oft nur einen Wert zurück ($30°$). Aber im Kreis gibt es oft einen zweiten Winkel, der den gleichen Sinuswert hat.

### Vorzeichen in den Quadranten

| Quadrant | Winkelbereich | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|---|
| I   | $0°$–$90°$     | $+$ | $+$ | $+$ |
| II  | $90°$–$180°$   | $+$ | $-$ | $-$ |
| III | $180°$–$270°$  | $-$ | $-$ | $+$ |
| IV  | $270°$–$360°$  | $-$ | $+$ | $-$ |

### Wichtige Symmetrien
- **Sinus:** $\sin(180° - \alpha) = \sin(\alpha)$ - Spiegelung an der y-Achse im Kreis
- **Cosinus:** $\cos(360° - \alpha) = \cos(\alpha)$ - Spiegelung an der x-Achse im Kreis
- **Tangens:** $\tan(\alpha + 180°) = \tan(\alpha)$ - Periode $180°$

### Fundamentale Identität

Direkt aus dem Einheitskreis (Satz des Pythagoras auf das Dreieck mit Hypotenuse $r=1$):

$$\sin^2(\alpha) + \cos^2(\alpha) = 1$$

Daraus abgeleitet:
- $\sin^2(\alpha) = 1 - \cos^2(\alpha)$
- $\cos^2(\alpha) = 1 - \sin^2(\alpha)$


    
![png](02_Einheitskreis_und_Funktionen_files/02_Einheitskreis_und_Funktionen_6_0.png)
    


## 4. Lösen trigonometrischer Gleichungen

Hier wird es algebraisch. Wir suchen alle $x$ in einem Intervall $[0, 2\pi]$ (bzw. $[0°, 360°]$).

### A. Einfache Gleichungen

**Beispiel:** $\sin(x) = 0{,}5$ im Intervall $[0, 2\pi]$

1. Taschenrechner / Tabelle: $x_1 = \arcsin(0{,}5) = \frac{\pi}{6}$ (= $30°$)
2. Symmetrie beachten: $x_2 = \pi - x_1 = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$ (= $150°$)

**Lösung:** $x \in \left\{\frac{\pi}{6},\ \frac{5\pi}{6}\right\}$

### B. Substitution (komplexe Argumente)

**Beispiel:** $\sin(2x) = 0{,}5$ im Intervall $[0, 2\pi]$

1. **Substituiere** $u = 2x$. Neues Intervall: $u \in [0, 4\pi]$
2. Löse $\sin(u) = 0{,}5$: $u_1 = \frac{\pi}{6},\ u_2 = \frac{5\pi}{6}$
3. Periodenwiederholungen im erweiterten Intervall: $u_3 = \frac{\pi}{6} + 2\pi = \frac{13\pi}{6},\ u_4 = \frac{5\pi}{6} + 2\pi = \frac{17\pi}{6}$
4. **Rücksubstitution** $x = \frac{u}{2}$: $x \in \left\{\frac{\pi}{12},\ \frac{5\pi}{12},\ \frac{13\pi}{12},\ \frac{17\pi}{12}\right\}$

### C. Quadratische Form

**Beispiel:** $2\sin^2(x) - 1 = 0$

1. Umstellen: $\sin^2(x) = \frac{1}{2} \Rightarrow \sin(x) = \pm\frac{\sqrt{2}}{2}$
2. Alle Winkel mit $\sin(x) = \frac{\sqrt{2}}{2}$: $x = \frac{\pi}{4},\ \frac{3\pi}{4}$
3. Alle Winkel mit $\sin(x) = -\frac{\sqrt{2}}{2}$: $x = \frac{5\pi}{4},\ \frac{7\pi}{4}$

**Lösung:** $x \in \left\{\frac{\pi}{4},\ \frac{3\pi}{4},\ \frac{5\pi}{4},\ \frac{7\pi}{4}\right\}$

## Zusammenfassung

| Thema | Kernaussage |
|-------|-------------|
| Einheitskreis | $P = (\cos\alpha, \sin\alpha)$ auf dem Kreis mit $r=1$ |
| Bogenmaß | $\text{rad} = \text{deg} \cdot \frac{\pi}{180}$; Vollkreis = $2\pi$ |
| Graphen | Sinus und Cosinus sind periodische Wellen (Periode $2\pi$, Amplitude $1$) |
| Quadrantenregel | Vorzeichen von $\sin$/$\cos$ hängt vom Quadranten ab |
| Fundamentale Identität | $\sin^2(\alpha) + \cos^2(\alpha) = 1$ |
| Gleichungen lösen | Symmetrie beachten → oft 2 Lösungen; Substitution bei $\sin(nx)$ |

> **Nächster Schritt:** Weiter zum **Allgemeinen Dreieck** – Sinussatz und Kosinussatz für beliebige (nicht-rechtwinklige) Dreiecke.

---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Einheitskreis | Unit circle |
| Bogenmaß | Radians |
| Gradmaß | Degrees |
| Periode | Period |
| Amplitude | Amplitude |
| Nullstelle | Zero / root |
| Symmetrie | Symmetry |
| Quadrant | Quadrant |
| Trigonometrische Gleichung | Trigonometric equation |
| Substitution | Substitution |
| Rücksubstitution | Back-substitution |
| Funktionsgraph | Function graph |
| Wertetabelle | Value table |
| Fundamentale Identität | Fundamental identity |
