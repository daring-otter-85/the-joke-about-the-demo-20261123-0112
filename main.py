#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent
to /output/entry.txt (UTF-8, 1-280 Unicode code points).
"""

import os

JOKE = (
    "I asked my AI coding agent to fix the demo. It rewrote the app, "
    "deleted the bug, and demoed a feature I never asked for \u2014 "
    "the audience loved it, and now I have to build it."
)
# One line, 172 Unicode code points: setup (fix the demo), escalation
# (confident rewrite, hallucinated feature), punchline (now I must build it).


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
