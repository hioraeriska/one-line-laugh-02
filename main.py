"""One-Line Laugh: write a single funny line to the output file.

The bounty gate checks that the output file holds UTF-8 text of 1 to 200
characters, not only whitespace, standing alone as one sentence. This
program validates the line against that gate and writes it out.
"""

import os

LINE = "I went to bed early for once, and my brain treated it as a meeting to discuss every mistake I've made since 2009."

MAX_CHARS = 200
SENTENCE_ENDINGS = ".!?"


def validate_length(line):
    """Check the line fits the 1-to-200 character gate."""
    if not line or not line.strip():
        raise ValueError("line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def validate_content(line):
    """Check the line is one line holding exactly one sentence."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    closers = sum(line.count(mark) for mark in SENTENCE_ENDINGS)
    if closers != 1 or line[-1] not in SENTENCE_ENDINGS:
        raise ValueError("line must be exactly one sentence")


def resolve_output_dir():
    """Return the directory the entry file goes in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    validate_length(LINE)
    validate_content(LINE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
