"""Execute the fast deterministic notebooks as a numerical smoke test."""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FAST_NOTEBOOKS = [
    "notebooks/chapter06/06_01_emanuel_oblique_shock.ipynb",
    "notebooks/chapter06/06_02_shock_polar.ipynb",
    "notebooks/chapter06/06_03_oblique_shock_collision_slip_line.ipynb",
    "notebooks/chapter07/07_01_shock_tube_pressure_solver.ipynb",
    "notebooks/chapter07/07_02_interacting_shock_pressure_ratios.ipynb",
    "notebooks/chapter08/08_normal_shock_location_cd_nozzle.ipynb",
    "notebooks/chapter10/10_01_conical_flow_from_shock_angle.ipynb",
]


def source_text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def execute_notebook(relative_path: str) -> str:
    notebook = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    module_name = "notebook_smoke_" + relative_path.replace("/", "_").replace(".", "_")
    module = types.ModuleType(module_name)
    module.__file__ = str(ROOT / relative_path)
    namespace = module.__dict__
    sys.modules[module_name] = module
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            for index, cell in enumerate(notebook["cells"], start=1):
                if cell.get("cell_type") != "code":
                    continue
                source = source_text(cell)
                exec(compile(source, f"{relative_path}#cell-{index}", "exec"), namespace)
    finally:
        sys.modules.pop(module_name, None)
    return output.getvalue()


def main() -> int:
    original_directory = Path.cwd()
    os.environ.setdefault("MPLBACKEND", "Agg")
    matplotlib_config = ROOT / ".mplconfig"
    matplotlib_config.mkdir(mode=0o777, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(matplotlib_config))
    generated_files = [ROOT / "R_phi_polar_90_180.png"]
    try:
        os.chdir(ROOT)
        for relative_path in FAST_NOTEBOOKS:
            output = execute_notebook(relative_path)
            print(f"PASS {relative_path} ({len(output)} captured characters)")
    finally:
        os.chdir(original_directory)
        for generated_file in generated_files:
            generated_file.unlink(missing_ok=True)
    print(f"\nExecuted {len(FAST_NOTEBOOKS)} fast deterministic notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
