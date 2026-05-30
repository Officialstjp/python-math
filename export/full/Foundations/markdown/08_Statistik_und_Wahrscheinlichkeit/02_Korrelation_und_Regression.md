# Statistik
## 02 - Korrelation und Regression

Korrelation (Pearson's $r$, Kovarianz, Streudiagramme — Stärke und Richtung des linearen Zusammenhangs) und lineare Regression ($\hat{y} = a + bx$ nach der Methode der kleinsten Quadrate, Bestimmtheitsmaß $R^2$); Korrelation impliziert keine Kausalität.

> Vorausgesetzt: Beschreibende Statistik — Mittelwert, Varianz, Standardabweichung (08_Statistik/01).

### Lernziele

- Du kannst **Streudiagramme** lesen und interpretieren.
- Du verstehst die **Kovarianz** als Grundlage der Korrelation.
- Du kannst den **Korrelationskoeffizienten nach Pearson** berechnen und interpretieren.
- Du kennst den Unterschied zwischen **Korrelation und Kausalität**.
- Du kannst eine **lineare Regressionsgerade** nach der Methode der kleinsten Quadrate bestimmen.
- Du kannst das **Bestimmtheitsmaß** $R^2$ interpretieren.

---

### 1. Das Streudiagramm

Wenn wir den Zusammenhang zwischen zwei metrischen Merkmalen $x$ und $y$ untersuchen wollen, ist der erste Schritt immer eine **grafische Darstellung**: das **Streudiagramm** (auch: Scatterplot).

Jedes Objekt der Stichprobe liefert ein **Wertepaar** $(x_i, y_i)$, das als Punkt in einem Koordinatensystem eingetragen wird.

> **Beispiel:** Wir messen bei $n = 10$ Schülerinnen und Schülern die **Lernzeit** (Stunden pro Woche) und die **Prüfungsnote** (Punkte von 0-100). Jeder Punkt im Streudiagramm entspricht einer Person.

Aus dem Streudiagramm lässt sich bereits **visuell** ablesen:

| Muster | Interpretation |
|--------|----------------|
| Punkte steigen von links nach rechts | **Positiver** Zusammenhang - wenn $x$ wächst, wächst tendenziell auch $y$ |
| Punkte fallen von links nach rechts | **Negativer** Zusammenhang - wenn $x$ wächst, sinkt tendenziell $y$ |
| Punkte bilden eine **enge** Wolke | **Starker** Zusammenhang |
| Punkte bilden eine **breite** Wolke | **Schwacher** Zusammenhang |
| Kein erkennbares Muster | **Kein linearer** Zusammenhang |

> **Merke:** Das Streudiagramm zeigt nur **lineare** Zusammenhänge deutlich. Ein perfekter quadratischer Zusammenhang kann im Streudiagramm wie „kein Zusammenhang" aussehen - daher immer auch an **nichtlineare** Muster denken!

---


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_2_0.png)
    


### 2. Kovarianz

Um den Zusammenhang zweier Merkmale **numerisch** zu erfassen, brauchen wir ein Maß dafür, wie $x$ und $y$ **gemeinsam** vom Mittelwert abweichen.

#### Intuition

Betrachte einen einzelnen Datenpunkt $(x_i, y_i)$:
- Wenn $x_i > \bar{x}$ **und** $y_i > \bar{y}$ (beide überdurchschnittlich), dann ist das Produkt $(x_i - \bar{x})(y_i - \bar{y}) > 0$.
- Wenn $x_i > \bar{x}$ **aber** $y_i < \bar{y}$ (gegenläufig), dann ist das Produkt $(x_i - \bar{x})(y_i - \bar{y}) < 0$.

Mittelt man diese Produkte über alle Datenpunkte, erhält man ein Maß für die **Tendenz des gemeinsamen Schwankens**.

#### Definition

> Die **empirische Kovarianz** zweier Merkmale $x$ und $y$ ist:
>
> $$s_{xy} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

| Wert von $s_{xy}$ | Interpretation |
|--------------------|----------------|
| $s_{xy} > 0$ | Tendenz: wenn $x$ steigt, steigt auch $y$ → **gleichsinniger** Zusammenhang |
| $s_{xy} < 0$ | Tendenz: wenn $x$ steigt, sinkt $y$ → **gegensinniger** Zusammenhang |
| $s_{xy} \approx 0$ | Kein (linearer) Zusammenhang erkennbar |

#### Rechenregel (Verschiebungssatz)

Analog zur Varianz gibt es eine äquivalente Berechnungsformel, die manchmal bequemer ist:

$$s_{xy} = \frac{1}{n} \sum_{i=1}^{n} x_i y_i - \bar{x} \cdot \bar{y} = \overline{xy} - \bar{x} \cdot \bar{y}$$

> **Problem der Kovarianz:** Ihr Wert hängt von den **Einheiten** der Merkmale ab. Messen wir Einkommen in Euro, erhalten wir einen anderen Wert als in Cent - obwohl der Zusammenhang derselbe ist. Wir brauchen ein **einheitenfreies** Maß.

---

    Mittelwerte:  x̄ = 5.9 h   |   ȳ = 61.0 Punkte
    Kovarianz:    s_xy = 39.70
    
    


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_4_1.png)
    


### 3. Der Korrelationskoeffizient nach Pearson

Um das Einheitenproblem der Kovarianz zu lösen, **normieren** wir: Wir teilen die Kovarianz durch das Produkt der Standardabweichungen beider Merkmale.

#### Definition

> Der **empirische Korrelationskoeffizient nach Pearson** ist:
>
> $$r = r_{xy} = \frac{s_{xy}}{s_x \cdot s_y} = \frac{\displaystyle\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\displaystyle\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2} \cdot \sqrt{\displaystyle\frac{1}{n}\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

#### Eigenschaften

| Eigenschaft | Erklärung |
|-------------|----------|
| $-1 \leq r \leq 1$ | Der Wert ist immer zwischen $-1$ und $1$ |
| $r = 1$ | **Perfekter positiver** linearer Zusammenhang - alle Punkte liegen exakt auf einer steigenden Geraden |
| $r = -1$ | **Perfekter negativer** linearer Zusammenhang - alle Punkte liegen exakt auf einer fallenden Geraden |
| $r = 0$ | **Kein linearer** Zusammenhang (aber möglicherweise ein nichtlinearer!) |
| **Einheitenfrei** | Egal in welcher Einheit gemessen wird - $r$ bleibt gleich |
| **Symmetrisch** | $r_{xy} = r_{yx}$ - es ist egal, welches Merkmal $x$ und welches $y$ ist |
| **Ausreißerempfindlich** | Ein einzelner extremer Punkt kann $r$ stark verändern |

#### Interpretation - Daumenregel

| Betrag von $r$ | Stärke des linearen Zusammenhangs |
|----------------|-----------------------------------|
| $0{,}0$ bis $0{,}3$ | schwach |
| $0{,}3$ bis $0{,}7$ | mittel |
| $0{,}7$ bis $1{,}0$ | stark |

> **Achtung:** Diese Einteilung ist eine grobe Orientierung. In der Physik erwartet man oft große Werte von $|r|$, in den Sozialwissenschaften kann bereits ein deutlich kleinerer Wert relevant sein. Der Kontext entscheidet.

---

    === Berechnung des Korrelationskoeffizienten ===
      n           = 10
      x̄           = 5.90
      ȳ           = 61.00
      s_xy (Kov.) = 39.70
      s_x         = 2.47
      s_y         = 16.36
      r           = 39.70 / (2.47 · 16.36) = 0.9831
    
      Kontrolle (np.corrcoef): r = 0.9831
    
    


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_6_1.png)
    


### 4. Korrelation ≠ Kausalität

Dies ist vielleicht die **wichtigste Erkenntnis** der gesamten Statistik:

> **Aus einer Korrelation zweier Merkmale darf man nicht schließen, dass eines das andere *verursacht*.**

Ein hoher Korrelationskoeffizient sagt lediglich: *Die beiden Größen verändern sich tendenziell gemeinsam.* Warum sie das tun, bleibt offen. Es gibt mehrere Möglichkeiten:

| Szenario | Beispiel |
|----------|----------|
| **Echte Kausalität** (x → y) | Mehr Lernen → bessere Note |
| **Umgekehrte Kausalität** (y → x) | Vielleicht lernen motivierte Schüler mehr, *weil* sie gute Noten erwarten |
| **Gemeinsame Ursache** (z → x und z → y) | Bildungsnähe des Elternhauses beeinflusst sowohl Lernverhalten als auch Noten |
| **Scheinkorrelation** (Zufall / Drittvariable) | Eisverkauf korreliert mit Badetoten - die gemeinsame Ursache ist das *Wetter* |

#### Klassische Scheinkorrelationen

- **Storchenpopulation** und **Geburtenrate** korrelieren in europäischen Ländern ($r \approx 0{,}6$). Gemeinsame Ursache: ländliche vs. städtische Regionen.
- **Schokoladenkonsum pro Kopf** und **Anzahl Nobelpreisträger** eines Landes. Gemeinsame Ursache: Wohlstand.
- **Schuhgröße** und **Lesefähigkeit** bei Kindern - beide wachsen mit dem Alter.

> **Merke:** *Correlation does not imply causation* - Korrelation impliziert keine Kausalität. Um Kausalität nachzuweisen, braucht man **kontrollierte Experimente** oder spezielle statistische Verfahren.

---

### 5. Lineare Regression - Gerade der besten Anpassung

Nachdem wir **erkannt** haben, dass ein linearer Zusammenhang besteht (Streudiagramm, $r$-Wert), wollen wir diesen Zusammenhang durch eine Gerade **modellieren**:

$$\hat{y} = mx + b$$

Dabei ist:
- $m$ die **Steigung** (um wie viel ändert sich $\hat{y}$, wenn $x$ um 1 steigt?)
- $b$ der **$y$-Achsenabschnitt** ($\hat{y}$-Wert bei $x = 0$)
- $\hat{y}$ der **geschätzte** Wert (im Unterschied zum tatsächlichen $y_i$)

> **Hinweis zur Notation:** In vielen Schulbüchern und Vorlesungen wird die lineare Funktion als $y = mx + b$ geschrieben. In anderen Statistikbüchern findet man oft auch $\hat{y} = a + bx$. Beide Schreibweisen meinen dasselbe - nur die Buchstaben für **Steigung** und **Achsenabschnitt** sind vertauscht.

Die zentrale Frage: **Welche** Gerade passt am besten?

---

#### 5.1 Methode der kleinsten Quadrate (OLS)

Für jeden Datenpunkt gibt es einen **Fehler** (Residuum) zwischen dem tatsächlichen Wert $y_i$ und dem von der Gerade geschätzten Wert $\hat{y}_i$:

$$e_i = y_i - \hat{y}_i = y_i - (mx_i + b)$$

Die **Methode der kleinsten Quadrate** (*Ordinary Least Squares*, OLS) findet die Gerade, die die **Summe der quadrierten Fehler** minimiert:

$$S(m, b) = \sum_{i=1}^{n} e_i^2 = \sum_{i=1}^{n} (y_i - b - mx_i)^2 \xrightarrow{\text{min!}}$$

> **Warum quadrieren?** Positive und negative Fehler sollen sich nicht aufheben (genau wie bei der Varianz). Außerdem werden große Fehler stärker bestraft.

#### 5.2 Formeln für $m$ und $b$

Durch Ableiten und Nullsetzen (Analysis!) erhält man:

> $$m = \frac{s_{xy}}{s_x^2} = \frac{\displaystyle\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\displaystyle\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$
>
> $$b = \bar{y} - m\bar{x}$$

Die Regressionsgerade geht **immer** durch den Schwerpunkt $(\bar{x}, \bar{y})$ der Daten.

#### Zusammenhang mit der Korrelation

Die Steigung $m$ lässt sich auch über den Korrelationskoeffizienten ausdrücken:

$$m = r \cdot \frac{s_y}{s_x}$$

Das zeigt: Die **Richtung** von $m$ (positiv/negativ) stimmt immer mit dem **Vorzeichen** von $r$ überein.

> **Wichtig:** Sowohl Korrelation als auch lineare Regression sind **empfindlich gegenüber Ausreißern**. Schon ein einzelner extremer Punkt kann $r$, $m$ und $b$ deutlich verändern.

---

    === Lineare Regression: ŷ = mx + b ===
      x̄     = 5.90
      ȳ     = 61.00
      s_xy  = 39.70
      s_x²  = 6.09
      m     = 39.70 / 6.09 = 6.5189
      b     = 61.00 − 6.5189 · 5.90 = 22.5386
    
      ➜ Regressionsgerade:  ŷ = 6.52x + 22.54
      ➜ Interpretation:     Pro Stunde mehr Lernen steigt die Punktzahl um ca. 6.5 Punkte.
    
      Hinweis: Manche Bücher schreiben äquivalent ŷ = a + bx.
    
      Kontrolle (np.polyfit): m = 6.5189, b = 22.5386
    


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_9_1.png)
    


### 6. Das Bestimmtheitsmaß $R^2$

Wir haben nun eine Regressionsgerade - aber **wie gut** beschreibt sie die Daten? Dafür brauchen wir ein Gütemaß.

#### Idee: Zerlegung der Gesamtstreuung

Die Abweichung jedes Datenpunkts $y_i$ vom Gesamtmittelwert $\bar{y}$ lässt sich in zwei Teile zerlegen:

$$\underbrace{y_i - \bar{y}}_{\text{Gesamtabweichung}} = \underbrace{(\hat{y}_i - \bar{y})}_{\text{durch Regression erklärt}} + \underbrace{(y_i - \hat{y}_i)}_{\text{Residuum (nicht erklärt)}}$$

Quadriert und summiert ergibt sich:

$$\underbrace{\sum(y_i - \bar{y})^2}_{SS_{\text{tot}}} = \underbrace{\sum(\hat{y}_i - \bar{y})^2}_{SS_{\text{reg}}} + \underbrace{\sum(y_i - \hat{y}_i)^2}_{SS_{\text{res}}}$$

#### Definition

> Das **Bestimmtheitsmaß** ist der Anteil der Gesamtstreuung, der durch die Regression **erklärt** wird:
>
> $$R^2 = \frac{SS_{\text{reg}}}{SS_{\text{tot}}} = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$$

| Wert | Bedeutung |
|------|----------|
| $R^2 = 1$ | Alle Punkte liegen **exakt** auf der Geraden - perfekte Anpassung |
| $R^2 = 0$ | Die Gerade erklärt **nichts** - der Mittelwert $\bar{y}$ wäre genauso gut |
| $R^2 = 0{,}85$ | 85 % der Streuung von $y$ werden durch den linearen Zusammenhang mit $x$ erklärt |

#### Zusammenhang mit $r$

Bei der **einfachen linearen Regression** (ein $x$-Merkmal) gilt ein eleganter Zusammenhang:

$$R^2 = r^2$$

Das Bestimmtheitsmaß ist das **Quadrat** des Korrelationskoeffizienten. Daher der Name $R^2$.

> **Beispiel:** Bei $r = 0{,}96$ ist $R^2 = 0{,}92$ - die Regressionsgerade erklärt 92 % der Streuung.

---

    === Streuungszerlegung ===
      SS_tot (Gesamt)   = 2678.00
      SS_reg (Erklärt)  = 2588.00
      SS_res (Rest)     = 90.00
      Kontrolle:  SS_reg + SS_res = 2678.00  (≈ SS_tot)
    
      R²  = 1 − 90.00/2678.00 = 0.9664
      r²  = 0.9831² = 0.9664
    
      ➜ 96.6 % der Streuung werden durch die Regression erklärt.
    


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_11_1.png)
    


### 7. Praxisbeispiel - Vollständige Analyse

Zum Abschluss führen wir eine **vollständige Korrelations- und Regressionsanalyse** an einem realistischeren Datensatz durch.

> **Aufgabe:** Ein Unternehmen möchte den Zusammenhang zwischen **Werbeausgaben** (in Tausend €) und **Umsatz** (in Tausend €) untersuchen. Es liegen Daten aus 15 Monaten vor.

Wir folgen dem systematischen Vorgehen:

1. **Streudiagramm** zeichnen
2. **Korrelationskoeffizient** berechnen und interpretieren
3. **Regressionsgerade** bestimmen
4. **$R^2$** berechnen und die Güte beurteilen
5. **Prognose** für einen neuen $x$-Wert erstellen

---

#### 7.1 Lösungsschema „von Hand"

Das folgende Schema kann fast immer direkt verwendet werden:

| Schritt | Was wird berechnet? | Formel |
|--------|----------------------|--------|
| 1 | Mittelwerte | $\bar{x} = \frac{1}{n}\sum x_i$, $\bar{y} = \frac{1}{n}\sum y_i$ |
| 2 | Kovarianz | $s_{xy} = \frac{1}{n}\sum (x_i-\bar{x})(y_i-\bar{y})$ |
| 3 | Varianz von $x$ | $s_x^2 = \frac{1}{n}\sum (x_i-\bar{x})^2$ |
| 4 | Korrelation | $r = \frac{s_{xy}}{s_x s_y}$ |
| 5 | Regression | $m = \frac{s_{xy}}{s_x^2}$, $b = \bar{y} - m\bar{x}$ |
| 6 | Gerade angeben | $\hat{y} = mx + b$ |
| 7 | Güte beurteilen | $R^2 = r^2$ (bei einfacher linearer Regression) |
| 8 | Prognose | gewünschten $x$-Wert in $\hat{y} = mx + b$ einsetzen |

#### Typische Tabelle für das Rechnen

Bei einer schriftlichen Lösung ist oft eine Tabelle mit folgenden Spalten hilfreich:

| $x_i$ | $y_i$ | $x_i-\bar{x}$ | $y_i-\bar{y}$ | $(x_i-\bar{x})(y_i-\bar{y})$ | $(x_i-\bar{x})^2$ |
|------|------|----------------|----------------|---------------------------------|-------------------|

Am Ende summiert man die letzten beiden bzw. drei Spalten und setzt die Werte in die Formeln ein.

> **Prüfungstipp:** In vielen Aufgaben genügt es nicht, nur die Gerade anzugeben. Man sollte auch kurz **interpretieren**, was die Steigung $m$, der Achsenabschnitt $b$, der Korrelationswert $r$ und das Bestimmtheitsmaß $R^2$ inhaltlich bedeuten.

> **Achtung vor Extrapolation:** Vorhersagen sind innerhalb des beobachteten Bereichs der $x$-Werte meist sinnvoller (**Interpolation**) als weit außerhalb (**Extrapolation**). Außerhalb des Datenbereichs kann die Gerade leicht in die Irre führen.

---

#### 7.2 Dasselbe Vorgehen mit Python

Die folgende Code-Zelle setzt genau dieses Schema rechnerisch um und visualisiert das Ergebnis.

---

    === Datensatz ===
     Werbeausgaben (T€)  Umsatz (T€)
                      5         57.3
                      8         83.6
                     10         84.3
                     12         76.3
                     14         90.2
                     15        111.2
                     18         88.2
                     20        110.6
                     22        130.5
                     24        119.9
                     25        124.6
                     28        138.8
                     30        157.9
                     32        147.3
                     35        158.4
    
    === Ergebnisse ===
      Korrelation:        r  = 0.9555  → starker positiver Zusammenhang
      Regressionsgerade:  ŷ = 3.26x + 47.21
      Bestimmtheitsmaß:   R² = 0.9129  → 91.3 % erklärt
    
      Prognose für Werbeausgaben = 25 T€:  Umsatz ≈ 128.7 T€
      Hinweis: Prognosen außerhalb des beobachteten Bereichs sind Extrapolationen und unsicherer.
    


    
![png](02_Korrelation_und_Regression_files/02_Korrelation_und_Regression_13_1.png)
    


#### 7.3 Taschenrechner: TI-Nspire CX II

Alle Berechnungen dieses Notebooks lassen sich direkt am **TI-Nspire CX II-T** durchführen. Hier das Vorgehen, das für Korrelation und Regression relevant ist.

##### Dateneingabe

1. Neues Dokument → **Lists & Spreadsheets** einfügen
2. Spalte **A**: $x$-Werte eingeben, Spalte **B**: $y$-Werte
3. Spaltenüberschriften vergeben (z.B. `werb`, `ums`) - diese Namen kann man danach in Formeln verwenden

##### Statistik-Befehle

Über **Menü → Statistik → Stat-Berechnungen**:

| Menüpunkt | Eingabe | Liefert |
|-----------|---------|---------|
| **Einvariable Statistik** | Liste wählen | $\bar{x}$, $\sum x$, $\sum x^2$, $\sigma_x$, $s_x$, $n$, Min, $Q_1$, Med, $Q_3$, Max |
| **Zweivariable Statistik** | Beide Listen wählen | Wie oben für $x$ und $y$, zusätzlich $\sum xy$ |
| **Lin. Regression (mx+b)** | $x$-Liste, $y$-Liste | $m$, $b$, $r$, $r^2$ |

> **Tipp:** Es gibt auch **Lin. Regression (a+bx)** - die Werte sind identisch, nur die Buchstaben vertauscht. Bei **(mx+b)** stehen $m$ = Steigung und $b$ = Achsenabschnitt direkt so, wie in diesem Notebook.

##### Streudiagramm am TR

1. Neue Seite → **Data & Statistics** hinzufügen
2. Unten auf *„Klicke, um Variable hinzuzufügen"* → $x$-Liste wählen
3. Links dasselbe → $y$-Liste wählen
4. **Menü → Analyse → Regression → Linear anzeigen** → Gerade wird eingeblendet

##### Notation am TR vs. Formelsammlung

| TR-Ausgabe | Divisor | Notebook / Formelsammlung |
|------------|---------|---------------------------|
| $\sigma_x$ | $\frac{1}{n}$ | $s_x$ - **diese verwenden wir** (deskriptive Statistik) |
| $s_x$ | $\frac{1}{n-1}$ | Stichproben-Std.abw. (schließende Statistik, hier nicht benötigt) |
| $r$ | - | Korrelationskoeffizient $r$ |
| $r^2$ | - | Bestimmtheitsmaß $R^2$ |
| $\Sigma xy$ | - | $\sum x_i y_i$ (nützlich für Verschiebungssatz) |

> **Achtung bei der Matura:** Der TR gibt **beide** Standardabweichungen aus ($\sigma_x$ und $s_x$). In der deskriptiven Statistik (und in diesem Notebook) verwenden wir immer **Divisor $n$** → das ist $\sigma_x$ am TR. Diesen Wert ablesen, nicht $s_x$!

---

---

## Verständnis-Check

*Löse die folgenden Aufgaben auf Papier.*

**Aufgabe 1:** Für 5 Datenpunkte gilt: $\bar x = 4$, $\bar y = 6$, $s_x = 2$, $s_y = 3$, $s_{xy} = 4{,}8$.

a) Berechne den Korrelationskoeffizienten $r$.

b) Bestimme die Regressionsgleichung $\hat y = mx + b$.

c) Sage $\hat y$ für $x = 7$ vorher.

**Aufgabe 2:** Ein Modell hat $SS_{\text{tot}} = 200$ und $SS_{\text{res}} = 50$.

a) Berechne $R^2$.

b) Interpretiere das Ergebnis.

**Aufgabe 3:** Erkläre anhand eines konkreten Beispiels, warum Korrelation nicht Kausalität bedeutet.

**Aufgabe 4:** Die Residuen einer Regression zeigen ein deutliches U-Muster. Was bedeutet das und was sollte man tun?

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $r = \dfrac{s_{xy}}{s_x \cdot s_y} = \dfrac{4{,}8}{2 \cdot 3} = 0{,}8$ → starker positiver linearer Zusammenhang

b) $m = \dfrac{s_{xy}}{s_x^2} = \dfrac{4{,}8}{4} = 1{,}2$

$b = \bar y - m \bar x = 6 - 1{,}2 \cdot 4 = 1{,}2$

$\hat y = 1{,}2x + 1{,}2$

c) $\hat y = 1{,}2 \cdot 7 + 1{,}2 = 9{,}6$

(Achtung: $x=7$ liegt außerhalb von $\bar x \pm 2s_x = [0, 8]$, also gerade noch im Bereich - trotzdem Vorsicht bei Extrapolation.)
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

a) $R^2 = 1 - \dfrac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \dfrac{50}{200} = 0{,}75$

b) 75 % der Streuung in $y$ werden durch das Modell (die Regressionsgerade) erklärt. Die restlichen 25 % sind unerklärte Reststreuung.
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

Beispiel: Je mehr Speiseeis verkauft wird, desto mehr Badeunfälle gibt es ($r > 0$). Eis *verursacht* aber keine Badeunfälle - beides hat eine gemeinsame Ursache: **Sommerhitze** (Drittvariable / Confounder). Korrelation zeigt statistischen Zusammenhang, nicht kausale Wirkung.
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

Ein U-Muster (oder umgekehrtes U) in den Residuen zeigt, dass der wahre Zusammenhang **nichtlinear** ist und die lineare Regression das Muster nicht korrekt erfasst.

Man sollte: ein nichtlineares Modell wählen (z. B. quadratische Regression) oder die Daten transformieren (z. B. logarithmisch), und erneut die Residuen prüfen.
</details>

## Zusammenfassung

Dieser Abschnitt untersucht den Zusammenhang zwischen zwei Merkmalen: Wie stark hängen sie zusammen, und lässt er sich modellieren?

Das **Streudiagramm** ist der Ausgangspunkt. Es zeigt, ob ein linearer Zusammenhang plausibel ist, ob Ausreißer vorhanden sind, und ob die Daten eher einer Kurve folgen. Jede Analyse sollte damit beginnen.

Die **Kovarianz** $s_{xy}$ zeigt die Richtung des Zusammenhangs. Sie ist einheitenabhängig und deshalb schwer zu interpretieren. Der **Korrelationskoeffizient** $r$ normiert die Kovarianz auf $[-1, 1]$. Er ist einheitenfrei und damit zwischen verschiedenen Datensätzen vergleichbar.

Die **Regressionsgerade** $\hat y = mx + b$ minimiert die Summe der quadrierten Abstände zu allen Punkten. Das **Bestimmtheitsmaß** $R^2$ gibt den Anteil der erklärten Streuung in $y$ an. $R^2 = 0{,}75$ bedeutet: 75 % der Streuung folgt dem Modell, 25 % ist unerklärte Reststreuung.

Korrelation bedeutet nicht Kausalität. Ein statistischer Zusammenhang kann auf eine gemeinsame Ursache (Drittvariable) zurückgehen oder zufällig sein. Die inhaltliche Interpretation ist nicht durch die Statistik allein möglich.

#### Systematisches Vorgehen bei der Analyse

1. **Streudiagramm** zeichnen — gibt es überhaupt einen (linearen) Zusammenhang?
2. **Ausreißer** und auffällige Muster prüfen — sie können $r$ und die Regression stark beeinflussen.
3. **Korrelationskoeffizient** $r$ berechnen — wie stark und in welche Richtung?
4. Prüfen: **Korrelation ≠ Kausalität** — gibt es eine plausible Erklärung?
5. **Regressionsgerade** bestimmen — Zusammenhang modellieren
6. **$R^2$** berechnen — wie gut passt das Modell?
7. **Residuen** prüfen — sind die Fehler zufällig verteilt? (Muster → Modell ungeeignet)
8. **Prognosen** nur mit Vorsicht verwenden — besonders außerhalb des beobachteten Bereichs.


---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Streudiagramm | Scatter plot |
| Kovarianz | Covariance |
| Korrelationskoeffizient | Correlation coefficient |
| Regressionsgerade | Regression line |
| Steigung | Slope |
| Achsenabschnitt | Intercept |
| Bestimmtheitsmaß | Coefficient of determination |
| Residuum (Pl. Residuen) | Residual |
| Quadratsumme | Sum of squares |
| Kausalität | Causality |
| Drittvariable | Confounding variable |
| Vorhersage / Prognose | Prediction |
| Extrapolation | Extrapolation |
