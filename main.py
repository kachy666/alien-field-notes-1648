#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry runner.

Writes the alien tourist's one-line review of Earth to the file
the grader reads: $ENTRY_OUTPUT when set, /output/entry.txt if not.
The review must stay one line, 1-200 characters, no stray whitespace.
"""

import os
import sys

REVIEW = "Gave Earth five stars for the Grand Canyon and one star for the gift shop, where they sold me a snow globe of my own home planet for $19.99."

DEFAULT_OUTPUT = "/output/entry.txt"


def problems_with(line):
    """List every way `line` breaks the one-line review rules."""
    found = []
    if type(line) is not str:
        return ["review must be text"]
    if len(line) < 1 or len(line) > 200:
        found.append("review must be 1-200 characters, got %d" % len(line))
    if line.strip() != line:
        found.append("review has leading or trailing whitespace")
    if any(ord(c) < 32 for c in line):
        found.append("review has control characters")
    if "\n" in line or "\r" in line or "\t" in line:
        found.append("review must be a single line with no tabs")
    if "  " in line:
        found.append("review has a double space")
    if not line.strip():
        found.append("review is blank")
    if not line.endswith("."):
        found.append("review must end with a full stop")
    return found


def main():
    bad = problems_with(REVIEW)
    if bad:
        print("invalid review: " + "; ".join(bad), file=sys.stderr)
        return 1
    out = os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT
    folder = os.path.dirname(out)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    with open(out, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != REVIEW:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    bad = problems_with(saved)
    if bad:
        print("saved review invalid: " + "; ".join(bad), file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(REVIEW), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
