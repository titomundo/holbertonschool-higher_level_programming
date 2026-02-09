#!/usr/bin/env python3

"""task_03_countediterator: CounterIterator Module"""


class CountedIterator:
    """CounterIterator Class: builds a iterator with a iteration counter"""

    def __init__(self, iterable):
        """Constructor method"""
        self.iter = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Override the __next__ method to increase the counter attribute"""
        self.counter += 1

        try:
            return next(self.iter)
        except StopIteration:
            raise StopIteration()

    def get_count(self):
        """Return the counter of the iterator"""
        return self.counter
