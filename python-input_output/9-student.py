#!/usr/bin/python3

"""9-student: Student class Module"""


class Student:
    """Student: They are the future

    Attributes:
        first_name (str): name of the student
        last_name (str): last name of the student
        age (int): age of the student in years
    """

    def __init__(self, first_name, last_name, age):
        """Student constructor:
        Args:
            first_name (str): name of the student
            last_name (str): last name of the student
            age (int): age of the student in years
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary with class attributes"""
        return self.__dict__
