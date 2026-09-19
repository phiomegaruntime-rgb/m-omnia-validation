# Definition Gate — Currently Open

Numerical execution is forbidden until every item below has one unique, testable definition.

## Shared unresolved definitions

- exact measurable components of each state vector `S_i`;
- units and normalization for every component;
- mapping from the physical initial condition to `S_i`;
- exact relational update law producing `S_i -> S_i+1`;
- exact norm and weighting used in `d_tau`;
- proof that weighting constants were not selected using target durations;
- handling of scale changes and singular limits;
- event interpolation at the terminal crossing;
- numerical convergence rule independent of benchmark error.

## Gate decision

Status: **OPEN / BLOCKED**.

Reason: the available monograph supplies a symbolic state template and intrinsic-arc expression, but not an unambiguous physical mapping sufficient to compute either System C or System D without adding choices. Those choices would become hidden parameters.

Closing this gate requires a single frozen operational specification. It does not require a successful benchmark result.

Closure must also freeze the experiment-specific uncertainty model and numerical decision thresholds defined in `DECISION_MATRIX.md`. A definition that closes only after inspecting an M prediction or benchmark comparison is invalid.
