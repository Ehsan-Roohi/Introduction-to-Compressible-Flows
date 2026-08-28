"""Normalize and document the public notebook set.

This script is intentionally standard-library only.  It adds a consistent
teaching header and interpretation guide, clears stale execution state, applies
a few audited portability/correctness fixes, and records machine-readable book
chapter metadata.  Running it repeatedly is safe.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Ehsan-Roohi/Introduction-to-Compressible-Flows"


NOTEBOOKS = {
    "notebooks/chapter04/04_rayleigh_flow_ai_solver.ipynb": {
        "chapter": 4,
        "chapter_title": "One-Dimensional Flow with Heat Transfer (Rayleigh Flow)",
        "title": "Interactive Rayleigh-Flow Solver with an ML Inverse Surrogate",
        "concepts": [
            "Rayleigh-star property ratios",
            "heat-addition choking",
            "subsonic and supersonic branches",
            "ML inverse surrogate versus an analytical baseline",
        ],
        "objectives": [
            "Compute Rayleigh-flow property ratios relative to the sonic state.",
            "Determine whether a prescribed heat input chokes the flow.",
            "Compare a learned inverse map with a branch-aware bisection solution.",
            "Interpret temperature, pressure, density, velocity, and stagnation-pressure changes.",
        ],
        "run_note": "Run the single code cell, wait for the three small neural networks to train, then move the four sliders.",
        "limitations": "The neural networks are surrogates trained on exact Rayleigh relations; they do not add new governing physics and must be judged against the analytical result shown in every valid case.",
        "checks": [
            "For heat addition, both subsonic and supersonic branches should move toward Mach 1.",
            "The reported maximum heat input marks the sonic limit for the selected inlet state.",
            "Treat the exact bisection result—not the smoother ML curve—as the reference.",
        ],
    },
    "notebooks/chapter06/06_01_emanuel_oblique_shock.ipynb": {
        "chapter": 6,
        "chapter_title": "Oblique Shock Waves and Expansion Waves",
        "title": "Weak and Strong Oblique-Shock Angles by Emanuel's Explicit Method",
        "concepts": ["theta-beta-Mach relation", "weak and strong shock branches", "shock detachment"],
        "objectives": [
            "Evaluate the explicit cubic solution for the shock angle.",
            "Distinguish weak and strong attached-shock branches.",
            "Detect inputs beyond the attached-shock limit.",
        ],
        "run_note": "Edit the worked-example Mach number, turning angle, or heat-capacity ratio in the final lines of the code cell and rerun it.",
        "limitations": "The method assumes a calorically perfect gas and an attached, two-dimensional oblique shock.",
        "checks": [
            "The weak-shock angle must lie between the Mach angle and the strong-shock angle.",
            "As the turning angle approaches zero, the weak branch approaches the Mach angle.",
            "A detached-shock message is a physical-domain result, not a numerical failure.",
        ],
    },
    "notebooks/chapter06/06_02_shock_polar.ipynb": {
        "chapter": 6,
        "chapter_title": "Oblique Shock Waves and Expansion Waves",
        "title": "Shock-Polar Diagram Across Upstream Mach Number",
        "concepts": ["shock polar", "velocity-space construction", "Mach-number dependence"],
        "objectives": [
            "Construct a family of shock polars for air at a prescribed temperature.",
            "Visualize how the admissible post-shock velocity locus changes with Mach number.",
            "Export a publication-quality polar plot for further interpretation.",
        ],
        "run_note": "Run the code cell; it writes `R_phi_polar_90_180.png` in the current working directory.",
        "limitations": "The plot uses a perfect-gas model with fixed gamma and temperature and is intended as a geometric teaching aid.",
        "checks": [
            "Confirm that every curve uses the same angular interval and thermodynamic constants.",
            "Relate intersections with a turning direction to admissible weak/strong solutions.",
            "Do not compare radial magnitudes across changed unit systems without recomputing the speed of sound.",
        ],
    },
    "notebooks/chapter06/06_03_oblique_shock_collision_slip_line.ipynb": {
        "chapter": 6,
        "chapter_title": "Oblique Shock Waves and Expansion Waves",
        "title": "Head-On Collision of Oblique Shocks and Slip-Line Matching",
        "concepts": ["interacting oblique shocks", "pressure compatibility", "slip-line angle", "root finding"],
        "objectives": [
            "Propagate the upper and lower incident shocks through two downstream states.",
            "Enforce equal static pressure across the slip line.",
            "Compare a bracketed hybrid root solve with a deliberately slow reference iteration.",
        ],
        "run_note": "Run the fast solver cell for the deterministic example. The final cell retains the slow reference algorithm as an optional function and does not run automatically.",
        "limitations": "The construction assumes attached shocks, a perfect gas, and an inviscid slip line; inputs outside the attached-shock domain can be nonphysical.",
        "checks": [
            "The converged pressure mismatch |P4-P5| should satisfy the declared tolerance.",
            "Verify that every intermediate normal Mach number is supersonic before applying an oblique-shock relation.",
            "Report both the sign convention and magnitude of the slip-line angle.",
        ],
    },
    "notebooks/chapter07/07_01_shock_tube_pressure_solver.ipynb": {
        "chapter": 7,
        "chapter_title": "Unsteady Wave Motion",
        "title": "Shock-Tube Pressure and State Solver",
        "concepts": ["shock tube", "incident-shock Mach number", "contact-surface matching", "expansion region"],
        "objectives": [
            "Solve the driver/driven pressure matching equation.",
            "Recover incident-shock speed and the states behind the shock and expansion.",
            "Check velocity and pressure compatibility across the contact surface.",
        ],
        "run_note": "Edit the driver/driven pressures and temperatures near the top of the code cell, then run it.",
        "limitations": "The example assumes equal perfect gases on both sides, constant specific heats, and one-dimensional inviscid motion.",
        "checks": [
            "The solved p2/p1 must remain inside the root bracket; widen the bracket only with a physical justification.",
            "Regions 2 and 3 share velocity and pressure across the contact surface.",
            "Pressure and density ratios are dimensionless; wave and particle velocities use m/s.",
        ],
    },
    "notebooks/chapter07/07_02_interacting_shock_pressure_ratios.ipynb": {
        "chapter": 7,
        "chapter_title": "Unsteady Wave Motion",
        "title": "Pressure Ratio After Interacting Shock Waves",
        "concepts": ["shock interaction", "implicit pressure matching", "Brent root solve"],
        "objectives": [
            "Form the nonlinear compatibility equation for sequential shocks.",
            "Solve for the final pressure ratio with a robust bracketed method.",
            "Trace local pressure ratios into a global p5/p1 value.",
        ],
        "run_note": "Set p2/p1 and p3/p2 in the parameter block and run the cell.",
        "limitations": "The implemented relation is specialized to the pressure-ratio configuration derived in Chapter 7 and assumes a perfect gas.",
        "checks": [
            "Confirm that the chosen root bracket contains a sign change.",
            "Recompute p1/p2 and p1/p3 whenever either prescribed ratio changes.",
            "Check that all returned pressure ratios are positive.",
        ],
    },
    "notebooks/chapter08/08_normal_shock_location_cd_nozzle.ipynb": {
        "chapter": 8,
        "chapter_title": "Quasi-One-Dimensional Flow in Converging-Diverging Nozzles",
        "title": "Normal-Shock Location in a Converging-Diverging Nozzle",
        "concepts": ["area-Mach relation", "nozzle choking", "normal-shock total-pressure loss", "shock location"],
        "objectives": [
            "Check whether the nozzle is choked for the prescribed back pressure.",
            "Infer the subsonic exit Mach number and total-pressure loss.",
            "Invert the normal-shock relation and report the shock area ratio As/At.",
        ],
        "run_note": "Edit the reservoir pressure, back pressure, exit-to-throat area ratio, and gamma in the worked example and run the cell.",
        "limitations": "The result locates the shock by area ratio in a quasi-one-dimensional, adiabatic, perfect-gas nozzle; converting As/At to an axial coordinate requires the nozzle geometry A(x).",
        "checks": [
            "An internal normal shock is considered only after the choking test passes.",
            "The pre-shock Mach number must be supersonic and the post-shock Mach number subsonic.",
            "Total pressure must decrease across the shock, so p02/p01 lies between zero and one.",
        ],
    },
    "notebooks/chapter10/10_01_conical_flow_from_shock_angle.ipynb": {
        "chapter": 10,
        "chapter_title": "Conical Flow",
        "title": "Taylor-Maccoll Integration from a Prescribed Shock Angle",
        "concepts": ["conical shock", "Taylor-Maccoll equation", "Runge-Kutta integration", "cone-surface condition"],
        "objectives": [
            "Initialize the conical-flow state immediately behind an oblique shock.",
            "Integrate the Taylor-Maccoll system from the shock toward the cone.",
            "Locate the cone surface where the tangential velocity vanishes.",
        ],
        "run_note": "Edit the free-stream Mach number and shock angle in the deterministic example at the bottom of the code cell, then rerun it.",
        "limitations": "The solver assumes steady axisymmetric flow over a sharp cone at zero angle of attack with a calorically perfect gas.",
        "checks": [
            "The prescribed shock angle must exceed the Mach angle asin(1/Minf).",
            "Reduce the angular step and tolerance together to check numerical convergence.",
            "Confirm that the reported cone angle is smaller than the shock angle.",
        ],
    },
    "notebooks/chapter10/10_02_taylor_maccoll_cone_sweep.ipynb": {
        "chapter": 10,
        "chapter_title": "Conical Flow",
        "title": "Cone Shock-Angle Search and Taylor-Maccoll Property Sweep",
        "concepts": ["cone-angle/shock-angle relation", "event-driven ODE integration", "surface Mach number", "surface pressure"],
        "objectives": [
            "Search for the shock angle associated with a prescribed cone half-angle.",
            "Integrate the Taylor-Maccoll equations with a cone-surface event.",
            "Map free-stream Mach number to surface Mach and pressure ratio.",
        ],
        "run_note": "The first cell defines an optional interactive shock-angle tool. The next cell performs the deterministic 10-degree cone sweep; the last cell saves its two figures under `outputs/`.",
        "limitations": "The beta sweep is a transparent teaching search rather than an optimized production solver; refine the sweep and ODE tolerances before using it as reference data.",
        "checks": [
            "Repeat the sweep with a finer beta grid and verify that the selected curves are stable.",
            "Reject states with nonpositive nondimensional sound-speed squared.",
            "Record cone angle, gamma, sweep resolution, and ODE tolerances with any reported curve.",
        ],
    },
}


def cell_id(path: str, role: str) -> str:
    digest = hashlib.sha1(f"{path}:{role}".encode()).hexdigest()[:10]
    return f"{role}-{digest}"


def markdown_cell(path: str, role: str, source: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id(path, role),
        "metadata": {"tags": [f"generated-{role}"]},
        "source": source.strip() + "\n",
    }


def source_text(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def patch_code(path: str, source: str, cell_number: int) -> str:
    if path.endswith("04_rayleigh_flow_ai_solver.ipynb"):
        source = source.replace("Physics-Informed", "Physics-Guided")
        source = source.replace("tol=1e-7)", "tol=1e-7, random_state=42)")

    if path.endswith("06_01_emanuel_oblique_shock.ipynb"):
        source = source.split("\n# Reproducible worked example", 1)[0]
        source = source.split('\nif __name__ == "__main__":', 1)[0]
        source += '''\n\n# Reproducible worked example\nM1_example = 2.0\ntheta_example_deg = 10.0\nbeta_w, beta_s, message = obliqueshock_emanuel(M1_example, theta_example_deg)\nprint(f"M1 = {M1_example:.2f}, theta = {theta_example_deg:.2f} deg")\nprint(f"weak beta = {beta_w:.4f} deg, strong beta = {beta_s:.4f} deg")\nprint(message)\n'''

    if path.endswith("06_03_oblique_shock_collision_slip_line.ipynb"):
        source = source.replace("(gamma - 1.0) / (gamma + 2.0)", "(gamma - 1.0) / (gamma + 1.0)")
        source = source.replace("(gamma - 1) / (gamma + 2)", "(gamma - 1) / (gamma + 1)")
        if cell_number == 1:
            source = source.split("\n# Reproducible worked example", 1)[0]
            source = source.split('\nif __name__ == "__main__":', 1)[0]
            source += '''\n\n# Reproducible worked example\nexample = solve_slipline_fast(\n    M1=3.0,\n    theta2=math.radians(8.0),\n    theta3=math.radians(12.0),\n    P1=1.0,\n)\nprint(f"P4 = {example['P4']:.6f}, P5 = {example['P5']:.6f}")\nprint(f"|P4-P5| = {abs(example['P4_minus_P5']):.3e}")\nprint(f"slip-line angle = {example['slip_line_angle_deg']:.6f} deg")\n'''
        elif cell_number == 2:
            source = source.split("\n# Optional: call slow_reference_demo()", 1)[0]
            source = source.replace("def main():", "def slow_reference_demo():")
            source = source.split('\nif __name__ == "__main__":', 1)[0]
            source += "\n\n# Optional: call slow_reference_demo() to reproduce the original incremental iteration.\n"

    if path.endswith("07_01_shock_tube_pressure_solver.ipynb"):
        source = source.replace('print(f" pressure ratio p3_p4 = {p3_p4:.2f} m/s")', 'print(f" Pressure ratio p3/p4 = {p3_p4:.4f}")')

    if path.endswith("08_normal_shock_location_cd_nozzle.ipynb"):
        source = source.replace("Textbook Equation (7-85)", "Chapter 8 explicit exit-Mach relation")
        source = source.replace("Textbook Equation (7-85):", "Chapter 8 explicit exit-Mach relation:")
        source = source.split("\n# Reproducible worked example", 1)[0]
        source = source.split('\nif __name__ == "__main__":', 1)[0]
        source += '''\n\n# Reproducible worked example\nP01 = 500_000.0       # Pa\npe = 150_000.0        # Pa\nAe_At = 2.5\ngamma = 1.4\n\nif pe / P01 >= critical_pressure_ratio(gamma):\n    print("Flow is not choked; no internal normal-shock solution is reported.")\nelse:\n    As_At, M1, M2, Me, p02p01 = solve_shock_location_textbook(P01, pe, Ae_At, gamma)\n    print(f"exit Mach Me = {Me:.6f}")\n    print(f"pre-/post-shock Mach = {M1:.6f} / {M2:.6f}")\n    print(f"total-pressure ratio p02/p01 = {p02p01:.6f}")\n    print(f"shock location As/At = {As_At:.6f}")\n'''

    if path.endswith("10_01_conical_flow_from_shock_angle.ipynb"):
        source = source.replace("** (-0.05)", "** (-0.5)")
        source = source.split("\n# Reproducible worked example", 1)[0]
        source = source.split('\nif __name__ == "__main__":', 1)[0]
        source += '''\n\n# Reproducible worked example\nresult, history = cone_mach_project(\n    Minf=2.0,\n    beta_deg=40.0,\n    h=0.001,\n    y2_tol=1e-4,\n    store_history=True,\n)\nprint(f"shock angle beta = {result.beta_deg:.4f} deg")\nprint(f"cone angle theta_c = {result.thetaC_deg:.4f} deg")\nprint(f"post-shock Mach M2 = {result.M2:.6f}")\nprint(f"iterations = {result.iterations}")\n'''

    if path.endswith("10_02_taylor_maccoll_cone_sweep.ipynb"):
        source = source.replace('\nif __name__ == "__main__":\n    conical_flow()\n', '\n# Optional interactive use: call conical_flow().\n')
        source = source.replace("np.sign(den)*1e-8", "np.copysign(1e-8, den if den != 0 else 1.0)")
        source = source.replace("except:\n            pass", "except (FloatingPointError, ValueError, ZeroDivisionError):\n            pass")
        if cell_number == 2:
            source = source.replace("M1_range = np.linspace(1.1, 3, 40)", "M1_range = np.linspace(1.1, 3, 20)")
            source = source.replace("        3000\n", "        160\n")
        if cell_number == 3:
            source = '''from pathlib import Path\nimport matplotlib.pyplot as plt\n\noutput_dir = Path("outputs")\noutput_dir.mkdir(exist_ok=True)\n\nplot1 = output_dir / "mach_vs_surface.png"\nplt.figure(figsize=(8, 5))\nplt.plot(M1_values, M_surface_values, "bo-", linewidth=2)\nplt.xlabel("Free-stream Mach number M1")\nplt.ylabel("Surface Mach number")\nplt.title("Surface Mach Number vs Free-stream Mach Number")\nplt.grid(True)\nplt.savefig(plot1, dpi=300, bbox_inches="tight")\nplt.show()\n\nplot2 = output_dir / "pressure_ratio.png"\nplt.figure(figsize=(8, 5))\nplt.plot(M1_values, pressure_values, "rs-", linewidth=2)\nplt.xlabel("Free-stream Mach number M1")\nplt.ylabel("Pressure ratio ps/p1")\nplt.title("Surface Pressure Ratio vs Free-stream Mach Number")\nplt.grid(True)\nplt.savefig(plot2, dpi=300, bbox_inches="tight")\nplt.show()\n\nprint(plot1.resolve())\nprint(plot2.resolve())\n'''

    return source.rstrip() + "\n"


def intro_markdown(path: str, spec: dict) -> str:
    colab = f"https://colab.research.google.com/github/{REPOSITORY}/blob/main/{path}"
    concepts = " · ".join(spec["concepts"])
    objectives = "\n".join(f"- {item}" for item in spec["objectives"])
    return f'''<a href="{colab}" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a>

# {spec['title']}

**Book:** *Introduction to Compressible Flows*<br>
**Chapter {spec['chapter']}:** {spec['chapter_title']}<br>
**Concepts:** {concepts}

## Learning objectives

{objectives}

## How to use this notebook

{spec['run_note']}

> **Model scope.** {spec['limitations']}
'''


def guide_markdown(spec: dict) -> str:
    checks = "\n".join(f"- {item}" for item in spec["checks"])
    return f'''## Interpretation and verification checklist

{checks}

## Reproducibility note

Restart the runtime and run the notebook from top to bottom after changing inputs. Record the input values, units, heat-capacity ratio, numerical tolerances, and dependency versions with any result used in coursework, research, or a publication.

Questions or reproducibility reports are welcome through the repository's issue templates.
'''


def prepare(path: str, spec: dict) -> None:
    notebook_path = ROOT / path
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    original_cells = []
    for cell in notebook.get("cells", []):
        tags = cell.get("metadata", {}).get("tags", [])
        if "generated-intro" in tags or "generated-guide" in tags:
            continue
        if cell.get("cell_type") == "code" and not source_text(cell).strip():
            continue
        original_cells.append(cell)

    code_number = 0
    for index, cell in enumerate(original_cells):
        if "id" not in cell:
            cell["id"] = cell_id(path, f"cell-{index + 1}")
        if cell.get("cell_type") == "code":
            code_number += 1
            cell["source"] = patch_code(path, source_text(cell), code_number)
            cell["execution_count"] = None
            cell["outputs"] = []

    notebook["cells"] = [
        markdown_cell(path, "intro", intro_markdown(path, spec)),
        *original_cells,
        markdown_cell(path, "guide", guide_markdown(spec)),
    ]
    notebook["nbformat"] = 4
    notebook["nbformat_minor"] = max(5, notebook.get("nbformat_minor", 0))
    metadata = notebook.setdefault("metadata", {})
    metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    metadata["language_info"] = {"name": "python", "version": "3.12"}
    metadata["compressible_flows"] = {
        "book": "Introduction to Compressible Flows",
        "chapter": spec["chapter"],
        "chapter_title": spec["chapter_title"],
        "title": spec["title"],
        "concepts": spec["concepts"],
    }
    notebook_path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    for path, spec in NOTEBOOKS.items():
        prepare(path, spec)
        print(f"prepared {path}")


if __name__ == "__main__":
    main()
