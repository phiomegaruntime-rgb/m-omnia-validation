# Preregistered Decision Matrix

## Quantities frozen before prediction

For observable `y`:

- `p_M`: prediction from M;
- `p_N`: prediction from the declared Newtonian/classical comparator;
- `u_exp`: one-standard-deviation experimental uncertainty;
- `u_M`, `u_N`: numerical uncertainties established by convergence studies without using observed agreement;
- `u_Mtot = sqrt(u_exp^2 + u_M^2)`;
- `u_Ntot = sqrt(u_exp^2 + u_N^2)`;
- `u_sep = sqrt(u_M^2 + u_N^2 + 2*u_exp^2)`;
- `Delta = abs(p_M - p_N)`.

The uncertainty model, distributional assumptions, treatment of systematic error, sample size, exclusion rules, and all quantities used to estimate uncertainty must be frozen before either prediction is revealed.

## Resolution gate

Model separation is declared experimentally resolvable only when:

```text
Delta > 5 * u_sep
```

If this condition fails, the result is labelled **non-discriminating / inconclusive**, regardless of which point prediction is numerically closer to the data.

## Compatibility statistics

```text
z_M = abs(y - p_M) / u_Mtot
z_N = abs(y - p_N) / u_Ntot
```

Predeclared bands:

- compatible: `z <= 2`;
- transition region: `2 < z < 5`;
- incompatible: `z >= 5`.

Any result containing a transition-region value is reported as inconclusive unless a separate rule was frozen before prediction.

## Five outcomes

1. **Operational equivalence:** `p_M` and `p_N` are identical within frozen numerical tolerance. The test cannot establish new predictive power.
2. **Below resolution:** predictions differ, but `Delta <= 5*u_sep`. The test is inconclusive by construction.
3. **Data favor Newton:** separation is resolvable, `z_N <= 2`, and `z_M >= 5`.
4. **Data favor M:** separation is resolvable, `z_M <= 2`, and `z_N >= 5`.
5. **Neither model:** separation is resolvable and both `z_M >= 5` and `z_N >= 5`.

If both models are compatible despite resolvable nominal separation, or neither decisive rule closes, the result is **inconclusive** and the raw record is retained.

The factors 2 and 5 are protocol thresholds, not universal truths. Changing them creates a new preregistered version and cannot alter an existing run.

