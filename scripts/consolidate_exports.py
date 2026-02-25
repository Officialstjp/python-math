"""
consolidate_exports.py - Merge individual notebook HTML exports into a single reference file.

Reads the exported HTML files from exports/html/, extracts their body content,
and combines them into one self-contained HTML document with:
  - A sidebar table of contents grouped by chapter folder
  - Clear section dividers between notebooks
  - Embedded images (base64, already done by nbconvert)
  - All styling inlined (no external dependencies except MathJax)

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

Usage:
    python scripts/consolidate_exports.py
    python scripts/consolidate_exports.py --output-dir exports --title "Mathematik Referenz"
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULTS = {
    "html_dir": "exports_clean/html",
    "output_dir": "exports_clean",
    "output_name": "reference.html",
    "title": "Mathematik - Gesamtreferenz",
}

# Human-readable chapter names (folder name → display name)
CHAPTER_NAMES: dict[str, str] = {
    "00_Grundlagen": "Grundlagen",
    "01_Algebra": "Algebra",
    "02_Funktionen": "Funktionen",
    "03_Geometrie": "Geometrie",
    "04_Trigonometrie": "Trigonometrie",
    "05_Vektoren_Matrizen": "Vektoren & Matrizen",
    "06_Folgen_Reihen": "Folgen & Reihen",
    "07_Analysis": "Analysis",
    "08_Stochastik": "Stochastik",
    "en": "English",
}


# ============================================================================
# HTML BODY EXTRACTION
# ============================================================================


class BodyExtractor(HTMLParser):
    """Extract content between <body ...> and </body> from nbconvert HTML."""

    def __init__(self) -> None:
        super().__init__()
        self._inside_body = False
        self._depth = 0
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "body":
            self._inside_body = True
            self._depth = 0
            return  # skip the <body> tag itself
        if self._inside_body:
            self._depth += 1
            attr_str = "".join(
                f' {k}="{v}"' if v is not None else f" {k}" for k, v in attrs
            )
            self._parts.append(f"<{tag}{attr_str}>")

    def handle_endtag(self, tag: str) -> None:
        if tag == "body":
            self._inside_body = False
            return
        if self._inside_body:
            self._depth -= 1
            self._parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self._inside_body:
            self._parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self._inside_body:
            self._parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self._inside_body:
            self._parts.append(f"&#{name};")

    def get_content(self) -> str:
        return "".join(self._parts)


class StyleExtractor(HTMLParser):
    """Extract <style> blocks from the <head> of nbconvert HTML."""

    def __init__(self) -> None:
        super().__init__()
        self._inside_style = False
        self._styles: list[str] = []
        self._current: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "style":
            self._inside_style = True
            self._current = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "style" and self._inside_style:
            self._inside_style = False
            self._styles.append("".join(self._current))

    def handle_data(self, data: str) -> None:
        if self._inside_style:
            self._current.append(data)

    def get_styles(self) -> str:
        return "\n".join(self._styles)


def extract_body(html: str) -> str:
    """Extract the inner content of <body> from a full HTML document."""
    parser = BodyExtractor()
    parser.feed(html)
    return parser.get_content()


def extract_styles(html: str) -> str:
    """Extract all <style> blocks from a full HTML document."""
    parser = StyleExtractor()
    parser.feed(html)
    return parser.get_styles()


def notebook_display_name(path: Path) -> str:
    """Turn '01_Zahlenmengen_Rechenarten.html' into 'Zahlenmengen Rechenarten'."""
    name = path.stem
    # Strip leading number prefix like '01_', '02_'
    name = re.sub(r"^\d+_", "", name)
    # Replace underscores with spaces
    return name.replace("_", " ")


# ============================================================================
# CONSOLIDATION
# ============================================================================


def discover_html_files(html_dir: Path) -> dict[str, list[Path]]:
    """
    Group HTML files by their parent chapter folder.
    Returns {chapter_folder: [sorted list of html files]}.
    """
    chapters: dict[str, list[Path]] = {}
    for html_file in sorted(html_dir.rglob("*.html")):
        # Relative path from html_dir, e.g. "02_Funktionen/01_Funktionsbegriff.html"
        rel = html_file.relative_to(html_dir)
        # Chapter = first path component (or nested for "en/Analysis")
        parts = rel.parts
        if len(parts) > 2:
            # e.g. en/Analysis/file.html → chapter key = "en/Analysis"
            chapter_key = "/".join(parts[:-1])
        elif len(parts) == 2:
            chapter_key = parts[0]
        else:
            chapter_key = "_root"

        chapters.setdefault(chapter_key, []).append(html_file)

    return chapters


def make_anchor(chapter: str, file: Path) -> str:
    """Generate a unique HTML anchor id for a notebook section."""
    slug = f"{chapter}--{file.stem}".replace("/", "-").replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9_-]", "", slug)


def chapter_display_name(chapter_key: str) -> str:
    """Map folder name to a human-readable chapter name."""
    # Handle nested paths like "en/Analysis"
    if "/" in chapter_key:
        parts = chapter_key.split("/")
        return " › ".join(CHAPTER_NAMES.get(p, p.replace("_", " ")) for p in parts)
    return CHAPTER_NAMES.get(chapter_key, chapter_key.replace("_", " "))


def build_consolidated_html(
    chapters: dict[str, list[Path]],
    html_dir: Path,
    title: str,
) -> str:
    """Build the final single-file HTML document."""

    # Collect styles from the first HTML file (they're all identical from nbconvert)
    first_file = next(iter(next(iter(chapters.values()))))
    first_html = first_file.read_text(encoding="utf-8")
    nb_styles = extract_styles(first_html)

    # ── Build TOC and sections ─────────────────────────────────────────────
    toc_items: list[str] = []
    sections: list[str] = []

    for chapter_key, files in chapters.items():
        ch_display = chapter_display_name(chapter_key)
        toc_items.append(f'<li class="toc-chapter">{ch_display}</li>')

        for file in files:
            anchor = make_anchor(chapter_key, file)
            nb_display = notebook_display_name(file)

            toc_items.append(
                f'<li class="toc-notebook"><a href="#{anchor}">{nb_display}</a></li>'
            )

            # Extract body content
            html_content = file.read_text(encoding="utf-8")
            body = extract_body(html_content)

            sections.append(f"""
<section id="{anchor}" class="notebook-section">
  <div class="section-header">
    <span class="section-chapter">{ch_display}</span>
    <h2 class="section-title">{nb_display}</h2>
  </div>
  <div class="notebook-content jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
    {body}
  </div>
</section>
<hr class="section-divider"/>
""")

    toc_html = "\n".join(toc_items)
    sections_html = "\n".join(sections)

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>

<!-- MathJax for LaTeX rendering -->
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$'], ['\\\\(','\\\\)']], displayMath: [['$$','$$'], ['\\\\[','\\\\]']] }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<!-- nbconvert styles (from exported notebooks) -->
<style>{nb_styles}</style>

<!-- Consolidated layout styles -->
<style>
:root {{
  --sidebar-width: 280px;
  --bg-sidebar: #1e1e2e;
  --bg-main: #ffffff;
  --text-sidebar: #cdd6f4;
  --accent: #89b4fa;
  --divider: #e0e0e0;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  display: flex;
  min-height: 100vh;
  background: var(--bg-main);
}}

/* ── Sidebar / TOC ─────────────────────────────────────────────────── */
nav.sidebar {{
  position: fixed; top: 0; left: 0;
  width: var(--sidebar-width); height: 100vh;
  background: var(--bg-sidebar); color: var(--text-sidebar);
  overflow-y: auto; padding: 1.5rem 1rem;
  z-index: 100;
  border-right: 1px solid #313244;
}}

nav.sidebar h1 {{
  font-size: 1.1rem; margin-bottom: 1.5rem;
  color: #cba6f7; text-align: center;
  padding-bottom: 0.8rem; border-bottom: 1px solid #45475a;
}}

nav.sidebar ul {{ list-style: none; }}

nav.sidebar .toc-chapter {{
  font-weight: 700; font-size: 0.85rem;
  color: var(--accent); margin-top: 1rem;
  text-transform: uppercase; letter-spacing: 0.05em;
}}

nav.sidebar .toc-notebook {{
  margin: 0.2rem 0 0.2rem 0.8rem;
}}

nav.sidebar .toc-notebook a {{
  color: var(--text-sidebar); text-decoration: none;
  font-size: 0.82rem; display: block;
  padding: 0.2rem 0.4rem; border-radius: 4px;
  transition: background 0.15s;
}}

nav.sidebar .toc-notebook a:hover {{
  background: #313244; color: #f5e0dc;
}}

/* ── Main content ──────────────────────────────────────────────────── */
main.content {{
  margin-left: var(--sidebar-width);
  flex: 1; padding: 2rem 3rem;
  max-width: 1000px;
}}

.notebook-section {{
  margin-bottom: 1rem;
}}

.section-header {{
  margin-bottom: 1rem;
  padding: 1.2rem 0 0.8rem 0;
}}

.section-chapter {{
  font-size: 0.8rem; text-transform: uppercase;
  color: #888; letter-spacing: 0.05em;
}}

.section-title {{
  font-size: 1.6rem; color: #333;
  margin-top: 0.2rem;
}}

.section-divider {{
  border: none;
  border-top: 2px solid var(--divider);
  margin: 3rem 0;
}}

/* ── Responsive: collapse sidebar on small screens ─────────────────── */
@media (max-width: 900px) {{
  nav.sidebar {{ display: none; }}
  main.content {{ margin-left: 0; padding: 1rem; }}
}}

/* ── Notebook content overrides ────────────────────────────────────── */
.notebook-content .jp-Cell {{ margin-bottom: 0.5rem; }}
.notebook-content img {{ max-width: 100%; height: auto; }}

/* ── Table fixes (prevent MathJax wrapping in narrow columns) ──────── */
.notebook-content table {{
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}}
.notebook-content th,
.notebook-content td {{
  padding: 0.5rem 0.75rem;
  vertical-align: top;
  border: 1px solid #ddd;
}}
.notebook-content th {{
  background: #f5f5f5;
  font-weight: 600;
}}
.notebook-content td .MathJax,
.notebook-content th .MathJax {{
  white-space: nowrap;
  display: inline !important;
}}
.notebook-content td mjx-container,
.notebook-content th mjx-container {{
  white-space: nowrap !important;
  display: inline !important;
}}

/* ── Print styles ──────────────────────────────────────────────────── */
@media print {{
  nav.sidebar {{ display: none; }}
  main.content {{ margin-left: 0; max-width: 100%; }}
  .notebook-section {{ page-break-inside: avoid; }}
  .section-divider {{ page-break-after: always; border: none; }}
}}
</style>
</head>

<body>

<nav class="sidebar">
  <h1>{title}</h1>
  <ul>
    {toc_html}
  </ul>
</nav>

<main class="content">
  {sections_html}
</main>

</body>
</html>
"""


# ============================================================================
# MAIN
# ============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Consolidate exported notebook HTMLs into a single reference file.",
    )
    parser.add_argument(
        "--html-dir",
        default=DEFAULTS["html_dir"],
        help=f"Directory with exported HTMLs (default: {DEFAULTS['html_dir']})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULTS["output_dir"],
        help=f"Where to write the consolidated file (default: {DEFAULTS['output_dir']})",
    )
    parser.add_argument(
        "--output-name",
        default=DEFAULTS["output_name"],
        help=f"Output filename (default: {DEFAULTS['output_name']})",
    )
    parser.add_argument(
        "--title",
        default=DEFAULTS["title"],
        help=f"Document title (default: {DEFAULTS['title']})",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    html_dir = repo_root / args.html_dir
    output_dir = repo_root / args.output_dir
    output_file = output_dir / args.output_name

    # ── Pre-flight ─────────────────────────────────────────────────────────
    if not html_dir.is_dir():
        print(f"ERROR: HTML export directory not found: {html_dir}")
        print("Run export_notebooks.py first to generate HTML files.")
        return 1

    chapters = discover_html_files(html_dir)
    total = sum(len(files) for files in chapters.values())

    if total == 0:
        print(f"No HTML files found under {html_dir}")
        return 1

    print(f"Consolidate Notebooks")
    print(f"  Source: {html_dir}")
    print(f"  Output: {output_file}")
    print(f"  Chapters: {len(chapters)}")
    print(f"  Notebooks: {total}")
    print()

    # ── Build ──────────────────────────────────────────────────────────────
    result = build_consolidated_html(chapters, html_dir, args.title)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")

    size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"Done: {output_file.name} ({size_mb:.1f} MB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
