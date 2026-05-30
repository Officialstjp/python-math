# Analysis
## 01 - Analysis 1: Einführung und die Ableitung

### Was ist Analysis?

Die Analysis (Infinitesimalrechnung) ist eines der mächtigsten Werkzeuge der Mathematik. Ihre zentrale Frage: **Wie beschreibt man Veränderung mathematisch exakt?** 

#### 1. Die drei Säulen der Analysis

Die Analysis besteht aus drei eng verbundenen Konzepten:

| Säule | Kernfrage | Werkzeug |
|-------|-----------|----------|
| **Grenzwerte** | Was passiert, wenn wir uns einem Wert *unendlich nah* annähern? | $\lim_{x \to a} f(x)$ |
| **Differentialrechnung** | Wie schnell ändert sich eine Funktion? Was ist die Steigung? | $f'(x) = \frac{df}{dx}$ |
| **Integralrechnung** | Wie groß ist die Fläche unter einer Kurve? Was ist das Gegenteil der Ableitung? | $\int f(x)\,dx$ |

Diese drei Konzepte sind eng miteinander verknüpft: Die Ableitung baut auf dem Grenzwertbegriff auf, und der **Hauptsatz der Analysis** stellt eine überraschende Verbindung her - Ableiten und Integrieren sind Umkehroperationen voneinander. Was genau das bedeutet, entfaltet sich schrittweise in den kommenden Notebooks.

##### Die große Idee

Viele Größen in der Natur verändern sich *ständig*. Ein Auto beschleunigt, die Temperatur schwankt, eine Population wächst. Die Analysis gibt uns die Sprache, um solche **kontinuierlichen Veränderungen** präzise zu beschreiben.

---

#### 2. Wozu braucht man Analysis?

Einige Beispiele, in denen Analysis unverzichtbar ist:

| Bereich | Anwendung | Analysis-Werkzeug |
|---------|-----------|-------------------|
| **Physik** | Bewegung, Kräfte, Energie | Ableitungen (Geschwindigkeit, Beschleunigung) |
| **Ingenieurwesen** | Optimierung von Formen, Materialien | Extremwertprobleme (Kurvendiskussion) |
| **Wirtschaft** | Gewinnmaximierung, Kostenfunktionen | Ableitung = Grenzkosten/Grenzertrag |
| **Medizin** | Medikamentenabbau im Körper | Differentialgleichungen (exp. Zerfall) |
| **Informatik / KI** | Maschinelles Lernen, neuronale Netze | Gradient Descent (partielle Ableitungen) |
| **Statistik** | Wahrscheinlichkeitsverteilungen | Integrale (Fläche unter der Verteilung) |

#### 3. Voraussetzungen

Vor der Analysis solltest Du mit folgenden Konzepten vertraut sein:
- **Funktionen** - Funktionsbegriff, Darstellungsformen, Graphen lesen 
- **Polynome** - Quadratische Funktionen, Parabeln
- **Exponential- und Logarithmusfunktionen** - $e^x$, $\ln(x)$ 
- **Trigonometrie** - $\sin$, $\cos$, $\tan$ 
- **Grenzwerte** - Grundlage in der Analysis

> **Hinweis:** Notebooks/Kapitel 06 und 07 (Partielle Ableitungen, Multivariate Kettenregel) gehen über den typischen Matura-Stoff hinaus und können bei Bedarf übersprungen werden.

---

## Ableitungen

Ableitung als momentane Änderungsrate — vom Differenzenquotienten $\frac{f(x+h)-f(x)}{h}$ (Sekantensteigung) über den Grenzübergang $h \to 0$ zur Tangentensteigung $f'(x) = \lim_{h\to 0} \frac{f(x+h)-f(x)}{h}$; Notationen: $f'(x)$, $\frac{df}{dx}$, $\dot f$.

> Vorausgesetzt: Grenzwerte (02_Funktionen/02).

### Lernziele

- **Was eine Ableitung ist** und warum sie die Steigung einer Kurve beschreibt
- **Den Übergang von der Sekante zur Tangente** visuell zu verstehen
- **Die Ableitung numerisch zu berechnen** mithilfe der Grenzwertdefinition
- **Die Ableitung symbolisch zu berechnen** mit SymPy
- **Die verschiedenen Notationen** der Ableitung ($f'(x)$, $\frac{df}{dx}$, $\dot f$)

---

### 1. Die Durchschnittliche & momentane Steigung

Bei einer Geraden, z.B. $y = 2x + 1$, ist die Steigung überall gleich. Für jeden Schritt in $x$ steigt $y$ um 2. Die Steigung ist konstant **2**.

Aber was ist mit einer Kurve wie $f(x) = x^2$? Die Steilheit dieser Funktion ändert sich ständig. Bei $x=10$ ist sie sehr steil, bei $x=0$ fast flach.

Die **Ableitung** einer Funktion an einer bestimmten Stelle ist die **Steigung der Kurve genau an diesem Punkt**.

#### Das Steigungsdreieck
Um die Steigung zu verstehen, beginnen wir mit dem **Steigungsdreieck** (auch: Differenzenquotient). Wir wählen zwei Punkte auf der Kurve und zeichnen eine Gerade durch sie - die **Sekante**. Ihre Steigung ist die *durchschnittliche* Änderungsrate zwischen diesen beiden Punkten.

Die Steigung einer Geraden zwischen zwei Punkten $(x_1, y_1)$ und $(x_2, y_2)$ ist:
$$
m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
$$

In Funktionsnotation: Wenn wir einen Punkt $x$ und einen zweiten Punkt $x + h$ haben (wobei $h$ eine kleine Änderung in $x$ ist), ist die Sekantensteigung:
$$
m_{\text{Sekante}} = \frac{f(x+h) - f(x)}{(x+h) - x} = \frac{f(x+h) - f(x)}{h}
$$

Diesen Ausdruck nennt man den **Differenzenquotienten**.

Die Kernidee der Analysis: **Was passiert, wenn wir $h$ unendlich klein machen?** Wenn der zweite Punkt immer näher an den ersten rückt, wird die Sekante zur **Tangente** - einer Geraden, die die Kurve in genau einem Punkt berührt.

Die Steigung dieser Tangente ist die Ableitung.

*Hinweis: Du kannst sowohl $h$ als auch $\Delta x$ als Notation für die Änderung in $x$ verwenden - beide sind gleichwertig. In diesem Abschnitt verwenden wir $h$.*


    
![png](01_Einf%C3%BChrung_Ableitung_files/01_Einf%C3%BChrung_Ableitung_3_0.png)
    


### 2. Die Ableitung berechnen

Der obige Prozess wird durch die **Grenzwertdefinition der Ableitung** formalisiert:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

Die Notation $f'(x)$ (gesprochen: „f Strich von x") ist eine der üblichen Schreibweisen. Die wichtigsten Notationen sind:

| Notation | Name | Wann verwendet |
|----------|------|---------------|
| $f'(x)$ | Lagrange-Notation | Am häufigsten in der Schulmathematik |
| $\frac{df}{dx}$ oder $\frac{dy}{dx}$ | Leibniz-Notation | Betont die Variablen, nützlich bei Kettenregel |
| $\dot{f}$ | Newton-Notation | Vor allem in der Physik (Ableitung nach der Zeit) |

Machen wir daraus eine Python-Funktion! Wir können $h$ nicht wirklich Null setzen (Division durch Null!), aber wir können es sehr klein machen, z.B. $h = 1 \cdot 10^{-7}$.

    Ableitung von f(x)=x² bei x=1: 2.000000  (exakt: 2)
    Ableitung von f(x)=x² bei x=3: 6.000000  (exakt: 6)
    Ableitung von g(x)=x³+2x bei x=2: 14.000001  (exakt: 14)
    

    Bei x=1.0: Punkt (1.00, 1.00), Steigung ≈ 2.00
    Bei x=3.0: Punkt (3.00, 9.00), Steigung ≈ 6.00
    Bei x=2.0: Punkt (2.00, 12.00), Steigung ≈ 14.00
    


    
![png](01_Einf%C3%BChrung_Ableitung_files/01_Einf%C3%BChrung_Ableitung_6_1.png)
    


### 3. Die exakte Ableitung mit SymPy

Unsere `numerische_ableitung`-Funktion ist nützlich für die Intuition, aber sie liefert nur eine **Näherung**. Für exakte Ergebnisse brauchen wir symbolische Mathematik. Das geht mit der Bibliothek `sympy`. Sie behandelt Variablen als Symbole, nicht als Zahlen.

Die Ableitung von $f(x) = x^2$ exakt mit SymPy berechnen:
```python
import sympy as sp

# 1. Variable als mathematisches Symbol deklarieren
x = sp.Symbol('x')

# 2. Funktion symbolisch definieren
f_sym = x**2

# 3. Ableitung berechnen mit sp.diff()
f_abl = sp.diff(f_sym, x)
```

    Die Funktion ist:  f(x) = x**2
    Die Ableitung ist: f'(x) = 2*x
    
    Die Funktion ist:  g(x) = x**3 + 2*x
    Die Ableitung ist: g'(x) = 3*x**2 + 2
    
    g'(2) = 14  (das bestätigt unsere numerische Berechnung!)
    

---

## Verständnis-Check
*Diese Aufgaben sind zum Üben auf Papier gedacht!*

**Aufgabe 1:** Berechne den Differenzenquotienten für $f(x) = x^2$ zwischen $x = 2$ und $x = 2{,}5$.
$$\frac{f(2{,}5) - f(2)}{2{,}5 - 2} = \frac{? - ?}{?} = \, ?$$

**Aufgabe 2:** Berechne die Ableitung $f'(x)$ für $f(x) = x^2$ an der Stelle $x = 3$ mit der Grenzwertdefinition. (Setze $f(x+h)$ ein und vereinfache!)

**Aufgabe 3:** Gegeben ist $f(x) = 3x^2 + 4x - 1$. Berechne den Differenzenquotienten für $x = 1$ und $h = 0{,}1$.

**Aufgabe 4:** Welche Steigung hat die Tangente an $f(x) = x^3$ bei $x = 2$? (Benutze die Grenzwertdefinition oder SymPy.)

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

$$\frac{f(2{,}5) - f(2)}{0{,}5} = \frac{6{,}25 - 4}{0{,}5} = \frac{2{,}25}{0{,}5} = 4{,}5$$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

$$f'(3) = \lim_{h \to 0} \frac{(3+h)^2 - 9}{h} = \lim_{h \to 0} \frac{9 + 6h + h^2 - 9}{h} = \lim_{h \to 0} \frac{6h + h^2}{h} = \lim_{h \to 0} (6 + h) = 6$$
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

$$\frac{f(1{,}1) - f(1)}{0{,}1} = \frac{3(1{,}21) + 4(1{,}1) - 1 - (3 + 4 - 1)}{0{,}1} = \frac{7{,}03 - 6}{0{,}1} = 10{,}3$$
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

$$f'(x) = 3x^2 \Rightarrow f'(2) = 3 \cdot 4 = 12$$
</details>

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| **Ableitung** | Momentane Steigung einer Kurve an einem Punkt |
| **Sekante → Tangente** | Übergang durch Grenzwert $h \to 0$ |
| **Differenzenquotient** | $\frac{f(x+h)-f(x)}{h}$ — Näherung der Ableitung |
| **Grenzwertdefinition** | $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ — exakte Definition |
| **SymPy** | Berechnet Ableitungen symbolisch (exakt) |


---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Ableitung | Derivative |
| Steigung | Slope |
| Tangente | Tangent (line) |
| Sekante | Secant (line) |
| Steigungsdreieck | Slope triangle |
| Differenzenquotient | Difference quotient |
| Grenzwert | Limit |
| Momentane Änderungsrate | Instantaneous rate of change |
| Durchschnittliche Änderungsrate | Average rate of change |
