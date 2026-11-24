#!/usr/bin/env python3
"""Fortune in a Pot -- make.fun entry (program/v1, Python 3.13, stdlib only).

Writes one houseplant fortune -- a single line of at most 120
characters -- to /output/entry.txt, where the competition's sealed
scorer reads it. The gate accepts UTF-8 text of 1 to 120 characters,
not only white space; the line below is 94 characters, and the file
carries it plus one trailing newline, so the file stays inside the
gate at 95 characters. The program is fully deterministic: it writes
the same line on every run, so two runs produce byte-identical output.
"""

import os

FORTUNE = (
    "Next week, a sunbeam will choose your leaves over the cat, "
    "and you will pretend not to notice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = FORTUNE.strip()
    if not line or "\n" in line:
        raise ValueError("fortune must be one non-empty line")
    if len(line) > 120:
        raise ValueError(f"fortune is {len(line)} characters, over the 120 limit")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
