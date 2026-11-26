#!/usr/bin/env python3
"""Midnight Fridge Roast (make.fun).

Writes the entry -- one original line -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = "At midnight the fridge light clicks on like a stage spotlight, and there I am, in socks, negotiating with last Tuesday's leftovers like they owe me rent."


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
