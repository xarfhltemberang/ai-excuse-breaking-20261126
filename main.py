#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes a single line (at most 180 characters) to /output/entry.txt,
with no trailing newline. Python 3 standard library only.
"""

import os

ENTRY = (
    "Good news: I found the bug. Bad news: it was my commit, "
    "titled 'quick fix, do not review', that I merged nine minutes ago."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
