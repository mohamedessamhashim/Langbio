# Langbio

Langbio is a Python library for multiscale computational biology. It aims to provide a small
set of simple, composable, white-box building blocks that stay biologically correct by
construction (units, conservation, non-negativity, volume coupling) and scale from molecules
to tissues.

**Status: pre-alpha.** There is no public API yet. The first goal is to replicate experiments
from the Spatio-Flux example of Agmon & Spangler, "Process bigraphs and the architecture of
compositional systems biology", *PLoS Comput Biol* 22(10): e1014819 (2026), and to compare
outputs and runtime with the original code.

## Development setup

Requires Python 3.12 or newer. Every dependency is installed into a virtual environment and
pinned in a requirements file; nothing is installed system-wide.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pip install --no-deps --no-build-isolation -e .
```

## Checks

```bash
.venv/bin/pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
.venv/bin/mypy
diff <(.venv/bin/pip freeze --exclude-editable) requirements-dev.txt   # must print nothing
```

## Dependencies

| File | Role |
|---|---|
| `pyproject.toml` | The version *ranges* Langbio supports. Runtime dependencies are `numpy` and `scipy` only. |
| `requirements.txt` | Exact runtime versions used in this repository. |
| `requirements-dev.txt` | Exact versions of everything in `.venv`, including transitive dependencies and the build backend. Generated, not hand-edited. |

After adding or upgrading a dependency (which first needs a logged decision), regenerate both:

```bash
.venv/bin/pip freeze --exclude-editable > requirements-dev.txt
grep -E '^(numpy|scipy)==' requirements-dev.txt > requirements.txt
```

## Conventions

- `src` layout; build backend `hatchling`.
- Type hints and docstrings on all public names. Docstrings are numpy-style and state units in
  square brackets after the type, for example `D : float [µm²/s]`.
- `ruff` formats and lints; `mypy` type-checks `src/`; `pytest` runs `tests/`.
- Library tests live in `tests/`. Replication experiments live in `benchmarks/`, outside the
  library, and run the original code in a separate environment (see `benchmarks/README.md`).
- Parameters and model structure used for replication are cited to a paper section or to a
  source file and line. Nothing is invented.

## Layout

```
src/langbio/        the library
tests/              library tests
benchmarks/         replication experiments (not part of the library)
docs/DECISIONS.md   log of every design decision
docs/design/        CURRENT.md, the living design
papers/             the Process Bigraph paper and its two supplements
```

## Design and decisions

- [`docs/design/CURRENT.md`](docs/design/CURRENT.md): what has actually been decided.
- [`docs/DECISIONS.md`](docs/DECISIONS.md): date, decision, alternatives, reason, who decided.

## License

BSD-3-Clause. See [`LICENSE`](LICENSE).
