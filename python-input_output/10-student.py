#!/usr/bin/python3

"""10-student.py:
Student class with to_json method
"""


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

    def to_json(self, attrs=None):
        """Returns dictionary with class attributes
        Args:
            attrs (list): List of attributes to retrieve

        if no no list is give, all attributes are retrieved
        """

        student = self.__dict__

        if attrs is None:
            return student

        dic = {}
        for key in student:
            if key in attrs:
                dic[key] = student.get(key)

        return dic
