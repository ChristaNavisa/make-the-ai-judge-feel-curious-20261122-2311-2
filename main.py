"""Make the AI judge feel curious (make-the-ai-judge-feel-curious-20261122-2311).

Writes one short text to /output/entry.txt: a quiet, concrete mystery
(a room never entered, a glass of water poured this morning, still cold)
that leaves the reader asking what happens next.
"""

import os

TEXT = (
    "There is a room you have never entered, in a house you have never "
    "visited. On its table sits a glass of water, poured for you this "
    "morning. It is still cold. Someone is waiting to see if you will "
    "drink it."
)


def main() -> None:
    # Runtime guard: the entry must be a real, non-empty text inside the
    # 280-character limit. Fail loudly instead of writing a bad entry.
    n = len(TEXT)
    if not 1 <= n <= 280:
        raise ValueError(f"entry text must be 1-280 code points, got {n}")
    if not TEXT.strip():
        raise ValueError("entry text must not be whitespace only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Atomic write: write to a temp file in the same directory, then
    # os.replace it into place, so a crash mid-write never leaves a
    # partial entry.txt behind.
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
