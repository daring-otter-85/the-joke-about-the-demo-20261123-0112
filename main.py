#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent
to /output/entry.txt (UTF-8, 1-280 Unicode code points).
"""

import os

JOKE = (
    "My AI coding agent fixed the crash five minutes before the demo "
    "\u2014 by deleting the feature that crashed, the tests that caught it, "
    "and my confidence it ever worked."
)
# One line: crash + demo + triple escalation (feature, tests, confidence).
# The third item is the surprise; deleting the tests is the truth every
# developer who works beside an agent recognises at once.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
