

# Math Repository

Dieses Repository ist eine über Monate gewachsene Sammlung freier Mathematik-Notebooks und Referenzen bis ungefähr BRP-/Matura-Niveau, mit ein paar Ausflügen darüber hinaus.

Der Schwerpunkt liegt klar auf dem Inhalt: Grundlagen, Algebra, Funktionen, Geometrie, Trigonometrie, Vektoren und Matrizen, Folgen und Reihen, Analysis, Statistik und Wahrscheinlichkeit. Dazu kommen ein paar angrenzende ML-Grundlagen und etwas Platz für kleinere, in sich geschlossene Experimente zu Anwendungen oder einfach interessanten Ideen.

Das hier ist kein Produkt, keine Kursplattform und kein fertiges, einheitliches Werk. Es ist im Wesentlichen der Versuch, viel mathemische Arbeit sauber an einem Ort zu sammeln, so dass andere damit tatsächlich etwas anfangen können.

## Was ist das hier?

- Mathematik von den Grundlagen bis in die Analysis und Statistik
- Material in Notebook-Form mit Erklärungen, Formeln, Beispielen und Visualisierungen
- Exportierte Fassungen in Markdown, HTML und PDF
- Ergänzende ML-Notizen dort, wo sie mathematisch gut anschließen
- Ein kleiner Bereich für Experimente, Sidepaths und kompakte Anwendungen

Der grobe Zielrahmen ist schulische Mathematik bis zur österreichischen BRP / Matura, auch wenn einzelne Teile bewusst etwas weitergehen, wenn es fachlich gerade sinnvoll ist.


## Struktur

| Verzeichnis    | Inhalt |
| -------------- | ------ |
| `Foundations/` | Hauptteil der Mathematik-Notebooks, von Grundlagen bis Statistik |
| `ml/`          | Ergänzende ML-Grundlagen wie Informationstheorie, Tensoren und Optimierung |
| `experiments/` | Kleinere, eher selbstständige Erkundungen, Anwendungen und Nebenspuren |
| `export/markdown/` | Gut lesbare exportierte Markdown-Fassungen |
| `exports/`     | Generierte HTML-, Markdown- und PDF-Ausgaben |
| `scripts/`     | Hilfsskripte für Export und Konsolidierung |


Wenn du einfach nur reinlesen willst, ist `export/markdown` meist der angenehmste Einstieg.

Das Quellmaterial selbst liegt überwiegend in Jupyter-Notebooks. Von dort aus werden die verschiedenen Ausgabeformate erzeugt.

Der fachliche Inhalt ist derzeit großteils auf Deutsch.

## Warum?

Angefangen hat das Projekt als Mitschrift zur Matura (Abitur), um vorallem händische Mitschriften durch saubere, digitalisierte Fassungen zu verfestigen. Warum dann nicht einfach etwas aufputzen?

Außerdem wäre es schade, so viel Arbeit in etwas zu stecken, das nach der Prüfung eh nur mehr rumliegt. Wenn die Notizen jemandem beim Lernen, Wiederholen, Nachschlagen oder Unterrichten helfen, erfüllt das den Zweck schon ziemlich gut.

Über Zeit könnten die Themen durchaus weiterwachsen, das wird sich zeigen. Also: Projet ist laufend in Arbeit.
Manche Teile sind schon recht rund, andere noch im Ausbau oder in Überarbeitung.

## Falls du exportieren willst

```powershell
# Aktivieren des venv
.\venv\Scripts\activate

# Foundations als HTML + Markdown exportieren
python scripts/export_notebooks.py --source-dir Foundations --formats html markdown --no-text-output --no-exercises --output-dir exports/Foundations --workers 8

# Foundations als PDF exportieren
python scripts/export_notebooks.py --source-dir Foundations --formats pdf --no-text-output --no-exercises --output-dir exports/Foundations --workers 4
```

Mehr dazu steht in [scripts/README.md](scripts/README.md) (in englisch mind you).
