#!/usr/bin/python3
"""define a class square"""


class Square:
    """size validation"""
    def __init__(self, size=0):
        """ init constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
