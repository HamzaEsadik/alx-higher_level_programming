#!/usr/bin/python3
"""
Square Module python3
from models.rectangle import Rectangle
Rectangle = __import__("rectangle").Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that enhirit from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        args:
            - size: int
            - x: int
            - y: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format:
            "[Square] (<id>) <x>/<y> - <size>"
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.size}"