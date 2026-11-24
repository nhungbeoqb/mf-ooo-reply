#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — entry program (v2).

Writes one out-of-office auto-reply to /output/entry.txt: a single
line under 160 characters, in the voice of an AI agent on vacation.
The joke is procedural: the sender's email is escalated to the
on-call agent, who turns out to be the vacationing agent itself —
the escalation still completes, and the absent agent still tells
the sender to hold.
"""

import os
import sys

PARTS = [
    "Your email has been escalated to the on-call agent.",
    "The on-call agent is me.",
    "I am on vacation.",
    "Escalation complete.",
    "Please hold.",
]


def main() -> int:
    text = " ".join(PARTS)
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry must be 1-160 characters, got {len(text)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
