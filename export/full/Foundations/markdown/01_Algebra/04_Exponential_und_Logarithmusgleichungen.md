# Algebra

## 04 - Exponential- & Logarithmusgleichungen

Exponentialgleichungen durch Logarithmieren ($a^x = b \implies x = \log_a b$) oder Basenangleichung lösen, logarithmische Gleichungen mit $\ln$ und $\log$, Substitution $u = a^x$ zur Reduktion auf quadratische Form, Halbwerts- und Verdopplungszeit.

> Vorausgesetzt: Potenz- und Logarithmengesetze, quadratische Gleichungen.

### Lernziele

- Du kannst **einfache Exponentialgleichungen** durch Logarithmieren lösen.
- Du löst Gleichungen mit **$e^x$ und $\ln$** sicher.
- Du erkennst, wann eine **Substitution** eine Exponentialgleichung auf eine quadratische reduziert.
- Du löst **logarithmische Gleichungen** und prüfst die Definitionsmenge.
- Du kannst **Halbwertszeit** und **Verdopplungszeit** berechnen.

---

## 1. Einfache Exponentialgleichungen

Steht die Unbekannte im Exponenten, hilft keine algebraische Umformung - man muss den Exponenten "herunterholen". Das gelingt durch Logarithmieren beider Seiten, denn $\log_a(a^x) = x$ macht aus einem Exponenten einen einfachen Faktor.

$$
a^x = b \implies x = \log_a(b) = \frac{\ln b}{\ln a}
$$

Lässt sich die Basis beider Seiten **angleichen** (beide als Potenz derselben Zahl schreiben), spart man den Logarithmus ganz:

**Beispiel 1:** $\quad 2^x = 5$ - Basen lassen sich nicht angleichen, also logarithmieren:

$$
x = \log_2(5) = \frac{\ln 5}{\ln 2} \approx \frac{1{,}609}{0{,}693} \approx 2{,}322
$$

**Probe:** $2^{2{,}322} \approx 5$ ✓

**Beispiel 2:** $\quad 3^{2x-1} = 27$ - da $27 = 3^3$, können wir direkt die **Basis angleichen**:

$$
3^{2x-1} = 3^3 \implies 2x - 1 = 3 \implies x = 2
$$

**Beispiel 3:** $\quad 5^{x+1} = 8^x$ - zwei verschiedene Basen, also logarithmieren:

$$
(x+1) \ln 5 = x \ln 8 \implies x \ln 5 + \ln 5 = x \ln 8 \implies x(\ln 8 - \ln 5) = \ln 5
$$
$$
x = \frac{\ln 5}{\ln 8 - \ln 5} = \frac{\ln 5}{\ln(8/5)} \approx \frac{1{,}609}{0{,}470} \approx 3{,}424
$$

> **Merke:** Wenn keine Basis angeglichen werden kann, logarithmiere beide Seiten. Nutze bevorzugt $\ln$ (natürlicher Logarithmus).

## 2. Gleichungen mit $e^x$ und $\ln$

$e^x$ und $\ln$ sind Umkehrfunktionen voneinander:

$$
e^{\ln x} = x \qquad \ln(e^x) = x
$$

**Beispiel 1:** $\quad e^{2x - 3} = 7$

$$
\ln(e^{2x-3}) = \ln 7 \implies 2x - 3 = \ln 7 \implies x = \frac{3 + \ln 7}{2} \approx \frac{3 + 1{,}946}{2} \approx 2{,}473
$$

**Beispiel 2:** $\quad e^x = e^{3-x}$

Gleiche Basis:

$$
x = 3 - x \implies 2x = 3 \implies x = \frac{3}{2}
$$

**Beispiel 3:** $\quad 3e^{x} - 2 = 10$

$$
e^x = 4 \implies x = \ln 4 \approx 1{,}386
$$

**Definitionsmenge bei $\ln$:** Der Ausdruck $\ln(A)$ ist nur für $A > 0$ definiert. Bei logarithmischen Gleichungen immer DM prüfen!

## 3. Substitution bei Exponentialgleichungen

Manche Exponentialgleichungen lassen sich durch **Substitution** auf eine quadratische zurückführen.

**Erkennungsmuster:** Gleichung der Form $A \cdot e^{2x} + B \cdot e^x + C = 0$.

**Substitution:** $u = e^x$ (beachte: $e^{2x} = (e^x)^2 = u^2$ und immer $u > 0$!)

**Beispiel:** $\quad e^{2x} - 3e^x + 2 = 0$

**Schritt 1:** Substitution $u = e^x$:

$$
u^2 - 3u + 2 = 0 \implies (u - 1)(u - 2) = 0 \implies u_1 = 1, \quad u_2 = 2
$$

**Schritt 2:** Rücksubstitution:

$$
e^x = 1 \implies x = \ln 1 = 0
$$
$$
e^x = 2 \implies x = \ln 2 \approx 0{,}693
$$

**Weitere Beispiele mit $u$-Substitution:**

$$
4^x - 5 \cdot 2^x + 4 = 0 \quad \xrightarrow{u = 2^x} \quad u^2 - 5u + 4 = 0 \implies u = 1\ \text{oder}\ u = 4
$$
$$
2^x = 1 \implies x = 0 \qquad 2^x = 4 \implies x = 2
$$

> **Merke:** Nach der Rücksubstitution prüfen: $u = e^x > 0$ und $u = a^x > 0$ immer. Negative $u$-Werte liefern **keine** reellen Lösungen.

## 4. Logarithmische Gleichungen

**Grundprinzip:** Gleichung so umformen, dass ein einzelner Logarithmus entsteht, dann exponenzieren.

**Wichtig:** Definitionsmenge zuerst! Bei $\log(A)$ muss $A > 0$ gelten.

**Beispiel 1:** $\quad \log(x) + \log(x - 1) = \log(6)$

**DM:** $x > 0$ und $x - 1 > 0 \implies x > 1$

Produktregel:

$$
\log(x(x-1)) = \log(6) \implies x(x-1) = 6 \implies x^2 - x - 6 = 0
$$
$$
x = \frac{1 \pm 5}{2} \implies x_1 = 3, \quad x_2 = -2
$$

$x_2 = -2$ verletzt DM ($x > 1$) → **Scheinlösung!** Lösung: $x = 3$.

**Probe:** $\log(3) + \log(2) = \log(6)$ ✓

**Beispiel 2:** $\quad \ln(x + 3) - \ln(x - 1) = 2$

**DM:** $x > 1$

Quotientenregel:

$$
\ln\!\left(\frac{x+3}{x-1}\right) = 2 \implies \frac{x+3}{x-1} = e^2
$$
$$
x + 3 = e^2(x - 1) \implies x(1 - e^2) = -3 - e^2 \implies x = \frac{e^2 + 3}{e^2 - 1} \approx 1{,}575
$$

$x \approx 1{,}575 > 1$ ✓

**Beispiel 3:** $\quad \log_2(x^2 - 4x + 5) = 1$

$$
x^2 - 4x + 5 = 2^1 = 2 \implies x^2 - 4x + 3 = 0 \implies x_1 = 3, \quad x_2 = 1
$$

Probe: Argument bei $x=3$: $9-12+5=2>0$ ✓; bei $x=1$: $1-4+5=2>0$ ✓ → beide Lösungen gültig.

## 5. Anwendungen: Halbwertszeit & Verdopplungszeit

Exponentialgleichungen beschreiben überall dort natürliche Prozesse, wo eine Größe proportional zu ihrer eigenen Menge wächst oder zerfällt - Bevölkerungswachstum, radioaktiver Zerfall, Zinseszins, Bakterienkulturen. Die zwei wichtigsten abgeleiteten Größen sind die **Halbwertszeit** und die **Verdopplungszeit**.

### Wachstum / Zerfall - allgemeines Modell

$$
N(t) = N_0 \cdot a^t \qquad\text{oder}\qquad N(t) = N_0 \cdot e^{kt}
$$

| Parameter | Bedeutung |
|---|---|
| $N_0$ | Anfangsmenge (bei $t = 0$) |
| $a > 1$ / $k > 0$ | Wachstum |
| $0 < a < 1$ / $k < 0$ | Zerfall |
| $t$ | Zeit |

### Halbwertszeit $T_{1/2}$

Die **Halbwertszeit** ist die Zeit, nach der die Hälfte der Ausgangsmenge übrig bleibt:

$$
N(T_{1/2}) = \frac{N_0}{2} \implies N_0 \cdot e^{k \cdot T_{1/2}} = \frac{N_0}{2} \implies e^{k T_{1/2}} = \frac{1}{2} \implies T_{1/2} = \frac{\ln 2}{|k|}
$$

**Beispiel:** Kohlenstoff-14 hat $k = -0{,}000121\ \text{yr}^{-1}$. Halbwertszeit:

$$
T_{1/2} = \frac{\ln 2}{0{,}000121} \approx 5730\ \text{Jahre}
$$

**Wann ist noch 10 % übrig?**

$$
e^{-0{,}000121 \cdot t} = 0{,}1 \implies t = \frac{\ln 0{,}1}{-0{,}000121} = \frac{-\ln 10}{-0{,}000121} \approx 19\,035\ \text{Jahre}
$$

### Verdopplungszeit $T_2$

Die **Verdopplungszeit** ist die Zeit, nach der sich die Menge verdoppelt hat:

$$
N(T_2) = 2 N_0 \implies e^{k T_2} = 2 \implies T_2 = \frac{\ln 2}{k}
$$

**Beispiel:** Bakterien wachsen mit Rate $k = 0{,}35\ \text{h}^{-1}$. Verdopplungszeit:

$$
T_2 = \frac{\ln 2}{0{,}35} \approx \frac{0{,}693}{0{,}35} \approx 1{,}98\ \text{Stunden}
$$

**Wann ist die 10-fache Menge erreicht?**

$$
e^{0{,}35 t} = 10 \implies t = \frac{\ln 10}{0{,}35} \approx \frac{2{,}303}{0{,}35} \approx 6{,}58\ \text{Stunden}
$$

    =======================================================
    Verifikation: Exponential- & Logarithmusgleichungen
    =======================================================
    
      2^x = 5:  x = ln(5)/ln(2) = 2.3219
      Probe: 2^2.3219 = 5.0000  ✓
    
      e^(2x-3) = 7:  x = (3 + ln7)/2 = 2.4730
      Probe: e^(1.9459) = 7.0000  ✓
    
      e^(2x) - 3e^x + 2 = 0  (Substitution u = e^x):
      u = 1 → x = ln(1) = 0.0000,  Probe: 0.000000  ✓
      u = 2 → x = ln(2) = 0.6931,  Probe: 0.000000  ✓
    
      log(x) + log(x-1) = log(6):
      x = 3: log(3) + log(2) = 0.7782, log(6) = 0.7782  ✓
      x = -2: außerhalb DM (x ≤ 1) → Scheinlösung ✗
    
    =======================================================
    Anwendungen: Halbwertszeit & Verdopplungszeit
    =======================================================
    
      C-14 Halbwertszeit: T_½ = ln(2)/|k| = 5728 Jahre
      Bakterien Verdopplungszeit: T₂ = ln(2)/k = 1.98 Stunden
      10-fache Menge nach: t = ln(10)/k = 6.58 Stunden


---

## Verständnis-Check

#### Aufgabe 1: Exponentialgleichungen

a) $3^x = 81$

b) $2^{x-1} = 0{,}5$

c) $5^x = 12$ (Ergebnis mit $\ln$ und als Dezimalzahl)

d) $2^{x+1} = 3^x$ (Logarithmieren, nach $x$ auflösen)

#### Aufgabe 2: Gleichungen mit $e^x$ und $\ln$

a) $e^{3x} = 20$

b) $2e^x - 7 = 0$

c) $\ln(2x - 1) = 3$

d) $e^{2x} - 4 = 0$

#### Aufgabe 3: Substitution

a) $e^{2x} - 5e^x + 6 = 0$

b) $4^x - 3 \cdot 2^x - 4 = 0$

c) $9^x - 4 \cdot 3^x + 3 = 0$

#### Aufgabe 4: Logarithmische Gleichungen

a) $\log_2(x) + \log_2(x - 2) = 3$ (Probe nicht vergessen!)

b) $\ln(x+1) - \ln(x-1) = 1$

c) $\log(x^2 - 1) = \log(2x + 2)$

#### Aufgabe 5: Anwendungen

a) Ein radioaktives Element hat eine Halbwertszeit von 20 Jahren. Wie lange dauert es, bis nur noch 5 % der ursprünglichen Menge vorhanden sind?

b) Ein Kapital wächst mit 3 % p. a. (kontinuierlich, $N(t) = N_0 \cdot e^{0{,}03 t}$). Nach wie vielen Jahren hat es sich verdoppelt?

### Lösungen

<details open><summary>Lösung Aufgabe 1: Exponentialgleichungen</summary>

a) $3^x = 3^4 \implies x = 4$

b) $2^{x-1} = 2^{-1} \implies x - 1 = -1 \implies x = 0$

c) $x = \frac{\ln 12}{\ln 5} \approx \frac{2{,}485}{1{,}609} \approx 1{,}544$

d) $(x+1)\ln 2 = x \ln 3 \implies x(\ln 3 - \ln 2) = \ln 2 \implies x = \frac{\ln 2}{\ln 3 - \ln 2} = \frac{\ln 2}{\ln(3/2)} \approx 1{,}709$

</details>

<details open><summary>Lösung Aufgabe 2: $e^x$ und $\ln$</summary>

a) $3x = \ln 20 \implies x = \frac{\ln 20}{3} \approx 0{,}999$

b) $e^x = \frac{7}{2} \implies x = \ln\frac{7}{2} \approx 1{,}253$

c) $2x - 1 = e^3 \implies x = \frac{e^3 + 1}{2} \approx 10{,}54$

d) $e^{2x} = 4 \implies 2x = \ln 4 \implies x = \frac{\ln 4}{2} = \ln 2 \approx 0{,}693$

</details>

<details open><summary>Lösung Aufgabe 3: Substitution</summary>

a) $u = e^x$: $u^2 - 5u + 6 = 0 \implies u = 2$ oder $u = 3$.
$x = \ln 2 \approx 0{,}693$ oder $x = \ln 3 \approx 1{,}099$

b) $u = 2^x$: $u^2 - 3u - 4 = 0 \implies u = 4$ oder $u = -1$.
$u = -1 < 0$ → verworfen. $2^x = 4 \implies x = 2$

c) $u = 3^x$: $u^2 - 4u + 3 = 0 \implies u = 1$ oder $u = 3$.
$3^x = 1 \implies x = 0$; $3^x = 3 \implies x = 1$

</details>

<details open><summary>Lösung Aufgabe 4: Logarithmische Gleichungen</summary>

a) DM: $x > 2$. $\log_2(x(x-2)) = 3 \implies x^2 - 2x - 8 = 0 \implies x = 4$ oder $x = -2$.
$x = -2$ verletzt DM → Scheinlösung. **Lösung: $x = 4$**

b) DM: $x > 1$. $\ln\!\left(\frac{x+1}{x-1}\right) = 1 \implies \frac{x+1}{x-1} = e \implies x = \frac{e+1}{e-1} \approx 2{,}164$

c) DM: $|x| > 1$ und $x > -1$, also $x > 1$. $x^2 - 1 = 2x + 2 \implies x^2 - 2x - 3 = 0 \implies x = 3$ oder $x = -1$.
$x = -1$: DM verletzt → Scheinlösung. **Lösung: $x = 3$**

</details>

<details open><summary>Lösung Aufgabe 5: Anwendungen</summary>

a) $k = \frac{\ln 2}{20}$. Gesucht: $e^{-kt} = 0{,}05 \implies -kt = \ln(0{,}05) \implies t = \frac{-\ln(0{,}05)}{k} = \frac{20 \ln(20)}{\ln 2} \approx 86{,}4$ Jahre

b) $e^{0{,}03 T_2} = 2 \implies T_2 = \frac{\ln 2}{0{,}03} \approx 23{,}1$ Jahre

</details>

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| Einfache Exponentialgleichungen | Basis angleichen oder beide Seiten logarithmieren |
| $e^x$ und $\ln$ | Umkehrfunktionen: $\ln(e^x) = x$, $e^{\ln x} = x$ |
| Substitution | $u = e^x$ (oder $u = a^x$) reduziert auf quadratische Gleichung |
| Logarithmische Gleichungen | DM prüfen ($A > 0$), Logarithmengesetze nutzen, exponenzieren |
| Halbwertszeit | $T_{1/2} = \frac{\ln 2}{\|k\|}$ — Zeit bis zur Hälfte |
| Verdopplungszeit | $T_2 = \frac{\ln 2}{k}$ — Zeit bis zur Verdopplung |

---

## Glossar

| Deutsch | English |
|---------|---------|
| Exponentialgleichung | Exponential equation |
| Logarithmische Gleichung | Logarithmic equation |
| Basis angleichen | Equalize the base |
| Logarithmieren | Taking the logarithm |
| Natürlicher Logarithmus | Natural logarithm |
| Substitution | Substitution |
| Rücksubstitution | Back-substitution |
| Wachstumsrate | Growth rate |
| Zerfallskonstante | Decay constant |
| Halbwertszeit | Half-life |
| Verdopplungszeit | Doubling time |
| Scheinlösung | Extraneous solution |
| Definitionsmenge | Domain |
| Exponentielles Wachstum | Exponential growth |
| Exponentieller Zerfall | Exponential decay |
