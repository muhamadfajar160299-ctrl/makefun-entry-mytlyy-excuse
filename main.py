"""Copy the one-line entry byte-identically to the grader output dir.

Reads entry.txt next to this script and writes it unchanged to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. No temp file is used,
so the output is exactly the shipped bytes.
"""

import os
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.txt"
OUT_DIR = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
OUT = OUT_DIR / "entry.txt"

try:
    data = SRC.read_bytes()
except OSError as exc:
    print(f"cannot read entry.txt: {exc}", file=sys.stderr)
    raise SystemExit(1)

if not data or not data.strip():
    print("entry.txt is empty or whitespace-only", file=sys.stderr)
    raise SystemExit(1)

try:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)
    os.chmod(OUT, 0o644)
except OSError as exc:
    print(f"cannot write output entry.txt: {exc}", file=sys.stderr)
    raise SystemExit(1)
