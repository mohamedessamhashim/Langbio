# Decisions

Every design decision is logged here: date, decision, alternatives considered, reason, and who
decided. "Owner" is the project owner. "Partner, approved by owner" means the engineering
partner proposed it and the owner approved it. Entries are never rewritten; a later decision
that changes an earlier one gets a new entry that names the one it replaces.

"Kickoff" refers to the project's kickoff design notes (with Appendix A and Appendix B), which
are kept outside this repository.

---

## D-0001 — 2026-11-11 — Engineering conventions

- **Decision:** `src` layout (`src/langbio/`), configured by `pyproject.toml` with `hatchling`,
  in a `.venv` virtual environment. Runtime dependencies start as `numpy` and `scipy` only;
  every other dependency, including a units library or JAX, is a design decision that needs a
  proposal. Dev tools: pytest, ruff (format and lint), mypy (lenient at first), ipykernel. Type
  hints and docstrings on all public names, with units stated in docstrings. `tests/` for
  library tests; `benchmarks/` for replication experiments, outside the library.
- **Alternatives:** none recorded.
- **Reason:** stated in the kickoff.
- **Decided by:** owner.

## D-0002 — 2026-11-11 — Replication standard and ground truth

- **Decision:** Replicating an experiment means: same model structure, parameters and initial
  conditions, each cited; matching outputs (within a stated tolerance for deterministic parts,
  statistically over seeds for stochastic parts); measured runtime at several sizes compared
  with the original, including the framework-overhead share where measurable; honest
  reporting, including where Langbio is worse. Ground truth comes from running the original
  code in a separate environment (`benchmarks/.venv-ref`) with pinned versions, with outputs
  saved to files that tests compare against. Parameters and model structure are never invented;
  they are cited to the papers or to the Spatio-Flux source (file and line).
- **Alternatives:** none recorded.
- **Reason:** stated in the kickoff.
- **Decided by:** owner.

## D-0003 — 2026-11-11 — License

- **Decision:** BSD-3-Clause, with the copyright line "Copyright (c) 2026, Langbio
  contributors".
- **Alternatives:** Apache-2.0 (explicit patent grant; the license of Spatio-Flux); MIT. For
  the copyright holder: the owner's own name, or an institution.
- **Reason:** BSD-3-Clause was the kickoff default and is the norm in scientific Python. A
  neutral holder keeps personal names out of the repository and can be changed later.
- **Decided by:** owner.

## D-0004 — 2026-11-11 — Python floor is 3.12

- **Decision:** `requires-python = ">=3.12"`. This replaces the kickoff's "Python ≥ 3.11".
- **Alternatives:** keep `>=3.11` and mark it untested.
- **Reason:** the development machine has only Python 3.12.3, so 3.11 could be declared but
  not tested; the current numpy (2.5.4) and scipy (1.18.1) releases already require 3.12.
- **Decided by:** owner, on partner's recommendation.

## D-0005 — 2026-11-11 — Assistant tooling is not named in the repository

- **Decision:** Tracked files and commit messages do not name any assistant tooling or its
  vendor, and commits carry no co-author or "generated with" line. The kickoff design notes
  and the session instruction file stay in the working directory but are never committed; they
  are listed in `.git/info/exclude`, not in `.gitignore`.
- **Alternatives:** commit an edited copy of the kickoff notes; exempt those two files.
- **Reason:** owner's preference. Accepted consequence: the working agreement and the design
  appendices are not in git history and do not travel with a clone.
- **Decided by:** owner.

## D-0006 — 2026-11-11 — Every dependency in a venv and a requirements file

- **Decision:** Nothing is installed system-wide. Every dependency lives in a virtual
  environment and is pinned to an exact version in a requirements file: `requirements.txt`
  (runtime), `requirements-dev.txt` (everything in `.venv`, including transitive dependencies
  and the build backend), and later `benchmarks/requirements-ref.txt` (the reference
  environment). `pyproject.toml` keeps the supported ranges.
- **Alternatives:** no lock for the development environment (the partner's first
  recommendation); a single hand-written requirements file with direct dependencies only.
- **Reason:** owner's instruction; makes each environment reproducible and checkable with
  `pip freeze`.
- **Decided by:** owner.

## D-0007 — 2026-11-11 — Setup choices

- **Decision:**
  1. Lower bounds `numpy>=2.0`, `scipy>=1.13` in `pyproject.toml`, no upper caps.
  2. The version is single-sourced from `src/langbio/__init__.py` through hatch.
  3. Ruff rule set `E, F, W, I, UP, B, NPY, D` with numpy-style docstrings, enforced on `src/`
     and waived in `tests/`; line length 100.
  4. Docstrings state units in a fixed slot: square brackets after the type, e.g.
     `D : float [µm²/s]`.
  5. The papers folder is `papers/` and the three PDFs are committed.
  6. One branch per step, named `step/NN-slug`. `main` is fast-forwarded only after the owner
     accepts the step report. The baseline commit (papers only) went straight to `main`.
  7. The build backend (`hatchling`, with the `editables` package its editable installs need)
     is installed in `.venv` and pinned; the editable install uses `--no-build-isolation`.
- **Alternatives:** (1) no bounds; (2) a static version in `pyproject.toml`; (3) ruff defaults;
  (4) free-text units; (5) keep `Papers/`, or leave the PDFs untracked; (6) partner merges each
  step without waiting; (7) pip's isolated temporary build environment.
- **Reason:** (1) one set of NumPy 2 type-promotion rules, and scipy 1.13 is the first release
  built for NumPy 2; (2) the package metadata and `langbio.__version__` cannot disagree;
  (3) enforcing docstrings is free while the codebase is empty; (4) units are findable by
  search; (5) the path named in the kickoff then exists, and the article is CC-BY; (6) the
  owner approves everything; (7) follows D-0006.
- **Decided by:** partner, approved by owner.

## D-0008 — 2026-11-11 — First replication target and ladder

- **Decision:** Replicate `brownian_particles` first (main paper Fig 7g–h; S2 §1.2.3, §1.2.5;
  S2 Table 3; `spatio_flux/composites/particles.py:22-54` at commit `99a4d59`). Then climb:
  1. `brownian_particles`
  2. `monod_kinetics`
  3. `ecoli_core_dfba`, then the Monod ↔ dFBA substitution
  4. `diffusion_process`, then `comets_diffusion`
  5. `br_particles_kinetics`, then `br_particles_dfba`
  6. `spatioflux_reference_demo`, then `reference_demo_x2y2`
- **Alternatives:** start with `monod_kinetics` (simpler and deterministic, exercises the
  conservation machinery, but has no size axis); start with the lattice dFBA comparison against
  COMETS (a published numeric target, but needs LPs and a much larger setup).
- **Reason:** it is the cheapest case for which the paper reports a framework overhead (61 %),
  so it tests the flat-array performance claim first; it has exact known answers (mean squared
  displacement 4·D·t, uniform long-time positions, binomial birth counts); and it builds the
  benchmark harness every later rung reuses. Each rung is split into steps of under ~200 lines,
  each with its own proposal.
- **Decided by:** partner, approved by owner.
