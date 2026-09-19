# Frozen Protocol

## Mandatory order

1. Solve conceptually using M alone.
2. Freeze the conceptual solution before looking at numerical outcomes.
3. Record the exact logical path used.
4. Formalize numerically only after the first three stages.
5. Freeze calibration data and parameters.
6. Execute untouched out-of-sample systems.
7. Reveal and compare benchmarks only after predictions exist.
8. Preserve failures. Do not retune.

## M cascade state

- `M = (F <-> F)^infinity`
- R1: `DELIMITATION != ISOLATION`
- R2: `PART != ISOLATED PART`
- R3: `PROPERTY OF CONFIGURATION != NECESSARY PROPERTY OF ISOLATED FRAGMENT`

For each frozen result `R_n`, search only for closures where removing `R_n` prevents the solution. Apply the subtraction test, derive only necessary consequences, and freeze them. A branch ends when no such closure exists. Infinity is not assumed as an empirical result.

## Evidence gate

A claim may be marked `verified` only when all are present:

- original source code or analytic derivation;
- immutable initial conditions;
- explicit stopping/event condition;
- parameter provenance;
- execution command and environment;
- generated prediction recorded before benchmark comparison;
- independent benchmark provenance;
- residual calculation;
- hashes for the evidence package.

Absence of any item leaves the claim `unverified` or `documented_pending_reproduction`.

