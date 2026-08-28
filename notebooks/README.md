# Notebook guide and one-click launcher

The notebooks are organized by the chapter numbering in *Introduction to Compressible Flows*. Open a file on GitHub for a static code view, or launch it in Google Colab for an executable copy.

| Chapter | Notebook | Interaction | Colab |
| --- | --- | --- | --- |
| 4 | [Rayleigh-flow AI inverse solver](chapter04/04_rayleigh_flow_ai_solver.ipynb) | Sliders; trains three small scikit-learn models | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter04/04_rayleigh_flow_ai_solver.ipynb) |
| 6 | [Emanuel oblique-shock method](chapter06/06_01_emanuel_oblique_shock.ipynb) | Edit deterministic example parameters | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter06/06_01_emanuel_oblique_shock.ipynb) |
| 6 | [Shock-polar diagram](chapter06/06_02_shock_polar.ipynb) | Generates a PNG figure | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter06/06_02_shock_polar.ipynb) |
| 6 | [Oblique-shock collision and slip line](chapter06/06_03_oblique_shock_collision_slip_line.ipynb) | Fast worked example; optional slow reference function | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter06/06_03_oblique_shock_collision_slip_line.ipynb) |
| 7 | [Shock-tube pressure solver](chapter07/07_01_shock_tube_pressure_solver.ipynb) | Edit parameter block | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter07/07_01_shock_tube_pressure_solver.ipynb) |
| 7 | [Interacting-shock pressure ratios](chapter07/07_02_interacting_shock_pressure_ratios.ipynb) | Edit pressure ratios | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter07/07_02_interacting_shock_pressure_ratios.ipynb) |
| 8 | [Normal-shock location in a C–D nozzle](chapter08/08_normal_shock_location_cd_nozzle.ipynb) | Edit worked-example nozzle state | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter08/08_normal_shock_location_cd_nozzle.ipynb) |
| 10 | [Taylor–Maccoll integration from shock angle](chapter10/10_01_conical_flow_from_shock_angle.ipynb) | Edit Mach and shock angle | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter10/10_01_conical_flow_from_shock_angle.ipynb) |
| 10 | [Cone shock-angle and property sweep](chapter10/10_02_taylor_maccoll_cone_sweep.ipynb) | Optional prompts plus deterministic ODE sweep | [Open](https://colab.research.google.com/github/Ehsan-Roohi/Introduction-to-Compressible-Flows/blob/main/notebooks/chapter10/10_02_taylor_maccoll_cone_sweep.ipynb) |

## Notebook contract

Every public notebook must have:

- a Colab badge and explicit chapter association;
- learning objectives, concepts, usage instructions, and model limitations;
- a deterministic default example or a clearly marked interactive entry point;
- no stale execution counts or committed outputs;
- no machine-specific absolute paths;
- valid Python syntax in every code cell; and
- an interpretation and verification checklist.

The continuous-integration workflow enforces this contract. Run `python scripts/validate_notebooks.py` from the repository root before contributing.
