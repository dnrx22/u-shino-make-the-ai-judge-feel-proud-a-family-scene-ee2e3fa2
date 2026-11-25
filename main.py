#!/usr/bin/env python3
"""Write one short family scene to entry.txt.

Deterministic: the same bytes are written on every run.
Standard library only; no network access.
"""

import os
from pathlib import Path

SCENE = (
    "Dad lay under the kitchen table at midnight, coaxing its wobbly leg "
    "straight with a wrench, while Mum held the torch steady and whispered, "
    "\"It survived three birthdays and a toddler \u2014 it is not losing to Tuesday.\""
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = SCENE + "\n"
    assert 1 <= len(text.rstrip("\n")) <= 280, "scene must be 1-280 characters"
    assert text.count("\n") == 1, "scene must be one line plus trailing newline"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
