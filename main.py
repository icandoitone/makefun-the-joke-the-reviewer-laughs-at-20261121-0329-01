#!/usr/bin/env python3
"""Entry for make.fun: "The joke the reviewer laughs at".

Writes a single one-line joke about working beside an AI coding agent
to entry.txt inside the output directory (MAKEFUN_OUTPUT_DIR when set,
otherwise /output). Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "The agent wrote the function, the tests, and the commit message — "
    "I just click Approve on diffs I've stopped pretending to read."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke must be 1-280 non-whitespace characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = JOKE + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
