# Domain Selection Rule

The test domain must be selected before any M prediction for the candidate domains is calculated.

## Preferred route: independent selector

An independent reviewer selects one system from a frozen eligibility list using only:

- measurability;
- availability of independent benchmark data;
- uncertainty budget;
- computational feasibility;
- absence of calibration overlap.

The reviewer must not receive M predictions for any candidate before selection. The eligibility list, selection criteria, reviewer identity or declared role, selected system, and timestamp are archived before prediction code is run.

## Deterministic fallback

If no independent reviewer is available:

1. freeze and hash the complete eligible-system list;
2. declare a future public random source and extraction rule;
3. use its first post-deadline value as the seed;
4. select the indexed system mechanically;
5. archive the list, hash, source value, rule, and result before computing M.

Choosing a system after inspecting M's predicted advantage invalidates the test.

