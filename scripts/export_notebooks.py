"""
export_notebooks.py - Export Jupyter notebooks to HTML, Markdown, and/or PDF.

Walks source directories for .ipynb files, converts them via nbconvert,
and writes the output into a mirrored folder structure under an export directory.
Exports run in parallel by default for faster throughput.

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

> Currently only HTML export works, havent figured PDF export out yet, not relevant at the moment.

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
    no_text_output: bool = False,
    no_exercises: bool = False,
) -> Path | None:
    """
    Apply content filters to a notebook and write the result to a temp file.

    Returns the temp file Path if preprocessing was performed, or None if
    no filters were active (so the original file can be exported directly).
    """
    if not no_text_output and not no_exercises:
        return None

    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

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

    # Preprocess notebook if any content filters are active
    processed = preprocess_notebook(
        notebook, no_text_output=no_text_output, no_exercises=no_exercises,
    )
    notebook_to_export = processed if processed else notebook

    # Build command - order matters: flags first, then positional notebook path last
    export_format = "webpdf" if fmt == "pdf" else fmt

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
