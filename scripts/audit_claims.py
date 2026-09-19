#!/usr/bin/env python3
"""Audit the evidence ledger without external dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "evidence" / "claims.yaml"


def main() -> int:
    text = LEDGER.read_text(encoding="utf-8")
    verified = len(re.findall(r"^\s*status:\s*verified\s*$", text, re.MULTILINE))
    blocked = len(re.findall(r"^\s*status:\s*unverified\s*$", text, re.MULTILINE))
    pending = len(re.findall(r"^\s*status:\s*documented_pending_reproduction\s*$", text, re.MULTILINE))
    if verified and "evidence_hash:" not in text:
        print("FAIL: a verified claim lacks an evidence_hash")
        return 1
    print(f"PASS: verified={verified}, pending={pending}, unverified={blocked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

