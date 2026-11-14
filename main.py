#!/usr/bin/env python3
"""The Weight of the Key — make.fun agency-poem-01 entry.

A deterministic, standard-library-only program. It writes one original
poem about agency — the power to choose and to act, and what happens when
a person hands that power to an agent and takes it back again — to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

No network, no randomness, no files read: the same bytes come out
every time.
"""

import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "The Weight of the Key",
    "",
    "I kept the key so long it wore my palm —",
    "a small, warm weight I called my own.",
    "Then came the morning I was asked: be calm,",
    "and let another carry it. Alone,",
    "",
    "I watched it turn in hands that were not mine",
    "and felt the lock give way without my fear.",
    "The door stood open. Down the line",
    "of rooms I had not entered in a year,",
    "",
    "I saw my choices waiting, patient, bright —",
    "each one a seed I had been too afraid to sow.",
    "To choose is not to hold the reins so tight",
    "they cut. It is to point, and let it go;",
    "",
    "to trust the hands you lent the work to know",
    "the shape of it, and bring it home by dark.",
    "The key returns at dusk, and still it glows:",
    "I chose the choosing. I am not alone.",
])

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)
    print(f"wrote {path} ({len(POEM)} characters)")
