# M-OMNIA Validation Repository

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22844638.svg)](https://doi.org/10.5281/zenodo.22844638)

This repository is an evidence-first workspace for testing Relational Substrate Mechanics (M-OMNIA / Phi-Infinity).

Author: **Massimiliano Brighindi**

Current protocol status: **v0.2.0-preregistration; no empirically verified result is claimed**.

Previous archived release v0.1.0 DOI: **[10.5281/zenodo.22844638](https://doi.org/10.5281/zenodo.22844638)**

All-version DOI: **[10.5281/zenodo.22844637](https://doi.org/10.5281/zenodo.22844637)**

## Frozen conceptual root

```text
M = (F <-> F)^infinity
```

Operationally: delimitation is not isolation; a part is not an isolated part; a property of a configuration is not automatically a necessary property of the isolated fragment.

## Scientific purpose

The central claim under test is **zero-parameter out-of-sample transferability** after a single calibration:

```text
dt = kappa * d_tau
kappa = 3.19275 s / arc-unit
```

The repository does not treat a numerical value as evidence unless its provenance, inputs, implementation, execution record, and independent benchmark are all present.

## Current evidence status

| System | Claim | Status |
| --- | --- | --- |
| Pendulum, 2.8 deg | Source of frozen `kappa` | Documented claim; original executable evidence still required |
| Pendulum, 150 deg | 3.5251 s vs 3.5255 s | Documented claim; independent reproduction still required |
| System C, N=7 | 0.12475 s vs 0.12480 s | Unverified; original source missing |
| System D | 0.785382 s vs pi/4 | Unverified; original source missing |

No missing implementation may be reconstructed from its advertised target value.

## Definition Gate: BLOCKED

Prospective numerical execution is currently forbidden. The operational definitions of the measurable state map, units, relational update, intrinsic increment `d_tau`, metric weights, terminal crossing, and benchmark-independent convergence rule are not yet unique.

The complete gate is frozen in [`preregistration/DEFINITION_GATE.md`](preregistration/DEFINITION_GATE.md). While the gate is blocked:

- no System C or System D prediction may be generated;
- no numerical agreement may be promoted to verified evidence;
- alternative definitions may not be selected by proximity to a known benchmark.

The pendulum is now classified as an **equivalence and code-control test**, not as discriminating evidence for new physics.

## Legitimate theory outcomes

The preregistered comparison allows five outcomes:

1. M and Newton are operationally equivalent in the tested domain;
2. their separation is below the preregistered experimental resolution, so the test is inconclusive;
3. the data discriminate in favor of Newton;
4. the data discriminate in favor of M;
5. the data reject both models within the declared error model.

Global equivalence with Newton is an admissible publishable result. It would classify M as a possible reformulation, not as a theory with demonstrated new predictive power.

## Repository map

- `PROTOCOL_FROZEN.md`: immutable order of analysis and falsification rules.
- `THEORY.md`: minimal theory statement, separated from empirical claims.
- `evidence/claims.yaml`: machine-readable claim ledger.
- `systems/`: one isolated package per physical regime.
- `benchmarks/`: benchmark definitions and provenance.
- `results/`: generated outputs only; failures must be retained.
- `scripts/audit_claims.py`: fails when a claim is labelled verified without the required evidence.
- `tests/`: repository integrity tests.

## First run

```bash
python scripts/audit_claims.py
python -m unittest discover -s tests -v
```

## Rule against retrofitting

System C and System D remain blocked until their original equations/code, initial conditions, stopping rules, and provenance are recovered. Adding an implementation chosen to reproduce the published numbers would be retrospective fitting, not out-of-sample validation.
