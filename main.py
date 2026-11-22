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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
