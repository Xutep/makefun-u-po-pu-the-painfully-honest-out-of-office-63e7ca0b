#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
to /output/entry.txt. Deterministic, stdlib only: the reply is a fixed
string, so every run produces byte-identical output.
"""

import os

MAX_CHARS = 200

REPLY = (
    "I'm away until Monday and, honestly, my inbox will be a small "
    "avalanche by the time I'm back, so I'll reply as soon as I've dug "
    "myself out \u2014 thank you for your patience."
)


def main() -> None:
    text = REPLY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("reply must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
