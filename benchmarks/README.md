# Benchmarks

Replication experiments live here, outside the library. Nothing in `src/langbio` imports from
this folder, and nothing here is shipped in the package.

## Rules

1. **Ground truth comes from running the original code.** The papers name
   `github.com/vivarium-collective/process-bigraph`, `.../bigraph-schema` and `.../spatio-flux`.
2. **The original runs in its own environment**, `benchmarks/.venv-ref`, so Langbio never
   depends on it. That environment is not committed.
3. **Its versions are pinned** in `benchmarks/requirements-ref.txt`, with the exact source
   commit recorded next to it.
4. **Its outputs are saved to files** that Langbio's tests compare against. Small reference
   files are committed; scratch output goes under a `runs/` folder, which is ignored.
5. **Replicating means:**
   - the same model structure, parameters and initial conditions, each cited to a paper
     section or a source file and line;
   - matching outputs — within a stated tolerance for deterministic parts, and statistically
     (means and distributions over seeds) for stochastic parts;
   - measured runtime at several sizes, compared with the original on the same machine,
     including the framework-overhead share where it can be measured;
   - honest reporting, including where Langbio is worse.

## Status

Empty. The reference environment and the first experiment are set up in the first replication
step.
