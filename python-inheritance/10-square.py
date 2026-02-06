#!/usr/bin/python3

"""10-square: Declares the Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, based on Rectangle class"""

    def __init__(self, size):
        """square declaration
        Args:
            size (int): size of the square's sides"""

        try:
            self.integer_validator("size", size)
        except Exception as Err:
            raise Err
        else:
            self.__size = size
            super().__init__(size, size)

    def area(self):
        """returns the area of the square"""

        return self.__size * self.__size
