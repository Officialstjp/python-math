# Geometrie und Trigonometrie

## 04 - Anwendungen der Trigonometrie

Vermessung (Höhen mit $\tan$, Entfernungen über zwei Winkel mit Sinussatz), Schwingungen ($y(t) = A \cdot \sin(\omega t + \varphi)$: Amplitude $A$, Kreisfrequenz $\omega$, Phase $\varphi$) und Vektorzerlegung von Kräften.

> Vorausgesetzt: Sinus/Cosinus, Sinussatz, Kosinussatz (04_Trigonometrie/01-03).

### Lernziele

- Du kannst **Höhen und Entfernungen** mit Trigonometrie berechnen (Vermessung).
- Du verstehst **Schwingungen** als Sinusfunktionen ($y = A \sin(\omega t + \varphi)$).
- Du kannst eine Kraft in **Komponenten** zerlegen (Vektorzerlegung).

---

## 1. Vermessung: Höhen und Entfernungen

### Höhe eines Objekts

Stehst du in Entfernung $d$ von einem Objekt und misst den **Elevationswinkel** $\alpha$ (von der Horizontalen nach oben), dann gilt:

$$h = d \cdot \tan(\alpha)$$

(wobei $h$ ab deiner Augenhöhe gemessen wird.)

### Entfernung über zwei Winkel

Misst du von zwei Standpunkten $A$ und $B$ (Abstand $d$ bekannt) die Winkel $\alpha$ und $\beta$ zum Zielpunkt $C$, kannst du mit dem **Sinussatz** alle fehlenden Größen berechnen.

### Beispiel

Du stehst $50\text{ m}$ von einem Turm entfernt und misst einen Elevationswinkel von $35°$.  
Deine Augenhöhe ist $1{,}7\text{ m}$.

$$h_{\text{Turm}} = 50 \cdot \tan(35°) + 1{,}7 \approx 50 \cdot 0{,}7002 + 1{,}7 \approx 36{,}7\text{ m}$$

## 2. Schwingungen und Wellen

Viele periodische Vorgänge lassen sich als Sinusfunktion beschreiben:

$$y(t) = A \cdot \sin(\omega t + \varphi)$$

| Parameter | Bedeutung | Einheit |
|---|---|---|
| $A$ | **Amplitude** — maximale Auslenkung | je nach Kontext (m, V, …) |
| $\omega = \frac{2\pi}{T} = 2\pi f$ | **Kreisfrequenz** | rad/s |
| $T$ | **Periode** — Dauer einer Schwingung | s |
| $f = \frac{1}{T}$ | **Frequenz** — Schwingungen pro Sekunde | Hz |
| $\varphi$ | **Phase** — horizontale Verschiebung | rad |

### Beispiel: Wechselstrom

Europäische Netzspannung: $U(t) = 325 \cdot \sin(2\pi \cdot 50 \cdot t)$

- Amplitude: $A = 325\text{ V}$ (Spitzenwert)
- Frequenz: $f = 50\text{ Hz}$
- Periode: $T = \frac{1}{50} = 0{,}02\text{ s}$


    
![png](04_Anwendungen_files/04_Anwendungen_3_0.png)
    


## 3. Kräftezerlegung (Vektorzerlegung)

Eine Kraft $\vec F$, die unter einem Winkel $\alpha$ zur Horizontalen wirkt, kann in zwei **Komponenten** zerlegt werden:

- **Horizontale Komponente:** $F_x = F \cdot \cos(\alpha)$
- **Vertikale Komponente:** $F_y = F \cdot \sin(\alpha)$

### Beispiel: Schiefe Ebene

Ein Block ($m = 10\text{ kg}$) liegt auf einer schiefen Ebene mit Neigungswinkel $30°$.  
Die Gewichtskraft ist $F_G = m \cdot g = 98{,}1\text{ N}$ (senkrecht nach unten).

Zerlegung relativ zur Ebene:
- **Hangabtriebskraft** (parallel zur Ebene): $F_{\parallel} = F_G \cdot \sin(30°) = 49{,}05\text{ N}$
- **Normalkraft** (senkrecht zur Ebene): $F_{\perp} = F_G \cdot \cos(30°) \approx 84{,}96\text{ N}$


    
![png](04_Anwendungen_files/04_Anwendungen_5_0.png)
    


---

## Verständnis-Check

**Aufgabe 1: Vermessung**

Du stehst $80\text{ m}$ von einem Gebäude entfernt und misst einen Elevationswinkel von $28°$. Deine Augenhöhe beträgt $1{,}65\text{ m}$.

Wie hoch ist das Gebäude?

**Aufgabe 2: Schwingung ablesen**

Gegeben: $y(t) = 3 \cdot \sin(100\pi t + \frac{\pi}{6})$

a) Bestimme Amplitude, Frequenz und Periode.

b) Was ist der Funktionswert bei $t = 0$?

**Aufgabe 3: Kräftezerlegung**

Ein Seil zieht mit $F = 200\text{ N}$ unter einem Winkel von $40°$ zur Horizontalen an einem Schlitten.

a) Wie groß ist die horizontale Zugkraft $F_x$?

b) Wie groß ist die vertikale Kraft $F_y$?

### Lösungen

<details open><summary>Lösung Aufgabe 1</summary>

$$h = d \cdot \tan(\alpha) + h_{\text{Auge}} = 80 \cdot \tan(28°) + 1{,}65$$
$$h = 80 \cdot 0{,}5317 + 1{,}65 = 42{,}54 + 1{,}65 \approx 44{,}19\text{ m}$$

</details>

<details open><summary>Lösung Aufgabe 2</summary>

a) Amplitude $A = 3$, $\omega = 100\pi$

$$f = \frac{\omega}{2\pi} = \frac{100\pi}{2\pi} = 50\text{ Hz}, \quad T = \frac{1}{f} = 0{,}02\text{ s} = 20\text{ ms}$$

b) $y(0) = 3 \cdot \sin\!\left(\frac{\pi}{6}\right) = 3 \cdot 0{,}5 = 1{,}5$

</details>

<details open><summary>Lösung Aufgabe 3</summary>

a) $F_x = F \cdot \cos(\alpha) = 200 \cdot \cos(40°) = 200 \cdot 0{,}7660 \approx 153{,}21\text{ N}$

b) $F_y = F \cdot \sin(\alpha) = 200 \cdot \sin(40°) = 200 \cdot 0{,}6428 \approx 128{,}56\text{ N}$

</details>

## Zusammenfassung

| Thema | Kernaussage |
|:------|:------------|
| **Vermessung** | Höhen und Entfernungen über $\tan(\alpha)$ und bekannte Abstände berechnen |
| **Schwingungen** | $y(t) = A\sin(\omega t + \varphi)$ — Amplitude, Frequenz $f = \frac{\omega}{2\pi}$, Periode $T = \frac{1}{f}$ |
| **Kräftezerlegung** | $F_x = F\cos(\alpha)$, $F_y = F\sin(\alpha)$ — Projektion auf Achsen |



---

## Glossar

| Deutsch | English |
|---------|---------|
| Vermessung | Surveying |
| Elevationswinkel | Angle of elevation |
| Schwingung | Oscillation |
| Amplitude | Amplitude |
| Frequenz | Frequency |
| Periode | Period |
| Kreisfrequenz | Angular frequency |
| Phase / Phasenverschiebung | Phase / phase shift |
| Kräftezerlegung | Force decomposition |
| Schiefe Ebene | Inclined plane |
| Hangabtriebskraft | Downhill force component |
