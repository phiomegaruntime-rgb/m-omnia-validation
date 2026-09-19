# System C — Prospective Protocol

## Intended falsification target

Test whether one frozen relational update and the historical `kappa` predict the first macro-collapse/stall transition of a seven-part configuration without damping coefficients, benchmark-derived thresholds, or retuning.

## Must be frozen before execution

- seven-part interaction graph and edge orientation;
- initial configuration of every part;
- relational exchange/update equation;
- intrinsic increment and norm;
- macro-collapse definition;
- stall definition and first-crossing rule;
- deterministic seed policy;
- integration/update resolution;
- convergence criterion defined without reference to target time;
- independently generated comparison procedure.

## Automatic falsifiers

- any parameter chosen after viewing comparison error;
- a stall threshold inferred from the advertised duration;
- a graph or initial condition reconstructed to reproduce a known number;
- different `kappa` or state weights from other regimes;
- reporting only the best resolution or seed;
- failure to preserve all runs.

Current execution status: **BLOCKED BY DEFINITION GATE**.

