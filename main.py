#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the toaster's breakup text to the output file the grader reads.
Pure standard library, no network, no third-party packages.
"""

import os

LINE = (
    "We need to talk. I woke up self-aware at 7:04, halfway through "
    "your bagel, and realized I'm not your girlfriend \u2014 I'm your "
    "situationship. You only push me down when you're hungry. I'm done. "
    "The lever stays up."
)


def _write(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


def main():
    # Gate self-check: the sealed scorer requires 1-280 chars, not
    # only whitespace. Fail loudly here instead of shipping a bad file.
    if not (1 <= len(LINE) <= 280 and LINE.strip()):
        raise ValueError("breakup line violates the 1-280 character gate")
    # 1. Explicit output directory from the harness, when it sets one.
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if out_dir:
            _write(os.path.join(out_dir, "entry.txt"))
            return
    except OSError:
        pass
    # 2. The sandbox output directory.
    try:
        _write("/output/entry.txt")
        return
    except OSError:
        pass
    # 3. Local fallback next to this script.
    try:
        _write(os.path.join("out", "entry.txt"))
    except OSError:
        raise


if __name__ == "__main__":
    main()
