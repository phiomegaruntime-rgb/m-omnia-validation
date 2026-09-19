# System D — Prospective Protocol

## Intended falsification target

Test whether one frozen relational update and the historical `kappa` produce a finite first-collision duration for a radial gravitational configuration without singularity-specific regularization or retuning.

## Must be frozen before execution

- number of bodies and masses;
- unit system and normalization;
- initial separation and velocity;
- accessible-field boundary assumptions;
- relational update equation;
- intrinsic increment and norm;
- exact collision/limit event;
- event interpolation method;
- integration resolution and convergence rule;
- independent analytic or high-precision benchmark procedure.

## Automatic falsifiers

- normalization chosen to force a known terminal duration;
- special near-collision coefficient introduced only for this system;
- stopping radius chosen from comparison error;
- different `kappa` or state weights from other regimes;
- discarded divergent or failed runs;
- benchmark code sharing the prediction code path.

Current execution status: **BLOCKED BY DEFINITION GATE**.

