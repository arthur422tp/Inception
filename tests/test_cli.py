from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from inception.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


class CliTests(unittest.TestCase):
    def test_standalone_script_accepts_document_text_domain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temporary_root = Path(directory)
            isolated_skill = temporary_root / "skills" / "inception"
            shutil.copytree(
                Path(__file__).resolve().parents[1] / "skills" / "inception",
                isolated_skill,
            )
            payload = json.loads(
                (FIXTURES / "valid-ledger.json").read_text(encoding="utf-8")
            )
            payload["domain"] = "document_text"
            ledger_path = temporary_root / "document-ledger.json"
            ledger_path.write_text(json.dumps(payload), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(isolated_skill / "scripts" / "validate_ledger.py"),
                    str(ledger_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_standalone_script_runs_without_inception_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            isolated_skill = Path(directory) / "skills" / "inception"
            shutil.copytree(
                Path(__file__).resolve().parents[1] / "skills" / "inception",
                isolated_skill,
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(isolated_skill / "scripts" / "validate_ledger.py"),
                    str(FIXTURES / "valid-ledger.json"),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), f"valid: {FIXTURES / 'valid-ledger.json'}")

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
