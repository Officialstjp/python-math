"""
export_notebooks.py - Export Jupyter notebooks to HTML, Markdown, and/or PDF.

Walks source directories for .ipynb files, converts them via nbconvert,
and writes the output into a mirrored folder structure under an export directory.
Exports run in parallel by default for faster throughput.

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

Usage:
    # Export HTML only (default)
    python scripts/export_notebooks.py

    # Export HTML and Markdown
    python scripts/export_notebooks.py --formats html markdown

    # Export both HTML and PDF
    python scripts/export_notebooks.py --formats html pdf

    # Custom source and output directories
    python scripts/export_notebooks.py --source-dir Foundations --output-dir exports

    # Show code cells in output
    python scripts/export_notebooks.py --with-input

    # Strip print/text output, keep only figures
    python scripts/export_notebooks.py --no-text-output

    # Exclude exercise and solution sections
    python scripts/export_notebooks.py --no-exercises

    # "Pure reference" mode: no code, no print output, no exercises
    python scripts/export_notebooks.py --no-text-output --no-exercises

    # CI mode: non-interactive, fail on first error
    python scripts/export_notebooks.py --ci

    # Control parallelism (default: 4 workers, use 1 to disable)
    python scripts/export_notebooks.py --workers 8
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULTS = {
    "source_dir": "Foundations",
    "output_dir": "exports",
    "formats": ["html"],
    "no_input": True,
    "notebook_glob": "**/*.ipynb",
    "workers": 4,
}

VALID_FORMATS = ("html", "markdown", "pdf")

# Heading patterns that mark exercise / solution cells to exclude.
# Matched line-by-line against markdown cell source (case-insensitive).
EXERCISE_HEADING_PATTERNS: list[str] = [
    r"^#+\s*Verständnis",      # "## Verständnis-Check"
    r"^#+\s*Lösungen?\b",      # "### Lösungen"
]

# Mime types considered visual (kept when stripping text output)
VISUAL_MIME_TYPES = {
    "image/png", "image/jpeg", "image/svg+xml", "image/gif",
    "text/html",  # Rendered outputs like DataFrames, widgets
}

# CSS injected into exported HTML to fix table rendering (MathJax wrapping)
TABLE_FIX_CSS = """
<style>
/* Prevent MathJax from wrapping inside table cells */
table { width: 100%; border-collapse: collapse; table-layout: auto; }
th, td { padding: 0.5rem 0.75rem; vertical-align: top; border: 1px solid #ddd; }
th { background: #f5f5f5; font-weight: 600; }
td .MathJax, th .MathJax { white-space: nowrap; display: inline !important; }
td mjx-container, th mjx-container { white-space: nowrap !important; display: inline !important; }
/* Hide empty code-cell input areas (produced by per-cell hide-input tag) */
div.input:has(.highlight pre > span:only-child:empty) { display: none; }
div.jp-Cell-inputWrapper:has(pre > span:only-child:empty) { display: none; }
</style>
"""

# Print-optimised CSS injected into HTML before Playwright renders to PDF.
PDF_PRINT_CSS = """
<style type="text/css">
/* ── 1. Compact fonts ──────────────────────────────────────────── */
:root {
  --jp-content-font-size1: 9pt;
  --jp-content-font-size0: 8pt;
  --jp-code-font-size: 7.5pt;
  --jp-content-line-height: 1.4;
  --jp-content-heading-line-height: 1.2;
}
body.jp-Notebook {
  font-size: 9pt;
  line-height: 1.4;
  padding: 0 0.15in;
}
.jp-RenderedHTMLCommon h1 { font-size: 1.5em; margin-top: 0.5em; margin-bottom: 0.25em; }
.jp-RenderedHTMLCommon h2 { font-size: 1.3em; margin-top: 0.45em; margin-bottom: 0.2em; }
.jp-RenderedHTMLCommon h3 { font-size: 1.12em; margin-top: 0.35em; margin-bottom: 0.15em; }
.jp-RenderedHTMLCommon h4 { font-size: 1.02em; margin-top: 0.3em; margin-bottom: 0.1em; }
.jp-RenderedHTMLCommon p { margin-top: 0.25em; margin-bottom: 0.25em; }
.jp-RenderedHTMLCommon ul,
.jp-RenderedHTMLCommon ol { margin-top: 0.15em; margin-bottom: 0.15em; }
.jp-RenderedHTMLCommon li { margin-top: 0.05em; margin-bottom: 0.05em; }
.jp-RenderedText pre,
.cm-editor.cm-s-jupyter .highlight pre {
  font-size: var(--jp-code-font-size);
  line-height: 1.35;
}
.jp-Cell { padding-top: 3px; padding-bottom: 3px; }
.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper { padding-top: 1px; padding-bottom: 1px; }

/* ── 2. Table formula layout ───────────────────────────────────── */
table { table-layout: auto; width: auto; max-width: 100%; border-collapse: collapse; font-size: 8.5pt; }
th, td { padding: 0.2rem 0.4rem; vertical-align: top; border: 1px solid #ddd; }
th { background: #f5f5f5; font-weight: 600; }
/* Prevent MathJax CHTML from using stacked block layout inside table cells */
td .MathJax_CHTML, th .MathJax_CHTML { white-space: nowrap !important; display: inline !important; }
td .MathJax_CHTML.mjx-full-width { width: auto !important; }
td .mjx-math, th .mjx-math { width: auto !important; }
td .mjx-mrow, th .mjx-mrow { width: auto !important; }
td .mjx-stack, th .mjx-stack { display: inline !important; vertical-align: middle !important; }
td .mjx-block, th .mjx-block { display: inline !important; }
/* Also handle MathJax 3 (mjx-container) */
td mjx-container, th mjx-container { display: inline !important; white-space: nowrap !important; }
/* Keep entire cell content on one line when it contains math */
td:has(.MathJax_CHTML), td:has(mjx-container) { white-space: nowrap; }

/* ── 3. Smart page breaks ──────────────────────────────────────── */
@page { margin: 0.6in 0.5in; }
table { break-inside: avoid; }
h1, h2, h3, h4,
.jp-RenderedHTMLCommon h1, .jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3, .jp-RenderedHTMLCommon h4 { break-after: avoid; }
p, li { orphans: 3; widows: 3; }
.jp-OutputArea-output img, .jp-OutputArea-output svg { break-inside: avoid; }

/* ── 4. Image sizing for print ─────────────────────────────────── */
.jp-OutputArea-output img { max-width: 100%; height: auto; }
</style>
"""


# ============================================================================
# EXPORT LOGIC
# ============================================================================


# ============================================================================
# NOTEBOOK PREPROCESSING
# ============================================================================


def _is_exercise_cell(source: str) -> bool:
    """Check if a markdown cell contains an exercise or solution heading."""
    for line in source.split("\n"):
        line = line.strip()
        for pattern in EXERCISE_HEADING_PATTERNS:
            if re.match(pattern, line, re.IGNORECASE):
                return True
    return False


def _should_show_input(tags: list[str], no_input: bool) -> bool:
    """Resolve per-cell input visibility from tags and the global default.

    Tags ``show-input`` / ``hide-input`` override the global *no_input* flag.
    Untagged cells follow the global default.
    """
    if "show-input" in tags:
        return True
    if "hide-input" in tags:
        return False
    return not no_input


def _filter_text_outputs(cell: dict) -> dict:
    """
    Remove text-only outputs from a code cell.

    Strips stream outputs (print/stdout/stderr) and error tracebacks.
    For display_data / execute_result, keeps only outputs that contain
    visual content (images, HTML) and drops their text/plain companions.
    """
    cell = copy.deepcopy(cell)
    filtered = []

    for output in cell.get("outputs", []):
        output_type = output.get("output_type", "")

        # Always drop print output and errors
        if output_type in ("stream", "error"):
            continue

        if output_type in ("display_data", "execute_result"):
            data = output.get("data", {})
            # Keep only if it carries visual content
            if any(mime in data for mime in VISUAL_MIME_TYPES):
                # Strip the text/plain companion (e.g. "<Figure size 640x480>")
                cleaned_data = {k: v for k, v in data.items() if k != "text/plain"}
                output = {**output, "data": cleaned_data}
                filtered.append(output)
            # else: text-only result → drop
            continue

        # Unknown output type → keep as-is
        filtered.append(output)

    cell["outputs"] = filtered
    return cell


def preprocess_notebook(
    notebook_path: Path,
    *,
    no_input: bool = True,
    no_text_output: bool = False,
    no_exercises: bool = False,
) -> Path | None:
    """
    Apply content filters to a notebook and write the result to a temp file.

    Returns the temp file Path if preprocessing was performed, or None if
    no filters were active (so the original file can be exported directly).

    Per-cell input visibility
    -------------------------
    Cells tagged ``show-input`` have their source inserted as a fenced
    markdown code block (visible even with ``--no-input``).  Cells tagged
    ``hide-input`` have their source cleared (hidden even with
    ``--with-input``).  Untagged cells follow the *no_input* global default.
    """
    with open(notebook_path, "r", encoding="utf-8-sig") as f:
        raw = f.read()

    has_input_tags = "show-input" in raw or "hide-input" in raw

    # Skip preprocessing when no filters or per-cell tags need to be applied
    if not no_text_output and not no_exercises and not has_input_tags:
        return None

    nb = json.loads(raw)
    filtered_cells = []

    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type", "")

        # Optionally skip exercise / solution markdown cells
        if no_exercises and cell_type == "markdown":
            source = "".join(cell.get("source", []))
            if _is_exercise_cell(source):
                continue

        # Optionally strip text-only outputs from code cells
        if no_text_output and cell_type == "code":
            cell = _filter_text_outputs(cell)

        # Per-cell input visibility (only when tags are present)
        if cell_type == "code" and has_input_tags:
            tags = cell.get("metadata", {}).get("tags", [])
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)

            show = _should_show_input(tags, no_input)

            if no_input and show and source.strip():
                # Global=hide, cell=show: insert markdown code block
                code = source.rstrip("\n")
                md_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": f"```python\n{code}\n```",
                }
                filtered_cells.append(md_cell)
            elif not no_input and not show:
                # Global=show, cell=hide: clear source
                cell = copy.deepcopy(cell)
                cell["source"] = ""

        filtered_cells.append(cell)

    nb["cells"] = filtered_cells

    tmp = tempfile.NamedTemporaryFile(
        suffix=".ipynb", delete=False, mode="w", encoding="utf-8",
    )
    json.dump(nb, tmp)
    tmp.close()
    return Path(tmp.name)


# ============================================================================
# POST-PROCESSING
# ============================================================================


def _fix_markdown_image_paths(md_path: Path) -> None:
    """Rewrite absolute image paths in exported markdown to be relative."""
    if not md_path.exists():
        return
    text = md_path.read_text(encoding="utf-8")
    md_dir = md_path.parent

    def _make_relative(match: re.Match) -> str:
        alt, raw_path = match.group(1), match.group(2)
        # URL-decode percent-encoded characters (e.g. %3A → :)
        from urllib.parse import unquote
        decoded = unquote(raw_path).replace("/", "\\")
        try:
            abs_path = Path(decoded)
            if abs_path.is_absolute():
                rel = abs_path.relative_to(md_dir)
                return f"![{alt}]({rel.as_posix()})"
        except (ValueError, OSError):
            pass
        return match.group(0)

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _make_relative, text)
    md_path.write_text(text, encoding="utf-8")


def _inject_table_css(html_path: Path) -> None:
    """Inject table-fix CSS into an exported HTML file (before </head>)."""
    if not html_path.exists():
        return
    html = html_path.read_text(encoding="utf-8")
    if "/* Prevent MathJax from wrapping inside table cells */" in html:
        return  # already injected
    html = html.replace("</head>", TABLE_FIX_CSS + "\n</head>", 1)
    html_path.write_text(html, encoding="utf-8")


def _html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    """Convert an HTML file to PDF via Playwright Chromium with print CSS injected."""
    html = html_path.read_text(encoding="utf-8")
    # Inject print-optimised CSS before </head>
    html = html.replace("</head>", PDF_PRINT_CSS + "\n</head>", 1)

    tmp = tempfile.NamedTemporaryFile(
        suffix=".html", delete=False, mode="w", encoding="utf-8",
    )
    tmp.write(html)
    tmp.close()

    try:
        import asyncio
        from playwright.async_api import async_playwright

        async def _render():
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.emulate_media(media="print")
                await page.goto(Path(tmp.name).as_uri(), wait_until="networkidle")
                pdf_bytes = await page.pdf(print_background=True)
                await browser.close()
            return pdf_bytes

        # On Windows, Playwright needs ProactorEventLoop
        if sys.platform == "win32":
            loop = asyncio.ProactorEventLoop()
        else:
            loop = asyncio.new_event_loop()
        try:
            pdf_bytes = loop.run_until_complete(_render())
        finally:
            loop.close()

        pdf_path.write_bytes(pdf_bytes)
    finally:
        Path(tmp.name).unlink(missing_ok=True)


# ============================================================================
# DISCOVERY
# ============================================================================


def discover_notebooks(source_dir: Path) -> list[Path]:
    """Find all .ipynb files under source_dir, sorted for deterministic output."""
    notebooks = sorted(source_dir.rglob("*.ipynb"))
    # Skip checkpoint files
    notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in str(nb)]
    return notebooks


def export_notebook(
    notebook: Path,
    source_dir: Path,
    output_dir: Path,
    fmt: str,
    no_input: bool,
    *,
    no_text_output: bool = False,
    no_exercises: bool = False,
) -> bool:
    """
    Export a single notebook to the given format.

    Optionally preprocesses the notebook to strip text outputs and/or
    exercise cells before conversion.

    Returns True on success, False on failure.
    """
    # Mirror the folder structure: Foundations/02_Funktionen/foo.ipynb → exports/html/02_Funktionen/foo.html
    relative = notebook.relative_to(source_dir)
    dest_dir = output_dir / fmt / relative.parent
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Preprocess notebook if any content filters or per-cell tags are active
    processed = preprocess_notebook(
        notebook, no_input=no_input,
        no_text_output=no_text_output, no_exercises=no_exercises,
    )
    notebook_to_export = processed if processed else notebook

    # Build command - order matters: flags first, then positional notebook path last
    # For PDF: first export to HTML, then convert with Playwright (to inject print CSS).
    export_format = "html" if fmt == "pdf" else fmt

    cmd = [sys.executable, "-m", "nbconvert", "--to", export_format]

    if no_input:
        cmd.append("--no-input")

    if fmt == "pdf":
        cmd.append("--allow-chromium-download")

    # For markdown, place extracted images in a sibling folder (relative path
    # so the markdown file references images with relative links, not absolute)
    if fmt == "markdown":
        cmd.extend(["--NbConvertApp.output_files_dir", f"{notebook.stem}_files"])

    # Explicit --output keeps the original notebook name even when exporting a temp file
    cmd.extend([
        "--output", notebook.stem,
        "--output-dir", str(dest_dir),
        str(notebook_to_export),
    ])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  FAIL  {relative} → {fmt}")
            print(f"        {result.stderr.strip()}")
            return False
        # Post-process HTML to inject table fix CSS
        if fmt == "html":
            _inject_table_css(dest_dir / f"{notebook.stem}.html")

        # Post-process markdown to fix absolute image paths
        if fmt == "markdown":
            _fix_markdown_image_paths(dest_dir / f"{notebook.stem}.md")

        # PDF: convert the intermediate HTML to PDF via Playwright, then clean up
        if fmt == "pdf":
            html_file = dest_dir / f"{notebook.stem}.html"
            pdf_file = dest_dir / f"{notebook.stem}.pdf"
            _html_to_pdf(html_file, pdf_file)
            html_file.unlink(missing_ok=True)

        print(f"  OK    {relative} → {fmt}")
        return True
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT  {relative} → {fmt}")
        return False
    except Exception as e:
        print(f"  ERROR {relative} → {fmt}: {e}")
        return False
    finally:
        # Clean up temp file from preprocessing
        if processed and processed.exists():
            processed.unlink()


# ============================================================================
# MAIN
# ============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export Jupyter notebooks to HTML/PDF with mirrored folder structure.",
    )
    parser.add_argument(
        "--source-dir",
        default=DEFAULTS["source_dir"],
        help=f"Root directory containing notebooks (default: {DEFAULTS['source_dir']})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULTS["output_dir"],
        help=f"Root output directory for exports (default: {DEFAULTS['output_dir']})",
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=VALID_FORMATS,
        default=DEFAULTS["formats"],
        help=f"Export formats (default: {' '.join(DEFAULTS['formats'])})",
    )
    parser.add_argument(
        "--no-input",
        action="store_true",
        default=DEFAULTS["no_input"],
        help="Hide code cells in output (default: True)",
    )
    parser.add_argument(
        "--with-input",
        action="store_true",
        default=False,
        help="Show code cells in output (overrides --no-input)",
    )
    parser.add_argument(
        "--no-text-output",
        action="store_true",
        default=False,
        help="Strip text/print output from code cells, keep only figures and rich HTML",
    )
    parser.add_argument(
        "--no-exercises",
        action="store_true",
        default=False,
        help="Exclude exercise and solution sections (Verständnis-Check, Lösungen)",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        default=False,
        help="CI mode: exit with non-zero code on any failure",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULTS["workers"],
        help=f"Number of parallel export workers (default: {DEFAULTS['workers']}, use 1 to disable)",
    )

    args = parser.parse_args()

    # Resolve paths relative to repo root (parent of scripts/)
    repo_root = Path(__file__).resolve().parent.parent
    source_dir = repo_root / args.source_dir
    output_dir = repo_root / args.output_dir

    no_input = args.no_input and not args.with_input

    # ── Pre-flight ─────────────────────────────────────────────────────────
    if not source_dir.is_dir():
        print(f"ERROR: Source directory not found: {source_dir}")
        return 1

    notebooks = discover_notebooks(source_dir)
    if not notebooks:
        print(f"No notebooks found under {source_dir}")
        return 0

    print(f"Export Notebooks")
    print(f"  Source:  {source_dir}")
    print(f"  Output:  {output_dir}")
    print(f"  Formats: {', '.join(args.formats)}")
    print(f"  Code:    {'hidden' if no_input else 'visible'}")
    print(f"  Text output: {'stripped' if args.no_text_output else 'included'}")
    print(f"  Exercises:   {'excluded' if args.no_exercises else 'included'}")
    print(f"  Workers: {args.workers}")
    print(f"  Found:   {len(notebooks)} notebook(s)")
    print()

    # ── Export ─────────────────────────────────────────────────────────────
    total = 0
    failed = 0

    for fmt in args.formats:
        print(f"── {fmt.upper()} ──")
        fmt_notebooks = list(notebooks)
        fmt_total = len(fmt_notebooks)

        if args.workers > 1 and fmt_total > 1:
            # Parallel export
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = {
                    pool.submit(
                        export_notebook,
                        nb, source_dir, output_dir, fmt, no_input,
                        no_text_output=args.no_text_output,
                        no_exercises=args.no_exercises,
                    ): nb
                    for nb in fmt_notebooks
                }
                for future in as_completed(futures):
                    total += 1
                    if not future.result():
                        failed += 1
        else:
            # Sequential fallback
            for nb in fmt_notebooks:
                total += 1
                success = export_notebook(
                    nb, source_dir, output_dir, fmt, no_input,
                    no_text_output=args.no_text_output,
                    no_exercises=args.no_exercises,
                )
                if not success:
                    failed += 1
        print()

    # ── Summary ────────────────────────────────────────────────────────────
    print(f"Done: {total - failed}/{total} succeeded", end="")
    if failed:
        print(f" ({failed} failed)")
    else:
        print()

    if failed and args.ci:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
