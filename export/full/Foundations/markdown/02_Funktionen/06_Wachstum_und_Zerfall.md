# Funktionen

## 06 - Wachstum und Zerfall

Exponentielles Wachstum und Zerfall: 
- Basis-Form $N(t) = N_0 \cdot a^t$ vs. e-Form $N(t) = N_0 \cdot e^{\lambda t}$ mit Umrechnung $a = e^\lambda$ 
- Verdopplungszeit ($T_2 = \ln 2 / \lambda$), Halbwertszeit ($T_{1/2} = \ln 2 / |\lambda|$)
- begrenztes und logistisches Wachstum.

> Vorausgesetzt: Exponential- und Logarithmusfunktionen.

### Lernziele

- **Exponentielles Wachstum** und **exponentiellen Zerfall** modellieren
- Zwischen der **Basis-Form** $N(t) = N_0 \cdot a^t$ und der **e-Form** $N(t) = N_0 \cdot e^{\lambda t}$ umrechnen
- **Verdopplungszeit** und **Halbwertszeit** bestimmen
- **Begrenztes Wachstum** und **logistisches Wachstum** einordnen
- Wachstumsmodelle auf realistische Probleme anwenden

---

### 1. Exponentielles Wachstum und Zerfall

Ein Prozess heisst **exponentiell**, wenn die Änderungsrate proportional zum aktuellen Bestand ist.

**Basis-Form (Wachstumsfaktor):**

$$N(t) = N_0 \cdot a^t$$

| Symbol | Bedeutung |
|--------|-----------|
| $N_0$ | Anfangswert zum Zeitpunkt $t = 0$ |
| $a$ | Wachstumsfaktor pro Zeiteinheit |
| $t$ | Zeit |

Ist $a > 1$, wächst der Bestand - der Prozess beschleunigt sich mit der Zeit. Ist $0 < a < 1$, nimmt er ab. Beides ist dasselbe Modell, nur mit verschiedenen Vorzeichen in $\lambda$.

**e-Form (Wachstumsrate):**

$$N(t) = N_0 \cdot e^{\lambda t}$$

| Symbol | Bedeutung |
|--------|-----------|
| $\lambda > 0$ | Wachstumsrate → Zunahme |
| $\lambda < 0$ | Zerfallsrate → Abnahme |

**Umrechnung** zwischen den Formen:

$$a = e^{\lambda} \quad \Longleftrightarrow \quad \lambda = \ln(a)$$

Die e-Form ist in der Mathematik und Physik üblicher, weil sich $e^{\lambda t}$ leichter differenzieren lässt: $\frac{d}{dt} N_0 \, e^{\lambda t} = \lambda \, N_0 \, e^{\lambda t}$.


    
![png](06_Wachstum_und_Zerfall_files/06_Wachstum_und_Zerfall_2_0.png)
    


### 2. Verdopplungszeit und Halbwertszeit

Zwei zentrale Kenngrößen für exponentielle Prozesse:

**Verdopplungszeit** $t_2$ (bei Wachstum, $\lambda > 0$):

$$N(t_2) = 2 \, N_0 \quad \Rightarrow \quad e^{\lambda t_2} = 2 \quad \Rightarrow \quad t_2 = \frac{\ln 2}{\lambda}$$

**Halbwertszeit** $t_{1/2}$ (bei Zerfall, $\lambda < 0$):

$$N(t_{1/2}) = \frac{N_0}{2} \quad \Rightarrow \quad e^{\lambda \, t_{1/2}} = \frac{1}{2} \quad \Rightarrow \quad t_{1/2} = \frac{\ln 2}{|\lambda|}$$

In der Basis-Form:

$$t_2 = \frac{\ln 2}{\ln a} \qquad \text{bzw.} \qquad t_{1/2} = \frac{\ln 2}{\ln(1/a)} = \frac{-\ln 2}{\ln a}$$

| Kenngrößen | Formel (e-Form) | Formel (Basis-Form) |
|------------|-----------------|---------------------|
| Verdopplungszeit | $t_2 = \frac{\ln 2}{\lambda}$ | $t_2 = \frac{\ln 2}{\ln a}$ |
| Halbwertszeit | $t_{1/2} = \frac{\ln 2}{\lvert\lambda\rvert}$ | $t_{1/2} = \frac{\ln 2}{\ln(1/a)}$ |
| Prozentuale Änderung/ZE | $p = e^{\lambda} - 1$ | $p = a - 1$ |


    
![png](06_Wachstum_und_Zerfall_files/06_Wachstum_und_Zerfall_4_0.png)
    


### 3. Weitere Wachstumsmodelle

Exponentielles Wachstum ist unbegrenzt - in der Realität gibt es oft eine **Kapazitätsgrenze**.

---

#### Begrenztes Wachstum (Sättigungsmodell)

$$N(t) = S - (S - N_0) \cdot e^{-k t} \qquad (k > 0)$$

Der Bestand nähert sich der **Schranke** $S$ an, ohne sie zu überschreiten. Die Änderungsrate wird kleiner, je näher $N$ an $S$ liegt.

*Beispiele:* Aufwärmen eines Körpers, Ladevorgang eines Kondensators, Lernen einer Fertigkeit.

---

#### Logistisches Wachstum

$$N(t) = \frac{K}{1 + \left(\frac{K - N_0}{N_0}\right) \cdot e^{-r t}}$$

| Symbol | Bedeutung |
|--------|-----------|
| $K$ | Kapazitätsgrenze (Carrying Capacity) |
| $r$ | Wachstumsrate |
| $N_0$ | Anfangswert |

Der Graph hat eine typische **S-Form** (Sigmoidkurve):
1. Anfangs nahezu exponentielles Wachstum
2. Wendepunkt bei $N = K/2$ - maximale Wachstumsgeschwindigkeit
3. Sättigung: $N(t) \to K$ für $t \to \infty$

*Beispiele:* Populationsdynamik, Verbreitung von Epidemien, Marktdurchdringung.


    
![png](06_Wachstum_und_Zerfall_files/06_Wachstum_und_Zerfall_6_0.png)
    


### 4. Anwendungsbeispiele

Das folgende Überblick zeigt, wie die verschiedenen Modelle auf reale Phänomene passen. Wichtig dabei: Die Wahl des Modells - unbeschränkt, begrenzt oder logistisch - hängt davon ab, ob es eine physikalische Obergrenze gibt.

| Anwendung | Modell | Typische Parameter |
|-----------|--------|--------------------|
| Radioaktiver Zerfall | $N(t) = N_0 \cdot e^{-\lambda t}$ | C-14: $t_{1/2} = 5730$ Jahre |
| Bakterienwachstum | $N(t) = N_0 \cdot 2^{t/t_2}$ | E. coli: $t_2 \approx 20$ min |
| Zinseszins | $K(t) = K_0 \cdot (1 + p/100)^t$ | Jahreszins $p$ in % |
| Stetige Verzinsung | $K(t) = K_0 \cdot e^{rt}$ | $r = \ln(1 + p/100)$ |
| Abkühlung (Newton) | $T(t) = T_U + (T_0 - T_U) \cdot e^{-kt}$ | Begrenztes Modell |
| Bevölkerung | Logistisch | Kapazitätsgrenze $K$ |

**Modellwahl:**  
- **Unbeschränktes** exponentielles Modell: geeignet für kurze Zeiträume  

- **Begrenztes** Modell: wenn ein Sättigungswert bekannt ist  - **Logistisches** Modell: wenn zunächst exponentielles Wachstum vorliegt, das sich dann verlangsamt

    === Zinseszins-Vergleich ===
    
    Anfangskapital: 1000 €, Zinssatz: 5%
    
    Jahre      Jährlich        Stetig         
    ----------------------------------------
    5          1276.28         1276.28        
    10         1628.89         1628.89        
    20         2653.30         2653.30        
    30         4321.94         4321.94        
    
    === Radioaktiver Zerfall (C-14) ===
    
    Halbwertszeit: 5730 Jahre
    Zerfallsrate λ = 0.000121 pro Jahr
    Nach 5730 Jahren: 50.0% übrig
    Nach 11460 Jahren: 25.0% übrig
    Nach 17190 Jahren: 12.5% übrig


---

## Verständnis-Check

**Aufgabe 1:** Eine Bakterienkultur verdoppelt sich alle 30 Minuten. Zu Beginn sind 500 Bakterien vorhanden.  
a) Stelle die Wachstumsfunktion in der Basis-Form auf.  
b) Wie viele Bakterien sind nach 3 Stunden vorhanden?

**Aufgabe 2:** Ein radioaktiver Stoff hat eine Halbwertszeit von 8 Tagen. Bestimme die Zerfallsrate $\lambda$ und berechne, nach wie vielen Tagen noch 10% der Ausgangssubstanz übrig sind.

**Aufgabe 3:** Du legst 5000 € zu 3,5% Jahreszins an. Berechne das Kapital nach 15 Jahren.

**Aufgabe 4:** Eine Population wächst logistisch mit $K = 10\,000$, $N_0 = 100$, $r = 0{,}4$. Bestimme den Wendepunkt (Zeitpunkt und Populationsgröße).

### Lösungen

<details open>
<summary>Lösung Aufgabe 1</summary>

a) $N(t) = 500 \cdot 2^{t/0{,}5} = 500 \cdot 2^{2t}$ (mit $t$ in Stunden)

Alternativ: $N(t) = 500 \cdot 2^{t/30}$ (mit $t$ in Minuten)

b) $N(3) = 500 \cdot 2^{6} = 500 \cdot 64 = 32\,000$
</details>

<details open>
<summary>Lösung Aufgabe 2</summary>

$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{\ln 2}{8} \approx 0{,}0866$ pro Tag

$0{,}1 = e^{-\lambda t} \Rightarrow t = \frac{-\ln(0{,}1)}{\lambda} = \frac{\ln 10}{\ln 2 / 8} = \frac{8 \ln 10}{\ln 2} \approx 26{,}6$ Tage
</details>

<details open>
<summary>Lösung Aufgabe 3</summary>

$K(15) = 5000 \cdot 1{,}035^{15} = 5000 \cdot 1{,}6753 \approx 8376{,}49$ €
</details>

<details open>
<summary>Lösung Aufgabe 4</summary>

Der Wendepunkt liegt bei $N = K/2 = 5000$.

Zeitpunkt: $\frac{K}{2} = \frac{K}{1 + \frac{K - N_0}{N_0} e^{-rt}}$

$\Rightarrow e^{-rt} = \frac{N_0}{K - N_0} \Rightarrow t = \frac{1}{r} \ln\left(\frac{K - N_0}{N_0}\right) = \frac{1}{0{,}4} \ln\left(\frac{9900}{100}\right) = 2{,}5 \cdot \ln(99) \approx 11{,}5$
</details>

---

## Zusammenfassung

| Thema | Kernaussage |
|-------|-------------|
| **Exp. Wachstum** | $N(t) = N_0 \cdot a^t$ mit $a > 1$, oder $N_0 \cdot e^{\lambda t}$ mit $\lambda > 0$ |
| **Exp. Zerfall** | $a < 1$ bzw. $\lambda < 0$ |
| **Umrechnung** | $a = e^{\lambda}$, $\lambda = \ln(a)$ |
| **Verdopplungszeit** | $t_2 = \frac{\ln 2}{\lambda}$ |
| **Halbwertszeit** | $t_{1/2} = \frac{\ln 2}{\lvert\lambda\rvert}$ |
| **Begrenztes Wachstum** | $N(t) = S - (S-N_0) \, e^{-kt}$ - nähert sich Schranke $S$ |
| **Logistisches Wachstum** | S-Kurve mit Kapazitätsgrenze $K$, Wendepunkt bei $K/2$ |



---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Exponentielles Wachstum | Exponential growth |
| Exponentieller Zerfall | Exponential decay |
| Halbwertszeit | Half-life |
| Verdopplungszeit | Doubling time |
| Wachstumsfaktor | Growth factor |
| Wachstumsrate | Growth rate |
| Begrenztes Wachstum | Limited/bounded growth |
| Logistisches Wachstum | Logistic growth |
| Kapazitätsgrenze | Carrying capacity |
| Wendepunkt | Inflection point |
