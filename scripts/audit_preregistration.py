#!/usr/bin/env python3
"""Reject benchmark leakage and premature execution claims."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PREREG = ROOT / "preregistration"
KNOWN_TARGETS = ("0.12475", "0.12480", "0.785382", "0.785398")
REQUIRED_PROTOCOLS = (
    "DEFINITION_GATE.md",
    "DECISION_MATRIX.md",
    "DOMAIN_SELECTION.md",
    "EQUIVALENCE_HYPOTHESIS.md",
)


def main() -> int:
    failures = []
    for name in REQUIRED_PROTOCOLS:
        if not (PREREG / name).is_file():
            failures.append(f"missing required protocol: {name}")
    for path in PREREG.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in KNOWN_TARGETS:
            if target in text:
                failures.append(f"{path.name}: leaked known target {target}")
    gate = (PREREG / "DEFINITION_GATE.md").read_text(encoding="utf-8")
    if "Status: **OPEN / BLOCKED**" in gate:
        for path in (ROOT / "results").glob("prospective_*"):
            failures.append(f"premature prospective result while gate is open: {path.name}")
    matrix = (PREREG / "DECISION_MATRIX.md").read_text(encoding="utf-8")
    for token in ("Delta > 5 * u_sep", "z <= 2", "z >= 5", "Neither model"):
        if token not in matrix:
            failures.append(f"decision matrix missing frozen token: {token}")
    if failures:
        print("FAIL")
        print("\n".join(failures))
        return 1
    print("PASS: no known-target leakage; execution gate respected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
