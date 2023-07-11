#!/usr/bin/python3
"""Module for read_file method"""


def write_file(filename="", text=""):
    """Method for writing to a file"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)
