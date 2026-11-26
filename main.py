"""Worst Pizza Topping entry: writes the one-liner to /output/entry.txt."""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def build_entry():
    """Assemble the entry line from its two beats: the topping, then the box."""
    topping = "Our pizza comes topped with wet cardboard"
    twist = "it folds like a love letter, and the box it arrived in is technically the second topping."
    return topping + " — " + twist


def validate_entry(text):
    """The entry must be a single line of 1-200 characters, UTF-8 safe."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError("entry must be %d-%d characters, got %d" % (MIN_LENGTH, MAX_LENGTH, len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    entry = validate_entry(build_entry())
    write_entry(OUTPUT_PATH, entry)


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError) as error:
        print("invalid entry: %s" % error, file=sys.stderr)
        sys.exit(1)
