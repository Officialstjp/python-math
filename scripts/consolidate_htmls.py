"""
consolidate_htmls.py - Merge individual notebook HTML exports into a single reference file.

Reads the exported HTML files from exports/html/, extracts their body content,
and combines them into one self-contained HTML document with:
  - A sidebar table of contents grouped by chapter folder
  - Clear section dividers between notebooks
  - Embedded images (base64, already done by nbconvert)
  - All styling inlined (no external dependencies except MathJax)

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

Usage:
    python scripts/consolidate_htmls.py
    python scripts/consolidate_htmls.py --output-dir exports --title "Mathematik Referenz"
  python scripts/consolidate_htmls.py --config scripts/export_profile.toml
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from export_profile import (
    CONSOLIDATE_HTML_DEFAULTS,
    PROFILE_LOAD_EXCEPTIONS,
    bootstrap_profile_settings,
    format_profile_path,
    resolve_repo_path,
)

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULTS = CONSOLIDATE_HTML_DEFAULTS

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
    "08_Statistik_und_Wahrscheinlichkeit": "Statistik & Wahrscheinlichkeit",
    "99_Glossare": "Glossare",
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
        if len(parts) == 1:
            # Root-level HTML files are usually previous consolidated references.
            continue
        if len(parts) > 2:
            # e.g. en/Analysis/file.html → chapter key = "en/Analysis"
            chapter_key = "/".join(parts[:-1])
        else:
            chapter_key = parts[0]

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


def exclude_chapters(
    chapters: dict[str, list[Path]],
    excluded: list[str],
) -> dict[str, list[Path]]:
    """Remove configured chapter groups from the consolidation input."""
    if not excluded:
        return chapters

    excluded_set = set(excluded)
    return {
        chapter_key: files
        for chapter_key, files in chapters.items()
        if chapter_key not in excluded_set
    }


def build_layout_css(layout: dict[str, str]) -> str:
    """Build the consolidated HTML layout CSS from profile settings."""
    return f"""
:root {{
  --sidebar-width: {layout['sidebar_width']};
  --bg-sidebar: {layout['sidebar_background']};
  --bg-main: #ffffff;
  --text-sidebar: {layout['sidebar_text']};
  --accent: {layout['accent']};
  --divider: {layout['divider']};
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: {layout['body_font_family']};
  display: flex;
  min-height: 100vh;
  background: var(--bg-main);
}}

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
  color: {layout['title_color']}; text-align: center;
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

main.content {{
  margin-left: var(--sidebar-width);
  flex: 1; padding: {layout['content_padding']};
  max-width: {layout['content_max_width']};
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

@media (max-width: {layout['hide_sidebar_below']}) {{
  nav.sidebar {{ display: none; }}
  main.content {{ margin-left: 0; padding: 1rem; }}
}}

.notebook-content .jp-Cell {{ margin-bottom: 0.5rem; }}
.notebook-content img {{
  max-width: {layout['notebook_image_max_width']};
  max-height: {layout['notebook_image_max_height']};
  height: auto;
  object-fit: contain;
}}

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

@media print {{
  nav.sidebar {{ display: none; }}
  main.content {{ margin-left: 0; max-width: 100%; }}
  .notebook-section {{ page-break-inside: avoid; }}
  .section-divider {{ page-break-after: {layout['section_break_after']}; border: none; }}
}}
"""


def build_consolidated_html(
    chapters: dict[str, list[Path]],
    title: str,
  layout: dict[str, str],
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
    layout_css = build_layout_css(layout)

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
<style>{layout_css}</style>
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
  repo_root = Path(__file__).resolve().parent.parent

  try:
    profile = bootstrap_profile_settings(
      repo_root,
      ("consolidate_htmls", "consolidate_html"),
      DEFAULTS,
    )
  except PROFILE_LOAD_EXCEPTIONS as exc:
    print(f"ERROR: {exc}")
    return 1

  settings = profile.settings
  profile_path = profile.profile_path

  parser = argparse.ArgumentParser(
    description="Consolidate exported notebook HTMLs into a single reference file.",
    parents=[profile.config_parser],
  )
  parser.add_argument(
    "--html-dir",
    default=settings["html_dir"],
    help=f"Directory with exported HTMLs (default: {settings['html_dir']})",
  )
  parser.add_argument(
    "--output-dir",
    default=settings["output_dir"],
    help=f"Where to write the consolidated file (default: {settings['output_dir']})",
  )
  parser.add_argument(
    "--output-name",
    default=settings["output_name"],
    help=f"Output filename (default: {settings['output_name']})",
  )
  parser.add_argument(
    "--title",
    default=settings["title"],
    help=f"Document title (default: {settings['title']})",
  )
  parser.add_argument(
    "--exclude-chapters",
    nargs="+",
    default=settings["filters"]["exclude_chapters"],
    help="Chapter folder keys to omit from the consolidated HTML",
  )

  args = parser.parse_args()
  html_dir = resolve_repo_path(repo_root, args.html_dir)
  output_dir = resolve_repo_path(repo_root, args.output_dir)
  output_file = output_dir / args.output_name

  # ── Pre-flight ─────────────────────────────────────────────────────────
  if not html_dir.is_dir():
    print(f"ERROR: HTML export directory not found: {html_dir}")
    print("Run export_notebooks.py first to generate HTML files.")
    return 1

  chapters = exclude_chapters(discover_html_files(html_dir), args.exclude_chapters)
  total = sum(len(files) for files in chapters.values())

  if total == 0:
    print(f"No HTML files found under {html_dir}")
    return 1

  print("Consolidate Notebooks")
  if profile_path is not None:
    print(f"  Profile: {format_profile_path(repo_root, profile_path)}")
  print(f"  Source: {html_dir}")
  print(f"  Output: {output_file}")
  if args.exclude_chapters:
    print(f"  Excluded chapters: {', '.join(args.exclude_chapters)}")
  print(f"  Chapters: {len(chapters)}")
  print(f"  Notebooks: {total}")
  print()

  # ── Build ──────────────────────────────────────────────────────────────
  result = build_consolidated_html(chapters, args.title, settings["layout"])

  output_dir.mkdir(parents=True, exist_ok=True)
  output_file.write_text(result, encoding="utf-8")

  size_mb = output_file.stat().st_size / (1024 * 1024)
  print(f"Done: {output_file.name} ({size_mb:.1f} MB)")

  return 0


if __name__ == "__main__":
    sys.exit(main())
