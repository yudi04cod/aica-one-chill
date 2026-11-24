#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single horror sentence to /output/entry.txt.

The line: a parent watches the baby monitor while climbing the stairs
and sees themselves already standing over the crib. The scare is earned
by the turn, not announced: no mirror, no doll, no basement, no gore —
just the quiet impossibility of being in two places at once, with the
last word ("crib") landing the blow.
"""

import os
import sys

# The entry: one sentence, under 200 characters.
LINE = (
    "I watched the baby monitor as I walked up the stairs — "
    "and saw myself already standing over the crib."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition's gate rules before writing anything."""
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal period, at the very end.
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    # Read the file back and confirm it round-trips byte for byte:
    # the grader runs the program twice and compares the outputs.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != LINE + "\n":
        raise RuntimeError("round-trip check failed: file differs from LINE")
    print(f"Wrote {len(LINE)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
