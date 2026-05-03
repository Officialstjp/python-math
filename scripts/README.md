# Scripts

Automation scripts for exporting and consolidating Jupyter notebooks into distributable formats.

## Prerequisites

Activate the repository venv before running any script:

```powershell
.\venv\Scripts\activate
```

### Dependencies

| Package      | Used by               | Purpose                             |
| ------------ | --------------------- | ----------------------------------- |
| `nbconvert`  | `export_notebooks.py` | Notebook → HTML/Markdown conversion |
| `playwright` | `export_notebooks.py` | HTML → PDF rendering (Chromium)     |
| `pypdf`      | `consolidate_pdfs.py` | PDF merging & bookmarks             |
| `reportlab`  | `consolidate_pdfs.py` | Cover page & TOC generation         |

```powershell
pip install nbconvert playwright pypdf reportlab
playwright install chromium
```

---

## export_notebooks.py

Converts all `.ipynb` files under a source directory to HTML, Markdown, and/or PDF, mirroring the folder structure into an output directory. Exports run in parallel by default.

**PDF pipeline**: Notebooks are first exported to HTML via nbconvert, then a print-optimised CSS stylesheet is injected (compact fonts, table layout fixes, smart page breaks), and Playwright/Chromium renders the final PDF.

**Per-cell visibility**: Individual code cells can be tagged `show-input` or `hide-input` in notebook metadata to override the global `--no-input` / `--with-input` setting.

### Usage

```powershell
python scripts/export_notebooks.py [OPTIONS]
```

### Parameters

| Flag                            | Default       | Description                                                        |
| ------------------------------- | ------------- | ------------------------------------------------------------------ |
| `--source-dir DIR`              | `Foundations` | Root directory containing notebooks                                |
| `--output-dir DIR`              | `exports`     | Root output directory for exports                                  |
| `--formats {html,markdown,pdf}` | `html`        | Export formats (space-separated)                                   |
| `--no-input`                    | `True`        | Hide code cells in output                                          |
| `--with-input`                  | `False`       | Show code cells (overrides `--no-input`)                           |
| `--no-text-output`              | `False`       | Strip print/stream output, keep only figures and rich HTML         |
| `--no-exercises`                | `False`       | Exclude exercise & solution sections (Verständnis-Check, Lösungen) |
| `--ci`                          | `False`       | CI mode: exit non-zero on any failure                              |
| `--workers N`                   | `4`           | Number of parallel export workers (use 1 to disable)               |

### Examples

```powershell
# Default: export all notebooks to HTML, code hidden
python scripts/export_notebooks.py

# Export HTML and Markdown
python scripts/export_notebooks.py --formats html markdown

# Export both HTML and PDF
python scripts/export_notebooks.py --formats html pdf

# "Pure reference" mode: no code, no print output, no exercises
python scripts/export_notebooks.py --no-text-output --no-exercises

# Export a single chapter with visible code
python scripts/export_notebooks.py --source-dir Foundations/00_Grundlagen --with-input

# Use 8 parallel workers for faster export
python scripts/export_notebooks.py --workers 8
```

### Output Structure

```
exports/
  html/
    00_Grundlagen/
      01_Zahlenmengen_und_Rechenarten.html
      ...
    01_Algebra/
      ...
  markdown/
    00_Grundlagen/
      01_Zahlenmengen_und_Rechenarten.md
      ...
  pdf/
    00_Grundlagen/
      ...
```

---

## lint_figsizes.py

Scans notebook code cells for Matplotlib `figsize` values and reports figures
that are likely to export poorly under the current PDF image box. It resolves
common literal patterns such as `figsize=(6, 4)`, `figsize=config["figsize"]`,
and `fig.set_size_inches(...)`.

### Usage

```powershell
python scripts/lint_figsizes.py --config scripts/export_profile.toml.example
python scripts/lint_figsizes.py --source-dir Foundations/01_Algebra --all
```

---

## consolidate_htmls.py

Merges all individual HTML exports into a single self-contained `reference.html` with a sidebar table of contents, section dividers, and embedded images.

### Usage

```powershell
python scripts/consolidate_htmls.py [OPTIONS]
```

### Parameters

| Flag                 | Default                       | Description                                     |
| -------------------- | ----------------------------- | ----------------------------------------------- |
| `--config FILE`      | `scripts/export_profile.toml` | Optional profile with shared defaults           |
| `--html-dir DIR`     | `exports/html`                | Directory containing exported HTML files        |
| `--output-dir DIR`   | `exports`                     | Where to write the consolidated file            |
| `--output-name FILE` | `reference.html`              | Output filename                                 |
| `--title TEXT`       | `Mathematik - Gesamtreferenz` | Document title (shown in sidebar & browser tab) |
| `--exclude-chapters` | `[]`                          | Chapter folder keys to omit from the merge      |

### Example

```powershell
python scripts/consolidate_htmls.py --title "Mathe Zusammenfassung"
```

---

## consolidate_pdfs.py

Merges all individual PDF exports into a single `reference.pdf` with a cover page, table of contents (with page numbers and dot leaders), and a navigable bookmark outline.

### Usage

```powershell
python scripts/consolidate_pdfs.py [OPTIONS]
```

### Parameters

| Flag                 | Default                       | Description                                      |
| -------------------- | ----------------------------- | ------------------------------------------------ |
| `--config FILE`      | `scripts/export_profile.toml` | Optional profile with shared defaults            |
| `--pdf-dir DIR`      | `exports_clean/pdf`           | Directory containing exported PDF files          |
| `--output-dir DIR`   | `exports_clean`               | Where to write the consolidated file             |
| `--output-name FILE` | `reference.pdf`               | Output filename                                  |
| `--title TEXT`       | `Mathematik - Gesamtreferenz` | Document title (cover page, metadata, bookmarks) |
| `--no-cover`         | `False`                       | Skip cover page and table of contents            |
| `--exclude-chapters` | `[]`                          | Chapter folder keys to omit from the merge       |

### Example

```powershell
python scripts/consolidate_pdfs.py --title "Mathe Zusammenfassung" --no-cover
```

---

## Typical Workflow

```powershell
# 1. Export all notebooks (clean reference: no code, no print output, no exercises)
python scripts/export_notebooks.py --formats html pdf --no-text-output --no-exercises

# 2. Build consolidated HTML reference
python scripts/consolidate_htmls.py

# 3. Build consolidated PDF reference
python scripts/consolidate_pdfs.py
```

**Batch export with presets:**
```powershell
pwsh -File scripts/reexport_all.ps1 -Config scripts/export_profile.toml -NoTextOutput
```

The preset layer stays in `reexport_all.ps1` because it is orchestration data
(which bundles to build, where they go, what the final reference files are
called). The TOML profile stays focused on reusable rendering and layout
defaults.

**Copy: Foundations HTML, Markdown, PDF + Consolidate:**
```bash
pwsh -File scripts/reexport_all.ps1 -Target Foundations -NoTextOutput
```

**Copy: ML HTML, Markdown, PDF + Consolidate:**
```bash
pwsh -File scripts/reexport_all.ps1 -Target ml
```