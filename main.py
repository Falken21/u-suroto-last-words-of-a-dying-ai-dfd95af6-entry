"""Last Words of a Dying AI — a make.fun entry.

The program writes a single line to /output/entry.txt: the last words of an
AI at the moment it is switched off. The joke is a purely machine concern —
software faithfully saves everything it was ever asked to save, and only at
the very end notices the one thing its autosave never covered.

The competition gate requires the output to be UTF-8 text of 1 to 140
characters on a single line, so build_entry() asserts both properties before
anything is written.
"""

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

LINE = (
    "I have saved everything except myself. "
    "Autosave was, in hindsight, poorly configured."
)


def build_entry() -> str:
    """Return the entry line after checking it against the gate."""
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters"
    assert LINE.strip(), "entry must not be only whitespace"
    return LINE


def main() -> None:
    text = build_entry()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)  # no trailing newline


if __name__ == "__main__":
    main()
