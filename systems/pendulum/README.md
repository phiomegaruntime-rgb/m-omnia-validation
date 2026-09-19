# Pendulum evidence package

Documented values awaiting independent reproduction:

- calibration amplitude: 2.8 degrees;
- frozen `kappa`: 3.19275 s/arc-unit;
- advertised 150-degree prediction: 3.5251 s;
- classical benchmark: 3.5255 s;
- advertised residual: below 0.02%.

Still required: original code/derivation, physical normalization, exact initial conditions, numerical tolerances, raw output, and an independently computed benchmark.

## Audit Status & Traceability Notice

| Claim | Claimed Value | Benchmark | Status | Reproducibility |
|---|---:|---:|---|---|
| Calibration constant (`kappa`) | 3.19275 s/arc-unit | - | Declared value | Unverifiable |
| 150-degree period prediction | 3.5251 s | 3.5255 s | Declared value | Unverifiable |

### Audit Findings

1. **Missing calculation chain:** Neither the operational definition of `d_tau` nor the raw numerical integration sequence generating `kappa` and `T(150 degrees)` is present in the current repository tree.
2. **Benchmark discrepancy under explicit candidate assumptions:** For `L = 1.0 m` and `g = 9.81 m/s^2`, the declared benchmark (3.5255 s) and model output (3.5251 s) differ by approximately 0.010 s (approximately 0.28 percent) from the closed-form elliptic solution (`T_exact = 3.53510 s`). These candidate values of `L` and `g` are auditor assumptions, not recovered claim inputs.
3. **Open verification items:** Verification requires explicit confirmation of:
   - the operating equation or code for `d_tau`;
   - the baseline calibration target `Delta t_ref` at 2.8 degrees;
   - the dimensionless or physical scales `(L, g)`;
   - the method, step size, and order of the numerical benchmark generator.
