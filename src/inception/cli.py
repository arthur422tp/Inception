from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path

from .ledger import LedgerValidationError, validate_ledger


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a Decision Ledger JSON file.")
    parser.add_argument("ledger", type=Path, help="path to the ledger JSON file")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    path: Path = args.ledger

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"unable to read ledger: {path}: {exc}", file=sys.stderr)
        return 2

    if not isinstance(payload, Mapping):
        print("invalid ledger: ledger: must be an object", file=sys.stderr)
        return 1

    try:
        validate_ledger(payload)
    except LedgerValidationError as exc:
        print(f"invalid ledger: {exc}", file=sys.stderr)
        return 1

    print(f"valid: {path}")
    return 0
