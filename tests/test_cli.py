from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inception.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


class CliTests(unittest.TestCase):
    def test_valid_file_returns_zero(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main([str(FIXTURES / "valid-ledger.json")])
        self.assertEqual(result, 0)
        self.assertIn("valid:", output.getvalue())

    def test_invalid_ledger_returns_one(self) -> None:
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            result = main([str(FIXTURES / "invalid-skipped-decision.json")])
        self.assertEqual(result, 1)
        self.assertIn("human_decision.status", error.getvalue())

    def test_malformed_json_returns_two(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main([str(path)]), 2)

    def test_missing_file_returns_two(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["does-not-exist.json"]), 2)
