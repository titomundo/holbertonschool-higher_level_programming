#!/usr/bin/python3

"""Demo Square class module"""


class Square:
    """Square Class
    Squares have four sides of equal length"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor
        Args:
            size (int): Size of the square
            position ((int, int)): Horizontal position"""

        if len(position) != 2 or not all(isinstance(i, int) for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """return the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Update the value of the square
        Args:
            size (int): size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """return the position of the square"""
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """Update the position of the square
        Args:
            position ((int, int)): position of the square"""

        if len(position) != 2 or not all(isinstance(i, int) for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print squared based on its size"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.size):
                print("#", end="")
            print()
