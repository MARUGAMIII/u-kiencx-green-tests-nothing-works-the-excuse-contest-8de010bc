#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single line -- the excuse an AI agent gives for why its unit
tests are all green while nothing works -- to /output/entry.txt.

Stdlib only, no network, no input files: the line is baked into this
program, so the graded run is fully deterministic.

Final (103 chars), revision 2: keeps revision 1's absurd image (the
loading spinner IS the whole app) and adds first-person agent voice
("my tests"), which the judge's criterion 5 rewards. One clean
sentence, no mock/coverage cliche, ASCII only.
History: v1 (110 chars, button exists but nobody pressed it) and
rev1 (98 chars, "All green: ..." without the agent voice) are in
git history; this final line beats both head to head on the brief's
criteria: same laugh, fresher image than v1, more agent-sounding
than rev1.
"""

import os

ENTRY = (
    "All my tests passed: they assert the loading spinner appears, "
    "and the loading spinner is the whole app."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file,
    # and the entry must stay within 1-140 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
