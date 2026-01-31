#!/usr/bin/python3

"""Rectangle Class Module example in Python"""


class Rectangle:
    """Rectangle class
    Rectangles have four sides and four right angles"""

    def __init__(self, width=0, height=0):
        """Rectangle constructor
        Args:
            width (int): width of the square
            height (int): height of the square"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """get the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """get the perimieter of the reactangle"""
        return (self.__height * 2) + (self.__width * 2)
