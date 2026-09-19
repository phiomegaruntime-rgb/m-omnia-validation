# Frozen Derivation Path

For each prospective system:

1. Declare the accessible field and every excluded interaction.
2. Declare the full configuration representation before evolution.
3. Define each relational difference and exchange used by the update.
4. Define the intrinsic path increment `d_tau` directly from consecutive configurations.
5. Define the terminal transition without coordinate-time fitting.
6. Accumulate `Delta tau` from initial configuration to the first terminal crossing.
7. Apply the already frozen scale conversion exactly once.
8. Serialize the prediction, source hash, inputs, and environment.
9. Timestamp the prediction package.
10. Only then compare it with an independently generated benchmark.

Subtraction test: remove each declared relation in turn. If removal does not change the generated path or terminal crossing, that relation was not necessary and cannot be cited as explanatory. If removal destroys the configuration definition, record the dependency rather than silently replacing it.

