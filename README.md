# M-OMNIA Validation Repository

This repository is an evidence-first workspace for testing Relational Substrate Mechanics (M-OMNIA / Phi-Infinity).

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

