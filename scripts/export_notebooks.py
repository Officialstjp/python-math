"""
export_notebooks.py — Export Jupyter notebooks to HTML and/or PDF.

Walks source directories for .ipynb files, converts them via nbconvert,
and writes the output into a mirrored folder structure under an export directory.

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

> Currently only HTML export works, havent figured PDF export out yet, not relevant at the moment.

Usage:
    # Export HTML only (default)
    python scripts/export_notebooks.py

    # Export both HTML and PDF
    python scripts/export_notebooks.py --formats html pdf

    # Custom source and output directories
    python scripts/export_notebooks.py --source-dir Foundations --output-dir exports

    # Show code cells in output
    python scripts/export_notebooks.py --with-input

    # CI mode: non-interactive, fail on first error
    python scripts/export_notebooks.py --ci
"""

from __future__ import annotations

import argparse
import subprocess
import sys
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
}

VALID_FORMATS = ("html", "pdf")


# ============================================================================
# EXPORT LOGIC
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
) -> bool:
    """
    Export a single notebook to the given format.

    Returns True on success, False on failure.
    """
    # Mirror the folder structure: Foundations/02_Funktionen/foo.ipynb → exports/html/02_Funktionen/foo.html
    relative = notebook.relative_to(source_dir)
    dest_dir = output_dir / fmt / relative.parent
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Build command — order matters: flags first, then positional notebook path last
    export_format = "webpdf" if fmt == "pdf" else fmt

    cmd = [sys.executable, "-m", "nbconvert", "--to", export_format]

    if no_input:
        cmd.append("--no-input")

    if fmt == "pdf":
        cmd.append("--allow-chromium-download")

    cmd.extend(["--output-dir", str(dest_dir), str(notebook)])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"  FAIL  {relative} → {fmt}")
            print(f"        {result.stderr.strip()}")
            return False
        print(f"  OK    {relative} → {fmt}")
        return True
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT  {relative} → {fmt}")
        return False
    except Exception as e:
        print(f"  ERROR {relative} → {fmt}: {e}")
        return False


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
        "--ci",
        action="store_true",
        default=False,
        help="CI mode: exit with non-zero code on any failure",
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
    print(f"  Found:   {len(notebooks)} notebook(s)")
    print()

    # ── Export ─────────────────────────────────────────────────────────────
    total = 0
    failed = 0

    for fmt in args.formats:
        print(f"── {fmt.upper()} ──")
        for nb in notebooks:
            total += 1
            success = export_notebook(nb, source_dir, output_dir, fmt, no_input)
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
