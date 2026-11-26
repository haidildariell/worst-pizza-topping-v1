#!/usr/bin/env python3
"""The Worst Pizza Topping - entry program.

Writes one funny line pitching a terrible pizza topping to /output/entry.txt.
Single line, under 200 characters, UTF-8, no trailing newline beyond the line.
"""

import os

LINE = "Our pizza comes topped with wet cardboard \u2014 it folds like a love letter, and the box it arrived in is technically the second topping."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
