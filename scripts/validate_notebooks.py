"""Validate the public notebook contract without third-party packages."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

from prepare_notebooks import NOTEBOOKS, ROOT


COLAB_PREFIX = (
    "https://colab.research.google.com/github/"
    "Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/"
)


def text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def validate_notebook(relative_path: str, specification: dict) -> list[str]:
    errors: list[str] = []
    path = ROOT / relative_path
    if not path.exists():
        return [f"missing notebook: {relative_path}"]

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read {relative_path}: {exc}"]

    cells = notebook.get("cells", [])
    if notebook.get("nbformat") != 4:
        errors.append("nbformat must be 4")
    if len(cells) < 3:
        errors.append("must contain an introduction, code, and interpretation guide")

    ids = [cell.get("id") for cell in cells]
    if any(not value for value in ids):
        errors.append("every cell must have an id")
    if len(ids) != len(set(ids)):
        errors.append("cell ids must be unique")

    if cells:
        first = cells[0]
        first_text = text(first)
        if first.get("cell_type") != "markdown":
            errors.append("first cell must be Markdown")
        if f"# {specification['title']}" not in first_text:
            errors.append("first cell is missing the canonical title")
        if f"**Chapter {specification['chapter']}:**" not in first_text:
            errors.append("first cell is missing the chapter association")
        expected_colab = COLAB_PREFIX + relative_path
        if expected_colab not in first_text:
            errors.append("first cell is missing the canonical Colab link")

        last = cells[-1]
        if last.get("cell_type") != "markdown" or "Interpretation and verification checklist" not in text(last):
            errors.append("last cell must contain the interpretation checklist")

    markdown_count = sum(cell.get("cell_type") == "markdown" for cell in cells)
    code_count = sum(cell.get("cell_type") == "code" for cell in cells)
    if markdown_count < 2:
        errors.append("requires at least two Markdown cells")
    if code_count < 1:
        errors.append("requires at least one code cell")

    forbidden_paths = ("/mnt/data", "C:\\\\Users\\\\", "C:/Users/")
    for index, cell in enumerate(cells, start=1):
        source = text(cell)
        if any(value in source for value in forbidden_paths):
            errors.append(f"cell {index} contains a machine-specific absolute path")
        if cell.get("cell_type") != "code":
            continue
        if cell.get("execution_count") is not None:
            errors.append(f"cell {index} has a committed execution count")
        if cell.get("outputs"):
            errors.append(f"cell {index} has committed outputs")
        try:
            ast.parse(source, filename=f"{relative_path}#cell-{index}")
        except SyntaxError as exc:
            errors.append(f"cell {index} has invalid Python syntax: {exc.msg} (line {exc.lineno})")

    metadata = notebook.get("metadata", {})
    kernelspec = metadata.get("kernelspec", {})
    if kernelspec.get("name") != "python3":
        errors.append("kernelspec must be python3")
    book_metadata = metadata.get("compressible_flows", {})
    if book_metadata.get("chapter") != specification["chapter"]:
        errors.append("machine-readable chapter metadata is incorrect")
    if book_metadata.get("chapter_title") != specification["chapter_title"]:
        errors.append("machine-readable chapter title is incorrect")

    return errors


def validate_repository_links() -> list[str]:
    errors: list[str] = []
    for markdown_path in (ROOT / "README.md", ROOT / "START_HERE.md", ROOT / "notebooks" / "README.md"):
        source = markdown_path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source):
            if target.startswith(("http://", "https://", "mailto:")) or target.startswith("#"):
                continue
            local_target = (markdown_path.parent / target.split("#", 1)[0]).resolve()
            if not local_target.exists():
                errors.append(f"broken local link in {markdown_path.relative_to(ROOT)}: {target}")
    return errors


def main() -> int:
    failures: list[str] = []
    discovered = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "notebooks").rglob("*.ipynb")
        if ".ipynb_checkpoints" not in path.parts
    }
    expected = set(NOTEBOOKS)
    for unexpected in sorted(discovered - expected):
        failures.append(f"unexpected unregistered notebook: {unexpected}")
    for missing in sorted(expected - discovered):
        failures.append(f"registered notebook is missing: {missing}")

    for relative_path, specification in NOTEBOOKS.items():
        notebook_errors = validate_notebook(relative_path, specification)
        if notebook_errors:
            failures.extend(f"{relative_path}: {message}" for message in notebook_errors)
        else:
            print(f"PASS {relative_path}")

    failures.extend(validate_repository_links())
    if failures:
        print("\nNotebook validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nValidated {len(expected)} notebooks and repository-local documentation links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
