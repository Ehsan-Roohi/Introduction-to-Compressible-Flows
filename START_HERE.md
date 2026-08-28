# Start here

This page is the shortest reliable path from a fresh browser to a meaningful compressible-flow result.

## 1. Choose a starting point

| Your goal | Start with | Why |
| --- | --- | --- |
| Review heat addition and choking | [Chapter 4 Rayleigh-flow solver](notebooks/chapter04/04_rayleigh_flow_ai_solver.ipynb) | Interactive property curves with an analytical reference beside the learned inverse map |
| Learn oblique-shock branches | [Chapter 6 Emanuel method](notebooks/chapter06/06_01_emanuel_oblique_shock.ipynb) | Short, deterministic weak/strong-shock calculation |
| Study unsteady waves | [Chapter 7 shock tube](notebooks/chapter07/07_01_shock_tube_pressure_solver.ipynb) | Connects pressure matching to shock speed and thermodynamic states |
| Locate a shock in a nozzle | [Chapter 8 nozzle notebook](notebooks/chapter08/08_normal_shock_location_cd_nozzle.ipynb) | A transparent choking → exit state → shock loss → area-ratio workflow |
| Study three-dimensional supersonic flow | [Chapter 10 Taylor–Maccoll integration](notebooks/chapter10/10_01_conical_flow_from_shock_angle.ipynb) | Integrates from an attached conical shock to the cone surface |

Use the complete [Colab launcher](notebooks/README.md) for all nine notebooks.

## 2. Run in Colab or locally

For the fastest start, click the Colab badge inside a notebook. For local work:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

## 3. Use the learning loop

Every notebook follows the same scientific loop:

**predict → calculate → check admissibility → compare → interpret → record**

Before running, predict the direction of the Mach-number, pressure, or temperature change. After running, verify at least one limit or conservation statement. A converged number is not automatically a physically admissible result.

## 4. Recommended sequence

1. Chapter 4: Rayleigh flow and thermal choking.
2. Chapter 6: Emanuel's explicit method, shock polar, then interacting shocks.
3. Chapter 7: shock tube, then interacting-wave pressure ratios.
4. Chapter 8: quasi-one-dimensional nozzle with an internal normal shock.
5. Chapter 10: prescribed-shock Taylor–Maccoll integration, then the cone-property sweep.

The sequence is conceptual rather than mandatory. Readers may jump directly to the chapter accompanying their book study.

## 5. Runtime expectations

Most deterministic notebooks run in seconds on a CPU. The Chapter 4 notebook trains three small scikit-learn networks and may take one to several minutes. The Chapter 10 cone sweep performs many ODE integrations and is intentionally slower; first use the default teaching resolution, then refine it for a convergence study.

## 6. Minimum record for a reusable result

Save the following with any figure, table, or reported value:

- repository version or commit;
- notebook path;
- all dimensional inputs and units;
- heat-capacity ratio and gas model;
- numerical tolerances, angular step, or sweep resolution;
- Python and package versions; and
- the physical admissibility checks you performed.

If a result appears inconsistent with the book, use the **Scientific discrepancy** issue template and include the complete record above.
