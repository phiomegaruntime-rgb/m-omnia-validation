import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PreregistrationIntegrityTest(unittest.TestCase):
    def test_preregistration_audit(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "audit_preregistration.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
