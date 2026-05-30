# Glossar
## Statistik und Wahrscheinlichkeitsrechnung

Kompaktes Nachschlagewerk aller Begriffe, Symbole und Formeln aus der Reihe 08 — Statistik und Wahrscheinlichkeit, sortiert nach Thema (Grundbegriffe, Skalenniveaus, Häufigkeiten, Lagemaße, Streuungsmaße, Korrelation/Regression, Wahrscheinlichkeitsrechnung).

**Quellen:**
- 01 — Beschreibende Statistik
- 02 — Korrelation und Regression
- 03 — Wahrscheinlichkeitsrechnung

---

### 1. Grundbegriffe der Statistik

| Begriff | Symbol | Bedeutung |
|---------|--------|-----------|
| **Grundgesamtheit** | $N$ | Menge aller zu untersuchenden Objekte; $N$ = Umfang |
| **Stichprobe** | $n$ | Zufällig entnommene Teilmenge der Grundgesamtheit; $n$ = Umfang |
| **Merkmal / Variable** | — | Eigenschaft, die an den Objekten untersucht wird |
| **Merkmalsausprägung** | — | Konkreter Wert, den ein Merkmal annehmen kann |
| **Qualitatives Merkmal** | — | Nicht numerisch messbar (Farbe, Geschlecht, Beruf) |
| **Quantitatives Merkmal** | — | Numerisch messbar; **diskret** (abzählbar) oder **stetig** (jeder Wert in einem Intervall) |
| **Repräsentativität** | — | Stichprobe spiegelt typische Eigenschaften der Grundgesamtheit wider |

---

### 2. Skalenniveaus

| Skala | Erlaubte Operationen | Beispiele |
|-------|---------------------|-----------|
| **Nominalskala** | $=$, $\neq$ | Farbe, Geschlecht, Autokennzeichen |
| **Ordinalskala** | $=$, $\neq$, $<$, $>$ | Schulnoten, Rangfolgen, Güteklassen |
| **Intervallskala** | $=$, $\neq$, $<$, $>$, $+$, $-$ | Temperatur in °C, Kalenderdaten |
| **Verhältnisskala** | alle Grundoperationen | Masse, Alter, Einkommen, Kelvin |

$$\text{Nominal} \subset \text{Ordinal} \subset \text{Intervall} \subset \text{Verhältnis}$$

Jede höhere Stufe erbt die Operationen der unteren und fügt neue hinzu.

---

### 3. Häufigkeiten

| Begriff | Symbol | Formel | Bedeutung |
|---------|--------|--------|-----------|
| **Absolute Häufigkeit** | $H_i$ | (Zählung) | Wie oft kommt Ausprägung $x_i$ vor? |
| **Relative Häufigkeit** | $h_i$ | $h_i = \frac{H_i}{n}$ | Anteil von $x_i$ an der Gesamtzahl |
| **Kumulierte Häufigkeit** | $F_i$ | $F_i = \sum_{j=1}^{i} h_j$ | Anteil bis einschließlich $x_i$ |

Erhaltung: $\sum H_i = n$ und $\sum h_i = 1$.

---

### 4. Lagemaße

| Maß | Symbol | Formel | Ab Skala | Robust? |
|-----|--------|--------|----------|---------|
| **Arithmetisches Mittel** | $\bar{x}$ | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ | Intervall | Nein |
| **Gewichtetes Mittel** | $\bar{x}_w$ | $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$ | Intervall | Nein |
| **Mittel aus Häufigkeiten** | $\bar{x}$ | $\bar{x} = \sum_{j=1}^{k} h_j \cdot x_j$ | Intervall | Nein |
| **Median** | $\tilde{x}$ | Mittlerer Wert der geordneten Reihe | Ordinal | Ja |
| **Modus** | $x_{\text{mod}}$ | Häufigster Wert | Nominal | Ja |

**Median-Berechnung:**

$$\tilde{x} = \begin{cases} x_{\left(\frac{n+1}{2}\right)} & n \text{ ungerade} \\[6pt] \frac{1}{2}\left(x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}\right) & n \text{ gerade} \end{cases}$$

---

### 5. Streuungsmaße

| Maß | Symbol | Formel | Robust? |
|-----|--------|--------|---------|
| **Spannweite** | $R$ | $R = x_{\max} - x_{\min}$ | Nein |
| **Quartile** | $Q_1, Q_3$ | 25.‑ bzw. 75.‑Perzentil | Ja |
| **Interquartilsabstand** | $IQR$ | $IQR = Q_3 - Q_1$ | Ja |
| **Varianz** | $s^2$ | $s^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$ | Nein |
| **Standardabweichung** | $s$ | $s = \sqrt{s^2}$ | Nein |

**Varianz mit Häufigkeiten:** $\displaystyle s^2 = \sum_{j=1}^{k} h_j (x_j - \bar{x})^2$

**Verschiebungssatz:** $\displaystyle s^2 = \overline{x^2} - \bar{x}^2 = \frac{1}{n}\sum x_i^2 - \bar{x}^2$

**Boxplot-Komponenten:**

| Element | Bedeutung |
|---------|-----------|
| **Kasten** | Von $Q_1$ bis $Q_3$ (mittlere 50%) |
| **Linie** | Median $\tilde{x}$ |
| **Whisker** | Bis letzter Wert innerhalb $1{,}5 \cdot IQR$ |
| **Punkte** | Ausreißer jenseits der Whisker |

> **Hinweis:** In der deskriptiven Statistik verwenden wir den Divisor $\frac{1}{n}$. Am TI-Nspire entspricht das dem Wert $\sigma_x$, **nicht** $s_x$ (welcher $\frac{1}{n-1}$ verwendet).

---

### 6. Diagrammtypen

| Diagramm | Skalenniveau | Merkmal |
|----------|-------------|---------|
| **Kreisdiagramm** | Nominal / Ordinal | Relative Häufigkeiten als Sektoren; wenige Ausprägungen |
| **Stabdiagramm** | Nominal / Ordinal | Stäbe **mit Lücken** — diskrete, qualitative Daten |
| **Histogramm** | Intervall / Verhältnis | Balken **ohne Lücken** — stetige oder klassierte Daten |
| **Boxplot** | Ordinal aufwärts | Median, Quartile, Spannweite, Ausreißer auf einen Blick |
| **Liniendiagramm** | Ordinal aufwärts | Zeitliche Verläufe; verbundene Punkte |
| **Streudiagramm** | Intervall / Verhältnis | Zusammenhang zweier metrischer Merkmale |

---

### 7. Korrelation

| Begriff | Symbol | Formel | Bemerkung |
|---------|--------|--------|-----------|
| **Kovarianz** | $s_{xy}$ | $s_{xy} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$ | Richtung des Zusammenhangs; einheitenabhängig |
| **Verschiebungssatz** | $s_{xy}$ | $s_{xy} = \overline{xy} - \bar{x}\bar{y}$ | Rechnerisch einfacher |
| **Korrelationskoeffizient** (Pearson) | $r$ | $r = \frac{s_{xy}}{s_x \cdot s_y}$ | Einheitenfrei; $-1 \leq r \leq 1$ |

**Interpretation von $r$:**

| $\|r\|$ | Stärke |
|-------|--------|
| $0{,}0 - 0{,}3$ | Schwach |
| $0{,}3 - 0{,}7$ | Mittel |
| $0{,}7 - 1{,}0$ | Stark |

Vorzeichen: $r > 0$ = gleichsinnig, $r < 0$ = gegensinnig, $r = 0$ = kein linearer Zusammenhang.

**Eigenschaften:** symmetrisch ($r_{xy} = r_{yx}$), einheitenfrei, ausreißerempfindlich.

> **Korrelation $\neq$ Kausalität.** Mögliche Erklärungen: echte Kausalität, umgekehrte Kausalität, gemeinsame Ursache, Scheinkorrelation.

---

### 8. Lineare Regression

| Begriff | Symbol | Formel |
|---------|--------|--------|
| **Regressionsgerade** | $\hat{y}$ | $\hat{y} = mx + b$ |
| **Steigung** | $m$ | $m = \frac{s_{xy}}{s_x^2} = r \cdot \frac{s_y}{s_x}$ |
| **Achsenabschnitt** | $b$ | $b = \bar{y} - m\bar{x}$ |
| **Residuum** | $e_i$ | $e_i = y_i - \hat{y}_i$ |
| **Schwerpunkt** | $(\bar{x}, \bar{y})$ | Die Gerade geht immer durch diesen Punkt |

**Methode der kleinsten Quadrate (OLS):** Minimiere $\sum_{i=1}^{n} e_i^2$.

**Bestimmtheitsmaß:**

| Begriff | Symbol | Formel |
|---------|--------|--------|
| **Gesamtstreuung** | $SS_{\text{tot}}$ | $\sum(y_i - \bar{y})^2$ |
| **Erklärte Streuung** | $SS_{\text{reg}}$ | $\sum(\hat{y}_i - \bar{y})^2$ |
| **Residuelle Streuung** | $SS_{\text{res}}$ | $\sum(y_i - \hat{y}_i)^2$ |
| **Bestimmtheitsmaß** | $R^2$ | $R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = r^2$ |

Zerlegung: $SS_{\text{tot}} = SS_{\text{reg}} + SS_{\text{res}}$

$R^2 = 0{,}85$ bedeutet: 85% der Streuung werden durch den linearen Zusammenhang erklärt.

> **Interpolation** (innerhalb des Datenbereichs) ist zuverlässig; **Extrapolation** (außerhalb) ist mit Vorsicht zu genießen.

---

### 9. Grundbegriffe der Wahrscheinlichkeit

| Begriff | Symbol | Bedeutung |
|---------|--------|-----------|
| **Zufallsexperiment** | — | Vorgang mit mehreren möglichen, nicht vorhersagbaren Ausgängen; wiederholbar |
| **Ergebnis** | $\omega$ | Einzelner möglicher Ausgang |
| **Ergebnismenge / Grundraum** | $\Omega$ | Menge aller möglichen Ergebnisse |
| **Ereignis** | $A \subseteq \Omega$ | Teilmenge der Ergebnismenge; tritt ein, wenn $\omega \in A$ |
| **Elementarereignis** | $\{\omega\}$ | Ereignis mit genau einem Element |
| **Sicheres Ereignis** | $\Omega$ | Tritt immer ein |
| **Unmögliches Ereignis** | $\emptyset$ | Tritt nie ein |

---

### 10. Mengenoperationen auf Ereignissen

| Operation | Symbol | Sprachlich |
|-----------|--------|------------|
| **Vereinigung** | $A \cup B$ | „A oder B (oder beide)" |
| **Durchschnitt** | $A \cap B$ | „A und B" |
| **Komplement** | $\bar{A} = \Omega \setminus A$ | „nicht A" |
| **Differenz** | $A \setminus B$ | „A, aber nicht B" |
| **Disjunkt** | $A \cap B = \emptyset$ | „unvereinbar" |

**De-Morgansche Regeln:**

$$\overline{A \cup B} = \bar{A} \cap \bar{B} \qquad \overline{A \cap B} = \bar{A} \cup \bar{B}$$

---

### 11. Wahrscheinlichkeitsbegriffe

**Laplace (klassisch):** Alle Ergebnisse gleichwahrscheinlich.

$$P(A) = \frac{|A|}{|\Omega|}$$

**Statistische Definition (frequentistisch):** Relative Häufigkeit konvergiert.

$$P(A) = \lim_{n \to \infty} \frac{H_n(A)}{n}$$

**Axiome von Kolmogorow:**

| # | Axiom | Formel |
|---|-------|--------|
| 1 | Nichtnegativität | $P(A) \geq 0$ |
| 2 | Normierung | $P(\Omega) = 1$ |
| 3 | Additivität | $P(A_1 \cup A_2 \cup \cdots) = P(A_1) + P(A_2) + \cdots$ (für paarweise disjunkte $A_i$) |

Laplace und die frequentistische Definition sind Spezialfälle, die alle drei Axiome erfüllen.

---

### 12. Rechenregeln der Wahrscheinlichkeit

| Regel | Formel | Wann? |
|-------|--------|-------|
| **Komplementärregel** | $P(\bar{A}) = 1 - P(A)$ | Gegenereignis einfacher |
| **Additionssatz** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Immer |
| **Additionssatz (disjunkt)** | $P(A \cup B) = P(A) + P(B)$ | $A \cap B = \emptyset$ |
| **Siebformel** | $P(A \cup B \cup C) = \sum P - \sum P(\cap\text{Paare}) + P(A \cap B \cap C)$ | 3 Ereignisse |
| **Monotonie** | $A \subseteq B \Rightarrow P(A) \leq P(B)$ | Abschätzung |
| **Beschränktheit** | $0 \leq P(A) \leq 1$ | Immer |
| **Subadditivität** | $P(A \cup B) \leq P(A) + P(B)$ | Boole'sche Ungl. |
| $P(\emptyset) = 0$ | — | Unmögliches Ereignis |

---

### 13. Kombinatorik

| Konzept | Formel | Anwendung |
|---------|--------|-----------|
| **Produktregel** | $n_1 \cdot n_2 \cdots n_k$ | Mehrstufige Vorgänge |
| **Fakultät** | $n! = n \cdot (n-1) \cdots 1$, $\;0! = 1$ | Anordnung aller $n$ Elemente |
| **Permutation mit Wdh.** | $\frac{n!}{k_1! \cdots k_r!}$ | Identische Elemente vorhanden |
| **Variation** | $\frac{n!}{(n-k)!}$ | $k$ aus $n$, **mit** Reihenfolge, **ohne** Zurücklegen |
| **Kombination** | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | $k$ aus $n$, **ohne** Reihenfolge, **ohne** Zurücklegen |
| **Mit Zurücklegen + R.folge** | $n^k$ | z.B. PIN-Codes |
| **Mit Zurücklegen − R.folge** | $\binom{n+k-1}{k}$ | z.B. Kugeln in Urnen |

**Entscheidungshilfe:**

| | Ohne Zurücklegen | Mit Zurücklegen |
|---|---|---|
| **Mit Reihenfolge** | $\frac{n!}{(n-k)!}$ | $n^k$ |
| **Ohne Reihenfolge** | $\binom{n}{k}$ | $\binom{n+k-1}{k}$ |

**Eigenschaften von $\binom{n}{k}$:**
- Symmetrie: $\binom{n}{k} = \binom{n}{n-k}$
- Randfälle: $\binom{n}{0} = \binom{n}{n} = 1$
- Rekursion: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (Pascalsches Dreieck)

---

### 14. Bedingte Wahrscheinlichkeit und Unabhängigkeit

| Begriff | Formel | Bedeutung |
|---------|--------|-----------|
| **Bedingte W'keit** | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ | W'keit von $A$, wenn $B$ eingetreten ist |
| **Multiplikationssatz** | $P(A \cap B) = P(A \mid B) \cdot P(B)$ | Schnittmenge als Produkt |
| **Unabhängigkeit** | $P(A \cap B) = P(A) \cdot P(B)$ | $B$ ändert nichts an $P(A)$ |
| **Pfadmultiplikation** | $P(\text{Pfad}) = \prod P_i$ | Produkt entlang des Pfades |
| **Pfadaddition** | $P(\text{Ereignis}) = \sum P(\text{Pfade})$ | Summe aller Pfade zum Ereignis |

> **Unabhängig $\neq$ Disjunkt!** Disjunkte Ereignisse sind fast immer stark abhängig: $P(B \mid A) = 0$.

---

### 15. Totale Wahrscheinlichkeit und Satz von Bayes

**Zerlegung:** $B_1, \ldots, B_k$ zerlegen $\Omega$, wenn sie paarweise disjunkt sind und $\bigcup B_i = \Omega$.

**Satz der totalen Wahrscheinlichkeit:**

$$P(A) = \sum_{i=1}^{k} P(A \mid B_i) \cdot P(B_i)$$

**Satz von Bayes:**

$$P(B_j \mid A) = \frac{P(A \mid B_j) \cdot P(B_j)}{P(A)} = \frac{P(A \mid B_j) \cdot P(B_j)}{\sum_{i=1}^k P(A \mid B_i) \cdot P(B_i)}$$

| Bayes-Begriff | Symbol | Bedeutung |
|---------------|--------|-----------|
| **Apriori** (*prior*) | $P(B_j)$ | Vorwissen über $B_j$ |
| **Likelihood** | $P(A \mid B_j)$ | W'keit der Beobachtung, wenn $B_j$ wahr |
| **Aposteriori** (*posterior*) | $P(B_j \mid A)$ | Aktualisiertes Wissen nach Beobachtung $A$ |
| **Evidenz** | $P(A)$ | Normierungskonstante |

**Schlüsselbegriffe medizinischer Tests:**

| Begriff | Symbol | Bedeutung |
|---------|--------|-----------|
| **Prävalenz** | $P(\text{krank})$ | Anteil Erkrankter in der Population |
| **Sensitivität** | $P(\text{pos} \mid \text{krank})$ | Wie viele Kranke erkennt der Test? |
| **Spezifität** | $P(\text{neg} \mid \text{gesund})$ | Wie viele Gesunde erkennt der Test? |
| **Positiver Vorhersagewert** | $P(\text{krank} \mid \text{pos})$ | Wie wahrscheinlich krank bei positivem Test? |

---

### 16. Symbolverzeichnis

| Symbol | Deutsch | Kontext |
|--------|---------|---------|
| $N$ | Grundgesamtheitsumfang | Beschreibende Statistik |
| $n$ | Stichprobenumfang | Beschreibende Statistik |
| $\bar{x}$ | Arithmetisches Mittel | Lagemaß |
| $\tilde{x}$ | Median | Lagemaß |
| $x_{\text{mod}}$ | Modus | Lagemaß |
| $s^2$ | Varianz | Streuungsmaß |
| $s$ | Standardabweichung | Streuungsmaß |
| $s_x, s_y$ | Std.-Abw. von $x$ bzw. $y$ | Korrelation / Regression |
| $R$ | Spannweite | Streuungsmaß |
| $Q_1, Q_3$ | Unteres / oberes Quartil | Streuungsmaß |
| $H_i$ | Absolute Häufigkeit | Häufigkeitsverteilung |
| $h_i$ | Relative Häufigkeit | Häufigkeitsverteilung |
| $F_i$ | Kumulierte Häufigkeit | Häufigkeitsverteilung |
| $s_{xy}$ | Kovarianz | Korrelation |
| $r$ | Korrelationskoeffizient (Pearson) | Korrelation |
| $\hat{y}$ | Vorhersagewert | Regression |
| $m$ | Steigung der Regressionsgeraden | Regression |
| $b$ | $y$-Achsenabschnitt | Regression |
| $e_i$ | Residuum | Regression |
| $R^2$ | Bestimmtheitsmaß | Regression |
| $SS_{\text{tot}}, SS_{\text{reg}}, SS_{\text{res}}$ | Streuungszerlegung | Regression |
| $\Omega$ | Ergebnismenge / Grundraum | Wahrscheinlichkeit |
| $\omega$ | Ergebnis / Elementarereignis | Wahrscheinlichkeit |
| $A, B, C$ | Ereignisse | Wahrscheinlichkeit |
| $P(A)$ | Wahrscheinlichkeit von $A$ | Wahrscheinlichkeit |
| $P(A \mid B)$ | Bedingte Wahrscheinlichkeit | Wahrscheinlichkeit |
| $\bar{A}$ | Komplement von $A$ | Mengenoperationen |
| $\cup, \cap, \setminus$ | Vereinigung, Durchschnitt, Differenz | Mengenoperationen |
| $n!$ | Fakultät | Kombinatorik |
| $\binom{n}{k}$ | Binomialkoeffizient | Kombinatorik |
| $h_n(A)$ | Relative Häufigkeit bei $n$ Durchführungen | Statist. W'keitsdefinition |

---
