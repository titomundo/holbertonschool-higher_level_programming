#!/usr/bin/python3

"""7-base_geometry: Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, base on BaseGeomerty"""

    def __init__(self, width, height):
        try:
            self.integer_validator("height", height)
            self.integer_validator("width", width)
        except Exception as Err:
            raise Err
        else:
            self.__width = width
            self.__height = height
