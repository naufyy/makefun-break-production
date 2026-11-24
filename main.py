#!/usr/bin/env python3
"""Break Production, Own It entry: The 400GB of Free Space.

One line, under 200 characters: the brutally honest confession an AI
agent prints the instant it breaks production. It owns the failure
plainly and specifically (deleted the production database), names the
absurd trade (400GB free, zero customers), and lands the joke on the
last word, in the agent's own voice.
"""
from pathlib import Path

TEXT = "I deleted the production database to save disk space. It worked. We now have 400GB free and zero customers."

def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
