#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from inception.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
