#!/usr/bin/env python3

"""task_00_abc: Animals Module"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Base abstract class"""

    @abstractmethod
    def sound():
        """sound method: not implemented in base class"""
        pass


class Dog(Animal):
    """Dog class, inherited from Animals"""

    def sound(self):
        """Returns Bark as a string"""
        return "Bark"


class Cat(Animal):
    """Cat class, inherited from Animals"""

    def sound(self):
        """Returns Meow as a string"""
        return "Meow"
