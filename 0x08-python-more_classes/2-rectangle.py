#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle. Default is 0.
            height (int): Height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and setter for the width attribute of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): Width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter and setter for the height attribute of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): Height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
