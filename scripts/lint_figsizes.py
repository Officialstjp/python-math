"""Lint Matplotlib figsize usage in notebook code cells.

The exporter scales figure outputs into a fixed PDF image box. Very wide
figures become short strips, while tall or square figures tend to consume the
full image height. This script finds common figsize patterns and points out
figures that are likely to export poorly.

Usage:
    python scripts/lint_figsizes.py
    python scripts/lint_figsizes.py --source-dir Foundations/01_Algebra
    python scripts/lint_figsizes.py --config scripts/export_profile.toml.example --all
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import tomllib


DEFAULT_SOURCE_DIR = "Foundations"
DEFAULT_PROFILE_CANDIDATES = (
    Path("scripts/export_profile.toml"),
    Path("scripts/export_profile.toml.example"),
)
DEFAULT_IMAGE_BOX = (5.6, 3.5)


@dataclass(frozen=True)
class FigureSize:
    width: float
    height: float

    @property
    def aspect(self) -> float:
        return self.width / self.height if self.height else math.inf


@dataclass(frozen=True)
class Finding:
    notebook: Path
    cell_number: int
    line_number: int
    call_name: str
    figsize: FigureSize
    source_line: str
    resolved_from: str | None
    rows: int | None
    columns: int | None


@dataclass(frozen=True)
class Assessment:
    severity: str
    reason: str
    suggestion: str
    rendered_size: FigureSize


class CellFigsizeVisitor(ast.NodeVisitor):
    """Find figsize arguments and simple literal assignments in one code cell."""

    def __init__(self, notebook: Path, cell_number: int, source_lines: list[str]) -> None:
        self.notebook = notebook
        self.cell_number = cell_number
        self.source_lines = source_lines
        self.values: dict[str, FigureSize] = {}
        self.dict_values: dict[str, dict[str, FigureSize]] = {}
        self.findings: list[Finding] = []

    def visit_Assign(self, node: ast.Assign) -> Any:
        self.visit(node.value)

        dict_value = self._dict_figsizes(node.value)
        size_value = self._resolve_figsize(node.value)

        for target in node.targets:
            if isinstance(target, ast.Name):
                if size_value is not None:
                    self.values[target.id] = size_value
                if dict_value:
                    self.dict_values[target.id] = dict_value

            rcparam_size = self._rcparam_figsize_target(target)
            if rcparam_size and size_value is not None:
                self.findings.append(
                    self._finding(
                        node,
                        "rcParams.figure.figsize",
                        size_value,
                        resolved_from=None,
                        rows=None,
                        columns=None,
                    )
                )

    def visit_AnnAssign(self, node: ast.AnnAssign) -> Any:
        if node.value is None:
            return

        self.visit(node.value)
        if isinstance(node.target, ast.Name):
            size_value = self._resolve_figsize(node.value)
            dict_value = self._dict_figsizes(node.value)
            if size_value is not None:
                self.values[node.target.id] = size_value
            if dict_value:
                self.dict_values[node.target.id] = dict_value

    def visit_Call(self, node: ast.Call) -> Any:
        call_name = _call_name(node.func)
        figsize_node = _keyword_value(node, "figsize")

        if figsize_node is not None:
            size_value = self._resolve_figsize(figsize_node)
            if size_value is not None:
                rows, columns = self._subplot_shape(node, call_name)
                self.findings.append(
                    self._finding(
                        node,
                        call_name or "call",
                        size_value,
                        resolved_from=self._resolved_from(figsize_node),
                        rows=rows,
                        columns=columns,
                    )
                )

        if call_name and call_name.endswith(".set_size_inches"):
            size_value = self._set_size_inches_value(node)
            if size_value is not None:
                self.findings.append(
                    self._finding(
                        node,
                        call_name,
                        size_value,
                        resolved_from=None,
                        rows=None,
                        columns=None,
                    )
                )

        self.generic_visit(node)

    def _finding(
        self,
        node: ast.AST,
        call_name: str,
        size_value: FigureSize,
        *,
        resolved_from: str | None,
        rows: int | None,
        columns: int | None,
    ) -> Finding:
        line_number = getattr(node, "lineno", 1)
        source_line = ""
        if 1 <= line_number <= len(self.source_lines):
            source_line = self.source_lines[line_number - 1].strip()
        return Finding(
            notebook=self.notebook,
            cell_number=self.cell_number,
            line_number=line_number,
            call_name=call_name,
            figsize=size_value,
            source_line=source_line,
            resolved_from=resolved_from,
            rows=rows,
            columns=columns,
        )

    def _subplot_shape(self, node: ast.Call, call_name: str | None) -> tuple[int | None, int | None]:
        if not call_name or not call_name.endswith("subplots"):
            return None, None

        rows = _number_arg(node, 0) or _number_keyword(node, "nrows") or 1
        columns = _number_arg(node, 1) or _number_keyword(node, "ncols") or 1
        if isinstance(rows, float) and rows.is_integer():
            rows = int(rows)
        if isinstance(columns, float) and columns.is_integer():
            columns = int(columns)
        return rows if isinstance(rows, int) else None, columns if isinstance(columns, int) else None

    def _set_size_inches_value(self, node: ast.Call) -> FigureSize | None:
        if len(node.args) >= 2:
            width = _number(node.args[0])
            height = _number(node.args[1])
            if width is not None and height is not None:
                return FigureSize(width, height)
        if len(node.args) == 1:
            return self._resolve_figsize(node.args[0])
        return None

    def _resolve_figsize(self, node: ast.AST) -> FigureSize | None:
        literal = _literal_figsize(node)
        if literal is not None:
            return literal

        if isinstance(node, ast.Name):
            return self.values.get(node.id)

        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
            key = _subscript_key(node)
            if key is not None:
                return self.dict_values.get(node.value.id, {}).get(key)

        return None

    def _dict_figsizes(self, node: ast.AST) -> dict[str, FigureSize]:
        if not isinstance(node, ast.Dict):
            return {}

        values: dict[str, FigureSize] = {}
        for key_node, value_node in zip(node.keys, node.values):
            if key_node is None:
                continue
            key = _constant_string(key_node)
            size_value = self._resolve_figsize(value_node)
            if key and size_value is not None:
                values[key] = size_value
        return values

    def _resolved_from(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
            key = _subscript_key(node)
            if key is not None:
                return f"{node.value.id}[{key!r}]"
        return None

    def _rcparam_figsize_target(self, node: ast.AST) -> bool:
        if not isinstance(node, ast.Subscript):
            return False
        key = _subscript_key(node)
        return key == "figure.figsize"


def _keyword_value(node: ast.Call, keyword_name: str) -> ast.AST | None:
    for keyword in node.keywords:
        if keyword.arg == keyword_name:
            return keyword.value
    return None


def _number_keyword(node: ast.Call, keyword_name: str) -> float | None:
    value = _keyword_value(node, keyword_name)
    return _number(value) if value is not None else None


def _number_arg(node: ast.Call, index: int) -> float | None:
    if len(node.args) <= index:
        return None
    return _number(node.args[index])


def _call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _call_name(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return None


def _literal_figsize(node: ast.AST) -> FigureSize | None:
    if not isinstance(node, (ast.Tuple, ast.List)) or len(node.elts) != 2:
        return None
    width = _number(node.elts[0])
    height = _number(node.elts[1])
    if width is None or height is None:
        return None
    return FigureSize(width, height)


def _number(node: ast.AST | None) -> float | None:
    if node is None:
        return None
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        value = _number(node.operand)
        return -value if value is not None else None
    return None


def _constant_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _subscript_key(node: ast.Subscript) -> str | None:
    return _constant_string(node.slice)


def notebook_source(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source)


def iter_notebooks(source_dir: Path) -> list[Path]:
    return sorted(
        path for path in source_dir.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in path.parts
    )


def extract_findings(notebook_path: Path, *, show_parse_errors: bool = False) -> list[Finding]:
    raw = json.loads(notebook_path.read_text(encoding="utf-8"))
    findings: list[Finding] = []
    for index, cell in enumerate(raw.get("cells", []), start=1):
        if cell.get("cell_type") != "code":
            continue

        source = notebook_source(cell)
        if not source.strip():
            continue

        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            if show_parse_errors:
                print(f"PARSE  {notebook_path} cell {index}: {exc.msg}", file=sys.stderr)
            continue

        visitor = CellFigsizeVisitor(notebook_path, index, source.splitlines())
        visitor.visit(tree)
        findings.extend(visitor.findings)
    return findings


def parse_inches(value: str | None) -> float | None:
    if not value:
        return None
    matches = re.findall(r"([0-9]+(?:\.[0-9]+)?)\s*in\b", value)
    if not matches:
        return None
    return float(matches[-1])


def resolve_profile_path(repo_root: Path, config_path: str | None) -> Path | None:
    if config_path:
        candidate = Path(config_path)
        return candidate if candidate.is_absolute() else repo_root / candidate

    for candidate in DEFAULT_PROFILE_CANDIDATES:
        resolved = repo_root / candidate
        if resolved.is_file():
            return resolved
    return None


def load_image_box(repo_root: Path, config_path: str | None) -> tuple[FigureSize, Path | None]:
    profile_path = resolve_profile_path(repo_root, config_path)
    if profile_path is None or not profile_path.is_file():
        return FigureSize(*DEFAULT_IMAGE_BOX), None

    with open(profile_path, "rb") as handle:
        raw = tomllib.load(handle)
    pdf_style = raw.get("export_notebooks", {}).get("styles", {}).get("pdf", {})
    width = parse_inches(pdf_style.get("image_max_width")) or DEFAULT_IMAGE_BOX[0]
    height = parse_inches(pdf_style.get("image_max_height")) or DEFAULT_IMAGE_BOX[1]
    return FigureSize(width, height), profile_path


def rendered_size(figsize: FigureSize, image_box: FigureSize) -> FigureSize:
    scale = min(image_box.width / figsize.width, image_box.height / figsize.height)
    return FigureSize(figsize.width * scale, figsize.height * scale)


def assess(finding: Finding, image_box: FigureSize) -> Assessment:
    size = finding.figsize
    rendered = rendered_size(size, image_box)
    aspect = size.aspect
    rows = finding.rows or 1
    columns = finding.columns or 1

    if columns >= 4 or aspect >= 3.5:
        return Assessment(
            "change",
            "very wide figure; PDF export compresses it into a short strip",
            "split into multiple figures or use a vertical/2-row layout",
            rendered,
        )

    if columns >= 3 or aspect >= 2.7:
        return Assessment(
            "change",
            "wide multi-panel figure; labels and curves will shrink in compact PDF",
            "prefer two panels per figure, or use a 2-row subplot layout",
            rendered,
        )

    if columns == 2 and aspect >= 2.25:
        return Assessment(
            "review",
            "two-panel figure is wider than the stable compact-export range",
            "target about (8, 4) to (9, 4.5), or split if labels matter",
            rendered,
        )

    if rows >= 2 and size.height >= 8:
        return Assessment(
            "review",
            "tall stacked figure will consume the PDF image height cap",
            "split stacked plots or reduce height toward 6 to 7 inches",
            rendered,
        )

    if aspect <= 1.15 and size.height >= 5.5:
        return Assessment(
            "review",
            "square/tall figure tends to take a large vertical block in PDF",
            "keep only when equal axes are essential; otherwise prefer about (6, 4)",
            rendered,
        )

    if rendered.height >= image_box.height * 0.98 and size.height >= 4:
        return Assessment(
            "ok-large",
            "height-limited by the export box; visually prominent but predictable",
            "leave as-is unless it feels page-dominant, then reduce figure height",
            rendered,
        )

    return Assessment(
        "ok",
        "fits the compact export pattern",
        "no change needed",
        rendered,
    )


def relative_to(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def fmt_size(size: FigureSize) -> str:
    return f"({size.width:g}, {size.height:g})"


def print_report(
    findings: list[Finding],
    image_box: FigureSize,
    repo_root: Path,
    *,
    show_all: bool,
    limit: int | None,
) -> int:
    pattern_counts = Counter((f.figsize.width, f.figsize.height) for f in findings)
    assessments = [(finding, assess(finding, image_box)) for finding in findings]
    visible = [item for item in assessments if show_all or item[1].severity not in {"ok", "ok-large"}]
    if limit is not None:
        visible = visible[:limit]

    print("Figsize lint")
    print(f"  Findings: {len(findings)}")
    print(f"  PDF image box: {image_box.width:g}in x {image_box.height:g}in")
    print()

    print("Most common figsize patterns:")
    for (width, height), count in pattern_counts.most_common(12):
        aspect = width / height if height else math.inf
        print(f"  {count:>3}x  ({width:g}, {height:g})  aspect {aspect:.2f}")
    print()

    if not visible:
        print("No figure sizes need review under the current rule set.")
        return 0

    print("Figures to review/change:")
    for finding, assessment in visible:
        path_label = relative_to(finding.notebook, repo_root)
        shape = ""
        if finding.rows is not None and finding.columns is not None:
            shape = f", layout {finding.rows}x{finding.columns}"
        resolved = f", via {finding.resolved_from}" if finding.resolved_from else ""
        print(f"- {assessment.severity.upper()} {path_label}")
        print(
            f"  Cell {finding.cell_number}, line {finding.line_number}: "
            f"{fmt_size(finding.figsize)}, aspect {finding.figsize.aspect:.2f}{shape}{resolved}"
        )
        print(
            f"  Renders about {assessment.rendered_size.width:.2f}in x "
            f"{assessment.rendered_size.height:.2f}in in the current PDF box"
        )
        print(f"  Why: {assessment.reason}")
        print(f"  Suggest: {assessment.suggestion}")
        if finding.source_line:
            print(f"  Source: {finding.source_line[:150]}")
    print()

    counts = Counter(assessment.severity for _, assessment in assessments)
    print("Assessment summary:")
    for severity in ("change", "review", "ok-large", "ok"):
        if counts[severity]:
            print(f"  {severity}: {counts[severity]}")
    return counts["change"] + counts["review"]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lint Matplotlib figsize values in notebook code cells.",
    )
    parser.add_argument(
        "--source-dir",
        default=DEFAULT_SOURCE_DIR,
        help=f"Notebook root to scan (default: {DEFAULT_SOURCE_DIR})",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Export profile used to estimate PDF image size",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show OK and OK-large figures as well as review/change findings",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of detailed findings to print",
    )
    parser.add_argument(
        "--show-parse-errors",
        action="store_true",
        help="Print code cells skipped because they are not valid Python syntax",
    )
    parser.add_argument(
        "--fail-on-warnings",
        action="store_true",
        help="Exit non-zero when any change/review findings are present",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    source_dir = Path(args.source_dir)
    if not source_dir.is_absolute():
        source_dir = repo_root / source_dir

    if not source_dir.is_dir():
        print(f"ERROR: Source directory not found: {source_dir}", file=sys.stderr)
        return 1

    image_box, profile_path = load_image_box(repo_root, args.config)
    notebooks = iter_notebooks(source_dir)
    findings: list[Finding] = []
    for notebook in notebooks:
        findings.extend(extract_findings(notebook, show_parse_errors=args.show_parse_errors))

    if profile_path is not None:
        print(f"Profile: {relative_to(profile_path, repo_root)}")
    else:
        print("Profile: built-in image box fallback")

    warning_count = print_report(
        findings,
        image_box,
        repo_root,
        show_all=args.all,
        limit=args.limit,
    )
    if args.fail_on_warnings and warning_count:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())