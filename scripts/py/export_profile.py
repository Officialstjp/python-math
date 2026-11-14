"""Helpers for loading export and consolidation profile settings.

An optional TOML profile at ``scripts/export_profile.toml`` can override the
built-in defaults for notebook export and consolidation scripts.
"""

from __future__ import annotations

import argparse
import copy
from pathlib import Path
from typing import Any, NamedTuple

import tomllib


DEFAULT_PROFILE_PATH = Path("scripts/export_profile.toml")
PROFILE_LOAD_EXCEPTIONS = (FileNotFoundError, ValueError, tomllib.TOMLDecodeError)


NOTEBOOK_EXPORT_DEFAULTS: dict[str, Any] = {
    "source_dir": "Foundations",
    "output_dir": "exports",
    "formats": ["html"],
    "no_input": True,
    "notebook_glob": "**/*.ipynb",
    "workers": 4,
    # Base URL of the published PDFs; links between notebooks in PDFs point there.
    # Empty: those links become plain text (a relative link would print as file:///).
    "pdf_link_base": "",
    "filters": {
        "exclude_glossary_formats": ["pdf"],
        "keep_glossary_notebooks": True,
        "no_exercises": False,
        "no_text_output": False,
        "expand_details": False,
    },
    "styles": {
        "html": {
            "body_padding": None,
            "content_font_size": None,
            "content_line_height": None,
            "image_max_width": None,
            "image_max_height": None,
            "image_margin": None,
            "side_by_side": {
                "enabled": True,
                "gap": "2rem",
                "min_column_width": "280px",
                "equal_columns": True,
                "show_divider": False,
            },
        },
        "pdf": {
            "page_format": "A4",
            "content_font_size": "8.5pt",
            "content_font_size_small": "7.75pt",
            "code_font_size": "7pt",
            "content_line_height": "1.32",
            "heading_line_height": "1.2",
            "body_padding": "0 0.15in",
            "page_margin": "0.6in 0.5in",
            "table_font_size": "8pt",
            "table_cell_padding": "0.16rem 0.3rem",
            "image_max_width": "min(100%, 7in)",
            "image_max_height": "3.7in",
            "image_margin": "0.08in auto 0.12in",
            "side_by_side": {
                "enabled": True,
                "gap": "0.4in",
                "min_column_width": "220px",
                "equal_columns": True,
                "show_divider": False,
            },
        },
    },
}


CONSOLIDATE_HTML_DEFAULTS: dict[str, Any] = {
    "html_dir": "exports/html",
    "output_dir": "exports",
    "output_name": "reference.html",
    "title": "Mathematik - Gesamtreferenz",
    "filters": {
        "exclude_chapters": [],
    },
    "layout": {
        "sidebar_width": "280px",
        "content_max_width": "1000px",
        "content_padding": "2rem 3rem",
        "hide_sidebar_below": "900px",
        "body_font_family": '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        "sidebar_background": "#1e1e2e",
        "sidebar_text": "#cdd6f4",
        "title_color": "#cba6f7",
        "accent": "#89b4fa",
        "divider": "#e0e0e0",
        "notebook_image_max_width": "100%",
        "notebook_image_max_height": "none",
        "section_break_after": "always",
    },
    "side_by_side": {
        "enabled": True,
        "gap": "2rem",
        "min_column_width": "280px",
        "equal_columns": True,
        "show_divider": False,
    },
}


CONSOLIDATE_PDF_DEFAULTS: dict[str, Any] = {
    "pdf_dir": "exports_clean/pdf",
    "output_dir": "exports_clean",
    "output_name": "reference.pdf",
    "title": "Mathematik - Gesamtreferenz",
    "include_cover": True,
    "filters": {
        "exclude_chapters": [],
    },
    "metadata": {
        "subject": "Mathematik Gesamtreferenz - Jupyter Notebooks",
        "creator": "consolidate_pdfs.py (pypdf + reportlab)",
    },
    "cover": {
        "subtitle": "Gesamtreferenz aller Notebooks",
        "footer_note": "Automatisch generiert aus Jupyter Notebooks",
    },
}


class LoadedProfile(NamedTuple):
    """Profile settings loaded for one CLI entrypoint."""

    config_parser: argparse.ArgumentParser
    settings: dict[str, Any]
    profile_path: Path | None


def deep_merge(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge two dictionaries without mutating either input."""
    merged = copy.deepcopy(base)
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def _resolve_profile_path(repo_root: Path, config_path: str | None) -> Path | None:
    if config_path:
        candidate = Path(config_path)
        if not candidate.is_absolute():
            candidate = repo_root / candidate
        if not candidate.is_file():
            raise FileNotFoundError(f"Config file not found: {candidate}")
        return candidate

    candidate = repo_root / DEFAULT_PROFILE_PATH
    if candidate.is_file():
        return candidate
    return None


def _normalize_section_names(section_name: str | list[str] | tuple[str, ...]) -> tuple[str, ...]:
    """Accept either one section name or a list of compatible aliases."""
    if isinstance(section_name, str):
        return (section_name,)
    return tuple(section_name)


def build_config_parser() -> argparse.ArgumentParser:
    """Create the shared parser used by scripts that support --config."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "--config",
        default=None,
        help=(
            "Optional TOML profile path (defaults to "
            f"{DEFAULT_PROFILE_PATH.as_posix()} when present)"
        ),
    )
    return parser


def bootstrap_profile_settings(
    repo_root: Path,
    section_name: str | list[str] | tuple[str, ...],
    defaults: dict[str, Any],
    config_path: str | None = None,
) -> LoadedProfile:
    """Load profile settings and the shared --config parser for one script."""
    config_parser = build_config_parser()
    resolved_config_path = config_path
    if resolved_config_path is None:
        config_args, _ = config_parser.parse_known_args()
        resolved_config_path = config_args.config

    settings, profile_path = load_profile_section(
        repo_root,
        section_name,
        defaults,
        resolved_config_path,
    )
    return LoadedProfile(config_parser, settings, profile_path)


def format_profile_path(repo_root: Path, profile_path: Path) -> str:
    """Format a profile path relative to the repo root when possible."""
    try:
        return profile_path.relative_to(repo_root).as_posix()
    except ValueError:
        return str(profile_path)


def resolve_repo_path(repo_root: Path, configured_path: str | Path) -> Path:
    """Resolve a configured path relative to the repository unless it is absolute."""
    candidate = Path(configured_path)
    if candidate.is_absolute():
        return candidate
    return repo_root / candidate


def load_profile_section(
    repo_root: Path,
    section_name: str | list[str] | tuple[str, ...],
    defaults: dict[str, Any],
    config_path: str | None = None,
) -> tuple[dict[str, Any], Path | None]:
    """Load one profile section and merge it into the provided defaults."""
    section_names = _normalize_section_names(section_name)
    profile_path = _resolve_profile_path(repo_root, config_path)
    if profile_path is None:
        return copy.deepcopy(defaults), None

    with open(profile_path, "rb") as handle:
        raw_profile = tomllib.load(handle)

    section_data: dict[str, Any] = {}
    for current_name in section_names:
        if current_name not in raw_profile:
            continue

        section_data = raw_profile[current_name]
        if not isinstance(section_data, dict):
            raise ValueError(f"Config section '{current_name}' must be a TOML table")
        break

    return deep_merge(defaults, section_data), profile_path