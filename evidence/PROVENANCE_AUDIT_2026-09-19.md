# Provenance Audit — 2026-09-19

## Question

Can the advertised values for the pendulum, System C, and System D be traced to original executable sources or derivations predating the claims?

## Sources inspected

1. The complete current and historical Git record of `phiomegaruntime-rgb/phi-infinity-runtime`.
2. All 19 commits reachable from every branch and tag in that repository.
3. Every public repository listed under the GitHub account `phiomegaruntime-rgb` at the audit date. The account listed only:
   - `phi-infinity-runtime`;
   - `m-omnia-validation` (created after the claims).
4. Repository-wide and GitHub account-wide searches for:
   - `0.12475`;
   - `0.12480`;
   - `0.785382`;
   - `3.19275`;
   - `System C` / `System D`;
   - `arc-unit`;
   - the 150-degree transfer.
5. The document `Relational_Substrate_Mechanics.pdf` and related persistent M/PHI material available at the audit date.

## Findings

### Pendulum

`Relational_Substrate_Mechanics.pdf` states:

- calibration at approximately 2.8 degrees;
- `kappa = 3.19275 s/arc-unit`;
- transfer to 150 degrees;
- `3.5251 s` predicted versus `3.5255 s` actual;
- advertised residual below 0.02 percent.

No original executable implementation, raw intrinsic-arc output, numerical environment, complete initial conditions, tolerance record, or pre-benchmark prediction timestamp was found. Therefore these values remain **documented claims pending reproduction**, not independently verified results.

### System C

The advertised `N=7` collapse values (`0.12475 s` prediction and `0.12480 s` benchmark) were not found in any repository source, commit, tag, executable artifact, or derivation inspected. No adjacency matrix, initial conditions, update equation, stall event, seed, tolerance, or benchmark provenance was recovered.

Status: **unverified; source absent**.

### System D

The advertised radial-fall value (`0.785382 s`) and its claimed `pi/4` benchmark were not found in any repository source, commit, tag, executable artifact, or derivation inspected. No normalization, masses, release distance, intrinsic increment definition, collision event, integration method, tolerance, or benchmark derivation was recovered.

Status: **unverified; source absent**.

## Falsification consequence

The three-regime “smoking gun” claim is not presently supported by a reproducible evidence chain. The absence of provenance does not prove that the numerical statements are false; it proves that they cannot currently function as scientific evidence.

No implementation may now be designed to reproduce the advertised target values and then presented as their original source. Any new System C or System D implementation must be labelled a **new preregistered test**, with definitions and prediction frozen before benchmark comparison.

## Evidence required to reopen the historical claims

A historical claim may be reconsidered only if a pre-existing artifact is recovered with independently checkable creation history and containing, at minimum:

- governing equations or source code;
- complete initial conditions and units;
- event/stopping definition;
- all numerical tolerances and random seeds;
- parameter provenance showing no target leakage;
- raw output establishing `Delta tau` before multiplication by frozen `kappa`;
- independent benchmark derivation or source;
- hashes and execution instructions.

Until then, the repository ledger statuses remain unchanged.
