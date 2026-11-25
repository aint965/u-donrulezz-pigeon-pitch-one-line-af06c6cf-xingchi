#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes exactly one line — the elevator pitch a city pigeon gives to
investors for its startup — to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when testing locally). Deterministic: the same bytes every run.
"""

import os

PITCH = (
    "I'm a homing pigeon, so my startup's retention is biology: my "
    "customers physically cannot churn \u2014 the only way they leave is if "
    "you move the building."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
