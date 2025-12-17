Ich möchte meine Jupyter Math notebooks erweitern. Einige sind bereits erstellt, diese nehmen wir als referenzen (und können natürlich weiterbauen)
Ich habe einige Notizbücher beigelegt, basierend auf diesen werden wir nun mit dem richtigen Mathematischen Wissen 01_Vektoren auch befüllen. Das Ziel hier ist eine auf BRP (Matura/Abitur) und hinausgehend (Studium) Datenbasis an notebooks.

Bitte erklär und gib mir jegliche additionen in selber Markdown / Code "Block" Struktur (e.g., Python Code Blöcke für Python Code, Markdown Code-blöcke für markdown (Achte auf Code-block-delimiter in den eigentlichen code-blöcken, um frühzeitiges escape zu vermeiden!))

Als ersten Schritt werden wir 01_Vektoren fertigstellen, bitte gib mir schritt für schritt die nötigen addition / Änderungen, sei es über mehrere Antworten




## Definition

Ein **Vektor** beschreibt eine gerichtete Größe: **Länge (Betrag)** und **Richtung**.  
Geometrisch kann man ihn als **Menge aller gleich langen, gleich gerichteten und gleich orientierten Pfeile** auffassen (unabhängig vom Ort).

Ein einzelner Pfeil dieser Menge ist ein **Repräsentant** (Stellvertreter) des entsprechenden Vektors.

### Notation
- Vektoren: $\vec a,\ \vec b$ (oder fett: $\mathbf a,\ \mathbf b$)
- Betrag / Norm: $|\vec a|$ oder $\|\vec a\|$

### Nullvektor
Der **Nullvektor** ist der Vektor mit Betrag $0$:
$$
\vec 0 = \begin{pmatrix}0\\0\end{pmatrix}\quad (\text{bzw. } \begin{pmatrix}0\\0\\0\end{pmatrix})
$$
Er hat **keine Richtung** (bzw. Richtung ist nicht sinnvoll definiert).

### Einheitsvektor
Ein **Einheitsvektor** hat Betrag $1$ und zeigt in eine bestimmte Richtung.

Der Einheitsvektor in Richtung eines Vektors $\vec a \neq \vec 0$ ist:
$$
\hat a = \frac{\vec a}{\|\vec a\|}.
$$

---





# Regeln für Vektoren

## Gegenvektor
- Der Vektor $\vec{BA} = -\vec{AB}$ heißt **Gegenvektor** des Vektors $\vec{AB}$.
- Der Gegenvektor $-\vec a$ hat **gleichen Betrag**, **gleiche Richtung**, aber **entgegengesetzte Orientierung**.

## Addition / Subtraktion (komponentenweise)
Vektoren werden komponentenweise addiert bzw. subtrahiert:
$$
\vec a \pm \vec b
=
\begin{pmatrix} a_x \\ a_y \end{pmatrix}
\pm
\begin{pmatrix} b_x \\ b_y \end{pmatrix}
=
\begin{pmatrix} a_x \pm b_x \\ a_y \pm b_y \end{pmatrix}.
$$

**Grafisch:** Bei $\vec a + \vec b$ wird der **Schaft** von $\vec b$ an die **Spitze** von $\vec a$ gesetzt.  
Die Summe ist der Pfeil **vom Schaft von $\vec a$ zur Spitze von $\vec b$**.

## Skalarmultiplikation (komponentenweise)
Für einen Skalar $c \in \mathbb{R}$ gilt:
$$
c \cdot \vec a
=
c \cdot \begin{pmatrix} a_x \\ a_y \end{pmatrix}
=
\begin{pmatrix} c\,a_x \\ c\,a_y \end{pmatrix}.
$$

- $c>0$: Richtung bleibt gleich, Länge skaliert.
- $c<0$: Orientierung kehrt sich um, Länge skaliert mit $|c|$.

---






## Lernziele 

Nach diesem Notebook kannst du:

- Vektoren als Elemente von $\mathbb{R}^2$ und $\mathbb{R}^3$ lesen und interpretieren
- Betrag/Norm, Abstand und Einheitsvektoren berechnen
- Vektoren addieren, subtrahieren und mit Skalaren multiplizieren (algebraisch + geometrisch)
- Vektoren zwischen zwei Punkten bestimmen (Spitze–Schaft)
- (als nächster Schritt) Skalarprodukt, Winkel, Projektion und Normal-/Orthogonalität anwenden





## Spitze – Schaft (Vektor zwischen zwei Punkten)

Seien $A(x_A, y_A)$ und $B(x_B, y_B)$ zwei Punkte.  
Der Vektor **von** $A$ **nach** $B$ ist:
$$
\vec{AB} = \vec B - \vec A
=
\begin{pmatrix}x_B\\y_B\end{pmatrix}
-
\begin{pmatrix}x_A\\y_A\end{pmatrix}
=
\begin{pmatrix}x_B-x_A\\y_B-y_A\end{pmatrix}.
$$

In $\mathbb{R}^3$ analog:
$$
\vec{AB}=
\begin{pmatrix}x_B-x_A\\y_B-y_A\\z_B-z_A\end{pmatrix}.
$$

**Merksatz:** *„Spitze minus Schaft“* (Endpunkt minus Startpunkt).

---