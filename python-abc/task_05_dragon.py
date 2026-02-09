#!/usr/bin/python3

"""
task_05_dragon: Ryujin no ken wo kurae!
"""


class SwimMixin:
    """
    SwimMixin class
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin class
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class: Ryujin no ken wo kurae!
    """

    def roar(self):
        print("The dragon roars!")
