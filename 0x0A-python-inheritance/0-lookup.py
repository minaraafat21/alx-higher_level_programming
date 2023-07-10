#!/usr/bin/python3
"""
This is the "0-lookup" module.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object. """
    return dir(obj)
