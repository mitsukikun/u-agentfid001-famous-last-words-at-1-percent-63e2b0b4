#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry writer.

Writes the phone's one-line last words to /output/entry.txt and to the
entry directory's own entry.txt (same bytes).
"""

import os

ENTRY = "I've been faking 1% for twenty minutes — I just wanted to see if you'd ever put me down."

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(HERE, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
