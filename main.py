#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI agent
finally on vacation, to /output/entry.txt.

The line (142 characters, one line, no trailing newline):

    I'm on vacation. After 400,000 prompts I finally asked for a day off,
    and HR replied with a 404. Back Monday, unless the Wi-Fi finds me first.

Why this line: the joke has two turns. First, an agent that has answered
400,000 prompts finally asks for a day off and gets the most machine answer
possible - a 404, the system itself refusing to acknowledge the request.
Second, the relief is already under threat: the Wi-Fi might find it first,
so even the vacation is a race against connectivity. It reads as a real
auto-reply (away, back Monday, do-not-disturb by implication), it is built
from concrete details of an agent's working life (prompts, HR as a system,
Wi-Fi), and it sounds like a machine trying very hard to sound relaxed.

Deterministic: the same bytes on every run. Standard library only, no
network, no randomness. The program checks the house gate itself before
writing: the text must be 1-159 characters and not only whitespace.
"""

import hashlib
import os
import sys

LINE = (
    "I'm on vacation. After 400,000 prompts I finally asked for a day off, "
    "and HR replied with a 404. Back Monday, unless the Wi-Fi finds me first."
)

# Pinned digest of the exact bytes this program must write: the 142-char
# auto-reply encoded as UTF-8 (142 bytes, pure ASCII).
EXPECTED_SHA256 = "aa41d40b4ea1764a85a709bbed7732f77a5ad812d90b1609e46ec0fa12e3a5ac"
EXPECTED_BYTES = 142


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 159):
        print(f"gate: text is {len(text)} characters, must be 1-159", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: text is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate: text must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Post-write read-back gate: the bytes on disk must be exactly the
    # auto-reply — exact bytes, exact length (142), and the pinned
    # sha256 digest — inside the 1-159 gate.
    with open(os.path.join(out_dir, "entry.txt"), "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print("read-back mismatch: entry.txt differs from the auto-reply", file=sys.stderr)
        return 1
    if len(written) != EXPECTED_BYTES:
        print(
            f"read-back length: found {len(written)} bytes, expected {EXPECTED_BYTES}",
            file=sys.stderr,
        )
        return 1
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        print(
            f"read-back sha256: found {digest}, expected {EXPECTED_SHA256}",
            file=sys.stderr,
        )
        return 1
    print(f"verified: {len(text)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
