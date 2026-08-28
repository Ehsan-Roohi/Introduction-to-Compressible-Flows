# Contributing

Corrections, reproducibility reports, documentation improvements, and well-scoped extensions are welcome.

## Before opening an issue

Use the matching issue form. Include the repository commit, notebook path, Python version, operating system, input values and units, `gamma`, numerical tolerances or sweep resolution, expected result, observed result, and complete traceback when applicable.

## Local checks

```bash
python -m pip install -r requirements.txt
python scripts/prepare_notebooks.py
python scripts/validate_notebooks.py
python scripts/smoke_test.py
```

## Scientific-change contract

- State the equation, assumption, or physical check motivating the change.
- Preserve units and the perfect-gas/model scope declared in the notebook.
- Compare numerical changes at tighter tolerance or resolution.
- Retain an analytical or conservation-law baseline when one exists.
- Explain changed outputs quantitatively; do not replace a result only because a new plot looks smoother.
- Keep manuscript files, unpublished student work, and restricted data out of this public repository.

## Pull requests

Keep each pull request focused. Explain the problem, change, validation performed, and remaining limitations. New dependencies require a clear reason. Generated outputs belong in the repository only when they are part of an explicitly declared reference result.

By contributing, you agree that your contribution is provided under the repository's MIT License.
