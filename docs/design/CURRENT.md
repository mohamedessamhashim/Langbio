# Current design

The living design: what has actually been decided. It may differ from the kickoff design notes
(Appendix A, the current proposal, and Appendix B, the original analysis), which are kept
outside this repository and are not binding. The owner's decisions override both.

Each item links to its entry in [`../DECISIONS.md`](../DECISIONS.md).

## Decided

| Topic | Decision | Entry |
|---|---|---|
| Packaging and tooling | `src` layout, `hatchling`, pytest, ruff, mypy; runtime dependencies `numpy` and `scipy` only | D-0001, D-0007 |
| Python | 3.12 or newer | D-0004 |
| Dependencies | Every one in a venv and pinned in a requirements file | D-0006 |
| License | BSD-3-Clause | D-0003 |
| Replication standard | Cited structure and parameters; matching outputs; measured runtime at several sizes; ground truth from the original code in a separate pinned environment | D-0002 |
| First target | `brownian_particles`, then a six-rung ladder up to the reference composite | D-0008 |
| Docstrings | numpy style, units in square brackets after the type | D-0007 |

Nothing about the library's own design is decided yet. There is no library code.

## Open

The kickoff proposes a direction. Each point below is still an open question, to be decided
only when a step needs it. The pointers say where the kickoff notes discuss it.

| Question | Discussed in |
|---|---|
| The primitives: Field, Place, Transfer, Potential, Event — and whether five is the right set | Appendix A §5; Appendix B §5 |
| State layout: flat arrays per place, fixed capacity plus a mask | Appendix A §6, §10; Appendix B §5.5 |
| Amounts stored, concentration always amount ÷ volume, volume computed from shape | Appendix A §2, §6 |
| How contributions are merged; the non-negativity limiter; exact conservation | Appendix A §6; Appendix B §5.1 |
| Units: mandatory or not, hand-written or a library | Appendix A §8; Appendix B §3, §5.3 |
| Automatic differentiation and the array backend (NumPy only, or JAX) | Appendix A §2, §13; Appendix B §6, §7 |
| Interfaces between scales and their closures | Appendix A §1, §6 |
| Time stepping, splitting and timescale checks | Appendix A §6; Appendix B §5.1 |
| Events: division, death, births, neighbour exchange | Appendix A §6; Appendix B §5.1 |
| Calibration and experiment design | Appendix A §9; Appendix B §5.4 |
| Random-number policy for stochastic mechanisms | not discussed; needed by the first target |
