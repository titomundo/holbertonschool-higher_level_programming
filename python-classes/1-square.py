#!/usr/bin/python3

''' Demo Square class module '''


class Square:
    ''' Square Class
    Squares have four sides of equal length '''

    def __init__(self, size):
        ''' Square constructor
        Enables to give parameters such as size

        Args:
            size (int): Size of the square
        '''
        self._size = size
