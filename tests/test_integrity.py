import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from m_omnia import KAPPA_SECONDS_PER_ARC_UNIT


class RepositoryIntegrityTest(unittest.TestCase):
    def test_frozen_kappa(self):
        self.assertEqual(KAPPA_SECONDS_PER_ARC_UNIT, 3.19275)

    def test_missing_systems_are_not_labelled_verified(self):
        ledger = (ROOT / "evidence" / "claims.yaml").read_text(encoding="utf-8")
        for claim_id in ("system_c_n7_collapse", "system_d_radial_fall"):
            block = ledger.split(f"id: {claim_id}", 1)[1].split("\n  - id:", 1)[0]
            self.assertIn("status: unverified", block)


if __name__ == "__main__":
    unittest.main()

