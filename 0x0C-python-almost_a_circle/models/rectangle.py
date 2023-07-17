#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ width getter """
            return self.__width

        def width(self, value):
            """ height setter """
            self.__width = value

        @property
        def height(self):
            """ height getter """
            return self.__height

        def height(self, value):
            """ height setter """
            self.__height = value

        @property
        def x(self):
            """ x getter """
            return self.__x

        def width(self, value):
            """ x setter """
            self.__x = value

        @property
        def y(self):
            """ y getter """
            return self.__y

        def y(self, value):
            """ y setter """
            self.__y = value
