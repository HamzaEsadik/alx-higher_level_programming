#!/usr/bin/python3
"""class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle class
    """
    def __init__(self, size):
        """
        new instance of Rectangle

        Arguments:
            -size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
