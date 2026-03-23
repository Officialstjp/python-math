# Analysis
## 01 - Einführung: Was ist Analysis?
Die Mathematik der Veränderung

Die **Analysis** (auch: Infinitesimalrechnung) ist eines der mächtigsten Werkzeuge der Mathematik. Sie wurde im 17. Jahrhundert unabhängig voneinander von **Isaac Newton** und **Gottfried Wilhelm Leibniz** entwickelt und ist heute die Grundlage für Physik, Ingenieurwesen, Wirtschaft, Informatik und vieles mehr.

Die zentrale Frage der Analysis: **Wie beschreibt man Veränderung mathematisch exakt?**

### Lernziele

In diesem Kapitel werden folgende Themen behandelt:

- **Was Analysis ist** und warum sie so wichtig ist
- **Grenzwerte** - die mathematische Grundlage (Wiederholung aus Funktionen)
- **Differentialrechnung** - Ableitungen, Steigungen, Kurvendiskussion
- **Integralrechnung** - Flächen, Stammfunktionen, der Hauptsatz
- **Partielle Ableitungen** - Funktionen mit mehreren Variablen

---

### 1. Die drei Säulen der Analysis

Die Analysis besteht aus drei eng verbundenen Konzepten:

| Säule | Kernfrage | Werkzeug |
|-------|-----------|----------|
| **Grenzwerte** | Was passiert, wenn wir uns einem Wert *unendlich nah* annähern? | $\lim_{x \to a} f(x)$ |
| **Differentialrechnung** | Wie schnell ändert sich eine Funktion? Was ist die Steigung? | $f'(x) = \frac{df}{dx}$ |
| **Integralrechnung** | Wie groß ist die Fläche unter einer Kurve? Was ist das Gegenteil der Ableitung? | $\int f(x)\,dx$ |

Diese drei Konzepte hängen zusammen:
- Die **Ableitung** ist als **Grenzwert** definiert: $f'(x) = \lim_{h\to 0} \frac{f(x+h)-f(x)}{h}$
- Der **Hauptsatz der Analysis** verbindet Ableitung und Integral: Ableiten und Integrieren sind *Umkehroperationen*

#### Die große Idee

Viele Größen in der Natur verändern sich *ständig*. Ein Auto beschleunigt, die Temperatur schwankt, eine Population wächst. Die Analysis gibt uns die Sprache, um solche **kontinuierlichen Veränderungen** präzise zu beschreiben:

- **Ableitung**: Geschwindigkeit ist die Ableitung des Ortes. Beschleunigung ist die Ableitung der Geschwindigkeit.
- **Integral**: Der zurückgelegte Weg ist das Integral der Geschwindigkeit. Die Gesamtmenge ist das Integral der Rate.


    
![png](01_Einf%C3%BChrung_in_die_Analysis_files/01_Einf%C3%BChrung_in_die_Analysis_2_0.png)
    


### 2. Wozu braucht man Analysis?

Einige Beispiele, in denen Analysis unverzichtbar ist:

| Bereich | Anwendung | Analysis-Werkzeug |
|---------|-----------|-------------------|
| **Physik** | Bewegung, Kräfte, Energie | Ableitungen (Geschwindigkeit, Beschleunigung) |
| **Ingenieurwesen** | Optimierung von Formen, Materialien | Extremwertprobleme (Kurvendiskussion) |
| **Wirtschaft** | Gewinnmaximierung, Kostenfunktionen | Ableitung = Grenzkosten/Grenzertrag |
| **Medizin** | Medikamentenabbau im Körper | Differentialgleichungen (exp. Zerfall) |
| **Informatik / KI** | Maschinelles Lernen, neuronale Netze | Gradient Descent (partielle Ableitungen) |
| **Statistik** | Wahrscheinlichkeitsverteilungen | Integrale (Fläche unter der Verteilung) |

### 3. Voraussetzungen für diese Reihe

Bevor Du in die Analysis eintauchst, solltest Du sicher sein mit:
- **Funktionen** - Funktionsbegriff, Darstellungsformen, Graphen lesen 
- **Polynome** - Quadratische Funktionen, Parabeln
- **Exponential- und Logarithmusfunktionen** - $e^x$, $\ln(x)$ 
- **Trigonometrie** - $\sin$, $\cos$, $\tan$ 
- **Grenzwerte** - Grundlage in der Analysis

---

### 4. Roadmap: Übersicht der Notebooks

| # | Notebook | Thema |
|---|----------|-------|
| 01 | **Einführung** (dieses Notebook) | Was ist Analysis? Überblick und Motivation |
| 02 | **Ableitungen: Einführung** | Sekante → Tangente, Grenzwertdefinition, numerisch & symbolisch |
| 03 | **Ableitungsregeln** | Potenz-, Produkt-, Quotienten-, Kettenregel |
| 04 | **Höhere Ableitungen & Kurvendiskussion** | $f'$, $f''$, Extrema, Wendepunkte, vollständige Kurvenanalyse |
| 05 | **Integralrechnung: Einführung** | Stammfunktion, bestimmtes Integral, Hauptsatz |
| 06 | **Integrationsregeln & Anwendungen** | Regeln, Flächen, Volumina, Anwendungen |
| 07 | **Partielle Ableitungen** | Funktionen mehrerer Variablen, Gradient |

### 5. Ein erstes Beispiel: Die Flächenberechnung

Eines der ältesten Probleme der Mathematik ist die Berechnung von Flächen unter Kurven. Schon **Archimedes** (ca. 250 v. Chr.) näherte die Fläche unter einer Parabel mit immer kleineren Rechtecken an.

Diese Idee - **eine krumme Fläche durch viele kleine Rechtecke annähern** - ist der Kern der Integralrechnung. Je mehr Rechtecke wir verwenden, desto genauer wird die Annäherung. Im Grenzwert (unendlich viele, unendlich schmale Rechtecke) erhalten wir die exakte Fläche.


    
![png](01_Einf%C3%BChrung_in_die_Analysis_files/01_Einf%C3%BChrung_in_die_Analysis_5_0.png)
    


Mit nur 4 Rechtecken ist die Annäherung grob, aber mit 100 Rechtecken wird der Fehler verschwindend klein. Im Grenzwert ($n \to \infty$) erhalten wir das **bestimmte Integral** - die exakte Fläche.

Das ist der rote Faden der gesamten Analysis: **Annäherung → Grenzwert → exakter Wert**.
Wie diese Idee in der Differentialrechnung (Ableitungen) und Integralrechnung (Integrale) umgesetzt wird, lernst du in den kommenden Notebooks!

---

## Zusammenfassung

| Konzept | Kernaussage |
|---------|-------------|
| **Analysis** | Mathematik der Veränderung: Grenzwerte, Ableitungen, Integrale |
| **Ableitung** | Misst, wie schnell sich etwas ändert (Steigung, Geschwindigkeit) |
| **Integral** | Summiert unendlich viele unendlich kleine Beiträge (Fläche, Gesamtweg) |
| **Hauptsatz** | Ableiten und Integrieren sind Umkehroperationen |
| **Grundidee** | *Annäherung → Grenzwert → exakter Wert* |

> **Nächster Schritt:** Wie misst man die Steigung einer Kurve? → 02_Ableitungen_Einfuehrung

---

## Glossar

| Deutsch | Englisch |
|---------|----------|
| Analysis / Infinitesimalrechnung | Calculus |
| Differentialrechnung | Differential calculus |
| Integralrechnung | Integral calculus |
| Grenzwert | Limit |
| Ableitung | Derivative |
| Integral | Integral |
| Stammfunktion | Antiderivative |
| Hauptsatz der Analysis | Fundamental Theorem of Calculus |
| Riemann-Summe | Riemann sum |
| Momentane Änderungsrate | Instantaneous rate of change |
