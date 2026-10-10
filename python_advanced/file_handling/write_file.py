#!/usr/bin/env python3
"""Write a string to a text file."""


def write_file(filename="", text=""):
    """Write text and return the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
