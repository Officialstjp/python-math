# Statistik
## 01 - Beschreibende (Deskriptive) Statistik

Die **Statistik** beschäftigt sich mit wissenschaftlichen Methoden des Sammelns, der Gliederung und der Analyse von Daten — und mit dem Ziehen von Schlüssen und Treffen von Entscheidungen aufgrund dieser Analysen.

Man unterscheidet zwei große Bereiche:

| Bereich | Ziel | Methoden |
|---------|------|----------|
| **Beschreibende (deskriptive) Statistik** | Daten erfassen, beschreiben und übersichtlich darstellen | Tabellen, Grafiken, Kenngrößen (Mittelwert, Streuung, …) |
| **Beurteilende (induktive) Statistik** | Von einer Stichprobe auf die Grundgesamtheit schließen | Schätzen, Testen, Konfidenzintervalle |

> **Beachte:** Statistische Aussagen gelten immer nur für eine **große Anzahl** von Objekten. Sie haben im Allgemeinen kaum eine Aussagekraft für einzelne Objekte.

In diesem Notebook befassen wir uns mit der **beschreibenden Statistik** — dem Fundament.

### Lernziele

- Du verstehst die Begriffe **Grundgesamtheit**, **Stichprobe** und **Stichprobenumfang**.
- Du kennst den Unterschied zwischen **Merkmalen** und **Merkmalsausprägungen**.
- Du kannst **qualitative** und **quantitative** Merkmale unterscheiden (inkl. Skalenniveaus).
- Du kannst einfache Daten mit Python erfassen und erste Übersichten erstellen.

---

### 1. Grundbegriffe

Bevor wir Daten analysieren können, müssen wir die Sprache der Statistik verstehen:

#### Grundgesamtheit und Stichprobe

> **Definition:**
> - Die **Grundgesamtheit** ist die **Menge** aller zu beurteilenden Objekte. Ihr **Umfang** $N$ ist die Anzahl der Elemente.
> - Eine **Stichprobe** ist eine **Teilmenge** der Grundgesamtheit, die zur Prüfung **zufällig** entnommen wird. Ihr **Umfang** ist $n$.
> - *Zufällig* bedeutet, dass jedes Objekt der Grundgesamtheit **dieselbe Chance** hat, in die Stichprobe aufgenommen zu werden.
> - Die Stichprobe muss **repräsentativ** sein — d.h. sie muss die typischen Eigenschaften der Grundgesamtheit widerspiegeln.

Im Allgemeinen ist $N$ sehr viel größer als $n$, also $N \gg n$.

**Warum Stichproben?** Eine Vollerhebung (alle $N$ Objekte untersuchen) ist oft zu teuer, zu zeitaufwendig oder schlicht unmöglich. Wenn die Stichprobe repräsentativ ist, können wir von ihr auf die Grundgesamtheit schließen.

---

#### Beispiel: Grundgesamtheit vs. Stichprobe

| Situation | Grundgesamtheit ($N$) | Stichprobe ($n$) |
|-----------|----------------------|-----------------|
| Getränkekonsum Jugendlicher einer Region | Alle Jugendliche (16–20 J.) der Region, $N \approx 12\,000$ | 50 befragte Jugendliche in einer Disco |
| Qualitätskontrolle Schrauben | Tagesproduktion: $N = 5\,000\,000$ | $n = 1\,000$ zufällig geprüfte Stück → $0{,}02\,\%$ |

### 2. Merkmale und Merkmalsausprägungen

Wenn wir Daten erheben, untersuchen wir bestimmte **Eigenschaften** der Objekte. Diese Eigenschaften nennt man **Merkmale**, und die möglichen Werte, die ein Merkmal annehmen kann, heißen **Merkmalsausprägungen**.

> **Definition:**
> - Ein **Merkmal** (auch: Variable) ist eine Eigenschaft, die an den Objekten der Grundgesamtheit untersucht wird.
> - Die **Merkmalsausprägungen** sind die konkreten Werte, die ein Merkmal annehmen kann.

**Beispiel:** Beim Kundenumfrage-Bogen könnte ein Merkmal *„Geschlecht"* sein, mit den Ausprägungen *männlich, weiblich, divers*. Ein anderes Merkmal wäre *„Alter"* mit Ausprägungen wie *18, 25, 42, …*

#### Qualitative vs. Quantitative Merkmale

| Art | Beschreibung | Beispiele |
|-----|-------------|-----------|
| **Qualitativ** | Beschreiben eine Eigenschaft, die **nicht numerisch** messbar ist | Geschlecht, Farbe, Beruf, Religion |
| **Quantitativ** | Beschreiben eine Eigenschaft, die **numerisch** messbar ist | Alter, Einkommen, Temperatur, Gewicht |

Quantitative Merkmale können weiter unterteilt werden:

| Unterart | Beschreibung | Beispiele |
|----------|-------------|-----------|
| **Diskret** | Nur **abzählbar** viele Werte möglich (meist ganzzahlig) | Anzahl Kinder, Würfelaugen, Schulnoten |
| **Stetig** | Kann **jeden** Wert in einem Intervall annehmen | Körpergröße, Temperatur, Zeit |

---

### 3. Skalen in der Statistik (Skalenniveaus)

Das **Skalenniveau** eines Merkmals bestimmt, welche mathematische Operationen sinnvoll sind. Es gibt vier Stufen — von „wenig Information" bis „viel Information":

#### Qualitative Skalen

| Skala | Erklärung | Beispiele | Erlaubte Operationen |
|-------|-----------|-----------|----------------------|
| **Nominalskala** | Die Ausprägungen bilden **keine natürliche Reihenfolge**. Sie stehen gleichberechtigt nebeneinander. Man kann sie nur **unterscheiden**. | Farbe, Autokennzeichen, Geschlecht, Religion | $=$, $\neq$ |
| **Ordinalskala** | Zwischen den Ausprägungen besteht eine **natürliche Reihung** (*„größer als"*-Beziehung). Die **Abstände** sind aber nicht quantifizierbar. | Schulnoten, Güteklassen (Eier, Obst), Rang beim Autorennen | $=$, $\neq$, $<$, $>$ |

> *nomen* (lat.) = Name, Benennung — *ordo* (lat.) = Reihenfolge, Ordnung

#### Metrische (quantitative) Skalen

| Skala | Erklärung | Beispiele | Erlaubte Operationen |
|-------|-----------|-----------|----------------------|
| **Intervallskala** | Abstände zwischen Ausprägungen sind messbar und vergleichbar. Der **Nullpunkt** ist allerdings **willkürlich** festgelegt → **kein sinnvoller Quotient**. | Temperatur in °C/°F, Kalenderzeitrechnung | $=$, $\neq$, $<$, $>$, $+$, $-$ |
| **Verhältnisskala** | Wie Intervallskala, aber mit **absolutem Nullpunkt**. Dadurch sind **Quotienten sinnvoll** (*„doppelt so viel"*). | Körpermasse, Alter, Einkommen, Temperatur in Kelvin | $=$, $\neq$, $<$, $>$, $+$, $-$, $\times$, $\div$ |

> **Beispiel Intervall vs. Verhältnis:** *20 °C ist nicht „doppelt so warm" wie 10 °C* (Intervallskala — willkürlicher Nullpunkt). Aber: *Franz ist doppelt so alt wie Karl* (Verhältnisskala — absoluter Nullpunkt bei 0 Jahren).

> **Merke:** Die Kelvinskala hat einen absoluten Nullpunkt bei 0 K (= $-273{,}15$ °C), deshalb ist Temperatur in Kelvin verhältnisskaliert, während Celsius und Fahrenheit nur intervallskaliert sind.

#### Zusammenfassung: Hierarchie der Skalen

$$\text{Nominalskala} \subset \text{Ordinalskala} \subset \text{Intervallskala} \subset \text{Verhältnisskala}$$

Jede höhere Skala erbt die Eigenschaften der niedrigeren. Je höher das Skalenniveau, desto **mehr statistische Verfahren** können angewandt werden.

---

### 4. Häufigkeitsverteilungen

Eine der ersten Aufgaben der deskriptiven Statistik ist es, die Daten **zusammenzufassen**. Dafür zählen wir, wie oft jede Merkmalsausprägung vorkommt.

#### Absolute und relative Häufigkeit

| Begriff | Symbol | Bedeutung | Formel |
|---------|--------|-----------|--------|
| **Absolute Häufigkeit** | $H_i$ | Wie oft kommt die Ausprägung $x_i$ vor? | Zählung |
| **Relative Häufigkeit** | $h_i$ | Welcher **Anteil** entfällt auf $x_i$? | $h_i = \dfrac{H_i}{n}$ |
| **Kumulierte Häufigkeit** | $F_i$ | Wie groß ist der Anteil **bis einschließlich** $x_i$? | $F_i = \displaystyle\sum_{j=1}^{i} h_j$ |

Es gilt immer:
$$\sum_{i=1}^{k} H_i = n \qquad \text{und} \qquad \sum_{i=1}^{k} h_i = 1$$

> **Kumulierte Häufigkeit** ist nur bei Merkmalen mit einer **natürlichen Reihenfolge** (ab Ordinalskala) sinnvoll.

---

### 5. Diagrammtypen — Darstellung von Häufigkeiten

Die Wahl des **richtigen Diagramms** hängt vom **Skalenniveau** des Merkmals ab:

#### Qualitative Merkmale (Nominal- & Ordinalskala)

| Diagramm | Beschreibung | Wann verwenden? |
|----------|-------------|-----------------|
| **Kreisdiagramm** (Tortendiagramm) | Anteile als Kreissektoren → zeigt die relative Häufigkeit | Gut bei **wenigen** Ausprägungen (z.B. Geschlecht, Lieblingsfach) |
| **Stabdiagramm** (Balkendiagramm) | Einzelne Stäbe pro Ausprägung, **mit Lücken** dazwischen | Standard für qualitative/ordinale Daten |

> **Wichtig:** Stäbe haben Lücken → die Ausprägungen sind **diskrete Kategorien**, nicht zusammenhängend.

#### Metrische Merkmale (Intervall- & Verhältnisskala)

| Diagramm | Beschreibung | Wann verwenden? |
|----------|-------------|-----------------|
| **Histogramm** | Balken **ohne Lücken** — die Breite entspricht dem Klassenintervall, die Höhe (oder Fläche) der Häufigkeit | Für **stetige** oder in Klassen eingeteilte Daten (z.B. Körpergröße, Einkommen) |
| **Boxplot** (Kastengrafik) | Zeigt **Median**, **Quartile**, **Spannweite** und **Ausreißer** auf einen Blick — ideal zum Vergleich mehrerer Verteilungen | Für metrische Daten, wenn **Lage und Streuung** kompakt dargestellt werden sollen |
| **Liniendiagramm / Polygonzug** | Punkte verbunden durch Linien | Für **zeitliche Verläufe** oder geordnete metrische Werte |

> **Histogramm vs. Stabdiagramm:** Beim Histogramm berühren sich die Balken — das zeigt, dass die Werte auf einer **kontinuierlichen Skala** liegen. Beim Stabdiagramm stehen die Stäbe getrennt.

> **Boxplot:** Kommt in **Abschnitt 7** (Streuungsmaße / IQR) vor, da er direkt auf den Quartilen aufbaut.

---


    
![png](01_Beschreibende_Statistik_files/01_Beschreibende_Statistik_9_0.png)
    


### 6. Lagemaße — Wo liegt das „Zentrum" der Daten?

Ein zentrales Ziel der deskriptiven Statistik ist es, einen **typischen** oder **repräsentativen Wert** für einen Datensatz zu finden.

---

#### 6.1 Arithmetisches Mittel (Durchschnitt)

Das **arithmetische Mittel** $\bar{x}$ ist die Summe aller Werte geteilt durch ihre Anzahl:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Eigenschaften:**
- Berücksichtigt **jeden** Datenwert → reagiert empfindlich auf **Ausreißer**
- Sinnvoll ab **Intervallskala** (Abstände müssen vergleichbar sein)

**Beispiel:** Noten $\{2, 1, 3, 2, 1, 4, 2, 3\}$ → $\bar{x} = \frac{2+1+3+2+1+4+2+3}{8} = \frac{18}{8} = 2{,}25$

---

#### 6.2 Gewichtetes Arithmetisches Mittel

In vielen Situationen sollen nicht alle Werte **gleich stark** in den Durchschnitt einfließen — z.B. wenn Schularbeiten stärker zählen als Mitarbeit, oder größere Unternehmen einen Aktienindex stärker beeinflussen.

> **Definition:** Gegeben sind $n$ Werte $x_1, \ldots, x_n$ mit Gewichten $w_1, \ldots, w_n$ ($w_i > 0$). Dann ist das **gewichtete arithmetische Mittel**:
>
> $$\bar{x}_w = \frac{\sum_{i=1}^{n} w_i \cdot x_i}{\sum_{i=1}^{n} w_i}$$

Sind alle Gewichte gleich, ergibt sich das gewöhnliche arithmetische Mittel.

**Beispiel — Zeugnisnote:**

| Prüfung | Note | Gewicht |
|---------|------|---------|
| Schularbeit 1 | 2 | 2 |
| Schularbeit 2 | 3 | 2 |
| Mündlich | 1 | 1 |
| Mitarbeit | 2 | 1 |

$$\bar{x}_w = \frac{2 \cdot 2 + 2 \cdot 3 + 1 \cdot 1 + 1 \cdot 2}{2 + 2 + 1 + 1} = \frac{13}{6} \approx 2{,}17 \qquad \text{(ungewichtet: } \bar{x} = 2{,}0\text{)}$$

> **Zusammenhang mit Häufigkeiten:** Relative Häufigkeiten $h_i$ können als Gewichte aufgefasst werden: $\bar{x} = \sum_{j=1}^{k} h_j \cdot x_j$

---


    
![png](01_Beschreibende_Statistik_files/01_Beschreibende_Statistik_11_0.png)
    


#### 6.3 Median (Zentralwert)

Der **Median** $\tilde{x}$ teilt die **geordnete** Datenreihe in zwei gleich große Hälften — 50 % der Werte liegen darunter, 50 % darüber.

**Berechnung:**
1. Daten der Größe nach ordnen: $x_{(1)} \leq x_{(2)} \leq \cdots \leq x_{(n)}$
2. Dann:

$$\tilde{x} = \begin{cases} x_{\left(\frac{n+1}{2}\right)} & \text{wenn } n \text{ ungerade} \\[6pt] \dfrac{1}{2}\left(x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}\right) & \text{wenn } n \text{ gerade} \end{cases}$$

**Eigenschaften:**
- **Robust** gegenüber Ausreißern (ein einzelner Extremwert ändert den Median kaum)
- Sinnvoll ab **Ordinalskala**

**Beispiel:** Geordnete Noten $\{1, 1, 2, 2, 2, 3, 3, 4\}$ → $n = 8$ (gerade) → $\tilde{x} = \frac{x_{(4)} + x_{(5)}}{2} = \frac{2 + 2}{2} = 2{,}0$

---

#### 6.4 Modus (Modalwert)

Der **Modus** $x_{\text{mod}}$ ist der Wert, der am **häufigsten** vorkommt.

**Eigenschaften:**
- Das einzige Lagemaß, das schon ab der **Nominalskala** sinnvoll ist (z.B. „häufigste Farbe")
- Kann **mehrdeutig** sein: zwei Werte mit gleicher Höchsthäufigkeit → **bimodal**; mehrere → **multimodal**
- Bei stetigen Daten oft wenig aussagekräftig → dann Klassen bilden

**Beispiel:** Noten $\{1, 1, 2, 2, 2, 3, 3, 4\}$ → $x_{\text{mod}} = 2$ (kommt 3× vor)

---

#### Wann welches Lagemaß?

| Situation | Empfehlung |
|-----------|------------|
| Symmetrische Verteilung, keine Ausreißer | **Arithmetisches Mittel** — nutzt alle Informationen |
| Unterschiedliche Bedeutung der Werte | **Gewichtetes Mittel** — berücksichtigt Wichtigkeit |
| Schiefe Verteilung oder Ausreißer vorhanden | **Median** — robuster, weniger verzerrt |
| Ordinalskala (z.B. Schulnoten) | **Median** — Abstände nicht gleich, Mittel fragwürdig |
| Nominalskala (z.B. Farbe, Geschlecht) | **Modus** — einziges sinnvolles Lagemaß |

> **Faustregel:** Wenn Mittelwert und Median stark voneinander abweichen, ist die Verteilung **schief** oder es gibt **Ausreißer**.

---


    
![png](01_Beschreibende_Statistik_files/01_Beschreibende_Statistik_13_0.png)
    


### 7. Streuungsmaße — Wie stark streuen die Daten?

Lagemaße allein reichen nicht aus — zwei Datensätze können denselben Mittelwert haben, aber völlig unterschiedlich verteilt sein. **Streuungsmaße** beschreiben, wie weit die Werte um das Zentrum herum verteilt sind.

#### Spannweite (Range)

Das einfachste Streuungsmaß — die Differenz zwischen dem größten und dem kleinsten Wert:

$$R = x_{\max} - x_{\min}$$

**Vorteil:** Leicht zu berechnen.
**Nachteil:** Berücksichtigt nur 2 Werte → extrem **empfindlich** gegenüber Ausreißern.

---

#### Quartile und Interquartilsabstand (IQR)

Quartile teilen die geordnete Datenreihe in **vier gleich große Teile**:

| Quartil | Symbol | Bedeutung |
|---------|--------|-----------|
| Unteres Quartil | $Q_1$ | 25 % der Werte liegen darunter |
| Median | $Q_2 = \tilde{x}$ | 50 % der Werte liegen darunter |
| Oberes Quartil | $Q_3$ | 75 % der Werte liegen darunter |

Der **Interquartilsabstand** (IQR) misst die Streuung der "mittleren 50 %" der Daten:

$$\text{IQR} = Q_3 - Q_1$$

> **Vorteil:** Robust gegenüber Ausreißern — genau wie der Median ignoriert der IQR die extremen Werte.

---

#### Der Boxplot (Kastengrafik)

Der **Boxplot** fasst die wichtigsten Lagemaße und Streuungsmaße in einer einzigen Grafik zusammen:

| Bestandteil | Bedeutung |
|-------------|-----------|
| **Box** (Kasten) | Reicht von $Q_1$ bis $Q_3$ → enthält die mittleren 50 % der Daten |
| **Strich in der Box** | Median ($Q_2 = \tilde{x}$) |
| **Whisker** (Antennen) | Reichen bis zum letzten Datenpunkt innerhalb von $1{,}5 \cdot \text{IQR}$ ab $Q_1$ bzw. $Q_3$ |
| **Punkte** außerhalb | **Ausreißer** — Werte jenseits der Whisker |

> **Warum $1{,}5 \cdot \text{IQR}$?** Bei einer Normalverteilung liegen ca. 99,3 % aller Werte innerhalb dieser Grenzen. Alles außerhalb ist „ungewöhnlich".

Der Boxplot eignet sich besonders gut zum **Vergleich** mehrerer Gruppen, da Lage und Streuung auf einen Blick erkennbar sind.

---


    
![png](01_Beschreibende_Statistik_files/01_Beschreibende_Statistik_15_0.png)
    


#### Varianz und Standardabweichung

Wir brauchen ein Streuungsmaß, das **alle** Datenwerte berücksichtigt. Die Idee: Messen, wie weit jeder Wert vom Mittelwert $\bar{x}$ abweicht.

**Warum nicht einfach den Durchschnitt der Abweichungen nehmen?**

$$\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x}) = 0 \quad \text{(immer!)}$$

Positive und negative Abweichungen heben sich gegenseitig auf. Lösung: Die Abweichungen **quadrieren**.

---

#### Empirische Varianz $s^2$

> **Definition:** Die **empirische Varianz** ist das arithmetische Mittel der quadrierten Abweichungen vom Mittelwert:
>
> $$s^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

Alternativ mit Häufigkeiten (wenn $k$ verschiedene Ausprägungen $x_1, \ldots, x_k$ mit absoluten Häufigkeiten $H_1, \ldots, H_k$):

$$s^2 = \frac{1}{n} \sum_{j=1}^{k} H_j \cdot (x_j - \bar{x})^2 = \sum_{j=1}^{k} h_j \cdot (x_j - \bar{x})^2$$

> **Hinweis:** Manchmal wird statt $\frac{1}{n}$ der Faktor $\frac{1}{n-1}$ verwendet (sog. **korrigierte Stichprobenvarianz**). Für die beschreibende Statistik (gesamte Daten bekannt) verwenden wir $\frac{1}{n}$.

---

#### Standardabweichung $s$

Die Varianz hat den Nachteil, dass sie in **quadrierten Einheiten** angegeben ist (z.B. €²). Die **Standardabweichung** behebt das:

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

> Die Standardabweichung hat **dieselbe Einheit** wie die Daten und ist daher direkt interpretierbar: *„Die Werte weichen im Durchschnitt um $s$ vom Mittelwert ab."*

#### Zusammenfassung: Streuungsmaße im Überblick

| Maß | Formel | Robust? | Sinnvoll ab |
|-----|--------|---------|-------------|
| **Spannweite** $R$ | $x_{\max} - x_{\min}$ | Nein | Ordinalskala |
| **IQR** | $Q_3 - Q_1$ | Ja | Ordinalskala |
| **Varianz** $s^2$ | $\frac{1}{n}\sum(x_i - \bar{x})^2$ | Nein | Intervallskala |
| **Standardabweichung** $s$ | $\sqrt{s^2}$ | Nein | Intervallskala |

---


    
![png](01_Beschreibende_Statistik_files/01_Beschreibende_Statistik_17_0.png)
    

