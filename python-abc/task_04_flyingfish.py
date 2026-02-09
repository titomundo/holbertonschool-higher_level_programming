#!/usr/bin/python3

"""
task_04_flyingfish: FlyingFish Module
"""


class Fish:
    """
    Fish class: Fishes live in the sea
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Bird class: Birds fly high
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish Class: the best of both worlds
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
