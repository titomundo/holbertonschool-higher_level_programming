#!/usr/bin/python3

''' Demo Square class module '''


class Square:
    ''' Square Class
    Squares have four sides of equal length '''

    def __init__(self, size=0):
        ''' Square constructor
        Enables to give parameters such as size

        Args:
            size (int): Size of the square '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        ''' return the area of the square '''
        return self.__size * self.__size
