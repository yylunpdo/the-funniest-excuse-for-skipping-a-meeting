#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Writes a single razor-sharp one-line excuse (200 characters or fewer)
to /output/entry.txt. Pure standard library, fully deterministic:
running it twice produces byte-identical output.
"""

import os

ENTRY = (
    "Sorry I missed it \u2014 my Wi-Fi dropped, my camera died, "
    "and my motivation filed for early retirement."
)


def main() -> None:
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify: what the judge will read must be exactly the line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == line, "read-back mismatch in /output/entry.txt"
    print(f"Wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()
