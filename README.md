

# Math Repository

Eine strukturierte Sammlung von Jupyter-Notebooks, die Mathematik von den Grundlagen bis zur Analysis sowie die Grundlagen des maschinellen Lernens abdecken. Jedes Notebook ist eine eigenständige Referenz, die Theorie, Formeln, Beispiele und Visualisierungen kombiniert.

## Struktur

| Verzeichnis    | Inhalt                                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Foundations/` | Kerncurriculum der Mathematik (Grundlagen → Algebra → Funktionen → Geometrie → Trigonometrie → Vektoren & Matrizen → Folgen & Reihen → Analysis → Statistik) |
| `ml/`          | Grundlagen des maschinellen Lernens (Informationstheorie, Tensoren, Optimierung)                                                                             |
| `experiments/` | Explorative Notebooks (zelluläre Automaten, Ableitungen)                                                                                                     |
| `scripts/`     | Export- & Konsolidierungspipeline (siehe [scripts/README.md](scripts/README.md))                                                                             |
| `exports/`     | Generierte HTML-, Markdown- und PDF-Ausgaben                                                                                                                 |

## Schnellstart

```powershell
# Aktivieren des venv
.\venv\Scripts\activate

# Exportieren der Foundations als HTML + Markdown (reine Referenz: kein Code, keine Übungen)
python scripts/export_notebooks.py --source-dir Foundations --formats html markdown --no-text-output --no-exercises --output-dir exports/Foundations --workers 8

# Exportieren der Foundations als PDF
python scripts/export_notebooks.py --source-dir Foundations --formats pdf --no-text-output --no-exercises --output-dir exports/Foundations --workers 4

# Konsolidierte PDF-Referenz erstellen
python scripts/consolidate_pdfs.py --pdf-dir exports/Foundations/pdf --output-dir exports/Foundations/pdf --title "Gesamtreferenz" --output-name GesamtReferenz.pdf
```

Siehe [scripts/README.md](scripts/README.md) für die vollständige Dokumentation aller Exportoptionen (englisch).
