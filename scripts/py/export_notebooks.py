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

    # Omit glossary sections in both HTML and PDF
    python scripts/export_notebooks.py --formats html pdf --exclude-glossary-formats html pdf

    # Custom source and output directories
    python scripts/export_notebooks.py --source-dir Foundations --output-dir exports

    # Load persistent defaults from a TOML profile
    python scripts/export_notebooks.py --config scripts/export_profile.toml

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
import posixpath
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote

try:
    from scripts.py.export_profile import (
        NOTEBOOK_EXPORT_DEFAULTS,
        PROFILE_LOAD_EXCEPTIONS,
        bootstrap_profile_settings,
        format_profile_path,
        resolve_repo_path,
    )
except ModuleNotFoundError:
    from export_profile import (
        NOTEBOOK_EXPORT_DEFAULTS,
        PROFILE_LOAD_EXCEPTIONS,
        bootstrap_profile_settings,
        format_profile_path,
        resolve_repo_path,
    )

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULTS = NOTEBOOK_EXPORT_DEFAULTS

VALID_FORMATS = ("html", "markdown", "pdf")

# Heading patterns that mark exercise / solution cells to exclude.
# Matched line-by-line against markdown cell source (case-insensitive).
EXERCISE_HEADING_PATTERNS: list[str] = [
    r"^#+\s*Verständnis",      # "## Verständnis-Check"
    r"^#+\s*Lösungen?\b",      # "### Lösungen"
]

# Heading patterns that mark glossary sections to exclude from compact PDFs.
GLOSSARY_HEADING_PATTERNS: list[str] = [
    r"^#+\s*Glossar\b",
    r"^#+\s*Glossary\b",
]

# Mime types considered visual (kept when stripping text output)
VISUAL_MIME_TYPES = {
    "image/png", "image/jpeg", "image/svg+xml", "image/gif",
    "text/html",  # Rendered outputs like DataFrames, widgets
}

MATPLOTLIB_ANIMATION_MARKERS = (
    "/* Define the Animation class */",
    "function Animation(frames",
    "Animation.prototype",
)

ANIMATION_SOURCE_MARKERS = (
    ".to_jshtml(",
    ".to_html5_video(",
)

ANIMATION_EXPORT_PLACEHOLDER = (
    "<div style=\"padding:0.75rem 1rem; border:1px solid #d8dee9; "
    "background:#f8fafc; color:#334155; border-radius:6px; font-style:italic;\">"
    "(Interaktive Matplotlib-Animation im statischen Export ausgelassen) "
    "</div>"
)

HTML_EXPORT_CSS_MARKER = "/* HTML export layout overrides */"

DETAILS_OPEN_TAG_PATTERN = re.compile(
    r"<details(\\s[^>]*)?>",
    re.IGNORECASE,
)


# ============================================================================
# SIDE-BY-SIDE ZUSAMMENFASSUNG / GLOSSAR TRANSFORM
# ============================================================================

# ============================================================================
# HEADING SECTION WRAPPER (keep content under a heading together)
# ============================================================================

# The heading-content cohesion is handled via CSS print rules:
#   - break-after: avoid on h1–h6 (don't leave heading at bottom of page)
#   - break-before: avoid on p, ul, ol (don't leave content orphaned at top)
# HTML-wrapping approaches caused cascading page breaks.

_SBS_CLASS_SUMMARY = "side-by-side-summary"
_SBS_CLASS_GLOSSARY = "side-by-side-glossary"
_SBS_SECTION_CLASS = "side-by-side-section"
_SBS_COLUMN_CLASS = "side-by-side-column"
_SBS_DIVIDER_CLASS = "side-by-side-divider"

# Headings that nbconvert renders with predictable id attributes.
_SBS_ZUSAMMENFASSUNG_ID = "Zusammenfassung"
_SBS_GLOSSAR_ID = "Glossar"


def _build_side_by_side_css(config: dict, media: str = "screen") -> str:
    """Build CSS rules for the side-by-side Zusammenfassung / Glossar layout.

    ``media`` should be ``"screen"`` for HTML exports and ``"print"`` for PDF.
    """
    gap = config.get("gap", "2rem")
    min_width = config.get("min_column_width", "280px")
    equal = config.get("equal_columns", True)
    show_divider = config.get("show_divider", False)

    column_flex = "1 1 0" if equal else "1 1 auto"
    table_font_size = config.get("table_font_size", "9pt")

    rules = [
        f""".{_SBS_SECTION_CLASS} {{
    display: flex !important;
    gap: {gap};
    align-items: flex-start;
    margin-top: 0.4em;
    margin-bottom: 0.4em;
}}""",
        f""".{_SBS_COLUMN_CLASS} {{
    flex: {column_flex} !important;
    min-width: 0 !important;
    overflow: hidden;
}}""",
        f""".{_SBS_COLUMN_CLASS} h2 {{
    margin-top: 0;
}}""",
        f""".{_SBS_COLUMN_CLASS} table {{
    width: 100% !important;
    max-width: 100% !important;
    table-layout: fixed !important;
    margin-top: 0.5em;
    font-size: {table_font_size} !important;
}}""",
        f""".{_SBS_COLUMN_CLASS} td, .{_SBS_COLUMN_CLASS} th {{
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    hyphens: auto;
}}""",
        # Relax MathJax nowrap inside side-by-side columns
        # so formulas can wrap instead of overflowing the column.
        f""".{_SBS_COLUMN_CLASS} td .MathJax_CHTML,""",
        f""".{_SBS_COLUMN_CLASS} th .MathJax_CHTML {{""",
        "    white-space: normal !important;",
        "    display: inline !important;",
        "}",
        f""".{_SBS_COLUMN_CLASS} td mjx-container,""",
        f""".{_SBS_COLUMN_CLASS} th mjx-container {{""",
        "    white-space: normal !important;",
        "    display: inline !important;",
        "}",
        f""".{_SBS_COLUMN_CLASS} td:has(.MathJax_CHTML),""",
        f""".{_SBS_COLUMN_CLASS} td:has(mjx-container) {{""",
        "    white-space: normal;",
        "}",
    ]

    if show_divider:
        rules.append(f""".{_SBS_DIVIDER_CLASS} {{
    width: 1px;
    background: #d8dee9;
    align-self: stretch;
    margin: 0 {gap};
}}""")

    if media == "screen":
        rules.append("""@media (max-width: 650px) {
    .side-by-side-section {
        flex-direction: column;
    }
    .side-by-side-divider {
        width: 100%;
        height: 1px;
        margin: 0.5rem 0;
    }
}""")

    return "\n".join(rules)


def _transform_side_by_side_html(html: str) -> str:
    """Post-process nbconvert HTML: wrap consecutive Zusammenfassung + Glossar
    sections inside a single rendered-markdown cell into a flex container.

    The transformation is skipped for cells that only contain one of the two
    sections, or where they appear in separate cells.
    """

    def _wrap_cell(cell_match: re.Match) -> str:
        """Try to wrap Zusammenfassung + Glossar within one markdown cell."""
        content = cell_match.group(0)
        z_id = f'id="{_SBS_ZUSAMMENFASSUNG_ID}"'
        g_id = f'id="{_SBS_GLOSSAR_ID}"'

        z_match = re.search(
            rf'<h2\s+[^>]*\b{z_id}[^>]*>.*?</h2>',
            content,
            re.DOTALL,
        )
        g_match = re.search(
            rf'<h2\s+[^>]*\b{g_id}[^>]*>.*?</h2>',
            content,
            re.DOTALL,
        )
        if not z_match or not g_match:
            return content

        # Find the <hr/> separator located between the two headings.
        between_start = z_match.end()
        between_end = g_match.start()
        between = content[between_start:between_end]
        hr_match = re.search(r"<hr/>", between)
        if not hr_match:
            return content

        hr_pos = between_start + hr_match.start()

        before = content[: z_match.start()]
        summary_block = content[z_match.start() : hr_pos]
        glossary_block = content[g_match.start() :]

        divider_html = ""
        if _SBS_DIVIDER_CLASS in content:
            divider_html = f'<div class="{_SBS_DIVIDER_CLASS}"></div>'

        return (
            f"{before}"
            f'<div class="{_SBS_SECTION_CLASS}">'
            f'<div class="{_SBS_COLUMN_CLASS} {_SBS_CLASS_SUMMARY}">'
            f"{summary_block}"
            f"</div>"
            f"{divider_html}"
            f'<div class="{_SBS_COLUMN_CLASS} {_SBS_CLASS_GLOSSARY}">'
            f"{glossary_block}"
            f"</div>"
            f"</div>"
        )

    return re.sub(
        r"<div[^>]*class=\"[^\"]*\bjp-RenderedMarkdown\b[^\"]*\"[^>]*>.*?</div>",
        _wrap_cell,
        html,
        flags=re.DOTALL,
    )


def _css_rule(name: str, value: str | None, indent: str = "    ") -> str:
    """Build a single CSS property rule when a value is configured."""
    if value is None:
        return ""
    return f"{indent}{name}: {value};"


def _join_rules(*rules: str) -> str:
    """Join non-empty CSS rules into a block body."""
    return "\n".join(rule for rule in rules if rule)


def _build_html_export_css(
    style: dict[str, str | None],
    side_by_side_config: dict | None = None,
) -> str:
    """Build CSS injected into exported HTML files."""
    sections = [
        HTML_EXPORT_CSS_MARKER,
        "/* Prevent MathJax from wrapping inside table cells */",
        ".jp-RenderedHTMLCommon table { width: 100%; border-collapse: collapse; table-layout: auto; }",
        ".jp-RenderedHTMLCommon th, .jp-RenderedHTMLCommon td { padding: 0.5rem 0.75rem; vertical-align: top; border: 1px solid #ddd; }",
        ".jp-RenderedHTMLCommon th { background: #f5f5f5; font-weight: 600; }",
        ".jp-RenderedHTMLCommon td .MathJax, .jp-RenderedHTMLCommon th .MathJax { white-space: nowrap; display: inline !important; }",
        ".jp-RenderedHTMLCommon td mjx-container, .jp-RenderedHTMLCommon th mjx-container { white-space: nowrap !important; display: inline !important; }",
        "/* Hide empty code-cell input areas (produced by per-cell hide-input tag) */",
        "div.input:has(.highlight pre > span:only-child:empty) { display: none; }",
        "div.jp-Cell-inputWrapper:has(pre > span:only-child:empty) { display: none; }",
    ]

    body_rules = _join_rules(
        _css_rule("padding", style.get("body_padding")),
        _css_rule("font-size", style.get("content_font_size")),
        _css_rule("line-height", style.get("content_line_height")),
    )
    if body_rules:
        sections.append(f"body.jp-Notebook {{\n{body_rules}\n}}")

    image_rules = _join_rules(
        _css_rule("max-width", style.get("image_max_width")),
        _css_rule("max-height", style.get("image_max_height")),
        _css_rule("margin", style.get("image_margin")),
    )
    if image_rules:
        sections.append(".jp-OutputArea-output { text-align: center; }")
        sections.append(
            "\n".join(
                [
                    ".jp-OutputArea-output img,",
                    ".jp-OutputArea-output svg {",
                    "    display: block;",
                    "    width: auto;",
                    "    height: auto;",
                    "    object-fit: contain;",
                    image_rules,
                    "}",
                ]
            )
        )

    # Side-by-side Zusammenfassung / Glossar CSS (screen mode)
    if side_by_side_config and side_by_side_config.get("enabled", True):
        sections.append(
            "/* Side-by-side Zusammenfassung / Glossar */\n"
            + _build_side_by_side_css(side_by_side_config, media="screen")
        )

    return "<style>\n" + "\n".join(sections) + "\n</style>"


def _build_pdf_print_css(
    style: dict[str, str],
    side_by_side_config: dict | None = None,
) -> str:
    """Build the print CSS injected before Playwright renders a PDF."""
    side_by_side_css = ""
    if side_by_side_config and side_by_side_config.get("enabled", True):
        side_by_side_css = (
            "/* ── 5. Side-by-side Zusammenfassung / Glossar ──────────────── */\n"
            + _build_side_by_side_css(side_by_side_config, media="print")
            + "\n"
        )

    return f"""
<style type="text/css">
/* ── 1. Compact fonts ──────────────────────────────────────────── */
:root {{
    --jp-content-font-size1: {style['content_font_size']};
    --jp-content-font-size0: {style['content_font_size_small']};
    --jp-code-font-size: {style['code_font_size']};
    --jp-content-line-height: {style['content_line_height']};
    --jp-content-heading-line-height: {style['heading_line_height']};
}}
body.jp-Notebook {{
    font-size: {style['content_font_size']};
    line-height: {style['content_line_height']};
    padding: {style['body_padding']};
}}
.jp-RenderedHTMLCommon h1 {{ font-size: 1.4em; margin-top: 0.45em; margin-bottom: 0.22em; }}
.jp-RenderedHTMLCommon h2 {{ font-size: 1.22em; margin-top: 0.38em; margin-bottom: 0.18em; }}
.jp-RenderedHTMLCommon h3 {{ font-size: 1.08em; margin-top: 0.3em; margin-bottom: 0.12em; }}
.jp-RenderedHTMLCommon h4 {{ font-size: 1em; margin-top: 0.25em; margin-bottom: 0.08em; }}
.jp-RenderedHTMLCommon p {{ margin-top: 0.25em; margin-bottom: 0.25em; }}
.jp-RenderedHTMLCommon ul,
.jp-RenderedHTMLCommon ol {{ margin-top: 0.15em; margin-bottom: 0.15em; }}
.jp-RenderedHTMLCommon li {{ margin-top: 0.05em; margin-bottom: 0.05em; }}
.jp-RenderedText pre,
.cm-editor.cm-s-jupyter .highlight pre {{
  font-size: var(--jp-code-font-size);
  line-height: 1.35;
}}
.jp-Cell {{ padding-top: 3px; padding-bottom: 3px; }}
.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {{ padding-top: 1px; padding-bottom: 1px; }}

/* ── 2. Table formula layout ───────────────────────────────────── */
.jp-RenderedHTMLCommon table {{
    table-layout: fixed;
    width: auto;
    max-width: 100%;
    border-collapse: collapse;
    font-size: {style['table_font_size']} !important;
    margin-left: 0;
    margin-right: 0;
    margin-top: 0.4em;
}}
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon td {{
    padding: {style['table_cell_padding']} !important;
    vertical-align: top;
    border: 1px solid #ddd;
    word-wrap: break-word;
    overflow-wrap: break-word;
}}
.jp-RenderedHTMLCommon th {{ background: #f5f5f5; font-weight: 600; }}
.jp-RenderedHTMLCommon td .MathJax_CHTML, .jp-RenderedHTMLCommon th .MathJax_CHTML {{ white-space: nowrap !important; display: inline !important; }}
.jp-RenderedHTMLCommon td .MathJax_CHTML.mjx-full-width {{ width: auto !important; }}
.jp-RenderedHTMLCommon td .mjx-math, .jp-RenderedHTMLCommon th .mjx-math {{ width: auto !important; }}
.jp-RenderedHTMLCommon td .mjx-mrow, .jp-RenderedHTMLCommon th .mjx-mrow {{ width: auto !important; }}
.jp-RenderedHTMLCommon td .mjx-stack, .jp-RenderedHTMLCommon th .mjx-stack {{ display: inline !important; vertical-align: middle !important; }}
.jp-RenderedHTMLCommon td .mjx-block, .jp-RenderedHTMLCommon th .mjx-block {{ display: inline !important; }}
.jp-RenderedHTMLCommon td mjx-container, .jp-RenderedHTMLCommon th mjx-container {{ display: inline !important; white-space: nowrap !important; }}
.jp-RenderedHTMLCommon td:has(.MathJax_CHTML), .jp-RenderedHTMLCommon td:has(mjx-container) {{ white-space: nowrap; }}

/* ── 3. Smart page breaks ─────────────────────────────────────── */
@page {{ margin: {style['page_margin']}; }}
table {{ break-inside: avoid; break-before: avoid; }}
hr {{ break-after: avoid; break-before: avoid; }}
h1, h2, h3, h4, h5, h6,
.jp-RenderedHTMLCommon h1, .jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3, .jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5, .jp-RenderedHTMLCommon h6 {{ break-after: avoid; }}
h1 + p, h2 + p, h3 + p, h4 + p, h5 + p, h6 + p,
h1 + ul, h2 + ul, h3 + ul, h4 + ul, h5 + ul, h6 + ul,
h1 + ol, h2 + ol, h3 + ol, h4 + ol, h5 + ol, h6 + ol,
h1 + table, h2 + table, h3 + table, h4 + table, h5 + table, h6 + table {{ break-before: avoid; }}
p, li {{ orphans: 3; widows: 3; }}
.jp-OutputArea-output img, .jp-OutputArea-output svg {{ break-inside: avoid; }}
.MathJax_Display,
mjx-container[display="true"] {{ break-inside: avoid; break-before: avoid; }}

/* ── 4. Image sizing for print ─────────────────────────────────── */
.jp-OutputArea-output {{ text-align: center; }}
.jp-OutputArea-output img,
.jp-OutputArea-output svg {{
    display: block;
    max-width: {style['image_max_width']};
    max-height: {style['image_max_height']};
    width: auto;
    height: auto;
    object-fit: contain;
    margin: {style['image_margin']};
}}
{side_by_side_css}</style>
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


def _is_glossary_cell(source: str) -> bool:
    """Check if a markdown cell starts a glossary section."""
    for line in source.split("\n"):
        line = line.strip()
        for pattern in GLOSSARY_HEADING_PATTERNS:
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


def _mime_bundle_to_text(value: object) -> str:
    """Normalize a notebook mime bundle value to plain text."""
    if isinstance(value, list):
        return "".join(str(part) for part in value)
    return str(value)


def _is_matplotlib_animation_output(output: dict) -> bool:
    """Detect HTML produced by matplotlib animation.to_jshtml()."""
    if output.get("output_type", "") not in ("display_data", "execute_result"):
        return False

    data = output.get("data", {})
    html = data.get("text/html")
    if html is None:
        return False

    html_text = _mime_bundle_to_text(html)
    return any(marker in html_text for marker in MATPLOTLIB_ANIMATION_MARKERS)


def _make_animation_placeholder_output() -> dict:
    """Return a lightweight note for static exports in place of JS animation."""
    return {
        "output_type": "display_data",
        "data": {
            "text/html": [ANIMATION_EXPORT_PLACEHOLDER],
            "text/plain": [
                "[Interaktive Matplotlib-Animation im statischen Export ausgelassen.]",
            ],
        },
        "metadata": {},
    }


def _cell_source_to_text(cell: dict) -> str:
    """Normalize a notebook cell source field to plain text."""
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source)


def _set_cell_source(cell: dict, text: str) -> dict:
    """Write normalized text back to a cell source, preserving list/string shape."""
    updated = copy.deepcopy(cell)
    source = updated.get("source", "")
    if isinstance(source, list):
        updated["source"] = [text]
    else:
        updated["source"] = text
    return updated


def _expand_markdown_details(source: str) -> str:
    """Force markdown <details> blocks to be expanded in static exports."""

    def _add_open_attribute(match: re.Match) -> str:
        tag = match.group(0)
        if re.search(r"\\bopen\\b", tag, re.IGNORECASE):
            return tag
        return tag[:-1] + " open>"

    return DETAILS_OPEN_TAG_PATTERN.sub(_add_open_attribute, source)


def _split_markdown_before_glossary(cell: dict) -> tuple[dict | None, bool]:
    """Return the markdown cell truncated before the first glossary heading."""

    if cell.get("cell_type") != "markdown":
        return cell, False

    source_text = _cell_source_to_text(cell)
    glossary_match = None

    for pattern in GLOSSARY_HEADING_PATTERNS:
        match = re.search(pattern, source_text, flags=re.IGNORECASE | re.MULTILINE)
        if match and (glossary_match is None or match.start() < glossary_match.start()):
            glossary_match = match

    if glossary_match is None:
        return cell, False

    before_glossary = source_text[: glossary_match.start()]
    # Drop trailing horizontal rules that only served as separators to the glossary
    before_glossary = re.sub(r"(?:\s*<hr\s*/?>\s*)+$", "", before_glossary, flags=re.IGNORECASE)
    trimmed = before_glossary.rstrip()

    if not trimmed.strip():
        return None, True

    if not trimmed.endswith("\n"):
        trimmed += "\n"

    return _set_cell_source(cell, trimmed), True


def _cell_requests_animation_export(cell: dict) -> bool:
    """Detect code cells that render an animation into notebook HTML output."""
    if cell.get("cell_type") != "code":
        return False
    source_text = _cell_source_to_text(cell)
    return any(marker in source_text for marker in ANIMATION_SOURCE_MARKERS)


def _replace_animation_outputs(cell: dict) -> dict:
    """Replace heavy matplotlib JS animation outputs with a small export note."""
    cell = copy.deepcopy(cell)
    filtered_outputs = []
    replaced_animation = False

    for output in cell.get("outputs", []):
        if _is_matplotlib_animation_output(output):
            if not replaced_animation:
                filtered_outputs.append(_make_animation_placeholder_output())
                replaced_animation = True
            continue
        filtered_outputs.append(output)

    if not replaced_animation and _cell_requests_animation_export(cell):
        filtered_outputs.append(_make_animation_placeholder_output())

    cell["outputs"] = filtered_outputs
    return cell


def _notebook_title(nb: dict, stem: str) -> str:
    """Page title: the first `## ` heading without its number ("01 - Zahlenmengen" -> "Zahlenmengen").

    Notebooks open with the chapter as `# ` and the topic as the first `## `.
    Falls back to the first `# ` heading, then to the file name.
    """
    first_h1 = None
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in _cell_source_to_text(cell).splitlines():
            if line.startswith("## "):
                return re.sub(r"^\d+\s*[-–.:]\s*", "", line[3:].strip()) or line[3:].strip()
            if line.startswith("# ") and first_h1 is None:
                first_h1 = line[2:].strip()
    return first_h1 or re.sub(r"^\d+[_ -]*", "", stem).replace("_", " ")


def preprocess_notebook(
    notebook_path: Path,
    *,
    no_input: bool = True,
    no_text_output: bool = False,
    no_exercises: bool = False,
    no_glossary: bool = False,
    strip_animation_outputs: bool = True,
    expand_details: bool = False,
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
    if (
        not no_text_output
        and not no_exercises
        and not no_glossary
        and not has_input_tags
        and not strip_animation_outputs
        and not expand_details
    ):
        return None

    nb = json.loads(raw)
    # The export runs on a temp copy; without a title nbconvert would name the
    # page after the temp file (<title>tmp_nba39c7</title>).
    nb.setdefault("metadata", {}).setdefault("title", _notebook_title(nb, notebook_path.stem))
    filtered_cells = []
    skip_remaining_for_glossary = False

    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type", "")

        if skip_remaining_for_glossary:
            continue

        # Optionally skip exercise / solution markdown cells
        if no_exercises and cell_type == "markdown":
            source = "".join(cell.get("source", []))
            if _is_exercise_cell(source):
                continue

        if expand_details and cell_type == "markdown":
            source = _cell_source_to_text(cell)
            expanded_source = _expand_markdown_details(source)
            if expanded_source != source:
                cell = _set_cell_source(cell, expanded_source)

        # Optionally skip glossary sections in compact PDF exports.
        if no_glossary and cell_type == "markdown":
            cell, hit_glossary = _split_markdown_before_glossary(cell)
            if hit_glossary:
                skip_remaining_for_glossary = True
                if cell is None:
                    continue

        # Optionally strip text-only outputs from code cells
        if strip_animation_outputs and cell_type == "code":
            cell = _replace_animation_outputs(cell)

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


# Links between notebooks are written as relative paths to the .ipynb file
# (`[02_Matrizen](../05_Vektoren_Matrizen/02_Matrizen.ipynb)`). Each export format
# must point them at its own output, or they end up broken or, in PDFs, as
# file:/// URLs that contain the local user's temp path.

_HTML_LINK = re.compile(r'(<a\b[^>]*?\bhref=")([^"]*)("[^>]*>)(.*?)</a>', re.IGNORECASE | re.DOTALL)
_MD_NOTEBOOK_LINK = re.compile(r"(?<!!)(\[[^\]]*\]\()([^)\s]+?)\.ipynb((?:#[^)\s]*)?\))")


def _is_relative_url(url: str) -> bool:
    """True for links like `../a/b.ipynb`; False for schemes, absolute paths and `#anchors`."""
    url = url.strip()
    return bool(url) and not url.startswith(("/", "#")) and not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", url)


def _rewrite_notebook_links_html(html: str, ext: str) -> str:
    """Point relative links to notebooks at the sibling export: `x.ipynb#a` -> `x.<ext>#a`."""

    def _sub(match: re.Match) -> str:
        href = match.group(2)
        path, sep, fragment = href.partition("#")
        if _is_relative_url(unescape(href)) and path.endswith(".ipynb"):
            href = f"{path[: -len('.ipynb')]}.{ext}{sep}{fragment}"
        return f"{match.group(1)}{href}{match.group(3)}{match.group(4)}</a>"

    return _HTML_LINK.sub(_sub, html)


def _rewrite_notebook_links_markdown(text: str) -> str:
    """Markdown exports: `[t](x.ipynb)` -> `[t](x.md)` for relative links."""

    def _sub(match: re.Match) -> str:
        if not _is_relative_url(match.group(2)):
            return match.group(0)
        return f"{match.group(1)}{match.group(2)}.md{match.group(3)}"

    return _MD_NOTEBOOK_LINK.sub(_sub, text)


def _resolve_pdf_links(html: str, chapter: PurePosixPath, link_base: str | None) -> str:
    """Leave no relative link in the HTML that Chromium prints.

    Chromium resolves relative links against the document URL, which is a temp
    file, so every relative link would become a file:/// URL with a local path.
    With `link_base` set, links to notebooks become `<link_base>/<chapter>/<stem>.pdf`.
    Every other relative link (and every notebook link without a base) is unwrapped
    to its text. Absolute URLs, `mailto:` and `#anchors` stay as they are.
    """

    def _sub(match: re.Match) -> str:
        href = unescape(match.group(2))
        if not _is_relative_url(href):
            return match.group(0)
        path = href.partition("#")[0]
        if link_base and path.endswith(".ipynb"):
            target = posixpath.normpath(posixpath.join(chapter.as_posix(), unquote(path)))
            if not target.startswith(".."):
                url = f"{link_base.rstrip('/')}/{quote(target[: -len('.ipynb')] + '.pdf')}"
                return f"{match.group(1)}{url}{match.group(3)}{match.group(4)}</a>"
        return match.group(4)

    return _HTML_LINK.sub(_sub, html)


def _inject_html_export_css(
    html_path: Path,
    html_style: dict[str, str | None],
    *,
    side_by_side_config: dict | None = None,
) -> None:
    """Inject HTML export CSS and side-by-side transform into an exported notebook file."""
    if not html_path.exists():
        return
    html = html_path.read_text(encoding="utf-8")
    if HTML_EXPORT_CSS_MARKER in html:
        return  # already injected

    # Inject CSS (including side-by-side rules)
    html = html.replace(
        "</head>",
        _build_html_export_css(html_style, side_by_side_config=side_by_side_config) + "\n</head>",
        1,
    )

    # Apply side-by-side Zusammenfassung / Glossar HTML transform
    if side_by_side_config and side_by_side_config.get("enabled", True):
        html = _transform_side_by_side_html(html)

    # Inject dark mode script right after opening <body> tag
    dark_mode_script = """
    <script>
    document.addEventListener("DOMContentLoaded", () => {
      const body = document.body;

      const setDarkMode = (isDark) => {
        if (isDark) {
          body.setAttribute("data-jp-theme-light", "false");
          body.setAttribute("data-jp-theme-name", "JupyterLab Dark");
          localStorage.setItem("theme", "dark");
        } else {
          body.setAttribute("data-jp-theme-light", "true");
          body.setAttribute("data-jp-theme-name", "JupyterLab Light");
          localStorage.setItem("theme", "light");
        }
      };

      const savedTheme = localStorage.getItem("theme");
      if (savedTheme === "dark" || (!savedTheme && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
        setDarkMode(true);
      } else {
        setDarkMode(false);
      }
    });
    </script>
    """
    import re
    html = re.sub(r"(<body[^>]*>)", r"\1\n" + dark_mode_script.replace("\\", "\\\\"), html, count=1)

    html_path.write_text(html, encoding="utf-8")


def _html_to_pdf(
    html_path: Path,
    pdf_path: Path,
    pdf_style: dict[str, str],
    *,
    side_by_side_config: dict | None = None,
    chapter: PurePosixPath = PurePosixPath("."),
    link_base: str | None = None,
) -> None:
    """Convert an HTML file to PDF via Playwright Chromium with print CSS injected."""
    html = _resolve_pdf_links(html_path.read_text(encoding="utf-8"), chapter, link_base)

    # Apply side-by-side HTML transform before injecting print CSS
    if side_by_side_config and side_by_side_config.get("enabled", True):
        html = _transform_side_by_side_html(html)

    # Inject print-optimised CSS before </head>
    html = html.replace(
        "</head>",
        _build_pdf_print_css(pdf_style, side_by_side_config=side_by_side_config) + "\n</head>",
        1,
    )

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
                pdf_bytes = await page.pdf(
                    format=pdf_style["page_format"],
                    print_background=True,
                )
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
    html_style: dict[str, str | None],
    pdf_style: dict[str, str],
    *,
    no_text_output: bool = False,
    no_exercises: bool = False,
    no_glossary: bool = False,
    expand_details: bool = False,
    keep_glossary_notebooks: bool = True,
    side_by_side_config: dict | None = None,
    pdf_link_base: str | None = None,
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
    is_glossary_notebook = "99_Glossare" in notebook.parts
    filter_glossary_sections = no_glossary and (
        not is_glossary_notebook or not keep_glossary_notebooks
    )

    if no_glossary and is_glossary_notebook and not keep_glossary_notebooks:
        (dest_dir / f"{notebook.stem}.{fmt}").unlink(missing_ok=True)
        print(f"  SKIP  {relative} -> {fmt} (glossary notebook excluded)")
        return True

    # Preprocess notebook if any content filters or per-cell tags are active
    processed = preprocess_notebook(
        notebook, no_input=no_input,
        no_text_output=no_text_output,
        no_exercises=no_exercises,
        no_glossary=filter_glossary_sections,
        strip_animation_outputs=True,
        expand_details=expand_details,
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
            print(f"  FAIL  {relative} -> {fmt}")
            print(f"        {result.stderr.strip()}")
            return False
        # Post-process HTML with layout fixes and optional sizing overrides.
        if fmt == "html":
            html_file = dest_dir / f"{notebook.stem}.html"
            _inject_html_export_css(
                html_file,
                html_style,
                side_by_side_config=side_by_side_config,
            )
            html_file.write_text(
                _rewrite_notebook_links_html(html_file.read_text(encoding="utf-8"), "html"),
                encoding="utf-8",
            )

        # Post-process markdown to fix absolute image paths and notebook links
        if fmt == "markdown":
            md_file = dest_dir / f"{notebook.stem}.md"
            _fix_markdown_image_paths(md_file)
            if md_file.exists():
                md_file.write_text(
                    _rewrite_notebook_links_markdown(md_file.read_text(encoding="utf-8")),
                    encoding="utf-8",
                )

        # PDF: convert the intermediate HTML to PDF via Playwright, then clean up
        if fmt == "pdf":
            html_file = dest_dir / f"{notebook.stem}.html"
            pdf_file = dest_dir / f"{notebook.stem}.pdf"
            _html_to_pdf(
                html_file, pdf_file, pdf_style,
                side_by_side_config=side_by_side_config,
                chapter=PurePosixPath(relative.parent.as_posix()),
                link_base=pdf_link_base,
            )
            html_file.unlink(missing_ok=True)

        print(f"  OK    {relative} -> {fmt}")
        return True
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT  {relative} -> {fmt}")
        return False
    except Exception as e:
        print(f"  ERROR {relative} -> {fmt}: {e}")
        return False
    finally:
        # Clean up temp file from preprocessing
        if processed and processed.exists():
            processed.unlink()


# ============================================================================
# MAIN
# ============================================================================


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]

    try:
        profile = bootstrap_profile_settings(
            repo_root,
            "export_notebooks",
            DEFAULTS,
        )
    except PROFILE_LOAD_EXCEPTIONS as exc:
        print(f"ERROR: {exc}")
        return 1

    settings = profile.settings
    profile_path = profile.profile_path

    parser = argparse.ArgumentParser(
        description="Export Jupyter notebooks to HTML/PDF with mirrored folder structure.",
        parents=[profile.config_parser],
    )
    parser.add_argument(
        "--source-dir",
        default=settings["source_dir"],
        help=f"Root directory containing notebooks (default: {settings['source_dir']})",
    )
    parser.add_argument(
        "--output-dir",
        default=settings["output_dir"],
        help=f"Root output directory for exports (default: {settings['output_dir']})",
    )
    parser.add_argument(
        "--formats",
        nargs="+",
        choices=VALID_FORMATS,
        default=settings["formats"],
        help=f"Export formats (default: {' '.join(settings['formats'])})",
    )
    parser.add_argument(
        "--no-input",
        action="store_true",
        default=settings["no_input"],
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
        default=settings["filters"]["no_text_output"],
        help="Strip text/print output from code cells, keep only figures and rich HTML",
    )
    parser.add_argument(
        "--no-exercises",
        action="store_true",
        default=settings["filters"]["no_exercises"],
        help="Exclude exercise and solution sections (Verständnis-Check, Lösungen)",
    )
    parser.add_argument(
        "--expand-details",
        action="store_true",
        default=settings["filters"].get("expand_details", False),
        help=(
            "Expand markdown <details> blocks in static exports so collapsed "
            "challenge/solution content is visible"
        ),
    )
    parser.add_argument(
        "--exclude-glossary-formats",
        nargs="+",
        choices=VALID_FORMATS,
        default=settings["filters"]["exclude_glossary_formats"],
        help=(
            "Formats where glossary sections should be omitted "
            f"(default: {' '.join(settings['filters']['exclude_glossary_formats']) or 'none'})"
        ),
    )
    parser.add_argument(
        "--html-no-glossary",
        action="store_true",
        default=False,
        help="Shortcut: omit glossary sections in HTML exports too",
    )
    parser.add_argument(
        "--pdf-with-glossary",
        action="store_true",
        default=False,
        help="Compatibility shortcut: keep glossary sections in PDF exports",
    )
    parser.add_argument(
        "--skip-glossary-notebooks",
        action="store_true",
        default=not settings["filters"]["keep_glossary_notebooks"],
        help="When glossary sections are omitted, skip dedicated 99_Glossare notebooks too",
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
        default=settings["workers"],
        help=f"Number of parallel export workers (default: {settings['workers']}, use 1 to disable)",
    )
    parser.add_argument(
        "--pdf-link-base",
        default=settings.get("pdf_link_base", ""),
        help=(
            "Base URL of the published PDFs, e.g. https://example.org/learning/math/pdf/full. "
            "Links between notebooks in PDFs point to <base>/<chapter>/<stem>.pdf; "
            "without a base they become plain text"
        ),
    )
    parser.add_argument(
        "--no-side-by-side",
        action="store_true",
        default=False,
        help="Disable side-by-side Zusammenfassung / Glossar layout in exports",
    )

    args = parser.parse_args()
    source_dir = resolve_repo_path(repo_root, args.source_dir)
    output_dir = resolve_repo_path(repo_root, args.output_dir)

    no_input = args.no_input and not args.with_input
    configured_formats = list(dict.fromkeys(args.formats))
    exclude_glossary_formats = set(args.exclude_glossary_formats)
    if args.html_no_glossary:
        exclude_glossary_formats.add("html")
    if args.pdf_with_glossary:
        exclude_glossary_formats.discard("pdf")
    keep_glossary_notebooks = not args.skip_glossary_notebooks
    html_style = settings["styles"]["html"]
    pdf_style = settings["styles"]["pdf"]

    # Side-by-side config: per-format, overridable by --no-side-by-side
    html_sbs = settings["styles"]["html"].get("side_by_side", {})
    pdf_sbs = settings["styles"]["pdf"].get("side_by_side", {})
    if args.no_side_by_side:
        html_sbs = {"enabled": False}
        pdf_sbs = {"enabled": False}

    invalid_formats = sorted(set(configured_formats) - set(VALID_FORMATS))
    invalid_glossary_formats = sorted(exclude_glossary_formats - set(VALID_FORMATS))
    if invalid_formats:
        print(f"ERROR: Invalid export format(s) in configuration: {', '.join(invalid_formats)}")
        return 1
    if invalid_glossary_formats:
        print(
            "ERROR: Invalid glossary exclusion format(s) in configuration: "
            f"{', '.join(invalid_glossary_formats)}"
        )
        return 1

    # ── Pre-flight ─────────────────────────────────────────────────────────
    if not source_dir.is_dir():
        print(f"ERROR: Source directory not found: {source_dir}")
        return 1

    notebooks = discover_notebooks(source_dir)
    if not notebooks:
        print(f"No notebooks found under {source_dir}")
        return 0

    print(f"Export Notebooks")
    if profile_path is not None:
        print(f"  Profile: {format_profile_path(repo_root, profile_path)}")
    print(f"  Source:  {source_dir}")
    print(f"  Output:  {output_dir}")
    print(f"  Formats: {', '.join(configured_formats)}")
    print(f"  Code:    {'hidden' if no_input else 'visible'}")
    print(f"  Text output: {'stripped' if args.no_text_output else 'included'}")
    print(f"  Exercises:   {'excluded' if args.no_exercises else 'included'}")
    print(f"  Details blocks: {'expanded' if args.expand_details else 'as-authored'}")
    print(
        "  Glossary sections omitted for: "
        f"{', '.join(sorted(exclude_glossary_formats)) if exclude_glossary_formats else 'none'}"
    )
    print(
        "  Dedicated glossary notebooks: "
        f"{'included' if keep_glossary_notebooks else 'skipped when glossary is omitted'}"
    )
    print(f"  Workers: {args.workers}")
    sbs_enabled_html = html_sbs.get("enabled", True) and not args.no_side_by_side
    sbs_enabled_pdf = pdf_sbs.get("enabled", True) and not args.no_side_by_side
    sbs_parts = []
    if "html" in configured_formats:
        sbs_parts.append(f"HTML={'on' if sbs_enabled_html else 'off'}")
    if "pdf" in configured_formats:
        sbs_parts.append(f"PDF={'on' if sbs_enabled_pdf else 'off'}")
    if sbs_parts:
        print(f"  Side-by-side: {', '.join(sbs_parts)}")
    print(f"  Found:   {len(notebooks)} notebook(s)")
    print()

    # ── Export ─────────────────────────────────────────────────────────────
    total = 0
    failed = 0

    for fmt in configured_formats:
        print(f"── {fmt.upper()} ──")
        fmt_notebooks = list(notebooks)
        fmt_total = len(fmt_notebooks)
        no_glossary_for_format = fmt in exclude_glossary_formats

        if args.workers > 1 and fmt_total > 1:
            # Parallel export
            sbs_config = html_sbs if fmt == "html" else (pdf_sbs if fmt == "pdf" else None)
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                futures = {
                    pool.submit(
                        export_notebook,
                        nb, source_dir, output_dir, fmt, no_input, html_style, pdf_style,
                        no_text_output=args.no_text_output,
                        no_exercises=args.no_exercises,
                        no_glossary=no_glossary_for_format,
                        expand_details=args.expand_details,
                        keep_glossary_notebooks=keep_glossary_notebooks,
                        side_by_side_config=sbs_config,
                        pdf_link_base=args.pdf_link_base or None,
                    ): nb
                    for nb in fmt_notebooks
                }
                for future in as_completed(futures):
                    total += 1
                    if not future.result():
                        failed += 1
        else:
            # Sequential fallback
            sbs_config = html_sbs if fmt == "html" else (pdf_sbs if fmt == "pdf" else None)
            for nb in fmt_notebooks:
                total += 1
                success = export_notebook(
                    nb, source_dir, output_dir, fmt, no_input, html_style, pdf_style,
                    no_text_output=args.no_text_output,
                    no_exercises=args.no_exercises,
                    no_glossary=no_glossary_for_format,
                    expand_details=args.expand_details,
                    keep_glossary_notebooks=keep_glossary_notebooks,
                    side_by_side_config=sbs_config,
                    pdf_link_base=args.pdf_link_base or None,
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
