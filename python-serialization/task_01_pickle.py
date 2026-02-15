#!/usr/bin/python3

"""01_pickle:
Serialize and deserialize objects in python using the pickle module
"""

from pickle import PicklingError, UnpicklingError, dump, load


class CustomObject:
    """CustomObject class:
    Simple custom class to showcase how to
    serialize and deserialize python objects

    Attributes:
        name (string): name of the object
        age (int): age of the object
        is_student (boolean): determines if the object is a student
    """

    def __init__(self, name="", age=0, is_student=False):
        """CustomObject class constructor

        Args:
            name (string): name of the object
            age (int): age of the object
            is_student (boolean): determines if the object is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """converts the object instance to a byte instance using pickle

        Args:
            filename (string): file to write object data into
        """
        try:
            with open(filename, mode="wb") as f:
                dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """constructs an object instance from a byte instance using pickle

        Args:
            filename (string): file to read object data from

        Returns: CustomObject instance
        """
        try:
            with open(filename, mode="rb") as f:
                my_obj = load(f)

                if isinstance(my_obj, cls):
                    return my_obj

                return None

        except Exception:
            return None

    def display(self):
        """displays data from the object in a simple format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
