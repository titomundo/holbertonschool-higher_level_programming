#!/usr/bin/env python3

"""task_00_abc: Animals Module"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Base abstract class"""

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Circle(Shape):
    """Circle class, inherited from Shape"""

    def __init__(self, radius):
        """Circle constructor"""
        self.radius = radius

    def area(self):
        """Returns the area of a circle shape"""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of a circle shape"""
        return pi * self.radius * 2


class Rectangle(Shape):
    """Rectangle class, inherited from Shape"""

    def __init__(self, height=0, width=0):
        """Rectangle constructor"""
        self.height = height
        self.width = width

    def area(self):
        """Returns the area of a rectangle shape"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle shape"""
        return (self.width * 2) + (self.height * 2)


def shape_info(shape):
    """shape_info: returns the dimensions of a shape instance
    Args:
        shape (Shape): shape instance to inspect"""

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
