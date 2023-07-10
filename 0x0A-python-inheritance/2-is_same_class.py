#!/usr/bin/python3
"""
a function that returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class
    otherwise False."""
    if a_class == object:
        return False
    else:
        return isinstance(obj, a_class)
