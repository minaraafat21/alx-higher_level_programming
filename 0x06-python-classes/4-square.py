#!/usr/bin/python3
"""define a class square"""


class Square:
    """size validation"""
    def __init__(self, size=0):
        """ init constructor"""

        self.__size = size

    def area(self):
        """return area"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
