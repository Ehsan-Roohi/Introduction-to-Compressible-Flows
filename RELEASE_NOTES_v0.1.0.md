# Release notes — v0.1.0

Initial public computational companion for *Introduction to Compressible Flows*.

## Included

- nine chapter-linked notebooks spanning Chapters 4, 6, 7, 8, and 10;
- direct GitHub and Google Colab launch paths;
- chapter metadata, learning objectives, model scope, and interpretation checks in every notebook;
- deterministic default examples and portable output paths;
- `START_HERE.md`, citation metadata, contribution rules, security guidance, and scientific-discrepancy reporting;
- automated notebook-contract validation across Python 3.10–3.12; and
- representative numerical smoke tests for seven fast notebooks.

## Audited corrections and reproducibility improvements

- corrected the nondimensional velocity exponent used to initialize one Taylor–Maccoll integration (`-1/2` rather than `-0.05`);
- corrected the normal-shock Mach relation denominator in the interacting-oblique-shock solver (`gamma + 1` rather than `gamma + 2`);
- corrected a dimensionless pressure-ratio output label;
- removed stale notebook outputs and execution counts;
- replaced machine-specific `/mnt/data` output paths with a portable `outputs/` directory;
- made Rayleigh-flow neural-network initialization deterministic; and
- reduced the default conical-flow sweep to a documented teaching resolution while retaining explicit refinement guidance.

The original manuscript files are not included in this public software repository.
