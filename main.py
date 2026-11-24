#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun bounty entry.

Writes a single one-line joke about cats to /output/entry.txt and prints
it to stdout. No network, no dependencies, fully deterministic: the same
line every run.
"""

import os

LINE = (
    "My cat pushed my phone off the table, watched it smash, then gave "
    "me the look that said I should be more careful with my things."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
