#!/usr/bin/env python3
"""Six Words, One Story — u-deranalabs-six-words-one-story-f982e410.

Writes one complete story in exactly six words to /output/entry.txt.
Stdlib only; no network, no randomness, no I/O besides the one file.

The story is built from two named beats so the turn is visible
in the code:

* ARRIVAL — the medal comes home, as medals do.
* ABSENCE — the soldier does not: one missing man turns the
  homecoming into a whole war, a whole grief, a whole life.

A medal arriving home implies the enlistment, the fighting, the
letter, the funeral — and the empty chair it never says aloud.
"""

import os

# The two beats of the story, joined in entry_text().
ARRIVAL = "The medal arrived."
ABSENCE = "The soldier didn't."

# The gate caps the entry at 60 characters; the story is 38.
MAX_CHARS = 60

ENTRY = "The medal arrived. The soldier didn't."


def entry_text() -> str:
    """Join the two beats into the six-word story."""
    return f"{ARRIVAL} {ABSENCE}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-60 chars,
    exactly six words, one line, no surrounding whitespace."""
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-60 characters"
    assert len(text.split()) == 6, "entry must be exactly six words"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry has leading/trailing whitespace"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the story itself, and
    # that it is exactly six words on one clean line.
    assert text == ENTRY, "joined story drifted from the entry sentence"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
