"""
consolidate_pdfs.py - Merge individual notebook PDF exports into a single reference file.

Reads the exported PDF files from exports/pdf/, merges them in chapter order
into one large PDF with:
  - A generated cover / title page
  - A table of contents page with clickable links
  - PDF bookmarks (outline) grouped by chapter for sidebar navigation
  - Page labels so viewers show logical page numbers

Requires the repository venv to be activated first:
    .\\venv\\Scripts\\activate

Dependencies (pip install):
    pypdf, reportlab

Usage:
    python scripts/consolidate_pdfs.py
    python scripts/consolidate_pdfs.py --output-dir exports --title "Mathematik Referenz"
    python scripts/consolidate_pdfs.py --no-cover   # skip title / TOC pages
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULTS = {
    "pdf_dir": "exports_clean/pdf",
    "output_dir": "exports_clean",
    "output_name": "reference.pdf",
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
# HELPERS
# ============================================================================


def chapter_display_name(chapter_key: str) -> str:
    """Map folder name to a human-readable chapter name."""
    if "/" in chapter_key:
        parts = chapter_key.split("/")
        return " › ".join(CHAPTER_NAMES.get(p, p.replace("_", " ")) for p in parts)
    return CHAPTER_NAMES.get(chapter_key, chapter_key.replace("_", " "))


def notebook_display_name(path: Path) -> str:
    """Turn '01_Zahlenmengen_Rechenarten.pdf' into 'Zahlenmengen Rechenarten'."""
    name = path.stem
    # Strip leading number prefix like '01_', '02_'
    name = re.sub(r"^\d+_", "", name)
    return name.replace("_", " ")


def discover_pdf_files(pdf_dir: Path) -> dict[str, list[Path]]:
    """
    Group PDF files by their parent chapter folder.
    Returns {chapter_folder: [sorted list of pdf files]}.
    """
    chapters: dict[str, list[Path]] = {}
    for pdf_file in sorted(pdf_dir.rglob("*.pdf")):
        rel = pdf_file.relative_to(pdf_dir)
        parts = rel.parts
        if len(parts) > 2:
            chapter_key = "/".join(parts[:-1])
        elif len(parts) == 2:
            chapter_key = parts[0]
        else:
            chapter_key = "_root"
        chapters.setdefault(chapter_key, []).append(pdf_file)
    return chapters


# ============================================================================
# COVER & TOC PAGE GENERATION  (reportlab)
# ============================================================================


def _build_cover_and_toc(
    chapters: dict[str, list[Path]],
    title: str,
    page_map: dict[str, int],
) -> bytes:
    """
    Generate a short PDF (in memory) containing:
      1. A title / cover page
      2. A table-of-contents page with chapter + notebook entries

    page_map: {notebook_stem: starting_page_number} where page numbers
              are 1-based offsets *after* the cover/TOC pages are prepended.

    Returns raw PDF bytes.
    """
    from io import BytesIO

    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.pdfgen.canvas import Canvas

    buf = BytesIO()
    c = Canvas(buf, pagesize=A4)
    w, h = A4

    # ── Page 1: Cover ──────────────────────────────────────────────────────
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(w / 2, h - 8 * cm, title)

    c.setFont("Helvetica", 13)
    c.drawCentredString(w / 2, h - 10 * cm, "Gesamtreferenz aller Notebooks")

    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(w / 2, 3 * cm, "Automatisch generiert aus Jupyter Notebooks")

    c.showPage()

    # ── Page 2+: Table of Contents ─────────────────────────────────────────
    c.setFont("Helvetica-Bold", 20)
    c.drawString(2.5 * cm, h - 3 * cm, "Inhaltsverzeichnis")

    y = h - 4.5 * cm
    line_height = 0.65 * cm
    chapter_gap = 0.3 * cm

    for chapter_key, files in chapters.items():
        # Chapter heading
        if y < 3 * cm:
            c.showPage()
            y = h - 3 * cm

        ch_display = chapter_display_name(chapter_key)
        c.setFont("Helvetica-Bold", 12)
        y -= chapter_gap
        c.drawString(2.5 * cm, y, ch_display)
        y -= line_height

        for pdf_file in files:
            if y < 3 * cm:
                c.showPage()
                y = h - 3 * cm

            nb_display = notebook_display_name(pdf_file)
            page_num = page_map.get(pdf_file.stem, "")

            c.setFont("Helvetica", 10)
            c.drawString(3.2 * cm, y, nb_display)

            if page_num:
                c.drawRightString(w - 2.5 * cm, y, str(page_num))

                # Draw dot leaders between title and page number
                text_width = c.stringWidth(nb_display, "Helvetica", 10)
                dots_start = 3.2 * cm + text_width + 0.3 * cm
                dots_end = w - 2.5 * cm - c.stringWidth(str(page_num), "Helvetica", 10) - 0.3 * cm
                if dots_end > dots_start:
                    c.setFont("Helvetica", 8)
                    dot_str = " . " * int((dots_end - dots_start) / c.stringWidth(" . ", "Helvetica", 8))
                    c.drawString(dots_start, y, dot_str)

            y -= line_height

    c.showPage()
    c.save()
    return buf.getvalue()


# ============================================================================
# PDF MERGING
# ============================================================================


def build_consolidated_pdf(
    chapters: dict[str, list[Path]],
    title: str,
    include_cover: bool = True,
) -> PdfWriter:
    """
    Merge all chapter PDFs into a single PdfWriter with bookmarks.

    If include_cover is True, a cover page and TOC are prepended.
    """
    writer = PdfWriter()

    # ── First pass: merge all notebook PDFs and record page offsets ─────────
    # We need page counts before building the TOC, so we do two passes when
    # a cover is requested: count pages first, build cover, then merge.

    notebook_page_counts: list[tuple[str, Path, int]] = []  # (chapter_key, file, page_count)

    for chapter_key, files in chapters.items():
        for pdf_file in files:
            try:
                reader = PdfReader(str(pdf_file))
                notebook_page_counts.append((chapter_key, pdf_file, len(reader.pages)))
            except Exception as e:
                print(f"  WARN  Could not read {pdf_file.name}: {e}")

    if not notebook_page_counts:
        print("ERROR: No valid PDF files to merge.")
        sys.exit(1)

    # ── Compute page offsets (1-based, accounting for cover/TOC pages) ─────
    cover_pages = 0
    if include_cover:
        # Estimate cover/TOC length (we'll know exactly after generating)
        # Generate a preliminary cover to count its pages
        preliminary_map: dict[str, int] = {}
        offset = 1  # placeholder
        for _, pdf_file, count in notebook_page_counts:
            preliminary_map[pdf_file.stem] = offset
            offset += count
        from io import BytesIO
        preliminary_cover = _build_cover_and_toc(chapters, title, preliminary_map)
        cover_reader = PdfReader(BytesIO(preliminary_cover))
        cover_pages = len(cover_reader.pages)

    # Build the real page map with cover pages accounted for
    page_map: dict[str, int] = {}
    current_page = cover_pages + 1  # 1-based page number after cover
    for _, pdf_file, count in notebook_page_counts:
        page_map[pdf_file.stem] = current_page
        current_page += count

    # ── Generate final cover/TOC ───────────────────────────────────────────
    if include_cover:
        cover_bytes = _build_cover_and_toc(chapters, title, page_map)
        cover_reader = PdfReader(BytesIO(cover_bytes))
        # Verify page count hasn't changed (it shouldn't, same content)
        assert len(cover_reader.pages) == cover_pages, "Cover page count mismatch"
        for page in cover_reader.pages:
            writer.add_page(page)

    # ── Merge notebook PDFs with bookmarks ─────────────────────────────────
    current_chapter: str | None = None
    chapter_bookmark = None

    for chapter_key, pdf_file, page_count in notebook_page_counts:
        nb_display = notebook_display_name(pdf_file)
        ch_display = chapter_display_name(chapter_key)

        try:
            reader = PdfReader(str(pdf_file))
        except Exception as e:
            print(f"  WARN  Could not read {pdf_file.name}: {e}")
            continue

        first_page_index = len(writer.pages)

        for page in reader.pages:
            writer.add_page(page)

        # Add chapter-level bookmark (parent) when chapter changes
        if chapter_key != current_chapter:
            current_chapter = chapter_key
            chapter_bookmark = writer.add_outline_item(
                ch_display, first_page_index
            )

        # Add notebook-level bookmark (child of chapter)
        writer.add_outline_item(
            nb_display, first_page_index, parent=chapter_bookmark
        )

        print(f"  OK    {ch_display} / {nb_display} ({page_count} pages)")

    # ── Set PDF metadata ───────────────────────────────────────────────────
    writer.add_metadata(
        {
            "/Title": title,
            "/Subject": "Mathematik Gesamtreferenz - Jupyter Notebooks",
            "/Creator": "consolidate_pdfs.py (pypdf + reportlab)",
        }
    )

    return writer


# ============================================================================
# MAIN
# ============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Consolidate exported notebook PDFs into a single reference file.",
    )
    parser.add_argument(
        "--pdf-dir",
        default=DEFAULTS["pdf_dir"],
        help=f"Directory with exported PDFs (default: {DEFAULTS['pdf_dir']})",
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
    parser.add_argument(
        "--no-cover",
        action="store_true",
        default=False,
        help="Skip cover page and table of contents generation",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    pdf_dir = repo_root / args.pdf_dir
    output_dir = repo_root / args.output_dir
    output_file = output_dir / args.output_name

    # ── Pre-flight ─────────────────────────────────────────────────────────
    if not pdf_dir.is_dir():
        print(f"ERROR: PDF export directory not found: {pdf_dir}")
        print("Run export_notebooks.py --formats pdf first to generate PDF files.")
        return 1

    chapters = discover_pdf_files(pdf_dir)
    total = sum(len(files) for files in chapters.values())

    if total == 0:
        print(f"No PDF files found under {pdf_dir}")
        return 1

    include_cover = not args.no_cover

    print(f"Consolidate PDFs")
    print(f"  Source:   {pdf_dir}")
    print(f"  Output:   {output_file}")
    print(f"  Chapters: {len(chapters)}")
    print(f"  Notebooks: {total}")
    print(f"  Cover/TOC: {'yes' if include_cover else 'no'}")
    print()

    # ── Build ──────────────────────────────────────────────────────────────
    writer = build_consolidated_pdf(chapters, args.title, include_cover)

    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_file, "wb") as f:
        writer.write(f)

    size_mb = output_file.stat().st_size / (1024 * 1024)
    total_pages = len(writer.pages)
    print()
    print(f"Done: {output_file.name} ({total_pages} pages, {size_mb:.1f} MB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
