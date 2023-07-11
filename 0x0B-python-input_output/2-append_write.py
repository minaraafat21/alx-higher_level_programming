#!/usr/bin/python3
"""Module for read_file method"""


def append_write(filename="", text=""):
    """Method for writing to a file"""
    with open(filename, mode="a", encoding="UTF-8") as f:
        f.write(text)
        return len(text)
