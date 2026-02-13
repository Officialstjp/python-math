Steigungsverhalten einer Funktionen

Man kann eine Sekante definieren, die durch zwei Punkte auf dem Graphen einer Funktion verläuft. Die Steigung dieser Sekante gibt eine durchschnittliche Änderungsrate der Funktion zwischen diesen beiden Punkten an.

Nähert man die beiden Punkte immer weiter aneinander an, und erreicht diesen Punkt, so ist dies nicht mehr eine Sekante, sondern eine Tangente. Die Steigung dieser Tangente gibt die momentane Änderungsrate der Funktion an diesem Punkt an.

Steigung und Tangente haben im Berührpunkt diesebe Steigung

Dies kann man mithilfe des Differenzialquotienten mathematisch ausdrücken, ist aber relativ aufwendig.

Daher wird in der Analysis oft mit vordefinierten Rechenregeln gearbeitet, um die Steigung von Funktionen zu bestimmen.



Allgemeine Ausdrücke:

Differenzenquotient: Mittlere Änderungsrate (Steigungsdreieck)
Differenzialquotient: Momentane Änderungsrate (Tangente / 1. Ableitung)
1. Ableitung: Steigungsverhalten einer Funktion -> aus diesen lassen sich Aussagen über das Verhalten der Funktion ableiten (Extremwerte, ...)
2. Ableitung: Krümmungsverhalten einer Funktion -> aus diesen lassen sich Aussagen über das Krümmungsverhalten der Funktion ableiten (Wendepunkte, Rechts/Links-Kurven...)
3. Ableitung: Momentanänderungsrate der Krümmung -> aus diesen lassen sich Aussagen über das Verhalten der Krümmung ableiten (Änderung des Krümmungsverhaltens...)



Weitere Begriffe:
Extremwerte, Hochpunkte, Tiefpunkte, Wendepunkte, 



Regeln zum Ableiten von Funktionen:

Potenzregel:
f(x) = x^n  =>  f'(x) = n*x^(n-1)

Faktorregel:
Wenn ein multiplikativer Faktor in der Funktion vorhanden ist, bleibt dieser beim Ableiten erhalten.
f(x) = k*g(x)  =>  f'(x) = k*g'(x)

Konstantenregel:
Beim ableiten, fallen Konstanten weg.
f(x) = k*x**2 + 1  =>  f'(x) = k*x

Summenregel:
Beim Ableiten von Summen, werden die einzelnen Summanden abgeleitet und die Ergebnisse addiert.
f(x) = g(x) + h(x)  =>  f'(x) = g'(x) + h'(x)



Spezialfälle:

Ableitung von e-Funktionen:
f(x) = e^x  =>  f'(x) = e^x
(Ableitung von e-Funktionen bleibt gleich)

Ableitung von ln-Funktionen:
f(x) = ln(x)  =>  f'(x) = 1/x
(Ableitung von ln-Funktionen ist der Kehrwert des Arguments)

Ableitung von Sinus-Funktionen:
f(x) = sin(x)  =>  f'(x) = cos(x)
f(x) = cos(x)  =>  f'(x) = -sin(x)
f(x) = -sin(x)  =>  f'(x) = -cos(x)
f(x) = -cos(x)  =>  f'(x) = sin(x)
(Ableitungen von Sinus- und Kosinus-Funktionen folgen einem zyklischen Muster)


Nullstellen: Funktion null setzen und nach x auflösen
Extremstellen: 1. Ableitung null setzen und nach x auflösen
Wendestellen: 2. Ableitung null setzen und nach x auflösen

Visualisierung:
Funktionsgraphen übereinander legen:
- Ursprungsfunktion f(x)
- 1. Ableitung f'(x)
- 2. Ableitung f''(x)
- 3. Ableitung f'''(x) (möglich?)

Extremwerte der Usprungsfunktion entsprechen den Nullstellen der 1. Ableitung.
Extremwerte der 1. Ableitung entsprechen den Wendepunkten der Ursprungsfunktion / den NUllstellen der 2. Abletung.
Extremwerte der 2. Ableitung entsprechen den Wendepunkten der 1. Ableitung / den Nullstellen der 3. Ableitung.