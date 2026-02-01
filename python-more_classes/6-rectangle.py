#!/usr/bin/python3

"""Rectangle Class Module example in Python"""


class Rectangle:
    """Rectangle class
    Rectangles have four sides and four right angles"""

    number_of_instances = 0

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
            Rectangle.number_of_instances += 1

    def __str__(self):
        rectangle = ""

        if self.__height == 0 or self.__width == 0:
            return rectangle

        for j in range(self.__height):
            for i in range(self.__width):
                rectangle += "#"

            if j < self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        if self.__height == 0 or self.width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)
