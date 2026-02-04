#!/usr/bin/python3

"""1-my_list: MyList subclass from list"""


class MyList(list):
    """MyList class, inherits list"""

    def print_sorted(self):
        """print_sorted: returns the list in ascending order"""
        s = sorted(self)
        print(s)
