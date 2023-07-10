#!/usr/bin/python3
"""Main"""


class BaseGeometry:
    """Doc"""
    def area(self):
        """Doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
