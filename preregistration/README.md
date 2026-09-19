# Prospective Preregistration

This directory freezes the next tests before any new prediction is computed.

These tests are **prospective and zero-retuning**, but they are not called blind within this repository because the previously advertised benchmark values are already known to the authors. A genuinely blind round requires an independent custodian to withhold the benchmark until prediction hashes have been timestamped.

Execution is blocked until the definition gate in `DEFINITION_GATE.md` closes.

Order:

1. freeze conceptual solution;
2. freeze derivation path;
3. close every operational definition;
4. freeze source, inputs, units, tolerances, and environment;
5. generate and hash prediction without benchmark comparison;
6. obtain the independent benchmark;
7. reveal comparison once;
8. retain success or failure without retuning.

