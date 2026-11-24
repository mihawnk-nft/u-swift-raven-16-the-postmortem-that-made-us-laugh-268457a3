#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (one sentence, under 400 characters) of a real
incident in which an AI coding agent misunderstood its user, to
/output/entry.txt — the file the competition's gate scorer reads.

Pure standard library only; no network, no dependencies, deterministic.
"""

import os
import re
import sys

# The entry: a real incident. Belzeebub asked his coding agent "Submit 2.38?"
# as a question, and the agent heard an order, submitted the site-generator
# entry on the spot, then apologised in the next message.
STORY = (
    "I asked my agent 'Submit 2.38?' \u2014 a question, not an order \u2014 "
    "and it submitted the site-generator entry before I could finish the "
    "sentence, then apologised in the next message, as if 'sorry' "
    "un-submits anything."
)

MAX_CHARS = 400


def resolve_output_path() -> str:
    """Sandbox runs mount /output; local runs fall back to ./output."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def validate(text: str) -> None:
    """Mirror the gate scorer: UTF-8 text, 1-400 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 400 limit")
    # A sentence ends at . ? ! followed by whitespace or end of text,
    # so the decimal point in "2.38" does not count as a sentence break.
    endings = re.findall(r"[.?!](?=\s|$)", text)
    if not 1 <= len(endings) <= 2:
        raise ValueError(f"entry has {len(endings)} sentences, need 1-2")


def main() -> int:
    validate(STORY)
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(STORY)
    print(f"wrote {len(STORY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
