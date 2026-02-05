#!/usr/bin/python3

"""Base Geometry Class"""


class BaseGeometry:
    """BaseGeometry: defines a geometrical shape"""

    def area(self):
        """area: currently not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator: validates a value
        Args:
            name (string): name of the value
            value (integer): value to evaluate"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
