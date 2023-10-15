#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def __init__(self):
        """new instance of BaseGeometry"""
        pass

    def area(self):
        """Public instance method that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
